---
title: "currentWeightChangeInKilograms property"
slug: "sdk-for-flutter-navigate-routing-waypoint-currentweightchangeinkilograms"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- currentWeightChangeInKilograms.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li>/sdk-for-flutter-navigate-routing-waypoint-class</li>
<li class="self-crumb">currentWeightChangeInKilograms property</li>
</ol>
<div class="self-name">currentWeightChangeInKilograms</div>
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
<div class="main-content" data-above-sidebar="routing/Waypoint-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>currentWeightChangeInKilograms property</h1></div>
<section class="multi-line-signature">
        
        int?
        currentWeightChangeInKilograms
<div class="features">getter/setter pair</div>
</section>
<section class="desc markdown">
<p>Changes the value of <code>vehicle[currentWeight]</code> by this value.
Enables the support of scenarios where the vehicle takes additional cargo or unloads its cargo along the route.
Changes to the configuration of the vehicle, such as adding a trailer, aren't supported.
Relative value in kilograms. Available range: from -40000 to 40000 (inclusive).
<strong>Note:</strong></p>
<ul>
<li>A route request with this parameter requires to set /sdk-for-flutter-navigate-transport-vehiclespecification-currentweightinkilograms and
/sdk-for-flutter-navigate-transport-vehiclespecification-grossweightinkilograms.</li>
<li>This feature is supported in transport modes of /sdk-for-flutter-navigate-transport-transportmode, /sdk-for-flutter-navigate-transport-transportmode, or
/sdk-for-flutter-navigate-transport-transportmode.</li>
</ul>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">int? currentWeightChangeInKilograms;</code></pre>
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
<li>/sdk-for-flutter-navigate-routing-waypoint-class</li>
<li class="self-crumb">currentWeightChangeInKilograms property</li>
</ol>
<h5>Waypoint class</h5>
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
