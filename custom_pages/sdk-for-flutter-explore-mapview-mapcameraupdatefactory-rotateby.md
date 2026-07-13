---
title: "rotateBy method - MapCameraUpdateFactory class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapcameraupdatefactory-rotateby"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapCameraUpdateFactory-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">rotateBy</span> static method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-explore-mapview-mapcameraupdate-class">MapCameraUpdate</a></span> <span class="name">rotateBy</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-rotateBy-param-delta" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geoorientationupdate-class">GeoOrientationUpdate</a></span> <span class="parameter-name">delta</span></span>

)

</div>

<div class="section desc markdown">

Creates an update to change map camera orientation by specified geodetic orientation delta.

Orientation elements that are not valid will be excluded from the update. Resulting bearing values are wrapped around degrees range \[0, 360\]. Resulting tilt values are clamped inside degrees range \[0, 180\]. Resulting roll values are wrapped around degrees range \[-180, 180\].

- `delta` Geodetic orientation delta update.

Returns <a href="sdk-for-flutter-explore-mapview-mapcameraupdate-class">MapCameraUpdate</a>. MapCameraUpdate instance.

</div>

## Implementation

``` dart
static MapCameraUpdate rotateBy(GeoOrientationUpdate delta) => $prototype.rotateBy(delta);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

