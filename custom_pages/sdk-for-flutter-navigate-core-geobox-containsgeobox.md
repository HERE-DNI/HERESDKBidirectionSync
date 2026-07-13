---
title: "containsGeoBox method - GeoBox class - core library - Dart API"
slug: "sdk-for-flutter-navigate-core-geobox-containsgeobox"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core/GeoBox-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">containsGeoBox</span> method

</div>

<div class="section multi-line-signature">

<span class="returntype">bool</span> <span class="name">containsGeoBox</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-containsGeoBox-param-geoBox" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geobox-class">GeoBox</a></span> <span class="parameter-name">geoBox</span></span>

)

</div>

<div class="section desc markdown">

Determines whether the specified `GeoBox` is covered entirely by this `GeoBox`.

The altitude values are ignored.

- `geoBox` A `GeoBox` to check for containment within this `GeoBox`.

Returns `bool`. `true` if covered by the `GeoBox`, `false` otherwise.

</div>

## Implementation

``` dart
bool containsGeoBox(GeoBox geoBox) => $prototype.containsGeoBox(this, geoBox);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

