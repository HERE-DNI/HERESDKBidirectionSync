---
title: "engineSizeInCubicCentimeters property - VehicleSpecification class - transport library - Dart API"
slug: "sdk-for-flutter-explore-transport-vehiclespecification-enginesizeincubiccentimeters"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="transport/VehicleSpecification-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">engineSizeInCubicCentimeters</span> property

</div>

<div class="section multi-line-signature">

int? <span class="name">engineSizeInCubicCentimeters</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Engine size of the scooter in cubic centimeters. Shouldn't be less than 1 or greater than 65535. Default value is `null`, which means the scooter route calculation ignores all engine size limits on the road.

**Notes**

- For now, this option is only relevant in Japan and will be ignored for other countries. Currently, map data for this option is only available for Japan.
- Supported only in <a href="sdk-for-flutter-explore-transport-transportmode">TransportMode.scooter</a> (Alpha) transport mode.

</div>

## Implementation

``` dart
int? engineSizeInCubicCentimeters;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

