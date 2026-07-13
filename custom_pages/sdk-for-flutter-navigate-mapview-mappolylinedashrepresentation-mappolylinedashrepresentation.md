---
title: "MapPolylineDashRepresentation constructor - MapPolylineDashRepresentation - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mappolylinedashrepresentation-mappolylinedashrepresentation"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapPolylineDashRepresentation-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">MapPolylineDashRepresentation</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">MapPolylineDashRepresentation</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-lineWidth" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a></span> <span class="parameter-name">lineWidth</span>, </span>
2.  <span id="sdk-for-flutter-navigate-param-dashLength" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a></span> <span class="parameter-name">dashLength</span>, </span>
3.  <span id="sdk-for-flutter-navigate-param-gapLength" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a></span> <span class="parameter-name">gapLength</span>, </span>
4.  <span id="sdk-for-flutter-navigate-param-dashColor" class="parameter"><span class="type-annotation">Color</span> <span class="parameter-name">dashColor</span>, </span>

)

</div>

<div class="section desc markdown">

Creates a representation for a dashed line.

Gaps are not displayed.

At map measures smaller than the smallest map measure in the `lineWidth`, `dashLength` and `gapLength`, the value used for rendering is constant and equal to the value given for the smallest map measure in the respective <a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a> object.

At map measures bigger than the biggest map measure in the `lineWidth`, `dashLength` and `gapLength`, the value used for rendering is constant and equal to the value given for the biggest map measure in the respective <a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a> object.

At map measures between two nearest given map measures, the values are linearly interpolated between values given for these map measures.

For <a href="sdk-for-flutter-navigate-mapview-mapmeasurekind">MapMeasureKind</a> only <a href="sdk-for-flutter-navigate-mapview-mapmeasurekind">MapMeasureKind.zoomLevel</a> is supported.

For <a href="sdk-for-flutter-navigate-mapview-rendersizeunit">RenderSizeUnit</a> only <a href="sdk-for-flutter-navigate-mapview-rendersizeunit">RenderSizeUnit.pixels</a> is supported.

All sizes must not be 0 (<a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-sizes">MapMeasureDependentRenderSize.sizes</a> with all values set to 0.0).

- `lineWidth` The width of the polyline depending on the map measure.

- `dashLength` The dash length of the polyline depending on the map measure.

- `gapLength` The gap length of the polyline depending on the map measure.

- `dashColor` The dash color of the polyline.

Throws <a href="sdk-for-flutter-navigate-mapview-mappolylinerepresentationinstantiationexception-class">MapPolylineRepresentationInstantiationException</a>. In case of invalid input parameters.

</div>

## Implementation

``` dart
factory MapPolylineDashRepresentation(MapMeasureDependentRenderSize lineWidth, MapMeasureDependentRenderSize dashLength, MapMeasureDependentRenderSize gapLength, ui.Color dashColor) => $prototype.$init(lineWidth, dashLength, gapLength, dashColor);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

