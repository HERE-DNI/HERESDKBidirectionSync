---
title: "ambientOcclusion property - MapFeatures class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapfeatures-ambientocclusion"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapFeatures-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">ambientOcclusion</span> property

</div>

<div class="section multi-line-signature">

String <span class="name">ambientOcclusion</span>

<div class="features">

<span class="feature">final</span>

</div>

</div>

<div class="section desc markdown">

Ambient occlusion effect for 3D geometries (extruded buildings and landmarks).

Supports only one mode: <a href="sdk-for-flutter-explore-mapview-mapfeaturemodes-ambientocclusionall">MapFeatureModes.ambientOcclusionAll</a>.

This visual effect has a performance impact and should be considered only for devices with sufficient performance.

Not supported for <a href="sdk-for-flutter-explore-mapview-mapscheme">MapScheme.satellite</a>, <a href="sdk-for-flutter-explore-mapview-mapscheme">MapScheme.roadNetworkDay</a>, <a href="sdk-for-flutter-explore-mapview-mapscheme">MapScheme.roadNetworkNight</a> and all hybrid schemes: <a href="sdk-for-flutter-explore-mapview-mapscheme">MapScheme.hybridDay</a> <a href="sdk-for-flutter-explore-mapview-mapscheme">MapScheme.hybridNight</a>, <a href="sdk-for-flutter-explore-mapview-mapscheme">MapScheme.liteHybridDay</a> <a href="sdk-for-flutter-explore-mapview-mapscheme">MapScheme.liteHybridNight</a>, <a href="sdk-for-flutter-explore-mapview-mapscheme">MapScheme.logisticsHybridDay</a> and <a href="sdk-for-flutter-explore-mapview-mapscheme">MapScheme.logisticsHybridNight</a>.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process. By default, this map feature is not enabled.

</div>

## Implementation

``` dart
static final String ambientOcclusion = "ambient occlusion";
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

