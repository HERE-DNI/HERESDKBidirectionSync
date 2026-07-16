---
title: "GeoPolyline Structure Reference"
slug: "sdk-for-ios-navigate-structs-geopolyline"
---

# GeoPolyline

<div class="declaration">

<div class="language">

``` highlight
public struct GeoPolyline : Hashable
```

</div>

</div>

A list of geographic coordinates representing the vertices of a polyline. An instance of this class, initialized with appropriate vertices. Represents a `GeoPolyline` as a series of geographic coordinates.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk11GeoPolylineV8verticesSayAA0B11CoordinatesVGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-vertices" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-geopolyline#sdk-for-ios-navigate-s-7heresdk11GeoPolylineV8verticesSayAA0B11CoordinatesVGvp" class="token"><code>vertices</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of vertices representing the polyline.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public let vertices: [GeoCoordinates]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-geocoordinates">GeoCoordinates</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk11GeoPolylineV8verticesACSayAA0B11CoordinatesVG_tKcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-vertices" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-geopolyline#sdk-for-ios-navigate-s-7heresdk11GeoPolylineV8verticesACSayAA0B11CoordinatesVG_tKcfc" class="token"><code>init(vertices:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs a GeoPolyline from the provided vertices. Throws an InstantiationError if the number of vertices is less than two.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-core#sdk-for-ios-navigate-s-7heresdk18InstantiationErrora">`InstantiationError`</a> Instantiation error.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(vertices: [GeoCoordinates]) throws
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
  <td><code> </code><em><code>vertices</code></em><code> </code></td>
  <td><div>
  <p>List of vertices representing the polyline.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk11GeoPolylineV6geoBoxAcA0bE0V_tcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-geoBox" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-geopolyline#sdk-for-ios-navigate-s-7heresdk11GeoPolylineV6geoBoxAcA0bE0V_tcfc" class="token"><code>init(geoBox:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Constructs an instance of this class from <a href="sdk-for-ios-navigate-structs-geobox">`GeoBox`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(geoBox: GeoBox)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-geobox">GeoBox</a>

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
  <td><code> </code><em><code>geoBox</code></em><code> </code></td>
  <td><div>
  <p>A rectangle defined by the <a href="sdk-for-ios-navigate-structs-geobox"><code>GeoBox</code></a> to be converted into <code>GeoPolyline</code>. The corner coordinates of the <a href="sdk-for-ios-navigate-structs-geobox"><code>GeoBox</code></a> will define the points of the resulting <code>GeoPolyline</code>.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk11GeoPolylineV17getNearestIndexTo5points6UInt32VAA0B11CoordinatesV_tF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-getNearestIndexTo-point" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-geopolyline#sdk-for-ios-navigate-s-7heresdk11GeoPolylineV17getNearestIndexTo5points6UInt32VAA0B11CoordinatesV_tF" class="token"><code>getNearestIndexTo(point:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Returns the index of the nearest vertex to the given point.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getNearestIndexTo(point: GeoCoordinates) -> UInt32
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
  <td><code> </code><em><code>point</code></em><code> </code></td>
  <td><div>
  <p>Coordinates of the point.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Index of the closest vertex of the polyline.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk11GeoPolylineV13coordinatesAt14offsetInMeters9directionAA0B11CoordinatesVSd_AA0bC9DirectionOtF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-coordinatesAt-offsetInMeters-direction" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-geopolyline#sdk-for-ios-navigate-s-7heresdk11GeoPolylineV13coordinatesAt14offsetInMeters9directionAA0B11CoordinatesVSd_AA0bC9DirectionOtF" class="token"><code>coordinatesAt(offsetInMeters:</code><wbr></wbr><code>direction:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Returns the coordinates at the given distance along the polyline. When the polyline is traversed from the beginning, the distance is calculated from the start of the polyline; while a direction from the end indicates a distance from the last vertex.

  The offset is expected to be non-negative and smaller than the length of the polyline. When the offset is negative, the function returns the starting end point of the polyline, i.e. the first vertex in positive direction and the last vertex in the negative direction. Similarly, when the offset is larger than the length of the polyline, then the function returns the opposite end point of the polyline.

  The distance between two consecutive vertices is calculated using the <a href="sdk-for-ios-navigate-structs-geocoordinates#sdk-for-ios-navigate-s-7heresdk14GeoCoordinatesV8distance2toSdAC_tF">`GeoCoordinates.distance(...)`</a> function. Therefore, it computes the distance (in meters) along the great circle between the two vertices. Similarly, the full length of the polyline is the sum of the distances between its vertices. The interpolation coordinates between two vertices is calculated using the <a href="sdk-for-ios-navigate-structs-geocoordinates#sdk-for-ios-navigate-s-7heresdk14GeoCoordinatesV11interpolate6toward2byA2C_SdtF">`GeoCoordinates.interpolate(...)`</a> function.

  Note: the result may different from the analogue result from other matching components since they may adapt the result to the length of the underlying object described by the polyline.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func coordinatesAt(offsetInMeters: Double, direction: GeoPolylineDirection) -> GeoCoordinates
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-geopolylinedirection">GeoPolylineDirection</a>
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
  <td><code> </code><em><code>offsetInMeters</code></em><code> </code></td>
  <td><div>
  <p>The distance along the polyline in meters</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>direction</code></em><code> </code></td>
  <td><div>
  <p>The direction in which the polyline is traversed.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The coordinates of the point at the given distance

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

