---
title: "Implementation"
slug: "sdk-for-flutter-explore-routing-routingengine-importevcarroutewithstops"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- importEVCarRouteWithStops.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li><a href="../../routing/RoutingEngine-class.html">/sdk-for-flutter-explore-routing-routingengine-class</a></li>
<li class="self-crumb">importEVCarRouteWithStops abstract method</li>
</ol>
<div class="self-name">importEVCarRouteWithStops</div>
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
<h1>importEVCarRouteWithStops abstract method</h1></div>
<section class="multi-line-signature">
<div>
<ol class="annotation-list">
<li>@Deprecated("Will be removed in v4.28.0. Use the `import_route()` methods with RoutingOptions parameter instead.")</li>
</ol>
</div>
<a href="../../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
importEVCarRouteWithStops(<wbr/><ol class="parameter-list"> <li>List&lt;<wbr/><a href="../../core/Location-class.html">/sdk-for-flutter-explore-core-location-class</a>&gt; locations, </li>
<li>List&lt;<wbr/><a href="../../routing/RouteStop-class.html">/sdk-for-flutter-explore-routing-routestop-class</a>&gt; routeStops, </li>
<li><a class="deprecated" href="../../routing/EVCarOptions-class.html">/sdk-for-flutter-explore-routing-evcaroptions-class</a> evCarOptions, </li>
<li><a href="../../routing/CalculateRouteCallback.html">/sdk-for-flutter-explore-routing-calculateroutecallback</a> callback, </li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Asynchronously creates an electric car route from a sequence of geographic coordinates very close to each other.</p>
<p>The route shape will
be kept as close as possible to the one provided. For best results please use 1Hz GPS data,
or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can
be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.</p>
<p><strong>Note:</strong> Any restrictions applied to a transport type or provided options will be
discarded and reported as violations in <a href="../../routing/Section/sectionNotices.html">/sdk-for-flutter-explore-routing-section-sectionnotices</a> .</p>
<ul>
<li><code>locations</code> The list of locations used to calculate the route. Note that only the <a href="../../core/Location/coordinates.html">/sdk-for-flutter-explore-core-location-coordinates</a> of a location are used to import the route.</li>
</ul>
<p>An <a href="../../routing/RoutingError.html">/sdk-for-flutter-explore-routing-routingerror</a> error is generated when the location list
size is not in the range [2,50000].</p>
<ul>
<li><code>routeStops</code> The list of RouteStop's which contains index of location from locations list used for route stop and duration in seconds spent on stop.</li>
</ul>
<p>An <a href="../../routing/RoutingError.html">/sdk-for-flutter-explore-routing-routingerror</a> error is generated when the route stops list
size is not in the range [1,locations.size()-2], any of location_index is &lt; 1 or location_indexes are not unique.</p>
<ul>
<li>
<p><code>evCarOptions</code> Options specific for an electric car route calculation, along with
common route options.
<strong>Note</strong> An <code>sdk.routing.RoutingError.INVALID_PARAMETER</code> is generated when the <code>sdk.routing.EVCarOptions.ensure_reachability</code> option is set to <code>true</code>.</p>
</li>
<li>
<p><code>callback</code> Callback object that will be invoked after route calculation.
It is always invoked on the main thread.</p>
</li>
</ul>
<p>Returns <a href="../../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>. Handle that will be used to manipulate the execution of the task.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">@Deprecated("Will be removed in v4.28.0. Use the `import_route()` methods with RoutingOptions parameter instead.")

TaskHandle importEVCarRouteWithStops(List&lt;Location&gt; locations, List&lt;RouteStop&gt; routeStops, EVCarOptions evCarOptions, CalculateRouteCallback callback);</code></pre>
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
<li class="self-crumb">importEVCarRouteWithStops abstract method</li>
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
