---
title: "MapMeasureDependentRenderSize constructor - MapMeasureDependentRenderSize - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-mapmeasuredependentrendersize"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapMeasureDependentRenderSize-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">MapMeasureDependentRenderSize</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">MapMeasureDependentRenderSize</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-param-measureKind" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapmeasurekind">MapMeasureKind</a></span> <span class="parameter-name">measureKind</span>, </span>
2.  <span id="sdk-for-flutter-explore-param-sizeUnit" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-rendersizeunit">RenderSizeUnit</a></span> <span class="parameter-name">sizeUnit</span>, </span>
3.  <span id="sdk-for-flutter-explore-param-sizes" class="parameter"><span class="type-annotation">Map<span class="signature">\<<wbr></wbr><span class="type-parameter">double</span>, <span class="type-parameter">double</span>\></span></span> <span class="parameter-name">sizes</span></span>

)

</div>

<div class="section desc markdown">

Constructs a `MapMeasureDependentRenderSize` from given parameters.

Supplying `sizes` map with a single entry indicates using a fixed size value across all map measures.

- `measureKind` The unit used for the key in `sizes`.

- `sizeUnit` The unit used for the value in `sizes`.

- `sizes` The dictionary describing the size (value) per map measure (key).

Throws <a href="sdk-for-flutter-explore-mapview-mapmeasuredependentrendersizeinstantiationexception-class">MapMeasureDependentRenderSizeInstantiationException</a>. Instantiation error if `sizes` map is empty or contains negative keys or values.

</div>

## Implementation

``` dart
factory MapMeasureDependentRenderSize(MapMeasureKind measureKind, RenderSizeUnit sizeUnit, Map<double, double> sizes) => $prototype.$init(measureKind, sizeUnit, sizes);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

