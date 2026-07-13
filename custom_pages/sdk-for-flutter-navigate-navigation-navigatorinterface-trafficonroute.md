---
title: "trafficOnRoute property - NavigatorInterface class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-navigatorinterface-trafficonroute"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/NavigatorInterface-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">trafficOnRoute</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-routing-trafficonroute-class">TrafficOnRoute</a>?</span> <span class="name">trafficOnRoute</span>

</div>

<div class="section desc markdown">

Traffic information for the current route. This impacts `RouteProgress` updates as the duration of the `SectionProgress` might change. However, the remaining distance and the route geometry will remain unchanged. Gets the traffic information for the current route.

</div>

## Implementation

``` dart
TrafficOnRoute? get trafficOnRoute;
```

</div>

<div id="sdk-for-flutter-navigate-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">trafficOnRoute=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-trafficOnRoute-param-value" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-trafficonroute-class">TrafficOnRoute</a>?</span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

Traffic information for the current route. This impacts `RouteProgress` updates as the duration of the `SectionProgress` might change. However, the remaining distance and the route geometry will remain unchanged. Sets the traffic information for the current route.

</div>

## Implementation

``` dart
set trafficOnRoute(TrafficOnRoute? value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

