---
title: "Constructors"
slug: "sdk-for-flutter-explore-routing-electricvehicleoptions-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- ElectricVehicleOptions-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="routing/ElectricVehicleOptions-class.html#constructors">Constructors</a></li>
<li><a href="routing/ElectricVehicleOptions/ElectricVehicleOptions.html">ElectricVehicleOptions</a></li>
<li class="section-title">
<a href="routing/ElectricVehicleOptions-class.html#instance-properties">Properties</a>
</li>
<li><a href="routing/ElectricVehicleOptions/batterySpecifications.html">batterySpecifications</a></li>
<li><a href="routing/ElectricVehicleOptions/empiricalConsumptionModel.html">empiricalConsumptionModel</a></li>
<li><a href="routing/ElectricVehicleOptions/ensureReachability.html">ensureReachability</a></li>
<li><a href="routing/ElectricVehicleOptions/evMobilityServiceProviderPreferences.html">evMobilityServiceProviderPreferences</a></li>
<li><a href="routing/ElectricVehicleOptions/hashCode.html">hashCode</a></li>
<li><a href="routing/ElectricVehicleOptions/physicalConsumptionModel.html">physicalConsumptionModel</a></li>
<li class="inherited"><a href="routing/ElectricVehicleOptions/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="routing/ElectricVehicleOptions-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="routing/ElectricVehicleOptions/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="routing/ElectricVehicleOptions/toString.html">toString</a></li>
<li class="section-title"><a href="routing/ElectricVehicleOptions-class.html#operators">Operators</a></li>
<li><a href="routing/ElectricVehicleOptions/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li class="self-crumb">ElectricVehicleOptions class</li>
</ol>
<div class="self-name">ElectricVehicleOptions</div>
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
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/ElectricVehicleOptions-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>ElectricVehicleOptions class</h1></div>
<section class="desc markdown">
<p>These options define the parameters of the electric vehicle.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="ElectricVehicleOptions">
<a href="../routing/ElectricVehicleOptions/ElectricVehicleOptions.html">/sdk-for-flutter-explore-routing-electricvehicleoptions-electricvehicleoptions</a>()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="batterySpecifications">
<a href="../routing/ElectricVehicleOptions/batterySpecifications.html">/sdk-for-flutter-explore-routing-electricvehicleoptions-batteryspecifications</a>
↔ <a href="../routing/BatterySpecifications-class.html">/sdk-for-flutter-explore-routing-batteryspecifications-class</a>?
</dt>
<dd>
  Parameters that describe the electric vehicle's battery.
By default, it is set to <code>null</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="empiricalConsumptionModel">
<a href="../routing/ElectricVehicleOptions/empiricalConsumptionModel.html">/sdk-for-flutter-explore-routing-electricvehicleoptions-empiricalconsumptionmodel</a>
↔ <a href="../routing/EmpiricalConsumptionModel-class.html">/sdk-for-flutter-explore-routing-empiricalconsumptionmodel-class</a>?
</dt>
<dd>
  Defines the empirical consumption model.
The model is used to calculate the energy consumption for the vehicle on a given route.
<strong>Note</strong>
Only one consumption model is supported per route.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="ensureReachability">
<a href="../routing/ElectricVehicleOptions/ensureReachability.html">/sdk-for-flutter-explore-routing-electricvehicleoptions-ensurereachability</a>
↔ bool
</dt>
<dd>
  Ensure that the vehicle does not run out of energy along the way.
Requires valid <code>battery_specifications</code>.
It also requires that
<a href="../routing/RouteOptions/optimizationMode.html">/sdk-for-flutter-explore-routing-routeoptions-optimizationmode</a> = <a href="../routing/OptimizationMode.html">/sdk-for-flutter-explore-routing-optimizationmode</a>,
<a href="../routing/RouteOptions/speedCapInMetersPerSecond.html">/sdk-for-flutter-explore-routing-routeoptions-speedcapinmeterspersecond</a> is not set, and
<a href="../routing/AvoidanceOptions-class.html">/sdk-for-flutter-explore-routing-avoidanceoptions-class</a> is empty. Otherwise, this object is considered invalid.
Setting this flag enables calculation of a route optimized for electric vehicles.
Charging stations may be added along the route to ensure that the vehicle does
not run out of energy along the way.
It is especially useful for longer routes, because after all, charging stations are much
less common than petrol stations.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="evMobilityServiceProviderPreferences">
<a href="../routing/ElectricVehicleOptions/evMobilityServiceProviderPreferences.html">/sdk-for-flutter-explore-routing-electricvehicleoptions-evmobilityserviceproviderpreferences</a>
↔ <a href="../routing/EVMobilityServiceProviderPreferences-class.html">/sdk-for-flutter-explore-routing-evmobilityserviceproviderpreferences-class</a>
</dt>
<dd>
  Defines the preferred E-Mobility Service Providers.
The The E-Mobility Service Provider Partner Ids can be received from
<a href="https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-roamings.html">https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-roamings.html</a>
An alternative way to get <code>partnerId</code> is the <code>eMobilityServiceProviders.partnerId</code> as part of <code>HERE SDK Search</code>.
Maximum number of E-Mobility Service Providers is limited to 10.
By default, all providers are used.
<strong>Note</strong> Not yet supported for offline routing.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
<a href="../routing/ElectricVehicleOptions/hashCode.html">/sdk-for-flutter-explore-routing-electricvehicleoptions-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="physicalConsumptionModel">
<a href="../routing/ElectricVehicleOptions/physicalConsumptionModel.html">/sdk-for-flutter-explore-routing-electricvehicleoptions-physicalconsumptionmodel</a>
↔ <a href="../routing/PhysicalConsumptionModel-class.html">/sdk-for-flutter-explore-routing-physicalconsumptionmodel-class</a>?
</dt>
<dd>
  Defines the physical consumption model.
The model is used to calculate the energy consumption for the vehicle on a given route.
<strong>Note</strong>
Only one consumption model is supported per route.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../routing/ElectricVehicleOptions/runtimeType.html">/sdk-for-flutter-explore-routing-electricvehicleoptions-runtimetype</a>
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
<a href="../routing/ElectricVehicleOptions/noSuchMethod.html">/sdk-for-flutter-explore-routing-electricvehicleoptions-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../routing/ElectricVehicleOptions/toString.html">/sdk-for-flutter-explore-routing-electricvehicleoptions-tostring</a>(<wbr/>)
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
<a href="../routing/ElectricVehicleOptions/operator_equals.html">/sdk-for-flutter-explore-routing-electricvehicleoptions-operator-equals</a>(<wbr/>Object other)
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
<li class="self-crumb">ElectricVehicleOptions class</li>
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
