---
title: "layerConfiguration property"
slug: "sdk-for-flutter-explore-core-engine-sdkoptions-layerconfiguration"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- layerConfiguration.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-core-engine-core-engine-library</li>
<li>/sdk-for-flutter-explore-core-engine-sdkoptions-class</li>
<li class="self-crumb">layerConfiguration property</li>
</ol>
<div class="self-name">layerConfiguration</div>
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
<div class="main-content" data-above-sidebar="core.engine/SDKOptions-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>layerConfiguration property</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-explore-core-engine-layerconfiguration-class
layerConfiguration
<div class="features">getter/setter pair</div>
</section>
<section class="desc markdown">
<p>Defines a list of data features that can be enabled / disabled. Once set to /sdk-for-flutter-explore-core-engine-sdkoptions-class when
a new HERE SDK is constructed, it will affect the map cache and offline maps.
When disabling certain features, less data will be prefetched when the map is rendered. Map
data that was already cached will not be removed until the least recently used strategy (LRU)
applies. That means you cannot remove any content from the map cache by updating the
/sdk-for-flutter-explore-core-engine-layerconfiguration-class. However, for new map data, it will be applied.
For offline maps, this /sdk-for-flutter-explore-core-engine-layerconfiguration-class can reduce the download size of all regions.
Note that the /sdk-for-flutter-explore-core-engine-layerconfiguration-class is applied globally to all regions that will be downloaded
in the future. It will not affect already downloaded regions. Updating a region will also
not update the /sdk-for-flutter-explore-core-engine-layerconfiguration-class. Only the /sdk-for-flutter-explore-core-engine-layerconfiguration-class will be used that was set
globally when a region was downloaded for the first time. If you want to update the
/sdk-for-flutter-explore-core-engine-layerconfiguration-class for an already downloaded region, please delete the region and download it again.</p>
<p>Please also note</p>
<ul>
<li>The /sdk-for-flutter-explore-core-engine-layerconfiguration-class is only applicable for the HERE SDK (Navigate) that contains the offline maps
feature. It has no effect on other licenses.</li>
<li>The /sdk-for-flutter-explore-core-engine-layerconfiguration-class cannot be set separately for a region, it will be applied globally
for all regions that will be downloaded in the future.</li>
<li>It is not possible to specify a separate /sdk-for-flutter-explore-core-engine-layerconfiguration-class for the map cache and offline maps.
The /sdk-for-flutter-explore-core-engine-layerconfiguration-class will be always applied to both.</li>
<li>The /sdk-for-flutter-explore-core-engine-layerconfiguration-class does affect the map cache when a device has connectivity. Even
when a device has connectivity it will only download the specified layers.</li>
<li>This is a beta feature and thus there can be bugs and unexpected behavior.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">LayerConfiguration layerConfiguration;</code></pre>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-core-engine-core-engine-library</li>
<li>/sdk-for-flutter-explore-core-engine-sdkoptions-class</li>
<li class="self-crumb">layerConfiguration property</li>
</ol>
<h5>SDKOptions class</h5>
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
