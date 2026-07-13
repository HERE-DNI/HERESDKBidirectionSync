---
title: "MapPolylineSolidRepresentation.withOutline constructor - MapPolylineSolidRepresentation - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mappolylinesolidrepresentation-mappolylinesolidrepresentation-withoutline"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapPolylineSolidRepresentation.withOutline.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapPolylineSolidRepresentation-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">MapPolylineSolidRepresentation.withOutline</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">MapPolylineSolidRepresentation.withOutline</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-withOutline-param-lineWidth" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a></span> <span class="parameter-name">lineWidth</span>, </span>
2.  <span id="sdk-for-flutter-navigate-withOutline-param-color" class="parameter"><span class="type-annotation">Color</span> <span class="parameter-name">color</span>, </span>
3.  <span id="sdk-for-flutter-navigate-withOutline-param-outlineWidth" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a></span> <span class="parameter-name">outlineWidth</span>, </span>
4.  <span id="sdk-for-flutter-navigate-withOutline-param-outlineColor" class="parameter"><span class="type-annotation">Color</span> <span class="parameter-name">outlineColor</span>, </span>
5.  <span id="sdk-for-flutter-navigate-withOutline-param-capShape" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-linecap">LineCap</a></span> <span class="parameter-name">capShape</span>, </span>

)

</div>

<div class="section desc markdown">

Creates a representation for a solid line with outline.

The total width of the polyline is `line width + 2 * outline width`.

At map measures smaller than smallest map measure in the `lineWidth` and `outlineWidth`, the value is constant and equal to the width given for the smallest map measure in the `lineWidth` and `outlineWidth`.

At map measures bigger than biggest map measure in the `lineWidth` and `outlineWidth`, the value is constant and equal to the width given for the biggest map measure in the `lineWidth` and `outlineWidth`.

At map measures between two nearest given map measure is linearly interpolated between width values given for these map measures.

For <a href="sdk-for-flutter-navigate-mapview-mapmeasurekind">MapMeasureKind</a> only <a href="sdk-for-flutter-navigate-mapview-mapmeasurekind">MapMeasureKind.zoomLevel</a> is supported.

For <a href="sdk-for-flutter-navigate-mapview-rendersizeunit">RenderSizeUnit</a> only <a href="sdk-for-flutter-navigate-mapview-rendersizeunit">RenderSizeUnit.pixels</a> is supported.

`lineWidth` must not be 0 (`lineWidth.sizes` with all values set to 0.0).

- `lineWidth` The width of the polyline depending on the map measure.

- `color` The color of the polyline.

- `outlineWidth` The width of the outline on one side of the polyline depending on the map measure.

- `outlineColor` The outline color of the polyline.

- `capShape` The cap shape applied to both ends of the polyline.

Throws <a href="sdk-for-flutter-navigate-mapview-mappolylinerepresentationinstantiationexception-class">MapPolylineRepresentationInstantiationException</a>. In case of invalid input parameters.

</div>

## Implementation

``` dart
factory MapPolylineSolidRepresentation.withOutline(MapMeasureDependentRenderSize lineWidth, ui.Color color, MapMeasureDependentRenderSize outlineWidth, ui.Color outlineColor, LineCap capShape) => $prototype.withOutline(lineWidth, color, outlineWidth, outlineColor, capShape);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
