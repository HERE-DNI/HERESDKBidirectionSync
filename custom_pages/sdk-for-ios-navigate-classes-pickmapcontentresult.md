---
title: "PickMapContentResult Class Reference"
slug: "sdk-for-ios-navigate-classes-pickmapcontentresult"
---

# PickMapContentResult

<div class="declaration">

<div class="language">

``` highlight
public class PickMapContentResult
```

``` highlight
extension PickMapContentResult: NativeBase
```

``` highlight
extension PickMapContentResult: Hashable
```

</div>

</div>

A class that contains possible results from picking map content on the map scene.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk20PickMapContentResultC12pickedPlacesSayAA11PickedPlaceVGvp"></span>` `<span id="//apple_ref/swift/Property/pickedPlaces" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-pickmapcontentresult#/s:7heresdk20PickMapContentResultC12pickedPlacesSayAA11PickedPlaceVGvp" class="token"><code>pickedPlaces</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of picked places containing the POIs at the location of picking.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var pickedPlaces: [PickedPlace] { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20PickMapContentResultC16trafficIncidentsSayAC015TrafficIncidentE0CGvp"></span>` `<span id="//apple_ref/swift/Property/trafficIncidents" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-pickmapcontentresult#/s:7heresdk20PickMapContentResultC16trafficIncidentsSayAC015TrafficIncidentE0CGvp" class="token"><code>trafficIncidents</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of traffic incidents at the location of picking.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var trafficIncidents: [PickMapContentResult.TrafficIncidentResult] { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20PickMapContentResultC19vehicleRestrictionsSayAC018VehicleRestrictionE0VGvp"></span>` `<span id="//apple_ref/swift/Property/vehicleRestrictions" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-pickmapcontentresult#/s:7heresdk20PickMapContentResultC19vehicleRestrictionsSayAC018VehicleRestrictionE0VGvp" class="token"><code>vehicleRestrictions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of vehicle restrictions at the location of picking, sorted by distance to the center of the picking rectangle.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var vehicleRestrictions: [PickMapContentResult.VehicleRestrictionResult] { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20PickMapContentResultC015TrafficIncidentE0C"></span>` `<span id="//apple_ref/swift/Class/TrafficIncidentResult" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-pickmapcontentresult#/s:7heresdk20PickMapContentResultC015TrafficIncidentE0C" class="token"><code>TrafficIncidentResult</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Carries the result of picking a Carto traffic incident object. Description of incident is currently not present in our map data, so `description` always returns an empty string.

  <a href="sdk-for-ios-navigate-classes-pickmapcontentresult-trafficincidentresult" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

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

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20PickMapContentResultC018VehicleRestrictionE0V"></span>` `<span id="//apple_ref/swift/Struct/VehicleRestrictionResult" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-pickmapcontentresult#/s:7heresdk20PickMapContentResultC018VehicleRestrictionE0V" class="token"><code>VehicleRestrictionResult</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Carries the result of picking a vehicle restriction object.

  <a href="sdk-for-ios-navigate-classes-pickmapcontentresult-vehiclerestrictionresult" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct VehicleRestrictionResult
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

