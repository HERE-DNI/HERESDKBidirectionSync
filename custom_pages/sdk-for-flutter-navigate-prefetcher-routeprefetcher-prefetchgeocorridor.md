---
title: "prefetchGeoCorridor abstract method"
slug: "sdk-for-flutter-navigate-prefetcher-routeprefetcher-prefetchgeocorridor"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- prefetchGeoCorridor.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-prefetcher-prefetcher-library</li>
<li>/sdk-for-flutter-navigate-prefetcher-routeprefetcher-class</li>
<li class="self-crumb">prefetchGeoCorridor abstract method</li>
</ol>
<div class="self-name">prefetchGeoCorridor</div>
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
<div class="main-content" data-above-sidebar="prefetcher/RoutePrefetcher-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>prefetchGeoCorridor abstract method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-core-threading-taskhandle-class
prefetchGeoCorridor(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-core-geocorridor-class corridor, </li>
<li>/sdk-for-flutter-navigate-prefetcher-prefetchstatuslistener-class callback</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Prefetch tiles for a given geo-corridor.</p>
<p>A geo-corridor can easily be created from a route with /sdk-for-flutter-navigate-routing-route-geometry
so navigation on this route is possible in offline cases.
Please note, tiles will be saved in mutable cache so when there is not enough space to accommodate new
prefetched tiles /sdk-for-flutter-navigate-maploader-maploadererror is returned.
When updating mutable cache, all tiles will be unusable. Please re-download the geoCorridor again.
Please also note, any route calculation may not possible on prefetched tiles.</p>
<p>To control list of map content features for corridor prefetch, use /sdk-for-flutter-navigate-core-engine-layerconfiguration-enabledfeatures.</p>
<ul>
<li>
<p><code>corridor</code> indicates <code>GeoCorridor</code> that can be constructed from the route.</p>
</li>
<li>
<p><code>callback</code> is invoked to report progress and the result of prefetch. After operation is
finished, /sdk-for-flutter-navigate-prefetcher-prefetchstatuslistener-oncomplete is invoked on the main thread. Progress is reported by invocation
of /sdk-for-flutter-navigate-prefetcher-prefetchstatuslistener-onprogress on the main thread.</p>
</li>
</ul>
<p>Returns /sdk-for-flutter-navigate-core-threading-taskhandle-class. Handle that will be used to manipulate the execution of the task.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle prefetchGeoCorridor(GeoCorridor corridor, PrefetchStatusListener callback);</code></pre>
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
<li>/sdk-for-flutter-navigate-prefetcher-routeprefetcher-class</li>
<li class="self-crumb">prefetchGeoCorridor abstract method</li>
</ol>
<h5>RoutePrefetcher class</h5>
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
