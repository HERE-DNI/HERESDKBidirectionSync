---
title: "publicTransit property - MapFeatures class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapfeatures-publictransit"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapFeatures-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">publicTransit</span> property

</div>

<div class="section multi-line-signature">

String <span class="name">publicTransit</span>

<div class="features">

<span class="feature">final</span>

</div>

</div>

<div class="section desc markdown">

Toggles the display of public transit lines for systems like subway, tram, train, monorail, and ferry, based on the selected mode.

Supported modes: <a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-publictransitall">MapFeatureModes.publicTransitAll</a>, <a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-publictransitasia">MapFeatureModes.publicTransitAsia</a>.

<a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-publictransitasia">MapFeatureModes.publicTransitAsia</a> is supported only when credentials enabled for the enriched Japan map are used.

Public transit is disabled by default for all map schemes when using Rest-of-World map data. When using enriched Japan map data, public transit is enabled by default with <a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-publictransitasia">MapFeatureModes.publicTransitAsia</a> on normal, lite and topo schemes (including their hybrid variants) and disabled by default on logistics schemes.

Not supported for <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.satellite</a>, <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.roadNetworkDay</a> and <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.roadNetworkNight</a>.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

</div>

## Implementation

``` dart
static final String publicTransit = "public transit";
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

