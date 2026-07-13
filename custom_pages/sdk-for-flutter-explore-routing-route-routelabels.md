---
title: "routeLabels property - Route class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-route-routelabels"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/Route-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">routeLabels</span> property

</div>

<div id="sdk-for-flutter-explore-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-routing-routelabel-class">RouteLabel</a></span>\></span></span> <span class="name">routeLabels</span>

</div>

<div class="section desc markdown">

A collection containing a maximum of 2 `RouteLabel` instances for the route. It will return an empty list if no labels are available. The main street names or route numbers through which the route is going to pass that differentiate it from other alternatives routes. The labels are ordered by importance based on how much time the route spends on each road segment, not by traversal sequence. This helps users quickly identify and distinguish between different route alternatives when alternative routes have been quested via `RouteOptions`. Gets route labels.

</div>

## Implementation

``` dart
List<RouteLabel> get routeLabels;
```

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

