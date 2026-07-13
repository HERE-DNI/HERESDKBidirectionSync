---
title: "Isoline constructor - Isoline - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-isoline-isoline"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- Isoline.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/Isoline-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">Isoline</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">Isoline</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-rangeType" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-isolinerangetype">IsolineRangeType</a></span> <span class="parameter-name">rangeType</span>, </span>
2.  <span id="sdk-for-flutter-navigate-param-rangeValue" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">rangeValue</span>, </span>
3.  <span id="sdk-for-flutter-navigate-param-center" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-mapmatchedcoordinates-class">MapMatchedCoordinates</a></span> <span class="parameter-name">center</span>, </span>
4.  <span id="sdk-for-flutter-navigate-param-polygons" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-geopolygon-class">GeoPolygon</a></span>\></span></span> <span class="parameter-name">polygons</span>, </span>

)

</div>

<div class="section desc markdown">

Constructs an isoline instance.

This instance is provided by the <a href="sdk-for-flutter-navigate-routing-calculateisolinecallback">CalculateIsolineCallback</a>.

- `rangeType` Specifies the range type of the provided

      Isoline.Isoline().rangeValue

  list.

  </p>

- `rangeValue` A list of range values. At least one value must be set.

- `center` The center of the isoline.

- `polygons` A list of polygons that belong to this isoline. At least one value must be set.

</div>

## Implementation

``` dart
factory Isoline(IsolineRangeType rangeType, double rangeValue, MapMatchedCoordinates center, List<GeoPolygon> polygons) => $prototype.make(rangeType, rangeValue, center, polygons);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
