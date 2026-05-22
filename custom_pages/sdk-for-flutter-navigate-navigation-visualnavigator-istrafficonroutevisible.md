---
title: "Untitled"
slug: "sdk-for-flutter-navigate-navigation-visualnavigator-istrafficonroutevisible"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- isTrafficOnRouteVisible.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-visualnavigator-class</li>
<li class="self-crumb">isTrafficOnRouteVisible property</li>
</ol>
<div class="self-name">isTrafficOnRouteVisible</div>
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
<div class="main-content" data-above-sidebar="navigation/VisualNavigator-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>isTrafficOnRouteVisible property</h1></div>
<section id="getter">
<section class="multi-line-signature">
bool
isTrafficOnRouteVisible
</section>
<section class="desc markdown">
<p>A boolean which defines whether to perform rendering of traffic conditions on the route when <code>Route</code> visualization
is enabled during visual navigation.
When enabled the route's <code>MapPolyline</code> will be enhanced with visualization of the traffic conditions.
Colors used for this visualization are defined in /sdk-for-flutter-navigate-navigation-visualnavigatorcolors-trafficonroutecolors.
The presented traffic information is either set by the user via /sdk-for-flutter-navigate-navigation-navigatorinterface-trafficonroute or
is generated from historical traffic data stored in the map.
<strong>Note:</strong> <code>VisualNavigator</code> does not perform automatic traffic data updates. The updated traffic information is available
through the <code>sdk.routing.RoutingEngine.calculate_traffic_on_route</code> interface. The returned /sdk-for-flutter-navigate-routing-trafficonroute-class
could then be used to update <code>sdk.navigation.NavigatorInterface.traffic_on_route</code> to refresh the traffic on route visualization.
Defaults to <code>false</code>.
Gets the current state whether traffic conditions on route should be displayed during visual navigation.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">bool get isTrafficOnRouteVisible;</code></pre>
</section>
</section>
<section id="setter">
<section class="multi-line-signature">
void
isTrafficOnRouteVisible=(<wbr/>bool value)
</section>
<section class="desc markdown">
<p>A boolean which defines whether to perform rendering of traffic conditions on the route when <code>Route</code> visualization
is enabled during visual navigation.
When enabled the route's <code>MapPolyline</code> will be enhanced with visualization of the traffic conditions.
Colors used for this visualization are defined in /sdk-for-flutter-navigate-navigation-visualnavigatorcolors-trafficonroutecolors.
The presented traffic information is either set by the user via /sdk-for-flutter-navigate-navigation-navigatorinterface-trafficonroute or
is generated from historical traffic data stored in the map.
<strong>Note:</strong> <code>VisualNavigator</code> does not perform automatic traffic data updates. The updated traffic information is available
through the <code>sdk.routing.RoutingEngine.calculate_traffic_on_route</code> interface. The returned /sdk-for-flutter-navigate-routing-trafficonroute-class
could then be used to update <code>sdk.navigation.NavigatorInterface.traffic_on_route</code> to refresh the traffic on route visualization.
Defaults to <code>false</code>.
Sets whether to perform rendering of traffic conditions on the route when <code>Route</code> visualization is enabled
during visual navigation.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set isTrafficOnRouteVisible(bool value);</code></pre>
</section>
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
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-navigation-visualnavigator-class</li>
<li class="self-crumb">isTrafficOnRouteVisible property</li>
</ol>
<h5>VisualNavigator class</h5>
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
