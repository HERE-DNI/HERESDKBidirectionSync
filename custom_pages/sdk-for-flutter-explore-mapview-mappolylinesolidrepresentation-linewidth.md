---
title: "lineWidth property - MapPolylineSolidRepresentation class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mappolylinesolidrepresentation-linewidth"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lineWidth.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapPolylineSolidRepresentation-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">lineWidth</span> property

</div>

<div id="sdk-for-flutter-explore-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a></span> <span class="name">lineWidth</span>

</div>

<div class="section desc markdown">

The width of the polyline depending on the map measure. At map measures smaller than smallest map measure in the `lineWidth` line width is constant and equal to the width given for the smallest map measure in the `lineWidth`.

At map measures bigger than biggest map measure in the `lineWidth` line width is constant and equal to the width given for the biggest map measure in the `lineWidth`.

At map measures between two nearest given map measures, the values are linearly interpolated between values given for these map measures. Gets the map measure dependent polyline width.

</div>

## Implementation

``` dart
MapMeasureDependentRenderSize get lineWidth;
```

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
