---
title: "RouteDeviation.withTraveledDistance constructor - RouteDeviation - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-routedeviation-routedeviation-withtraveleddistance"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/RouteDeviation-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">RouteDeviation.withTraveledDistance</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">RouteDeviation.withTraveledDistance</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-withTraveledDistance-param-lastLocationOnRoute" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-navigablelocation-class">NavigableLocation</a>?</span> <span class="parameter-name">lastLocationOnRoute</span>, </span>
2.  <span id="sdk-for-flutter-navigate-withTraveledDistance-param-lastTraveledSectionIndex" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">lastTraveledSectionIndex</span>, </span>
3.  <span id="sdk-for-flutter-navigate-withTraveledDistance-param-traveledDistanceOnLastSectionInMeters" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">traveledDistanceOnLastSectionInMeters</span>, </span>
4.  <span id="sdk-for-flutter-navigate-withTraveledDistance-param-currentLocation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-navigablelocation-class">NavigableLocation</a></span> <span class="parameter-name">currentLocation</span>, </span>

)

</div>

<div class="section desc markdown">

Creates a new instance.

- `lastLocationOnRoute` The last known location on the route.
- `lastTraveledSectionIndex` Indicates the index of the last traveled route section.
- `traveledDistanceOnLastSectionInMeters` Offset in meter to the last visited position on the route section defined by the last traveled section index.
- `currentLocation` The current location.

</div>

## Implementation

``` dart
RouteDeviation.withTraveledDistance(this.lastLocationOnRoute, this.lastTraveledSectionIndex, this.traveledDistanceOnLastSectionInMeters, this.currentLocation);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

