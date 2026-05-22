---
title: "Untitled"
slug: "sdk-for-flutter-explore-routing-routingengine-importtruckroute"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- importTruckRoute.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-routing-routing-library</li>
<li>/sdk-for-flutter-explore-routing-routingengine-class</li>
<li class="self-crumb">importTruckRoute abstract method</li>
</ol>
<div class="self-name">importTruckRoute</div>
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
<h1>importTruckRoute abstract method</h1></div>
<section class="multi-line-signature">
<div>
<ol class="annotation-list">
<li>@Deprecated("Will be removed in v4.28.0. Use the <code>import_route()</code> methods with RoutingOptions parameter instead.")</li>
</ol>
</div>
/sdk-for-flutter-explore-core-threading-taskhandle-class
importTruckRoute(<wbr/><ol class="parameter-list single-line"> <li>List&lt;<wbr/>/sdk-for-flutter-explore-core-location-class&gt; locations, </li>
<li>/sdk-for-flutter-explore-routing-truckoptions-class truckOptions, </li>
<li>/sdk-for-flutter-explore-routing-calculateroutecallback callback</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Asynchronously creates a truck route from a sequence of geographic coordinates very close to each other.</p>
<p>The route shape will
be kept as close as possible to the one provided. For best results please use 1Hz GPS data,
or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can
be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.</p>
<p><strong>Note:</strong> Any restrictions applied to a transport type or provided options will be
discarded and reported as violations in /sdk-for-flutter-explore-routing-section-sectionnotices .</p>
<ul>
<li><code>locations</code> The list of locations used to calculate the route. Note that only the /sdk-for-flutter-explore-core-location-coordinates of a location are used to import the route.</li>
</ul>
<p>An /sdk-for-flutter-explore-routing-routingerror error is generated when the location list
size is not in the range [2,50000].</p>
<ul>
<li>
<p><code>truckOptions</code> Options specific for truck route calculation, along with
common route options.</p>
</li>
<li>
<p><code>callback</code> Callback object that will be invoked after route calculation.
It is always invoked on the main thread.</p>
</li>
</ul>
<p>Returns /sdk-for-flutter-explore-core-threading-taskhandle-class. Handle that will be used to manipulate the execution of the task.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">@Deprecated("Will be removed in v4.28.0. Use the `import_route()` methods with RoutingOptions parameter instead.")

TaskHandle importTruckRoute(List&lt;Location&gt; locations, TruckOptions truckOptions, CalculateRouteCallback callback);</code></pre>
</section>
</div> 
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">

<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-routing-routing-library</li>
<li>/sdk-for-flutter-explore-routing-routingengine-class</li>
<li class="self-crumb">importTruckRoute abstract method</li>
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
