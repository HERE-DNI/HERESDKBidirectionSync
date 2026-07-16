---
title: "DashRepresentation Class Reference"
slug: "sdk-for-ios-explore-classes-mappolyline-dashrepresentation"
---

# DashRepresentation

<div class="declaration">

<div class="language">

``` highlight
public class DashRepresentation : MapPolyline.Representation
```

</div>

Related types:

- <a href="sdk-for-ios-explore-classes-mappolyline">MapPolyline</a>
- <a href="sdk-for-ios-explore-classes-mappolyline-representation">Representation</a>

</div>

Represents a dash pattern for map polyline where the dash can be rendered as a colored line and the gap can be either empty or colored.

The length of the dash and gap are set independently, allowing for patterns like `' — — — —'` (dash length = gap length) or `' ——— ——— ———'` (dash length != gap length).

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11MapPolylineC18DashRepresentationC9lineWidth10dashLength03gapI00H5ColorAeA0B26MeasureDependentRenderSizeV_A2KSo7UIColorCtKcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-lineWidth-dashLength-gapLength-dashColor" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mappolyline-dashrepresentation#sdk-for-ios-explore-s-7heresdk11MapPolylineC18DashRepresentationC9lineWidth10dashLength03gapI00H5ColorAeA0B26MeasureDependentRenderSizeV_A2KSo7UIColorCtKcfc" class="token"><code>init(lineWidth:</code><wbr></wbr><code>dashLength:</code><wbr></wbr><code>gapLength:</code><wbr></wbr><code>dashColor:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a representation for a dashed line. Gaps are not displayed.

  At map measures smaller than the smallest map measure in the <a href="sdk-for-ios-explore-classes-mappolyline-dashrepresentation#sdk-for-ios-explore-s-7heresdk11MapPolylineC18DashRepresentationC9lineWidthAA0B26MeasureDependentRenderSizeVvp">`lineWidth`</a>, <a href="sdk-for-ios-explore-classes-mappolyline-dashrepresentation#sdk-for-ios-explore-s-7heresdk11MapPolylineC18DashRepresentationC10dashLengthAA0B26MeasureDependentRenderSizeVvp">`dashLength`</a> and <a href="sdk-for-ios-explore-classes-mappolyline-dashrepresentation#sdk-for-ios-explore-s-7heresdk11MapPolylineC18DashRepresentationC9gapLengthAA0B26MeasureDependentRenderSizeVvp">`gapLength`</a>, the value used for rendering is constant and equal to the value given for the smallest map measure in the respective <a href="sdk-for-ios-explore-structs-mapmeasuredependentrendersize">`MapMeasureDependentRenderSize`</a> object.

  At map measures bigger than the biggest map measure in the <a href="sdk-for-ios-explore-classes-mappolyline-dashrepresentation#sdk-for-ios-explore-s-7heresdk11MapPolylineC18DashRepresentationC9lineWidthAA0B26MeasureDependentRenderSizeVvp">`lineWidth`</a>, <a href="sdk-for-ios-explore-classes-mappolyline-dashrepresentation#sdk-for-ios-explore-s-7heresdk11MapPolylineC18DashRepresentationC10dashLengthAA0B26MeasureDependentRenderSizeVvp">`dashLength`</a> and <a href="sdk-for-ios-explore-classes-mappolyline-dashrepresentation#sdk-for-ios-explore-s-7heresdk11MapPolylineC18DashRepresentationC9gapLengthAA0B26MeasureDependentRenderSizeVvp">`gapLength`</a>, the value used for rendering is constant and equal to the value given for the biggest map measure in the respective <a href="sdk-for-ios-explore-structs-mapmeasuredependentrendersize">`MapMeasureDependentRenderSize`</a> object.

  At map measures between two nearest given map measures, the values are linearly interpolated between values given for these map measures.

  For <a href="sdk-for-ios-explore-structs-mapmeasure-kind">`MapMeasure.Kind`</a> only <a href="sdk-for-ios-explore-structs-mapmeasure-kind#sdk-for-ios-explore-s-7heresdk10MapMeasureV4KindO9zoomLevelyA2EmF">`MapMeasure.Kind.zoomLevel`</a> is supported.

  For <a href="sdk-for-ios-explore-structs-rendersize-unit">`RenderSize.Unit`</a> only <a href="sdk-for-ios-explore-structs-rendersize-unit#sdk-for-ios-explore-s-7heresdk10RenderSizeV4UnitO6pixelsyA2EmF">`RenderSize.Unit.pixels`</a> is supported.

  All sizes must not be 0 (<a href="sdk-for-ios-explore-structs-mapmeasuredependentrendersize#sdk-for-ios-explore-s-7heresdk29MapMeasureDependentRenderSizeV5sizesSDyS2dGvp">`MapMeasureDependentRenderSize.sizes`</a> with all values set to 0.0).

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-explore-classes-mappolyline-representation#sdk-for-ios-explore-s-7heresdk11MapPolylineC14RepresentationC18InstantiationErrora">`MapPolyline.Representation.InstantiationError`</a> In case of invalid input parameters.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(lineWidth: MapMeasureDependentRenderSize, dashLength: MapMeasureDependentRenderSize, gapLength: MapMeasureDependentRenderSize, dashColor: UIColor) throws
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a>

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
  <td><code> </code><em><code>dashLength</code></em><code> </code></td>
  <td><div>
  <p>The dash length of the polyline depending on the map measure.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>gapLength</code></em><code> </code></td>
  <td><div>
  <p>The gap length of the polyline depending on the map measure.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>dashColor</code></em><code> </code></td>
  <td><div>
  <p>The dash color of the polyline.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11MapPolylineC18DashRepresentationC9lineWidth10dashLength03gapI00H5Color0jK0AeA0B26MeasureDependentRenderSizeV_A2LSo7UIColorCANtKcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-lineWidth-dashLength-gapLength-dashColor-gapColor" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mappolyline-dashrepresentation#sdk-for-ios-explore-s-7heresdk11MapPolylineC18DashRepresentationC9lineWidth10dashLength03gapI00H5Color0jK0AeA0B26MeasureDependentRenderSizeV_A2LSo7UIColorCANtKcfc" class="token"><code>init(lineWidth:</code><wbr></wbr><code>dashLength:</code><wbr></wbr><code>gapLength:</code><wbr></wbr><code>dashColor:</code><wbr></wbr><code>gapColor:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a representation for a dashed line with both dash and the gap being colored.

  At map measures smaller than the smallest map measure in the <a href="sdk-for-ios-explore-classes-mappolyline-dashrepresentation#sdk-for-ios-explore-s-7heresdk11MapPolylineC18DashRepresentationC9lineWidthAA0B26MeasureDependentRenderSizeVvp">`lineWidth`</a>, <a href="sdk-for-ios-explore-classes-mappolyline-dashrepresentation#sdk-for-ios-explore-s-7heresdk11MapPolylineC18DashRepresentationC10dashLengthAA0B26MeasureDependentRenderSizeVvp">`dashLength`</a> and <a href="sdk-for-ios-explore-classes-mappolyline-dashrepresentation#sdk-for-ios-explore-s-7heresdk11MapPolylineC18DashRepresentationC9gapLengthAA0B26MeasureDependentRenderSizeVvp">`gapLength`</a>, the value used for rendering is constant and equal to the value given for the smallest map measure in the respective <a href="sdk-for-ios-explore-structs-mapmeasuredependentrendersize">`MapMeasureDependentRenderSize`</a> object.

  At map measures bigger than the biggest map measure in the <a href="sdk-for-ios-explore-classes-mappolyline-dashrepresentation#sdk-for-ios-explore-s-7heresdk11MapPolylineC18DashRepresentationC9lineWidthAA0B26MeasureDependentRenderSizeVvp">`lineWidth`</a>, <a href="sdk-for-ios-explore-classes-mappolyline-dashrepresentation#sdk-for-ios-explore-s-7heresdk11MapPolylineC18DashRepresentationC10dashLengthAA0B26MeasureDependentRenderSizeVvp">`dashLength`</a> and <a href="sdk-for-ios-explore-classes-mappolyline-dashrepresentation#sdk-for-ios-explore-s-7heresdk11MapPolylineC18DashRepresentationC9gapLengthAA0B26MeasureDependentRenderSizeVvp">`gapLength`</a>, the value used for rendering is constant and equal to the value given for the biggest map measure in the respective <a href="sdk-for-ios-explore-structs-mapmeasuredependentrendersize">`MapMeasureDependentRenderSize`</a> object.

  At map measures between two nearest given map measures, the values are linearly interpolated between values given for these map measures.

  For <a href="sdk-for-ios-explore-structs-mapmeasure-kind">`MapMeasure.Kind`</a> only <a href="sdk-for-ios-explore-structs-mapmeasure-kind#sdk-for-ios-explore-s-7heresdk10MapMeasureV4KindO9zoomLevelyA2EmF">`MapMeasure.Kind.zoomLevel`</a> is supported.

  For <a href="sdk-for-ios-explore-structs-rendersize-unit">`RenderSize.Unit`</a> only <a href="sdk-for-ios-explore-structs-rendersize-unit#sdk-for-ios-explore-s-7heresdk10RenderSizeV4UnitO6pixelsyA2EmF">`RenderSize.Unit.pixels`</a> is supported.

  All sizes must not be 0 (<a href="sdk-for-ios-explore-structs-mapmeasuredependentrendersize#sdk-for-ios-explore-s-7heresdk29MapMeasureDependentRenderSizeV5sizesSDyS2dGvp">`MapMeasureDependentRenderSize.sizes`</a> with all values set to 0.0).

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-explore-classes-mappolyline-representation#sdk-for-ios-explore-s-7heresdk11MapPolylineC14RepresentationC18InstantiationErrora">`MapPolyline.Representation.InstantiationError`</a> In case of invalid input parameters.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(lineWidth: MapMeasureDependentRenderSize, dashLength: MapMeasureDependentRenderSize, gapLength: MapMeasureDependentRenderSize, dashColor: UIColor, gapColor: UIColor) throws
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a>

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
  <td><code> </code><em><code>dashLength</code></em><code> </code></td>
  <td><div>
  <p>The dash length of the polyline depending on the map measure.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>gapLength</code></em><code> </code></td>
  <td><div>
  <p>The gap length of the polyline depending on the map measure.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>dashColor</code></em><code> </code></td>
  <td><div>
  <p>The color of the dashes.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>gapColor</code></em><code> </code></td>
  <td><div>
  <p>The color of the gaps.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11MapPolylineC18DashRepresentationC9lineWidthAA0B26MeasureDependentRenderSizeVvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-lineWidth" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mappolyline-dashrepresentation#sdk-for-ios-explore-s-7heresdk11MapPolylineC18DashRepresentationC9lineWidthAA0B26MeasureDependentRenderSizeVvp" class="token"><code>lineWidth</code></a> 

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

  - <a href="sdk-for-ios-explore-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11MapPolylineC18DashRepresentationC10dashLengthAA0B26MeasureDependentRenderSizeVvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-dashLength" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mappolyline-dashrepresentation#sdk-for-ios-explore-s-7heresdk11MapPolylineC18DashRepresentationC10dashLengthAA0B26MeasureDependentRenderSizeVvp" class="token"><code>dashLength</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The dash length of the polyline depending on the map measure. At map measures smaller than smallest map measure in the `dashLength` line width is constant and equal to the width given for the smallest map measure in the `dashLength`.

  At map measures bigger than biggest map measure in the `dashLength` line width is constant and equal to the width given for the biggest map measure in the `dashLength`.

  At map measures between two nearest given map measures, the values are linearly interpolated between values given for these map measures.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var dashLength: MapMeasureDependentRenderSize { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11MapPolylineC18DashRepresentationC9gapLengthAA0B26MeasureDependentRenderSizeVvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-gapLength" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mappolyline-dashrepresentation#sdk-for-ios-explore-s-7heresdk11MapPolylineC18DashRepresentationC9gapLengthAA0B26MeasureDependentRenderSizeVvp" class="token"><code>gapLength</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The gap length of the polyline depending on the map measure. At map measures smaller than smallest map measure in the `gapLength` line width is constant and equal to the width given for the smallest map measure in the `gapLength`.

  At map measures bigger than biggest map measure in the `gapLength` line width is constant and equal to the width given for the biggest map measure in the `gapLength`.

  At map measures between two nearest given map measures, the values are linearly interpolated between values given for these map measures.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var gapLength: MapMeasureDependentRenderSize { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11MapPolylineC18DashRepresentationC9dashColorSo7UIColorCvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-dashColor" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mappolyline-dashrepresentation#sdk-for-ios-explore-s-7heresdk11MapPolylineC18DashRepresentationC9dashColorSo7UIColorCvp" class="token"><code>dashColor</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The color of the dashes of the polyline.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var dashColor: UIColor { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk11MapPolylineC18DashRepresentationC8gapColorSo7UIColorCSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-gapColor" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mappolyline-dashrepresentation#sdk-for-ios-explore-s-7heresdk11MapPolylineC18DashRepresentationC8gapColorSo7UIColorCSgvp" class="token"><code>gapColor</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The color for the gaps of the polyline. The default value is `nil` and no color is used.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var gapColor: UIColor? { get }
  ```

  </div>

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

