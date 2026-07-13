---
title: "PolylineSimplificationCallback typedef - core library - Dart API"
slug: "sdk-for-flutter-explore-core-polylinesimplificationcallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- PolylineSimplificationCallback.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core/core-library-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-typedef">PolylineSimplificationCallback</span> typedef

</div>

<div class="section multi-line-signature">

<span class="name">PolylineSimplificationCallback</span> = <span class="returntype">void Function<span class="signature">(<span id="sdk-for-flutter-explore-param-queryError" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-polylinesimplificationerror">PolylineSimplificationError</a>?</span> <span class="parameter-name">queryError</span>, </span><span id="sdk-for-flutter-explore-param-result" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span>\></span>?</span> <span class="parameter-name">result</span></span>)</span></span>

</div>

<div class="section desc markdown">

The method will be called on the main thread when <a href="sdk-for-flutter-explore-core-polylinesimplifier-simplify">PolylineSimplifier.simplify</a> is finished.

- `queryError` The optional error, which occurred during simplification.

- `result` The simplified polyline with number of points less or equal to the input polyline of <a href="sdk-for-flutter-explore-core-polylinesimplifier-simplify">PolylineSimplifier.simplify</a>.

</div>

## Implementation

``` dart
typedef PolylineSimplificationCallback = void Function(PolylineSimplificationError? queryError, List<GeoCoordinates>? result);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
