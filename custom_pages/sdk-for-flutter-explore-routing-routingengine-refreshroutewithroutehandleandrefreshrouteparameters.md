---
title: "Implementation"
slug: "sdk-for-flutter-explore-routing-routingengine-refreshroutewithroutehandleandrefreshrouteparameters"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- refreshRouteWithRouteHandleAndRefreshRouteParameters.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li><a href="../../routing/RoutingEngine-class.html">/sdk-for-flutter-explore-routing-routingengine-class</a></li>
<li class="self-crumb">refreshRouteWithRouteHandleAndRefreshRouteParameters abstract method</li>
</ol>
<div class="self-name">refreshRouteWithRouteHandleAndRefreshRouteParameters</div>
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
<h1>refreshRouteWithRouteHandleAndRefreshRouteParameters abstract method</h1></div>
<section class="multi-line-signature">
<a href="../../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
refreshRouteWithRouteHandleAndRefreshRouteParameters(<wbr/><ol class="parameter-list single-line"> <li><a href="../../routing/RefreshRouteParameters-class.html">/sdk-for-flutter-explore-routing-refreshrouteparameters-class</a> refreshRouteParameters, </li>
<li><a href="../../routing/RoutingOptions-class.html">/sdk-for-flutter-explore-routing-routingoptions-class</a> routingOptions, </li>
<li><a href="../../routing/CalculateRouteCallback.html">/sdk-for-flutter-explore-routing-calculateroutecallback</a> callback</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Asynchronously refreshes a previously calculated route from the provided <a href="../../routing/RouteHandle-class.html">/sdk-for-flutter-explore-routing-routehandle-class</a>, updating
the starting point and route metadata based on <a href="../../routing/RoutingOptions-class.html">/sdk-for-flutter-explore-routing-routingoptions-class</a>.</p>
<p>The route shape from the new
starting point to the destination remains unchanged, and only metadata such as arrival time and traffic
delays are updated.</p>
<ul>
<li>
<p><code>refreshRouteParameters</code> The parameters used to refresh the route</p>
</li>
<li>
<p><code>routingOptions</code> The options define the vehicle and route options used to calculate the route.</p>
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
<pre class="language-dart"><code class="language-dart">TaskHandle refreshRouteWithRouteHandleAndRefreshRouteParameters(RefreshRouteParameters refreshRouteParameters, RoutingOptions routingOptions, CalculateRouteCallback callback);</code></pre>
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
<li class="self-crumb">refreshRouteWithRouteHandleAndRefreshRouteParameters abstract method</li>
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
