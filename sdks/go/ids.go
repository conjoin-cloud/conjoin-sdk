package conjoin

import (
	"crypto/rand"
	"encoding/hex"
	"regexp"
	"sync"
	"time"
)

const requestIDPrefix = "cnj_req_"

var (
	requestIDPattern      = regexp.MustCompile(`^cnj_req_[0-9a-f]{8}-[0-9a-f]{4}-7[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$`)
	idempotencyKeyPattern = regexp.MustCompile(`^[A-Za-z0-9\-_:.]{1,64}$`)
)

type uuidV7Clock struct {
	mu       sync.Mutex
	unixMsec int64
	sequence uint32
}

var requestIDClock uuidV7Clock

func (c *uuidV7Clock) next(now int64, random []byte) (int64, uint32) {
	c.mu.Lock()
	defer c.mu.Unlock()

	if now > c.unixMsec {
		c.unixMsec = now
		c.sequence = uint32(random[6])<<23 | uint32(random[7])<<16 | uint32(random[8])<<8 | uint32(random[9])
		return c.unixMsec, c.sequence
	}

	c.sequence++
	if c.sequence == 0 {
		c.unixMsec++
	}
	return c.unixMsec, c.sequence
}

func formatUUID(b [16]byte) string {
	var out [36]byte
	hex.Encode(out[0:8], b[0:4])
	out[8] = '-'
	hex.Encode(out[9:13], b[4:6])
	out[13] = '-'
	hex.Encode(out[14:18], b[6:8])
	out[18] = '-'
	hex.Encode(out[19:23], b[8:10])
	out[23] = '-'
	hex.Encode(out[24:36], b[10:16])
	return string(out[:])
}

func newRequestID() string {
	var random [16]byte
	rand.Read(random[:])
	msec, seq := requestIDClock.next(time.Now().UnixMilli(), random[:])

	var b [16]byte
	b[0] = byte(msec >> 40)
	b[1] = byte(msec >> 32)
	b[2] = byte(msec >> 24)
	b[3] = byte(msec >> 16)
	b[4] = byte(msec >> 8)
	b[5] = byte(msec)
	b[6] = 0x70 | byte(seq>>28)&0x0f
	b[7] = byte(seq >> 20)
	b[8] = 0x80 | byte(seq>>14)&0x3f
	b[9] = byte(seq >> 6)
	b[10] = byte(seq<<2) | random[10]&0x03
	copy(b[11:], random[11:16])

	return requestIDPrefix + formatUUID(b)
}

func isValidRequestID(value string) bool {
	return requestIDPattern.MatchString(value)
}

func newIdempotencyKey() string {
	var b [16]byte
	rand.Read(b[:])
	b[6] = b[6]&0x0f | 0x40
	b[8] = b[8]&0x3f | 0x80
	return formatUUID(b)
}

func validateIdempotencyKey(key string) error {
	if !idempotencyKeyPattern.MatchString(key) {
		return configurationError("the idempotency key must be 1 to 64 characters of letters, digits, hyphens, underscores, colons, and dots")
	}
	return nil
}
