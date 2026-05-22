---
title: "Untitled"
slug: "sdk-for-flutter-navigate-prefetcher-routeprefetcher-prefetcharoundrouteonintervals"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- prefetchAroundRouteOnIntervals.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-prefetcher-prefetcher-library</li>
<li>/sdk-for-flutter-navigate-prefetcher-routeprefetcher-class</li>
<li class="self-crumb">prefetchAroundRouteOnIntervals abstract method</li>
</ol>
<div class="self-name">prefetchAroundRouteOnIntervals</div>
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
<h1>prefetchAroundRouteOnIntervals abstract method</h1></div>
<section class="multi-line-signature">
void
prefetchAroundRouteOnIntervals(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-navigatorinterface-class navigator</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Prefetches map data within a corridor along the route, that is currently set for the
provided /sdk-for-flutter-navigate-navigation-navigatorinterface-class instance.</p>
<p>If no route is set, no data will be prefetched.
The route corridor defaults to a length of 10 km and a width of 5 km.
To prefetch the whole route before navigation has been started see /sdk-for-flutter-navigate-prefetcher-routeprefetcher-prefetchgeocorridor.
Map data is prefetched only in discrete intervals. Prefetching starts 1 km before reaching the
end of the current corridor. Prefetching happens based on the current map-matched location - as
indicated by the /sdk-for-flutter-navigate-navigation-routeprogress-class event.
This method should be called right after navigation has started.
In case of default prefetch length first prefetching will start after traveling a distance
of 9 km along the route.</p>
<p>To control list of map content features for prefetch, use /sdk-for-flutter-navigate-core-engine-layerconfiguration-enabledfeatures.</p>
<ul>
<li><code>navigator</code> The /sdk-for-flutter-navigate-navigation-navigatorinterface-class to listen for Route Progress to prefetch data ahead.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void prefetchAroundRouteOnIntervals(NavigatorInterface navigator);</code></pre>
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
<li class="self-crumb">prefetchAroundRouteOnIntervals abstract method</li>
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
