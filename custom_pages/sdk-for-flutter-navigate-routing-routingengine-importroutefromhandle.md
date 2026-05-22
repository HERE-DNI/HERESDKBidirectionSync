---
title: "Untitled"
slug: "sdk-for-flutter-navigate-routing-routingengine-importroutefromhandle"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- importRouteFromHandle.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li>/sdk-for-flutter-navigate-routing-routingengine-class</li>
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
<li>@Deprecated("Will be removed in v4.28.0. Use the <code>import_route()</code> methods with RoutingOptions parameter instead.")</li>
</ol>
</div>
/sdk-for-flutter-navigate-core-threading-taskhandle-class
importRouteFromHandle(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-routing-routehandle-class routeHandle, </li>
<li>/sdk-for-flutter-navigate-routing-refreshrouteoptions-class refreshRouteOptions, </li>
<li>/sdk-for-flutter-navigate-routing-calculateroutecallback callback</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Asynchronously recreates a route from the /sdk-for-flutter-navigate-routing-routehandle-class provided, i.e.</p>
<p>refreshes a previously
calculated route, with the specified /sdk-for-flutter-navigate-routing-refreshrouteoptions-class.</p>
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
<p>Returns /sdk-for-flutter-navigate-core-threading-taskhandle-class. Handle that will be used to manipulate the execution of the task.</p>
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
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li>/sdk-for-flutter-navigate-routing-routingengine-class</li>
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



</div>
`
}</HTMLBlock>
