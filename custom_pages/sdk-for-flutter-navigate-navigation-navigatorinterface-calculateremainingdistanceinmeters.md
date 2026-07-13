---
title: "calculateRemainingDistanceInMeters method - NavigatorInterface class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-navigatorinterface-calculateremainingdistanceinmeters"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/NavigatorInterface-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">calculateRemainingDistanceInMeters</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">int?</span> <span class="name">calculateRemainingDistanceInMeters</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-calculateRemainingDistanceInMeters-param-coordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">coordinates</span></span>

)

</div>

<div class="section desc markdown">

This method calculates the distance between the current position and given coordinates.

The coordinates must be on the polyline.

- `coordinates` The geographic coordinates of the location.

Returns `int?`. distance in meters or null if given coordinates are not on route or given coordinates were already traversed.

</div>

## Implementation

``` dart
int? calculateRemainingDistanceInMeters(GeoCoordinates coordinates);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

