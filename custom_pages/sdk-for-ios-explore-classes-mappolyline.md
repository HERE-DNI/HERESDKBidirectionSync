---
title: "MapPolyline Class Reference"
slug: "sdk-for-ios-explore-classes-mappolyline"
---

# MapPolyline

<div class="declaration">

<div class="language">

``` highlight
public class MapPolyline
```

``` highlight
extension MapPolyline: NativeBase
```

``` highlight
extension MapPolyline: Hashable
```

</div>

</div>

A visual representation of a line on the map.

The geometry to be visualized is represented by an instance of <a href="sdk-for-ios-explore-structs-geopolyline">`GeoPolyline`</a>.

Altitude component of <a href="sdk-for-ios-explore-structs-geopolyline">`GeoPolyline`</a>‘s vertices is ignored.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11MapPolylineC8geometry14representationAcA03GeoC0V_AC14RepresentationCtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-geometry-representation" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mappolyline#sdk-for-ios-explore-s-7heresdk11MapPolylineC8geometry14representationAcA03GeoC0V_AC14RepresentationCtcfc" class="token"><code>init(geometry:</code><wbr></wbr><code>representation:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new `MapPolyline` instance with a specified visual representation.

  Altitude component of <a href="sdk-for-ios-explore-structs-geopolyline">`GeoPolyline`</a>‘s vertices is ignored.

  After creating a `MapPolyline` with this representation, the deprecated `MapPolyline` properties do not work and any change to them will be ignored. Any modifications to polyline’s appearance must be done with <a href="sdk-for-ios-explore-classes-mappolyline#sdk-for-ios-explore-s-7heresdk11MapPolylineC17setRepresentationyyAC0E0CF">`MapPolyline.setRepresentation(...)`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(geometry: GeoPolyline, representation: MapPolyline.Representation)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geopolyline">GeoPolyline</a>
  - <a href="sdk-for-ios-explore-classes-mappolyline-representation">Representation</a>

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
  <p>The list of vertices representing the polyline.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>representation</code></em><code> </code></td>
  <td><div>
  <p>The styling properties of the polyline.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11MapPolylineC8geometryAA03GeoC0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-geometry" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mappolyline#sdk-for-ios-explore-s-7heresdk11MapPolylineC8geometryAA03GeoC0Vvp" class="token"><code>geometry</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of vertices that represent the geometry of the polyline. Altitude component of <a href="sdk-for-ios-explore-structs-geopolyline">`GeoPolyline`</a>‘s vertices is ignored.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var geometry: GeoPolyline { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geopolyline">GeoPolyline</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11MapPolylineC8metadataAA8MetadataCSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-metadata" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mappolyline#sdk-for-ios-explore-s-7heresdk11MapPolylineC8metadataAA8MetadataCSgvp" class="token"><code>metadata</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The <a href="sdk-for-ios-explore-classes-metadata">`Metadata`</a> instance attached to this polyline. This will be `nil` if nothing has been attached before.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var metadata: Metadata? { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-metadata">Metadata</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11MapPolylineC9drawOrders5Int32Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-drawOrder" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mappolyline#sdk-for-ios-explore-s-7heresdk11MapPolylineC9drawOrders5Int32Vvp" class="token"><code>drawOrder</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The draw order of the polyline. Polylines with a higher draw order are drawn on top of polylines with a lower draw order.

  In case multiple polylines have the same draw order, they can be rendered in different ways depending on the <a href="sdk-for-ios-explore-classes-mappolyline#sdk-for-ios-explore-s-7heresdk11MapPolylineC13drawOrderTypeAA04DraweF0Ovp">`MapPolyline.drawOrderType`</a> set.

  The value is clamped to the range \[0; 1023\]. The default draw order is 0.

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

   <span id="sdk-for-ios-explore-s-7heresdk11MapPolylineC13drawOrderTypeAA04DraweF0Ovp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-drawOrderType" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mappolyline#sdk-for-ios-explore-s-7heresdk11MapPolylineC13drawOrderTypeAA04DraweF0Ovp" class="token"><code>drawOrderType</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The draw order type of the polyline. The default value is <a href="sdk-for-ios-explore-enums-drawordertype#sdk-for-ios-explore-s-7heresdk13DrawOrderTypeO016mapSceneAdditionC9DependentyA2CmF">`DrawOrderType.mapSceneAdditionOrderDependent`</a>.

  For <a href="sdk-for-ios-explore-enums-drawordertype#sdk-for-ios-explore-s-7heresdk13DrawOrderTypeO016mapSceneAdditionC9DependentyA2CmF">`DrawOrderType.mapSceneAdditionOrderDependent`</a>, map polylines with outlines having the same draw order are drawn as a whole in the order of addition to a map scene. There is no possibility that parts of another polyline, regardless of its draw order value, are drawn between outline and mainline of another polyline.

  With <a href="sdk-for-ios-explore-enums-drawordertype#sdk-for-ios-explore-s-7heresdk13DrawOrderTypeO016mapSceneAdditionC9DependentyA2CmF">`DrawOrderType.mapSceneAdditionOrderDependent`</a> polylines are rendered one by one. For <a href="sdk-for-ios-explore-enums-drawordertype#sdk-for-ios-explore-s-7heresdk13DrawOrderTypeO016mapSceneAdditionC11IndependentyA2CmF">`DrawOrderType.mapSceneAdditionOrderIndependent`</a> for multiple polylines with outlines having the same draw order, all outlines are rendered first in an arbitrary order and then all mainlines are drawn on top of those polylines in an arbitrary order.

  <a href="sdk-for-ios-explore-enums-drawordertype#sdk-for-ios-explore-s-7heresdk13DrawOrderTypeO016mapSceneAdditionC11IndependentyA2CmF">`DrawOrderType.mapSceneAdditionOrderIndependent`</a> allows speeding up the rendering process and keeping high frame rates when many similar polylines (with same styling attributes and <a href="sdk-for-ios-explore-classes-mappolyline-representation">`MapPolyline.Representation`</a>) are present in a map scene.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var drawOrderType: DrawOrderType { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-drawordertype">DrawOrderType</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11MapPolylineC16visibilityRangesSayAA0B12MeasureRangeVGvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-visibilityRanges" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mappolyline#sdk-for-ios-explore-s-7heresdk11MapPolylineC16visibilityRangesSayAA0B12MeasureRangeVGvp" class="token"><code>visibilityRanges</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of visibility ranges. The map polyline is visible only inside these map measure ranges. A range is half open - \<a href="sdk-for-ios-explore-structs-mapmeasurerange">minimumZoomLevel, maximumZoomLevel), the given maximum value is not contained in the range.

  When empty (the default), the map polyline is visible without map measure restrictions. Only [`MapMeasureRange`</a>(s) of <a href="sdk-for-ios-explore-structs-mapmeasure-kind#sdk-for-ios-explore-s-7heresdk10MapMeasureV4KindO9zoomLevelyA2EmF">`MapMeasure.Kind.zoomLevel`</a> type are supported. <a href="sdk-for-ios-explore-structs-mapmeasurerange">`MapMeasureRange`</a>(s) of other unsupported types will be ignored.

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

  - <a href="sdk-for-ios-explore-structs-mapmeasurerange">MapMeasureRange</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11MapPolylineC8progressSdvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-progress" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mappolyline#sdk-for-ios-explore-s-7heresdk11MapPolylineC8progressSdvp" class="token"><code>progress</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The progress from the polyline’s starting point, as a ratio of its total length clamped to the range \[0, 1\]. As the progress varies, the equivalent part of the polyline gets covered by the progress color and progress outline color. The rest of the polyline until its end point retains the line color and outline color along with an optional dash pattern.

  The default progress is 0.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var progress: Double { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11MapPolylineC13progressColorSo7UIColorCvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-progressColor" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mappolyline#sdk-for-ios-explore-s-7heresdk11MapPolylineC13progressColorSo7UIColorCvp" class="token"><code>progressColor</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The color used for the progress part of the polyline. The default progress color is opaque white.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var progressColor: UIColor { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11MapPolylineC20progressOutlineColorSo7UIColorCvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-progressOutlineColor" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mappolyline#sdk-for-ios-explore-s-7heresdk11MapPolylineC20progressOutlineColorSo7UIColorCvp" class="token"><code>progressOutlineColor</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The color used for outline of the progress part of the polyline. The default progress color is opaque white.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var progressOutlineColor: UIColor { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11MapPolylineC22progressGradientLengthAA0B26MeasureDependentRenderSizeVvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-progressGradientLength" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mappolyline#sdk-for-ios-explore-s-7heresdk11MapPolylineC22progressGradientLengthAA0B26MeasureDependentRenderSizeVvp" class="token"><code>progressGradientLength</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The maximum gradient length between `MapPolyline.lineColor' and 'MapPolyline.progressColor` in zoom level dependent pixels. To achieve a constant gradient length, use <a href="sdk-for-ios-explore-structs-mapmeasuredependentrendersize">`MapMeasureDependentRenderSize`</a> with a single value. To achieve a gradient length dependent on map zoom, use <a href="sdk-for-ios-explore-structs-mapmeasuredependentrendersize">`MapMeasureDependentRenderSize`</a> with multiple values. The default value is a constant gradient length of zero pixels. The gradient is guaranteed to fit into polyline, i.e. the actual gradient can be shorter then `progressGradientLength`.

  For <a href="sdk-for-ios-explore-structs-mapmeasure-kind">`MapMeasure.Kind`</a> only <a href="sdk-for-ios-explore-structs-mapmeasure-kind#sdk-for-ios-explore-s-7heresdk10MapMeasureV4KindO9zoomLevelyA2EmF">`MapMeasure.Kind.zoomLevel`</a> is supported. For <a href="sdk-for-ios-explore-structs-rendersize-unit">`RenderSize.Unit`</a> only <a href="sdk-for-ios-explore-structs-rendersize-unit#sdk-for-ios-explore-s-7heresdk10RenderSizeV4UnitO6pixelsyA2EmF">`RenderSize.Unit.pixels`</a> is supported. When setting the attribute with with unsupported values, the operation is ignored.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var progressGradientLength: MapMeasureDependentRenderSize { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11MapPolylineC27mapContentCategoriesToBlockSayAA0bE8CategoryOGvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-mapContentCategoriesToBlock" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mappolyline#sdk-for-ios-explore-s-7heresdk11MapPolylineC27mapContentCategoriesToBlockSayAA0bE8CategoryOGvp" class="token"><code>mapContentCategoriesToBlock</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of map content categories this polyline should block. Map content categories overlapping the polyline geometry (progress and non-progress) will be discarded from being rendered.

  Duplicate entries will be ignored and will have no additional effect.

  Default value is an empty list meaning none of the map categories will be blocked.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var mapContentCategoriesToBlock: [MapContentCategory] { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-mapcontentcategory">MapContentCategory</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11MapPolylineC14RepresentationC"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Class-Representation" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mappolyline#sdk-for-ios-explore-s-7heresdk11MapPolylineC14RepresentationC" class="token"><code>Representation</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Base class to represent the visual appearance of a <a href="sdk-for-ios-explore-classes-mappolyline">`MapPolyline`</a>.

  <a href="sdk-for-ios-explore-classes-mappolyline-representation" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class Representation : MapItemRepresentation
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-maps#sdk-for-ios-explore-s-7heresdk21MapItemRepresentationC">MapItemRepresentation</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11MapPolylineC23DashImageRepresentationC"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Class-DashImageRepresentation" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mappolyline#sdk-for-ios-explore-s-7heresdk11MapPolylineC23DashImageRepresentationC" class="token"><code>DashImageRepresentation</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents a dash pattern for the map polyline consisting of images rendered with certain gaps from each other.

  This dash pattern representation consists only of images rendered at certain points along the polyline. For rendering them without any distortions, polyline gets sliced into series of straight segments that are multiple of sum of dash and gap lengths. For this reason, the new polyline geometry might not align fully with original geometry.

  The <a href="sdk-for-ios-explore-classes-mappolyline-dashimagerepresentation#sdk-for-ios-explore-s-7heresdk11MapPolylineC23DashImageRepresentationC04dashE0AA0bE0Cvp">`MapPolyline.DashImageRepresentation.dashImage`</a> is stretched according to <a href="sdk-for-ios-explore-classes-mappolyline-dashimagerepresentation#sdk-for-ios-explore-s-7heresdk11MapPolylineC23DashImageRepresentationC10dashLengthAA0B26MeasureDependentRenderSizeVvp">`MapPolyline.DashImageRepresentation.dashLength`</a> and <a href="sdk-for-ios-explore-classes-mappolyline-dashimagerepresentation#sdk-for-ios-explore-s-7heresdk11MapPolylineC23DashImageRepresentationC9dashWidthAA0B26MeasureDependentRenderSizeVvp">`MapPolyline.DashImageRepresentation.dashWidth`</a>, with image’s width matched to `dashLength` and image’s height matched to `dashWidth`. The image is oriented so that its bottom is on the left-hand side between vertices `n` and `n+1`.

  The spacing between images is specified by <a href="sdk-for-ios-explore-classes-mappolyline-dashimagerepresentation#sdk-for-ios-explore-s-7heresdk11MapPolylineC23DashImageRepresentationC9gapLengthAA0B26MeasureDependentRenderSizeVvp">`MapPolyline.DashImageRepresentation.gapLength`</a>.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-classes-mappolyline-dashimagerepresentation" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class DashImageRepresentation : MapPolyline.Representation
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mappolyline">MapPolyline</a>
  - <a href="sdk-for-ios-explore-classes-mappolyline-representation">Representation</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11MapPolylineC19SolidRepresentationC"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Class-SolidRepresentation" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mappolyline#sdk-for-ios-explore-s-7heresdk11MapPolylineC19SolidRepresentationC" class="token"><code>SolidRepresentation</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Representation for a solid line without outline.

  Can represent polylines that have constant width or width dependent on the map zoom.

  To achieve constant width lines, use <a href="sdk-for-ios-explore-structs-mapmeasuredependentrendersize">`MapMeasureDependentRenderSize`</a> with a single value.

  To achieve line width dependent on map zoom, use <a href="sdk-for-ios-explore-structs-mapmeasuredependentrendersize">`MapMeasureDependentRenderSize`</a> with multiple values.

  For <a href="sdk-for-ios-explore-structs-mapmeasure-kind">`MapMeasure.Kind`</a> only <a href="sdk-for-ios-explore-structs-mapmeasure-kind#sdk-for-ios-explore-s-7heresdk10MapMeasureV4KindO9zoomLevelyA2EmF">`MapMeasure.Kind.zoomLevel`</a> is supported.

  For <a href="sdk-for-ios-explore-structs-rendersize-unit">`RenderSize.Unit`</a> only <a href="sdk-for-ios-explore-structs-rendersize-unit#sdk-for-ios-explore-s-7heresdk10RenderSizeV4UnitO6pixelsyA2EmF">`RenderSize.Unit.pixels`</a> is supported.

  <a href="sdk-for-ios-explore-classes-mappolyline-solidrepresentation" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class SolidRepresentation : MapPolyline.Representation
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mappolyline">MapPolyline</a>
  - <a href="sdk-for-ios-explore-classes-mappolyline-representation">Representation</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11MapPolylineC18DashRepresentationC"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Class-DashRepresentation" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mappolyline#sdk-for-ios-explore-s-7heresdk11MapPolylineC18DashRepresentationC" class="token"><code>DashRepresentation</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents a dash pattern for map polyline where the dash can be rendered as a colored line and the gap can be either empty or colored.

  The length of the dash and gap are set independently, allowing for patterns like `' — — — —'` (dash length = gap length) or `' ——— ——— ———'` (dash length != gap length).

  <a href="sdk-for-ios-explore-classes-mappolyline-dashrepresentation" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class DashRepresentation : MapPolyline.Representation
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mappolyline">MapPolyline</a>
  - <a href="sdk-for-ios-explore-classes-mappolyline-representation">Representation</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11MapPolylineC29SolidMultiColorRepresentationC"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Class-SolidMultiColorRepresentation" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mappolyline#sdk-for-ios-explore-s-7heresdk11MapPolylineC29SolidMultiColorRepresentationC" class="token"><code>SolidMultiColorRepresentation</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Representation allows map polyline to be colored in multiple specified color segments.

  Color segment is defined by color stops. Color stop is specified as a polyline length ratio (0.0 - start of the polyline, 1.0 - end of the polyline). Color stop represents a color change starting at that exact point up until either the next color stop (if one exists) or the end of the polyline.

  Progress color <a href="sdk-for-ios-explore-classes-mappolyline#sdk-for-ios-explore-s-7heresdk11MapPolylineC13progressColorSo7UIColorCvp">`MapPolyline.progressColor`</a> overrides any of the multiple color.

  Examples: The following configuration will color map polyline as follows:

  - from the start to the middle of it at the 0.5 point - in Red
  - from the middle point 0.5 to the 0.7 point - in Green
  - from 0.7 to 1.0 - in Red ‘colorStops: {0.0, 0.5, 0.7}, colorIndices: {0, 1, 0}, colors: {Red, Green}’

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-explore-classes-mappolyline-solidmulticolorrepresentation" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class SolidMultiColorRepresentation : MapPolyline.Representation
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mappolyline">MapPolyline</a>
  - <a href="sdk-for-ios-explore-classes-mappolyline-representation">Representation</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11MapPolylineC17setRepresentationyyAC0E0CF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-setRepresentation-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mappolyline#sdk-for-ios-explore-s-7heresdk11MapPolylineC17setRepresentationyyAC0E0CF" class="token"><code>setRepresentation(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Changes the appearance of the `MapPolyline` instance.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setRepresentation(_ representation: MapPolyline.Representation)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mappolyline-representation">Representation</a>

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
  <td><code> </code><em><code>representation</code></em><code> </code></td>
  <td><div>
  <p>The representation describing a new appearance of the <code>MapPolyline</code>.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11MapPolylineC14startAnimation_17animationDelegateyAA0bcE0C_AA0eG0_ptF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-startAnimation-_-animationDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mappolyline#sdk-for-ios-explore-s-7heresdk11MapPolylineC14startAnimation_17animationDelegateyAA0bcE0C_AA0eG0_ptF" class="token"><code>startAnimation(_:</code><wbr></wbr><code>animationDelegate:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Starts an animation of this map polyline.

  The <a href="sdk-for-ios-explore-classes-mappolylineanimation">`MapPolylineAnimation`</a> may be shared between multiple instances of `MapPolyline`.

  Starting animation on one polyline does not influence any ongoing animations on other polylines. Any ongoing animation of this map polyline will get cancelled.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func startAnimation(_ animation: MapPolylineAnimation, animationDelegate: AnimationDelegate)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mappolylineanimation">MapPolylineAnimation</a>
  - <a href="sdk-for-ios-explore-protocols-animationdelegate">AnimationDelegate</a>

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
  <td><code> </code><em><code>animation</code></em><code> </code></td>
  <td><div>
  <p>The animation to start.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>animationDelegate</code></em><code> </code></td>
  <td><div>
  <p>The delegate to receive notifications about animation start, completion or cancellation.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11MapPolylineC15cancelAnimationyyAA0bcE0CF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-cancelAnimation-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mappolyline#sdk-for-ios-explore-s-7heresdk11MapPolylineC15cancelAnimationyyAA0bcE0CF" class="token"><code>cancelAnimation(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Cancels single ongoing animation of this map polyline.

  Does nothing if the specified animation is not currently in progress for this polyline. Does not affect other polylines that might be running this animation.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func cancelAnimation(_ animation: MapPolylineAnimation)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mappolylineanimation">MapPolylineAnimation</a>

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
  <td><code> </code><em><code>animation</code></em><code> </code></td>
  <td><div>
  <p>The animation to cancel</p>
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

