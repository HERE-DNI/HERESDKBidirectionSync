---
title: "GeoCoordinates Structure Reference"
slug: "sdk-for-ios-navigate-structs-geocoordinates"
---

# GeoCoordinates

<div class="declaration">

<div class="language">

``` highlight
public struct GeoCoordinates : Hashable
```

</div>

</div>

Represents geographical coordinates in 3D space.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14GeoCoordinatesV8latitudeSdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-latitude" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-geocoordinates#sdk-for-ios-navigate-s-7heresdk14GeoCoordinatesV8latitudeSdvp" class="token"><code>latitude</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Latitude in degrees.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public let latitude: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14GeoCoordinatesV9longitudeSdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-longitude" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-geocoordinates#sdk-for-ios-navigate-s-7heresdk14GeoCoordinatesV9longitudeSdvp" class="token"><code>longitude</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Longitude in degrees.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public let longitude: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14GeoCoordinatesV8altitudeSdSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-altitude" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-geocoordinates#sdk-for-ios-navigate-s-7heresdk14GeoCoordinatesV8altitudeSdSgvp" class="token"><code>altitude</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Optional altitude in meters. By convention, on iOS devices, altitude is set as meters relative to the mean sea level. On Android devices, altitude is set as meters relative to the WGS 84 reference ellipsoid.

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

   <span id="sdk-for-ios-navigate-s-7heresdk14GeoCoordinatesV8latitude9longitude8altitudeACSd_S2dtcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-latitude-longitude-altitude" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-geocoordinates#sdk-for-ios-navigate-s-7heresdk14GeoCoordinatesV8latitude9longitude8altitudeACSd_S2dtcfc" class="token"><code>init(latitude:</code><wbr></wbr><code>longitude:</code><wbr></wbr><code>altitude:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs a GeoCoordinates from the provided latitude, longitude and altitude values. Corrects values of lat and long if they exceed the ranges.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(latitude: Double, longitude: Double, altitude: Double)
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
  <p>Latitude in degrees. Positive value means Northern hemisphere. If the value is out of range of [-90.0, 90.0] it’s clamped to that range. NaN value is converted to 0.0.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>longitude</code></em><code> </code></td>
  <td><div>
  <p>Longitude in degrees. Positive value means Eastern hemisphere. If the value is out of range of [-180.0, 180.0] it’s replaced with a value within the range, representing effectively the same meridian. NaN value is converted to 0.0.</p>
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

   <span id="sdk-for-ios-navigate-s-7heresdk14GeoCoordinatesV8latitude9longitudeACSd_Sdtcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-latitude-longitude" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-geocoordinates#sdk-for-ios-navigate-s-7heresdk14GeoCoordinatesV8latitude9longitudeACSd_Sdtcfc" class="token"><code>init(latitude:</code><wbr></wbr><code>longitude:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs a GeoCoordinates from the provided latitude and longitude values. Corrects values of latitude and longitude if they exceed the ranges. Altitude set to `nil`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(latitude: Double, longitude: Double)
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
  <p>Latitude in degrees. Positive value means Northern hemisphere. If the value is out of range of [-90.0, 90.0] it’s clamped to that range. NaN value is converted to 0.0.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>longitude</code></em><code> </code></td>
  <td><div>
  <p>Longitude in degrees. Positive value means Eastern hemisphere. If the value is out of range of [-180.0, 180.0] it’s replaced with a value within the range, representing effectively the same meridian. NaN value is converted to 0.0.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14GeoCoordinatesV8distance2toSdAC_tF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-distance-to" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-geocoordinates#sdk-for-ios-navigate-s-7heresdk14GeoCoordinatesV8distance2toSdAC_tF" class="token"><code>distance(to:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Computes distance (in meters) along the great circle between two coordinates. This method ignores altitude of both points.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func distance(to point: GeoCoordinates) -> Double
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
  <td><code> </code><em><code>point</code></em><code> </code></td>
  <td><div>
  <p>Coordinates of the point to which the distance is computed.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  distance in meters.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14GeoCoordinatesV11interpolate6toward2byA2C_SdtF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-interpolate-toward-by" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-geocoordinates#sdk-for-ios-navigate-s-7heresdk14GeoCoordinatesV11interpolate6toward2byA2C_SdtF" class="token"><code>interpolate(toward:</code><wbr></wbr><code>by:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Computes the coordinates of the interpolated location along the great circle between the two coordinates.

  The interpolation factor is clamped to the range `[0.0, 1.0]` where `0.0` identifies this `GeoCoordinates` and `1.0` indicates the other coordinates.

  The ratio between the distance to the interpolated coordinates and the distance to the other coordinates is approximately equal to the interpolation factor. When both coordinates have the altitude, then the altitude is interpolated as well; `nil` otherwise.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func interpolate(toward towardCoords: GeoCoordinates, by factor: Double) -> GeoCoordinates
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
  <td><code> </code><em><code>towardCoords</code></em><code> </code></td>
  <td><div>
  <p>Coordinates of the point to which the interpolation is directed.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>factor</code></em><code> </code></td>
  <td><div>
  <p>The interpolation factor</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  interpolated coordinates

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14GeoCoordinatesV10fromString5inputACSgSS_tFZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-fromString-input" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-geocoordinates#sdk-for-ios-navigate-s-7heresdk14GeoCoordinatesV10fromString5inputACSgSS_tFZ" class="token"><code>fromString(input:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs GeoCoordinates from the provided string in specified format. Corrects values of lat and long if they exceed the ranges. If the latitude value is out of range of \[-90.0, 90.0\] it’s clamped to that range. If the longitude value is out of range of \[-180.0, 180.0\] it’s replaced with a value within the range, representing effectively the same meridian. Examples: `53.43762,-13.65468`. `49°59'56.948"N, 15°48'22.989"E` `50d4m17.698N 14d24m2.826E` `49.9991522N, 150.8063858E` `40°26′47″N 79°58′36″W`

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func fromString(input: String) -> GeoCoordinates?
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
  <td><code> </code><em><code>input</code></em><code> </code></td>
  <td><div>
  <p>String representing GeoCoordinates in one of supported formats.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Created GeoCoordinates, or ‘null’ if string was not in appropriate format.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14GeoCoordinatesV2eeoiySbAC_ACtFZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-_-_" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-geocoordinates#sdk-for-ios-navigate-s-7heresdk14GeoCoordinatesV2eeoiySbAC_ACtFZ" class="token"><code>==(_:</code><wbr></wbr><code>_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Undocumented

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  static func == (lhs: GeoCoordinates, rhs: GeoCoordinates) -> Bool
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

