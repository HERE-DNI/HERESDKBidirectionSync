---
title: "zoomBy method - MapCameraUpdateFactory class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapcameraupdatefactory-zoomby"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapCameraUpdateFactory-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">zoomBy</span> static method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-explore-mapview-mapcameraupdate-class">MapCameraUpdate</a></span> <span class="name">zoomBy</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-zoomBy-param-factor" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">factor</span>, </span>
2.  <span id="sdk-for-flutter-explore-zoomBy-param-origin" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-point2d-class">Point2D</a></span> <span class="parameter-name">origin</span></span>

)

</div>

<div class="section desc markdown">

Creates an update to zoom map camera by a given factor preserving a given focus point.

Values greater than 1 zoom in map camera, by moving it closer to the ground; less than 1 - zoom out, which moves map camera further.

If factor is zero, negative or not finite, no update will be applied to the map camera.

If the focusPoint is not inside the viewport bounds, then the current principal point will be used.

- `factor` Zooming factor.

- `origin` Pixel location on the screen to use as zoom origin.

Returns <a href="sdk-for-flutter-explore-mapview-mapcameraupdate-class">MapCameraUpdate</a>. MapCameraUpdate instance.

</div>

## Implementation

``` dart
static MapCameraUpdate zoomBy(double factor, Point2D origin) => $prototype.zoomBy(factor, origin);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

