---
title: "TrafficIncidentOnRoute Class Reference"
slug: "sdk-for-ios-navigate-classes-trafficincidentonroute"
---

# TrafficIncidentOnRoute

<div class="declaration">

<div class="language">

``` highlight
public class TrafficIncidentOnRoute : TrafficIncidentBase
```

``` highlight
extension TrafficIncidentOnRoute: NativeBase
```

``` highlight
extension TrafficIncidentOnRoute: Hashable
```

</div>

Related types:

- <a href="sdk-for-ios-navigate-protocols-trafficincidentbase">TrafficIncidentBase</a>

</div>

Traffic incidents on a route. Use <a href="sdk-for-ios-navigate-classes-section#sdk-for-ios-navigate-s-7heresdk7SectionC16trafficIncidentsSayAA22TrafficIncidentOnRouteCGvp">`Section.trafficIncidents`</a> to get a list of incidents on a route section. Use <a href="sdk-for-ios-navigate-classes-span#sdk-for-ios-navigate-s-7heresdk4SpanC22trafficIncidentIndexesSays5Int32VGvp">`Span.trafficIncidentIndexes`</a> to associate incidents with spans. Each incident takes at least the whole geometry of matching spans. Also, an incident can take some place out of the built route.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22TrafficIncidentOnRouteC6impactAA0bC6ImpactOvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-impact" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-trafficincidentonroute#sdk-for-ios-navigate-s-7heresdk22TrafficIncidentOnRouteC6impactAA0bC6ImpactOvp" class="token"><code>impact</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The impact of the incident. The value is <a href="sdk-for-ios-navigate-enums-trafficincidentimpact#sdk-for-ios-navigate-s-7heresdk21TrafficIncidentImpactO7unknownyA2CmF">`TrafficIncidentImpact.unknown`</a> if it hasn’t been provided by the traffic incidents supplier.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var impact: TrafficIncidentImpact { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-trafficincidentimpact">TrafficIncidentImpact</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22TrafficIncidentOnRouteC4typeAA0bC4TypeOvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-type" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-trafficincidentonroute#sdk-for-ios-navigate-s-7heresdk22TrafficIncidentOnRouteC4typeAA0bC4TypeOvp" class="token"><code>type</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The category of the incident. The value is <a href="sdk-for-ios-navigate-enums-trafficincidenttype#sdk-for-ios-navigate-s-7heresdk19TrafficIncidentTypeO7unknownyA2CmF">`TrafficIncidentType.unknown`</a> if it hasn’t been provided by the traffic incidents supplier.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var type: TrafficIncidentType { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-trafficincidenttype">TrafficIncidentType</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22TrafficIncidentOnRouteC11descriptionAA13LocalizedTextVvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-description" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-trafficincidentonroute#sdk-for-ios-navigate-s-7heresdk22TrafficIncidentOnRouteC11descriptionAA13LocalizedTextVvp" class="token"><code>description</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The human readable description of the incident, possibly with location information. The description is currently not present in our map data. Therefore, when accessing the data from a picked carto POI via `TrafficIncidentResult`, then always an empty string is returned. This does not apply when using the <a href="sdk-for-ios-navigate-classes-trafficengine">`TrafficEngine`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var description: LocalizedText { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-localizedtext">LocalizedText</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22TrafficIncidentOnRouteC9startTime10Foundation4DateVSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-startTime" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-trafficincidentonroute#sdk-for-ios-navigate-s-7heresdk22TrafficIncidentOnRouteC9startTime10Foundation4DateVSgvp" class="token"><code>startTime</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The time from which the incident is valid, before this time the incident should not be considered. The value is `nil` if it hasn’t been provided by the traffic incidents supplier.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var startTime: Date? { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22TrafficIncidentOnRouteC7endTime10Foundation4DateVSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-endTime" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-trafficincidentonroute#sdk-for-ios-navigate-s-7heresdk22TrafficIncidentOnRouteC7endTime10Foundation4DateVSgvp" class="token"><code>endTime</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The time until which the incident is valid, after this time the incident should not be considered. The value is `nil` if it hasn’t been provided by the traffic incidents supplier.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var endTime: Date? { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk22TrafficIncidentOnRouteC2idSSSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-id" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-trafficincidentonroute#sdk-for-ios-navigate-s-7heresdk22TrafficIncidentOnRouteC2idSSSgvp" class="token"><code>id</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The unique current identifier for a traffic incident. The identifier can be changed by the backend due to some events, e.g. changing of <a href="sdk-for-ios-navigate-classes-trafficincidentonroute#sdk-for-ios-navigate-s-7heresdk22TrafficIncidentOnRouteC7endTime10Foundation4DateVSgvp">`endTime`</a>. This field will be empty for `OfflineRouting`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var id: String? { get }
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

