---
title: "MapImageOverlay.withAnchor constructor - MapImageOverlay - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapimageoverlay-mapimageoverlay-withanchor"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapImageOverlay.withAnchor.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapImageOverlay-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">MapImageOverlay.withAnchor</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">MapImageOverlay.withAnchor</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-withAnchor-param-viewCoordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-point2d-class">Point2D</a></span> <span class="parameter-name">viewCoordinates</span>, </span>
2.  <span id="sdk-for-flutter-explore-withAnchor-param-image" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapimage-class">MapImage</a></span> <span class="parameter-name">image</span>, </span>
3.  <span id="sdk-for-flutter-explore-withAnchor-param-anchor" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-anchor2d-class">Anchor2D</a></span> <span class="parameter-name">anchor</span></span>

)

</div>

<div class="section desc markdown">

Creates an instance of an overlay at given view coordinates, represented by specified image, with anchor point specifying how the image is positioned relative to the overlay's view coordinates.

The anchor is a way of specifying position offset relative to image's dimensions on the view. For example, (0, 0) places the top-left corner of the image at the overlay's view coordinates. (1, 1) would place the bottom-right corner of the image at the overlay's view coordinates. (0.5, 0.5) which is the default value would center the image at the overlay's view coordinates.

Values outside the 0..1 range are also allowed, for example (0.5, 2) would display the image centered horizontally with its bottom edge above the overlay's view coordinates at the distance in pixels that is equal to the height of the image.

- `viewCoordinates` The overlay's view coordinates in pixels.

- `image` The image to draw on the map.

- `anchor` The anchor point for the overlay image which specifies the position offset relative to the overlay's view coordinates.

</div>

## Implementation

``` dart
factory MapImageOverlay.withAnchor(Point2D viewCoordinates, MapImage image, Anchor2D anchor) => $prototype.withAnchor(viewCoordinates, image, anchor);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
