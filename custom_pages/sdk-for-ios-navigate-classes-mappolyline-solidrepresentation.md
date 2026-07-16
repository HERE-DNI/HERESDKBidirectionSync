---
title: "SolidRepresentation Class Reference"
slug: "sdk-for-ios-navigate-classes-mappolyline-solidrepresentation"
---

# SolidRepresentation

<div class="declaration">

<div class="language">

``` highlight
public class SolidRepresentation : MapPolyline.Representation
```

</div>

Related types:

- <a href="sdk-for-ios-navigate-classes-mappolyline">MapPolyline</a>
- <a href="sdk-for-ios-navigate-classes-mappolyline-representation">Representation</a>

</div>

Representation for a solid line without outline.

Can represent polylines that have constant width or width dependent on the map zoom.

To achieve constant width lines, use <a href="sdk-for-ios-navigate-structs-mapmeasuredependentrendersize">`MapMeasureDependentRenderSize`</a> with a single value.

To achieve line width dependent on map zoom, use <a href="sdk-for-ios-navigate-structs-mapmeasuredependentrendersize">`MapMeasureDependentRenderSize`</a> with multiple values.

For <a href="sdk-for-ios-navigate-structs-mapmeasure-kind">`MapMeasure.Kind`</a> only <a href="sdk-for-ios-navigate-structs-mapmeasure-kind#sdk-for-ios-navigate-s-7heresdk10MapMeasureV4KindO9zoomLevelyA2EmF">`MapMeasure.Kind.zoomLevel`</a> is supported.

For <a href="sdk-for-ios-navigate-structs-rendersize-unit">`RenderSize.Unit`</a> only <a href="sdk-for-ios-navigate-structs-rendersize-unit#sdk-for-ios-navigate-s-7heresdk10RenderSizeV4UnitO6pixelsyA2EmF">`RenderSize.Unit.pixels`</a> is supported.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk11MapPolylineC19SolidRepresentationC9lineWidth5color8capShapeAeA0B26MeasureDependentRenderSizeV_So7UIColorCAA7LineCapOtKcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-lineWidth-color-capShape" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mappolyline-solidrepresentation#sdk-for-ios-navigate-s-7heresdk11MapPolylineC19SolidRepresentationC9lineWidth5color8capShapeAeA0B26MeasureDependentRenderSizeV_So7UIColorCAA7LineCapOtKcfc" class="token"><code>init(lineWidth:</code><wbr></wbr><code>color:</code><wbr></wbr><code>capShape:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a representation for a solid line without outline.

  At map measures smaller than smallest map measure in the <a href="sdk-for-ios-navigate-classes-mappolyline-solidrepresentation#sdk-for-ios-navigate-s-7heresdk11MapPolylineC19SolidRepresentationC9lineWidthAA0B26MeasureDependentRenderSizeVvp">`lineWidth`</a> line width is constant and equal to the width given for the smallest map measure in the <a href="sdk-for-ios-navigate-classes-mappolyline-solidrepresentation#sdk-for-ios-navigate-s-7heresdk11MapPolylineC19SolidRepresentationC9lineWidthAA0B26MeasureDependentRenderSizeVvp">`lineWidth`</a>.

  At map measures bigger than biggest map measure in the <a href="sdk-for-ios-navigate-classes-mappolyline-solidrepresentation#sdk-for-ios-navigate-s-7heresdk11MapPolylineC19SolidRepresentationC9lineWidthAA0B26MeasureDependentRenderSizeVvp">`lineWidth`</a> line width is constant and equal to the width given for the biggest map measure in the <a href="sdk-for-ios-navigate-classes-mappolyline-solidrepresentation#sdk-for-ios-navigate-s-7heresdk11MapPolylineC19SolidRepresentationC9lineWidthAA0B26MeasureDependentRenderSizeVvp">`lineWidth`</a>.

  At map measures between two nearest given map measures line width is linearly interpolated between width values given for these map measures.

  For <a href="sdk-for-ios-navigate-structs-mapmeasure-kind">`MapMeasure.Kind`</a> only <a href="sdk-for-ios-navigate-structs-mapmeasure-kind#sdk-for-ios-navigate-s-7heresdk10MapMeasureV4KindO9zoomLevelyA2EmF">`MapMeasure.Kind.zoomLevel`</a> is supported.

  For <a href="sdk-for-ios-navigate-structs-rendersize-unit">`RenderSize.Unit`</a> only <a href="sdk-for-ios-navigate-structs-rendersize-unit#sdk-for-ios-navigate-s-7heresdk10RenderSizeV4UnitO6pixelsyA2EmF">`RenderSize.Unit.pixels`</a> is supported.

  <a href="sdk-for-ios-navigate-classes-mappolyline-solidrepresentation#sdk-for-ios-navigate-s-7heresdk11MapPolylineC19SolidRepresentationC9lineWidthAA0B26MeasureDependentRenderSizeVvp">`lineWidth`</a> must not be 0 (`lineWidth.sizes` with all values set to 0.0).

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-classes-mappolyline-representation#sdk-for-ios-navigate-s-7heresdk11MapPolylineC14RepresentationC18InstantiationErrora">`MapPolyline.Representation.InstantiationError`</a> In case of invalid input parameters.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(lineWidth: MapMeasureDependentRenderSize, color: UIColor, capShape: LineCap) throws
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a>
  - <a href="sdk-for-ios-navigate-enums-linecap">LineCap</a>

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
  <td><code> </code><em><code>lineWidth</code></em><code> </code></td>
  <td><div>
  <p>The width of the polyline depending on the map measure.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>color</code></em><code> </code></td>
  <td><div>
  <p>The color of the polyline.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>capShape</code></em><code> </code></td>
  <td><div>
  <p>The cap shape applied to both ends of the polyline.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk11MapPolylineC19SolidRepresentationC9lineWidth5color07outlineG00I5Color8capShapeAeA0B26MeasureDependentRenderSizeV_So7UIColorCAlnA7LineCapOtKcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-lineWidth-color-outlineWidth-outlineColor-capShape" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mappolyline-solidrepresentation#sdk-for-ios-navigate-s-7heresdk11MapPolylineC19SolidRepresentationC9lineWidth5color07outlineG00I5Color8capShapeAeA0B26MeasureDependentRenderSizeV_So7UIColorCAlnA7LineCapOtKcfc" class="token"><code>init(lineWidth:</code><wbr></wbr><code>color:</code><wbr></wbr><code>outlineWidth:</code><wbr></wbr><code>outlineColor:</code><wbr></wbr><code>capShape:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a representation for a solid line with outline.

  The total width of the polyline is `line width + 2 * outline width`.

  At map measures smaller than smallest map measure in the <a href="sdk-for-ios-navigate-classes-mappolyline-solidrepresentation#sdk-for-ios-navigate-s-7heresdk11MapPolylineC19SolidRepresentationC9lineWidthAA0B26MeasureDependentRenderSizeVvp">`lineWidth`</a> and <a href="sdk-for-ios-navigate-classes-mappolyline-solidrepresentation#sdk-for-ios-navigate-s-7heresdk11MapPolylineC19SolidRepresentationC12outlineWidthAA0B26MeasureDependentRenderSizeVvp">`outlineWidth`</a>, the value is constant and equal to the width given for the smallest map measure in the <a href="sdk-for-ios-navigate-classes-mappolyline-solidrepresentation#sdk-for-ios-navigate-s-7heresdk11MapPolylineC19SolidRepresentationC9lineWidthAA0B26MeasureDependentRenderSizeVvp">`lineWidth`</a> and <a href="sdk-for-ios-navigate-classes-mappolyline-solidrepresentation#sdk-for-ios-navigate-s-7heresdk11MapPolylineC19SolidRepresentationC12outlineWidthAA0B26MeasureDependentRenderSizeVvp">`outlineWidth`</a>.

  At map measures bigger than biggest map measure in the <a href="sdk-for-ios-navigate-classes-mappolyline-solidrepresentation#sdk-for-ios-navigate-s-7heresdk11MapPolylineC19SolidRepresentationC9lineWidthAA0B26MeasureDependentRenderSizeVvp">`lineWidth`</a> and <a href="sdk-for-ios-navigate-classes-mappolyline-solidrepresentation#sdk-for-ios-navigate-s-7heresdk11MapPolylineC19SolidRepresentationC12outlineWidthAA0B26MeasureDependentRenderSizeVvp">`outlineWidth`</a>, the value is constant and equal to the width given for the biggest map measure in the <a href="sdk-for-ios-navigate-classes-mappolyline-solidrepresentation#sdk-for-ios-navigate-s-7heresdk11MapPolylineC19SolidRepresentationC9lineWidthAA0B26MeasureDependentRenderSizeVvp">`lineWidth`</a> and <a href="sdk-for-ios-navigate-classes-mappolyline-solidrepresentation#sdk-for-ios-navigate-s-7heresdk11MapPolylineC19SolidRepresentationC12outlineWidthAA0B26MeasureDependentRenderSizeVvp">`outlineWidth`</a>.

  At map measures between two nearest given map measure is linearly interpolated between width values given for these map measures.

  For <a href="sdk-for-ios-navigate-structs-mapmeasure-kind">`MapMeasure.Kind`</a> only <a href="sdk-for-ios-navigate-structs-mapmeasure-kind#sdk-for-ios-navigate-s-7heresdk10MapMeasureV4KindO9zoomLevelyA2EmF">`MapMeasure.Kind.zoomLevel`</a> is supported.

  For <a href="sdk-for-ios-navigate-structs-rendersize-unit">`RenderSize.Unit`</a> only <a href="sdk-for-ios-navigate-structs-rendersize-unit#sdk-for-ios-navigate-s-7heresdk10RenderSizeV4UnitO6pixelsyA2EmF">`RenderSize.Unit.pixels`</a> is supported.

  <a href="sdk-for-ios-navigate-classes-mappolyline-solidrepresentation#sdk-for-ios-navigate-s-7heresdk11MapPolylineC19SolidRepresentationC9lineWidthAA0B26MeasureDependentRenderSizeVvp">`lineWidth`</a> must not be 0 (`lineWidth.sizes` with all values set to 0.0).

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-classes-mappolyline-representation#sdk-for-ios-navigate-s-7heresdk11MapPolylineC14RepresentationC18InstantiationErrora">`MapPolyline.Representation.InstantiationError`</a> In case of invalid input parameters.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(lineWidth: MapMeasureDependentRenderSize, color: UIColor, outlineWidth: MapMeasureDependentRenderSize, outlineColor: UIColor, capShape: LineCap) throws
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a>
  - <a href="sdk-for-ios-navigate-enums-linecap">LineCap</a>

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
  <td><code> </code><em><code>lineWidth</code></em><code> </code></td>
  <td><div>
  <p>The width of the polyline depending on the map measure.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>color</code></em><code> </code></td>
  <td><div>
  <p>The color of the polyline.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>outlineWidth</code></em><code> </code></td>
  <td><div>
  <p>The width of the outline on one side of the polyline depending on the map measure.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>outlineColor</code></em><code> </code></td>
  <td><div>
  <p>The outline color of the polyline.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>capShape</code></em><code> </code></td>
  <td><div>
  <p>The cap shape applied to both ends of the polyline.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk11MapPolylineC19SolidRepresentationC9lineWidthAA0B26MeasureDependentRenderSizeVvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-lineWidth" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mappolyline-solidrepresentation#sdk-for-ios-navigate-s-7heresdk11MapPolylineC19SolidRepresentationC9lineWidthAA0B26MeasureDependentRenderSizeVvp" class="token"><code>lineWidth</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The width of the polyline depending on the map measure. At map measures smaller than smallest map measure in the `lineWidth` line width is constant and equal to the width given for the smallest map measure in the `lineWidth`.

  At map measures bigger than biggest map measure in the `lineWidth` line width is constant and equal to the width given for the biggest map measure in the `lineWidth`.

  At map measures between two nearest given map measures, the values are linearly interpolated between values given for these map measures.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var lineWidth: MapMeasureDependentRenderSize { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk11MapPolylineC19SolidRepresentationC9lineColorSo7UIColorCvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-lineColor" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mappolyline-solidrepresentation#sdk-for-ios-navigate-s-7heresdk11MapPolylineC19SolidRepresentationC9lineColorSo7UIColorCvp" class="token"><code>lineColor</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The color of the polyline.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var lineColor: UIColor { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk11MapPolylineC19SolidRepresentationC12outlineWidthAA0B26MeasureDependentRenderSizeVvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-outlineWidth" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mappolyline-solidrepresentation#sdk-for-ios-navigate-s-7heresdk11MapPolylineC19SolidRepresentationC12outlineWidthAA0B26MeasureDependentRenderSizeVvp" class="token"><code>outlineWidth</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The width of the outline on one side of the polyline depending on the map measure. The total width of the polyline is `line width + 2 * outline width`.

  At map measures smaller than smallest map measure in the `outlineWidth`, outline width is constant and equal to the width given for the smallest map measure in the `outlineWidth`.

  At map measures bigger than biggest map measure in the `outlineWidth`, outline width is constant and equal to the width given for the biggest map measure in the `outlineWidth`.

  At map measures between two nearest given map measures, the values are linearly interpolated between values given for these map measures.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var outlineWidth: MapMeasureDependentRenderSize { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk11MapPolylineC19SolidRepresentationC12outlineColorSo7UIColorCvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-outlineColor" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mappolyline-solidrepresentation#sdk-for-ios-navigate-s-7heresdk11MapPolylineC19SolidRepresentationC12outlineColorSo7UIColorCvp" class="token"><code>outlineColor</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The outline color of the polyline.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var outlineColor: UIColor { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk11MapPolylineC19SolidRepresentationC8capShapeAA7LineCapOvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-capShape" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mappolyline-solidrepresentation#sdk-for-ios-navigate-s-7heresdk11MapPolylineC19SolidRepresentationC8capShapeAA7LineCapOvp" class="token"><code>capShape</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The cap shape applied to both ends of the polyline and its outline.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var capShape: LineCap { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-linecap">LineCap</a>

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

