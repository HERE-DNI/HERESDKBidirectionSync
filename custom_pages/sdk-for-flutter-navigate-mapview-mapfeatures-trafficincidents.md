---
title: "trafficIncidents property - MapFeatures class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapfeatures-trafficincidents"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- trafficIncidents.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapFeatures-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">trafficIncidents</span> property

</div>

<div class="section multi-line-signature">

String <span class="name">trafficIncidents</span>

<div class="features">

<span class="feature">final</span>

</div>

</div>

<div class="section desc markdown">

Traffic incidents. An online connection is required for the traffic incidents to be shown.

If the offline-mode is enabled for offline maps usage, the live traffic incidents can still be shown in offline mode by enabling pass-through feature for traffic incidents on `sdk.core.engine.SDKNativeEngine`. See `sdk.core.engine.SDKNativeEngine.pass_through_features` for details.

Supports only one mode: <a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-trafficincidentsall">MapFeatureModes.trafficIncidentsAll</a>.

Not supported for <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.satellite</a>, <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.roadNetworkDay</a> and <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.roadNetworkNight</a>. By default, this map feature is not enabled.

</div>

## Implementation

``` dart
static final String trafficIncidents = "traffic incidents";
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
