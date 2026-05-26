---
title: "EVConsumptionModel class"
slug: "sdk-for-flutter-explore-routing-evconsumptionmodel-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- EVConsumptionModel-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="routing/EVConsumptionModel-class.html#constructors">Constructors</a></li>
<li><a href="routing/EVConsumptionModel/EVConsumptionModel.html">EVConsumptionModel</a></li>
<li class="section-title">
<a href="routing/EVConsumptionModel-class.html#instance-properties">Properties</a>
</li>
<li><a href="routing/EVConsumptionModel/ascentConsumptionInWattHoursPerMeter.html">ascentConsumptionInWattHoursPerMeter</a></li>
<li><a href="routing/EVConsumptionModel/auxiliaryConsumptionInWattHoursPerSecond.html">auxiliaryConsumptionInWattHoursPerSecond</a></li>
<li><a href="routing/EVConsumptionModel/descentRecoveryInWattHoursPerMeter.html">descentRecoveryInWattHoursPerMeter</a></li>
<li><a href="routing/EVConsumptionModel/freeFlowSpeedTable.html">freeFlowSpeedTable</a></li>
<li><a href="routing/EVConsumptionModel/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="routing/EVConsumptionModel/runtimeType.html">runtimeType</a></li>
<li><a href="routing/EVConsumptionModel/trafficSpeedTable.html">trafficSpeedTable</a></li>
<li class="section-title inherited"><a href="routing/EVConsumptionModel-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="routing/EVConsumptionModel/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="routing/EVConsumptionModel/toString.html">toString</a></li>
<li class="section-title"><a href="routing/EVConsumptionModel-class.html#operators">Operators</a></li>
<li><a href="routing/EVConsumptionModel/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-routing-routing-library</li>
<li class="self-crumb">EVConsumptionModel class</li>
</ol>
<div class="self-name">EVConsumptionModel</div>
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
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/EVConsumptionModel-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>EVConsumptionModel class</h1></div>
<section class="desc markdown">
<p>Parameters specific for the electric vehicle, which are then used to calculate
energy consumption on a given route.</p>
<p>At minimum, you must provide /sdk-for-flutter-explore-routing-evconsumptionmodel-ascentconsumptioninwatthourspermeter,
/sdk-for-flutter-explore-routing-evconsumptionmodel-descentrecoveryinwatthourspermeter and a
/sdk-for-flutter-explore-routing-evconsumptionmodel-freeflowspeedtable.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="EVConsumptionModel">
/sdk-for-flutter-explore-routing-evconsumptionmodel-evconsumptionmodel()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="ascentConsumptionInWattHoursPerMeter">
/sdk-for-flutter-explore-routing-evconsumptionmodel-ascentconsumptioninwatthourspermeter
↔ double
</dt>
<dd>
  Rate of energy consumed per meter rise in elevation (in Wh/m, i.e., Watt-hours per meter).
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="auxiliaryConsumptionInWattHoursPerSecond">
/sdk-for-flutter-explore-routing-evconsumptionmodel-auxiliaryconsumptioninwatthourspersecond
↔ double
</dt>
<dd>
  Rate of energy (in Wh/s) consumed by the vehicle's auxiliary systems
(e.g., air conditioning, lights) per second of travel.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="descentRecoveryInWattHoursPerMeter">
/sdk-for-flutter-explore-routing-evconsumptionmodel-descentrecoveryinwatthourspermeter
↔ double
</dt>
<dd>
  Rate of energy recovered per meter fall in elevation (in Wh/m, i.e., Watt-hours per meter).
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="freeFlowSpeedTable">
/sdk-for-flutter-explore-routing-evconsumptionmodel-freeflowspeedtable
↔ Map&lt;<wbr/>int, double&gt;
</dt>
<dd>
  Free flow speed table describes energy consumption when traveling at constant speed.
It defines a function curve specifying consumption rate at a given free flow speed
on a flat stretch of road.
Map keys represent speed values that are non-negative integers in units of (km/h).
Map values represent consumption values that are non-negative floating point values
in units of (Wh/m).
The function is linearly interpolated between each successive pair of data points:
For values below the first list value, the first value is used.
For values after the last list value, the last list value is used.
At minimum, one key/value pair must be set. In this case the consumption value is
used for all possible speed keys.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-explore-routing-evconsumptionmodel-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-routing-evconsumptionmodel-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="trafficSpeedTable">
/sdk-for-flutter-explore-routing-evconsumptionmodel-trafficspeedtable
↔ Map&lt;<wbr/>int, double&gt;
</dt>
<dd>
  Traffic speed table describes energy consumption when traveling under heavy traffic
conditions, i.e. when the vehicle is expected to often change the travel speed.
It defines a function curve specifying consumption rate at a given speed under traffic
conditions on a flat stretch of road.
Map keys represent traffic speed values that are non-negative integers in units of (km/h).
Map values represent consumption values that are non-negative floating point values
in units of (Wh/m).
The function is linearly interpolated between each successive pair of data points:
For values below the first list value, the first value is used.
For values after the last list value, the last list value is used.
If only one key/value pair is set, the consumption value is
used for all possible traffic speed keys.
If /sdk-for-flutter-explore-routing-evconsumptionmodel-trafficspeedtable is empty then only
/sdk-for-flutter-explore-routing-evconsumptionmodel-freeflowspeedtable is used for calculating speed-related
energy consumption.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-explore-routing-evconsumptionmodel-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-routing-evconsumptionmodel-tostring(<wbr/>)
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
/sdk-for-flutter-explore-routing-evconsumptionmodel-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">EVConsumptionModel class</li>
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
`
}</HTMLBlock>
