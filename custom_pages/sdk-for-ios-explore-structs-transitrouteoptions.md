---
title: "TransitRouteOptions Structure Reference"
slug: "sdk-for-ios-explore-structs-transitrouteoptions"
---

# TransitRouteOptions

<div class="declaration">

<div class="language">

``` highlight
public struct TransitRouteOptions : Hashable
```

</div>

</div>

All the options to specify how a public transit route should be calculated.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19TransitRouteOptionsV13departureTime10Foundation4DateVSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-departureTime" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-transitrouteoptions#sdk-for-ios-explore-s-7heresdk19TransitRouteOptionsV13departureTime10Foundation4DateVSgvp" class="token"><code>departureTime</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Optional time when travel is expected to start. If it is not specified, it is set to the current time.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var departureTime: Date?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19TransitRouteOptionsV11arrivalTime10Foundation4DateVSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-arrivalTime" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-transitrouteoptions#sdk-for-ios-explore-s-7heresdk19TransitRouteOptionsV11arrivalTime10Foundation4DateVSgvp" class="token"><code>arrivalTime</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Optional time when travel is expected to end.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var arrivalTime: Date?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19TransitRouteOptionsV12alternativess5Int32Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-alternatives" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-transitrouteoptions#sdk-for-ios-explore-s-7heresdk19TransitRouteOptionsV12alternativess5Int32Vvp" class="token"><code>alternatives</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Number of alternative routes to return aside from the optimal route. The provided value must be in the range \[0, 6\]. By default, it is 0 and only one route is calculated.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var alternatives: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19TransitRouteOptionsV7changess5Int32VSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-changes" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-transitrouteoptions#sdk-for-ios-explore-s-7heresdk19TransitRouteOptionsV7changess5Int32VSgvp" class="token"><code>changes</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Maximum number of changes or transfers allowed in a route. When it is not set, unlimited number of changes is permitted. The provided value must be in the range \[0, 6\].

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var changes: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19TransitRouteOptionsV10modeFilterAA0b4ModeF0Ovp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-modeFilter" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-transitrouteoptions#sdk-for-ios-explore-s-7heresdk19TransitRouteOptionsV10modeFilterAA0b4ModeF0Ovp" class="token"><code>modeFilter</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines inclusion or exclusion of transit modes for route calculation. By default, the inclusion mode is used.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var modeFilter: TransitModeFilter
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-transitmodefilter">TransitModeFilter</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19TransitRouteOptionsV5modesSayAA0B4ModeOGvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-modes" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-transitrouteoptions#sdk-for-ios-explore-s-7heresdk19TransitRouteOptionsV5modesSayAA0B4ModeOGvp" class="token"><code>modes</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This list is used to determine which transit modes should be used for route calculation, <a href="sdk-for-ios-explore-structs-transitrouteoptions#sdk-for-ios-explore-s-7heresdk19TransitRouteOptionsV10modeFilterAA0b4ModeF0Ovp">`TransitRouteOptions.modeFilter`</a> specifies whether this list is an inclusion or an exclusion. For example, specifying subway and bus transit modes with the include filter, returns only subway and bus transit modes, and with the exclude filter, returns all the transit modes except subway and bus. When not set, all the supported transit modes are permitted. By default, this list is empty.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var modes: [TransitMode]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-transitmode">TransitMode</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19TransitRouteOptionsV32pedestrianSpeedInMetersPerSecondSdvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-pedestrianSpeedInMetersPerSecond" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-transitrouteoptions#sdk-for-ios-explore-s-7heresdk19TransitRouteOptionsV32pedestrianSpeedInMetersPerSecondSdvp" class="token"><code>pedestrianSpeedInMetersPerSecond</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Walking speed in meters per second. Influences the duration of walking segments from origin to a station, from a station to destination and in-between the stations (e.g. if transfer is needed). The provided value must be in the range \[0.5, 2.0\]. The default value is 1.0 mps.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var pedestrianSpeedInMetersPerSecond: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19TransitRouteOptionsV29pedestrianMaxDistanceInMeterss5Int32Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-pedestrianMaxDistanceInMeters" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-transitrouteoptions#sdk-for-ios-explore-s-7heresdk19TransitRouteOptionsV29pedestrianMaxDistanceInMeterss5Int32Vvp" class="token"><code>pedestrianMaxDistanceInMeters</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Maximum allowed walking distance in meters (e.g. when looking for nearest stations). The provided value must be in the range \[0, 6000\]. The default value is 2000 meters.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var pedestrianMaxDistanceInMeters: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19TransitRouteOptionsV04textD0AA0c4TextD0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-textOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-transitrouteoptions#sdk-for-ios-explore-s-7heresdk19TransitRouteOptionsV04textD0AA0c4TextD0Vvp" class="token"><code>textOptions</code></a> 

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

   <span id="sdk-for-ios-explore-s-7heresdk19TransitRouteOptionsV13departureTime07arrivalF012alternatives7changes10modeFilter5modes32pedestrianSpeedInMetersPerSecond0m11MaxDistanceoP004textD0AC10Foundation4DateVSg_APs5Int32VARSgAA0b4ModeK0OSayAA0bY0OGSdArA0c4TextD0Vtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-departureTime-arrivalTime-alternatives-changes-modeFilter-modes-pedestrianSpeedInMetersPerSecond-pedestrianMaxDistanceInMeters-textOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-transitrouteoptions#sdk-for-ios-explore-s-7heresdk19TransitRouteOptionsV13departureTime07arrivalF012alternatives7changes10modeFilter5modes32pedestrianSpeedInMetersPerSecond0m11MaxDistanceoP004textD0AC10Foundation4DateVSg_APs5Int32VARSgAA0b4ModeK0OSayAA0bY0OGSdArA0c4TextD0Vtcfc" class="token"><code>init(departureTime:</code><wbr></wbr><code>arrivalTime:</code><wbr></wbr><code>alternatives:</code><wbr></wbr><code>changes:</code><wbr></wbr><code>modeFilter:</code><wbr></wbr><code>modes:</code><wbr></wbr><code>pedestrianSpeedInMetersPerSecond:</code><wbr></wbr><code>pedestrianMaxDistanceInMeters:</code><wbr></wbr><code>textOptions:</code><wbr></wbr><code>)</code></a> 

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
  public init(departureTime: Date? = nil, arrivalTime: Date? = nil, alternatives: Int32 = 0, changes: Int32? = nil, modeFilter: TransitModeFilter = TransitModeFilter.include, modes: [TransitMode] = [], pedestrianSpeedInMetersPerSecond: Double = 1.0, pedestrianMaxDistanceInMeters: Int32 = 2000, textOptions: RouteTextOptions = RouteTextOptions())
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-transitmodefilter">TransitModeFilter</a>
  - <a href="sdk-for-ios-explore-enums-transitmode">TransitMode</a>
  - <a href="sdk-for-ios-explore-structs-routetextoptions">RouteTextOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19TransitRouteOptionsV33fromDefaultParameterConfigurationACyFZ"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-fromDefaultParameterConfiguration" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-transitrouteoptions#sdk-for-ios-explore-s-7heresdk19TransitRouteOptionsV33fromDefaultParameterConfigurationACyFZ" class="token"><code>fromDefaultParameterConfiguration()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Returns TransitRouteOptions instance with default values used in SDK.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func fromDefaultParameterConfiguration() -> TransitRouteOptions
  ```

  </div>

  </div>

  <div>

  #### Return Value

  An `TransitRouteOptions` instance with default values used in SDK.

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

