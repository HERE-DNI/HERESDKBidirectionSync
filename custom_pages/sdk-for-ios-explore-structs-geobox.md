---
title: "GeoBox Structure Reference"
slug: "sdk-for-ios-explore-structs-geobox"
---

# GeoBox

<div class="declaration">

<div class="language">

``` highlight
public struct GeoBox : Hashable
```

</div>

</div>

Represents a bounding rectangle aligned with latitude and longitude. Geographic area represented by this would be visualised as a rectangle when using a normal cylindrical projection (such as Mercator). The box has a maximum span of 360 degrees in longitude and 180 degrees in latitude direction. The box with equal values in longitude for the corners is considered as a span of 360 degrees. The box is considered empty if the latitude of the <a href="sdk-for-ios-explore-structs-geobox#sdk-for-ios-explore-s-7heresdk6GeoBoxV15southWestCornerAA0B11CoordinatesVvp">`GeoBox.southWestCorner`</a> is larger than the the latitude of the <a href="sdk-for-ios-explore-structs-geobox#sdk-for-ios-explore-s-7heresdk6GeoBoxV15northEastCornerAA0B11CoordinatesVvp">`GeoBox.northEastCorner`</a>.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk6GeoBoxV15southWestCornerAA0B11CoordinatesVvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-southWestCorner" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-geobox#sdk-for-ios-explore-s-7heresdk6GeoBoxV15southWestCornerAA0B11CoordinatesVvp" class="token"><code>southWestCorner</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  South west corner coordinates.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public let southWestCorner: GeoCoordinates
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geocoordinates">GeoCoordinates</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk6GeoBoxV15northEastCornerAA0B11CoordinatesVvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-northEastCorner" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-geobox#sdk-for-ios-explore-s-7heresdk6GeoBoxV15northEastCornerAA0B11CoordinatesVvp" class="token"><code>northEastCorner</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  North east corner coordinates.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public let northEastCorner: GeoCoordinates
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geocoordinates">GeoCoordinates</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk6GeoBoxV15southWestCorner09northEastF0AcA0B11CoordinatesV_AGtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-southWestCorner-northEastCorner" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-geobox#sdk-for-ios-explore-s-7heresdk6GeoBoxV15southWestCorner09northEastF0AcA0B11CoordinatesV_AGtcfc" class="token"><code>init(southWestCorner:</code><wbr></wbr><code>northEastCorner:</code><wbr></wbr><code>)</code></a> 

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
  public init(southWestCorner: GeoCoordinates, northEastCorner: GeoCoordinates)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geocoordinates">GeoCoordinates</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk6GeoBoxV10containing14geoCoordinatesACSgSayAA0bF0VG_tFZ"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-containing-geoCoordinates" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-geobox#sdk-for-ios-explore-s-7heresdk6GeoBoxV10containing14geoCoordinatesACSgSayAA0bF0VG_tFZ" class="token"><code>containing(geoCoordinates:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a `GeoBox` which encompases all coordinates from the list. The provided list must contain at least two points. The altitude values of the input coordinates are not considered for the result.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func containing(geoCoordinates: [GeoCoordinates]) -> GeoBox?
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
  <td><code> </code><em><code>geoCoordinates</code></em><code> </code></td>
  <td><div>
  <p>List of coordinates to encompass inside bounding box.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  `GeoBox` containing all supplied coordinates, or `nil` if less than two coordinates were provided.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk6GeoBoxV8envelope03geoC0A2C_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-envelope-geoBox" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-geobox#sdk-for-ios-explore-s-7heresdk6GeoBoxV8envelope03geoC0A2C_tF" class="token"><code>envelope(geoBox:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Envelopes two `GeoBox` areas by returning the smallest `GeoBox` covering both this GeoBox and the specified `GeoBox`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func envelope(geoBox: GeoBox) -> GeoBox
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
  <td><code> </code><em><code>geoBox</code></em><code> </code></td>
  <td><div>
  <p>Another <code>GeoBox</code> to envelope with.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  `GeoBox` covering two`GeoBox` areas

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk6GeoBoxV08envelopeB5Boxes03geoE0ACSgSayACG_tFZ"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-envelopeGeoBoxes-geoBoxes" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-geobox#sdk-for-ios-explore-s-7heresdk6GeoBoxV08envelopeB5Boxes03geoE0ACSgSayACG_tFZ" class="token"><code>envelopeGeoBoxes(geoBoxes:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Envelopes the list of `GeoBox` areas by returning the smallest `GeoBox` covering all specified `GeoBox` objects.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func envelopeGeoBoxes(geoBoxes: [GeoBox]) -> GeoBox?
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
  <td><code> </code><em><code>geoBoxes</code></em><code> </code></td>
  <td><div>
  <p>List of <code>GeoBox</code> objects.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  `GeoBox` covering all `GeoBox` areas, or `nil` if input is empty.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk6GeoBoxV10intersects03geoC0SbAC_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-intersects-geoBox" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-geobox#sdk-for-ios-explore-s-7heresdk6GeoBoxV10intersects03geoC0SbAC_tF" class="token"><code>intersects(geoBox:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Determines whether this `GeoBox` intersects with the passed `GeoBox`. The altitude values are ignored.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func intersects(geoBox: GeoBox) -> Bool
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
  <td><code> </code><em><code>geoBox</code></em><code> </code></td>
  <td><div>
  <p>A <code>GeoBox</code> to check for intersection.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  `true` if intersects with the `GeoBox, false` otherwise.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk6GeoBoxV12intersection03geoC0SayACGAC_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-intersection-geoBox" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-geobox#sdk-for-ios-explore-s-7heresdk6GeoBoxV12intersection03geoC0SayACGAC_tF" class="token"><code>intersection(geoBox:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Computes the intersection with the passed `GeoBox`. The altitude values are ignored. Limitation: Geo boxes are considered as non-intersecting if they overlap only on a single point, horizontal line or vertical line.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func intersection(geoBox: GeoBox) -> [GeoBox]
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
  <td><code> </code><em><code>geoBox</code></em><code> </code></td>
  <td><div>
  <p>Another geo box to check intersection with.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  It will be empty if there is no overlap. Otherwise, 1 or more geo boxes covering common area by this and passed `GeoBox`.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk6GeoBoxV12intersection8geoBoxesSayACGAF_tFZ"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-intersection-geoBoxes" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-geobox#sdk-for-ios-explore-s-7heresdk6GeoBoxV12intersection8geoBoxesSayACGAF_tFZ" class="token"><code>intersection(geoBoxes:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Computes intersection of list of `GeoBox` instances. The altitude values are ignored. Limitation: Geo boxes are considered as non-intersecting if they overlap only on a single point, horizontal line or vertical line.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func intersection(geoBoxes: [GeoBox]) -> [GeoBox]
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
  <td><code> </code><em><code>geoBoxes</code></em><code> </code></td>
  <td><div>
  <p>List of <code>GeoBox</code> instances.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  It will be empty if there is no overlap between all the passed `GeoBox` instances. Otherwise, 1 or more geo boxes covering common area by all the passed `GeoBox` instances.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk6GeoBoxV8contains03geoC0SbAC_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-contains-geoBox" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-geobox#sdk-for-ios-explore-s-7heresdk6GeoBoxV8contains03geoC0SbAC_tF" class="token"><code>contains(geoBox:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Determines whether the specified `GeoBox` is covered entirely by this `GeoBox`. The altitude values are ignored.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func contains(geoBox: GeoBox) -> Bool
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
  <td><code> </code><em><code>geoBox</code></em><code> </code></td>
  <td><div>
  <p>A <code>GeoBox</code> to check for containment within this <code>GeoBox</code>.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  `true` if covered by the `GeoBox, false` otherwise.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk6GeoBoxV8contains14geoCoordinatesSbAA0bF0V_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-contains-geoCoordinates" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-geobox#sdk-for-ios-explore-s-7heresdk6GeoBoxV8contains14geoCoordinatesSbAA0bF0V_tF" class="token"><code>contains(geoCoordinates:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Determines whether the specified GeoCoordinates is contained within this `GeoBox`. The altitude values are ignored.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func contains(geoCoordinates: GeoCoordinates) -> Bool
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
  <td><code> </code><em><code>geoCoordinates</code></em><code> </code></td>
  <td><div>
  <p>A GeoCoordinates to check for containment within this <code>GeoBox</code>.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  `true` if contained within the `GeoBox, false` otherwise.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk6GeoBoxV10expandedBy11southMeters04westG005northG004eastG0ACSd_S3dtKF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-expandedBy-southMeters-westMeters-northMeters-eastMeters" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-geobox#sdk-for-ios-explore-s-7heresdk6GeoBoxV10expandedBy11southMeters04westG005northG004eastG0ACSd_S3dtKF" class="token"><code>expandedBy(southMeters:</code><wbr></wbr><code>westMeters:</code><wbr></wbr><code>northMeters:</code><wbr></wbr><code>eastMeters:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a `GeoBox` which is expanded by a fixed distance. Throws an InstantiationError if it is not possible to create a valid `GeoBox` with the given arguments.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-explore-core#sdk-for-ios-explore-s-7heresdk18InstantiationErrora">`InstantiationError`</a> Instantiation error.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func expandedBy(southMeters: Double, westMeters: Double, northMeters: Double, eastMeters: Double) throws -> GeoBox
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
  <td><code> </code><em><code>southMeters</code></em><code> </code></td>
  <td><div>
  <p>Distance in the south direction in meters to expand the <code>GeoBox</code>.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>westMeters</code></em><code> </code></td>
  <td><div>
  <p>Distance in the west direction in meters to expand the <code>GeoBox</code>.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>northMeters</code></em><code> </code></td>
  <td><div>
  <p>Distance in the north direction in meters to expand the <code>GeoBox</code>.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>eastMeters</code></em><code> </code></td>
  <td><div>
  <p>Distance in the east direction in meters to expand the <code>GeoBox</code>.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The expanded `GeoBox`.

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

