---
title: "Untitled"
slug: "sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-startwithwaypointsandroutingoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- startWithWaypointsAndRoutingOptions.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-trafficawarenavigation-trafficawarenavigation-library</li>
<li>/sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-class</li>
<li class="self-crumb">startWithWaypointsAndRoutingOptions abstract method</li>
</ol>
<div class="self-name">startWithWaypointsAndRoutingOptions</div>
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
<div class="main-content" data-above-sidebar="trafficawarenavigation/DynamicRoutingEngine-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>startWithWaypointsAndRoutingOptions abstract method</h1></div>
<section class="multi-line-signature">
void
startWithWaypointsAndRoutingOptions(<wbr/><ol class="parameter-list"> <li>/sdk-for-flutter-navigate-routing-routehandle-class routeHandle, </li>
<li>List&lt;<wbr/>/sdk-for-flutter-navigate-routing-waypoint-class&gt; waypoints, </li>
<li>/sdk-for-flutter-navigate-routing-routingoptions-class routingOptions, </li>
<li>/sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutinglistener-class listener, </li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Starts polling the HERE backend services to find a better route,
as defined by the /sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengineoptions-class.</p>
<p><strong>Note:</strong> The engine will be internally stopped, if it was started before.
Therefore, it is not necessary to stop the engine before starting it again.</p>
<ul>
<li>
<p><code>routeHandle</code> The route handle from the HERE routing backend.</p>
</li>
<li>
<p><code>waypoints</code> Allows to specify detailed information on the waypoints of the route.
This parameter can be useful, when additional information needs to be
specified besides the coordinates - as the coordinates can be retrieved
from the contained /sdk-for-flutter-navigate-routing-routeplace-class that are already contained in
the /sdk-for-flutter-navigate-routing-routehandle-class parameter.</p>
</li>
<li>
<p><code>routingOptions</code> The options for the route calculation.</p>
</li>
<li>
<p><code>listener</code> The listener to receive the events.</p>
</li>
</ul>
<p>Throws /sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingenginestartexception-class. when the passed parameter are invalid.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void startWithWaypointsAndRoutingOptions(RouteHandle routeHandle, List&lt;Waypoint&gt; waypoints, RoutingOptions routingOptions, DynamicRoutingListener listener);</code></pre>
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
<li>/sdk-for-flutter-navigate-trafficawarenavigation-trafficawarenavigation-library</li>
<li>/sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-class</li>
<li class="self-crumb">startWithWaypointsAndRoutingOptions abstract method</li>
</ol>
<h5>DynamicRoutingEngine class</h5>
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
