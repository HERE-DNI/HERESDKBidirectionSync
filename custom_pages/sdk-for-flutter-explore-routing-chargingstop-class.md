---
title: "Constructors"
slug: "sdk-for-flutter-explore-routing-chargingstop-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- ChargingStop-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="routing/ChargingStop-class.html#constructors">Constructors</a></li>
<li><a href="routing/ChargingStop/ChargingStop.html">ChargingStop</a></li>
<li><a href="routing/ChargingStop/ChargingStop.withDefaults.html">withDefaults</a></li>
<li class="section-title">
<a href="routing/ChargingStop-class.html#instance-properties">Properties</a>
</li>
<li><a href="routing/ChargingStop/currentInAmperes.html">currentInAmperes</a></li>
<li><a href="routing/ChargingStop/hashCode.html">hashCode</a></li>
<li><a href="routing/ChargingStop/maxDuration.html">maxDuration</a></li>
<li><a href="routing/ChargingStop/minDuration.html">minDuration</a></li>
<li><a href="routing/ChargingStop/powerInKilowatts.html">powerInKilowatts</a></li>
<li class="inherited"><a href="routing/ChargingStop/runtimeType.html">runtimeType</a></li>
<li><a href="routing/ChargingStop/supplyType.html">supplyType</a></li>
<li><a href="routing/ChargingStop/voltageInVolts.html">voltageInVolts</a></li>
<li class="section-title inherited"><a href="routing/ChargingStop-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="routing/ChargingStop/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="routing/ChargingStop/toString.html">toString</a></li>
<li class="section-title"><a href="routing/ChargingStop-class.html#operators">Operators</a></li>
<li><a href="routing/ChargingStop/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li class="self-crumb">ChargingStop class</li>
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
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/ChargingStop-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>ChargingStop class</h1></div>
<section class="desc markdown">
<p>The options to specify a user-planned charging stop.</p>
<p><strong>Note:</strong>
In order to specify this <a href="../routing/ChargingStop-class.html">/sdk-for-flutter-explore-routing-chargingstop-class</a>, it is also required to set
<code>sdk.routing.BatterySpecifications.total_capacity_in_kilowatt_hours</code>, <code>sdk.routing.BatterySpecifications.initial_charge_in_kilowatt_hours</code>,
and <a href="../routing/BatterySpecifications/chargingCurve.html">/sdk-for-flutter-explore-routing-batteryspecifications-chargingcurve</a>.
Without all of them, the route calculation will fail as an invalid parameter error.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="ChargingStop">
<a href="../routing/ChargingStop/ChargingStop.html">/sdk-for-flutter-explore-routing-chargingstop-chargingstop</a>(double powerInKilowatts, double currentInAmperes, double voltageInVolts, <a href="../routing/ChargingSupplyType.html">/sdk-for-flutter-explore-routing-chargingsupplytype</a>? supplyType, Duration? minDuration, Duration? maxDuration)
</dt>
<dd>
          Creates a new instance.
        </dd>
<dt class="callable" id="ChargingStop.withDefaults">
<a href="../routing/ChargingStop/ChargingStop.withDefaults.html">/sdk-for-flutter-explore-routing-chargingstop-chargingstop-withdefaults</a>()
</dt>
<dd>
          Creates a new instance.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="currentInAmperes">
<a href="../routing/ChargingStop/currentInAmperes.html">/sdk-for-flutter-explore-routing-chargingstop-currentinamperes</a>
↔ double
</dt>
<dd>
  The value of rated current of the connector (in A).
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
<a href="../routing/ChargingStop/hashCode.html">/sdk-for-flutter-explore-routing-chargingstop-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="maxDuration">
<a href="../routing/ChargingStop/maxDuration.html">/sdk-for-flutter-explore-routing-chargingstop-maxduration</a>
↔ Duration?
</dt>
<dd>
  The maximum duration the user plans to charge at the station,
including <a href="../routing/BatterySpecifications/chargingSetupDuration.html">/sdk-for-flutter-explore-routing-batteryspecifications-chargingsetupduration</a>.
<strong>Note:</strong>
At least one of <code>min_duration</code> and <code>max_duration</code> is required for a user-planned charging stop.
For most use cases, providing at least <code>min_duration</code> is recommended.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="minDuration">
<a href="../routing/ChargingStop/minDuration.html">/sdk-for-flutter-explore-routing-chargingstop-minduration</a>
↔ Duration?
</dt>
<dd>
  The minimum duration the user expects to charge at the station,
including <a href="../routing/BatterySpecifications/chargingSetupDuration.html">/sdk-for-flutter-explore-routing-batteryspecifications-chargingsetupduration</a>.
<strong>Note:</strong>
At least one of <code>min_duration</code> and <code>max_duration</code> is required for a user-planned charging stop.
For most use cases, providing at least <code>min_duration</code> is recommended.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="powerInKilowatts">
<a href="../routing/ChargingStop/powerInKilowatts.html">/sdk-for-flutter-explore-routing-chargingstop-powerinkilowatts</a>
↔ double
</dt>
<dd>
  The value of rated power of the connector (in kW).
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../routing/ChargingStop/runtimeType.html">/sdk-for-flutter-explore-routing-chargingstop-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="supplyType">
<a href="../routing/ChargingStop/supplyType.html">/sdk-for-flutter-explore-routing-chargingstop-supplytype</a>
↔ <a href="../routing/ChargingSupplyType.html">/sdk-for-flutter-explore-routing-chargingsupplytype</a>?
</dt>
<dd>
  Supply type of the suggested connector.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="voltageInVolts">
<a href="../routing/ChargingStop/voltageInVolts.html">/sdk-for-flutter-explore-routing-chargingstop-voltageinvolts</a>
↔ double
</dt>
<dd>
  The value of rated voltage of the connector (in V).
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
<a href="../routing/ChargingStop/noSuchMethod.html">/sdk-for-flutter-explore-routing-chargingstop-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../routing/ChargingStop/toString.html">/sdk-for-flutter-explore-routing-chargingstop-tostring</a>(<wbr/>)
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
<a href="../routing/ChargingStop/operator_equals.html">/sdk-for-flutter-explore-routing-chargingstop-operator-equals</a>(<wbr/>Object other)
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
<li class="self-crumb">ChargingStop class</li>
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
