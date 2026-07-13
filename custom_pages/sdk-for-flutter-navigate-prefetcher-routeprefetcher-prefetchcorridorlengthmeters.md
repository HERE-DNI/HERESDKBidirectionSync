---
title: "prefetchCorridorLengthMeters property - RoutePrefetcher class - prefetcher library - Dart API"
slug: "sdk-for-flutter-navigate-prefetcher-routeprefetcher-prefetchcorridorlengthmeters"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="prefetcher/RoutePrefetcher-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">prefetchCorridorLengthMeters</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype">int</span> <span class="name">prefetchCorridorLengthMeters</span>

</div>

<div class="section desc markdown">

The length of the corridor along the route in front of the car which will be used to prefetch data. Upper limit for length is 50000 meters, when the requested length is greater than upper limit, then 50000 meters set. Lower limit for length is 1000 meters, when the requested length is less than lower limit, then 1000 meters set. The route corridor has a default length of 10 km and a width of 5 km. Gets the length of the corridor along the route in front of the car which will be used to prefetch data.

</div>

## Implementation

``` dart
int get prefetchCorridorLengthMeters;
```

</div>

<div id="sdk-for-flutter-navigate-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">prefetchCorridorLengthMeters=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-prefetchCorridorLengthMeters-param-value" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

The length of the corridor along the route in front of the car which will be used to prefetch data. Upper limit for length is 50000 meters, when the requested length is greater than upper limit, then 50000 meters set. Lower limit for length is 1000 meters, when the requested length is less than lower limit, then 1000 meters set. The route corridor has a default length of 10 km and a width of 5 km. Sets the length of the corridor along the route in front of the car which will be used to prefetch data.

</div>

## Implementation

``` dart
set prefetchCorridorLengthMeters(int value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

