---
title: "Location.withCoordinates constructor - Location - core library - Dart API"
slug: "sdk-for-flutter-explore-core-location-location-withcoordinates"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core/Location-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">Location.withCoordinates</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">Location.withCoordinates</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-withCoordinates-param-coordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">coordinates</span></span>

)

</div>

<div class="section desc markdown">

Creates a new Location instance from the provided GeoCoordinates value. timestamp is initialized with `January 1, 1970, 00:00:00 GMT` value. The rest of the fields will be initialized to null.

- `coordinates` The geographic coordinates of the location.

</div>

## Implementation

``` dart
Location.withCoordinates(this.coordinates)
    : bearingInDegrees = null, speedInMetersPerSecond = null, time = null, horizontalAccuracyInMeters = null, verticalAccuracyInMeters = null, bearingAccuracyInDegrees = null, speedAccuracyInMetersPerSecond = null, timestampSinceBoot = null, locationTechnology = null, source = null, gnssTime = null, pitchInDegrees = null;
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

