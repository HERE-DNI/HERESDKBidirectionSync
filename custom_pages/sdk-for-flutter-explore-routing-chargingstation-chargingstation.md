---
title: "ChargingStation constructor"
slug: "sdk-for-flutter-explore-routing-chargingstation-chargingstation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ChargingStation.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-routing-routing-library</li>
<li>/sdk-for-flutter-explore-routing-chargingstation-class</li>
<li class="self-crumb">ChargingStation constructor</li>
</ol>
<div class="self-name">ChargingStation</div>
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
<div class="main-content" data-above-sidebar="routing/ChargingStation-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>ChargingStation constructor</h1></div>
<section class="multi-line-signature">
ChargingStation(<wbr/><ol class="parameter-list single-line"> <li>String? id, </li>
<li>String? name, </li>
<li>/sdk-for-flutter-explore-routing-chargingconnectorattributes-class? connectorAttributes</li>
</ol>)
    </section>
<section class="desc markdown">
<p>Creates a new instance.</p>
<ul>
<li><code>id</code> Identifier of this charging station. It can only be null when custom charging
stations from non-HERE datasets have been injected on the HERE platform.
By default, with HERE datasets it is guranteed to be not null.</li>
<li><code>name</code> Human readable name of this charging station. It can be null when there is no
name associated with the station.</li>
<li><code>connectorAttributes</code> Details of the connector suggested to be used.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">ChargingStation(this.id, this.name, this.connectorAttributes)
    : brand = null, chargePointOperator = null, matchingEMobilityServiceProviders = [];</code></pre>
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
<li>/sdk-for-flutter-explore-routing-chargingstation-class</li>
<li class="self-crumb">ChargingStation constructor</li>
</ol>
<h5>ChargingStation class</h5>
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
