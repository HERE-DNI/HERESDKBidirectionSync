---
title: "isTrafficOnRouteVisible property - VisualNavigator class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-visualnavigator-istrafficonroutevisible"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/VisualNavigator-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">isTrafficOnRouteVisible</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype">bool</span> <span class="name">isTrafficOnRouteVisible</span>

</div>

<div class="section desc markdown">

A boolean which defines whether to perform rendering of traffic conditions on the route when `Route` visualization is enabled during visual navigation. When enabled the route's `MapPolyline` will be enhanced with visualization of the traffic conditions. Colors used for this visualization are defined in <a href="sdk-for-flutter-navigate-navigation-visualnavigatorcolors-trafficonroutecolors">VisualNavigatorColors.trafficOnRouteColors</a>. The presented traffic information is either set by the user via <a href="sdk-for-flutter-navigate-navigation-navigatorinterface-trafficonroute">NavigatorInterface.trafficOnRoute</a> or is generated from historical traffic data stored in the map. **Note:** `VisualNavigator` does not perform automatic traffic data updates. The updated traffic information is available through the `sdk.routing.RoutingEngine.calculate_traffic_on_route` interface. The returned <a href="sdk-for-flutter-navigate-routing-trafficonroute-class">TrafficOnRoute</a> could then be used to update `sdk.navigation.NavigatorInterface.traffic_on_route` to refresh the traffic on route visualization. Defaults to `false`. Gets the current state whether traffic conditions on route should be displayed during visual navigation.

</div>

## Implementation

``` dart
bool get isTrafficOnRouteVisible;
```

</div>

<div id="sdk-for-flutter-navigate-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">isTrafficOnRouteVisible=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-isTrafficOnRouteVisible-param-value" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

A boolean which defines whether to perform rendering of traffic conditions on the route when `Route` visualization is enabled during visual navigation. When enabled the route's `MapPolyline` will be enhanced with visualization of the traffic conditions. Colors used for this visualization are defined in <a href="sdk-for-flutter-navigate-navigation-visualnavigatorcolors-trafficonroutecolors">VisualNavigatorColors.trafficOnRouteColors</a>. The presented traffic information is either set by the user via <a href="sdk-for-flutter-navigate-navigation-navigatorinterface-trafficonroute">NavigatorInterface.trafficOnRoute</a> or is generated from historical traffic data stored in the map. **Note:** `VisualNavigator` does not perform automatic traffic data updates. The updated traffic information is available through the `sdk.routing.RoutingEngine.calculate_traffic_on_route` interface. The returned <a href="sdk-for-flutter-navigate-routing-trafficonroute-class">TrafficOnRoute</a> could then be used to update `sdk.navigation.NavigatorInterface.traffic_on_route` to refresh the traffic on route visualization. Defaults to `false`. Sets whether to perform rendering of traffic conditions on the route when `Route` visualization is enabled during visual navigation.

</div>

## Implementation

``` dart
set isTrafficOnRouteVisible(bool value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

