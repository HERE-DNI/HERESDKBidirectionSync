---
title: "orbitBy method - MapCameraUpdateFactory class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-orbitby"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapCameraUpdateFactory-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">orbitBy</span> static method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a></span> <span class="name">orbitBy</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-orbitBy-param-delta" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geoorientationupdate-class">GeoOrientationUpdate</a></span> <span class="parameter-name">delta</span>, </span>
2.  <span id="sdk-for-flutter-navigate-orbitBy-param-origin" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-point2d-class">Point2D</a></span> <span class="parameter-name">origin</span></span>

)

</div>

<div class="section desc markdown">

Creates an update to orbit map camera around a pixel origin by specified geodetic orientation delta.

If the origin cannot be converted to geo coordinates, no update will be applied to the map camera.

Orientation elements that are not valid will be excluded from the update. Resulting bearing values are wrapped around degrees range \[0, 360\]. Resulting tilt values are clamped inside degrees range \[0, 180\]. Resulting roll values are wrapped around degrees range \[-180, 180\].

- `delta` Geodetic orientation delta update.

- `origin` Screen pixel origin of rotation.

Returns <a href="sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a>. MapCameraUpdate instance.

</div>

## Implementation

``` dart
static MapCameraUpdate orbitBy(GeoOrientationUpdate delta, Point2D origin) => $prototype.orbitBy(delta, origin);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

