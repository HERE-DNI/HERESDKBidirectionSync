---
title: "EmpiricalConsumptionModel class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-empiricalconsumptionmodel-class"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/EmpiricalConsumptionModel-class-sidebar.html">

<div>

# <span class="kind-class">EmpiricalConsumptionModel</span> class

</div>

<div class="section desc markdown">

This model defines a data-driven energy consumption model for electric vehicles.

It estimates the electrical energy required to traverse a route by combining empirically derived vehicle parameters with route characteristics such as distance, elevation changes, and driving speed. Rather than relying on a full physical simulation, this model uses observed consumption behavior to produce realistic and efficient energy estimates suitable for routing, range prediction, and navigation use cases.

Parameters specific to the electric vehicle are used to calculate energy consumption on a given route. At minimum, you must provide <a href="sdk-for-flutter-explore-routing-empiricalconsumptionmodel-ascentconsumptioninwatthourspermeter">EmpiricalConsumptionModel.ascentConsumptionInWattHoursPerMeter</a>, <a href="sdk-for-flutter-explore-routing-empiricalconsumptionmodel-descentrecoveryinwatthourspermeter">EmpiricalConsumptionModel.descentRecoveryInWattHoursPerMeter</a> and a <a href="sdk-for-flutter-explore-routing-empiricalconsumptionmodel-freeflowspeedtable">EmpiricalConsumptionModel.freeFlowSpeedTable</a>. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-routing-empiricalconsumptionmodel-empiricalconsumptionmodel">EmpiricalConsumptionModel</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-explore-routing-empiricalconsumptionmodel-ascentconsumptioninwatthourspermeter">ascentConsumptionInWattHoursPerMeter</a></span> <span class="signature">↔ double</span>  
Rate of energy consumed per meter rise in elevation (in Wh/m, i.e., Watt-hours per meter).

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-empiricalconsumptionmodel-auxiliaryconsumptioninwatthourspersecond">auxiliaryConsumptionInWattHoursPerSecond</a></span> <span class="signature">↔ double</span>  
Rate of energy (in Wh/s) consumed by the vehicle's auxiliary systems (e.g., air conditioning, lights) per second of travel.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-empiricalconsumptionmodel-descentrecoveryinwatthourspermeter">descentRecoveryInWattHoursPerMeter</a></span> <span class="signature">↔ double</span>  
Rate of energy recovered per meter fall in elevation (in Wh/m, i.e., Watt-hours per meter).

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-empiricalconsumptionmodel-freeflowspeedtable">freeFlowSpeedTable</a></span> <span class="signature">↔ Map<span class="signature">\<<wbr></wbr><span class="type-parameter">int</span>, <span class="type-parameter">double</span>\></span></span>  
Free flow speed table describes energy consumption when traveling at constant speed. It defines a function curve specifying consumption rate at a given free flow speed on a flat stretch of road. Map keys represent speed values that are non-negative integers in units of (km/h). Map values represent consumption values that are non-negative floating point values in units of (Wh/m). The function is linearly interpolated between each successive pair of data points: For values below the first list value, the first value is used. For values after the last list value, the last list value is used. At minimum, one key/value pair must be set. In this case the consumption value is used for all possible speed keys.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-empiricalconsumptionmodel-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-empiricalconsumptionmodel-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-empiricalconsumptionmodel-trafficspeedtable">trafficSpeedTable</a></span> <span class="signature">↔ Map<span class="signature">\<<wbr></wbr><span class="type-parameter">int</span>, <span class="type-parameter">double</span>\></span></span>  
Traffic speed table describes energy consumption when traveling under heavy traffic conditions, i.e. when the vehicle is expected to often change the travel speed. It defines a function curve specifying consumption rate at a given speed under traffic conditions on a flat stretch of road. Map keys represent traffic speed values that are non-negative integers in units of (km/h). Map values represent consumption values that are non-negative floating point values in units of (Wh/m). The function is linearly interpolated between each successive pair of data points: For values below the first list value, the first value is used. For values after the last list value, the last list value is used. If only one key/value pair is set, the consumption value is used for all possible traffic speed keys. If <a href="sdk-for-flutter-explore-routing-empiricalconsumptionmodel-trafficspeedtable">EmpiricalConsumptionModel.trafficSpeedTable</a> is empty then only <a href="sdk-for-flutter-explore-routing-empiricalconsumptionmodel-freeflowspeedtable">EmpiricalConsumptionModel.freeFlowSpeedTable</a> is used for calculating speed-related energy consumption.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-routing-empiricalconsumptionmodel-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-empiricalconsumptionmodel-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-routing-empiricalconsumptionmodel-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

