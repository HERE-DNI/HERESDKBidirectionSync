---
title: "MapMarker constructor - MapMarker - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapmarker-mapmarker"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapMarker-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">MapMarker</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">MapMarker</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-coordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">coordinates</span>, </span>
2.  <span id="sdk-for-flutter-navigate-param-image" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapimage-class">MapImage</a></span> <span class="parameter-name">image</span></span>

)

</div>

<div class="section desc markdown">

Creates an instance of a marker at given coordinates, represented by specified image.

The altitude component of the coordinates is ignored.

- `coordinates` The marker's geographical coordinates.

- `image` The image to draw on the map.

</div>

## Implementation

``` dart
factory MapMarker(GeoCoordinates coordinates, MapImage image) => $prototype.$init(coordinates, image);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

