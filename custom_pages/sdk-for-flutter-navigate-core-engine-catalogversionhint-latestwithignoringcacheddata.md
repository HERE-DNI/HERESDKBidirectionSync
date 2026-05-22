---
title: "Untitled"
slug: "sdk-for-flutter-navigate-core-engine-catalogversionhint-latestwithignoringcacheddata"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- latestWithIgnoringCachedData.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-core-engine-core-engine-library</li>
<li>/sdk-for-flutter-navigate-core-engine-catalogversionhint-class</li>
<li class="self-crumb">latestWithIgnoringCachedData static method</li>
</ol>
<div class="self-name">latestWithIgnoringCachedData</div>
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
<div class="main-content" data-above-sidebar="core.engine/CatalogVersionHint-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>latestWithIgnoringCachedData static method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-core-engine-catalogversionhint-class
latestWithIgnoringCachedData(<wbr/><ol class="parameter-list single-line"> <li>bool ignoreCachedData</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>This static method can be called when you are interested in getting the most latest version of
a catalog when initializing the HERE SDK with <code>SDKOptions</code> where you can specify the
catalog(s) you want to use.</p>
<p>In effect, this will auto-update the cached map data on each
start, if possible. Use this only when you have no installed <code>Regions</code>. Since this affects
only the map data cache, calling this at initialization time has no or only a very limited
effect on the start-up time.</p>
<p>In order to auto-update cached OCM-based map data, such as for the HERE SDK (Navigate), use the
default HRN value: "hrn:here:data::olp-here:ocm" in your <code>DesiredCatalog</code>. Note that the
HERE SDK (Explore) cannot be used with such settings and the
initialization of the HERE SDK may fail - since it is based on a different map
format.</p>
<ul>
<li><code>ignoreCachedData</code> A flag to specify handling of any cached data present on a device when
trying to update the map version.
If set to true, the HERE SDK will auto-update to the latest catalog version when no installed
<code>Regions</code> are present. If present, this call will have no effect - use <code>updateCatalog()</code>
via <code>MapUpdater</code> instead to update all map data to the latest version.
Note that cached data present on a device - for example, data in the map cache or data cached
by <code>PrefetchAroundLocationWithRadius</code> or <code>PrefetchAroundRouteOnIntervals</code> - will be become obsolete if
a newer map version is available. Such data will be evicted using a LRU strategy over time.
If set to false, the HERE SDK will auto-update to use the latest version, only
when there is no cached map data at all (for example, at first install or after
clearing the cache) <em>and</em> no installed map data. Otherwise, this call will have no effect.</li>
</ul>
<p>Returns /sdk-for-flutter-navigate-core-engine-catalogversionhint-class. Instance of /sdk-for-flutter-navigate-core-engine-catalogversionhint-class.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static CatalogVersionHint latestWithIgnoringCachedData(bool ignoreCachedData) =&gt; $prototype.latestWithIgnoringCachedData(ignoreCachedData);</code></pre>
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
<li>/sdk-for-flutter-navigate-core-engine-catalogversionhint-class</li>
<li class="self-crumb">latestWithIgnoringCachedData static method</li>
</ol>
<h5>CatalogVersionHint class</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>



</div>
`
}</HTMLBlock>
