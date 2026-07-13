---
title: "MapLayerVisibilityRange constructor - MapLayerVisibilityRange - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-maplayervisibilityrange-maplayervisibilityrange"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapLayerVisibilityRange.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapLayerVisibilityRange-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">MapLayerVisibilityRange</span> constructor

</div>

<div class="section multi-line-signature">

const <span class="name">MapLayerVisibilityRange</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-minimumZoomLevel" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">minimumZoomLevel</span>, </span>
2.  <span id="sdk-for-flutter-navigate-param-maximumZoomLevel" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">maximumZoomLevel</span></span>

)

</div>

<div class="section desc markdown">

Creates a new instance.

- `minimumZoomLevel` Minimum zoom level on which the layer will be visible. The value must be greater than or equal to the `MapCameraLimits.MIN_ZOOM_LEVEL`.
- `maximumZoomLevel` Minimum zoom level from which the layer will not be visible. The value must be less than or equal to the `MapCameraLimits.MAX_ZOOM_LEVEL`. Note that the map layer is not visible at the maximum zoom level.

</div>

## Implementation

``` dart
const MapLayerVisibilityRange(this.minimumZoomLevel, this.maximumZoomLevel);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
