---
title: "lookAtAreaWithGeoOrientation method - MapCamera class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapcamera-lookatareawithgeoorientation"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapCamera-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">lookAtAreaWithGeoOrientation</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">lookAtAreaWithGeoOrientation</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-lookAtAreaWithGeoOrientation-param-target" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geobox-class">GeoBox</a></span> <span class="parameter-name">target</span>, </span>
2.  <span id="sdk-for-flutter-explore-lookAtAreaWithGeoOrientation-param-orientation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geoorientationupdate-class">GeoOrientationUpdate</a></span> <span class="parameter-name">orientation</span></span>

)

</div>

<div class="section desc markdown">

Makes the camera look at the specified geodetic area.

The supplied orientation is the orientation of the camera looking at the target, so the resulting camera state will have the same orientation as the one supplied to this method.

The altitude of the target points is ignored.

- `target` Geodetic area at which the camera will point

- `orientation` Desired orientation of the camera

</div>

## Implementation

``` dart
void lookAtAreaWithGeoOrientation(GeoBox target, GeoOrientationUpdate orientation);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

