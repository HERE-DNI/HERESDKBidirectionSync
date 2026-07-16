---
title: "TrafficOnSpan Structure Reference"
slug: "sdk-for-ios-navigate-structs-trafficonspan"
---

# TrafficOnSpan

<div class="declaration">

<div class="language">

``` highlight
public struct TrafficOnSpan : Hashable
```

</div>

</div>

Traffic information of a span along a route.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13TrafficOnSpanV28trafficSectionPolylineOffsets5Int32Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-trafficSectionPolylineOffset" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-trafficonspan#sdk-for-ios-navigate-s-7heresdk13TrafficOnSpanV28trafficSectionPolylineOffsets5Int32Vvp" class="token"><code>trafficSectionPolylineOffset</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Index over <a href="sdk-for-ios-navigate-structs-trafficonsection#sdk-for-ios-navigate-s-7heresdk16TrafficOnSectionV8geometrySayAA14GeoCoordinatesVGvp">`TrafficOnSection.geometry`</a> where this span starts.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var trafficSectionPolylineOffset: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13TrafficOnSpanV14lengthInMetersSdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-lengthInMeters" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-trafficonspan#sdk-for-ios-navigate-s-7heresdk13TrafficOnSpanV14lengthInMetersSdvp" class="token"><code>lengthInMeters</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Length of the traffic span, in meters.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var lengthInMeters: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13TrafficOnSpanV8durationSdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-duration" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-trafficonspan#sdk-for-ios-navigate-s-7heresdk13TrafficOnSpanV8durationSdvp" class="token"><code>duration</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The time duration necessary to traverse the traffic span. This duration takes also into consideration the delays caused by the traffic.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var duration: TimeInterval
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13TrafficOnSpanV12trafficDelaySdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-trafficDelay" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-trafficonspan#sdk-for-ios-navigate-s-7heresdk13TrafficOnSpanV12trafficDelaySdvp" class="token"><code>trafficDelay</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The estimated extra time in seconds spent due to traffic delays along this traffic span. Negative values indicate that the traffic span can be traversed faster than usual.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var trafficDelay: TimeInterval
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13TrafficOnSpanV26baseSpeedInMetersPerSecondSdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-baseSpeedInMetersPerSecond" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-trafficonspan#sdk-for-ios-navigate-s-7heresdk13TrafficOnSpanV26baseSpeedInMetersPerSecondSdvp" class="token"><code>baseSpeedInMetersPerSecond</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The speed, in meters per second, without taking traffic into consideration.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var baseSpeedInMetersPerSecond: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13TrafficOnSpanV29trafficSpeedInMetersPerSecondSdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-trafficSpeedInMetersPerSecond" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-trafficonspan#sdk-for-ios-navigate-s-7heresdk13TrafficOnSpanV29trafficSpeedInMetersPerSecondSdvp" class="token"><code>trafficSpeedInMetersPerSecond</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The speed, in meters per second, considering traffic.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var trafficSpeedInMetersPerSecond: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13TrafficOnSpanV9jamFactorSdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-jamFactor" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-trafficonspan#sdk-for-ios-navigate-s-7heresdk13TrafficOnSpanV9jamFactorSdvp" class="token"><code>jamFactor</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The traffic jam factor shows the traffic condition in a numeric way. It is a value in the range \[0.0, 10.0\]. A large jamFactor value means more traffic jam in general. Specifically, 0.0 means free traffic and 10.0 means stationary traffic.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var jamFactor: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13TrafficOnSpanV15incidentIndicesSays5Int32VGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-incidentIndices" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-trafficonspan#sdk-for-ios-navigate-s-7heresdk13TrafficOnSpanV15incidentIndicesSays5Int32VGvp" class="token"><code>incidentIndices</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The indices of traffic incidents from the field <a href="sdk-for-ios-navigate-structs-trafficonsection#sdk-for-ios-navigate-s-7heresdk16TrafficOnSectionV16trafficIncidentsSayAA0b8IncidentC5RouteCGvp">`TrafficOnSection.trafficIncidents`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var incidentIndices: [Int32]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13TrafficOnSpanV26consumptionInKilowattHoursSdSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-consumptionInKilowattHours" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-trafficonspan#sdk-for-ios-navigate-s-7heresdk13TrafficOnSpanV26consumptionInKilowattHoursSdSgvp" class="token"><code>consumptionInKilowattHours</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The power consumption in kilowatt-hours (kWh) necessary to traverse the span.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var consumptionInKilowattHours: Double?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13TrafficOnSpanV28trafficSectionPolylineOffset14lengthInMeters8duration0E5Delay09baseSpeedjK9PerSecond0eojkpQ09jamFactor15incidentIndices011consumptionJ13KilowattHoursACs5Int32V_S6dSayANGSdSgtcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-trafficSectionPolylineOffset-lengthInMeters-duration-trafficDelay-baseSpeedInMetersPerSecond-trafficSpeedInMetersPerSecond-jamFactor-incidentIndices-consumptionInKilowattHours" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-trafficonspan#sdk-for-ios-navigate-s-7heresdk13TrafficOnSpanV28trafficSectionPolylineOffset14lengthInMeters8duration0E5Delay09baseSpeedjK9PerSecond0eojkpQ09jamFactor15incidentIndices011consumptionJ13KilowattHoursACs5Int32V_S6dSayANGSdSgtcfc" class="token"><code>init(trafficSectionPolylineOffset:</code><wbr></wbr><code>lengthInMeters:</code><wbr></wbr><code>duration:</code><wbr></wbr><code>trafficDelay:</code><wbr></wbr><code>baseSpeedInMetersPerSecond:</code><wbr></wbr><code>trafficSpeedInMetersPerSecond:</code><wbr></wbr><code>jamFactor:</code><wbr></wbr><code>incidentIndices:</code><wbr></wbr><code>consumptionInKilowattHours:</code><wbr></wbr><code>)</code></a> 

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
  public init(trafficSectionPolylineOffset: Int32 = 0, lengthInMeters: Double = 0.0, duration: TimeInterval = 0, trafficDelay: TimeInterval = 0, baseSpeedInMetersPerSecond: Double = 0.0, trafficSpeedInMetersPerSecond: Double = 0.0, jamFactor: Double = 0.0, incidentIndices: [Int32] = [], consumptionInKilowattHours: Double? = nil)
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

