---
title: "MapMarker.withAnchor constructor - MapMarker - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapmarker-mapmarker-withanchor"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapMarker-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">MapMarker.withAnchor</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">MapMarker.withAnchor</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-withAnchor-param-coordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">coordinates</span>, </span>
2.  <span id="sdk-for-flutter-explore-withAnchor-param-image" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapimage-class">MapImage</a></span> <span class="parameter-name">image</span>, </span>
3.  <span id="sdk-for-flutter-explore-withAnchor-param-anchor" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-anchor2d-class">Anchor2D</a></span> <span class="parameter-name">anchor</span></span>

)

</div>

<div class="section desc markdown">

Creates an instance of a marker at given coordinates, represented by specified image, with anchor point specifying how the image is positioned relative to the marker's coordinates.

The anchor is a way of specifying position offset relative to image's dimensions on the screen. For example, (0, 0) places the top-left corner of the image at the marker's coordinates. (1, 1) would place the bottom-right corner of the image at the marker's coordinates. (0.5, 0.5) which is the default value would center the image at the marker's coordinates. Values outside the 0..1 range are also allowed, for example (0.5, 2) would display the image centered horizontally with its bottom edge above the marker's coordinates at the distance in pixels that is equal to the height of the image.

- `coordinates` The marker's geographical coordinates.

- `image` The image to draw on the map.

- `anchor` The anchor point for the marker image which specifies the position offset relative to the marker's coordinates.

</div>

## Implementation

``` dart
factory MapMarker.withAnchor(GeoCoordinates coordinates, MapImage image, Anchor2D anchor) => $prototype.withAnchor(coordinates, image, anchor);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

