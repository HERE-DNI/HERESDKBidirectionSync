---
title: "Untitled"
slug: "sdk-for-flutter-navigate-prefetcher-polygonprefetcher-prefetch"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- prefetch.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-prefetcher-prefetcher-library</li>
<li>/sdk-for-flutter-navigate-prefetcher-polygonprefetcher-class</li>
<li class="self-crumb">prefetch abstract method</li>
</ol>
<div class="self-name">prefetch</div>
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
<h1>prefetch abstract method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-core-threading-taskhandle-class
prefetch(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-core-geopolygon-class geoPolygon, </li>
<li>/sdk-for-flutter-navigate-prefetcher-prefetchstatuslistener-class callback</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Prefetches map data for an area bounded by geo polygon.</p>
<p>After the operation is finished /sdk-for-flutter-navigate-prefetcher-prefetchstatuslistener-oncomplete is
invoked on the main thread. Progress is reported by invocation
of /sdk-for-flutter-navigate-prefetcher-prefetchstatuslistener-onprogress on the main thread.
If there is not enough space left in the cache to store needed tiles, operation will
fail with /sdk-for-flutter-navigate-maploader-maploadererror. To increase cache size, use
/sdk-for-flutter-navigate-core-engine-sdkoptions-cachesizeinbytes API.</p>
<p>To control list of map content features for area prefetch, use /sdk-for-flutter-navigate-core-engine-layerconfiguration-enabledfeatures.</p>
<p>To prefetch map data within user-defined circular area around a given location:</p>
<ol>
<li>Create a GeoCircle using the given location and radius.</li>
<li>Create a GeoPolygon using the GeoCircle.</li>
<li>Pass the afroementioned GeoPolygon to the sdk.prefetcher.PolygonPrefetcher.prefetch API.
Usage:
GeoCircle geoCircle = GeoCircle(location, radius);
GeoPolygon geoPolygon = GeoPolygon.withGeoCircle(geoCircle);</li>
</ol>
<ul>
<li>
<p><code>geoPolygon</code> Area to prefetch map data for.</p>
</li>
<li>
<p><code>callback</code> Callback that is triggered to report progress and the result of prefetch.</p>
</li>
</ul>
<p>Returns /sdk-for-flutter-navigate-core-threading-taskhandle-class. Handle that will be used to manipulate execution of the task.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle prefetch(GeoPolygon geoPolygon, PrefetchStatusListener callback);</code></pre>
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
<li class="self-crumb">prefetch abstract method</li>
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



</div>
`
}</HTMLBlock>
