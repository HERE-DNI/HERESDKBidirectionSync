---
title: "Implementation"
slug: "sdk-for-flutter-explore-routing-chargingstation-chargingstation-withdetails"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- ChargingStation.withDetails.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li><a href="../../routing/ChargingStation-class.html">/sdk-for-flutter-explore-routing-chargingstation-class</a></li>
<li class="self-crumb">ChargingStation.withDetails constructor</li>
</ol>
<div class="self-name">ChargingStation.withDetails</div>
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
<h1>ChargingStation.withDetails constructor</h1></div>
<section class="multi-line-signature">
ChargingStation.withDetails(<wbr/><ol class="parameter-list"> <li>String? id, </li>
<li>String? name, </li>
<li><a href="../../routing/ChargingConnectorAttributes-class.html">/sdk-for-flutter-explore-routing-chargingconnectorattributes-class</a>? connectorAttributes, </li>
<li><a href="../../core/NameID-class.html">/sdk-for-flutter-explore-core-nameid-class</a>? brand, </li>
<li><a href="../../core/NameID-class.html">/sdk-for-flutter-explore-core-nameid-class</a>? chargePointOperator, </li>
<li>List&lt;<wbr/><a href="../../core/NameID-class.html">/sdk-for-flutter-explore-core-nameid-class</a>&gt; matchingEMobilityServiceProviders, </li>
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
<li><code>brand</code> Charging station brand.
<a href="../../core/NameID/name.html">/sdk-for-flutter-explore-core-nameid-name</a> reflect to charging station brand name.
<a href="../../core/NameID/id.html">/sdk-for-flutter-explore-core-nameid-id</a> reflect to charging station brand unique ID.</li>
<li><code>chargePointOperator</code> Charging station charge-point-operator.
<a href="../../core/NameID/name.html">/sdk-for-flutter-explore-core-nameid-name</a> reflect to charge-point-operator name.
<a href="../../core/NameID/id.html">/sdk-for-flutter-explore-core-nameid-id</a> reflect to charge-point-operator ID.</li>
<li><code>matchingEMobilityServiceProviders</code> List of matched E-Mobility Service Providers.
Populated only when <a href="../../routing/ElectricVehicleOptions/evMobilityServiceProviderPreferences.html">/sdk-for-flutter-explore-routing-electricvehicleoptions-evmobilityserviceproviderpreferences</a> was set.
This list reflects the subset of E-Mobility Service Providers supported by the charging station,
from the list specified in the request parameter <a href="../../routing/ElectricVehicleOptions/evMobilityServiceProviderPreferences.html">/sdk-for-flutter-explore-routing-electricvehicleoptions-evmobilityserviceproviderpreferences</a>.
<a href="../../core/NameID/name.html">/sdk-for-flutter-explore-core-nameid-name</a> in each list item reflect to E-Mobility Service Provider name.
<a href="../../core/NameID/id.html">/sdk-for-flutter-explore-core-nameid-id</a> in each list item reflect to E-Mobility Service Provider id.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">ChargingStation.withDetails(this.id, this.name, this.connectorAttributes, this.brand, this.chargePointOperator, this.matchingEMobilityServiceProviders);</code></pre>
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
<li><a href="../../routing/ChargingStation-class.html">/sdk-for-flutter-explore-routing-chargingstation-class</a></li>
<li class="self-crumb">ChargingStation.withDetails constructor</li>
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
</HTMLBlock>
