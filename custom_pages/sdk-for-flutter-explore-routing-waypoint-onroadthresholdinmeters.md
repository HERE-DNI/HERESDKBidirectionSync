---
title: "onRoadThresholdInMeters property - Waypoint class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-waypoint-onroadthresholdinmeters"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/Waypoint-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">onRoadThresholdInMeters</span> property

</div>

<div class="section multi-line-signature">

int? <span class="name">onRoadThresholdInMeters</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Optional threshold allows specifying a distance within which the waypoint could be considered as being on a highway/bridge/tunnel/sliproad. Within this threshold, the attributes of the segments do not impact the matching. Outside the threshold only segments which aren't one of highway/bridge/tunnel/sliproad can be matched.

</div>

## Implementation

``` dart
int? onRoadThresholdInMeters;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

