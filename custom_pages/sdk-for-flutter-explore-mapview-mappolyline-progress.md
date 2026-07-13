---
title: "progress property - MapPolyline class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mappolyline-progress"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- progress.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapPolyline-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">progress</span> property

</div>

<div id="sdk-for-flutter-explore-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype">double</span> <span class="name">progress</span>

</div>

<div class="section desc markdown">

The progress from the polyline's starting point, as a ratio of its total length clamped to the range \[0, 1\]. Gets the progress of the polyline, 0 by default.

</div>

## Implementation

``` dart
double get progress;
```

</div>

<div id="sdk-for-flutter-explore-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">progress=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-progress-param-value" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

The progress from the polyline's starting point, as a ratio of its total length clamped to the range \[0, 1\]. Sets the progress of the polyline from its starting point as a ratio of its total length clamped to the range \[0; 1\].

As the progress varies, the equivalent part of the polyline gets covered by the progress color and progress outline color. The rest of the polyline until its end point retains the line color and outline color along with an optional dash pattern.

</div>

## Implementation

``` dart
set progress(double value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
