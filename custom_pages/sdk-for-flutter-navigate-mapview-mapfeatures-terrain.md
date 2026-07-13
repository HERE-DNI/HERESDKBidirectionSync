---
title: "terrain property - MapFeatures class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapfeatures-terrain"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- terrain.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapFeatures-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">terrain</span> property

</div>

<div class="section multi-line-signature">

String <span class="name">terrain</span>

<div class="features">

<span class="feature">final</span>

</div>

</div>

<div class="section desc markdown">

Show elevation topography.

Supported modes: <a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-terrainhillshade">MapFeatureModes.terrainHillshade</a>, <a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-terrain3d">MapFeatureModes.terrain3d</a>.

<a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-terrainhillshade">MapFeatureModes.terrainHillshade</a> is only supported for schemes <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.normalDay</a>, <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.normalNight</a>, <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.liteDay</a>, <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.liteNight</a>, <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.logisticsDay</a> and <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.logisticsNight</a>, <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.topoDay</a> and <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.topoNight</a>.

Default mode is <a href="sdk-for-flutter-navigate-mapview-mapfeaturemodes-terrainhillshade">MapFeatureModes.terrainHillshade</a> for the supporting schemes.

By default, terrain is disabled, except for <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.topoDay</a> and <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.topoNight</a>.

Note that this feature has performance implications, with extra data use and impact on frame rate. If performance is a concern, this feature can be disabled from the application side when loading the map scene.

Not supported for <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.satellite</a>, <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.roadNetworkDay</a> and <a href="sdk-for-flutter-navigate-mapview-mapscheme">MapScheme.roadNetworkNight</a>.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

</div>

## Implementation

``` dart
static final String terrain = "terrain";
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
