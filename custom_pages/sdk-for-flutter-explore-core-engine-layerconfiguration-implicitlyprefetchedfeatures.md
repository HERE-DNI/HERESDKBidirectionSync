---
title: "implicitlyPrefetchedFeatures property - LayerConfiguration class - core.engine library - Dart API"
slug: "sdk-for-flutter-explore-core-engine-layerconfiguration-implicitlyprefetchedfeatures"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/LayerConfiguration-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">implicitlyPrefetchedFeatures</span> property

</div>

<div class="section multi-line-signature">

List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></span>\></span> <span class="name">implicitlyPrefetchedFeatures</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Specifies the list of features enabled for implicit and explicit map prefetch. Implicit map prefetch will download map content for implicit prefetch features when showing a map in the MapView.

Allows to specify an empty list, effectively disabling implicit prefetching. In this case, the system will prioritize minimal network usage, at the cost of reduced offline map availability. When disabling certain implicitly prefetched features, less data will be prefetched when the map is rendered. Map data that was already cached will not be removed until the least recently used strategy (LRU) applies. That means you cannot remove any content from the map cache by updating the `LayerConfiguration`. However, for new map data, it will be applied.

By default the list contains:

- <a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature">LayerConfigurationFeature.navigation</a>

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Implementation

``` dart
List<LayerConfigurationFeature> implicitlyPrefetchedFeatures;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

