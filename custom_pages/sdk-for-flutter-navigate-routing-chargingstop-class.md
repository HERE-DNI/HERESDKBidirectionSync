---
title: "Untitled"
slug: "sdk-for-flutter-navigate-routing-chargingstop-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ChargingStop-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
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
In order to specify this /sdk-for-flutter-navigate-routing-chargingstop-class, it is also required to set
<code>sdk.routing.BatterySpecifications.total_capacity_in_kilowatt_hours</code>, <code>sdk.routing.BatterySpecifications.initial_charge_in_kilowatt_hours</code>,
and /sdk-for-flutter-navigate-routing-batteryspecifications-chargingcurve.
Without all of them, the route calculation will fail as an invalid parameter error.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="ChargingStop">
/sdk-for-flutter-navigate-routing-chargingstop-chargingstop(double powerInKilowatts, double currentInAmperes, double voltageInVolts, /sdk-for-flutter-navigate-routing-chargingsupplytype? supplyType, Duration? minDuration, Duration? maxDuration)
</dt>
<dd>
          Creates a new instance.
        </dd>
<dt class="callable" id="ChargingStop.withDefaults">
/sdk-for-flutter-navigate-routing-chargingstop-chargingstop-withdefaults()
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
/sdk-for-flutter-navigate-routing-chargingstop-currentinamperes
↔ double
</dt>
<dd>
  The value of rated current of the connector (in A).
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-routing-chargingstop-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="maxDuration">
/sdk-for-flutter-navigate-routing-chargingstop-maxduration
↔ Duration?
</dt>
<dd>
  The maximum duration the user plans to charge at the station,
including /sdk-for-flutter-navigate-routing-batteryspecifications-chargingsetupduration.
<strong>Note:</strong>
At least one of <code>min_duration</code> and <code>max_duration</code> is required for a user-planned charging stop.
For most use cases, providing at least <code>min_duration</code> is recommended.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="minDuration">
/sdk-for-flutter-navigate-routing-chargingstop-minduration
↔ Duration?
</dt>
<dd>
  The minimum duration the user expects to charge at the station,
including /sdk-for-flutter-navigate-routing-batteryspecifications-chargingsetupduration.
<strong>Note:</strong>
At least one of <code>min_duration</code> and <code>max_duration</code> is required for a user-planned charging stop.
For most use cases, providing at least <code>min_duration</code> is recommended.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="powerInKilowatts">
/sdk-for-flutter-navigate-routing-chargingstop-powerinkilowatts
↔ double
</dt>
<dd>
  The value of rated power of the connector (in kW).
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-routing-chargingstop-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="supplyType">
/sdk-for-flutter-navigate-routing-chargingstop-supplytype
↔ /sdk-for-flutter-navigate-routing-chargingsupplytype?
</dt>
<dd>
  Supply type of the suggested connector.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="voltageInVolts">
/sdk-for-flutter-navigate-routing-chargingstop-voltageinvolts
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
/sdk-for-flutter-navigate-routing-chargingstop-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-routing-chargingstop-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-routing-chargingstop-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
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



</div>
`
}</HTMLBlock>
