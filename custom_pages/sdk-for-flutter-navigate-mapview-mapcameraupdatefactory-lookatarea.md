---
title: "lookAtArea method - MapCameraUpdateFactory class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-lookatarea"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lookAtArea.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapCameraUpdateFactory-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">lookAtArea</span> static method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a></span> <span class="name">lookAtArea</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-lookAtArea-param-target" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geobox-class">GeoBox</a></span> <span class="parameter-name">target</span></span>

)

</div>

<div class="section desc markdown">

Creates an update to look at the given geo-box, preserving current orientation and zooming at the center of viewport.

If geoBox is not valid, no update will be applied to the map camera.

The altitude of the target points is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.

- `target` Geodetic box that should be visible inside the viewport rectangle.

Returns <a href="sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a>. MapCameraUpdate instance.

</div>

## Implementation

``` dart
static MapCameraUpdate lookAtArea(GeoBox target) => $prototype.lookAtArea(target);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
