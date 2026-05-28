---
title: "onBetterRouteFound abstract method"
slug: "sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutinglistener-onbetterroutefound"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- onBetterRouteFound.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-trafficawarenavigation-trafficawarenavigation-library</li>
<li>/sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutinglistener-class</li>
<li class="self-crumb">onBetterRouteFound abstract method</li>
</ol>
<div class="self-name">onBetterRouteFound</div>
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
<div class="main-content" data-above-sidebar="trafficawarenavigation/DynamicRoutingListener-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>onBetterRouteFound abstract method</h1></div>
<section class="multi-line-signature">
void
onBetterRouteFound(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-routing-route-class newRoute, </li>
<li>int etaDifferenceInSeconds, </li>
<li>int distanceDifferenceInMeters</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>This event is issued when a better route could be found,
as defined by /sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengineoptions-class.</p>
<p>To find a better route, two routes are calculated.
The updated current route: A route that is calculated via the route specified.
The dynamic route: A route that starts at the current position on the route specified
and passes through the remaining waypoints.</p>
<ul>
<li>
<p><code>newRoute</code> The newly calculated route with the remaining waypoints starting from the
current location.</p>
</li>
<li>
<p><code>etaDifferenceInSeconds</code> The difference in seconds:
eta of the current updated route - eta of the dynamic route.</p>
</li>
<li>
<p><code>distanceDifferenceInMeters</code> The difference in meters:
distance of the current updated route - distance of the dynamic route.
The value can be negative in case the current updated route has
a shorter distance, but its now assumed to be longer than the dynamic route.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void onBetterRouteFound(Route newRoute, int etaDifferenceInSeconds, int distanceDifferenceInMeters);</code></pre>
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
<li>/sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutinglistener-class</li>
<li class="self-crumb">onBetterRouteFound abstract method</li>
</ol>
<h5>DynamicRoutingListener class</h5>
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
