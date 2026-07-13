---
title: "vehicleRestrictions property - MapFeatures class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapfeatures-vehiclerestrictions"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapFeatures-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">vehicleRestrictions</span> property

</div>

<div class="section multi-line-signature">

String <span class="name">vehicleRestrictions</span>

<div class="features">

<span class="feature">final</span>

</div>

</div>

<div class="section desc markdown">

Vehicle restrictions. Requires map version 25 as minimum. If old map data is stored on disk, it might require updating using `MapUpdater`.

Supported modes: <a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-vehiclerestrictionsactive">MapFeatureModes.vehicleRestrictionsActive</a>, <a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-vehiclerestrictionsactiveandinactive">MapFeatureModes.vehicleRestrictionsActiveAndInactive</a> and <a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-vehiclerestrictionsactiveandinactivedifferentiated">MapFeatureModes.vehicleRestrictionsActiveAndInactiveDifferentiated</a>.

Default mode when enabled is <a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-vehiclerestrictionsactiveandinactive">MapFeatureModes.vehicleRestrictionsActiveAndInactive</a>.

Not supported for <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.satellite</a>, <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.roadNetworkDay</a> and <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.roadNetworkNight</a>. By default, this map feature is not enabled.

</div>

## Implementation

``` dart
static final String vehicleRestrictions = "vehicle restrictions";
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

