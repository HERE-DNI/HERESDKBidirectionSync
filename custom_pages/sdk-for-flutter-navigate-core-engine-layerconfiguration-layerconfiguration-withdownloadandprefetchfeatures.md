---
title: "LayerConfiguration.withDownloadAndPrefetchFeatures constructor"
slug: "sdk-for-flutter-navigate-core-engine-layerconfiguration-layerconfiguration-withdownloadandprefetchfeatures"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LayerConfiguration.withDownloadAndPrefetchFeatures.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-core-engine-core-engine-library</li>
<li>/sdk-for-flutter-navigate-core-engine-layerconfiguration-class</li>
<li class="self-crumb">LayerConfiguration.withDownloadAndPrefetchFeatures constructor</li>
</ol>
<div class="self-name">LayerConfiguration.withDownloadAndPrefetchFeatures</div>
<form class="search navbar-right" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-box" placeholder="Loading search..." type="text"/>
</form>
<div class="toggle" id="theme-button" title="Toggle brightness">
<label for="theme">
<input id="theme" type="checkbox" value="light-theme"/>

        dark_mode
      

        light_mode
      
</label>
</div>
</header>
<main>
<div class="main-content" data-above-sidebar="core.engine/LayerConfiguration-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>LayerConfiguration.withDownloadAndPrefetchFeatures constructor</h1></div>
<section class="multi-line-signature">
LayerConfiguration.withDownloadAndPrefetchFeatures(<wbr/><ol class="parameter-list single-line"> <li>List&lt;<wbr/>/sdk-for-flutter-navigate-core-engine-layerconfigurationfeature&gt; enabledFeatures, </li>
<li>List&lt;<wbr/>/sdk-for-flutter-navigate-core-engine-layerconfigurationfeature&gt; implicitlyPrefetchedFeatures</li>
</ol>)
    </section>
<section class="desc markdown">
<p>Creates a new instance.</p>
<ul>
<li><code>enabledFeatures</code> Specifies feature configuration for enabling list of features enabled for map download.
Empty list disables map download, as no map content specified for download in this case.</li>
<li><code>implicitlyPrefetchedFeatures</code> Specifies the list of features enabled for implicit and explicit map prefetch.
Implicit map prefetch will download map content for implicit prefetch features when showing a map in the MapView.</li>
</ul>
<p>Allows to specify an empty list, effectively disabling implicit prefetching. In this case,
the system will prioritize minimal network usage, at the cost of reduced offline map availability.
When disabling certain implicitly prefetched features, less data will be prefetched when the map is rendered. Map
data that was already cached will not be removed until the least recently used strategy (LRU)
applies. That means you cannot remove any content from the map cache by updating the
<code>LayerConfiguration</code>. However, for new map data, it will be applied.</p>
<p>By default the list contains:</p>
<ul>
<li>/sdk-for-flutter-navigate-core-engine-layerconfigurationfeature</li>
</ul>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">LayerConfiguration.withDownloadAndPrefetchFeatures(this.enabledFeatures, this.implicitlyPrefetchedFeatures)
    : _onDemandImplicitlyPrefetchedFeatures = [LayerConfigurationFeature.detailRendering, LayerConfigurationFeature.navigation, LayerConfigurationFeature.offlineSearch, LayerConfigurationFeature.offlineRouting, LayerConfigurationFeature.rendering, LayerConfigurationFeature.truck, LayerConfigurationFeature.landmarks3d, LayerConfigurationFeature.rdsTraffic, LayerConfigurationFeature.ev, LayerConfigurationFeature.truckServiceAttributes, LayerConfigurationFeature.fuelStationAttributes, LayerConfigurationFeature.offlineBusRouting, LayerConfigurationFeature.junctionView3x4, LayerConfigurationFeature.junctionView16x9, LayerConfigurationFeature.junctionSign3x4, LayerConfigurationFeature.junctionSign3x5, LayerConfigurationFeature.junctionSign4x3, LayerConfigurationFeature.junctionSign5x3, LayerConfigurationFeature.junctionSign16x9, LayerConfigurationFeature.terrain, LayerConfigurationFeature.detailedTerrain, LayerConfigurationFeature.adas, LayerConfigurationFeature.ehorizon];</code></pre>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-core-engine-core-engine-library</li>
<li>/sdk-for-flutter-navigate-core-engine-layerconfiguration-class</li>
<li class="self-crumb">LayerConfiguration.withDownloadAndPrefetchFeatures constructor</li>
</ol>
<h5>LayerConfiguration class</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>
</div></div>
</div>
`
}</HTMLBlock>
