---
title: "IndoorRouteOptions Structure Reference"
slug: "sdk-for-ios-explore-structs-indoorrouteoptions"
---

# IndoorRouteOptions

<div class="declaration">

<div class="language">

``` highlight
public struct IndoorRouteOptions : Hashable
```

</div>

</div>

All the options to specify how an indoor route should be calculated.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk18IndoorRouteOptionsV05routeD0AA0cD0Vvp"></span>` `<span id="//apple_ref/swift/Property/routeOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-indoorrouteoptions#/s:7heresdk18IndoorRouteOptionsV05routeD0AA0cD0Vvp" class="token"><code>routeOptions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies the common route calculation options.

  **Note:** Currently, only <a href="sdk-for-ios-explore-structs-routeoptions#/s:7heresdk12RouteOptionsV16optimizationModeAA012OptimizationE0Ovp">`RouteOptions.optimizationMode`</a> parameter is utilized for indoor route calculation.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var routeOptions: RouteOptions
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18IndoorRouteOptionsV13transportModeAA014VenueTransportF0Ovp"></span>` `<span id="//apple_ref/swift/Property/transportMode" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-indoorrouteoptions#/s:7heresdk18IndoorRouteOptionsV13transportModeAA014VenueTransportF0Ovp" class="token"><code>transportMode</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The transport mode for route calculation.

  **Note:** Indoor route sections of the resulting route will always be <a href="sdk-for-ios-explore-enums-venuetransportmode#/s:7heresdk18VenueTransportModeO10pedestrianyA2CmF">`VenueTransportMode.pedestrian`</a> in the current implementation. This option will affect only outdoor route sections.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var transportMode: VenueTransportMode
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18IndoorRouteOptionsV015indoorAvoidanceD0AA0bfD0Vvp"></span>` `<span id="//apple_ref/swift/Property/indoorAvoidanceOptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-indoorrouteoptions#/s:7heresdk18IndoorRouteOptionsV015indoorAvoidanceD0AA0bfD0Vvp" class="token"><code>indoorAvoidanceOptions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Options to specify restrictions for indoor route calculations. By default no restrictions are applied.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var indoorAvoidanceOptions: IndoorAvoidanceOptions
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18IndoorRouteOptionsV22speedInMetersPerSecondSdvp"></span>` `<span id="//apple_ref/swift/Property/speedInMetersPerSecond" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-indoorrouteoptions#/s:7heresdk18IndoorRouteOptionsV22speedInMetersPerSecondSdvp" class="token"><code>speedInMetersPerSecond</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies the speed that will be used by the service as the speed for <a href="sdk-for-ios-explore-enums-venuetransportmode">`VenueTransportMode`</a> in meters per second. It influences the duration of segments along the route. The default speed is 1 meter per second.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var speedInMetersPerSecond: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(routeOptions: transportMode: indoorAvoidanceOptions: speedInMetersPerSecond: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates an object and assign default values for route options.

  - Parameters

    - routeOptions: Specifies the common route calculation options.

    **Note:** Currently, only <a href="sdk-for-ios-explore-structs-routeoptions#/s:7heresdk12RouteOptionsV16optimizationModeAA012OptimizationE0Ovp">`RouteOptions.optimizationMode`</a> parameter is utilized for indoor route calculation.

    - transportMode: The transport mode for route calculation.

    **Note:** Indoor route sections of the resulting route will always be <a href="sdk-for-ios-explore-enums-venuetransportmode#/s:7heresdk18VenueTransportModeO10pedestrianyA2CmF">`VenueTransportMode.pedestrian`</a> in the current implementation. This option will affect only outdoor route sections.

    - indoorAvoidanceOptions: Options to specify restrictions for indoor route calculations. By default no restrictions are applied.
    - speedInMetersPerSecond: Specifies the speed that will be used by the service as the speed for <a href="sdk-for-ios-explore-enums-venuetransportmode">`VenueTransportMode`</a> in meters per second. It influences the duration of segments along the route. The default speed is 1 meter per second.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( routeOptions : RouteOptions = RouteOptions (), transportMode : VenueTransportMode = VenueTransportMode . pedestrian , indoorAvoidanceOptions : IndoorAvoidanceOptions = IndoorAvoidanceOptions (), speedInMetersPerSecond : Double = 1.0 )
  ```

  </pre>

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

