---
title: "TrafficIncidentResult Class Reference"
slug: "sdk-for-ios-navigate-classes-pickmapcontentresult-trafficincidentresult"
---

# TrafficIncidentResult

<div class="declaration">

<div class="language">

``` highlight
public class TrafficIncidentResult : TrafficIncidentBase
```

``` highlight
extension PickMapContentResult.TrafficIncidentResult: NativeBase
```

``` highlight
extension PickMapContentResult.TrafficIncidentResult: Hashable
```

</div>

</div>

Carries the result of picking a Carto traffic incident object. Description of incident is currently not present in our map data, so `description` always returns an empty string.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk20PickMapContentResultC015TrafficIncidentE0C6impactAA0fG6ImpactOvp"></span>` `<span id="//apple_ref/swift/Property/impact" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-pickmapcontentresult-trafficincidentresult#/s:7heresdk20PickMapContentResultC015TrafficIncidentE0C6impactAA0fG6ImpactOvp" class="token"><code>impact</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The impact of the incident. The value is <a href="sdk-for-ios-navigate-enums-trafficincidentimpact#/s:7heresdk21TrafficIncidentImpactO7unknownyA2CmF">`TrafficIncidentImpact.unknown`</a> if it hasn’t been provided by the traffic incidents supplier.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var impact: TrafficIncidentImpact { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20PickMapContentResultC015TrafficIncidentE0C4typeAA0fG4TypeOvp"></span>` `<span id="//apple_ref/swift/Property/type" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-pickmapcontentresult-trafficincidentresult#/s:7heresdk20PickMapContentResultC015TrafficIncidentE0C4typeAA0fG4TypeOvp" class="token"><code>type</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The category of the incident. The value is <a href="sdk-for-ios-navigate-enums-trafficincidenttype#/s:7heresdk19TrafficIncidentTypeO7unknownyA2CmF">`TrafficIncidentType.unknown`</a> if it hasn’t been provided by the traffic incidents supplier.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var type: TrafficIncidentType { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20PickMapContentResultC015TrafficIncidentE0C11descriptionAA13LocalizedTextVvp"></span>` `<span id="//apple_ref/swift/Property/description" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-pickmapcontentresult-trafficincidentresult#/s:7heresdk20PickMapContentResultC015TrafficIncidentE0C11descriptionAA13LocalizedTextVvp" class="token"><code>description</code></a>` `

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

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20PickMapContentResultC015TrafficIncidentE0C9startTime10Foundation4DateVSgvp"></span>` `<span id="//apple_ref/swift/Property/startTime" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-pickmapcontentresult-trafficincidentresult#/s:7heresdk20PickMapContentResultC015TrafficIncidentE0C9startTime10Foundation4DateVSgvp" class="token"><code>startTime</code></a>` `

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

  ` `<span id="/s:7heresdk20PickMapContentResultC015TrafficIncidentE0C7endTime10Foundation4DateVSgvp"></span>` `<span id="//apple_ref/swift/Property/endTime" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-pickmapcontentresult-trafficincidentresult#/s:7heresdk20PickMapContentResultC015TrafficIncidentE0C7endTime10Foundation4DateVSgvp" class="token"><code>endTime</code></a>` `

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

  ` `<span id="/s:7heresdk20PickMapContentResultC015TrafficIncidentE0C10originalIdSSvp"></span>` `<span id="//apple_ref/swift/Property/originalId" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-pickmapcontentresult-trafficincidentresult#/s:7heresdk20PickMapContentResultC015TrafficIncidentE0C10originalIdSSvp" class="token"><code>originalId</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Unique traffic event ID. Can be referenced when checking for updated traffic information for the specified event.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var originalId: String { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20PickMapContentResultC015TrafficIncidentE0C11coordinatesAA14GeoCoordinatesVvp"></span>` `<span id="//apple_ref/swift/Property/coordinates" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-pickmapcontentresult-trafficincidentresult#/s:7heresdk20PickMapContentResultC015TrafficIncidentE0C11coordinatesAA14GeoCoordinatesVvp" class="token"><code>coordinates</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The geographic coordinates of the traffic incident.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var coordinates: GeoCoordinates { get }
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

