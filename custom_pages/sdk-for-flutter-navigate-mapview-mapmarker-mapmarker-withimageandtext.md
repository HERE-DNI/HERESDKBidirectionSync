---
title: "MapMarker.withImageAndText constructor - MapMarker - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapmarker-mapmarker-withimageandtext"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapMarker-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">MapMarker.withImageAndText</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">MapMarker.withImageAndText</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-withImageAndText-param-coordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">coordinates</span>, </span>
2.  <span id="sdk-for-flutter-navigate-withImageAndText-param-image" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapimage-class">MapImage</a></span> <span class="parameter-name">image</span>, </span>
3.  <span id="sdk-for-flutter-navigate-withImageAndText-param-text" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">text</span></span>

)

</div>

<div class="section desc markdown">

Creates a `MapMarker` instance at given coordinates with specified image and text and a default text style.

The altitude component of the coordinates is ignored.

- `coordinates` The marker's geographical coordinates.

- `image` The image to draw on the map.

- `text` The text to draw on the map.

</div>

## Implementation

``` dart
factory MapMarker.withImageAndText(GeoCoordinates coordinates, MapImage image, String text) => $prototype.withImageAndText(coordinates, image, text);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

