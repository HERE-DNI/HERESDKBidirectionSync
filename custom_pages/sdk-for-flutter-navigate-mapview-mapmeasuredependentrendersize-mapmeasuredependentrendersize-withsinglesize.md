---
title: "MapMeasureDependentRenderSize.withSingleSize constructor - MapMeasureDependentRenderSize - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-mapmeasuredependentrendersize-withsinglesize"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapMeasureDependentRenderSize-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">MapMeasureDependentRenderSize.withSingleSize</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">MapMeasureDependentRenderSize.withSingleSize</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-withSingleSize-param-sizeUnit" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-rendersizeunit">RenderSizeUnit</a></span> <span class="parameter-name">sizeUnit</span>, </span>
2.  <span id="sdk-for-flutter-navigate-withSingleSize-param-size" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">size</span></span>

)

</div>

<div class="section desc markdown">

Constructs a `MapMeasureDependentRenderSize` from single size value which is constant across all map measures.

The given `size` value is stored in <a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-sizes">MapMeasureDependentRenderSize.sizes</a> map at key 0 and <a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-measurekind">MapMeasureDependentRenderSize.measureKind</a> is set to <a href="sdk-for-flutter-navigate-mapview-mapmeasurekind">MapMeasureKind.zoomLevel</a>.

- `sizeUnit` The unit used for the value in `size`.

- `size` The size independent of map measure. Must not be negative.

Throws <a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersizeinstantiationexception-class">MapMeasureDependentRenderSizeInstantiationException</a>. Instantiation error if `size` is negative.

</div>

## Implementation

``` dart
factory MapMeasureDependentRenderSize.withSingleSize(RenderSizeUnit sizeUnit, double size) => $prototype.withSingleSize(sizeUnit, size);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

