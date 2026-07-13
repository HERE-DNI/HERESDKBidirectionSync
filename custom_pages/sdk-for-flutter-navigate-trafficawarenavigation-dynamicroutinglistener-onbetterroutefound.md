---
title: "onBetterRouteFound method - DynamicRoutingListener class - trafficawarenavigation library - Dart API"
slug: "sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutinglistener-onbetterroutefound"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- onBetterRouteFound.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="trafficawarenavigation/DynamicRoutingListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">onBetterRouteFound</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">onBetterRouteFound</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-onBetterRouteFound-param-newRoute" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-route-class">Route</a></span> <span class="parameter-name">newRoute</span>, </span>
2.  <span id="sdk-for-flutter-navigate-onBetterRouteFound-param-etaDifferenceInSeconds" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">etaDifferenceInSeconds</span>, </span>
3.  <span id="sdk-for-flutter-navigate-onBetterRouteFound-param-distanceDifferenceInMeters" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">distanceDifferenceInMeters</span></span>

)

</div>

<div class="section desc markdown">

This event is issued when a better route could be found, as defined by <a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengineoptions-class">DynamicRoutingEngineOptions</a>.

To find a better route, two routes are calculated. The updated current route: A route that is calculated via the route specified. The dynamic route: A route that starts at the current position on the route specified and passes through the remaining waypoints.

- `newRoute` The newly calculated route with the remaining waypoints starting from the current location.

- `etaDifferenceInSeconds` The difference in seconds: eta of the current updated route - eta of the dynamic route.

- `distanceDifferenceInMeters` The difference in meters: distance of the current updated route - distance of the dynamic route. The value can be negative in case the current updated route has a shorter distance, but its now assumed to be longer than the dynamic route.

</div>

## Implementation

``` dart
void onBetterRouteFound(Route newRoute, int etaDifferenceInSeconds, int distanceDifferenceInMeters);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
