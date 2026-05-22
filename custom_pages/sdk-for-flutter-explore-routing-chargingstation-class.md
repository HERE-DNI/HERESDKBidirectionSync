---
title: "Untitled"
slug: "sdk-for-flutter-explore-routing-chargingstation-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ChargingStation-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-routing-routing-library</li>
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
/sdk-for-flutter-explore-routing-chargingstation-chargingstation(String? id, String? name, /sdk-for-flutter-explore-routing-chargingconnectorattributes-class? connectorAttributes)
</dt>
<dd>
          Creates a new instance.
        </dd>
<dt class="callable" id="ChargingStation.withDetails">
/sdk-for-flutter-explore-routing-chargingstation-chargingstation-withdetails(String? id, String? name, /sdk-for-flutter-explore-routing-chargingconnectorattributes-class? connectorAttributes, /sdk-for-flutter-explore-core-nameid-class? brand, /sdk-for-flutter-explore-core-nameid-class? chargePointOperator, List&lt;<wbr/>/sdk-for-flutter-explore-core-nameid-class&gt; matchingEMobilityServiceProviders)
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
/sdk-for-flutter-explore-routing-chargingstation-brand
↔ /sdk-for-flutter-explore-core-nameid-class?
</dt>
<dd>
  Charging station brand.
/sdk-for-flutter-explore-core-nameid-name reflect to charging station brand name.
/sdk-for-flutter-explore-core-nameid-id reflect to charging station brand unique ID.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="chargePointOperator">
/sdk-for-flutter-explore-routing-chargingstation-chargepointoperator
↔ /sdk-for-flutter-explore-core-nameid-class?
</dt>
<dd>
  Charging station charge-point-operator.
/sdk-for-flutter-explore-core-nameid-name reflect to charge-point-operator name.
/sdk-for-flutter-explore-core-nameid-id reflect to charge-point-operator ID.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="connectorAttributes">
/sdk-for-flutter-explore-routing-chargingstation-connectorattributes
↔ /sdk-for-flutter-explore-routing-chargingconnectorattributes-class?
</dt>
<dd>
  Details of the connector suggested to be used.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-explore-routing-chargingstation-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="id">
/sdk-for-flutter-explore-routing-chargingstation-id
↔ String?
</dt>
<dd>
  Identifier of this charging station. It can only be null when custom charging
stations from non-HERE datasets have been injected on the HERE platform.
By default, with HERE datasets it is guranteed to be not null.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="matchingEMobilityServiceProviders">
/sdk-for-flutter-explore-routing-chargingstation-matchingemobilityserviceproviders
↔ List&lt;<wbr/>/sdk-for-flutter-explore-core-nameid-class&gt;
</dt>
<dd>
  List of matched E-Mobility Service Providers.
Populated only when /sdk-for-flutter-explore-routing-electricvehicleoptions-evmobilityserviceproviderpreferences was set.
This list reflects the subset of E-Mobility Service Providers supported by the charging station,
from the list specified in the request parameter /sdk-for-flutter-explore-routing-electricvehicleoptions-evmobilityserviceproviderpreferences.
/sdk-for-flutter-explore-core-nameid-name in each list item reflect to E-Mobility Service Provider name.
/sdk-for-flutter-explore-core-nameid-id in each list item reflect to E-Mobility Service Provider id.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="name">
/sdk-for-flutter-explore-routing-chargingstation-name
↔ String?
</dt>
<dd>
  Human readable name of this charging station. It can be null when there is no
name associated with the station.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-routing-chargingstation-runtimetype
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
/sdk-for-flutter-explore-routing-chargingstation-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-routing-chargingstation-tostring(<wbr/>)
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
/sdk-for-flutter-explore-routing-chargingstation-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-routing-routing-library</li>
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



</div>
`
}</HTMLBlock>
