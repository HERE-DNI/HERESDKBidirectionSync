---
title: "Untitled"
slug: "sdk-for-flutter-navigate-transport-vehiclespecification-weightperaxleinkilograms"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- weightPerAxleInKilograms.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-transport-transport-library</li>
<li>/sdk-for-flutter-navigate-transport-vehiclespecification-class</li>
<li class="self-crumb">weightPerAxleInKilograms property</li>
</ol>
<div class="self-name">weightPerAxleInKilograms</div>
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
<h1>weightPerAxleInKilograms property</h1></div>
<section class="multi-line-signature">
        
        int?
        weightPerAxleInKilograms
<div class="features">getter/setter pair</div>
</section>
<section class="desc markdown">
<p>Heaviest weight per axle, regardless of axle type or axle group.
It is evaluated against all axle weight restrictions, including single axle and tandem axle weight restrictions.
The provided value must be greater or equal to 0.
By default, it is not set.</p>
<p><strong>Notes:</strong></p>
<ul>
<li>/sdk-for-flutter-navigate-transport-vehiclespecification-weightperaxleinkilograms and /sdk-for-flutter-navigate-transport-vehiclespecification-weightperaxlegroup are incompatible.
When available for your edition, if both attributes are set, during online <code>RoutingEngine</code> an <code>RoutingError.INVALID_PARAMETER</code>
error is generated. Otherwise, when offline <code>RoutingEngine</code> is in place, both parameters are evaluated and the
maximum value between them will be used.</li>
<li>Supported in /sdk-for-flutter-navigate-transport-transportmode, /sdk-for-flutter-navigate-transport-transportmode, /sdk-for-flutter-navigate-transport-transportmode,
/sdk-for-flutter-navigate-transport-transportmode (Beta), /sdk-for-flutter-navigate-transport-transportmode (Beta) transport modes.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">int? weightPerAxleInKilograms;</code></pre>
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
<li>/sdk-for-flutter-navigate-transport-transport-library</li>
<li>/sdk-for-flutter-navigate-transport-vehiclespecification-class</li>
<li class="self-crumb">weightPerAxleInKilograms property</li>
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



</div>
`
}</HTMLBlock>
