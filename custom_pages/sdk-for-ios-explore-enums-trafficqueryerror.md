---
title: "TrafficQueryError Enumeration Reference"
slug: "sdk-for-ios-explore-enums-trafficqueryerror"
---

# TrafficQueryError

<div class="declaration">

<div class="language">

``` highlight
public enum TrafficQueryError : UInt32, CaseIterable, Codable
```

</div>

</div>

Represents various errors that could occur from a traffic queries.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk17TrafficQueryErrorO22failedToRetrieveResultyA2CmF"></span>` `<span id="//apple_ref/swift/Element/failedToRetrieveResult" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-enums-trafficqueryerror#/s:7heresdk17TrafficQueryErrorO22failedToRetrieveResultyA2CmF" class="token"><code>failedToRetrieveResult</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Failed to retrieve result since the server has returned an error or invalid result that couldn’t be processed correctly.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case failedToRetrieveResult
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17TrafficQueryErrorO20authenticationFailedyA2CmF"></span>` `<span id="//apple_ref/swift/Element/authenticationFailed" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-enums-trafficqueryerror#/s:7heresdk17TrafficQueryErrorO20authenticationFailedyA2CmF" class="token"><code>authenticationFailed</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Incident query/flow operation is not authenticated. Check your credentials.

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

  ` `<span id="/s:7heresdk17TrafficQueryErrorO9forbiddenyA2CmF"></span>` `<span id="//apple_ref/swift/Element/forbidden" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-enums-trafficqueryerror#/s:7heresdk17TrafficQueryErrorO9forbiddenyA2CmF" class="token"><code>forbidden</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The provided credentials don’t give access to the requested resource.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case forbidden
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17TrafficQueryErrorO17serverUnreachableyA2CmF"></span>` `<span id="//apple_ref/swift/Element/serverUnreachable" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-enums-trafficqueryerror#/s:7heresdk17TrafficQueryErrorO17serverUnreachableyA2CmF" class="token"><code>serverUnreachable</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Server unreachable.

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

  ` `<span id="/s:7heresdk17TrafficQueryErrorO8timedOutyA2CmF"></span>` `<span id="//apple_ref/swift/Element/timedOut" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-enums-trafficqueryerror#/s:7heresdk17TrafficQueryErrorO8timedOutyA2CmF" class="token"><code>timedOut</code></a>` `

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

  ` `<span id="/s:7heresdk17TrafficQueryErrorO7offlineyA2CmF"></span>` `<span id="//apple_ref/swift/Element/offline" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-enums-trafficqueryerror#/s:7heresdk17TrafficQueryErrorO7offlineyA2CmF" class="token"><code>offline</code></a>` `

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

  ` `<span id="/s:7heresdk17TrafficQueryErrorO04httpD0yA2CmF"></span>` `<span id="//apple_ref/swift/Element/httpError" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-enums-trafficqueryerror#/s:7heresdk17TrafficQueryErrorO04httpD0yA2CmF" class="token"><code>httpError</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Network request error.

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

  ` `<span id="/s:7heresdk17TrafficQueryErrorO9invalidInyA2CmF"></span>` `<span id="//apple_ref/swift/Element/invalidIn" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-enums-trafficqueryerror#/s:7heresdk17TrafficQueryErrorO9invalidInyA2CmF" class="token"><code>invalidIn</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Invalid “in” parameter: wrong type, missing or invalid “in”.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case invalidIn
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17TrafficQueryErrorO15invalidGeometryyA2CmF"></span>` `<span id="//apple_ref/swift/Element/invalidGeometry" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-enums-trafficqueryerror#/s:7heresdk17TrafficQueryErrorO15invalidGeometryyA2CmF" class="token"><code>invalidGeometry</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Invalid geometry: bounding box, circle, or corridor.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case invalidGeometry
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17TrafficQueryErrorO15invalidIncidentyA2CmF"></span>` `<span id="//apple_ref/swift/Element/invalidIncident" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-enums-trafficqueryerror#/s:7heresdk17TrafficQueryErrorO15invalidIncidentyA2CmF" class="token"><code>invalidIncident</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Invalid incident ID, type, earliestStartTime or latestEndTime.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case invalidIncident
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17TrafficQueryErrorO18incidentIdNotFoundyA2CmF"></span>` `<span id="//apple_ref/swift/Element/incidentIdNotFound" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-enums-trafficqueryerror#/s:7heresdk17TrafficQueryErrorO18incidentIdNotFoundyA2CmF" class="token"><code>incidentIdNotFound</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Incident ID is not found in the system.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case incidentIdNotFound
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17TrafficQueryErrorO20invalidFilterOptionsyA2CmF"></span>` `<span id="//apple_ref/swift/Element/invalidFilterOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-enums-trafficqueryerror#/s:7heresdk17TrafficQueryErrorO20invalidFilterOptionsyA2CmF" class="token"><code>invalidFilterOptions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  One or several filter options are invalid.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case invalidFilterOptions
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17TrafficQueryErrorO16invalidParameteryA2CmF"></span>` `<span id="//apple_ref/swift/Element/invalidParameter" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-enums-trafficqueryerror#/s:7heresdk17TrafficQueryErrorO16invalidParameteryA2CmF" class="token"><code>invalidParameter</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  One or more input parameters in the query is not valid.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case invalidParameter
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk17TrafficQueryErrorO08internalD0yA2CmF"></span>` `<span id="//apple_ref/swift/Element/internalError" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-enums-trafficqueryerror#/s:7heresdk17TrafficQueryErrorO08internalD0yA2CmF" class="token"><code>internalError</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Internal error.

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

  ` `<span id="/s:7heresdk17TrafficQueryErrorO18operationCancelledyA2CmF"></span>` `<span id="//apple_ref/swift/Element/operationCancelled" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-enums-trafficqueryerror#/s:7heresdk17TrafficQueryErrorO18operationCancelledyA2CmF" class="token"><code>operationCancelled</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Operation cancelled.

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

  ` `<span id="/s:7heresdk17TrafficQueryErrorO25proxyAuthenticationFailedyA2CmF"></span>` `<span id="//apple_ref/swift/Element/proxyAuthenticationFailed" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-enums-trafficqueryerror#/s:7heresdk17TrafficQueryErrorO25proxyAuthenticationFailedyA2CmF" class="token"><code>proxyAuthenticationFailed</code></a>` `

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

  ` `<span id="/s:7heresdk17TrafficQueryErrorO22proxyServerUnreachableyA2CmF"></span>` `<span id="//apple_ref/swift/Element/proxyServerUnreachable" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-enums-trafficqueryerror#/s:7heresdk17TrafficQueryErrorO22proxyServerUnreachableyA2CmF" class="token"><code>proxyServerUnreachable</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Proxy server unreachable. Error indicates a problem with a proxy server’s accessibility or connectivity.

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

  ` `<span id="/s:7heresdk17TrafficQueryErrorO10badRequestyA2CmF"></span>` `<span id="//apple_ref/swift/Element/badRequest" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-enums-trafficqueryerror#/s:7heresdk17TrafficQueryErrorO10badRequestyA2CmF" class="token"><code>badRequest</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Bad request. Error indicates server could not understand or process the request made by the client because the request itself was malformed or incorrect.

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

  ` `<span id="/s:7heresdk17TrafficQueryErrorO15tooManyRequestsyA2CmF"></span>` `<span id="//apple_ref/swift/Element/tooManyRequests" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-enums-trafficqueryerror#/s:7heresdk17TrafficQueryErrorO15tooManyRequestsyA2CmF" class="token"><code>tooManyRequests</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Server has received an excessive number of requests from client within a specific timeframe and client should slow down or wait before sending more requests.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case tooManyRequests
  ```

  </div>

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

