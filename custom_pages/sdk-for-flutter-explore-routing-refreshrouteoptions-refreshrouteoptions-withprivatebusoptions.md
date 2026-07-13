---
title: "RefreshRouteOptions.withPrivateBusOptions constructor - RefreshRouteOptions - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-refreshrouteoptions-refreshrouteoptions-withprivatebusoptions"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/RefreshRouteOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">RefreshRouteOptions.withPrivateBusOptions</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">RefreshRouteOptions.withPrivateBusOptions</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-withPrivateBusOptions-param-privateBusOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-privatebusoptions-class" class="deprecated">PrivateBusOptions</a></span> <span class="parameter-name">privateBusOptions</span></span>

)

</div>

<div class="section desc markdown">

Constructs a RefreshRouteOptions object with <a href="sdk-for-flutter-explore-routing-privatebusoptions-class" class="deprecated">PrivateBusOptions</a>.

- `privateBusOptions` Converts the route to a private bus route, if a different transport mode was used for the <a href="sdk-for-flutter-explore-routing-routehandle-class">RouteHandle</a>. Note that in case this is not possible, an <a href="sdk-for-flutter-explore-routing-routingerror">RoutingError.noRouteFound</a> error will be triggered.

</div>

## Implementation

``` dart
factory RefreshRouteOptions.withPrivateBusOptions(PrivateBusOptions privateBusOptions) => $prototype.withPrivateBusOptions(privateBusOptions);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

