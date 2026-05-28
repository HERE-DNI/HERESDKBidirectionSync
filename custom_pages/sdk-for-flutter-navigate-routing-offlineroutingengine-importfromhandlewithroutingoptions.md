---
title: "importFromHandleWithRoutingOptions abstract method"
slug: "sdk-for-flutter-navigate-routing-offlineroutingengine-importfromhandlewithroutingoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- importFromHandleWithRoutingOptions.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li>/sdk-for-flutter-navigate-routing-offlineroutingengine-class</li>
<li class="self-crumb">importFromHandleWithRoutingOptions abstract method</li>
</ol>
<div class="self-name">importFromHandleWithRoutingOptions</div>
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
<div class="main-content" data-above-sidebar="routing/OfflineRoutingEngine-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>importFromHandleWithRoutingOptions abstract method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-core-threading-taskhandle-class
importFromHandleWithRoutingOptions(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-routing-routehandle-class routeHandle, </li>
<li>/sdk-for-flutter-navigate-routing-routingoptions-class options, </li>
<li>/sdk-for-flutter-navigate-routing-calculateroutecallback callback</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Asynchronously recreates a route from the /sdk-for-flutter-navigate-routing-routehandle-class provided, i.e.</p>
<p>refreshes a previously
calculated route, with the specified /sdk-for-flutter-navigate-routing-refreshrouteoptions-class.</p>
<p>A route handle can be invalid when the map data changes that is used by the HERE sdk to recreate the route. This happens regularly.
Therefore, the route handle is not meant to be persisted for a longer time.</p>
<ul>
<li>
<p><code>routeHandle</code> The route handle holding the route to be refreshed.</p>
</li>
<li>
<p><code>options</code> Options to import the route from handle.</p>
</li>
<li>
<p><code>callback</code> Callback object that will be invoked after refreshing the route.
It is always invoked on the main thread.</p>
</li>
</ul>
<p>Returns /sdk-for-flutter-navigate-core-threading-taskhandle-class. Handle that will be used to manipulate the execution of the task.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle importFromHandleWithRoutingOptions(RouteHandle routeHandle, RoutingOptions options, CalculateRouteCallback callback);</code></pre>
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
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li>/sdk-for-flutter-navigate-routing-offlineroutingengine-class</li>
<li class="self-crumb">importFromHandleWithRoutingOptions abstract method</li>
</ol>
<h5>OfflineRoutingEngine class</h5>
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
