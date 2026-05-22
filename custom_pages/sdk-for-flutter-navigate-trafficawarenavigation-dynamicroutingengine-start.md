---
title: "Untitled"
slug: "sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-start"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- start.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-trafficawarenavigation-trafficawarenavigation-library</li>
<li>/sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-class</li>
<li class="self-crumb">start abstract method</li>
</ol>
<div class="self-name">start</div>
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
<h1>start abstract method</h1></div>
<section class="multi-line-signature">
void
start(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-routing-route-class route, </li>
<li>/sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutinglistener-class listener</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Starts polling the HERE backend services to find a better route,
as defined by the DynamicRoutingEngineOptions.</p>
<p><strong>Note:</strong> The engine will be internally stopped, if it was started before.
Therefore, it is not necessary to stop the engine before starting it again.</p>
<ul>
<li>
<p><code>route</code> The route to be refreshed. The route must contain a /sdk-for-flutter-navigate-routing-routehandle-class,
therefore the route must have been requested with
/sdk-for-flutter-navigate-routing-routeoptions-enableroutehandle set to <code>true</code>.
The information to calculate new routes will be extracted from the provided route parameter.
If more information from the original waypoints is important besides their location,
consider to use one of the overloaded methods instead.</p>
</li>
<li>
<p><code>listener</code> The listener to receive the events.</p>
</li>
</ul>
<p>Throws /sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingenginestartexception-class. when the passed parameter are invalid.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void start(Route route, DynamicRoutingListener listener);</code></pre>
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
<li class="self-crumb">start abstract method</li>
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
