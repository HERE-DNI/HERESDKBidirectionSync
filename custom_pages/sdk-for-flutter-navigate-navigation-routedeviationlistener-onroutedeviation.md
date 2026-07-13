---
title: "onRouteDeviation method - RouteDeviationListener class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-routedeviationlistener-onroutedeviation"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/RouteDeviationListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">onRouteDeviation</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">onRouteDeviation</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-onRouteDeviation-param-routeDeviation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-routedeviation-class">RouteDeviation</a></span> <span class="parameter-name">routeDeviation</span></span>

)

</div>

<div class="section desc markdown">

Called whenever route deviation has been observed.

It contains the information that can be used to decide whether to request a re-route calculation from the routing engine.

- `routeDeviation` The route deviation observed.

</div>

## Implementation

``` dart
void onRouteDeviation(RouteDeviation routeDeviation);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

