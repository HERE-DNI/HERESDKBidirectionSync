---
title: "outlineWidth property - MapPolylineSolidRepresentation class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mappolylinesolidrepresentation-outlinewidth"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- outlineWidth.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapPolylineSolidRepresentation-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">outlineWidth</span> property

</div>

<div id="sdk-for-flutter-explore-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a></span> <span class="name">outlineWidth</span>

</div>

<div class="section desc markdown">

The width of the outline on one side of the polyline depending on the map measure. The total width of the polyline is `line width + 2 * outline width`.

At map measures smaller than smallest map measure in the `outlineWidth`, outline width is constant and equal to the width given for the smallest map measure in the `outlineWidth`.

At map measures bigger than biggest map measure in the `outlineWidth`, outline width is constant and equal to the width given for the biggest map measure in the `outlineWidth`.

At map measures between two nearest given map measures, the values are linearly interpolated between values given for these map measures. Gets the map measure dependent polyline outline width.

</div>

## Implementation

``` dart
MapMeasureDependentRenderSize get outlineWidth;
```

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
