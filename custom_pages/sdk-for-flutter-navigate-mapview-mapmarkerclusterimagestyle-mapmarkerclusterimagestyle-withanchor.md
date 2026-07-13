---
title: "MapMarkerClusterImageStyle.withAnchor constructor - MapMarkerClusterImageStyle - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapmarkerclusterimagestyle-mapmarkerclusterimagestyle-withanchor"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapMarkerClusterImageStyle.withAnchor.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapMarkerClusterImageStyle-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">MapMarkerClusterImageStyle.withAnchor</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">MapMarkerClusterImageStyle.withAnchor</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-withAnchor-param-image" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapimage-class">MapImage</a></span> <span class="parameter-name">image</span>, </span>
2.  <span id="sdk-for-flutter-navigate-withAnchor-param-anchor" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-anchor2d-class">Anchor2D</a></span> <span class="parameter-name">anchor</span></span>

)

</div>

<div class="section desc markdown">

Creates a cluster marker image style using a map image with anchor.

The anchor is a way of specifying position offset relative to image's dimensions on the screen. For example, (0, 0) places the top-left corner of the image at the cluster's position. (1, 1) would place the bottom-right corner of the image at the cluster's position.

- `image` The map image for the cluster marker.

- `anchor` The anchor point for the marker image which specifies the position offset relative to the cluster's position.

</div>

## Implementation

``` dart
factory MapMarkerClusterImageStyle.withAnchor(MapImage image, Anchor2D anchor) => $prototype.withAnchor(image, anchor);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
