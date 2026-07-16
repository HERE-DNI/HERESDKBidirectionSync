---
title: "MapArrow Class Reference"
slug: "sdk-for-ios-navigate-classes-maparrow"
---

# MapArrow

<div class="declaration">

<div class="language">

``` highlight
public class MapArrow
```

``` highlight
extension MapArrow: NativeBase
```

``` highlight
extension MapArrow: Hashable
```

</div>

</div>

A visual representation of an arrow on the map. It consists of a tail - a polyline with an arbitrary number of points - and a head at its end.

The map arrows are only visible on zoom levels \>= 13.

Altitude component of <a href="sdk-for-ios-navigate-structs-geopolyline">`GeoPolyline`</a>‘s vertices is ignored.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8MapArrowC8geometry13widthInPixels5colorAcA11GeoPolylineV_SdSo7UIColorCtcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-geometry-widthInPixels-color" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-maparrow#sdk-for-ios-navigate-s-7heresdk8MapArrowC8geometry13widthInPixels5colorAcA11GeoPolylineV_SdSo7UIColorCtcfc" class="token"><code>init(geometry:</code><wbr></wbr><code>widthInPixels:</code><wbr></wbr><code>color:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new `MapArrow` instance.

  Altitude component of <a href="sdk-for-ios-navigate-structs-geopolyline">`GeoPolyline`</a>‘s vertices is ignored.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(geometry: GeoPolyline, widthInPixels: Double, color: UIColor)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-geopolyline">GeoPolyline</a>

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
  <td><code> </code><em><code>geometry</code></em><code> </code></td>
  <td><div>
  <p>The geometry of the arrow tail. The last coordinate in the list defines the position where the head of the arrow is located.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>widthInPixels</code></em><code> </code></td>
  <td><div>
  <p>The width of the arrow tail in pixel. Negative values are clamped to 0. The tip is scaled accordingly.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>color</code></em><code> </code></td>
  <td><div>
  <p>The color of the arrow. The alpha channel is ignored, the color is interpreted as fully opaque.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8MapArrowC25measureDependentTailWidthSDyAA0B7MeasureVSdGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-measureDependentTailWidth" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-maparrow#sdk-for-ios-navigate-s-7heresdk8MapArrowC25measureDependentTailWidthSDyAA0B7MeasureVSdGvp" class="token"><code>measureDependentTailWidth</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The width of the arrow tail in pixels, where the key is a <a href="sdk-for-ios-navigate-structs-mapmeasure">`MapMeasure`</a> and the value is a tail width in pixels at this <a href="sdk-for-ios-navigate-structs-mapmeasure">`MapMeasure`</a>. The width values are linearly interpolated between nearest dictionary entries. Width values for <a href="sdk-for-ios-navigate-structs-mapmeasure">`MapMeasure`</a> outside the dictionary entries are kept constant, using the value of the largest/smallest key.

  Only <a href="sdk-for-ios-navigate-structs-mapmeasure">`MapMeasure`</a> of <a href="sdk-for-ios-navigate-structs-mapmeasure-kind#sdk-for-ios-navigate-s-7heresdk10MapMeasureV4KindO9zoomLevelyA2EmF">`MapMeasure.Kind.zoomLevel`</a> type is supported. Other <a href="sdk-for-ios-navigate-structs-mapmeasure">`MapMeasure`</a> types are unsupported and hence, will be ignored.

  `measureDependentTailWidth` with a single entry is equivalent to the use of the `widthInPixels` value in the constructor, so a constant width setting, independent of camera.

  Empty `measureDependentTailWidth` is ignored and existing width is maintained.

  The width values should be positive. Dictionary entries with width values less than or equal to 0 are ignored.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var measureDependentTailWidth: [MapMeasure : Double] { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-mapmeasure">MapMeasure</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8MapArrowC16visibilityRangesSayAA0B12MeasureRangeVGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-visibilityRanges" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-maparrow#sdk-for-ios-navigate-s-7heresdk8MapArrowC16visibilityRangesSayAA0B12MeasureRangeVGvp" class="token"><code>visibilityRanges</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of visibility ranges, in which the map arrow is visible. A range is half-open - \<a href="sdk-for-ios-navigate-structs-mapmeasurerange">minimumZoomLevel, maximumZoomLevel), the given maximum value is not contained in the range.

  When empty (the default), the map arrows are visible without map measure restrictions. Only [`MapMeasureRange`</a>(s) of <a href="sdk-for-ios-navigate-structs-mapmeasure-kind#sdk-for-ios-navigate-s-7heresdk10MapMeasureV4KindO9zoomLevelyA2EmF">`MapMeasure.Kind.zoomLevel`</a> type are supported. <a href="sdk-for-ios-navigate-structs-mapmeasurerange">`MapMeasureRange`</a>(s) of other unsupported types will be ignored.}

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var visibilityRanges: [MapMeasureRange] { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-mapmeasurerange">MapMeasureRange</a>

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

