---
title: "Untitled"
slug: "sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-updatecurrentlocation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- updateCurrentLocation.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-trafficawarenavigation-trafficawarenavigation-library</li>
<li>/sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-class</li>
<li class="self-crumb">updateCurrentLocation abstract method</li>
</ol>
<div class="self-name">updateCurrentLocation</div>
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
<h1>updateCurrentLocation abstract method</h1></div>
<section class="multi-line-signature">
void
updateCurrentLocation(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-navigation-mapmatchedlocation-class mapMatchedLocation, </li>
<li>int sectionIndex</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Updates the current location.</p>
<p>This location will be used as new starting point when the next
/sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengineoptions-pollinterval is reached and a new route is requested.
If an immediate route update is needed, consider to use the RoutingEngine instead.
All subsequently calculated routes used for the ETA calculation will start from this location.
The location needs to lie on the route or a <code>RoutingError</code> will be issued.</p>
<ul>
<li>
<p><code>mapMatchedLocation</code> The last known location.
It is recommended to use a /sdk-for-flutter-navigate-navigation-navigablelocation-mapmatchedlocation
as the driver is expected to be on a road.</p>
</li>
<li>
<p><code>sectionIndex</code> The current section from /sdk-for-flutter-navigate-navigation-routeprogress-sectionindex.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void updateCurrentLocation(MapMatchedLocation mapMatchedLocation, int sectionIndex);</code></pre>
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
<li class="self-crumb">updateCurrentLocation abstract method</li>
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
