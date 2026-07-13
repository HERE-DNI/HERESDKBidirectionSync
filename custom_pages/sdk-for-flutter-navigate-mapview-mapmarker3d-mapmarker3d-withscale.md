---
title: "MapMarker3D.withScale constructor - MapMarker3D - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapmarker3d-mapmarker3d-withscale"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapMarker3D-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">MapMarker3D.withScale</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">MapMarker3D.withScale</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-withScale-param-at" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">at</span>, </span>
2.  <span id="sdk-for-flutter-navigate-withScale-param-model" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapmarker3dmodel-class">MapMarker3DModel</a></span> <span class="parameter-name">model</span>, </span>
3.  <span id="sdk-for-flutter-navigate-withScale-param-scale" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">scale</span></span>

)

</div>

<div class="section desc markdown">

Creates an instance of a 3D marker with scale factor.

One unit of the 3D marker model will cover `MapMarker3D.withScale.scale` pixels. The size of the 3D marker remains constant on the screen.

The origin of the 3D model's local coordinate system is placed at the specified geographical coordinates.

Altitude component of the coordinates, if set, controls 3D marker's elevation above ground. If not set, the 3D marker is placed at ground level.

- `at` The geographical coordinates where the 3D marker is placed corresponding to origin of the 3D model's local coordinate system.

- `model` The 3D model used to render the 3D marker.

- `scale` Scale factor to apply to the 3D model.

</div>

## Implementation

``` dart
factory MapMarker3D.withScale(GeoCoordinates at, MapMarker3DModel model, double scale) => $prototype.withScale(at, model, scale);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

