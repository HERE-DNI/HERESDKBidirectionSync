---
title: "landmarks property - MapFeatures class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapfeatures-landmarks"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapFeatures-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">landmarks</span> property

</div>

<div class="section multi-line-signature">

String <span class="name">landmarks</span>

<div class="features">

<span class="feature">final</span>

</div>

</div>

<div class="section desc markdown">

Displays 3D landmarks on the map.

Please note: Enabling 3D landmarks with 3D terrain may result in instances where landmarks sink into or float above the terrain.

Supported modes: <a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-landmarkstextured">MapFeatureModes.landmarksTextured</a>, <a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-landmarksgrayscale">MapFeatureModes.landmarksGrayscale</a> and <a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-landmarkstextureless">MapFeatureModes.landmarksTextureless</a>.

Default mode is <a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-landmarksgrayscale">MapFeatureModes.landmarksGrayscale</a>.

By default, 3D landmarks are enabled on all compatible map schemes.

Not supported for <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.satellite</a>, <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.roadNetworkDay</a>, <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.roadNetworkNight</a> and all hybrid schemes: <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.hybridDay</a> <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.hybridNight</a>, <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.liteHybridDay</a> <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.liteHybridNight</a>, <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.logisticsHybridDay</a> and <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.logisticsHybridNight</a>.

</div>

## Implementation

``` dart
static final String landmarks = "building landmarks";
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

