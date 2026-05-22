---
title: "Untitled"
slug: "sdk-for-flutter-explore-routing-routingoptions-transportspecification"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- transportSpecification.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-routing-routing-library</li>
<li>/sdk-for-flutter-explore-routing-routingoptions-class</li>
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
/sdk-for-flutter-explore-transport-transportspecification-class
transportSpecification
<div class="features">getter/setter pair</div>
</section>
<section class="desc markdown">
<p>Defines the transport specification which contains the transport mode and the vehicle specifications
for the transport mode chosen.
<strong>Notes:</strong></p>
<ul>
<li>The transport mode /sdk-for-flutter-explore-transport-transportmode is not supported.</li>
<li>By default all vehicle specifications from /sdk-for-flutter-explore-routing-routingoptions-transportspecification are set to <code>null</code> and the
/sdk-for-flutter-explore-transport-transportspecification-transportmode from /sdk-for-flutter-explore-routing-routingoptions-transportspecification is set to /sdk-for-flutter-explore-transport-transportmode.</li>
<li>A route can be calculated with only the /sdk-for-flutter-explore-transport-transportspecification-transportmode from /sdk-for-flutter-explore-routing-routingoptions-transportspecification set.</li>
<li>It is highly recommended to define the /sdk-for-flutter-explore-transport-truckcategory that is being used in /sdk-for-flutter-explore-transport-vehiclespecification-truckcategory from
/sdk-for-flutter-explore-transport-transportspecification-vehiclespecification from /sdk-for-flutter-explore-routing-routingoptions-transportspecification, if the
/sdk-for-flutter-explore-transport-transportspecification-transportmode from /sdk-for-flutter-explore-routing-routingoptions-transportspecification is set to /sdk-for-flutter-explore-transport-transportmode.</li>
<li>The /sdk-for-flutter-explore-transport-vehiclespecification-occupancy from /sdk-for-flutter-explore-transport-transportspecification-vehiclespecification won't have effect
if HOV and/or HOT lane usage is not allowed using /sdk-for-flutter-explore-routing-evtruckoptions-allowoptions.</li>
<li>The /sdk-for-flutter-explore-transport-pedestrianspecification-walkingspeedinmeterspersecond from /sdk-for-flutter-explore-transport-transportspecification-pedestrianspecification
if present, will be used by the service as the walking speed for pedestrian routing. It influences the duration of walking
along the route. The provided value must be in the range [0.5, 2.0]. When the value is outside this
range, an invalid parameter error is raised. Refer to /sdk-for-flutter-explore-routing-routingerror for details. The
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
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-routing-routing-library</li>
<li>/sdk-for-flutter-explore-routing-routingoptions-class</li>
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



</div>
`
}</HTMLBlock>
