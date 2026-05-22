---
title: "Untitled"
slug: "sdk-for-flutter-navigate-routing-routinginterface-calculatetruckroute"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- calculateTruckRoute.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li>/sdk-for-flutter-navigate-routing-routinginterface-class</li>
<li class="self-crumb">calculateTruckRoute abstract method</li>
</ol>
<div class="self-name">calculateTruckRoute</div>
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
<h1>calculateTruckRoute abstract method</h1></div>
<section class="multi-line-signature">
<div>
<ol class="annotation-list">
<li>@Deprecated("Will be removed in v4.28.0. Use the <code>calculate_route()</code> methods with RoutingOptions parameter instead.")</li>
</ol>
</div>
/sdk-for-flutter-navigate-core-threading-taskhandle-class
calculateTruckRoute(<wbr/><ol class="parameter-list single-line"> <li>List&lt;<wbr/>/sdk-for-flutter-navigate-routing-waypoint-class&gt; waypoints, </li>
<li>/sdk-for-flutter-navigate-routing-truckoptions-class truckOptions, </li>
<li>/sdk-for-flutter-navigate-routing-calculateroutecallback callback</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Asynchronously calculates a truck route from one point to another,
passing through the given waypoints in the given order.</p>
<ul>
<li><code>waypoints</code> The list of waypoints used to calculate the route.
The first element marks the starting position, the last marks the destination.
Waypoints in between are interpreted as intermediate.</li>
</ul>
<p>An /sdk-for-flutter-navigate-routing-routingerror error is generated when the waypoint list
contains less than two elements or when the first and the last waypoints are not of type
/sdk-for-flutter-navigate-routing-waypointtype.</p>
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
<p>Returns /sdk-for-flutter-navigate-core-threading-taskhandle-class. Handle that will be used to manipulate the execution of the task.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">@Deprecated("Will be removed in v4.28.0. Use the `calculate_route()` methods with RoutingOptions parameter instead.")

TaskHandle calculateTruckRoute(List&lt;Waypoint&gt; waypoints, TruckOptions truckOptions, CalculateRouteCallback callback);</code></pre>
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
<li>/sdk-for-flutter-navigate-routing-routinginterface-class</li>
<li class="self-crumb">calculateTruckRoute abstract method</li>
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



</div>
`
}</HTMLBlock>
