---
title: "MapPolylineSolidMultiColorRepresentation constructor - MapPolylineSolidMultiColorRepresentation - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mappolylinesolidmulticolorrepresentation-mappolylinesolidmulticolorrepresentation"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapPolylineSolidMultiColorRepresentation-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">MapPolylineSolidMultiColorRepresentation</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">MapPolylineSolidMultiColorRepresentation</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-param-lineWidth" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a></span> <span class="parameter-name">lineWidth</span>, </span>
2.  <span id="sdk-for-flutter-explore-param-capShape" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-linecap">LineCap</a></span> <span class="parameter-name">capShape</span>, </span>
3.  <span id="sdk-for-flutter-explore-param-colorStops" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">double</span>\></span></span> <span class="parameter-name">colorStops</span>, </span>
4.  <span id="sdk-for-flutter-explore-param-colorIndices" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">int</span>\></span></span> <span class="parameter-name">colorIndices</span>, </span>
5.  <span id="sdk-for-flutter-explore-param-colors" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">Color</span>\></span></span> <span class="parameter-name">colors</span>, </span>
6.  <span id="sdk-for-flutter-explore-param-gradientLength" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">gradientLength</span>, </span>

)

</div>

<div class="section desc markdown">

Creates a representation for a multicolored line without an outline.

Color segment is defined by color stops. Color stop is specified as a polyline length ratio (0.0 - start of the polyline, 1.0 - end of the polyline). Color stop represents a color change starting at that exact point up until either the next color stop (if one exists) or the end of the polyline.

Progress color `MapPolyline.progressColor` overrides any of the multiple color.

At map measures smaller than smallest map measure in the `lineWidth` line width is constant and equal to the width given for the smallest map measure in the `lineWidth`.

At map measures bigger than biggest map measure in the `lineWidth` line width is constant and equal to the width given for the biggest map measure in the `lineWidth`.

At map measures between two nearest given map measures line width is linearly interpolated between width values given for these map measures.

For <a href="sdk-for-flutter-explore-mapview-mapmeasurekind">MapMeasureKind</a> only <a href="sdk-for-flutter-explore-mapview-mapmeasurekind">MapMeasureKind.zoomLevel</a> is supported.

For <a href="sdk-for-flutter-explore-mapview-rendersizeunit">RenderSizeUnit</a> only <a href="sdk-for-flutter-explore-mapview-rendersizeunit">RenderSizeUnit.pixels</a> is supported.

`lineWidth` must not be 0 (`lineWidth.sizes` with all values set to 0.0).

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

- `lineWidth` The width of the polyline depending on the map measure.

- `capShape` The cap shape applied to both ends of the polyline.

- `colorStops` List containing color stop values indicating a change of color on a polyline. Color stops must be in the range of \[0.0, 1.0\]. Color stop values must be sorted in ascending order (e.g. 0.0, 0.2, 0.3, 1.0). Duplicate values are not allowed. Color stop list must be of the same size as color indices list. Maximum size is 100 color stops. An empty list is not allowed. The first color stop value in the list must be 0.0.

- `colorIndices` List of color indices (from the color list) corresponding to the color stops. Value range is: \[0, (color list size - 1)\]. Values outside of the range are not allowed. Color indices list must be of the same size as color stop list. Maximum size is 100 color indices.

- `colors` List of colors. Maximum size is 16 colors. An empty list is not allowed.

- `gradientLength` Multiple color segment gradient length.

Colors of two adjacent color segments can be blended to have a nicer visual appeal. Blending produces color gradient of specific length which is part of the color segment being blended.

Start of the segment is blended with a color from the previous segment. Blending length is specified as a ratio of the smallest color segment length (from the list of color stops). E.g. a value of '0.1' means 10% of the length of the smallest segment will be blended with a color from its previous segment. For this smallest segment gradient length is applied as-is, for all other segments it is scaled proportionally based on the smallest segment's size to other segment size ratio.

Length of '0.0' is the default value which means blending will not be applied. Valid value range is \[0.0, 1.0\]. Out of range values are not supported.

Throws <a href="sdk-for-flutter-explore-mapview-mappolylinerepresentationinstantiationexception-class">MapPolylineRepresentationInstantiationException</a>. In case of invalid input parameters.

</div>

## Implementation

``` dart
factory MapPolylineSolidMultiColorRepresentation(MapMeasureDependentRenderSize lineWidth, LineCap capShape, List<double> colorStops, List<int> colorIndices, List<ui.Color> colors, double gradientLength) => $prototype.$init(lineWidth, capShape, colorStops, colorIndices, colors, gradientLength);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

