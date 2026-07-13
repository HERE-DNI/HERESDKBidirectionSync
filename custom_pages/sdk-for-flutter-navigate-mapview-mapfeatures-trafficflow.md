---
title: "trafficFlow property - MapFeatures class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapfeatures-trafficflow"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- trafficFlow.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapFeatures-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">trafficFlow</span> property

</div>

<div class="section multi-line-signature">

String <span class="name">trafficFlow</span>

<div class="features">

<span class="feature">final</span>

</div>

</div>

<div class="section desc markdown">

Traffic flow speed. An online connection is required for the traffic flow to be shown.

If the offline-mode is enabled for offline maps usage, the live traffic flow can still be shown in offline mode by enabling pass-through feature for traffic flow on `sdk.core.engine.SDKNativeEngine`. See `sdk.core.engine.SDKNativeEngine.pass_through_features` for details.

Supported modes:

- <a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-trafficflowjapanwithoutfreeflow">MapFeatureModes.trafficFlowJapanWithoutFreeFlow</a>,
- <a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-trafficflowwithfreeflow">MapFeatureModes.trafficFlowWithFreeFlow</a>,
- <a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-trafficflowwithoutfreeflow">MapFeatureModes.trafficFlowWithoutFreeFlow</a>.

Default mode is <a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-trafficflowwithfreeflow">MapFeatureModes.trafficFlowWithFreeFlow</a>.

Not supported for <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.satellite</a>, <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.roadNetworkDay</a> and <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.roadNetworkNight</a>. By default, this map feature is not enabled.

</div>

## Implementation

``` dart
static final String trafficFlow = "traffic flow";
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
