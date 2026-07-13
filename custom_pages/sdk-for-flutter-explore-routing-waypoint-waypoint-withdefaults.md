---
title: "Waypoint.withDefaults constructor - Waypoint - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-waypoint-waypoint-withdefaults"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/Waypoint-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">Waypoint.withDefaults</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">Waypoint.withDefaults</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-withDefaults-param-coordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">coordinates</span></span>

)

</div>

<div class="section desc markdown">

Creates a new instance.

- `coordinates` The waypoint's geographic coordinates.

</div>

## Implementation

``` dart
Waypoint.withDefaults(this.coordinates)
    : type = WaypointType.stopover, transitRadiusInMeters = 0, headingInDegrees = null, sideOfStreetHint = null, displayLocation = null, minCourseDistanceInMeters = null, nameHint = null, matchSideOfStreet = null, duration = const Duration(seconds: 0), segmentHint = null, onRoadThresholdInMeters = null, chargingStop = null, currentWeightChangeInKilograms = null;
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

