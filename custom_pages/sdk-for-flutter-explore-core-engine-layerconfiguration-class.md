---
title: "Constructors"
slug: "sdk-for-flutter-explore-core-engine-layerconfiguration-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- LayerConfiguration-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="core.engine/LayerConfiguration-class.html#constructors">Constructors</a></li>
<li><a href="core.engine/LayerConfiguration/LayerConfiguration.html">LayerConfiguration</a></li>
<li><a href="core.engine/LayerConfiguration/LayerConfiguration.withDefaults.html">withDefaults</a></li>
<li><a href="core.engine/LayerConfiguration/LayerConfiguration.withDownloadAndPrefetchFeatures.html">withDownloadAndPrefetchFeatures</a></li>
<li class="section-title">
<a href="core.engine/LayerConfiguration-class.html#instance-properties">Properties</a>
</li>
<li><a href="core.engine/LayerConfiguration/enabledFeatures.html">enabledFeatures</a></li>
<li><a href="core.engine/LayerConfiguration/hashCode.html">hashCode</a></li>
<li><a href="core.engine/LayerConfiguration/implicitlyPrefetchedFeatures.html">implicitlyPrefetchedFeatures</a></li>
<li class="inherited"><a href="core.engine/LayerConfiguration/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="core.engine/LayerConfiguration-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="core.engine/LayerConfiguration/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="core.engine/LayerConfiguration/toString.html">toString</a></li>
<li class="section-title"><a href="core.engine/LayerConfiguration-class.html#operators">Operators</a></li>
<li><a href="core.engine/LayerConfiguration/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../core.engine/core.engine-library.html">/sdk-for-flutter-explore-core-engine-core-engine-library</a></li>
<li class="self-crumb">LayerConfiguration class</li>
</ol>
<div class="self-name">LayerConfiguration</div>
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
<div class="main-content" data-above-sidebar="core.engine/core.engine-library-sidebar.html" data-below-sidebar="core.engine/LayerConfiguration-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>LayerConfiguration class</h1></div>
<section class="desc markdown">
<p>A class to configure which layers should be enabled or disabled in the OCM map data.</p>
<p>Disabling a layer allows to reduce the amount of data that will be
downloaded or prefetched from the internet, for example, when panning the map view online or when downloading maps for offline use.</p>
<p><code>LayerConfiguration</code> changes made via <a href="../core.engine/SDKOptions-class.html">/sdk-for-flutter-explore-core-engine-sdkoptions-class</a> require <code>sdk.maploader.MapUpdater</code> to align previously downloaded content.
To ensure that the changes in <a href="../core.engine/SDKOptions-class.html">/sdk-for-flutter-explore-core-engine-sdkoptions-class</a> affect the map data,
it is recommended to trigger a map update. Without calling <code>mapUpdater.updateCatalog(...)</code>,
the adjustments will apply only to future map downloads and will not impact the currently installed map data, either in the cache or in the persisted storage.
Note that calling <code>updateCatalog(...)</code> will
update the version, only when a map update is available in the catalog.</p>
<p><strong>Notes</strong></p>
<ul>
<li>
<p>The <code>LayerConfiguration</code> is only available for the Navigate licenses that contains the offline maps
feature. It has no effect on other license.</p>
</li>
<li>
<p>The <code>LayerConfiguration</code> cannot be set separately for a region, it will be applied globally
for all regions that will be downloaded in the future.</p>
</li>
<li>
<p>It is not possible to specify a separate <code>LayerConfiguration</code> for the map cache and offline maps.
The <code>LayerConfiguration</code> will be always applied to both.</p>
</li>
<li>
<p>If a <code>LayerConfiguration</code> is applied, then only the listed features will be enabled,
all others will be disabled. For example, if you want to
disable only one feature, then all other features need to be present, or they will be also disabled.</p>
</li>
</ul>
<p>The <code>LayerConfiguration</code> controls which content will be subject of</p>
<ul>
<li>map download for features in <code>enabledFeatures()</code>,</li>
<li>explicit prefetching using <code>sdk.prefetcher.RoutePrefetcher</code>, <code>sdk.prefetcher.PolygonPrefetcher</code> and
implicit prefetching, such as when displaying a map view, for features in <code>implicitlyPrefetchedFeatures()</code>.</li>
</ul>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="LayerConfiguration">
<a href="../core.engine/LayerConfiguration/LayerConfiguration.html">/sdk-for-flutter-explore-core-engine-layerconfiguration-layerconfiguration</a>(List&lt;<wbr/><a href="../core.engine/LayerConfigurationFeature.html">/sdk-for-flutter-explore-core-engine-layerconfigurationfeature</a>&gt; enabledFeatures)
</dt>
<dd>
          Initializes both, <code>enabled_features</code> and <code>implicitly_prefetched_features</code> with value passed to constructor.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="LayerConfiguration.withDefaults">
<a href="../core.engine/LayerConfiguration/LayerConfiguration.withDefaults.html">/sdk-for-flutter-explore-core-engine-layerconfiguration-layerconfiguration-withdefaults</a>()
</dt>
<dd>
          Initializes <code>enabled_features</code>, <code>implicitly_prefetched_features</code> and <code>on_demand_implicitly_prefetched_features</code> with it's default values.
        </dd>
<dt class="callable" id="LayerConfiguration.withDownloadAndPrefetchFeatures">
<a href="../core.engine/LayerConfiguration/LayerConfiguration.withDownloadAndPrefetchFeatures.html">/sdk-for-flutter-explore-core-engine-layerconfiguration-layerconfiguration-withdownloadandprefetchfeatures</a>(List&lt;<wbr/><a href="../core.engine/LayerConfigurationFeature.html">/sdk-for-flutter-explore-core-engine-layerconfigurationfeature</a>&gt; enabledFeatures, List&lt;<wbr/><a href="../core.engine/LayerConfigurationFeature.html">/sdk-for-flutter-explore-core-engine-layerconfigurationfeature</a>&gt; implicitlyPrefetchedFeatures)
</dt>
<dd>
          Creates a new instance.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="enabledFeatures">
<a href="../core.engine/LayerConfiguration/enabledFeatures.html">/sdk-for-flutter-explore-core-engine-layerconfiguration-enabledfeatures</a>
↔ List&lt;<wbr/><a href="../core.engine/LayerConfigurationFeature.html">/sdk-for-flutter-explore-core-engine-layerconfigurationfeature</a>&gt;
</dt>
<dd>
  Specifies feature configuration for enabling list of features enabled for map download.
Empty list disables map download, as no map content specified for download in this case.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
<a href="../core.engine/LayerConfiguration/hashCode.html">/sdk-for-flutter-explore-core-engine-layerconfiguration-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="implicitlyPrefetchedFeatures">
<a href="../core.engine/LayerConfiguration/implicitlyPrefetchedFeatures.html">/sdk-for-flutter-explore-core-engine-layerconfiguration-implicitlyprefetchedfeatures</a>
↔ List&lt;<wbr/><a href="../core.engine/LayerConfigurationFeature.html">/sdk-for-flutter-explore-core-engine-layerconfigurationfeature</a>&gt;
</dt>
<dd>
  Specifies the list of features enabled for implicit and explicit map prefetch.
Implicit map prefetch will download map content for implicit prefetch features when showing a map in the MapView.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../core.engine/LayerConfiguration/runtimeType.html">/sdk-for-flutter-explore-core-engine-layerconfiguration-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
<a href="../core.engine/LayerConfiguration/noSuchMethod.html">/sdk-for-flutter-explore-core-engine-layerconfiguration-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../core.engine/LayerConfiguration/toString.html">/sdk-for-flutter-explore-core-engine-layerconfiguration-tostring</a>(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable" id="operator ==">
<a href="../core.engine/LayerConfiguration/operator_equals.html">/sdk-for-flutter-explore-core-engine-layerconfiguration-operator-equals</a>(<wbr/>Object other)
    → bool

</dt>
<dd>
  The equality operator.
  

</dd>
</dl>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../core.engine/core.engine-library.html">/sdk-for-flutter-explore-core-engine-core-engine-library</a></li>
<li class="self-crumb">LayerConfiguration class</li>
</ol>
<h5>core.engine library</h5>
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
</HTMLBlock>
