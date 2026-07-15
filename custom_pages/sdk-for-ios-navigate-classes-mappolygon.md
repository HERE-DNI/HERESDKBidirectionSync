---
title: "MapPolygon Class Reference"
slug: "sdk-for-ios-navigate-classes-mappolygon"
---

# MapPolygon

<div class="declaration">

<div class="language">

``` highlight
public class MapPolygon
```

``` highlight
extension MapPolygon: NativeBase
```

``` highlight
extension MapPolygon: Hashable
```

</div>

</div>

A visual representation of a polygon on the map. Can be used to visualize areas of all shapes and sizes.

The geometry to be visualized is represented by an instance of <a href="sdk-for-ios-navigate-structs-geopolygon">`GeoPolygon`</a>. To display circular areas (for example, a position accuracy indicator) use a GeoPolygon created from a <a href="sdk-for-ios-navigate-structs-geocircle">`GeoCircle`</a> using

    GeoPolygon.init(GeoCircle)

.
</p>

Note:

- The polygon shape should not cover more than half of the globe, otherwise unexpected results may occur.
- Polygons which are self-intersecting are not supported and may lead to render artifacts.
- The inner boundaries (holes) specified in the GeoPolygon are ignored.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

      init(geometry: color: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new MapPolygon instance with outline visualization disabled and containing the geometry passed in.

  The winding order of the vertices can be in clockwise or counter-clockwise order. It is recomended to provide the outer boundary ordered clockwise and closed.

  Note:

  - The polygon shape should not cover more than half of the globe, otherwise unexpected results may occur.
  - Polygons which are self-intersecting are not supported and may lead to render artifacts.
  - The inner boundaries (holes) specified in the GeoPolygon are ignored.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( geometry : GeoPolygon , color : UIColor )
  ```

  </pre>

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
  <td><code> </code><em><code>geometry</code></em><code> </code></td>
  <td><div>
  <p>The list of vertices representing the outer boundary of polygon.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>color</code></em><code> </code></td>
  <td><div>
  <p>The fill color for the polygon</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      init(geometry: color: outlineColor: outlineWidthInPixels: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new MapPolygon instance with outline visualization enabled and containing the geometry passed in.

  Transparent outlines are not supported. Any color with transparency (alpha value other than 1) will be rendered as fully opaque by interpreting the alpha value as 1.

  The winding order of the vertices can be in clockwise or counter-clockwise order. It is recomended to provide the outer boundary ordered clockwise and closed.

  Note:

  - The polygon shape should not cover more than half of the globe, otherwise unexpected results may occur.
  - Polygons which are self-intersecting are not supported and may lead to render artifacts.
  - The inner boundaries (holes) specified in the GeoPolygon are ignored.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( geometry : GeoPolygon , color : UIColor , outlineColor : UIColor , outlineWidthInPixels : Double )
  ```

  </pre>

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
  <td><code> </code><em><code>geometry</code></em><code> </code></td>
  <td><div>
  <p>The list of vertices representing the outer boundary of polygon.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>color</code></em><code> </code></td>
  <td><div>
  <p>The fill color for the polygon.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>outlineColor</code></em><code> </code></td>
  <td><div>
  <p>The color of the polygon outline, alpha channel is ignored and treated as 1.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>outlineWidthInPixels</code></em><code> </code></td>
  <td><div>
  <p>The width of the polygon outline (in pixels). Negative values are clamped to 0.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10MapPolygonC8geometryAA03GeoC0Vvp"></span>` `<span id="//apple_ref/swift/Property/geometry" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-mappolygon#/s:7heresdk10MapPolygonC8geometryAA03GeoC0Vvp" class="token"><code>geometry</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The geometry of the polygon. Setting a new geometry will update the appearance. The winding order of the vertices can be in clockwise or counter-clockwise order. It is recomended to provide the outer boundary ordered clockwise and closed.

  Note:

  - The polygon shape should not cover more than half of the globe, otherwise unexpected results may occur.
  - Polygons which are self-intersecting are not supported and may lead to render artifacts.
  - The inner boundaries (holes) specified in the GeoPolygon are ignored.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var geometry: GeoPolygon { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10MapPolygonC8metadataAA8MetadataCSgvp"></span>` `<span id="//apple_ref/swift/Property/metadata" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-mappolygon#/s:7heresdk10MapPolygonC8metadataAA8MetadataCSgvp" class="token"><code>metadata</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The Metadata instance attached to this polygon, `nil` by default.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var metadata: Metadata? { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10MapPolygonC9fillColorSo7UIColorCvp"></span>` `<span id="//apple_ref/swift/Property/fillColor" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-mappolygon#/s:7heresdk10MapPolygonC9fillColorSo7UIColorCvp" class="token"><code>fillColor</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Color of the polygon’s fill. Fully transparent color (alpha set to 0) disables the fill completely.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var fillColor: UIColor { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10MapPolygonC9drawOrders5Int32Vvp"></span>` `<span id="//apple_ref/swift/Property/drawOrder" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-mappolygon#/s:7heresdk10MapPolygonC9drawOrders5Int32Vvp" class="token"><code>drawOrder</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The draw order of this map polygon relative to other map polygons. Polygons with higher draw order value are drawn on top of polygons with lower draw order.

  In case multiple polygons have the same draw order value then the order in which they were added to the scene matters. Last added polygon is drawn on top.

  Allowed range is 0-1023. Values outside this range will be clamped. Default value is 0.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var drawOrder: Int32 { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10MapPolygonC16visibilityRangesSayAA0B12MeasureRangeVGvp"></span>` `<span id="//apple_ref/swift/Property/visibilityRanges" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-mappolygon#/s:7heresdk10MapPolygonC16visibilityRangesSayAA0B12MeasureRangeVGvp" class="token"><code>visibilityRanges</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of visibility ranges. The map polygon is visible only inside these map measure ranges. A range is half open - \<a href="sdk-for-ios-navigate-classes-s">minimumZoomLevel, maximumZoomLevel), the given maximum value is not contained in the range.

  When empty (the default), the map polygon is visible without map measure restrictions. Only [MapMeasureRange</a> of <a href="sdk-for-ios-navigate-structs-mapmeasure-kind#/s:7heresdk10MapMeasureV4KindO9zoomLevelyA2EmF">`MapMeasure.Kind.zoomLevel`</a> type are supported. <a href="sdk-for-ios-navigate-classes-s">MapMeasureRange</a> of other unsupported types will be ignored.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var visibilityRanges: [MapMeasureRange] { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10MapPolygonC12outlineColorSo7UIColorCvp"></span>` `<span id="//apple_ref/swift/Property/outlineColor" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-mappolygon#/s:7heresdk10MapPolygonC12outlineColorSo7UIColorCvp" class="token"><code>outlineColor</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The color of the polygon outline. The default outline color is opaque white.

  Transparent outlines are not supported. Any color with transparency (alpha value other than 1) will be rendered as fully opaque.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var outlineColor: UIColor { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk10MapPolygonC12outlineWidthSdvp"></span>` `<span id="//apple_ref/swift/Property/outlineWidth" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-mappolygon#/s:7heresdk10MapPolygonC12outlineWidthSdvp" class="token"><code>outlineWidth</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The width of the polygon outline in pixels. The value should be greater than or equal to zero. Negative values are clamped to zero.

  By default, the outline width is set to zero.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var outlineWidth: Double { get set }
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

