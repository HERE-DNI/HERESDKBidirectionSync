---
title: "updateCurrentLocation method - DynamicRoutingEngine class - trafficawarenavigation library - Dart API"
slug: "sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-updatecurrentlocation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- updateCurrentLocation.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="trafficawarenavigation/DynamicRoutingEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">updateCurrentLocation</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">updateCurrentLocation</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-updateCurrentLocation-param-mapMatchedLocation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-mapmatchedlocation-class">MapMatchedLocation</a></span> <span class="parameter-name">mapMatchedLocation</span>, </span>
2.  <span id="sdk-for-flutter-navigate-updateCurrentLocation-param-sectionIndex" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">sectionIndex</span></span>

)

</div>

<div class="section desc markdown">

Updates the current location.

This location will be used as new starting point when the next <a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengineoptions-pollinterval">DynamicRoutingEngineOptions.pollInterval</a> is reached and a new route is requested. If an immediate route update is needed, consider to use the RoutingEngine instead. All subsequently calculated routes used for the ETA calculation will start from this location. The location needs to lie on the route or a `RoutingError` will be issued.

- `mapMatchedLocation` The last known location. It is recommended to use a <a href="sdk-for-flutter-navigate-navigation-navigablelocation-mapmatchedlocation">NavigableLocation.mapMatchedLocation</a> as the driver is expected to be on a road.

- `sectionIndex` The current section from <a href="sdk-for-flutter-navigate-navigation-routeprogress-sectionindex" class="deprecated">RouteProgress.sectionIndex</a>.

</div>

## Implementation

``` dart
void updateCurrentLocation(MapMatchedLocation mapMatchedLocation, int sectionIndex);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
