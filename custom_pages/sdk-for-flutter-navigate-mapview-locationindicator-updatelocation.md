---
title: "updateLocation method - LocationIndicator class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-locationindicator-updatelocation"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/LocationIndicator-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">updateLocation</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">updateLocation</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-updateLocation-param-location" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-location-class">Location</a></span> <span class="parameter-name">location</span></span>

)

</div>

<div class="section desc markdown">

Updates the indicator to a new location.

If accuracy visualized is set to `true` the field <a href="sdk-for-flutter-navigate-core-location-horizontalaccuracyinmeters">Location.horizontalAccuracyInMeters</a> determines the size of the accuracy indicator halo.

The altitude of the location is ignored.

- `location` The updated location of the user.

</div>

## Implementation

``` dart
void updateLocation(Location location);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

