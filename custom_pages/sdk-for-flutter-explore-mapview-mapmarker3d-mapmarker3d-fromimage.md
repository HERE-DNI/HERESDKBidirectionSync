---
title: "MapMarker3D.fromImage constructor - MapMarker3D - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapmarker3d-mapmarker3d-fromimage"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapMarker3D.fromImage.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapMarker3D-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">MapMarker3D.fromImage</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">MapMarker3D.fromImage</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-fromImage-param-at" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">at</span>, </span>
2.  <span id="sdk-for-flutter-explore-fromImage-param-image" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapimage-class">MapImage</a></span> <span class="parameter-name">image</span>, </span>
3.  <span id="sdk-for-flutter-explore-fromImage-param-scale" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">scale</span>, </span>
4.  <span id="sdk-for-flutter-explore-fromImage-param-unit" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-rendersizeunit">RenderSizeUnit</a></span> <span class="parameter-name">unit</span>, </span>

)

</div>

<div class="section desc markdown">

Creates a flat marker from provided map image.

Such map marker is a flat 3D marker of rectangular shape textured with given image. Aspect ratio of the flat marker is determined by aspect ratio of the image.

Only bitmap images are supported, using a <a href="sdk-for-flutter-explore-mapview-mapimage-class">MapImage</a> created from SVG data will result in distorted rendering of the flat marker.

Altitude component of the coordinates, if set, controls 3D marker's elevation above ground. If not set, the 3D marker is placed at ground level.

Size of the rendered flat marker can be specified in either world or screen coordinate space.

For <a href="sdk-for-flutter-explore-mapview-rendersizeunit">RenderSizeUnit.pixels</a>, the flat marker will cover `MapMarker3D.fromImage.scale` \* image's width pixels horizontally and `MapMarker3D.fromImage.scale` \* image's height pixels vertically. The size of the flat marker remains constant on the screen.

For <a href="sdk-for-flutter-explore-mapview-rendersizeunit">RenderSizeUnit.densityIndependentPixels</a> the flat marker will cover `MapMarker3D.fromImage.scale` \* image's width density independent pixels horizontally and `MapMarker3D.fromImage.scale` \* image's height density independent pixels vertically. The size of the flat marker remains constant on the screen.

For <a href="sdk-for-flutter-explore-mapview-rendersizeunit">RenderSizeUnit.meters</a> the flat marker will cover `MapMarker3D.fromImage.scale` \* image's width meters horizontally and `MapMarker3D.fromImage.scale` \* image's height meters vertically. Unlike with pixels or density independent pixels the size of the flat marker will grow and shrink together with regular map content like streets or buildings.

- `at` The geographical coordinates where the flat marker is placed corresponding to center of the provided map image.

- `image` The MapImage containing the texture data of the flat marker. SVG images are not supported.

- `scale` Scale factor applied to the dimensions of the image.

- `unit` Determines whether the size of the flat marker is represented in world or in screen space.

</div>

## Implementation

``` dart
factory MapMarker3D.fromImage(GeoCoordinates at, MapImage image, double scale, RenderSizeUnit unit) => $prototype.fromImage(at, image, scale, unit);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
