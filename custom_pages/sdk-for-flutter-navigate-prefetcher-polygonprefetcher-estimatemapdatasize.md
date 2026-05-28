---
title: "estimateMapDataSize abstract method"
slug: "sdk-for-flutter-navigate-prefetcher-polygonprefetcher-estimatemapdatasize"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- estimateMapDataSize.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-prefetcher-prefetcher-library</li>
<li>/sdk-for-flutter-navigate-prefetcher-polygonprefetcher-class</li>
<li class="self-crumb">estimateMapDataSize abstract method</li>
</ol>
<div class="self-name">estimateMapDataSize</div>
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
<div class="main-content" data-above-sidebar="prefetcher/PolygonPrefetcher-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>estimateMapDataSize abstract method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-core-threading-taskhandle-class
estimateMapDataSize(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-core-geopolygon-class geoPolygon, </li>
<li>/sdk-for-flutter-navigate-prefetcher-mapdatasizelistener-class callback</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Estimates map data size for the area bounded by geo polygon.</p>
<p>Size for tiles that are already
in the cache will not be included in the final result.</p>
<ul>
<li>
<p><code>geoPolygon</code> Area to estimate map data size for.</p>
</li>
<li>
<p><code>callback</code> Callback that is triggered to report the result of map data size estimation.</p>
</li>
</ul>
<p>Returns /sdk-for-flutter-navigate-core-threading-taskhandle-class. Handle that will be used to manipulate execution of the task.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle estimateMapDataSize(GeoPolygon geoPolygon, MapDataSizeListener callback);</code></pre>
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
<li>/sdk-for-flutter-navigate-prefetcher-prefetcher-library</li>
<li>/sdk-for-flutter-navigate-prefetcher-polygonprefetcher-class</li>
<li class="self-crumb">estimateMapDataSize abstract method</li>
</ol>
<h5>PolygonPrefetcher class</h5>
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
