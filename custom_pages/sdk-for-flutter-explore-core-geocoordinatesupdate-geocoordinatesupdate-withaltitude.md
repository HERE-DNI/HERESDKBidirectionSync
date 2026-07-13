---
title: "GeoCoordinatesUpdate.withAltitude constructor - GeoCoordinatesUpdate - core library - Dart API"
slug: "sdk-for-flutter-explore-core-geocoordinatesupdate-geocoordinatesupdate-withaltitude"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- GeoCoordinatesUpdate.withAltitude.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core/GeoCoordinatesUpdate-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">GeoCoordinatesUpdate.withAltitude</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">GeoCoordinatesUpdate.withAltitude</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-withAltitude-param-latitude" class="parameter"><span class="type-annotation">double?</span> <span class="parameter-name">latitude</span>, </span>
2.  <span id="sdk-for-flutter-explore-withAltitude-param-longitude" class="parameter"><span class="type-annotation">double?</span> <span class="parameter-name">longitude</span>, </span>
3.  <span id="sdk-for-flutter-explore-withAltitude-param-altitude" class="parameter"><span class="type-annotation">double?</span> <span class="parameter-name">altitude</span></span>

)

</div>

<div class="section desc markdown">

Constructs a GeoCoordinatesUpdate from the provided latitude, longitude and alt values.

Corrects values of latitude and longitude if they exceed the ranges.

- `latitude` Latitude in degrees. Positive value means Northern hemisphere. If the value is out of range of \[-90.0, 90.0\] it's clamped to that range. NaN value is converted to `null`.

- `longitude` Longitude in degrees. Positive value means Eastern hemisphere. If the value is out of range of \[-180.0, 180.0\] it's replaced with a value within the range, representing effectively the same meridian. NaN value is converted to `null`.

- `altitude` Altitude in meters. NaN value is converted to `null`.

</div>

## Implementation

``` dart
factory GeoCoordinatesUpdate.withAltitude(double? latitude, double? longitude, double? altitude) => $prototype.withAltitude(latitude, longitude, altitude);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
