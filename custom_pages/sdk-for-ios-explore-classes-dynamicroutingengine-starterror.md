---
title: "StartError Enumeration Reference"
slug: "sdk-for-ios-explore-classes-dynamicroutingengine-starterror"
---

# StartError

<div class="declaration">

<div class="language">

``` highlight
public enum StartError : UInt32, CaseIterable, Codable
```

``` highlight
extension DynamicRoutingEngine.StartError : Error
```

</div>

</div>

Start error

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk20DynamicRoutingEngineC10StartErrorO08internalF0yA2EmF"></span>` `<span id="//apple_ref/swift/Element/internalError" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-dynamicroutingengine-starterror#/s:7heresdk20DynamicRoutingEngineC10StartErrorO08internalF0yA2EmF" class="token"><code>internalError</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  An internal issue occurred. Maybe the logs can provide some information.

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

  ` `<span id="/s:7heresdk20DynamicRoutingEngineC10StartErrorO12missingRouteyA2EmF"></span>` `<span id="//apple_ref/swift/Element/missingRoute" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-dynamicroutingengine-starterror#/s:7heresdk20DynamicRoutingEngineC10StartErrorO12missingRouteyA2EmF" class="token"><code>missingRoute</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The passed route object is invalid/`nil`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case missingRoute
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20DynamicRoutingEngineC10StartErrorO18missingRouteHandleyA2EmF"></span>` `<span id="//apple_ref/swift/Element/missingRouteHandle" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-dynamicroutingengine-starterror#/s:7heresdk20DynamicRoutingEngineC10StartErrorO18missingRouteHandleyA2EmF" class="token"><code>missingRouteHandle</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The passed route has no route handle. <a href="sdk-for-ios-explore-structs-routeoptions#/s:7heresdk12RouteOptionsV06enableB6HandleSbvp">`RouteOptions.enableRouteHandle`</a> needs to be set to true on the initial route calculation.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case missingRouteHandle
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20DynamicRoutingEngineC10StartErrorO15missingListeneryA2EmF"></span>` `<span id="//apple_ref/swift/Element/missingListener" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-dynamicroutingengine-starterror#/s:7heresdk20DynamicRoutingEngineC10StartErrorO15missingListeneryA2EmF" class="token"><code>missingListener</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The listener is not valid.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case missingListener
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20DynamicRoutingEngineC10StartErrorO15tooFewWaypointsyA2EmF"></span>` `<span id="//apple_ref/swift/Element/tooFewWaypoints" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-dynamicroutingengine-starterror#/s:7heresdk20DynamicRoutingEngineC10StartErrorO15tooFewWaypointsyA2EmF" class="token"><code>tooFewWaypoints</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Too few waypoints where passed.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case tooFewWaypoints
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20DynamicRoutingEngineC10StartErrorO26invalidRefreshRouteOptionsyA2EmF"></span>` `<span id="//apple_ref/swift/Element/invalidRefreshRouteOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-dynamicroutingengine-starterror#/s:7heresdk20DynamicRoutingEngineC10StartErrorO26invalidRefreshRouteOptionsyA2EmF" class="token"><code>invalidRefreshRouteOptions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Invalid RefreshRouteOptions passed.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case invalidRefreshRouteOptions
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

