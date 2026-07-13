---
title: "enableTolls property - RouteOptions class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-routeoptions-enabletolls"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/RouteOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">enableTolls</span> property

</div>

<div class="section multi-line-signature">

bool <span class="name">enableTolls</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

A flag that indicates whether the resulting route <a href="sdk-for-flutter-explore-routing-section-tolls">Section.tolls</a> properties should contain tolls data. Defaults to `false`.

**Note:** When a route calculation request asks tolls, a pricing scheme with higher rates might be applied. Consult your HERE representative to get more information on the related pricing schemes.

**Note:** For users of the `OfflineRoutingEngine` this is a beta release of this feature, so there could be a few bugs and unexpected behaviors. The `OfflineRoutingEngine` is only available for the Navigate license. For users of the `RoutingEngine` the feature is stable.

</div>

## Implementation

``` dart
bool enableTolls;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

