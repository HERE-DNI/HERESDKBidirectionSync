---
title: "MapPolylineDashImageRepresentation constructor - MapPolylineDashImageRepresentation - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mappolylinedashimagerepresentation-mappolylinedashimagerepresentation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapPolylineDashImageRepresentation.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapPolylineDashImageRepresentation-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">MapPolylineDashImageRepresentation</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">MapPolylineDashImageRepresentation</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-dashLength" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a></span> <span class="parameter-name">dashLength</span>, </span>
2.  <span id="sdk-for-flutter-navigate-param-gapLength" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a></span> <span class="parameter-name">gapLength</span>, </span>
3.  <span id="sdk-for-flutter-navigate-param-dashWidth" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a></span> <span class="parameter-name">dashWidth</span>, </span>
4.  <span id="sdk-for-flutter-navigate-param-image" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapimage-class">MapImage</a></span> <span class="parameter-name">image</span>, </span>

)

</div>

<div class="section desc markdown">

Creates a simple dash pattern in which the lengths of a dash and gap can be different.

Dashes are rendered as image.

This allows for patterns like `' — — — —'` or `' ——— ——— ———'`.

For <a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a> supplied for `dashLength`, `gapLength` and `dashWidth`, only <a href="sdk-for-flutter-navigate-mapview-mapmeasurekind">MapMeasureKind.zoomLevel</a> is supported for <a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-measurekind">MapMeasureDependentRenderSize.measureKind</a> and only <a href="sdk-for-flutter-navigate-mapview-rendersizeunit">RenderSizeUnit.meters</a> is supported for <a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-sizeunit">MapMeasureDependentRenderSize.sizeUnit</a>.

Only map measure values in range \[3-19\] are supported.

The value of the keys in <a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-sizes">MapMeasureDependentRenderSize.sizes</a> is truncated to integer values, hence only a single value can be provided per zoom level.

The values are interpolated linearly between zoom levels.

- `dashLength` The map measure dependent length of a dash, to which image width is stretched.

- `gapLength` The map measure dependent length of a gap between dash images.

- `dashWidth` The map measure dependent width of a dash, to which image height is stretched.

- `image` Image to be rendered in place of dash space. It is stretched to match `dashWidth` and `dashLength`.

Throws <a href="sdk-for-flutter-navigate-mapview-mappolylinerepresentationinstantiationexception-class">MapPolylineRepresentationInstantiationException</a>. In case of invalid input parameters.

</div>

## Implementation

``` dart
factory MapPolylineDashImageRepresentation(MapMeasureDependentRenderSize dashLength, MapMeasureDependentRenderSize gapLength, MapMeasureDependentRenderSize dashWidth, MapImage image) => $prototype.$init(dashLength, gapLength, dashWidth, image);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
