---
title: "EVSearchError Enumeration Reference"
slug: "sdk-for-ios-navigate-enums-evsearcherror"
---

# EVSearchError

<div class="declaration">

<div class="language">

``` highlight
public enum EVSearchError : UInt32, CaseIterable, Codable
```

</div>

</div>

Specifies possible errors that <a href="sdk-for-ios-navigate-classes-evsearchengine">`EVSearchEngine`</a> may report. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk13EVSearchErrorO8emptyIdsyA2CmF"></span>` `<span id="//apple_ref/swift/Element/emptyIds" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-enums-evsearcherror#/s:7heresdk13EVSearchErrorO8emptyIdsyA2CmF" class="token"><code>emptyIds</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Empty list of IDs passed.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case emptyIds
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13EVSearchErrorO9invalidIdyA2CmF"></span>` `<span id="//apple_ref/swift/Element/invalidId" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-enums-evsearcherror#/s:7heresdk13EVSearchErrorO9invalidIdyA2CmF" class="token"><code>invalidId</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  At least one empty or invalid ID passed.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case invalidId
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13EVSearchErrorO10badRequestyA2CmF"></span>` `<span id="//apple_ref/swift/Element/badRequest" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-enums-evsearcherror#/s:7heresdk13EVSearchErrorO10badRequestyA2CmF" class="token"><code>badRequest</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Something wrong or missing in the request.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case badRequest
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13EVSearchErrorO07parsingC0yA2CmF"></span>` `<span id="//apple_ref/swift/Element/parsingError" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-enums-evsearcherror#/s:7heresdk13EVSearchErrorO07parsingC0yA2CmF" class="token"><code>parsingError</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  EVCP3 backend returns result with unexpected json schema.

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

  ` `<span id="/s:7heresdk13EVSearchErrorO08internalC0yA2CmF"></span>` `<span id="//apple_ref/swift/Element/internalError" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-enums-evsearcherror#/s:7heresdk13EVSearchErrorO08internalC0yA2CmF" class="token"><code>internalError</code></a>` `

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

  ` `<span id="/s:7heresdk13EVSearchErrorO17serverUnreachableyA2CmF"></span>` `<span id="//apple_ref/swift/Element/serverUnreachable" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-enums-evsearcherror#/s:7heresdk13EVSearchErrorO17serverUnreachableyA2CmF" class="token"><code>serverUnreachable</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  EVCP3 server is unreachable.

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

  ` `<span id="/s:7heresdk13EVSearchErrorO04httpC0yA2CmF"></span>` `<span id="//apple_ref/swift/Element/httpError" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-enums-evsearcherror#/s:7heresdk13EVSearchErrorO04httpC0yA2CmF" class="token"><code>httpError</code></a>` `

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

  ` `<span id="/s:7heresdk13EVSearchErrorO20authenticationFailedyA2CmF"></span>` `<span id="//apple_ref/swift/Element/authenticationFailed" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-enums-evsearcherror#/s:7heresdk13EVSearchErrorO20authenticationFailedyA2CmF" class="token"><code>authenticationFailed</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  EVCP3 operation is not authenticated. Check your credentials.

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

  ` `<span id="/s:7heresdk13EVSearchErrorO18exceededUsageLimityA2CmF"></span>` `<span id="//apple_ref/swift/Element/exceededUsageLimit" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-enums-evsearcherror#/s:7heresdk13EVSearchErrorO18exceededUsageLimityA2CmF" class="token"><code>exceededUsageLimit</code></a>` `

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

  ` `<span id="/s:7heresdk13EVSearchErrorO8timedOutyA2CmF"></span>` `<span id="//apple_ref/swift/Element/timedOut" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-enums-evsearcherror#/s:7heresdk13EVSearchErrorO8timedOutyA2CmF" class="token"><code>timedOut</code></a>` `

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

  ` `<span id="/s:7heresdk13EVSearchErrorO7offlineyA2CmF"></span>` `<span id="//apple_ref/swift/Element/offline" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-enums-evsearcherror#/s:7heresdk13EVSearchErrorO7offlineyA2CmF" class="token"><code>offline</code></a>` `

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

  ` `<span id="/s:7heresdk13EVSearchErrorO18operationCancelledyA2CmF"></span>` `<span id="//apple_ref/swift/Element/operationCancelled" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-enums-evsearcherror#/s:7heresdk13EVSearchErrorO18operationCancelledyA2CmF" class="token"><code>operationCancelled</code></a>` `

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

  ` `<span id="/s:7heresdk13EVSearchErrorO25proxyAuthenticationFailedyA2CmF"></span>` `<span id="//apple_ref/swift/Element/proxyAuthenticationFailed" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-enums-evsearcherror#/s:7heresdk13EVSearchErrorO25proxyAuthenticationFailedyA2CmF" class="token"><code>proxyAuthenticationFailed</code></a>` `

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

  ` `<span id="/s:7heresdk13EVSearchErrorO22proxyServerUnreachableyA2CmF"></span>` `<span id="//apple_ref/swift/Element/proxyServerUnreachable" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-enums-evsearcherror#/s:7heresdk13EVSearchErrorO22proxyServerUnreachableyA2CmF" class="token"><code>proxyServerUnreachable</code></a>` `

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

  ` `<span id="/s:7heresdk13EVSearchErrorO14noResultsFoundyA2CmF"></span>` `<span id="//apple_ref/swift/Element/noResultsFound" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-enums-evsearcherror#/s:7heresdk13EVSearchErrorO14noResultsFoundyA2CmF" class="token"><code>noResultsFound</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  No results found.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case noResultsFound
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk13EVSearchErrorO15operationFailedyA2CmF"></span>` `<span id="//apple_ref/swift/Element/operationFailed" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-enums-evsearcherror#/s:7heresdk13EVSearchErrorO15operationFailedyA2CmF" class="token"><code>operationFailed</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Search operation failed due to some reason.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case operationFailed
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

