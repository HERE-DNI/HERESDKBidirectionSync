---
title: "MapPolylineSolidRepresentation constructor - MapPolylineSolidRepresentation - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mappolylinesolidrepresentation-mappolylinesolidrepresentation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapPolylineSolidRepresentation.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapPolylineSolidRepresentation-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">MapPolylineSolidRepresentation</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">MapPolylineSolidRepresentation</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-param-lineWidth" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a></span> <span class="parameter-name">lineWidth</span>, </span>
2.  <span id="sdk-for-flutter-explore-param-color" class="parameter"><span class="type-annotation">Color</span> <span class="parameter-name">color</span>, </span>
3.  <span id="sdk-for-flutter-explore-param-capShape" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-linecap">LineCap</a></span> <span class="parameter-name">capShape</span></span>

)

</div>

<div class="section desc markdown">

Creates a representation for a solid line without outline.

At map measures smaller than smallest map measure in the `lineWidth` line width is constant and equal to the width given for the smallest map measure in the `lineWidth`.

At map measures bigger than biggest map measure in the `lineWidth` line width is constant and equal to the width given for the biggest map measure in the `lineWidth`.

At map measures between two nearest given map measures line width is linearly interpolated between width values given for these map measures.

For <a href="sdk-for-flutter-explore-mapview-mapmeasurekind">MapMeasureKind</a> only <a href="sdk-for-flutter-explore-mapview-mapmeasurekind">MapMeasureKind.zoomLevel</a> is supported.

For <a href="sdk-for-flutter-explore-mapview-rendersizeunit">RenderSizeUnit</a> only <a href="sdk-for-flutter-explore-mapview-rendersizeunit">RenderSizeUnit.pixels</a> is supported.

`lineWidth` must not be 0 (`lineWidth.sizes` with all values set to 0.0).

- `lineWidth` The width of the polyline depending on the map measure.

- `color` The color of the polyline.

- `capShape` The cap shape applied to both ends of the polyline.

Throws <a href="sdk-for-flutter-explore-mapview-mappolylinerepresentationinstantiationexception-class">MapPolylineRepresentationInstantiationException</a>. In case of invalid input parameters.

</div>

## Implementation

``` dart
factory MapPolylineSolidRepresentation(MapMeasureDependentRenderSize lineWidth, ui.Color color, LineCap capShape) => $prototype.$init(lineWidth, color, capShape);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
