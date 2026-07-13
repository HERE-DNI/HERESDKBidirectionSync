---
title: "PolylineSimplifierOptions.withMaxPointsAndTolerance constructor - PolylineSimplifierOptions - core library - Dart API"
slug: "sdk-for-flutter-navigate-core-polylinesimplifieroptions-polylinesimplifieroptions-withmaxpointsandtolerance"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- PolylineSimplifierOptions.withMaxPointsAndTolerance.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core/PolylineSimplifierOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">PolylineSimplifierOptions.withMaxPointsAndTolerance</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">PolylineSimplifierOptions.withMaxPointsAndTolerance</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-withMaxPointsAndTolerance-param-maxPoints" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">maxPoints</span>, </span>
2.  <span id="sdk-for-flutter-navigate-withMaxPointsAndTolerance-param-simplificationToleranceInMeters" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">simplificationToleranceInMeters</span></span>

)

</div>

<div class="section desc markdown">

Creates options with explicitly specified <a href="sdk-for-flutter-navigate-core-polylinesimplifieroptions-maxpoints">PolylineSimplifierOptions.maxPoints</a> and <a href="sdk-for-flutter-navigate-core-polylinesimplifieroptions-simplificationtoleranceinmeters">PolylineSimplifierOptions.simplificationToleranceInMeters</a>.

- `maxPoints` Sets the upper limit on the resulting collection for the <a href="sdk-for-flutter-navigate-core-polylinesimplifier-simplify">PolylineSimplifier.simplify</a>. Lower value results in the lower accuracy of the resulting polyline. If `maxPoints` is less than `2` then resulting polyline will not have an upper limit on the size and only <a href="sdk-for-flutter-navigate-core-polylinesimplifieroptions-simplificationtoleranceinmeters">PolylineSimplifierOptions.simplificationToleranceInMeters</a> will be considered. When `maxPoints` is greater than size of the passed polyline then simplification algorithm will take into account only <a href="sdk-for-flutter-navigate-core-polylinesimplifieroptions-simplificationtoleranceinmeters">PolylineSimplifierOptions.simplificationToleranceInMeters</a>.
- `simplificationToleranceInMeters` Sets the accuracy limit for the <a href="sdk-for-flutter-navigate-core-polylinesimplifier-simplify">PolylineSimplifier.simplify</a>:
- higher tolerance results in more simplification (fewer points);
- lower tolerance keeps the line closer to its original shape.

If removing a point produces polyline, which deviates from the original one more than `simplificationToleranceInMeters`, then this point is left in the collection.

If specified tolerance will not allow to create a polyline conforming to <a href="sdk-for-flutter-navigate-core-polylinesimplifieroptions-maxpoints">PolylineSimplifierOptions.maxPoints</a>, then `simplificationToleranceInMeters` is ignored.

Default value is equal to <a href="sdk-for-flutter-navigate-core-polylinesimplifieroptions-simplificationinmeters14zoomlevel">PolylineSimplifierOptions.simplificationInMeters14ZoomLevel</a>.

</div>

## Implementation

``` dart
PolylineSimplifierOptions.withMaxPointsAndTolerance(this.maxPoints, this.simplificationToleranceInMeters);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
