---
title: "RoutingError Enumeration Reference"
slug: "sdk-for-ios-explore-enums-routingerror"
---

# RoutingError

<div class="declaration">

<div class="language">

``` highlight
public enum RoutingError : UInt32, CaseIterable, Codable
```

</div>

</div>

Specifies possible errors that may result from the calculation of a route.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12RoutingErrorO08internalC0yA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-internalError" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-routingerror#sdk-for-ios-explore-s-7heresdk12RoutingErrorO08internalC0yA2CmF" class="token"><code>internalError</code></a> 

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
  case internalError = 1
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12RoutingErrorO16invalidParameteryA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-invalidParameter" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-routingerror#sdk-for-ios-explore-s-7heresdk12RoutingErrorO16invalidParameteryA2CmF" class="token"><code>invalidParameter</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  An invalid input parameter.

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

   <span id="sdk-for-ios-explore-s-7heresdk12RoutingErrorO17serverUnreachableyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-serverUnreachable" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-routingerror#sdk-for-ios-explore-s-7heresdk12RoutingErrorO17serverUnreachableyA2CmF" class="token"><code>serverUnreachable</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Routing server is unreachable.

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

   <span id="sdk-for-ios-explore-s-7heresdk12RoutingErrorO04httpC0yA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-httpError" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-routingerror#sdk-for-ios-explore-s-7heresdk12RoutingErrorO04httpC0yA2CmF" class="token"><code>httpError</code></a> 

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

   <span id="sdk-for-ios-explore-s-7heresdk12RoutingErrorO20authenticationFailedyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-authenticationFailed" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-routingerror#sdk-for-ios-explore-s-7heresdk12RoutingErrorO20authenticationFailedyA2CmF" class="token"><code>authenticationFailed</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Routing operation is not authenticated. Check your credentials.

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

   <span id="sdk-for-ios-explore-s-7heresdk12RoutingErrorO9forbiddenyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-forbidden" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-routingerror#sdk-for-ios-explore-s-7heresdk12RoutingErrorO9forbiddenyA2CmF" class="token"><code>forbidden</code></a> 

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

   <span id="sdk-for-ios-explore-s-7heresdk12RoutingErrorO18exceededUsageLimityA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-exceededUsageLimit" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-routingerror#sdk-for-ios-explore-s-7heresdk12RoutingErrorO18exceededUsageLimityA2CmF" class="token"><code>exceededUsageLimit</code></a> 

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

   <span id="sdk-for-ios-explore-s-7heresdk12RoutingErrorO07parsingC0yA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-parsingError" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-routingerror#sdk-for-ios-explore-s-7heresdk12RoutingErrorO07parsingC0yA2CmF" class="token"><code>parsingError</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Error while parsing route data. This is not expected to happen. Try updating to the newest version of the SDK. If the problem persists, please report a bug in the SDK.

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

   <span id="sdk-for-ios-explore-s-7heresdk12RoutingErrorO12noRouteFoundyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-noRouteFound" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-routingerror#sdk-for-ios-explore-s-7heresdk12RoutingErrorO12noRouteFoundyA2CmF" class="token"><code>noRouteFound</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  No route can be calculated for the given input.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case noRouteFound
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12RoutingErrorO8timedOutyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-timedOut" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-routingerror#sdk-for-ios-explore-s-7heresdk12RoutingErrorO8timedOutyA2CmF" class="token"><code>timedOut</code></a> 

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

   <span id="sdk-for-ios-explore-s-7heresdk12RoutingErrorO7offlineyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-offline" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-routingerror#sdk-for-ios-explore-s-7heresdk12RoutingErrorO7offlineyA2CmF" class="token"><code>offline</code></a> 

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

   <span id="sdk-for-ios-explore-s-7heresdk12RoutingErrorO14noIsolineFoundyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-noIsolineFound" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-routingerror#sdk-for-ios-explore-s-7heresdk12RoutingErrorO14noIsolineFoundyA2CmF" class="token"><code>noIsolineFound</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  No isoline can be calculated for the given input.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case noIsolineFound
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12RoutingErrorO13noRouteHandleyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-noRouteHandle" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-routingerror#sdk-for-ios-explore-s-7heresdk12RoutingErrorO13noRouteHandleyA2CmF" class="token"><code>noRouteHandle</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The route has no <a href="sdk-for-ios-explore-classes-route#sdk-for-ios-explore-s-7heresdk5RouteC11routeHandleAA0bD0VSgvp">`Route.routeHandle`</a>, but it was used for a feature that requires one. Consider to recalculate the route with a route handle. See <a href="sdk-for-ios-explore-structs-routeoptions#sdk-for-ios-explore-s-7heresdk12RouteOptionsV06enableB6HandleSbvp">`RouteOptions.enableRouteHandle`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case noRouteHandle
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12RoutingErrorO18operationCancelledyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-operationCancelled" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-routingerror#sdk-for-ios-explore-s-7heresdk12RoutingErrorO18operationCancelledyA2CmF" class="token"><code>operationCancelled</code></a> 

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

   <span id="sdk-for-ios-explore-s-7heresdk12RoutingErrorO24couldNotMatchDestinationyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-couldNotMatchDestination" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-routingerror#sdk-for-ios-explore-s-7heresdk12RoutingErrorO24couldNotMatchDestinationyA2CmF" class="token"><code>couldNotMatchDestination</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Destination waypoint could not be matched to a road network. Either this waypoint is far from road network or not enough data has been downloaded. When both, origin and destination, cannot be matched, then the origin waypoint error will take precedence.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case couldNotMatchDestination
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12RoutingErrorO19couldNotMatchOriginyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-couldNotMatchOrigin" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-routingerror#sdk-for-ios-explore-s-7heresdk12RoutingErrorO19couldNotMatchOriginyA2CmF" class="token"><code>couldNotMatchOrigin</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Origin waypoint could not be matched to a road network. Either this waypoint is far from road network or not enough data has been downloaded. When both, origin and destination, cannot be matched, then the origin waypoint error will take precedence.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case couldNotMatchOrigin
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12RoutingErrorO25failedRouteHandleCreationyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-failedRouteHandleCreation" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-routingerror#sdk-for-ios-explore-s-7heresdk12RoutingErrorO25failedRouteHandleCreationyA2CmF" class="token"><code>failedRouteHandleCreation</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  No RouteHandle was created.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case failedRouteHandleCreation
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12RoutingErrorO12importFailedyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-importFailed" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-routingerror#sdk-for-ios-explore-s-7heresdk12RoutingErrorO12importFailedyA2CmF" class="token"><code>importFailed</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  No route section was found for imported waypoints.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case importFailed
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12RoutingErrorO31noReachableChargingStationFoundyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-noReachableChargingStationFound" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-routingerror#sdk-for-ios-explore-s-7heresdk12RoutingErrorO31noReachableChargingStationFoundyA2CmF" class="token"><code>noReachableChargingStationFound</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Initial charge is not enough to reach any known charging stations.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case noReachableChargingStationFound
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12RoutingErrorO22routeCalculationFailedyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-routeCalculationFailed" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-routingerror#sdk-for-ios-explore-s-7heresdk12RoutingErrorO22routeCalculationFailedyA2CmF" class="token"><code>routeCalculationFailed</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Calculation did not succeed.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case routeCalculationFailed
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12RoutingErrorO24routeLengthLimitExceededyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-routeLengthLimitExceeded" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-routingerror#sdk-for-ios-explore-s-7heresdk12RoutingErrorO24routeLengthLimitExceededyA2CmF" class="token"><code>routeLengthLimitExceeded</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Distance between waypoints is too large for current options.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case routeLengthLimitExceeded
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12RoutingErrorO42violatedTransportModeInRouteHandleDecodingyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-violatedTransportModeInRouteHandleDecoding" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-routingerror#sdk-for-ios-explore-s-7heresdk12RoutingErrorO42violatedTransportModeInRouteHandleDecodingyA2CmF" class="token"><code>violatedTransportModeInRouteHandleDecoding</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Route handle decoding failed due to forbidden segments for the specified transport mode.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case violatedTransportModeInRouteHandleDecoding
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12RoutingErrorO25proxyAuthenticationFailedyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-proxyAuthenticationFailed" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-routingerror#sdk-for-ios-explore-s-7heresdk12RoutingErrorO25proxyAuthenticationFailedyA2CmF" class="token"><code>proxyAuthenticationFailed</code></a> 

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

   <span id="sdk-for-ios-explore-s-7heresdk12RoutingErrorO22proxyServerUnreachableyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-proxyServerUnreachable" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-routingerror#sdk-for-ios-explore-s-7heresdk12RoutingErrorO22proxyServerUnreachableyA2CmF" class="token"><code>proxyServerUnreachable</code></a> 

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

   <span id="sdk-for-ios-explore-s-7heresdk12RoutingErrorO15activeMapUpdateyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-activeMapUpdate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-routingerror#sdk-for-ios-explore-s-7heresdk12RoutingErrorO15activeMapUpdateyA2CmF" class="token"><code>activeMapUpdate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Route cannot be calculated due to active map update. Please, repeat the request after map update is finished successfully.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case activeMapUpdate
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

