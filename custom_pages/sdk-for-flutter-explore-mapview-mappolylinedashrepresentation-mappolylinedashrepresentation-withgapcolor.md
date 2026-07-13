---
title: "MapPolylineDashRepresentation.withGapColor constructor - MapPolylineDashRepresentation - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mappolylinedashrepresentation-mappolylinedashrepresentation-withgapcolor"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapPolylineDashRepresentation.withGapColor.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapPolylineDashRepresentation-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">MapPolylineDashRepresentation.withGapColor</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">MapPolylineDashRepresentation.withGapColor</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-withGapColor-param-lineWidth" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a></span> <span class="parameter-name">lineWidth</span>, </span>
2.  <span id="sdk-for-flutter-explore-withGapColor-param-dashLength" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a></span> <span class="parameter-name">dashLength</span>, </span>
3.  <span id="sdk-for-flutter-explore-withGapColor-param-gapLength" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a></span> <span class="parameter-name">gapLength</span>, </span>
4.  <span id="sdk-for-flutter-explore-withGapColor-param-dashColor" class="parameter"><span class="type-annotation">Color</span> <span class="parameter-name">dashColor</span>, </span>
5.  <span id="sdk-for-flutter-explore-withGapColor-param-gapColor" class="parameter"><span class="type-annotation">Color</span> <span class="parameter-name">gapColor</span>, </span>

)

</div>

<div class="section desc markdown">

Creates a representation for a dashed line with both dash and the gap being colored.

At map measures smaller than the smallest map measure in the `lineWidth`, `dashLength` and `gapLength`, the value used for rendering is constant and equal to the value given for the smallest map measure in the respective <a href="sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a> object.

At map measures bigger than the biggest map measure in the `lineWidth`, `dashLength` and `gapLength`, the value used for rendering is constant and equal to the value given for the biggest map measure in the respective <a href="sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a> object.

At map measures between two nearest given map measures, the values are linearly interpolated between values given for these map measures.

For <a href="sdk-for-flutter-explore-mapview-mapmeasurekind">MapMeasureKind</a> only <a href="sdk-for-flutter-explore-mapview-mapmeasurekind">MapMeasureKind.zoomLevel</a> is supported.

For <a href="sdk-for-flutter-explore-mapview-rendersizeunit">RenderSizeUnit</a> only <a href="sdk-for-flutter-explore-mapview-rendersizeunit">RenderSizeUnit.pixels</a> is supported.

All sizes must not be 0 (<a href="sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-sizes">MapMeasureDependentRenderSize.sizes</a> with all values set to 0.0).

- `lineWidth` The width of the polyline depending on the map measure.

- `dashLength` The dash length of the polyline depending on the map measure.

- `gapLength` The gap length of the polyline depending on the map measure.

- `dashColor` The color of the dashes.

- `gapColor` The color of the gaps.

Throws <a href="sdk-for-flutter-explore-mapview-mappolylinerepresentationinstantiationexception-class">MapPolylineRepresentationInstantiationException</a>. In case of invalid input parameters.

</div>

## Implementation

``` dart
factory MapPolylineDashRepresentation.withGapColor(MapMeasureDependentRenderSize lineWidth, MapMeasureDependentRenderSize dashLength, MapMeasureDependentRenderSize gapLength, ui.Color dashColor, ui.Color gapColor) => $prototype.withGapColor(lineWidth, dashLength, gapLength, dashColor, gapColor);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
