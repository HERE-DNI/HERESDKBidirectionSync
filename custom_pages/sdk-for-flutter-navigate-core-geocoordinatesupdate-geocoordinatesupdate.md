---
title: "GeoCoordinatesUpdate constructor - GeoCoordinatesUpdate - core library - Dart API"
slug: "sdk-for-flutter-navigate-core-geocoordinatesupdate-geocoordinatesupdate"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core/GeoCoordinatesUpdate-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">GeoCoordinatesUpdate</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">GeoCoordinatesUpdate</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-latitude" class="parameter"><span class="type-annotation">double?</span> <span class="parameter-name">latitude</span>, </span>
2.  <span id="sdk-for-flutter-navigate-param-longitude" class="parameter"><span class="type-annotation">double?</span> <span class="parameter-name">longitude</span></span>

)

</div>

<div class="section desc markdown">

Constructs a GeoCoordinatesUpdate from the provided latitude and longitude values.

Corrects values of latitude and longitude if they exceed the ranges.

- `latitude` Latitude in degrees. Positive value means Northern hemisphere. If the value is out of range of \[-90.0, 90.0\] it's clamped to that range. NaN value is converted to `null`.

- `longitude` Longitude in degrees. Positive value means Eastern hemisphere. If the value is out of range of \[-180.0, 180.0\] it's replaced with a value within the range, representing effectively the same meridian. NaN value is converted to `null`.

</div>

## Implementation

``` dart
factory GeoCoordinatesUpdate(double? latitude, double? longitude) => $prototype.$init(latitude, longitude);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

