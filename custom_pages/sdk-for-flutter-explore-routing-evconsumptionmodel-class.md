---
title: "EVConsumptionModel class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-evconsumptionmodel-class"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/EVConsumptionModel-class-sidebar.html">

<div>

# <span class="kind-class">EVConsumptionModel</span> class

</div>

<div class="section desc markdown">

Parameters specific for the electric vehicle, which are then used to calculate energy consumption on a given route.

At minimum, you must provide <a href="sdk-for-flutter-explore-routing-evconsumptionmodel-ascentconsumptioninwatthourspermeter">EVConsumptionModel.ascentConsumptionInWattHoursPerMeter</a>, <a href="sdk-for-flutter-explore-routing-evconsumptionmodel-descentrecoveryinwatthourspermeter">EVConsumptionModel.descentRecoveryInWattHoursPerMeter</a> and a <a href="sdk-for-flutter-explore-routing-evconsumptionmodel-freeflowspeedtable">EVConsumptionModel.freeFlowSpeedTable</a>.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-routing-evconsumptionmodel-evconsumptionmodel">EVConsumptionModel</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-explore-routing-evconsumptionmodel-ascentconsumptioninwatthourspermeter">ascentConsumptionInWattHoursPerMeter</a></span> <span class="signature">↔ double</span>  
Rate of energy consumed per meter rise in elevation (in Wh/m, i.e., Watt-hours per meter).

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-evconsumptionmodel-auxiliaryconsumptioninwatthourspersecond">auxiliaryConsumptionInWattHoursPerSecond</a></span> <span class="signature">↔ double</span>  
Rate of energy (in Wh/s) consumed by the vehicle's auxiliary systems (e.g., air conditioning, lights) per second of travel.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-evconsumptionmodel-descentrecoveryinwatthourspermeter">descentRecoveryInWattHoursPerMeter</a></span> <span class="signature">↔ double</span>  
Rate of energy recovered per meter fall in elevation (in Wh/m, i.e., Watt-hours per meter).

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-evconsumptionmodel-freeflowspeedtable">freeFlowSpeedTable</a></span> <span class="signature">↔ Map<span class="signature">\<<wbr></wbr><span class="type-parameter">int</span>, <span class="type-parameter">double</span>\></span></span>  
Free flow speed table describes energy consumption when traveling at constant speed. It defines a function curve specifying consumption rate at a given free flow speed on a flat stretch of road. Map keys represent speed values that are non-negative integers in units of (km/h). Map values represent consumption values that are non-negative floating point values in units of (Wh/m). The function is linearly interpolated between each successive pair of data points: For values below the first list value, the first value is used. For values after the last list value, the last list value is used. At minimum, one key/value pair must be set. In this case the consumption value is used for all possible speed keys.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-evconsumptionmodel-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-evconsumptionmodel-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-evconsumptionmodel-trafficspeedtable">trafficSpeedTable</a></span> <span class="signature">↔ Map<span class="signature">\<<wbr></wbr><span class="type-parameter">int</span>, <span class="type-parameter">double</span>\></span></span>  
Traffic speed table describes energy consumption when traveling under heavy traffic conditions, i.e. when the vehicle is expected to often change the travel speed. It defines a function curve specifying consumption rate at a given speed under traffic conditions on a flat stretch of road. Map keys represent traffic speed values that are non-negative integers in units of (km/h). Map values represent consumption values that are non-negative floating point values in units of (Wh/m). The function is linearly interpolated between each successive pair of data points: For values below the first list value, the first value is used. For values after the last list value, the last list value is used. If only one key/value pair is set, the consumption value is used for all possible traffic speed keys. If <a href="sdk-for-flutter-explore-routing-evconsumptionmodel-trafficspeedtable">EVConsumptionModel.trafficSpeedTable</a> is empty then only <a href="sdk-for-flutter-explore-routing-evconsumptionmodel-freeflowspeedtable">EVConsumptionModel.freeFlowSpeedTable</a> is used for calculating speed-related energy consumption.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-routing-evconsumptionmodel-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-evconsumptionmodel-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-routing-evconsumptionmodel-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

