# @conjoin-cloud/react-core

`@conjoin-cloud/react-core` gives you headless React bindings for [Conjoin](https://conjoin.delalify.com). You get the auth and data hooks, a framework-agnostic provider primitive, and an SSR-safe web provider, theme, and transport. The package ships no UI components, so you bring your own.

The package ships ESM and CJS builds with two entry points. Import the root for the agnostic provider and hooks. Import `@conjoin-cloud/react-core/web` for the web provider, theme, and `useConjoinTheme`.

[![npm version](https://img.shields.io/npm/v/@conjoin-cloud/react-core)](https://www.npmjs.com/package/@conjoin-cloud/react-core)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](../../LICENSE)

## Install

Install the package with your package manager:

```bash
npm install @conjoin-cloud/react-core
pnpm add @conjoin-cloud/react-core
yarn add @conjoin-cloud/react-core
```

Install peer dependencies for the entry points you import:

- Install `react` `>=18.0.0` for the root entry.
- Install `react-dom` `>=18.0.0` when you import `@conjoin-cloud/react-core/web`.

## Entry Points

- Import `@conjoin-cloud/react-core` for `ConjoinProviderCore`, the auth and data hooks, `useConjoinClient`, and the shared provider types. This entry needs `react` only and touches no DOM, so it works in any React renderer.
- Import `@conjoin-cloud/react-core/web` for `ConjoinProvider`, `useConjoinTheme`, and the `ConjoinThemeState` type. This entry is SSR-safe and reads the DOM only inside browser guards.

## Web Quick Start

```tsx
import { ConjoinProvider } from '@conjoin-cloud/react-core/web'
import { useAccount, useAuth } from '@conjoin-cloud/react-core'

function App() {
  return (
    <ConjoinProvider publishableKey="cpk_live_...">
      <Profile />
    </ConjoinProvider>
  )
}

function Profile() {
  const { isLoaded, isSignedIn } = useAuth()
  const { account } = useAccount()

  if (!isLoaded) {
    return <div>Loading...</div>
  }

  if (!isSignedIn) {
    return <a href="/sign-in">Sign in</a>
  }

  return <div>Hello, {account?.name}</div>
}
```

`ConjoinProvider` accepts `publishableKey`, `config`, and `appearance`. It reads your project's SDK settings with the publishable key, and it calls the auth domain from those settings for sign-in and for the signed-in account. On the web, the session lives in the auth domain's cookies, and the provider renews it before it expires. The hooks include `useAuth`, `useSignIn`, `useSignUp`, `useSession`, `useSessions`, `useAccount`, `useUpdateAccount`, `useOrg`, `useEntitlements`, `useCheckout`, `useBundles`, `usePaymentMethods`, `useChannel`, `useStorageUpload`, `useConjoinStatus`, and `useConjoinTheme`.

The billing hooks call the auth domain with the signed-in session and the billing entity that you pass, so a page needs only its publishable key. A checkout charges a card that the signed-in customer saved: `useCheckout().startCardSetup` returns the `authorisation_url` where the customer authorises the card, `usePaymentMethods` lists the saved cards, and `useCheckout().activate` takes the `paymentMethodId` of an authorised one. The activation it returns stays `pending_payment` until the charge succeeds, and `useEntitlements` grants nothing from it before then.

## Sign In

`useSignIn` and `useSignUp` each return `start`, `complete`, `startRedirect`, `completeRedirect`, and `reset`. Every step returns the server's `status`, and the hook signs the user in once a step returns `complete`:

```tsx
const signIn = useSignIn()

const result = await signIn.start({ email, password })

if (result.status === 'mfa_required') {
  await signIn.complete({ verification_result: {}, mfa: { method: 'totp', totp_code: code } })
}
```

A `verification_required` status asks for a code, which you send with `complete({ verification_result: { pin_code } })`. For OAuth, call `startRedirect({ provider_key, verification_option: 'oauth_token' })` and send the browser to the `redirect_url` that it returns. When the provider sends the user back, pass the `code` and `state` from the callback URL to `completeRedirect`. The hook keeps the pending sign-in for ten minutes, and it rejects a callback whose `state` doesn't match one that this app started.

## Organizations and Roles

`useOrg` returns the active `organizationId`, its `organizationRoles`, the account's `memberships`, and `switchOrganization(organizationId)`, which takes `null` to clear the active organization. `useAuth().has({ role })` checks the active organization's roles.

## Realtime Channels

`useChannel` connects to the project's relay and subscribes to one channel:

```tsx
const { status, events, publish } = useChannel({
  channel: 'support:room-42',
  getConnectionToken: () => fetchConnectionTokenFromYourServer(),
})
```

`getConnectionToken` is required, and it returns the token that the relay checks when the socket connects. Pass `authToken` for a channel that needs a separate token, and `maxEvents` to cap how many events the hook keeps. The default is 200.

## Custom Transports

`ConjoinProviderCore` takes a `transport` prop, so you can use the provider in a renderer without DOM access. Pass an object that satisfies the `AuthTransport` type to control how the session is kept, renewed, and ended, and which credentials each call sends.

## License

This package uses the [MIT](../../LICENSE) license.
