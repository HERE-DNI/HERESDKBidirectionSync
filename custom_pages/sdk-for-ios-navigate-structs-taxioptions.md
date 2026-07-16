---
title: "TaxiOptions Structure Reference"
slug: "sdk-for-ios-navigate-structs-taxioptions"
---

# TaxiOptions

<div class="declaration">

<div class="language">

``` highlight
@available(*, deprecated, message: "Will be removed in v4.28.0. Use `RoutingOptions` class instead.")
public struct TaxiOptions : Hashable
```

</div>

</div>

All the options to specify how a taxi route should be calculated. See, <a href="sdk-for-ios-navigate-enums-transportmode#sdk-for-ios-navigate-s-7heresdk13TransportModeO4taxiyA2CmF">`TransportMode.taxi`</a>.

**Note:** Specify the optional <a href="sdk-for-ios-navigate-structs-waypoint#sdk-for-ios-navigate-s-7heresdk8WaypointV16sideOfStreetHintAA14GeoCoordinatesVSgvp">`Waypoint.sideOfStreetHint`</a> to indicate at which side of the street a passenger wants to leave the taxi.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk11TaxiOptionsV05routeC0AA05RouteC0Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-routeOptions" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-taxioptions#sdk-for-ios-navigate-s-7heresdk11TaxiOptionsV05routeC0AA05RouteC0Vvp" class="token"><code>routeOptions</code></a> 

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

  - <a href="sdk-for-ios-navigate-structs-routeoptions">RouteOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk11TaxiOptionsV04textC0AA09RouteTextC0Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-textOptions" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-taxioptions#sdk-for-ios-navigate-s-7heresdk11TaxiOptionsV04textC0AA09RouteTextC0Vvp" class="token"><code>textOptions</code></a> 

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

  - <a href="sdk-for-ios-navigate-structs-routetextoptions">RouteTextOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk11TaxiOptionsV09avoidanceC0AA09AvoidanceC0Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-avoidanceOptions" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-taxioptions#sdk-for-ios-navigate-s-7heresdk11TaxiOptionsV09avoidanceC0AA09AvoidanceC0Vvp" class="token"><code>avoidanceOptions</code></a> 

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

  - <a href="sdk-for-ios-navigate-structs-avoidanceoptions">AvoidanceOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk11TaxiOptionsV04tollC0AA04TollC0Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-tollOptions" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-taxioptions#sdk-for-ios-navigate-s-7heresdk11TaxiOptionsV04tollC0AA04TollC0Vvp" class="token"><code>tollOptions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Options to specify how the tolls should be calculated, such as transponders, vehicle category, and emission type.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var tollOptions: TollOptions
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-tolloptions">TollOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk11TaxiOptionsV27lastCharacterOfLicensePlateSSSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-lastCharacterOfLicensePlate" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-taxioptions#sdk-for-ios-navigate-s-7heresdk11TaxiOptionsV27lastCharacterOfLicensePlateSSSgvp" class="token"><code>lastCharacterOfLicensePlate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies the last character of a vehicle’s license plate, typically used to evaluate traffic restrictions in certain environmental or low-emission zones. In cities like Bogotá, Mexico City, or Jakarta, specific license plate digits may be restricted on certain days or in certain areas to reduce congestion and emissions. When this value is provided, the HERE SDK considers it during route calculation to avoid roads or areas where your vehicle may be restricted based on local regulations. Example usage: “7”, when the license plate of a vehicle looks like “B-ET-182487”.

  If this value is not set, such license plate-based restrictions are ignored, and routing is performed without considering them.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var lastCharacterOfLicensePlate: String?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk11TaxiOptionsV18maxSpeedOnSegmentsSayAA03MaxeF7SegmentVGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-maxSpeedOnSegments" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-taxioptions#sdk-for-ios-navigate-s-7heresdk11TaxiOptionsV18maxSpeedOnSegmentsSayAA03MaxeF7SegmentVGvp" class="token"><code>maxSpeedOnSegments</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Segments with restriction on maximum <a href="sdk-for-ios-navigate-structs-dynamicspeedinfo#sdk-for-ios-navigate-s-7heresdk16DynamicSpeedInfoV04baseC17InMetersPerSecondSdvp">`DynamicSpeedInfo.baseSpeedInMetersPerSecond`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var maxSpeedOnSegments: [MaxSpeedOnSegment]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-maxspeedonsegment">MaxSpeedOnSegment</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk11TaxiOptionsV017allowDriveThroughB5RoadsSbvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-allowDriveThroughTaxiRoads" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-taxioptions#sdk-for-ios-navigate-s-7heresdk11TaxiOptionsV017allowDriveThroughB5RoadsSbvp" class="token"><code>allowDriveThroughTaxiRoads</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies if a vehicle is allowed to drive through the taxi-only roads and lanes. When set to `false`, it is still allowed on taxi roads after the route start and before the route destination.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var allowDriveThroughTaxiRoads: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk11TaxiOptionsV17carSpecificationsAA03CarE0Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-carSpecifications" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-taxioptions#sdk-for-ios-navigate-s-7heresdk11TaxiOptionsV17carSpecificationsAA03CarE0Vvp" class="token"><code>carSpecifications</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Detailed car specifications such as dimensions and weight.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var carSpecifications: CarSpecifications
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-carspecifications">CarSpecifications</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk11TaxiOptionsVACycfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-taxioptions#sdk-for-ios-navigate-s-7heresdk11TaxiOptionsVACycfc" class="token"><code>init()</code></a> 

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
  public init()
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk11TaxiOptionsV05routeC004textC009avoidanceC0AcA05RouteC0V_AA0g4TextC0VAA09AvoidanceC0Vtcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-routeOptions-textOptions-avoidanceOptions" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-taxioptions#sdk-for-ios-navigate-s-7heresdk11TaxiOptionsV05routeC004textC009avoidanceC0AcA05RouteC0V_AA0g4TextC0VAA09AvoidanceC0Vtcfc" class="token"><code>init(routeOptions:</code><wbr></wbr><code>textOptions:</code><wbr></wbr><code>avoidanceOptions:</code><wbr></wbr><code>)</code></a> 

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
  public init(routeOptions: RouteOptions, textOptions: RouteTextOptions, avoidanceOptions: AvoidanceOptions)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-routeoptions">RouteOptions</a>
  - <a href="sdk-for-ios-navigate-structs-routetextoptions">RouteTextOptions</a>
  - <a href="sdk-for-ios-navigate-structs-avoidanceoptions">AvoidanceOptions</a>

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

