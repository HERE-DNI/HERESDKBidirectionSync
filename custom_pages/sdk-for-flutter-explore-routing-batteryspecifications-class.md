---
title: "Constructors"
slug: "sdk-for-flutter-explore-routing-batteryspecifications-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- BatterySpecifications-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="routing/BatterySpecifications-class.html#constructors">Constructors</a></li>
<li><a href="routing/BatterySpecifications/BatterySpecifications.html">BatterySpecifications</a></li>
<li><a href="routing/BatterySpecifications/BatterySpecifications.withDefaults.html">withDefaults</a></li>
<li class="section-title">
<a href="routing/BatterySpecifications-class.html#instance-properties">Properties</a>
</li>
<li><a href="routing/BatterySpecifications/chargingCurve.html">chargingCurve</a></li>
<li><a href="routing/BatterySpecifications/chargingSetupDuration.html">chargingSetupDuration</a></li>
<li><a href="routing/BatterySpecifications/connectorTypes.html">connectorTypes</a></li>
<li><a href="routing/BatterySpecifications/hashCode.html">hashCode</a></li>
<li><a href="routing/BatterySpecifications/initialChargeInKilowattHours.html">initialChargeInKilowattHours</a></li>
<li><a href="routing/BatterySpecifications/maxChargingCurrentInAmperes.html">maxChargingCurrentInAmperes</a></li>
<li><a href="routing/BatterySpecifications/maxChargingVoltageInVolts.html">maxChargingVoltageInVolts</a></li>
<li><a href="routing/BatterySpecifications/maxPowerAtLowVoltageInKilowatts.html">maxPowerAtLowVoltageInKilowatts</a></li>
<li><a href="routing/BatterySpecifications/minChargeAtChargingStationInKilowattHours.html">minChargeAtChargingStationInKilowattHours</a></li>
<li><a href="routing/BatterySpecifications/minChargeAtDestinationInKilowattHours.html">minChargeAtDestinationInKilowattHours</a></li>
<li><a href="routing/BatterySpecifications/minChargeAtFirstChargingStationInKilowattHours.html">minChargeAtFirstChargingStationInKilowattHours</a></li>
<li class="inherited"><a href="routing/BatterySpecifications/runtimeType.html">runtimeType</a></li>
<li><a href="routing/BatterySpecifications/targetChargeInKilowattHours.html">targetChargeInKilowattHours</a></li>
<li><a href="routing/BatterySpecifications/totalCapacityInKilowattHours.html">totalCapacityInKilowattHours</a></li>
<li class="section-title inherited"><a href="routing/BatterySpecifications-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="routing/BatterySpecifications/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="routing/BatterySpecifications/toString.html">toString</a></li>
<li class="section-title"><a href="routing/BatterySpecifications-class.html#operators">Operators</a></li>
<li><a href="routing/BatterySpecifications/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
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
<a href="../routing/BatterySpecifications/BatterySpecifications.html">/sdk-for-flutter-explore-routing-batteryspecifications-batteryspecifications</a>([double totalCapacityInKilowattHours = 0.0, double initialChargeInKilowattHours = 0.0, double targetChargeInKilowattHours = 0.0, Map&lt;<wbr/>double, double&gt; chargingCurve = const {}, List&lt;<wbr/><a href="../routing/ChargingConnectorType.html">/sdk-for-flutter-explore-routing-chargingconnectortype</a>&gt; connectorTypes = const [], double minChargeAtChargingStationInKilowattHours = 0.0, double? minChargeAtFirstChargingStationInKilowattHours = null, double minChargeAtDestinationInKilowattHours = 0.0, double? maxChargingVoltageInVolts = null, double? maxChargingCurrentInAmperes = null, Duration chargingSetupDuration = const Duration(seconds: 0), double? maxPowerAtLowVoltageInKilowatts = null])
</dt>
<dd>
          Creates a new instance.
        </dd>
<dt class="callable" id="BatterySpecifications.withDefaults">
<a href="../routing/BatterySpecifications/BatterySpecifications.withDefaults.html">/sdk-for-flutter-explore-routing-batteryspecifications-batteryspecifications-withdefaults</a>()
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
<a href="../routing/BatterySpecifications/chargingCurve.html">/sdk-for-flutter-explore-routing-batteryspecifications-chargingcurve</a>
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
[0, <a href="../routing/BatterySpecifications/targetChargeInKilowattHours.html">/sdk-for-flutter-explore-routing-batteryspecifications-targetchargeinkilowatthours</a>],
otherwise the <a href="../routing/BatterySpecifications-class.html">/sdk-for-flutter-explore-routing-batteryspecifications-class</a> instance is considered invalid.
The charging curve is considered piecewise constant instead of being interpolated.
Defaults to an empty container.
<strong>Note:</strong>
For a user-planned <a href="../routing/ChargingStop-class.html">/sdk-for-flutter-explore-routing-chargingstop-class</a>, this parameter is also required.
If one or more values are not set, the route calculation will fail as an invalid parameter error.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="chargingSetupDuration">
<a href="../routing/BatterySpecifications/chargingSetupDuration.html">/sdk-for-flutter-explore-routing-batteryspecifications-chargingsetupduration</a>
↔ Duration
</dt>
<dd>
  Time in seconds spent after arriving at a charging station, but before actually charging,
e.g., time spent for payment processing.
Defaults to 0 seconds.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="connectorTypes">
<a href="../routing/BatterySpecifications/connectorTypes.html">/sdk-for-flutter-explore-routing-batteryspecifications-connectortypes</a>
↔ List&lt;<wbr/><a href="../routing/ChargingConnectorType.html">/sdk-for-flutter-explore-routing-chargingconnectortype</a>&gt;
</dt>
<dd>
  List of available charging connector types.
It must be at least one charging connector type added, otherwise
the <a href="../routing/BatterySpecifications-class.html">/sdk-for-flutter-explore-routing-batteryspecifications-class</a> instance is considered invalid.
Defaults to an empty container.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
<a href="../routing/BatterySpecifications/hashCode.html">/sdk-for-flutter-explore-routing-batteryspecifications-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="initialChargeInKilowattHours">
<a href="../routing/BatterySpecifications/initialChargeInKilowattHours.html">/sdk-for-flutter-explore-routing-batteryspecifications-initialchargeinkilowatthours</a>
↔ double
</dt>
<dd>
  Charge level of the vehicle's battery at the start of the route (in kWh).
It must be non-negative and less than or equal to the value of
<a href="../routing/BatterySpecifications/totalCapacityInKilowattHours.html">/sdk-for-flutter-explore-routing-batteryspecifications-totalcapacityinkilowatthours</a>,
otherwise the <a href="../routing/BatterySpecifications-class.html">/sdk-for-flutter-explore-routing-batteryspecifications-class</a> instance is considered invalid.
Defaults to 0.
<strong>Note:</strong>
For a user-planned <a href="../routing/ChargingStop-class.html">/sdk-for-flutter-explore-routing-chargingstop-class</a>, this parameter is also required.
If not set greater than 0, the route calculation will fail as an an invalid parameter error.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="maxChargingCurrentInAmperes">
<a href="../routing/BatterySpecifications/maxChargingCurrentInAmperes.html">/sdk-for-flutter-explore-routing-batteryspecifications-maxchargingcurrentinamperes</a>
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
<a href="../routing/BatterySpecifications/maxChargingVoltageInVolts.html">/sdk-for-flutter-explore-routing-batteryspecifications-maxchargingvoltageinvolts</a>
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
<a href="../routing/BatterySpecifications/maxPowerAtLowVoltageInKilowatts.html">/sdk-for-flutter-explore-routing-batteryspecifications-maxpoweratlowvoltageinkilowatts</a>
↔ double?
</dt>
<dd>
  The maximum power in kilowatts at which a vehicle can charge under given these conditions:
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="minChargeAtChargingStationInKilowattHours">
<a href="../routing/BatterySpecifications/minChargeAtChargingStationInKilowattHours.html">/sdk-for-flutter-explore-routing-batteryspecifications-minchargeatchargingstationinkilowatthours</a>
↔ double
</dt>
<dd>
  Minimum charge when arriving at a charging station in kWh.
It must be non-negative and less than the value of
<a href="../routing/BatterySpecifications/targetChargeInKilowattHours.html">/sdk-for-flutter-explore-routing-batteryspecifications-targetchargeinkilowatthours</a>,
otherwise the <a href="../routing/BatterySpecifications-class.html">/sdk-for-flutter-explore-routing-batteryspecifications-class</a> instance is considered invalid.
Defaults to 0.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="minChargeAtDestinationInKilowattHours">
<a href="../routing/BatterySpecifications/minChargeAtDestinationInKilowattHours.html">/sdk-for-flutter-explore-routing-batteryspecifications-minchargeatdestinationinkilowatthours</a>
↔ double
</dt>
<dd>
  Minimum charge at the final route destination in kWh.
It must be non-negative and less than the value of
<a href="../routing/BatterySpecifications/targetChargeInKilowattHours.html">/sdk-for-flutter-explore-routing-batteryspecifications-targetchargeinkilowatthours</a>,
otherwise the <a href="../routing/BatterySpecifications-class.html">/sdk-for-flutter-explore-routing-batteryspecifications-class</a> instance is considered invalid.
Defaults to 0.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="minChargeAtFirstChargingStationInKilowattHours">
<a href="../routing/BatterySpecifications/minChargeAtFirstChargingStationInKilowattHours.html">/sdk-for-flutter-explore-routing-batteryspecifications-minchargeatfirstchargingstationinkilowatthours</a>
↔ double?
</dt>
<dd>
  Minimum charge when arriving at first charging station in kWh.
This overrides <a href="../routing/BatterySpecifications/minChargeAtChargingStationInKilowattHours.html">/sdk-for-flutter-explore-routing-batteryspecifications-minchargeatchargingstationinkilowatthours</a> for the first charging station.
If not specified, <a href="../routing/BatterySpecifications/minChargeAtChargingStationInKilowattHours.html">/sdk-for-flutter-explore-routing-batteryspecifications-minchargeatchargingstationinkilowatthours</a> will be used
for all charging stations, including the first one.
Defaults to <code>null</code>.
When initialized, it must be non-negative and less than the value of
<a href="../routing/BatterySpecifications/targetChargeInKilowattHours.html">/sdk-for-flutter-explore-routing-batteryspecifications-targetchargeinkilowatthours</a>,
otherwise the <a href="../routing/BatterySpecifications-class.html">/sdk-for-flutter-explore-routing-batteryspecifications-class</a> instance is considered invalid.
This is usually used when the current charge is too low to reach a charging station within <code>minChargeAtChargingStation</code> limits.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../routing/BatterySpecifications/runtimeType.html">/sdk-for-flutter-explore-routing-batteryspecifications-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="targetChargeInKilowattHours">
<a href="../routing/BatterySpecifications/targetChargeInKilowattHours.html">/sdk-for-flutter-explore-routing-batteryspecifications-targetchargeinkilowatthours</a>
↔ double
</dt>
<dd>
  Maximum charge to which the battery should be charged at a charging station (in kWh).
It must be positive and less than or equal to the value of
<a href="../routing/BatterySpecifications/totalCapacityInKilowattHours.html">/sdk-for-flutter-explore-routing-batteryspecifications-totalcapacityinkilowatthours</a>,
otherwise the <a href="../routing/BatterySpecifications-class.html">/sdk-for-flutter-explore-routing-batteryspecifications-class</a> instance is considered invalid.
Defaults to 0.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="totalCapacityInKilowattHours">
<a href="../routing/BatterySpecifications/totalCapacityInKilowattHours.html">/sdk-for-flutter-explore-routing-batteryspecifications-totalcapacityinkilowatthours</a>
↔ double
</dt>
<dd>
  Total capacity of the vehicle's battery (in kWh).
It must be positive.
Defaults to 0.
<strong>Note:</strong>
For a user-planned <a href="../routing/ChargingStop-class.html">/sdk-for-flutter-explore-routing-chargingstop-class</a>, this parameter is also required.
If not set greater than 0, the route calculation will fail as an invalid parameter error.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
<a href="../routing/BatterySpecifications/noSuchMethod.html">/sdk-for-flutter-explore-routing-batteryspecifications-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../routing/BatterySpecifications/toString.html">/sdk-for-flutter-explore-routing-batteryspecifications-tostring</a>(<wbr/>)
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
<a href="../routing/BatterySpecifications/operator_equals.html">/sdk-for-flutter-explore-routing-batteryspecifications-operator-equals</a>(<wbr/>Object other)
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
</div></div>
</div>
</HTMLBlock>
