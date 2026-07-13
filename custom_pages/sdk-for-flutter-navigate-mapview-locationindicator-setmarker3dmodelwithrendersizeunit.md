---
title: "setMarker3dModelWithRenderSizeUnit method - LocationIndicator class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-locationindicator-setmarker3dmodelwithrendersizeunit"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setMarker3dModelWithRenderSizeUnit.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/LocationIndicator-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">setMarker3dModelWithRenderSizeUnit</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">setMarker3dModelWithRenderSizeUnit</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-setMarker3dModelWithRenderSizeUnit-param-model" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapmarker3dmodel-class">MapMarker3DModel</a></span> <span class="parameter-name">model</span>, </span>
2.  <span id="sdk-for-flutter-navigate-setMarker3dModelWithRenderSizeUnit-param-scale" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">scale</span>, </span>
3.  <span id="sdk-for-flutter-navigate-setMarker3dModelWithRenderSizeUnit-param-type" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-locationindicatormarkertype">LocationIndicatorMarkerType</a></span> <span class="parameter-name">type</span>, </span>
4.  <span id="sdk-for-flutter-navigate-setMarker3dModelWithRenderSizeUnit-param-renderSizeUnit" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-rendersizeunit">RenderSizeUnit</a></span> <span class="parameter-name">renderSizeUnit</span>, </span>

)

</div>

<div class="section desc markdown">

Sets the <a href="sdk-for-flutter-navigate-mapview-mapmarker3dmodel-class">MapMarker3DModel</a> asset to be displayed as location indicator for a specified type.

The 3D model should be oriented with y axis up and thus standing on the x/z plane where the z axis is the depth. The direction in which the location indicator is pointing is the positive z axis. Please note that only <a href="sdk-for-flutter-navigate-mapview-mapmarker3dmodel-class">MapMarker3DModel</a> created from `obj` files are supported. Models created from Mesh will be ignored.

- `model` The <a href="sdk-for-flutter-navigate-mapview-mapmarker3dmodel-class">MapMarker3DModel</a> object to be displayed for the specified type. Only models created from `obj` files are supported. Those created from mesh will be ignored.

- `scale` A scale factor applied to the marker model.

- `type` The type of location marker for which the marker 3d model should be replaced.

- `renderSizeUnit` The <a href="sdk-for-flutter-navigate-mapview-rendersizeunit">RenderSizeUnit</a> specifying how the vertex coordinates of the 3D model are being interpreted. It specifies whether the 3D model is placed in world or screen coordinate space.

<a href="sdk-for-flutter-navigate-mapview-rendersizeunit">RenderSizeUnit.meters</a> will make the 3D model use world coordinate space, meaning that it will change size together with the map when it is zoomed in and out. A simple 10 by 10 by 10 (in model space) cube will have a size of 10 by 10 by 10 meters in world space.

<a href="sdk-for-flutter-navigate-mapview-rendersizeunit">RenderSizeUnit.pixels</a> makes the 3D model use screen coordinate space, meaning that it will have constant size on the screen regardless of how the map zoom changes. A simple 10 by 10 (in model space) rectangle will have a size of 10 by 10 pixels on the screen.

<a href="sdk-for-flutter-navigate-mapview-rendersizeunit">RenderSizeUnit.densityIndependentPixels</a> is similar to pixels, but the resulting size will take into account the pixel density of the display, meaning that physical size on the screen will be approximately the same regardless of the size or resolution of the display.

</div>

## Implementation

``` dart
void setMarker3dModelWithRenderSizeUnit(MapMarker3DModel model, double scale, LocationIndicatorMarkerType type, RenderSizeUnit renderSizeUnit);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
