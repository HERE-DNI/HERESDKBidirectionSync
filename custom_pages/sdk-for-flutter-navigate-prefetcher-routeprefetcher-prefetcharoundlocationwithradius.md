---
title: "Untitled"
slug: "sdk-for-flutter-navigate-prefetcher-routeprefetcher-prefetcharoundlocationwithradius"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- prefetchAroundLocationWithRadius.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-prefetcher-prefetcher-library</li>
<li>/sdk-for-flutter-navigate-prefetcher-routeprefetcher-class</li>
<li class="self-crumb">prefetchAroundLocationWithRadius abstract method</li>
</ol>
<div class="self-name">prefetchAroundLocationWithRadius</div>
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
<h1>prefetchAroundLocationWithRadius abstract method</h1></div>
<section class="multi-line-signature">
<div>
<ol class="annotation-list">
<li>@Deprecated("Will be removed in v4.27.0. Please use [PolygonPrefetcher.prefetch] instead.")</li>
</ol>
</div>
void
prefetchAroundLocationWithRadius(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-core-geocoordinates-class currentLocation, </li>
<li>double? radiusInMeters</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Prefetches map data within a user-defined circular area around a given location.</p>
<p>The radius, specified in meters, must be between 1 km and 50 km.
If <code>null</code> is passed as the radius, a default value of 2 km is used.
It is recommended to call this method once before starting navigation
to ensure a smooth experience.</p>
<p>To control list of map content features for area prefetch, use /sdk-for-flutter-navigate-core-engine-layerconfiguration-enabledfeatures.</p>
<ul>
<li>
<p><code>currentLocation</code> The center of the circle to prefetch data within.</p>
</li>
<li>
<p><code>radiusInMeters</code> The radius of the circle to prefetch data within.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">@Deprecated("Will be removed in v4.27.0. Please use [PolygonPrefetcher.prefetch] instead.")

void prefetchAroundLocationWithRadius(GeoCoordinates currentLocation, double? radiusInMeters);</code></pre>
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
<li class="self-crumb">prefetchAroundLocationWithRadius abstract method</li>
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



</div>
`
}</HTMLBlock>
