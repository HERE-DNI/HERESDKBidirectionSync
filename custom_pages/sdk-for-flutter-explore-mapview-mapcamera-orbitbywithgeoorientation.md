---
title: "orbitByWithGeoOrientation method - MapCamera class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapcamera-orbitbywithgeoorientation"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapCamera-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">orbitByWithGeoOrientation</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">orbitByWithGeoOrientation</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-orbitByWithGeoOrientation-param-delta" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geoorientationupdate-class">GeoOrientationUpdate</a></span> <span class="parameter-name">delta</span>, </span>
2.  <span id="sdk-for-flutter-explore-orbitByWithGeoOrientation-param-origin" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-point2d-class">Point2D</a></span> <span class="parameter-name">origin</span></span>

)

</div>

<div class="section desc markdown">

Orbits the camera around a specified view point by increasing tilt and bearing by specified delta values.

- `delta` Camera orientation change, containing tilt and bearing angle deltas.

- `origin` Pixel point in view coordinates around which orbiting occurs.

</div>

## Implementation

``` dart
void orbitByWithGeoOrientation(GeoOrientationUpdate delta, Point2D origin);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

