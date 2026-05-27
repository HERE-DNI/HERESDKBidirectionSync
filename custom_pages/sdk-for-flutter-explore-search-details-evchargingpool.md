---
title: "Implementation"
slug: "sdk-for-flutter-explore-search-details-evchargingpool"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- evChargingPool.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
<li><a href="../../search/Details-class.html">/sdk-for-flutter-explore-search-details-class</a></li>
<li class="self-crumb">evChargingPool property</li>
</ol>
<div class="self-name">evChargingPool</div>
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
<div class="main-content" data-above-sidebar="search/Details-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>evChargingPool property</h1></div>
<section class="multi-line-signature">
<a href="../../search/EVChargingPool-class.html">/sdk-for-flutter-explore-search-evchargingpool-class</a>?
        evChargingPool
<div class="features">getter/setter pair</div>
</section>
<section class="desc markdown">
<p>EV charging pool details. It is available only for a place that is a charging pool
for electric vehicles.
It is fully supported for offline search, provided that <a href="../../core.engine/LayerConfigurationFeature.html">/sdk-for-flutter-explore-core-engine-layerconfigurationfeature</a>
is enabled in <a href="../../core.engine/SDKOptions/layerConfiguration.html">/sdk-for-flutter-explore-core-engine-sdkoptions-layerconfiguration</a>.</p>
<p>For online search, this feature is only available if it is explicitly enabled.
To do that, call <code>SearchEngine.set_custom_option()</code> with arguments:
name: "lookup.show" or "discover.show" or "browse.show"
value: "ev"
To enable this feature for all queries, call <code>SearchEngine.set_custom_option()</code> for all:
"lookup.show", "discover.show" and "browse.show".
To enable fuel station details or truck amenities, the custom option value can be combined
as "ev,truck", "ev,truck,fuel" etc.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">EVChargingPool? evChargingPool;</code></pre>
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
<li><a href="../../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
<li><a href="../../search/Details-class.html">/sdk-for-flutter-explore-search-details-class</a></li>
<li class="self-crumb">evChargingPool property</li>
</ol>
<h5>Details class</h5>
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
