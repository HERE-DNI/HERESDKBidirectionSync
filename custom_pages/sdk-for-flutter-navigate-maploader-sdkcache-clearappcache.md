---
title: "clearAppCache abstract method"
slug: "sdk-for-flutter-navigate-maploader-sdkcache-clearappcache"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- clearAppCache.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-maploader-maploader-library</li>
<li>/sdk-for-flutter-navigate-maploader-sdkcache-class</li>
<li class="self-crumb">clearAppCache abstract method</li>
</ol>
<div class="self-name">clearAppCache</div>
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
<div class="main-content" data-above-sidebar="maploader/SDKCache-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>clearAppCache abstract method</h1></div>
<section class="multi-line-signature">
void
clearAppCache(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-maploader-sdkcachecallback callback</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Clears all data that is currently stored in the SDK cache.</p>
<p>Path for cache is specified by /sdk-for-flutter-navigate-core-engine-sdkoptions-cachepath.
The operation can have unexpected behaviour when it is called during a map interaction, during turn-by-turn navigation (only available for the Navigate license) or
during ongoing requests initiated by the OfflineSearchEngine or the OfflineRouteEngine (only available for the Navigate license).</p>
<ul>
<li><code>callback</code> Callback which receives the result on the main thread.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void clearAppCache(SDKCacheCallback callback);</code></pre>
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
<li>/sdk-for-flutter-navigate-maploader-maploader-library</li>
<li>/sdk-for-flutter-navigate-maploader-sdkcache-class</li>
<li class="self-crumb">clearAppCache abstract method</li>
</ol>
<h5>SDKCache class</h5>
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
