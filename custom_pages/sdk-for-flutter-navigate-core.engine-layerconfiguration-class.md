---
title: "LayerConfiguration class - core.engine library - Dart API"
slug: "sdk-for-flutter-navigate-core.engine-layerconfiguration-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LayerConfiguration-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/core.engine-library-sidebar.html" data-below-sidebar="core.engine/LayerConfiguration-class-sidebar.html">

<div>

# <span class="kind-class">LayerConfiguration</span> class

</div>

<div class="section desc markdown">

A class to configure which layers should be enabled or disabled in the OCM map data.

Disabling a layer allows to reduce the amount of data that will be downloaded or prefetched from the internet, for example, when panning the map view online or when downloading maps for offline use.

`LayerConfiguration` changes made via <a href="sdk-for-flutter-navigate-core-engine-sdkoptions-class">SDKOptions</a> require `sdk.maploader.MapUpdater` to align previously downloaded content. To ensure that the changes in <a href="sdk-for-flutter-navigate-core-engine-sdkoptions-class">SDKOptions</a> affect the map data, it is recommended to trigger a map update. Without calling

    mapUpdater.updateCatalog(...)

, the adjustments will apply only to future map downloads and will not impact the currently installed map data, either in the cache or in the persisted storage. Note that calling

    updateCatalog(...)

will update the version, only when a map update is available in the catalog.
</p>

**Notes**

- The `LayerConfiguration` is only available for the Navigate licenses that contains the offline maps feature. It has no effect on other license.

- The `LayerConfiguration` cannot be set separately for a region, it will be applied globally for all regions that will be downloaded in the future.

- It is not possible to specify a separate `LayerConfiguration` for the map cache and offline maps. The `LayerConfiguration` will be always applied to both.

- If a `LayerConfiguration` is applied, then only the listed features will be enabled, all others will be disabled. For example, if you want to disable only one feature, then all other features need to be present, or they will be also disabled.

The `LayerConfiguration` controls which content will be subject of

- map download for features in

      enabledFeatures()

  ,

- explicit prefetching using `sdk.prefetcher.RoutePrefetcher`, `sdk.prefetcher.PolygonPrefetcher` and implicit prefetching, such as when displaying a map view, for features in

      implicitlyPrefetchedFeatures()

  .

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-layerconfiguration-layerconfiguration">LayerConfiguration</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-enabledFeatures" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></span>\></span></span> <span class="parameter-name">enabledFeatures</span></span>)</span>  
Initializes both, `enabled_features` and `implicitly_prefetched_features` with value passed to constructor.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-layerconfiguration-layerconfiguration-withdefaults">LayerConfiguration.withDefaults</a></span><span class="signature">()</span>  
Initializes `enabled_features`, `implicitly_prefetched_features` and `on_demand_implicitly_prefetched_features` with it's default values.

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-layerconfiguration-layerconfiguration-withdownloadandprefetchfeatures">LayerConfiguration.withDownloadAndPrefetchFeatures</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withDownloadAndPrefetchFeatures-param-enabledFeatures" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></span>\></span></span> <span class="parameter-name">enabledFeatures</span>, </span><span id="sdk-for-flutter-navigate-withDownloadAndPrefetchFeatures-param-implicitlyPrefetchedFeatures" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></span>\></span></span> <span class="parameter-name">implicitlyPrefetchedFeatures</span></span>)</span>  
Creates a new instance.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-layerconfiguration-enabledfeatures">enabledFeatures</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></span>\></span></span>  
Specifies feature configuration for enabling list of features enabled for map download. Empty list disables map download, as no map content specified for download in this case.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-layerconfiguration-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-layerconfiguration-implicitlyprefetchedfeatures">implicitlyPrefetchedFeatures</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></span>\></span></span>  
Specifies the list of features enabled for implicit and explicit map prefetch. Implicit map prefetch will download map content for implicit prefetch features when showing a map in the MapView.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-layerconfiguration-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-layerconfiguration-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-layerconfiguration-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-layerconfiguration-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
