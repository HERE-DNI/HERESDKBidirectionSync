---
title: "Implementation"
slug: "sdk-for-flutter-explore-routing-routingengine-importroutefromhandle"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- importRouteFromHandle.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li><a href="../../routing/RoutingEngine-class.html">/sdk-for-flutter-explore-routing-routingengine-class</a></li>
<li class="self-crumb">importRouteFromHandle abstract method</li>
</ol>
<div class="self-name">importRouteFromHandle</div>
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
<div class="main-content" data-above-sidebar="routing/RoutingEngine-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>importRouteFromHandle abstract method</h1></div>
<section class="multi-line-signature">
<div>
<ol class="annotation-list">
<li>@Deprecated("Will be removed in v4.28.0. Use the `import_route()` methods with RoutingOptions parameter instead.")</li>
</ol>
</div>
<a href="../../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
importRouteFromHandle(<wbr/><ol class="parameter-list single-line"> <li><a href="../../routing/RouteHandle-class.html">/sdk-for-flutter-explore-routing-routehandle-class</a> routeHandle, </li>
<li><a class="deprecated" href="../../routing/RefreshRouteOptions-class.html">/sdk-for-flutter-explore-routing-refreshrouteoptions-class</a> refreshRouteOptions, </li>
<li><a href="../../routing/CalculateRouteCallback.html">/sdk-for-flutter-explore-routing-calculateroutecallback</a> callback</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Asynchronously recreates a route from the <a href="../../routing/RouteHandle-class.html">/sdk-for-flutter-explore-routing-routehandle-class</a> provided, i.e.</p>
<p>refreshes a previously
calculated route, with the specified <a class="deprecated" href="../../routing/RefreshRouteOptions-class.html">/sdk-for-flutter-explore-routing-refreshrouteoptions-class</a>.</p>
<p>A route handle can be invalid when the map data changes that is used by the HERE backend to recreate the route. This happens regularly.
Therefore, the route handle is not meant to be persisted for a longer time. Instead, a possible use case can be to plan a route with another HERE service.
For example, a HERE REST API that allows to calculate a route on a desktop. Then this route can be transferred via the handle to a mobile device for further use with the HERE SDK.</p>
<ul>
<li>
<p><code>routeHandle</code> The route handle holding the route to be refreshed.</p>
</li>
<li>
<p><code>refreshRouteOptions</code> The options define the vehicle and route options to calculate the route.
<strong>Note</strong> An <code>sdk.routing.RoutingError.INVALID_PARAMETER</code> is generated when the <code>sdk.routing.ElectricVehicleOptions.ensure_reachability</code> option is set to <code>true</code>.</p>
</li>
<li>
<p><code>callback</code> Callback object that will be invoked after refreshing the route.
It is always invoked on the main thread.</p>
</li>
</ul>
<p>Returns <a href="../../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>. Handle that will be used to manipulate the execution of the task.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">@Deprecated("Will be removed in v4.28.0. Use the `import_route()` methods with RoutingOptions parameter instead.")

TaskHandle importRouteFromHandle(RouteHandle routeHandle, RefreshRouteOptions refreshRouteOptions, CalculateRouteCallback callback);</code></pre>
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
<li><a href="../../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li><a href="../../routing/RoutingEngine-class.html">/sdk-for-flutter-explore-routing-routingengine-class</a></li>
<li class="self-crumb">importRouteFromHandle abstract method</li>
</ol>
<h5>RoutingEngine class</h5>
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
