---
title: "Implementation"
slug: "sdk-for-flutter-explore-routing-batteryspecifications-initialchargeinkilowatthours"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- initialChargeInKilowattHours.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li><a href="../../routing/BatterySpecifications-class.html">/sdk-for-flutter-explore-routing-batteryspecifications-class</a></li>
<li class="self-crumb">initialChargeInKilowattHours property</li>
</ol>
<div class="self-name">initialChargeInKilowattHours</div>
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
<div class="main-content" data-above-sidebar="routing/BatterySpecifications-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>initialChargeInKilowattHours property</h1></div>
<section class="multi-line-signature">
        
        double
        initialChargeInKilowattHours
<div class="features">getter/setter pair</div>
</section>
<section class="desc markdown">
<p>Charge level of the vehicle's battery at the start of the route (in kWh).
It must be non-negative and less than or equal to the value of
<a href="../../routing/BatterySpecifications/totalCapacityInKilowattHours.html">/sdk-for-flutter-explore-routing-batteryspecifications-totalcapacityinkilowatthours</a>,
otherwise the <a href="../../routing/BatterySpecifications-class.html">/sdk-for-flutter-explore-routing-batteryspecifications-class</a> instance is considered invalid.
Defaults to 0.
<strong>Note:</strong>
For a user-planned <a href="../../routing/ChargingStop-class.html">/sdk-for-flutter-explore-routing-chargingstop-class</a>, this parameter is also required.
If not set greater than 0, the route calculation will fail as an an invalid parameter error.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">double initialChargeInKilowattHours;</code></pre>
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
<li><a href="../../routing/BatterySpecifications-class.html">/sdk-for-flutter-explore-routing-batteryspecifications-class</a></li>
<li class="self-crumb">initialChargeInKilowattHours property</li>
</ol>
<h5>BatterySpecifications class</h5>
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
