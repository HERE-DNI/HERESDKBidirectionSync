---
title: "Untitled"
slug: "sdk-for-flutter-explore-routing-batteryspecifications-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- BatterySpecifications-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-routing-routing-library</li>
<li class="self-crumb">BatterySpecifications class</li>
</ol>
<div class="self-name">BatterySpecifications</div>
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
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/BatterySpecifications-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>BatterySpecifications class</h1></div>
<section class="desc markdown">
<p>Parameters related to the electric vehicle's battery.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="BatterySpecifications">
/sdk-for-flutter-explore-routing-batteryspecifications-batteryspecifications([double totalCapacityInKilowattHours = 0.0, double initialChargeInKilowattHours = 0.0, double targetChargeInKilowattHours = 0.0, Map&lt;<wbr/>double, double&gt; chargingCurve = const {}, List&lt;<wbr/>/sdk-for-flutter-explore-routing-chargingconnectortype&gt; connectorTypes = const [], double minChargeAtChargingStationInKilowattHours = 0.0, double? minChargeAtFirstChargingStationInKilowattHours = null, double minChargeAtDestinationInKilowattHours = 0.0, double? maxChargingVoltageInVolts = null, double? maxChargingCurrentInAmperes = null, Duration chargingSetupDuration = const Duration(seconds: 0), double? maxPowerAtLowVoltageInKilowatts = null])
</dt>
<dd>
          Creates a new instance.
        </dd>
<dt class="callable" id="BatterySpecifications.withDefaults">
/sdk-for-flutter-explore-routing-batteryspecifications-batteryspecifications-withdefaults()
</dt>
<dd>
          Creates a new instance.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="chargingCurve">
/sdk-for-flutter-explore-routing-batteryspecifications-chargingcurve
↔ Map&lt;<wbr/>double, double&gt;
</dt>
<dd>
  Function curve describing the maximum battery charging rate (in kW) at a given charge
level (in kWh).
Map keys represent charge levels that are non-negative floating point values
in units of (kWh).
Map values represent charging rate values that are positive floating point values
in units of (kW).
Given charge levels must cover the entire range of
[0, /sdk-for-flutter-explore-routing-batteryspecifications-targetchargeinkilowatthours],
otherwise the /sdk-for-flutter-explore-routing-batteryspecifications-class instance is considered invalid.
The charging curve is considered piecewise constant instead of being interpolated.
Defaults to an empty container.
<strong>Note:</strong>
For a user-planned /sdk-for-flutter-explore-routing-chargingstop-class, this parameter is also required.
If one or more values are not set, the route calculation will fail as an invalid parameter error.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="chargingSetupDuration">
/sdk-for-flutter-explore-routing-batteryspecifications-chargingsetupduration
↔ Duration
</dt>
<dd>
  Time in seconds spent after arriving at a charging station, but before actually charging,
e.g., time spent for payment processing.
Defaults to 0 seconds.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="connectorTypes">
/sdk-for-flutter-explore-routing-batteryspecifications-connectortypes
↔ List&lt;<wbr/>/sdk-for-flutter-explore-routing-chargingconnectortype&gt;
</dt>
<dd>
  List of available charging connector types.
It must be at least one charging connector type added, otherwise
the /sdk-for-flutter-explore-routing-batteryspecifications-class instance is considered invalid.
Defaults to an empty container.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-explore-routing-batteryspecifications-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="initialChargeInKilowattHours">
/sdk-for-flutter-explore-routing-batteryspecifications-initialchargeinkilowatthours
↔ double
</dt>
<dd>
  Charge level of the vehicle's battery at the start of the route (in kWh).
It must be non-negative and less than or equal to the value of
/sdk-for-flutter-explore-routing-batteryspecifications-totalcapacityinkilowatthours,
otherwise the /sdk-for-flutter-explore-routing-batteryspecifications-class instance is considered invalid.
Defaults to 0.
<strong>Note:</strong>
For a user-planned /sdk-for-flutter-explore-routing-chargingstop-class, this parameter is also required.
If not set greater than 0, the route calculation will fail as an an invalid parameter error.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="maxChargingCurrentInAmperes">
/sdk-for-flutter-explore-routing-batteryspecifications-maxchargingcurrentinamperes
↔ double?
</dt>
<dd>
  Maximum charging current supported by the vehicle's battery in Amperes.
It must be positive.
When omitted, the charging current is determined by the charging station attributes.
Defaults to <code>null</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="maxChargingVoltageInVolts">
/sdk-for-flutter-explore-routing-batteryspecifications-maxchargingvoltageinvolts
↔ double?
</dt>
<dd>
  Maximum charging voltage supported by the vehicle's battery in Volts.
It must be positive.
When omitted, the voltage is determined by the charging station attributes.
Defaults to <code>null</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="maxPowerAtLowVoltageInKilowatts">
/sdk-for-flutter-explore-routing-batteryspecifications-maxpoweratlowvoltageinkilowatts
↔ double?
</dt>
<dd>
  The maximum power in kilowatts at which a vehicle can charge under given these conditions:
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="minChargeAtChargingStationInKilowattHours">
/sdk-for-flutter-explore-routing-batteryspecifications-minchargeatchargingstationinkilowatthours
↔ double
</dt>
<dd>
  Minimum charge when arriving at a charging station in kWh.
It must be non-negative and less than the value of
/sdk-for-flutter-explore-routing-batteryspecifications-targetchargeinkilowatthours,
otherwise the /sdk-for-flutter-explore-routing-batteryspecifications-class instance is considered invalid.
Defaults to 0.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="minChargeAtDestinationInKilowattHours">
/sdk-for-flutter-explore-routing-batteryspecifications-minchargeatdestinationinkilowatthours
↔ double
</dt>
<dd>
  Minimum charge at the final route destination in kWh.
It must be non-negative and less than the value of
/sdk-for-flutter-explore-routing-batteryspecifications-targetchargeinkilowatthours,
otherwise the /sdk-for-flutter-explore-routing-batteryspecifications-class instance is considered invalid.
Defaults to 0.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="minChargeAtFirstChargingStationInKilowattHours">
/sdk-for-flutter-explore-routing-batteryspecifications-minchargeatfirstchargingstationinkilowatthours
↔ double?
</dt>
<dd>
  Minimum charge when arriving at first charging station in kWh.
This overrides /sdk-for-flutter-explore-routing-batteryspecifications-minchargeatchargingstationinkilowatthours for the first charging station.
If not specified, /sdk-for-flutter-explore-routing-batteryspecifications-minchargeatchargingstationinkilowatthours will be used
for all charging stations, including the first one.
Defaults to <code>null</code>.
When initialized, it must be non-negative and less than the value of
/sdk-for-flutter-explore-routing-batteryspecifications-targetchargeinkilowatthours,
otherwise the /sdk-for-flutter-explore-routing-batteryspecifications-class instance is considered invalid.
This is usually used when the current charge is too low to reach a charging station within <code>minChargeAtChargingStation</code> limits.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-routing-batteryspecifications-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="targetChargeInKilowattHours">
/sdk-for-flutter-explore-routing-batteryspecifications-targetchargeinkilowatthours
↔ double
</dt>
<dd>
  Maximum charge to which the battery should be charged at a charging station (in kWh).
It must be positive and less than or equal to the value of
/sdk-for-flutter-explore-routing-batteryspecifications-totalcapacityinkilowatthours,
otherwise the /sdk-for-flutter-explore-routing-batteryspecifications-class instance is considered invalid.
Defaults to 0.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="totalCapacityInKilowattHours">
/sdk-for-flutter-explore-routing-batteryspecifications-totalcapacityinkilowatthours
↔ double
</dt>
<dd>
  Total capacity of the vehicle's battery (in kWh).
It must be positive.
Defaults to 0.
<strong>Note:</strong>
For a user-planned /sdk-for-flutter-explore-routing-chargingstop-class, this parameter is also required.
If not set greater than 0, the route calculation will fail as an invalid parameter error.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-explore-routing-batteryspecifications-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-routing-batteryspecifications-tostring(<wbr/>)
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
/sdk-for-flutter-explore-routing-batteryspecifications-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">BatterySpecifications class</li>
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
