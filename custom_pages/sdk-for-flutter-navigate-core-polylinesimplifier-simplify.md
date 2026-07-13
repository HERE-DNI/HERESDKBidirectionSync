---
title: "simplify method - PolylineSimplifier class - core library - Dart API"
slug: "sdk-for-flutter-navigate-core-polylinesimplifier-simplify"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core/PolylineSimplifier-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">simplify</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> <span class="name">simplify</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-simplify-param-polyline" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span>\></span></span> <span class="parameter-name">polyline</span>, </span>
2.  <span id="sdk-for-flutter-navigate-simplify-param-simplificationParameters" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-polylinesimplifieroptions-class">PolylineSimplifierOptions</a></span> <span class="parameter-name">simplificationParameters</span>, </span>
3.  <span id="sdk-for-flutter-navigate-simplify-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-polylinesimplificationcallback">PolylineSimplificationCallback</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Reduces the number of points in the input polyline.

Does this by removing points which are not significant according to the passed <a href="sdk-for-flutter-navigate-core-polylinesimplifieroptions-class">PolylineSimplifierOptions</a>. Simplification process is performed on the device without connecting to the network and is computationally intensive.

- `polyline` Input polyline that should be reduced in size.

- `simplificationParameters` Strategy, that controls the behavior of the underlying algorithm.

- `callback` Callback, which will be invoked on the main thread, when operation is finished.

Returns <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Controls an asynchronous operation.

</div>

## Implementation

``` dart
TaskHandle simplify(List<GeoCoordinates> polyline, PolylineSimplifierOptions simplificationParameters, PolylineSimplificationCallback callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

