---
title: "RefreshRouteOptions.withTaxiOptions constructor - RefreshRouteOptions - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-refreshrouteoptions-refreshrouteoptions-withtaxioptions"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/RefreshRouteOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">RefreshRouteOptions.withTaxiOptions</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">RefreshRouteOptions.withTaxiOptions</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-withTaxiOptions-param-taxiOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-taxioptions-class" class="deprecated">TaxiOptions</a></span> <span class="parameter-name">taxiOptions</span></span>

)

</div>

<div class="section desc markdown">

Constructs a RefreshRouteOptions object with <a href="sdk-for-flutter-explore-routing-taxioptions-class" class="deprecated">TaxiOptions</a>.

- `taxiOptions` Converts the route to a taxi route, if a different transport mode was used for the <a href="sdk-for-flutter-explore-routing-routehandle-class">RouteHandle</a>. Note that in case this is not possible, an <a href="sdk-for-flutter-explore-routing-routingerror">RoutingError.noRouteFound</a> error will be triggered.

</div>

## Implementation

``` dart
factory RefreshRouteOptions.withTaxiOptions(TaxiOptions taxiOptions) => $prototype.withTaxiOptions(taxiOptions);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

