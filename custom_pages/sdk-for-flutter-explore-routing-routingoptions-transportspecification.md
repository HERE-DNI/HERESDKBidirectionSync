---
title: "Implementation"
slug: "sdk-for-flutter-explore-routing-routingoptions-transportspecification"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- transportSpecification.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li><a href="../../routing/RoutingOptions-class.html">/sdk-for-flutter-explore-routing-routingoptions-class</a></li>
<li class="self-crumb">transportSpecification property</li>
</ol>
<div class="self-name">transportSpecification</div>
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
<div class="main-content" data-above-sidebar="routing/RoutingOptions-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>transportSpecification property</h1></div>
<section class="multi-line-signature">
<a href="../../transport/TransportSpecification-class.html">/sdk-for-flutter-explore-transport-transportspecification-class</a>
transportSpecification
<div class="features">getter/setter pair</div>
</section>
<section class="desc markdown">
<p>Defines the transport specification which contains the transport mode and the vehicle specifications
for the transport mode chosen.
<strong>Notes:</strong></p>
<ul>
<li>The transport mode <a href="../../transport/TransportMode.html">/sdk-for-flutter-explore-transport-transportmode</a> is not supported.</li>
<li>By default all vehicle specifications from <a href="../../routing/RoutingOptions/transportSpecification.html">/sdk-for-flutter-explore-routing-routingoptions-transportspecification</a> are set to <code>null</code> and the
<a href="../../transport/TransportSpecification/transportMode.html">/sdk-for-flutter-explore-transport-transportspecification-transportmode</a> from <a href="../../routing/RoutingOptions/transportSpecification.html">/sdk-for-flutter-explore-routing-routingoptions-transportspecification</a> is set to <a href="../../transport/TransportMode.html">/sdk-for-flutter-explore-transport-transportmode</a>.</li>
<li>A route can be calculated with only the <a href="../../transport/TransportSpecification/transportMode.html">/sdk-for-flutter-explore-transport-transportspecification-transportmode</a> from <a href="../../routing/RoutingOptions/transportSpecification.html">/sdk-for-flutter-explore-routing-routingoptions-transportspecification</a> set.</li>
<li>It is highly recommended to define the <a href="../../transport/TruckCategory.html">/sdk-for-flutter-explore-transport-truckcategory</a> that is being used in <a href="../../transport/VehicleSpecification/truckCategory.html">/sdk-for-flutter-explore-transport-vehiclespecification-truckcategory</a> from
<a href="../../transport/TransportSpecification/vehicleSpecification.html">/sdk-for-flutter-explore-transport-transportspecification-vehiclespecification</a> from <a href="../../routing/RoutingOptions/transportSpecification.html">/sdk-for-flutter-explore-routing-routingoptions-transportspecification</a>, if the
<a href="../../transport/TransportSpecification/transportMode.html">/sdk-for-flutter-explore-transport-transportspecification-transportmode</a> from <a href="../../routing/RoutingOptions/transportSpecification.html">/sdk-for-flutter-explore-routing-routingoptions-transportspecification</a> is set to <a href="../../transport/TransportMode.html">/sdk-for-flutter-explore-transport-transportmode</a>.</li>
<li>The <a href="../../transport/VehicleSpecification/occupancy.html">/sdk-for-flutter-explore-transport-vehiclespecification-occupancy</a> from <a href="../../transport/TransportSpecification/vehicleSpecification.html">/sdk-for-flutter-explore-transport-transportspecification-vehiclespecification</a> won't have effect
if HOV and/or HOT lane usage is not allowed using <a href="../../routing/EVTruckOptions/allowOptions.html">/sdk-for-flutter-explore-routing-evtruckoptions-allowoptions</a>.</li>
<li>The <a href="../../transport/PedestrianSpecification/walkingSpeedInMetersPerSecond.html">/sdk-for-flutter-explore-transport-pedestrianspecification-walkingspeedinmeterspersecond</a> from <a href="../../transport/TransportSpecification/pedestrianSpecification.html">/sdk-for-flutter-explore-transport-transportspecification-pedestrianspecification</a>
if present, will be used by the service as the walking speed for pedestrian routing. It influences the duration of walking
along the route. The provided value must be in the range [0.5, 2.0]. When the value is outside this
range, an invalid parameter error is raised. Refer to <a href="../../routing/RoutingError.html">/sdk-for-flutter-explore-routing-routingerror</a> for details. The
default speed is 1 meter per second.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TransportSpecification transportSpecification;</code></pre>
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
<li><a href="../../routing/RoutingOptions-class.html">/sdk-for-flutter-explore-routing-routingoptions-class</a></li>
<li class="self-crumb">transportSpecification property</li>
</ol>
<h5>RoutingOptions class</h5>
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
