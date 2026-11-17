# @conjoin-cloud/expo

`@conjoin-cloud/expo` gives you React Native bindings for [Conjoin](https://conjoin.delalify.com). You get a native `ConjoinProvider` and the auth and data hooks re-exported from the headless core. The provider stores the refresh token in the device keychain through `expo-secure-store` and keeps the access token in memory only. The package ships no DOM or web code, so it works on iOS and Android.

[![npm version](https://img.shields.io/npm/v/@conjoin-cloud/expo)](https://www.npmjs.com/package/@conjoin-cloud/expo)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](../../LICENSE)

## Install

Install the package with your package manager:

```bash
npm install @conjoin-cloud/expo
pnpm add @conjoin-cloud/expo
yarn add @conjoin-cloud/expo
```

Install `react` `>=18.0.0` and `expo-secure-store` `>=13.0.2` in your app, and add `expo-crypto` `>=12.2.0` when your JavaScript engine has no `crypto.subtle`. Sign-in uses them to keep the session and to create the PKCE proof for every sign-in, and the provider loads them on demand and throws an error that tells you which one is missing. Add both with `npx expo install expo-secure-store expo-crypto`.

## Quick Start

```tsx
import { ConjoinProvider, useAccount, useAuth } from '@conjoin-cloud/expo'
import { Text } from 'react-native'

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
    return <Text>Loading...</Text>
  }

  if (!isSignedIn) {
    return <Text>Sign in to continue</Text>
  }

  return <Text>Hello, {account?.name}</Text>
}
```

`ConjoinProvider` accepts `publishableKey` and `config`. The hooks include `useAuth`, `useSignIn`, `useSignUp`, `useSession`, `useSessions`, `useAccount`, `useUpdateAccount`, `useOrg`, `useEntitlements`, `useCheckout`, `useBundles`, `useChannel`, `useStorageUpload`, and `useConjoinStatus`, and the `@conjoin-cloud/react-core` README describes each of them. `useSignIn` and `useSignUp` use the native sign-in calls, so the provider exchanges the finished sign-in for tokens and renews them with the refresh token.

## License

This package uses the [MIT](../../LICENSE) license.
