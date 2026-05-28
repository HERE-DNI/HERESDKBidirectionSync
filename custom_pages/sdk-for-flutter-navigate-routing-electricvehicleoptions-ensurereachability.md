---
title: "ensureReachability property"
slug: "sdk-for-flutter-navigate-routing-electricvehicleoptions-ensurereachability"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ensureReachability.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li>/sdk-for-flutter-navigate-routing-electricvehicleoptions-class</li>
<li class="self-crumb">ensureReachability property</li>
</ol>
<div class="self-name">ensureReachability</div>
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
<div class="main-content" data-above-sidebar="routing/ElectricVehicleOptions-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>ensureReachability property</h1></div>
<section class="multi-line-signature">
        
        bool
        ensureReachability
<div class="features">getter/setter pair</div>
</section>
<section class="desc markdown">
<p>Ensure that the vehicle does not run out of energy along the way.
Requires valid <code>battery_specifications</code>.
It also requires that
/sdk-for-flutter-navigate-routing-routeoptions-optimizationmode = /sdk-for-flutter-navigate-routing-optimizationmode,
/sdk-for-flutter-navigate-routing-routeoptions-speedcapinmeterspersecond is not set, and
/sdk-for-flutter-navigate-routing-avoidanceoptions-class is empty. Otherwise, this object is considered invalid.
Setting this flag enables calculation of a route optimized for electric vehicles.
Charging stations may be added along the route to ensure that the vehicle does
not run out of energy along the way.
It is especially useful for longer routes, because after all, charging stations are much
less common than petrol stations.</p>
<p><strong>Note</strong> An /sdk-for-flutter-navigate-routing-routingerror is generated when
this option is set to <code>true</code> in case <code>sdk.routing.RoutingEngine.import_route</code> is called.
Defaults to <code>false</code>.</p>
<p><strong>Note</strong>
Not supported for offline routing.</p>
<p><strong>Note</strong>
Only supported for car routing.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">bool ensureReachability;</code></pre>
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
<li>/sdk-for-flutter-navigate-routing-electricvehicleoptions-class</li>
<li class="self-crumb">ensureReachability property</li>
</ol>
<h5>ElectricVehicleOptions class</h5>
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
