---
title: "MapMarker3D.withUnit constructor - MapMarker3D - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapmarker3d-mapmarker3d-withunit"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapMarker3D.withUnit.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapMarker3D-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">MapMarker3D.withUnit</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">MapMarker3D.withUnit</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-withUnit-param-at" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">at</span>, </span>
2.  <span id="sdk-for-flutter-explore-withUnit-param-model" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapmarker3dmodel-class">MapMarker3DModel</a></span> <span class="parameter-name">model</span>, </span>
3.  <span id="sdk-for-flutter-explore-withUnit-param-scale" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">scale</span>, </span>
4.  <span id="sdk-for-flutter-explore-withUnit-param-unit" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-rendersizeunit">RenderSizeUnit</a></span> <span class="parameter-name">unit</span>, </span>

)

</div>

<div class="section desc markdown">

Creates a new 3D marker at given world coordinates, using the supplied 3D model.

The unit specifies how the 3D geometry of the model is interpreted (meters for world space, pixels or density independent pixels for screen space), while scale determines its relative size.

For <a href="sdk-for-flutter-explore-mapview-rendersizeunit">RenderSizeUnit.pixels</a> one unit of the 3D marker model will cover `MapMarker3D.withUnit.scale` pixels. The size of the 3D marker remains constant on the screen.

For <a href="sdk-for-flutter-explore-mapview-rendersizeunit">RenderSizeUnit.densityIndependentPixels</a> one unit of the 3D marker model will cover `MapMarker3D.withUnit.scale` density independent pixels. The size of the 3D marker remains constant on the screen.

For <a href="sdk-for-flutter-explore-mapview-rendersizeunit">RenderSizeUnit.meters</a> one unit of the 3D marker model will cover `MapMarker3D.withUnit.scale` meters in the real world. Unlike with pixels or density-independent pixels the size of the 3D marker will grow and shrink together with regular map content like streets or buildings.

The origin of the 3D model's local coordinate system is placed at the specified geographical coordinates.

Altitude component of the coordinates, if set, controls 3D marker's elevation above ground. If not set, the 3D marker is placed at ground level.

- `at` The geographical coordinates where the 3D marker is placed corresponding to origin of the 3D model's local coordinate system.

- `model` The 3D model used to render the 3D marker.

- `scale` Scale factor to apply to the 3D model.

- `unit` Determines the unit of the model vertices and whether the size of the 3D marker is expressed in world or screen space.

</div>

## Implementation

``` dart
factory MapMarker3D.withUnit(GeoCoordinates at, MapMarker3DModel model, double scale, RenderSizeUnit unit) => $prototype.withUnit(at, model, scale, unit);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
