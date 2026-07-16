---
title: "PedestrianOptions Structure Reference"
slug: "sdk-for-ios-explore-structs-pedestrianoptions"
---

# PedestrianOptions

<div class="declaration">

<div class="language">

``` highlight
@available(*, deprecated, message: "Will be removed in v4.28.0. Use `RoutingOptions` class instead.")
public struct PedestrianOptions : Hashable
```

</div>

</div>

All the options to specify how a pedestrian route should be calculated.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17PedestrianOptionsV05routeC0AA05RouteC0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-routeOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-pedestrianoptions#sdk-for-ios-explore-s-7heresdk17PedestrianOptionsV05routeC0AA05RouteC0Vvp" class="token"><code>routeOptions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies the common route calculation options.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var routeOptions: RouteOptions
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-routeoptions">RouteOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17PedestrianOptionsV04textC0AA09RouteTextC0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-textOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-pedestrianoptions#sdk-for-ios-explore-s-7heresdk17PedestrianOptionsV04textC0AA09RouteTextC0Vvp" class="token"><code>textOptions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Customize textual content returned from the route calculation, such as localization, format, and unit system.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var textOptions: RouteTextOptions
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-routetextoptions">RouteTextOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17PedestrianOptionsV09avoidanceC0AA09AvoidanceC0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-avoidanceOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-pedestrianoptions#sdk-for-ios-explore-s-7heresdk17PedestrianOptionsV09avoidanceC0AA09AvoidanceC0Vvp" class="token"><code>avoidanceOptions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Options to specify restrictions for route calculations. By default no restrictions are applied.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var avoidanceOptions: AvoidanceOptions
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-avoidanceoptions">AvoidanceOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17PedestrianOptionsV26walkSpeedInMetersPerSecondSdvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-walkSpeedInMetersPerSecond" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-pedestrianoptions#sdk-for-ios-explore-s-7heresdk17PedestrianOptionsV26walkSpeedInMetersPerSecondSdvp" class="token"><code>walkSpeedInMetersPerSecond</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies the speed that will be used by the service as the walking speed for pedestrian routing in meters per second. It influences the duration of walking segments along the route. The provided value must be in the range \[0.5, 2.0\]. When the value is outside this range, an invalid parameter error is raised. Refer to <a href="sdk-for-ios-explore-enums-routingerror">`RoutingError`</a> for details. The default speed is 1 meter per second.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var walkSpeedInMetersPerSecond: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17PedestrianOptionsV05routeC004textC009avoidanceC026walkSpeedInMetersPerSecondAcA05RouteC0V_AA0m4TextC0VAA09AvoidanceC0VSdtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-routeOptions-textOptions-avoidanceOptions-walkSpeedInMetersPerSecond" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-pedestrianoptions#sdk-for-ios-explore-s-7heresdk17PedestrianOptionsV05routeC004textC009avoidanceC026walkSpeedInMetersPerSecondAcA05RouteC0V_AA0m4TextC0VAA09AvoidanceC0VSdtcfc" class="token"><code>init(routeOptions:</code><wbr></wbr><code>textOptions:</code><wbr></wbr><code>avoidanceOptions:</code><wbr></wbr><code>walkSpeedInMetersPerSecond:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(routeOptions: RouteOptions = RouteOptions(), textOptions: RouteTextOptions = RouteTextOptions(), avoidanceOptions: AvoidanceOptions = AvoidanceOptions(), walkSpeedInMetersPerSecond: Double = 1.0)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-routeoptions">RouteOptions</a>
  - <a href="sdk-for-ios-explore-structs-routetextoptions">RouteTextOptions</a>
  - <a href="sdk-for-ios-explore-structs-avoidanceoptions">AvoidanceOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17PedestrianOptionsV33fromDefaultParameterConfigurationACyFZ"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-fromDefaultParameterConfiguration" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-pedestrianoptions#sdk-for-ios-explore-s-7heresdk17PedestrianOptionsV33fromDefaultParameterConfigurationACyFZ" class="token"><code>fromDefaultParameterConfiguration()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Returns PedestrianOptions instance with default values used in SDK.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func fromDefaultParameterConfiguration() -> PedestrianOptions
  ```

  </div>

  </div>

  <div>

  #### Return Value

  A `PedestrianOptions` instance with default values used in SDK.

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

