---
title: "containsGeoCoordinates method - GeoBox class - core library - Dart API"
slug: "sdk-for-flutter-explore-core-geobox-containsgeocoordinates"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core/GeoBox-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">containsGeoCoordinates</span> method

</div>

<div class="section multi-line-signature">

<span class="returntype">bool</span> <span class="name">containsGeoCoordinates</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-containsGeoCoordinates-param-geoCoordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">geoCoordinates</span></span>

)

</div>

<div class="section desc markdown">

Determines whether the specified GeoCoordinates is contained within this `GeoBox`.

The altitude values are ignored.

- `geoCoordinates` A GeoCoordinates to check for containment within this `GeoBox`.

Returns `bool`. `true` if contained within the `GeoBox`, `false` otherwise.

</div>

## Implementation

``` dart
bool containsGeoCoordinates(GeoCoordinates geoCoordinates) => $prototype.containsGeoCoordinates(this, geoCoordinates);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

