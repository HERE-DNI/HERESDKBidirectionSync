---
title: "maxPoints property - PolylineSimplifierOptions class - core library - Dart API"
slug: "sdk-for-flutter-explore-core-polylinesimplifieroptions-maxpoints"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core/PolylineSimplifierOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">maxPoints</span> property

</div>

<div class="section multi-line-signature">

int <span class="name">maxPoints</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Sets the upper limit on the resulting collection for the <a href="sdk-for-flutter-explore-core-polylinesimplifier-simplify">PolylineSimplifier.simplify</a>. Lower value results in the lower accuracy of the resulting polyline. If `maxPoints` is less than `2` then resulting polyline will not have an upper limit on the size and only <a href="sdk-for-flutter-explore-core-polylinesimplifieroptions-simplificationtoleranceinmeters">PolylineSimplifierOptions.simplificationToleranceInMeters</a> will be considered. When `maxPoints` is greater than size of the passed polyline then simplification algorithm will take into account only <a href="sdk-for-flutter-explore-core-polylinesimplifieroptions-simplificationtoleranceinmeters">PolylineSimplifierOptions.simplificationToleranceInMeters</a>.

</div>

## Implementation

``` dart
int maxPoints;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

