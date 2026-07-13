---
title: "simplificationToleranceInMeters property - PolylineSimplifierOptions class - core library - Dart API"
slug: "sdk-for-flutter-navigate-core-polylinesimplifieroptions-simplificationtoleranceinmeters"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core/PolylineSimplifierOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">simplificationToleranceInMeters</span> property

</div>

<div class="section multi-line-signature">

int <span class="name">simplificationToleranceInMeters</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Sets the accuracy limit for the <a href="sdk-for-flutter-navigate-core-polylinesimplifier-simplify">PolylineSimplifier.simplify</a>:

- higher tolerance results in more simplification (fewer points);
- lower tolerance keeps the line closer to its original shape.

If removing a point produces polyline, which deviates from the original one more than `simplificationToleranceInMeters`, then this point is left in the collection.

If specified tolerance will not allow to create a polyline conforming to <a href="sdk-for-flutter-navigate-core-polylinesimplifieroptions-maxpoints">PolylineSimplifierOptions.maxPoints</a>, then `simplificationToleranceInMeters` is ignored.

Default value is equal to <a href="sdk-for-flutter-navigate-core-polylinesimplifieroptions-simplificationinmeters14zoomlevel">PolylineSimplifierOptions.simplificationInMeters14ZoomLevel</a>.

</div>

## Implementation

``` dart
int simplificationToleranceInMeters;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

