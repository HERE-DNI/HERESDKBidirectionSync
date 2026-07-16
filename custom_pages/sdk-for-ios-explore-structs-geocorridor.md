---
title: "GeoCorridor Structure Reference"
slug: "sdk-for-ios-explore-structs-geocorridor"
---

# GeoCorridor

<div class="declaration">

<div class="language">

``` highlight
public struct GeoCorridor : Hashable
```

</div>

</div>

A geographical area that wraps around a geographical polyline with a given distance. The corridor has round edges at the endpoints of the polyline. The distance from any point of the polyline to the closest border of the corridor is always the same.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11GeoCorridorV8polylineSayAA0B11CoordinatesVGvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-polyline" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-geocorridor#sdk-for-ios-explore-s-7heresdk11GeoCorridorV8polylineSayAA0B11CoordinatesVGvp" class="token"><code>polyline</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The polyline passing through the middle of the corridor.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public let polyline: [GeoCoordinates]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geocoordinates">GeoCoordinates</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11GeoCorridorV17halfWidthInMeterss5Int32VSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-halfWidthInMeters" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-geocorridor#sdk-for-ios-explore-s-7heresdk11GeoCorridorV17halfWidthInMeterss5Int32VSgvp" class="token"><code>halfWidthInMeters</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The shortest distance from any point on the polyline to the border of the corridor.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public let halfWidthInMeters: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11GeoCorridorV8polyline17halfWidthInMetersACSayAA0B11CoordinatesVG_s5Int32Vtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-polyline-halfWidthInMeters" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-geocorridor#sdk-for-ios-explore-s-7heresdk11GeoCorridorV8polyline17halfWidthInMetersACSayAA0B11CoordinatesVG_s5Int32Vtcfc" class="token"><code>init(polyline:</code><wbr></wbr><code>halfWidthInMeters:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs a GeoCorridor from the provided polyline and half-width in meters.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(polyline: [GeoCoordinates], halfWidthInMeters: Int32)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geocoordinates">GeoCoordinates</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>polyline</code></em><code> </code></td>
  <td><div>
  <p>The polyline passing through the middle of the corridor.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>halfWidthInMeters</code></em><code> </code></td>
  <td><div>
  <p>The shortest distance from any point on the polyline to the border of the corridor.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11GeoCorridorV8polylineACSayAA0B11CoordinatesVG_tcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-polyline" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-geocorridor#sdk-for-ios-explore-s-7heresdk11GeoCorridorV8polylineACSayAA0B11CoordinatesVG_tcfc" class="token"><code>init(polyline:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs a GeoCorridor from the provided polyline.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(polyline: [GeoCoordinates])
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geocoordinates">GeoCoordinates</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>polyline</code></em><code> </code></td>
  <td><div>
  <p>The polyline passing through the middle of the corridor.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

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

