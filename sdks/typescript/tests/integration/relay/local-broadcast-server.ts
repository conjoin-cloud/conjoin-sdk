import { createHash } from 'node:crypto'
import { createServer } from 'node:http'
import type { Duplex } from 'node:stream'

export async function startBroadcastServer() {
  const frames: Record<string, unknown>[] = []
  const sockets = new Set<Duplex>()
  let connections = 0
  const server = createServer()
  const write = (socket: Duplex, frame: Record<string, unknown>) => {
    const payload = Buffer.from(JSON.stringify(frame))
    const header = payload.length < 126 ? Buffer.from([0x81, payload.length]) : Buffer.from([0x81, 126, 0, 0])
    if (payload.length >= 126) header.writeUInt16BE(payload.length, 2)
    socket.write(Buffer.concat([header, payload]))
  }
  server.on('upgrade', (request, socket) => {
    const key = request.headers['sec-websocket-key']
    if (typeof key !== 'string') return socket.destroy()
    connections++
    sockets.add(socket)
    socket.on('close', () => sockets.delete(socket))
    socket.on('error', () => socket.destroy())
    const accept = createHash('sha1').update(`${key}258EAFA5-E914-47DA-95CA-C5AB0DC85B11`).digest('base64')
    socket.write(
      `HTTP/1.1 101 Switching Protocols\r\nUpgrade: websocket\r\nConnection: Upgrade\r\nSec-WebSocket-Accept: ${accept}\r\n\r\n`,
    )
    let buffered = Buffer.alloc(0)
    socket.on('data', chunk => {
      buffered = Buffer.concat([buffered, chunk])
      while (buffered.length >= 2) {
        const opcode = buffered[0] ?? 0
        const lengthByte = buffered[1] ?? 0
        let length = lengthByte & 127
        let offset = 2
        if (length === 126) {
          if (buffered.length < 4) return
          length = buffered.readUInt16BE(2)
          offset = 4
        }
        if (length === 127) return socket.destroy()
        const masked = (lengthByte & 128) !== 0
        const start = offset + (masked ? 4 : 0)
        if (buffered.length < start + length) return
        const payload = Buffer.from(buffered.subarray(start, start + length))
        if (masked) {
          for (let index = 0; index < length; index++)
            payload[index] = (payload[index] ?? 0) ^ (buffered[offset + (index % 4)] ?? 0)
        }
        buffered = buffered.subarray(start + length)
        if ((opcode & 15) === 8) return socket.end(Buffer.from([0x88, 0]))
        const frame = JSON.parse(payload.toString()) as Record<string, unknown>
        frames.push(frame)
        const type = frame.type
        if (type === 'connect') write(socket, { type: 'connected', socket_id: connections })
        if (type === 'subscribe') write(socket, { type: 'subscribed', channel: frame.channel })
        if (type === 'unsubscribe') write(socket, { type: 'unsubscribed', channel: frame.channel })
        if (type === 'publish') write(socket, { type: 'published', channel: frame.channel, event_id: 'event_1' })
        if (type === 'history') write(socket, { type: 'history', channel: frame.channel, events: [] })
      }
    })
  })
  await new Promise<void>(resolve => server.listen(0, '127.0.0.1', resolve))
  const address = server.address()
  if (address === null || typeof address === 'string') throw new Error('No server address')
  return {
    url: `ws://127.0.0.1:${address.port}/v1/relay/broadcast`,
    frames,
    get connections() {
      return connections
    },
    drop: () => {
      for (const socket of sockets) socket.destroy()
    },
    stop: async () => {
      for (const socket of sockets) socket.destroy()
      await new Promise<void>(resolve => server.close(() => resolve()))
    },
  }
}
