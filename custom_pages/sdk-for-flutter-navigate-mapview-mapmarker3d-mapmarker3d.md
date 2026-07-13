---
title: "MapMarker3D constructor - MapMarker3D - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapmarker3d-mapmarker3d"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapMarker3D.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapMarker3D-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">MapMarker3D</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">MapMarker3D</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-at" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">at</span>, </span>
2.  <span id="sdk-for-flutter-navigate-param-model" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapmarker3dmodel-class">MapMarker3DModel</a></span> <span class="parameter-name">model</span></span>

)

</div>

<div class="section desc markdown">

Creates an instance of a 3D marker.

The origin of the 3D model's local coordinate system is placed at the specified geographical coordinates.

Altitude component of the coordinates, if set, controls 3D marker's elevation above ground. If not set, the 3D marker is placed at ground level.

- `at` The geographical coordinates where the 3D marker is placed corresponding to origin of the 3D model's local coordinate system.

- `model` The 3D model used to draw 3D marker.

</div>

## Implementation

``` dart
factory MapMarker3D(GeoCoordinates at, MapMarker3DModel model) => $prototype.$init(at, model);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
