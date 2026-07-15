---
title: "TrafficFlow Class Reference"
slug: "sdk-for-ios-navigate-classes-trafficflow"
---

# TrafficFlow

<div class="declaration">

<div class="language">

``` highlight
public class TrafficFlow : TrafficFlowBase
```

``` highlight
extension TrafficFlow: NativeBase
```

``` highlight
extension TrafficFlow: Hashable
```

</div>

</div>

This class provides details about traffic flow along a <a href="sdk-for-ios-navigate-structs-geocorridor">`GeoCorridor`</a>, inside a <a href="sdk-for-ios-navigate-structs-geocircle">`GeoCircle`</a> or a <a href="sdk-for-ios-navigate-structs-geobox">`GeoBox`</a>, that represents particular path of the road network.\
Backends for TrafficEngine and traffic vector tiles are different however backends may share the same data.\
For additional information about fields, refer to <a href="https://www.here.com/docs/bundle/traffic-api-v7-api-reference/page/index.html#tag/Real-Time-Traffic">Traffic API v7 API Reference: Traffic API v7</a>.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk11TrafficFlowC04freeC22SpeedInMetersPerSecondSdvp"></span>` `<span id="//apple_ref/swift/Property/freeFlowSpeedInMetersPerSecond" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-trafficflow#/s:7heresdk11TrafficFlowC04freeC22SpeedInMetersPerSecondSdvp" class="token"><code>freeFlowSpeedInMetersPerSecond</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The reference speed in meters per second along the roadway when no traffic is present.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var freeFlowSpeedInMetersPerSecond: Double { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11TrafficFlowC9jamFactorSdvp"></span>` `<span id="//apple_ref/swift/Property/jamFactor" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-trafficflow#/s:7heresdk11TrafficFlowC9jamFactorSdvp" class="token"><code>jamFactor</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A value for the amount of traffic on the roadway. The value, between 0.0 and 10.0, indicate the expected quality of travel. A value of 0.0 indicates that there is no congestion on the roadway. As the value approaches 10.0, it indicates increasing congestion. A value of 10.0 is reserved to represent a blocked roadway (closure).

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var jamFactor: Double { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11TrafficFlowC8locationAA0B8LocationVvp"></span>` `<span id="//apple_ref/swift/Property/location" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-trafficflow#/s:7heresdk11TrafficFlowC8locationAA0B8LocationVvp" class="token"><code>location</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines the location affected by traffic flow.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var location: TrafficLocation { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11TrafficFlowC22speedInMetersPerSecondSdSgvp"></span>` `<span id="//apple_ref/swift/Property/speedInMetersPerSecond" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-trafficflow#/s:7heresdk11TrafficFlowC22speedInMetersPerSecondSdSgvp" class="token"><code>speedInMetersPerSecond</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The expected speed in meters per second along the roadway; will not exceed the legal speed limit.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var speedInMetersPerSecond: Double? { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11TrafficFlowC30speedUncappedInMetersPerSecondSdSgvp"></span>` `<span id="//apple_ref/swift/Property/speedUncappedInMetersPerSecond" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-trafficflow#/s:7heresdk11TrafficFlowC30speedUncappedInMetersPerSecondSdSgvp" class="token"><code>speedUncappedInMetersPerSecond</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The expected speed in meters per second that a car can drive along a roadway right now; may exceed the legal speed limit. It is based on probe data (GPS coordinates sent by vehicles or mobile devices driving along that roadway). The calculated ‘expected speed’ may be over the legal speed limit for that roadway because people are driving over the speed limit.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var speedUncappedInMetersPerSecond: Double? { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11TrafficFlowC11jamTendencys5Int16VSgvp"></span>` `<span id="//apple_ref/swift/Property/jamTendency" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-trafficflow#/s:7heresdk11TrafficFlowC11jamTendencys5Int16VSgvp" class="token"><code>jamTendency</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The jamTendency field denotes whether the congestion is increasing, decreasing, or constant. The congestion tendency may take the following values:

  - +2 - rapidly increasing congestion
  - +1 - increasing congestion
  - 0 - constant congestion
  - -1 - decreasing congestion
  - -2 - rapidly decreasing congestion Default value of 0 can be assumed when this attribute is not present.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var jamTendency: Int16? { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11TrafficFlowC10confidenceSdSgvp"></span>` `<span id="//apple_ref/swift/Property/confidence" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-trafficflow#/s:7heresdk11TrafficFlowC10confidenceSdSgvp" class="token"><code>confidence</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The confidence field indicates the proportion of real-time data included in the speed calculation. It is a normalized value between 0.0 and 1.0 with the following meaning:

  - 0.7 \< confidence \<= 1.0 indicates real time speeds
  - 0.5 \< confidence \<= 0.7 indicates historical speeds
  - 0.0 \< confidence \<= 0.5 indicates speed limit

  This field can be used to identify whether the data for a location is derived from real-time probe sources or historical information only. All confidence data 0.71 and above is based on real-time information, where a confidence value of 0.75 or greater indicates high confidence real-time information. A confidence value equal to 0.70 or lower means that the data is derived from historical data only.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var confidence: Double? { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11TrafficFlowC14traversabilityAA14TraversabilityOSgvp"></span>` `<span id="//apple_ref/swift/Property/traversability" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-trafficflow#/s:7heresdk11TrafficFlowC14traversabilityAA14TraversabilityOSgvp" class="token"><code>traversability</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The traversability of roadway.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var traversability: Traversability? { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk11TrafficFlowC23junctionsTraversabilityAA09JunctionsE0OSgvp"></span>` `<span id="//apple_ref/swift/Property/junctionsTraversability" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-trafficflow#/s:7heresdk11TrafficFlowC23junctionsTraversabilityAA09JunctionsE0OSgvp" class="token"><code>junctionsTraversability</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The traversability of junctions along the affected road.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var junctionsTraversability: JunctionsTraversability? { get }
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

