---
title: "Constructors"
slug: "sdk-for-flutter-explore-routing-empiricalconsumptionmodel-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- EmpiricalConsumptionModel-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="routing/EmpiricalConsumptionModel-class.html#constructors">Constructors</a></li>
<li><a href="routing/EmpiricalConsumptionModel/EmpiricalConsumptionModel.html">EmpiricalConsumptionModel</a></li>
<li class="section-title">
<a href="routing/EmpiricalConsumptionModel-class.html#instance-properties">Properties</a>
</li>
<li><a href="routing/EmpiricalConsumptionModel/ascentConsumptionInWattHoursPerMeter.html">ascentConsumptionInWattHoursPerMeter</a></li>
<li><a href="routing/EmpiricalConsumptionModel/auxiliaryConsumptionInWattHoursPerSecond.html">auxiliaryConsumptionInWattHoursPerSecond</a></li>
<li><a href="routing/EmpiricalConsumptionModel/descentRecoveryInWattHoursPerMeter.html">descentRecoveryInWattHoursPerMeter</a></li>
<li><a href="routing/EmpiricalConsumptionModel/freeFlowSpeedTable.html">freeFlowSpeedTable</a></li>
<li><a href="routing/EmpiricalConsumptionModel/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="routing/EmpiricalConsumptionModel/runtimeType.html">runtimeType</a></li>
<li><a href="routing/EmpiricalConsumptionModel/trafficSpeedTable.html">trafficSpeedTable</a></li>
<li class="section-title inherited"><a href="routing/EmpiricalConsumptionModel-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="routing/EmpiricalConsumptionModel/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="routing/EmpiricalConsumptionModel/toString.html">toString</a></li>
<li class="section-title"><a href="routing/EmpiricalConsumptionModel-class.html#operators">Operators</a></li>
<li><a href="routing/EmpiricalConsumptionModel/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li class="self-crumb">EmpiricalConsumptionModel class</li>
</ol>
<div class="self-name">EmpiricalConsumptionModel</div>
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
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/EmpiricalConsumptionModel-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>EmpiricalConsumptionModel class</h1></div>
<section class="desc markdown">
<p>This model defines a data-driven energy consumption model for electric vehicles.</p>
<p>It estimates the electrical energy required to traverse a route by combining empirically derived vehicle
parameters with route characteristics such as distance, elevation changes, and driving speed. Rather than
relying on a full physical simulation, this model uses observed consumption behavior to produce realistic
and efficient energy estimates suitable for routing, range prediction, and navigation use cases.</p>
<p>Parameters specific to the electric vehicle are used to calculate energy consumption on a given route.
At minimum, you must provide <a href="../routing/EmpiricalConsumptionModel/ascentConsumptionInWattHoursPerMeter.html">/sdk-for-flutter-explore-routing-empiricalconsumptionmodel-ascentconsumptioninwatthourspermeter</a>,
<a href="../routing/EmpiricalConsumptionModel/descentRecoveryInWattHoursPerMeter.html">/sdk-for-flutter-explore-routing-empiricalconsumptionmodel-descentrecoveryinwatthourspermeter</a> and a
<a href="../routing/EmpiricalConsumptionModel/freeFlowSpeedTable.html">/sdk-for-flutter-explore-routing-empiricalconsumptionmodel-freeflowspeedtable</a>.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="EmpiricalConsumptionModel">
<a href="../routing/EmpiricalConsumptionModel/EmpiricalConsumptionModel.html">/sdk-for-flutter-explore-routing-empiricalconsumptionmodel-empiricalconsumptionmodel</a>()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="ascentConsumptionInWattHoursPerMeter">
<a href="../routing/EmpiricalConsumptionModel/ascentConsumptionInWattHoursPerMeter.html">/sdk-for-flutter-explore-routing-empiricalconsumptionmodel-ascentconsumptioninwatthourspermeter</a>
↔ double
</dt>
<dd>
  Rate of energy consumed per meter rise in elevation (in Wh/m, i.e., Watt-hours per meter).
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="auxiliaryConsumptionInWattHoursPerSecond">
<a href="../routing/EmpiricalConsumptionModel/auxiliaryConsumptionInWattHoursPerSecond.html">/sdk-for-flutter-explore-routing-empiricalconsumptionmodel-auxiliaryconsumptioninwatthourspersecond</a>
↔ double
</dt>
<dd>
  Rate of energy (in Wh/s) consumed by the vehicle's auxiliary systems
(e.g., air conditioning, lights) per second of travel.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="descentRecoveryInWattHoursPerMeter">
<a href="../routing/EmpiricalConsumptionModel/descentRecoveryInWattHoursPerMeter.html">/sdk-for-flutter-explore-routing-empiricalconsumptionmodel-descentrecoveryinwatthourspermeter</a>
↔ double
</dt>
<dd>
  Rate of energy recovered per meter fall in elevation (in Wh/m, i.e., Watt-hours per meter).
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="freeFlowSpeedTable">
<a href="../routing/EmpiricalConsumptionModel/freeFlowSpeedTable.html">/sdk-for-flutter-explore-routing-empiricalconsumptionmodel-freeflowspeedtable</a>
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
<a href="../routing/EmpiricalConsumptionModel/hashCode.html">/sdk-for-flutter-explore-routing-empiricalconsumptionmodel-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../routing/EmpiricalConsumptionModel/runtimeType.html">/sdk-for-flutter-explore-routing-empiricalconsumptionmodel-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="trafficSpeedTable">
<a href="../routing/EmpiricalConsumptionModel/trafficSpeedTable.html">/sdk-for-flutter-explore-routing-empiricalconsumptionmodel-trafficspeedtable</a>
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
If <a href="../routing/EmpiricalConsumptionModel/trafficSpeedTable.html">/sdk-for-flutter-explore-routing-empiricalconsumptionmodel-trafficspeedtable</a> is empty then only
<a href="../routing/EmpiricalConsumptionModel/freeFlowSpeedTable.html">/sdk-for-flutter-explore-routing-empiricalconsumptionmodel-freeflowspeedtable</a> is used for calculating speed-related
energy consumption.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
<a href="../routing/EmpiricalConsumptionModel/noSuchMethod.html">/sdk-for-flutter-explore-routing-empiricalconsumptionmodel-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../routing/EmpiricalConsumptionModel/toString.html">/sdk-for-flutter-explore-routing-empiricalconsumptionmodel-tostring</a>(<wbr/>)
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
<a href="../routing/EmpiricalConsumptionModel/operator_equals.html">/sdk-for-flutter-explore-routing-empiricalconsumptionmodel-operator-equals</a>(<wbr/>Object other)
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
<li class="self-crumb">EmpiricalConsumptionModel class</li>
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
