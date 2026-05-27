---
title: "Implementation"
slug: "sdk-for-flutter-explore-transport-vehiclespecification-currentweightinkilograms"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- currentWeightInKilograms.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../transport/transport-library.html">/sdk-for-flutter-explore-transport-transport-library</a></li>
<li><a href="../../transport/VehicleSpecification-class.html">/sdk-for-flutter-explore-transport-vehiclespecification-class</a></li>
<li class="self-crumb">currentWeightInKilograms property</li>
</ol>
<div class="self-name">currentWeightInKilograms</div>
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
<div class="main-content" data-above-sidebar="transport/VehicleSpecification-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>currentWeightInKilograms property</h1></div>
<section class="multi-line-signature">
        
        int?
        currentWeightInKilograms
<div class="features">getter/setter pair</div>
</section>
<section class="desc markdown">
<p>Current truck weight, including trailers and shipped goods currently loaded, specified in
kilograms. The provided value must be greater than or equal to 0. If unspecified,
it will default to <a href="../../transport/VehicleSpecification/grossWeightInKilograms.html">/sdk-for-flutter-explore-transport-vehiclespecification-grossweightinkilograms</a>.
By default, it is not set.</p>
<p><strong>Notes:</strong></p>
<ul>
<li>Supported in <a href="../../transport/TransportMode.html">/sdk-for-flutter-explore-transport-transportmode</a>, <a href="../../transport/TransportMode.html">/sdk-for-flutter-explore-transport-transportmode</a>, <a href="../../transport/TransportMode.html">/sdk-for-flutter-explore-transport-transportmode</a>,
<a href="../../transport/TransportMode.html">/sdk-for-flutter-explore-transport-transportmode</a> (Beta), <a href="../../transport/TransportMode.html">/sdk-for-flutter-explore-transport-transportmode</a> (Beta) transport modes.</li>
<li>Maximum weight for a car or taxi <em>without</em> a trailer is 5000 kg.</li>
<li>Maximum weight for a car or taxi <em>with</em> a trailer is 8500 kg.</li>
<li>A route request with <a href="../../transport/VehicleSpecification/currentWeightInKilograms.html">/sdk-for-flutter-explore-transport-vehiclespecification-currentweightinkilograms</a> above <a href="../../transport/VehicleSpecification/grossWeightInKilograms.html">/sdk-for-flutter-explore-transport-vehiclespecification-grossweightinkilograms</a> may result in
non-compliant or invalid routes.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">int? currentWeightInKilograms;</code></pre>
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
<li><a href="../../transport/transport-library.html">/sdk-for-flutter-explore-transport-transport-library</a></li>
<li><a href="../../transport/VehicleSpecification-class.html">/sdk-for-flutter-explore-transport-vehiclespecification-class</a></li>
<li class="self-crumb">currentWeightInKilograms property</li>
</ol>
<h5>VehicleSpecification class</h5>
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
