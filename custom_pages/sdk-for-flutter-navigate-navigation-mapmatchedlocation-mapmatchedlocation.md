---
title: "MapMatchedLocation constructor - MapMatchedLocation - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-mapmatchedlocation-mapmatchedlocation"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/MapMatchedLocation-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">MapMatchedLocation</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">MapMatchedLocation</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-coordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">coordinates</span>, </span>
2.  <span id="sdk-for-flutter-navigate-param-bearingInDegrees" class="parameter"><span class="type-annotation">double?</span> <span class="parameter-name">bearingInDegrees</span></span>

)

</div>

<div class="section desc markdown">

Creates a new instance.

- `coordinates` The geographic coordinates of the map-matched location.
- `bearingInDegrees` The bearing orientation points to the direction of travel, and has the same angle as the street where it is matched to. Therefore, it must not necessarily be the same as the bearing of a location source. Starts at 0 in the geographic north and rotates in a clockwise direction around the compass. It means that for going north it's equal to 0, for northeast it's equal to 45, for east it's equal to 90, and so on. If it cannot be determined, the value is `null`. Otherwise, it is guaranteed to be in the range \[0, 360).

</div>

## Implementation

``` dart
MapMatchedLocation(this.coordinates, this.bearingInDegrees)
    : segmentReference = SegmentReference.withDefaults(), segmentOffsetInCentimeters = 0, confidence = 0.0, isDrivingInTheWrongWay = false, horizontalAccuracyInMeters = null, speedInMetersPerSecond = null, timestamp = null;
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

