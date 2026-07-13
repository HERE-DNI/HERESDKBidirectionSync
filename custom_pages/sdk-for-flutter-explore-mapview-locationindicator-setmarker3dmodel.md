---
title: "setMarker3dModel method - LocationIndicator class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-locationindicator-setmarker3dmodel"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/LocationIndicator-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">setMarker3dModel</span> abstract method

</div>

<div class="section multi-line-signature">

<div>

1.  @Deprecated("Will be removed in v4.27.0. Please use the \`setMarker3dModelWithRenderSizeUnit\` instead.")

</div>

<span class="returntype">void</span> <span class="name deprecated">setMarker3dModel</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-setMarker3dModel-param-model" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapmarker3dmodel-class">MapMarker3DModel</a></span> <span class="parameter-name">model</span>, </span>
2.  <span id="sdk-for-flutter-explore-setMarker3dModel-param-scale" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">scale</span>, </span>
3.  <span id="sdk-for-flutter-explore-setMarker3dModel-param-type" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-locationindicatormarkertype">LocationIndicatorMarkerType</a></span> <span class="parameter-name">type</span></span>

)

</div>

<div class="section desc markdown">

Sets the MapMarker3DModel asset to be displayed as location indicator for a specified type.

The 3D model should be oriented with y axis up and thus standing on the x/z plane where the z axis is the depth. The direction in which the location indicator is pointing is the positive z axis. Please note that only MapMarker3DModel created from \*.obj files are supported. Models created from Mesh will be ignored.

- `model` The MapMarker3DModel object to be displayed for the specified type. Only models created from obj files are supported. Those created from mesh will be ignored.

- `scale` The scaling which will be applied to the marker model. As the size of the location marker should be aligned on devices with different resolutions the scale factor is applied relative to the ppi value and thus differs from the scale which is passed to <a href="sdk-for-flutter-explore-mapview-mapmarker3d-class">MapMarker3D</a> objects. Meter is used for the unit of the map marker 3d model coordinate system. For historical reason, the scale factor is internally devided by 6. To display a unit qube of 1x1x1 meter as is, please use a scale value of 6.0.

- `type` The type of location marker for which the marker 3d model should be replaced.

</div>

## Implementation

``` dart
@Deprecated("Will be removed in v4.27.0. Please use the `setMarker3dModelWithRenderSizeUnit` instead.")

void setMarker3dModel(MapMarker3DModel model, double scale, LocationIndicatorMarkerType type);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

