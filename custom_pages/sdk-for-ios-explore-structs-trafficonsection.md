---
title: "TrafficOnSection Structure Reference"
slug: "sdk-for-ios-explore-structs-trafficonsection"
---

# TrafficOnSection

<div class="declaration">

<div class="language">

``` highlight
public struct TrafficOnSection : Hashable
```

</div>

</div>

Traffic information on a section.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk16TrafficOnSectionV8geometrySayAA14GeoCoordinatesVGvp"></span>` `<span id="//apple_ref/swift/Property/geometry" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-trafficonsection#/s:7heresdk16TrafficOnSectionV8geometrySayAA14GeoCoordinatesVGvp" class="token"><code>geometry</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of coordinates representing the polyline of this section.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var geometry: [GeoCoordinates]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16TrafficOnSectionV12trafficSpansSayAA0bC4SpanVGvp"></span>` `<span id="//apple_ref/swift/Property/trafficSpans" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-trafficonsection#/s:7heresdk16TrafficOnSectionV12trafficSpansSayAA0bC4SpanVGvp" class="token"><code>trafficSpans</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of traffic spans.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var trafficSpans: [TrafficOnSpan]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16TrafficOnSectionV16trafficIncidentsSayAA0b8IncidentC5RouteCGvp"></span>` `<span id="//apple_ref/swift/Property/trafficIncidents" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-trafficonsection#/s:7heresdk16TrafficOnSectionV16trafficIncidentsSayAA0b8IncidentC5RouteCGvp" class="token"><code>trafficIncidents</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of traffic incidents.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var trafficIncidents: [TrafficIncidentOnRoute]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16TrafficOnSectionV14departurePlaceAA05RouteF0Vvp"></span>` `<span id="//apple_ref/swift/Property/departurePlace" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-trafficonsection#/s:7heresdk16TrafficOnSectionV14departurePlaceAA05RouteF0Vvp" class="token"><code>departurePlace</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Describes the departure place.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var departurePlace: RoutePlace
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16TrafficOnSectionV12arrivalPlaceAA05RouteF0Vvp"></span>` `<span id="//apple_ref/swift/Property/arrivalPlace" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-trafficonsection#/s:7heresdk16TrafficOnSectionV12arrivalPlaceAA05RouteF0Vvp" class="token"><code>arrivalPlace</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Describes the arrival place.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var arrivalPlace: RoutePlace
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(geometry: trafficSpans: trafficIncidents: departurePlace: arrivalPlace: )

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
  public init ( geometry : [ GeoCoordinates ] = [], trafficSpans : [ TrafficOnSpan ] = [], trafficIncidents : [ TrafficIncidentOnRoute ] = [], departurePlace : RoutePlace , arrivalPlace : RoutePlace )
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

