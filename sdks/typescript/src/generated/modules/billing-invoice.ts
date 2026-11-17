import { encodePathParam } from '../../core/path'
import type { ConjoinCallOptions, ConjoinClient } from '../../core/types'
import type { operations } from '../api-types'

type ListData = NonNullable<operations['listInvoices']['responses']['200']['content']['application/json']['data']>[number]
type ListQuery = NonNullable<operations['listInvoices']['parameters']['query']>
type CreateBody = NonNullable<operations['createInvoice']['requestBody']>['content']['application/json']
type CreateData = NonNullable<operations['createInvoice']['responses']['201']['content']['application/json']['data']>
type ListCountData = NonNullable<operations['listInvoicesCount']['responses']['200']['content']['application/json']['data']>
type ListCountQuery = NonNullable<operations['listInvoicesCount']['parameters']['query']>
type UpdateBody = NonNullable<operations['updateInvoice']['requestBody']>['content']['application/json']
type UpdateData = NonNullable<operations['updateInvoice']['responses']['200']['content']['application/json']['data']>
type FinalizeData = NonNullable<operations['finalizeInvoice']['responses']['200']['content']['application/json']['data']>
type PayBody = NonNullable<operations['payInvoice']['requestBody']>['content']['application/json']
type PayData = NonNullable<operations['payInvoice']['responses']['200']['content']['application/json']['data']>
type VoidData = NonNullable<operations['voidInvoice']['responses']['200']['content']['application/json']['data']>
type PayOutOfBandBody = NonNullable<operations['payInvoiceOutOfBand']['requestBody']>['content']['application/json']
type PayOutOfBandData = NonNullable<operations['payInvoiceOutOfBand']['responses']['200']['content']['application/json']['data']>
type SendData = NonNullable<operations['sendInvoice']['responses']['200']['content']['application/json']['data']>
type ExportPdfData = NonNullable<operations['exportInvoicePdf']['responses']['200']['content']['application/json']['data']>

export function createBillingInvoices(client: ConjoinClient) {
  return {
    list: (query?: ListQuery, options?: ConjoinCallOptions) =>
      client.fetchList<ListData>('billing/invoices/', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),

    create: (data: CreateBody, options?: ConjoinCallOptions) =>
      client.fetch<CreateData>('billing/invoices/', { ...options, method: 'POST', body: data, scopes: ['billingEntityId'], acceptsIdempotencyKey: true }),

    listCount: (query?: ListCountQuery, options?: ConjoinCallOptions) =>
      client.fetch<ListCountData>('billing/invoices/count', { ...options, method: 'GET', query: query as Record<string, unknown> | undefined, scopes: ['billingEntityId'] }),

    update: (invoiceId: string, data: UpdateBody, options?: ConjoinCallOptions) =>
      client.fetch<UpdateData>(`billing/invoices/${encodePathParam(invoiceId)}`, { ...options, method: 'PATCH', body: data, scopes: ['billingEntityId'] }),

    finalize: (invoiceId: string, options?: ConjoinCallOptions) =>
      client.fetch<FinalizeData>(`billing/invoices/${encodePathParam(invoiceId)}/finalize`, { ...options, method: 'POST', scopes: ['billingEntityId'], acceptsIdempotencyKey: true }),

    pay: (invoiceId: string, data: PayBody, options?: ConjoinCallOptions) =>
      client.fetch<PayData>(`billing/invoices/${encodePathParam(invoiceId)}/pay`, { ...options, method: 'POST', body: data, scopes: ['billingEntityId'], acceptsIdempotencyKey: true }),

    void: (invoiceId: string, options?: ConjoinCallOptions) =>
      client.fetch<VoidData>(`billing/invoices/${encodePathParam(invoiceId)}/void`, { ...options, method: 'POST', scopes: ['billingEntityId'], acceptsIdempotencyKey: true }),

    payOutOfBand: (invoiceId: string, data: PayOutOfBandBody, options?: ConjoinCallOptions) =>
      client.fetch<PayOutOfBandData>(`billing/invoices/${encodePathParam(invoiceId)}/pay-out-of-band`, { ...options, method: 'POST', body: data, scopes: ['billingEntityId'], acceptsIdempotencyKey: true }),

    send: (invoiceId: string, options?: ConjoinCallOptions) =>
      client.fetch<SendData>(`billing/invoices/${encodePathParam(invoiceId)}/send`, { ...options, method: 'POST', scopes: ['billingEntityId'], acceptsIdempotencyKey: true }),

    exportPdf: (invoiceId: string, options?: ConjoinCallOptions) =>
      client.fetch<ExportPdfData>(`billing/invoices/${encodePathParam(invoiceId)}/export`, { ...options, method: 'POST', scopes: ['billingEntityId'], acceptsIdempotencyKey: true }),
  }
}
