---
title: "LayerConfiguration constructor - LayerConfiguration - core.engine library - Dart API"
slug: "sdk-for-flutter-explore-core.engine-layerconfiguration-layerconfiguration"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/LayerConfiguration-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">LayerConfiguration</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">LayerConfiguration</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-param-enabledFeatures" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></span>\></span></span> <span class="parameter-name">enabledFeatures</span></span>

)

</div>

<div class="section desc markdown">

Initializes both, `enabled_features` and `implicitly_prefetched_features` with value passed to constructor.

- `enabledFeatures` List of map features to downloader through `MapDownloader`, and implicitly prefetch when using `MapView`

</div>

## Implementation

``` dart
factory LayerConfiguration(List<LayerConfigurationFeature> enabledFeatures) => $prototype.$init(enabledFeatures);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

