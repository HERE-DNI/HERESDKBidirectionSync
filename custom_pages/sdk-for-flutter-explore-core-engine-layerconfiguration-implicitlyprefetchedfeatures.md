---
title: "Implementation"
slug: "sdk-for-flutter-explore-core-engine-layerconfiguration-implicitlyprefetchedfeatures"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- implicitlyPrefetchedFeatures.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../core.engine/core.engine-library.html">/sdk-for-flutter-explore-core-engine-core-engine-library</a></li>
<li><a href="../../core.engine/LayerConfiguration-class.html">/sdk-for-flutter-explore-core-engine-layerconfiguration-class</a></li>
<li class="self-crumb">implicitlyPrefetchedFeatures property</li>
</ol>
<div class="self-name">implicitlyPrefetchedFeatures</div>
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
<h1>implicitlyPrefetchedFeatures property</h1></div>
<section class="multi-line-signature">
        
        List&lt;<wbr/><a href="../../core.engine/LayerConfigurationFeature.html">/sdk-for-flutter-explore-core-engine-layerconfigurationfeature</a>&gt;
implicitlyPrefetchedFeatures
<div class="features">getter/setter pair</div>
</section>
<section class="desc markdown">
<p>Specifies the list of features enabled for implicit and explicit map prefetch.
Implicit map prefetch will download map content for implicit prefetch features when showing a map in the MapView.</p>
<p>Allows to specify an empty list, effectively disabling implicit prefetching. In this case,
the system will prioritize minimal network usage, at the cost of reduced offline map availability.
When disabling certain implicitly prefetched features, less data will be prefetched when the map is rendered. Map
data that was already cached will not be removed until the least recently used strategy (LRU)
applies. That means you cannot remove any content from the map cache by updating the
<code>LayerConfiguration</code>. However, for new map data, it will be applied.</p>
<p>By default the list contains:</p>
<ul>
<li><a href="../../core.engine/LayerConfigurationFeature.html">/sdk-for-flutter-explore-core-engine-layerconfigurationfeature</a></li>
</ul>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;LayerConfigurationFeature&gt; implicitlyPrefetchedFeatures;</code></pre>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../core.engine/core.engine-library.html">/sdk-for-flutter-explore-core-engine-core-engine-library</a></li>
<li><a href="../../core.engine/LayerConfiguration-class.html">/sdk-for-flutter-explore-core-engine-layerconfiguration-class</a></li>
<li class="self-crumb">implicitlyPrefetchedFeatures property</li>
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
</HTMLBlock>
