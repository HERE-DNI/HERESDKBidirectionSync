---
title: "Constructors"
slug: "sdk-for-flutter-explore-routing-chargingstation-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- ChargingStation-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="routing/ChargingStation-class.html#constructors">Constructors</a></li>
<li><a href="routing/ChargingStation/ChargingStation.html">ChargingStation</a></li>
<li><a href="routing/ChargingStation/ChargingStation.withDetails.html">withDetails</a></li>
<li class="section-title">
<a href="routing/ChargingStation-class.html#instance-properties">Properties</a>
</li>
<li><a href="routing/ChargingStation/brand.html">brand</a></li>
<li><a href="routing/ChargingStation/chargePointOperator.html">chargePointOperator</a></li>
<li><a href="routing/ChargingStation/connectorAttributes.html">connectorAttributes</a></li>
<li><a href="routing/ChargingStation/hashCode.html">hashCode</a></li>
<li><a href="routing/ChargingStation/id.html">id</a></li>
<li><a href="routing/ChargingStation/matchingEMobilityServiceProviders.html">matchingEMobilityServiceProviders</a></li>
<li><a href="routing/ChargingStation/name.html">name</a></li>
<li class="inherited"><a href="routing/ChargingStation/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="routing/ChargingStation-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="routing/ChargingStation/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="routing/ChargingStation/toString.html">toString</a></li>
<li class="section-title"><a href="routing/ChargingStation-class.html#operators">Operators</a></li>
<li><a href="routing/ChargingStation/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li class="self-crumb">ChargingStation class</li>
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
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/ChargingStation-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>ChargingStation class</h1></div>
<section class="desc markdown">
<p>Data for an electric vehicle charging station.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="ChargingStation">
<a href="../routing/ChargingStation/ChargingStation.html">/sdk-for-flutter-explore-routing-chargingstation-chargingstation</a>(String? id, String? name, <a href="../routing/ChargingConnectorAttributes-class.html">/sdk-for-flutter-explore-routing-chargingconnectorattributes-class</a>? connectorAttributes)
</dt>
<dd>
          Creates a new instance.
        </dd>
<dt class="callable" id="ChargingStation.withDetails">
<a href="../routing/ChargingStation/ChargingStation.withDetails.html">/sdk-for-flutter-explore-routing-chargingstation-chargingstation-withdetails</a>(String? id, String? name, <a href="../routing/ChargingConnectorAttributes-class.html">/sdk-for-flutter-explore-routing-chargingconnectorattributes-class</a>? connectorAttributes, <a href="../core/NameID-class.html">/sdk-for-flutter-explore-core-nameid-class</a>? brand, <a href="../core/NameID-class.html">/sdk-for-flutter-explore-core-nameid-class</a>? chargePointOperator, List&lt;<wbr/><a href="../core/NameID-class.html">/sdk-for-flutter-explore-core-nameid-class</a>&gt; matchingEMobilityServiceProviders)
</dt>
<dd>
          Creates a new instance.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="brand">
<a href="../routing/ChargingStation/brand.html">/sdk-for-flutter-explore-routing-chargingstation-brand</a>
↔ <a href="../core/NameID-class.html">/sdk-for-flutter-explore-core-nameid-class</a>?
</dt>
<dd>
  Charging station brand.
<a href="../core/NameID/name.html">/sdk-for-flutter-explore-core-nameid-name</a> reflect to charging station brand name.
<a href="../core/NameID/id.html">/sdk-for-flutter-explore-core-nameid-id</a> reflect to charging station brand unique ID.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="chargePointOperator">
<a href="../routing/ChargingStation/chargePointOperator.html">/sdk-for-flutter-explore-routing-chargingstation-chargepointoperator</a>
↔ <a href="../core/NameID-class.html">/sdk-for-flutter-explore-core-nameid-class</a>?
</dt>
<dd>
  Charging station charge-point-operator.
<a href="../core/NameID/name.html">/sdk-for-flutter-explore-core-nameid-name</a> reflect to charge-point-operator name.
<a href="../core/NameID/id.html">/sdk-for-flutter-explore-core-nameid-id</a> reflect to charge-point-operator ID.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="connectorAttributes">
<a href="../routing/ChargingStation/connectorAttributes.html">/sdk-for-flutter-explore-routing-chargingstation-connectorattributes</a>
↔ <a href="../routing/ChargingConnectorAttributes-class.html">/sdk-for-flutter-explore-routing-chargingconnectorattributes-class</a>?
</dt>
<dd>
  Details of the connector suggested to be used.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
<a href="../routing/ChargingStation/hashCode.html">/sdk-for-flutter-explore-routing-chargingstation-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="id">
<a href="../routing/ChargingStation/id.html">/sdk-for-flutter-explore-routing-chargingstation-id</a>
↔ String?
</dt>
<dd>
  Identifier of this charging station. It can only be null when custom charging
stations from non-HERE datasets have been injected on the HERE platform.
By default, with HERE datasets it is guranteed to be not null.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="matchingEMobilityServiceProviders">
<a href="../routing/ChargingStation/matchingEMobilityServiceProviders.html">/sdk-for-flutter-explore-routing-chargingstation-matchingemobilityserviceproviders</a>
↔ List&lt;<wbr/><a href="../core/NameID-class.html">/sdk-for-flutter-explore-core-nameid-class</a>&gt;
</dt>
<dd>
  List of matched E-Mobility Service Providers.
Populated only when <a href="../routing/ElectricVehicleOptions/evMobilityServiceProviderPreferences.html">/sdk-for-flutter-explore-routing-electricvehicleoptions-evmobilityserviceproviderpreferences</a> was set.
This list reflects the subset of E-Mobility Service Providers supported by the charging station,
from the list specified in the request parameter <a href="../routing/ElectricVehicleOptions/evMobilityServiceProviderPreferences.html">/sdk-for-flutter-explore-routing-electricvehicleoptions-evmobilityserviceproviderpreferences</a>.
<a href="../core/NameID/name.html">/sdk-for-flutter-explore-core-nameid-name</a> in each list item reflect to E-Mobility Service Provider name.
<a href="../core/NameID/id.html">/sdk-for-flutter-explore-core-nameid-id</a> in each list item reflect to E-Mobility Service Provider id.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="name">
<a href="../routing/ChargingStation/name.html">/sdk-for-flutter-explore-routing-chargingstation-name</a>
↔ String?
</dt>
<dd>
  Human readable name of this charging station. It can be null when there is no
name associated with the station.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../routing/ChargingStation/runtimeType.html">/sdk-for-flutter-explore-routing-chargingstation-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
<a href="../routing/ChargingStation/noSuchMethod.html">/sdk-for-flutter-explore-routing-chargingstation-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../routing/ChargingStation/toString.html">/sdk-for-flutter-explore-routing-chargingstation-tostring</a>(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable" id="operator ==">
<a href="../routing/ChargingStation/operator_equals.html">/sdk-for-flutter-explore-routing-chargingstation-operator-equals</a>(<wbr/>Object other)
    → bool

</dt>
<dd>
  The equality operator.
  

</dd>
</dl>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li class="self-crumb">ChargingStation class</li>
</ol>
<h5>routing library</h5>
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
