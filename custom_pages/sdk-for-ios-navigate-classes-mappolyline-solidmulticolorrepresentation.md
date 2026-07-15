---
title: "SolidMultiColorRepresentation Class Reference"
slug: "sdk-for-ios-navigate-classes-mappolyline-solidmulticolorrepresentation"
---

# SolidMultiColorRepresentation

<div class="declaration">

<div class="language">

``` highlight
public class SolidMultiColorRepresentation : MapPolyline.Representation
```

</div>

</div>

Representation allows map polyline to be colored in multiple specified color segments.

Color segment is defined by color stops. Color stop is specified as a polyline length ratio (0.0 - start of the polyline, 1.0 - end of the polyline). Color stop represents a color change starting at that exact point up until either the next color stop (if one exists) or the end of the polyline.

Progress color <a href="sdk-for-ios-navigate-classes-mappolyline#/s:7heresdk11MapPolylineC13progressColorSo7UIColorCvp">`MapPolyline.progressColor`</a> overrides any of the multiple color.

Examples: The following configuration will color map polyline as follows:

- from the start to the middle of it at the 0.5 point - in Red
- from the middle point 0.5 to the 0.7 point - in Green
- from 0.7 to 1.0 - in Red ‘colorStops: {0.0, 0.5, 0.7}, colorIndices: {0, 1, 0}, colors: {Red, Green}’

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

      init(lineWidth: capShape: colorStops: colorIndices: colors: gradientLength: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a representation for a multicolored line without an outline.

  Color segment is defined by color stops. Color stop is specified as a polyline length ratio (0.0 - start of the polyline, 1.0 - end of the polyline). Color stop represents a color change starting at that exact point up until either the next color stop (if one exists) or the end of the polyline.

  Progress color <a href="sdk-for-ios-navigate-classes-mappolyline#/s:7heresdk11MapPolylineC13progressColorSo7UIColorCvp">`MapPolyline.progressColor`</a> overrides any of the multiple color.

  At map measures smaller than smallest map measure in the `lineWidth` line width is constant and equal to the width given for the smallest map measure in the `lineWidth`.

  At map measures bigger than biggest map measure in the `lineWidth` line width is constant and equal to the width given for the biggest map measure in the `lineWidth`.

  At map measures between two nearest given map measures line width is linearly interpolated between width values given for these map measures.

  For <a href="sdk-for-ios-navigate-structs-mapmeasure-kind">`MapMeasure.Kind`</a> only <a href="sdk-for-ios-navigate-structs-mapmeasure-kind#/s:7heresdk10MapMeasureV4KindO9zoomLevelyA2EmF">`MapMeasure.Kind.zoomLevel`</a> is supported.

  For <a href="sdk-for-ios-navigate-structs-rendersize-unit">`RenderSize.Unit`</a> only <a href="sdk-for-ios-navigate-structs-rendersize-unit#/s:7heresdk10RenderSizeV4UnitO6pixelsyA2EmF">`RenderSize.Unit.pixels`</a> is supported.

  `lineWidth` must not be 0 (`lineWidth.sizes` with all values set to 0.0).

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-classes-mappolyline-representation#/s:7heresdk11MapPolylineC14RepresentationC18InstantiationErrora">`MapPolyline.Representation.InstantiationError`</a> In case of invalid input parameters.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( lineWidth : MapMeasureDependentRenderSize , capShape : LineCap , colorStops : [ Double ], colorIndices : [ UInt32 ], colors : [ UIColor ], gradientLength : Double ) throws
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
  <td><code> </code><em><code>lineWidth</code></em><code> </code></td>
  <td><div>
  <p>The width of the polyline depending on the map measure.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>capShape</code></em><code> </code></td>
  <td><div>
  <p>The cap shape applied to both ends of the polyline.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>colorStops</code></em><code> </code></td>
  <td><div>
  <p>List containing color stop values indicating a change of color on a polyline. Color stops must be in the range of [0.0, 1.0]. Color stop values must be sorted in ascending order (e.g. 0.0, 0.2, 0.3, 1.0). Duplicate values are not allowed. Color stop list must be of the same size as color indices list. Maximum size is 100 color stops. An empty list is not allowed. The first color stop value in the list must be 0.0.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>colorIndices</code></em><code> </code></td>
  <td><div>
  <p>List of color indices (from the color list) corresponding to the color stops. Value range is: [0, (color list size - 1)]. Values outside of the range are not allowed. Color indices list must be of the same size as color stop list. Maximum size is 100 color indices.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>colors</code></em><code> </code></td>
  <td><div>
  <p>List of colors. Maximum size is 16 colors. An empty list is not allowed.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>gradientLength</code></em><code> </code></td>
  <td><div>
  <p>Multiple color segment gradient length.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      init(lineWidth: outlineWidth: outlineColor: capShape: colorStops: colorIndices: colors: gradientLength: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a representation for a multicolored line with an outline.

  Color segment is defined by color stops. Color stop is specified as a polyline length ratio (0.0 - start of the polyline, 1.0 - end of the polyline). Color stop represents a color change starting at that exact point up until either the next color stop (if one exists) or the end of the polyline.

  Progress color <a href="sdk-for-ios-navigate-classes-mappolyline#/s:7heresdk11MapPolylineC13progressColorSo7UIColorCvp">`MapPolyline.progressColor`</a> overrides any of the multiple color.

  The total width of the polyline is `line width + 2 * outline width`.

  At map measures smaller than smallest map measure in the `lineWidth` and `outlineWidth`, the value is constant and equal to the width given for the smallest map measure in the `lineWidth` and `outlineWidth`.

  At map measures bigger than biggest map measure in the `lineWidth` and `outlineWidth`, the value is constant and equal to the width given for the biggest map measure in the `lineWidth` and `outlineWidth`.

  At map measures between two nearest given map measure is linearly interpolated between width values given for these map measures.

  For <a href="sdk-for-ios-navigate-structs-mapmeasure-kind">`MapMeasure.Kind`</a> only <a href="sdk-for-ios-navigate-structs-mapmeasure-kind#/s:7heresdk10MapMeasureV4KindO9zoomLevelyA2EmF">`MapMeasure.Kind.zoomLevel`</a> is supported.

  For <a href="sdk-for-ios-navigate-structs-rendersize-unit">`RenderSize.Unit`</a> only <a href="sdk-for-ios-navigate-structs-rendersize-unit#/s:7heresdk10RenderSizeV4UnitO6pixelsyA2EmF">`RenderSize.Unit.pixels`</a> is supported.

  `lineWidth` must not be 0 (`lineWidth.sizes` with all values set to 0.0).

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-classes-mappolyline-representation#/s:7heresdk11MapPolylineC14RepresentationC18InstantiationErrora">`MapPolyline.Representation.InstantiationError`</a> In case of invalid input parameters.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( lineWidth : MapMeasureDependentRenderSize , outlineWidth : MapMeasureDependentRenderSize , outlineColor : UIColor , capShape : LineCap , colorStops : [ Double ], colorIndices : [ UInt32 ], colors : [ UIColor ], gradientLength : Double ) throws
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
  <td><code> </code><em><code>lineWidth</code></em><code> </code></td>
  <td><div>
  <p>The width of the polyline depending on the map measure.</p>
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
  <tr>
  <td><code> </code><em><code>colorStops</code></em><code> </code></td>
  <td><div>
  <p>List containing color stop values indicating a change of color on a polyline. Color stops must be in the range of [0.0, 1.0]. Color stop values must be sorted in ascending order (e.g. 0.0, 0.2, 0.3, 1.0). Duplicate values are not allowed. Color stop list must be of the same size as color indices list. Maximum size is 100 color stops. An empty list is not allowed. The first color stop value in the list must be 0.0.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>colorIndices</code></em><code> </code></td>
  <td><div>
  <p>List of color indices (from the color list) corresponding to the color stops. Value range is: [0, (color list size - 1)]. Values outside of the range are not allowed. Color indices list must be of the same size as color stop list. Maximum size is 100 color indices.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>colors</code></em><code> </code></td>
  <td><div>
  <p>List of colors. Maximum size is 16 colors. An empty list is not allowed.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>gradientLength</code></em><code> </code></td>
  <td><div>
  <p>Multiple color segment gradient length.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      setMultiColors(colorStops: colorIndices: colors: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets lists of colors and multiple color segment stops for the polyline to be colored in. When this representation is already set on any <a href="sdk-for-ios-navigate-classes-mappolyline">`MapPolyline`</a>, values will be applied on that <a href="sdk-for-ios-navigate-classes-mappolyline">`MapPolyline`</a> right away. If this representation is not set on any <a href="sdk-for-ios-navigate-classes-mappolyline">`MapPolyline`</a>, values will be applied once representation is set on a <a href="sdk-for-ios-navigate-classes-mappolyline">`MapPolyline`</a>.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setMultiColors ( colorStops : [ Double ], colorIndices : [ UInt32 ], colors : [ UIColor ]) -> Bool
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
  <td><code> </code><em><code>colorStops</code></em><code> </code></td>
  <td><div>
  <p>List containing color stop values indicating a change of color on a polyline. Color stops must be in the range of [0.0, 1.0]. Color stop values must be sorted in ascending order (e.g. 0.0, 0.2, 0.3, 1.0). Duplicate values are not allowed. Color stop list must be of the same size as color indices list. Maximum size is 100 color stops. An empty list is not allowed. The first color stop value in the list must be 0.0.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>colorIndices</code></em><code> </code></td>
  <td><div>
  <p>List of color indices (from the color list) corresponding to the color stops. Value range is: [0, (color list size - 1)]. Values outside of the range are not allowed. Color indices list must be of the same size as color stop list. Maximum size is 100 color indices.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>colors</code></em><code> </code></td>
  <td><div>
  <p>List of colors. Maximum size is 16 colors. An empty list is not allowed.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Value indicating whether parameters are valid and can be applied.

  </div>

  </div>

  </div>

- <div>

      setMultiColorGradientLength(length: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the multiple color segment gradient length.

  Colors of two adjacent color segments can be blended to have a nicer visual appeal. Blending produces color gradient of specific length which is part of the color segment being blended.

  Start of the segment is blended with a color from the previous segment. Blending length is specified as a ratio of the smallest color segment length (from the list of color stops). E.g. a value of ‘0.1’ means 10% of the length of the smallest segment will be blended with a color from its previous segment. For this smallest segment gradient length is applied as-is, for all other segments it is scaled proportionally based on the smallest segment’s size to other segment size ratio.

  Length of ‘0.0’ is the default value which means blending will not be applied. Valid value range is \[0.0, 1.0\]. Out of range values are not supported. When this representation is already set on any <a href="sdk-for-ios-navigate-classes-mappolyline">`MapPolyline`</a>, value will be applied on that <a href="sdk-for-ios-navigate-classes-mappolyline">`MapPolyline`</a> right away. If this representation is not set on any <a href="sdk-for-ios-navigate-classes-mappolyline">`MapPolyline`</a>, value will be applied once representation is set on a <a href="sdk-for-ios-navigate-classes-mappolyline">`MapPolyline`</a>.

  Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setMultiColorGradientLength ( length : Double ) -> Bool
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
  <td><code> </code><em><code>length</code></em><code> </code></td>
  <td><div>
  <p>Multiple color segment gradient length. Length of ‘0.0’ is the default value which means blending will not be applied. Valid value range is [0.0, 1.0]. Out of range values are not supported.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Value indicating whether specified value is valid and can be applied.

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

