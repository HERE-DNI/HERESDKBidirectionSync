---
title: "GeoCoordinatesUpdate Structure Reference"
slug: "sdk-for-ios-navigate-structs-geocoordinatesupdate"
---

# GeoCoordinatesUpdate

<div class="declaration">

<div class="language">

``` highlight
public struct GeoCoordinatesUpdate : Hashable
```

</div>

</div>

Represents geographical coordinates in 3D space. Unlike <a href="sdk-for-ios-navigate-structs-geocoordinates">`GeoCoordinates`</a>, its members can be undefined, allowing for APIs that update only the specified parts of geo coordinates.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk20GeoCoordinatesUpdateV8latitudeSdSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-latitude" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-geocoordinatesupdate#sdk-for-ios-navigate-s-7heresdk20GeoCoordinatesUpdateV8latitudeSdSgvp" class="token"><code>latitude</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Optional latitude in degrees.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public let latitude: Double?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk20GeoCoordinatesUpdateV9longitudeSdSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-longitude" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-geocoordinatesupdate#sdk-for-ios-navigate-s-7heresdk20GeoCoordinatesUpdateV9longitudeSdSgvp" class="token"><code>longitude</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Optional longitude in degrees.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public let longitude: Double?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk20GeoCoordinatesUpdateV8altitudeSdSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-altitude" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-geocoordinatesupdate#sdk-for-ios-navigate-s-7heresdk20GeoCoordinatesUpdateV8altitudeSdSgvp" class="token"><code>altitude</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Optional altitude in meters.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public let altitude: Double?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk20GeoCoordinatesUpdateV8latitude9longitudeACSdSg_AFtcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-latitude-longitude" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-geocoordinatesupdate#sdk-for-ios-navigate-s-7heresdk20GeoCoordinatesUpdateV8latitude9longitudeACSdSg_AFtcfc" class="token"><code>init(latitude:</code><wbr></wbr><code>longitude:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs a GeoCoordinatesUpdate from the provided latitude and longitude values. Corrects values of latitude and longitude if they exceed the ranges.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(latitude: Double?, longitude: Double?)
  ```

  </div>

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
  <td><code> </code><em><code>latitude</code></em><code> </code></td>
  <td><div>
  <p>Latitude in degrees. Positive value means Northern hemisphere. If the value is out of range of [-90.0, 90.0] it’s clamped to that range. NaN value is converted to <code>nil</code>.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>longitude</code></em><code> </code></td>
  <td><div>
  <p>Longitude in degrees. Positive value means Eastern hemisphere. If the value is out of range of [-180.0, 180.0] it’s replaced with a value within the range, representing effectively the same meridian. NaN value is converted to <code>nil</code>.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk20GeoCoordinatesUpdateV8latitude9longitude8altitudeACSdSg_A2Gtcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-latitude-longitude-altitude" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-geocoordinatesupdate#sdk-for-ios-navigate-s-7heresdk20GeoCoordinatesUpdateV8latitude9longitude8altitudeACSdSg_A2Gtcfc" class="token"><code>init(latitude:</code><wbr></wbr><code>longitude:</code><wbr></wbr><code>altitude:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs a GeoCoordinatesUpdate from the provided latitude, longitude and alt values. Corrects values of latitude and longitude if they exceed the ranges.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(latitude: Double?, longitude: Double?, altitude: Double?)
  ```

  </div>

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
  <td><code> </code><em><code>latitude</code></em><code> </code></td>
  <td><div>
  <p>Latitude in degrees. Positive value means Northern hemisphere. If the value is out of range of [-90.0, 90.0] it’s clamped to that range. NaN value is converted to <code>nil</code>.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>longitude</code></em><code> </code></td>
  <td><div>
  <p>Longitude in degrees. Positive value means Eastern hemisphere. If the value is out of range of [-180.0, 180.0] it’s replaced with a value within the range, representing effectively the same meridian. NaN value is converted to <code>nil</code>.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>altitude</code></em><code> </code></td>
  <td><div>
  <p>Altitude in meters. NaN value is converted to <code>nil</code>.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk20GeoCoordinatesUpdateVyAcA0bC0Vcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-_" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-geocoordinatesupdate#sdk-for-ios-navigate-s-7heresdk20GeoCoordinatesUpdateVyAcA0bC0Vcfc" class="token"><code>init(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs a GeoCoordinatesUpdate from GeoCoordinates

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(_ coordinates: GeoCoordinates)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-geocoordinates">GeoCoordinates</a>

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
  <td><code> </code><em><code>coordinates</code></em><code> </code></td>
  <td><div>
  <p>GeoCoordinates to construct GeoCoordinatesUpdate.</p>
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

<div id="sdk-for-ios-navigate-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

