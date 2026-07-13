---
title: "setPrincipalPoint method - MapCameraUpdateFactory class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-setprincipalpoint"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapCameraUpdateFactory-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">setPrincipalPoint</span> static method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a></span> <span class="name">setPrincipalPoint</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-setPrincipalPoint-param-principalPoint" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-point2d-class">Point2D</a></span> <span class="parameter-name">principalPoint</span></span>

)

</div>

<div class="section desc markdown">

Creates an update to change the map camera's principal point (where the view vector intersects the image plane - default is the center of the view).

Point values are in screen coordinates and values that fall outside of the viewport, are clamped. (0,0) is top left of the viewport.

- `principalPoint` Principal point in absolute viewport pixel coordinates.

Returns <a href="sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a>. MapCameraUpdate instance.

</div>

## Implementation

``` dart
static MapCameraUpdate setPrincipalPoint(Point2D principalPoint) => $prototype.setPrincipalPoint(principalPoint);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

