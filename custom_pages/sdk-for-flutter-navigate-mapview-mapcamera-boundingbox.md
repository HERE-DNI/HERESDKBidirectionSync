---
title: "boundingBox property - MapCamera class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapcamera-boundingbox"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapCamera-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">boundingBox</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-core-geobox-class">GeoBox</a>?</span> <span class="name">boundingBox</span>

</div>

<div class="section desc markdown">

Currently visible map area encompassed in a GeoBox. Note that this bounding box is always rectangular, and its sides are always parallel to the latitude and longitude. If the camera is rotated, the returned bounding box will be a circumscribed rectangle that is larger than the visible map area. Similarly, when the map is tilted (for example, if the map is tilted by 45 degrees), the visible map area represents a trapezoidal area in the world. Resulting value will then be a larger circumscribed rectangle that contains this trapezoid area. Because on this, corners of the resulting bounding box may be located outside of the currently visible area.

When the map area does not fully fill the viewport, `null` is returned. Gets the current visible map area encompassed in a GeoBox.

</div>

## Implementation

``` dart
GeoBox? get boundingBox;
```

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

