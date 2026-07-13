---
title: "dashLength property - MapPolylineDashRepresentation class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mappolylinedashrepresentation-dashlength"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- dashLength.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapPolylineDashRepresentation-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">dashLength</span> property

</div>

<div id="sdk-for-flutter-explore-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a></span> <span class="name">dashLength</span>

</div>

<div class="section desc markdown">

The dash length of the polyline depending on the map measure. At map measures smaller than smallest map measure in the `dashLength` line width is constant and equal to the width given for the smallest map measure in the `dashLength`.

At map measures bigger than biggest map measure in the `dashLength` line width is constant and equal to the width given for the biggest map measure in the `dashLength`.

At map measures between two nearest given map measures, the values are linearly interpolated between values given for these map measures. Gets the map measure dependent polyline dash length.

</div>

## Implementation

``` dart
MapMeasureDependentRenderSize get dashLength;
```

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
