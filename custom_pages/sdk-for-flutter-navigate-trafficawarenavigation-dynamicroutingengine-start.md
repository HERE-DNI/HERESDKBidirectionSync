---
title: "start method - DynamicRoutingEngine class - trafficawarenavigation library - Dart API"
slug: "sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-start"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- start.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="trafficawarenavigation/DynamicRoutingEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">start</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">start</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-start-param-route" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-route-class">Route</a></span> <span class="parameter-name">route</span>, </span>
2.  <span id="sdk-for-flutter-navigate-start-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutinglistener-class">DynamicRoutingListener</a></span> <span class="parameter-name">listener</span></span>

)

</div>

<div class="section desc markdown">

Starts polling the HERE backend services to find a better route, as defined by the DynamicRoutingEngineOptions.

**Note:** The engine will be internally stopped, if it was started before. Therefore, it is not necessary to stop the engine before starting it again.

- `route` The route to be refreshed. The route must contain a <a href="sdk-for-flutter-navigate-routing-routehandle-class">RouteHandle</a>, therefore the route must have been requested with <a href="sdk-for-flutter-navigate-routing-routeoptions-enableroutehandle">RouteOptions.enableRouteHandle</a> set to `true`. The information to calculate new routes will be extracted from the provided route parameter. If more information from the original waypoints is important besides their location, consider to use one of the overloaded methods instead.

- `listener` The listener to receive the events.

Throws <a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingenginestartexception-class">DynamicRoutingEngineStartException</a>. when the passed parameter are invalid.

</div>

## Implementation

``` dart
void start(Route route, DynamicRoutingListener listener);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
