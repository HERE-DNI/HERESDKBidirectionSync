---
title: "progressGradientLength property - MapPolyline class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mappolyline-progressgradientlength"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapPolyline-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">progressGradientLength</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a></span> <span class="name">progressGradientLength</span>

</div>

<div class="section desc markdown">

The maximum gradient length between `MapPolyline.lineColor' and 'MapPolyline.progressColor` in zoom level dependent pixels. Gets the maximum gradient length between `MapPolyline.lineColor' and 'MapPolyline.progressColor` in zoom level dependent pixels.

</div>

## Implementation

``` dart
MapMeasureDependentRenderSize get progressGradientLength;
```

</div>

<div id="sdk-for-flutter-navigate-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">progressGradientLength=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-progressGradientLength-param-value" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a></span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

The maximum gradient length between `MapPolyline.lineColor' and 'MapPolyline.progressColor` in zoom level dependent pixels. Sets the maximum gradient length between `MapPolyline.lineColor' and 'MapPolyline.progressColor` in zoom level dependent pixels. To achieve a constant gradient length, use <a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a> with a single value. To achieve a gradient length dependent on map zoom, use <a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a> with multiple values. The default value is a constant gradient length of zero pixels. The gradient is guaranteed to fit into polyline, i.e. the actual gradient can be shorter then `progressGradientLength`.

For <a href="sdk-for-flutter-navigate-mapview-mapmeasurekind">MapMeasureKind</a> only <a href="sdk-for-flutter-navigate-mapview-mapmeasurekind">MapMeasureKind.zoomLevel</a> is supported. For <a href="sdk-for-flutter-navigate-mapview-rendersizeunit">RenderSizeUnit</a> only <a href="sdk-for-flutter-navigate-mapview-rendersizeunit">RenderSizeUnit.pixels</a> is supported. A parameter with unsupported values is ignored.

</div>

## Implementation

``` dart
set progressGradientLength(MapMeasureDependentRenderSize value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

