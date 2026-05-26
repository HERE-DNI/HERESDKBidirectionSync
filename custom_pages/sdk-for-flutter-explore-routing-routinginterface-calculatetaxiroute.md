---
title: "calculateTaxiRoute abstract method"
slug: "sdk-for-flutter-explore-routing-routinginterface-calculatetaxiroute"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- calculateTaxiRoute.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-routing-routing-library</li>
<li>/sdk-for-flutter-explore-routing-routinginterface-class</li>
<li class="self-crumb">calculateTaxiRoute abstract method</li>
</ol>
<div class="self-name">calculateTaxiRoute</div>
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
<div class="main-content" data-above-sidebar="routing/RoutingInterface-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>calculateTaxiRoute abstract method</h1></div>
<section class="multi-line-signature">
<div>
<ol class="annotation-list">
<li>@Deprecated("Will be removed in v4.28.0. Use the <code>calculate_route()</code> methods with RoutingOptions parameter instead.")</li>
</ol>
</div>
/sdk-for-flutter-explore-core-threading-taskhandle-class
calculateTaxiRoute(<wbr/><ol class="parameter-list single-line"> <li>List&lt;<wbr/>/sdk-for-flutter-explore-routing-waypoint-class&gt; waypoints, </li>
<li>/sdk-for-flutter-explore-routing-taxioptions-class taxiOptions, </li>
<li>/sdk-for-flutter-explore-routing-calculateroutecallback callback</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Asynchronously calculates a taxi route from one point to another,
passing through the given waypoints in the given order.</p>
<ul>
<li><code>waypoints</code> The list of waypoints used to calculate the route.
The first element marks the starting position, the last marks the destination.
Waypoints in between are interpreted as intermediate.</li>
</ul>
<p>An /sdk-for-flutter-explore-routing-routingerror error is generated when the waypoint list
contains less than two elements or when the first and the last waypoints are not of type
/sdk-for-flutter-explore-routing-waypointtype.</p>
<ul>
<li>
<p><code>taxiOptions</code> Options specific for taxi route calculation, along with
common route options. Note that /sdk-for-flutter-explore-routing-optimizationmode is
is not supported for taxis and converted to
/sdk-for-flutter-explore-routing-optimizationmode automatically.</p>
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
<pre class="language-dart"><code class="language-dart">@Deprecated("Will be removed in v4.28.0. Use the calculate_route() methods with RoutingOptions parameter instead.")

TaskHandle calculateTaxiRoute(List&lt;Waypoint&gt; waypoints, TaxiOptions taxiOptions, CalculateRouteCallback callback);</code></pre>
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
<li>/sdk-for-flutter-explore-routing-routinginterface-class</li>
<li class="self-crumb">calculateTaxiRoute abstract method</li>
</ol>
<h5>RoutingInterface class</h5>
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
