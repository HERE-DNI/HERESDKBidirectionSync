---
title: "AuthenticationMode Class Reference"
slug: "sdk-for-ios-explore-classes-authenticationmode"
---

# AuthenticationMode

<div class="declaration">

<div class="language">

``` highlight
public class AuthenticationMode
```

``` highlight
extension AuthenticationMode: NativeBase
```

``` highlight
extension AuthenticationMode: Hashable
```

</div>

</div>

This is a bearer authentication mode which adds or does not add a header (“Authorization”, “Bearer \$Token”) to each online request of the module the object is added to. The token (if used) can be provided or is retrieved via key/secret from a dedicated backend.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18AuthenticationModeC19AccessTokenProvidera"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Alias-AccessTokenProvider" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-authenticationmode#sdk-for-ios-explore-s-7heresdk18AuthenticationModeC19AccessTokenProvidera" class="token"><code>AccessTokenProvider</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This lambda is used to retrieve access token in synchronous manner. It returns the access token or null if it is not set. The lambda is called each time the access token is needed and it is executed on the main thread of the application.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias AccessTokenProvider = () -> String?
  ```

  </div>

  </div>

  <div>

  #### Return Value

  Access token in case it is set or null otherwise.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18AuthenticationModeC9withToken06accessE0ACSS_tFZ"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-withToken-accessToken" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-authenticationmode#sdk-for-ios-explore-s-7heresdk18AuthenticationModeC9withToken06accessE0ACSS_tFZ" class="token"><code>withToken(accessToken:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  SDK will pass access token as a Bearer.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func withToken(accessToken: String) -> AuthenticationMode
  ```

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>accessToken</code></em><code> </code></td>
  <td><div>
  <p>Access token</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Instance of `AuthenticationMode` configured to use token

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18AuthenticationModeC17withTokenProvider05tokenF0ACSSSgyc_tFZ"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-withTokenProvider-tokenProvider" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-authenticationmode#sdk-for-ios-explore-s-7heresdk18AuthenticationModeC17withTokenProvider05tokenF0ACSSSgyc_tFZ" class="token"><code>withTokenProvider(tokenProvider:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  SDK will use access token provider to retrieve access token.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func withTokenProvider(tokenProvider: @escaping AuthenticationMode.AccessTokenProvider) -> AuthenticationMode
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-authenticationmode#sdk-for-ios-explore-s-7heresdk18AuthenticationModeC19AccessTokenProvidera">AccessTokenProvider</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>tokenProvider</code></em><code> </code></td>
  <td><div>
  <p>Access token provider</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Instance of `AuthenticationMode` configured to use token provider

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18AuthenticationModeC12withExternalACyFZ"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-withExternal" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-authenticationmode#sdk-for-ios-explore-s-7heresdk18AuthenticationModeC12withExternalACyFZ" class="token"><code>withExternal()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Assumes the authentication is provided by the client.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func withExternal() -> AuthenticationMode
  ```

  </div>

  </div>

  <div>

  #### Return Value

  Instance of `AuthenticationMode` configured to use externally provided authentication

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18AuthenticationModeC13withKeySecret06accessE2Id0geF0ACSS_SStFZ"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-withKeySecret-accessKeyId-accessKeySecret" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-authenticationmode#sdk-for-ios-explore-s-7heresdk18AuthenticationModeC13withKeySecret06accessE2Id0geF0ACSS_SStFZ" class="token"><code>withKeySecret(accessKeyId:</code><wbr></wbr><code>accessKeySecret:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  SDK will authenticate with access key id access key secret to obtain authentication token.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func withKeySecret(accessKeyId: String, accessKeySecret: String) -> AuthenticationMode
  ```

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>accessKeyId</code></em><code> </code></td>
  <td><div>
  <p>The access key id</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>accessKeySecret</code></em><code> </code></td>
  <td><div>
  <p>The access key secret</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Instance of `AuthenticationMode` configured to use key ID and secret

  </div>

  </div>

  </div>

</div>

</div>

</div>

<div id="sdk-for-ios-explore-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

