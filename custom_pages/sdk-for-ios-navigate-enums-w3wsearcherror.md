---
title: "W3WSearchError Enumeration Reference"
slug: "sdk-for-ios-navigate-enums-w3wsearcherror"
---

# W3WSearchError

<div class="declaration">

<div class="language">

``` highlight
public enum W3WSearchError : UInt32, CaseIterable, Codable
```

</div>

</div>

Specifies possible errors that may result from a w3w search query.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14W3WSearchErrorO8badWordsyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-badWords" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-w3wsearcherror#sdk-for-ios-navigate-s-7heresdk14W3WSearchErrorO8badWordsyA2CmF" class="token"><code>badWords</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Invalid or non-existent 3 word address.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case badWords
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14W3WSearchErrorO11badLanguageyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-badLanguage" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-w3wsearcherror#sdk-for-ios-navigate-s-7heresdk14W3WSearchErrorO11badLanguageyA2CmF" class="token"><code>badLanguage</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Bad parameter `language`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case badLanguage
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14W3WSearchErrorO12missingWordsyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-missingWords" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-w3wsearcherror#sdk-for-ios-navigate-s-7heresdk14W3WSearchErrorO12missingWordsyA2CmF" class="token"><code>missingWords</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Missing parameter: a required words parameter was missing.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case missingWords
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14W3WSearchErrorO07parsingD0yA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-parsingError" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-w3wsearcherror#sdk-for-ios-navigate-s-7heresdk14W3WSearchErrorO07parsingD0yA2CmF" class="token"><code>parsingError</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  W3W backend return result with unexpected json schema. This is not expected to happen. Try updating to the newest version of the SDK. If the problem persists, please report a bug in the SDK.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case parsingError
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14W3WSearchErrorO08internalD0yA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-internalError" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-w3wsearcherror#sdk-for-ios-navigate-s-7heresdk14W3WSearchErrorO08internalD0yA2CmF" class="token"><code>internalError</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Generic internal error.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case internalError
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14W3WSearchErrorO17serverUnreachableyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-serverUnreachable" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-w3wsearcherror#sdk-for-ios-navigate-s-7heresdk14W3WSearchErrorO17serverUnreachableyA2CmF" class="token"><code>serverUnreachable</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  What3Words server is unreachable.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case serverUnreachable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14W3WSearchErrorO04httpD0yA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-httpError" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-w3wsearcherror#sdk-for-ios-navigate-s-7heresdk14W3WSearchErrorO04httpD0yA2CmF" class="token"><code>httpError</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A general network request error.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case httpError
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14W3WSearchErrorO20authenticationFailedyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-authenticationFailed" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-w3wsearcherror#sdk-for-ios-navigate-s-7heresdk14W3WSearchErrorO20authenticationFailedyA2CmF" class="token"><code>authenticationFailed</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  What3Words operation is not authenticated. Check your credentials.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case authenticationFailed
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14W3WSearchErrorO18exceededUsageLimityA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-exceededUsageLimit" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-w3wsearcherror#sdk-for-ios-navigate-s-7heresdk14W3WSearchErrorO18exceededUsageLimityA2CmF" class="token"><code>exceededUsageLimit</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Credentials exceeded the allowed requests limit.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case exceededUsageLimit
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14W3WSearchErrorO8timedOutyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-timedOut" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-w3wsearcherror#sdk-for-ios-navigate-s-7heresdk14W3WSearchErrorO8timedOutyA2CmF" class="token"><code>timedOut</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The request timed out.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case timedOut
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14W3WSearchErrorO7offlineyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-offline" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-w3wsearcherror#sdk-for-ios-navigate-s-7heresdk14W3WSearchErrorO7offlineyA2CmF" class="token"><code>offline</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The device has no internet connection.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case offline
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14W3WSearchErrorO18operationCancelledyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-operationCancelled" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-w3wsearcherror#sdk-for-ios-navigate-s-7heresdk14W3WSearchErrorO18operationCancelledyA2CmF" class="token"><code>operationCancelled</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The request was cancelled (usually by the user).

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case operationCancelled
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14W3WSearchErrorO25proxyAuthenticationFailedyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-proxyAuthenticationFailed" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-w3wsearcherror#sdk-for-ios-navigate-s-7heresdk14W3WSearchErrorO25proxyAuthenticationFailedyA2CmF" class="token"><code>proxyAuthenticationFailed</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Proxy is not authenticated. Check your proxy credentials.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case proxyAuthenticationFailed
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14W3WSearchErrorO22proxyServerUnreachableyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-proxyServerUnreachable" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-w3wsearcherror#sdk-for-ios-navigate-s-7heresdk14W3WSearchErrorO22proxyServerUnreachableyA2CmF" class="token"><code>proxyServerUnreachable</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Proxy server unreachable.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case proxyServerUnreachable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14W3WSearchErrorO7unknownyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-unknown" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-w3wsearcherror#sdk-for-ios-navigate-s-7heresdk14W3WSearchErrorO7unknownyA2CmF" class="token"><code>unknown</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Unknown error, that was not introduced by HERE SDK, but exists on W3W backend.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case unknown
  ```

  </div>

  </div>

  </div>

  </div>

</div>

</div>

</div>

<div id="sdk-for-ios-navigate-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

