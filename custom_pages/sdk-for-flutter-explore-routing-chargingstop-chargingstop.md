---
title: "Implementation"
slug: "sdk-for-flutter-explore-routing-chargingstop-chargingstop"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- ChargingStop.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li><a href="../../routing/ChargingStop-class.html">/sdk-for-flutter-explore-routing-chargingstop-class</a></li>
<li class="self-crumb">ChargingStop constructor</li>
</ol>
<div class="self-name">ChargingStop</div>
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
<div class="main-content" data-above-sidebar="routing/ChargingStop-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>ChargingStop constructor</h1></div>
<section class="multi-line-signature">
ChargingStop(<wbr/><ol class="parameter-list"> <li>double powerInKilowatts, </li>
<li>double currentInAmperes, </li>
<li>double voltageInVolts, </li>
<li><a href="../../routing/ChargingSupplyType.html">/sdk-for-flutter-explore-routing-chargingsupplytype</a>? supplyType, </li>
<li>Duration? minDuration, </li>
<li>Duration? maxDuration, </li>
</ol>)
    </section>
<section class="desc markdown">
<p>Creates a new instance.</p>
<ul>
<li><code>powerInKilowatts</code> The value of rated power of the connector (in kW).</li>
<li><code>currentInAmperes</code> The value of rated current of the connector (in A).</li>
<li><code>voltageInVolts</code> The value of rated voltage of the connector (in V).</li>
<li><code>supplyType</code> Supply type of the suggested connector.</li>
<li><code>minDuration</code> The minimum duration the user expects to charge at the station,
including <a href="../../routing/BatterySpecifications/chargingSetupDuration.html">/sdk-for-flutter-explore-routing-batteryspecifications-chargingsetupduration</a>.
<strong>Note:</strong>
At least one of <code>min_duration</code> and <code>max_duration</code> is required for a user-planned charging stop.
For most use cases, providing at least <code>min_duration</code> is recommended.</li>
<li><code>maxDuration</code> The maximum duration the user plans to charge at the station,
including <a href="../../routing/BatterySpecifications/chargingSetupDuration.html">/sdk-for-flutter-explore-routing-batteryspecifications-chargingsetupduration</a>.
<strong>Note:</strong>
At least one of <code>min_duration</code> and <code>max_duration</code> is required for a user-planned charging stop.
For most use cases, providing at least <code>min_duration</code> is recommended.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">ChargingStop(this.powerInKilowatts, this.currentInAmperes, this.voltageInVolts, this.supplyType, this.minDuration, this.maxDuration);</code></pre>
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
<li><a href="../../routing/ChargingStop-class.html">/sdk-for-flutter-explore-routing-chargingstop-class</a></li>
<li class="self-crumb">ChargingStop constructor</li>
</ol>
<h5>ChargingStop class</h5>
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
