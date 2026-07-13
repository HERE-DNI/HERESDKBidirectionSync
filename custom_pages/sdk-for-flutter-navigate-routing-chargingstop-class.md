---
title: "ChargingStop class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-chargingstop-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ChargingStop-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/ChargingStop-class-sidebar.html">

<div>

# <span class="kind-class">ChargingStop</span> class

</div>

<div class="section desc markdown">

The options to specify a user-planned charging stop.

**Note:** In order to specify this <a href="sdk-for-flutter-navigate-routing-chargingstop-class">ChargingStop</a>, it is also required to set `sdk.routing.BatterySpecifications.total_capacity_in_kilowatt_hours`, `sdk.routing.BatterySpecifications.initial_charge_in_kilowatt_hours`, and <a href="sdk-for-flutter-navigate-routing-batteryspecifications-chargingcurve">BatterySpecifications.chargingCurve</a>. Without all of them, the route calculation will fail as an invalid parameter error.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-routing-chargingstop-chargingstop">ChargingStop</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-powerInKilowatts" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">powerInKilowatts</span>, </span><span id="sdk-for-flutter-navigate-param-currentInAmperes" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">currentInAmperes</span>, </span><span id="sdk-for-flutter-navigate-param-voltageInVolts" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">voltageInVolts</span>, </span><span id="sdk-for-flutter-navigate-param-supplyType" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-chargingsupplytype">ChargingSupplyType</a>?</span> <span class="parameter-name">supplyType</span>, </span><span id="sdk-for-flutter-navigate-param-minDuration" class="parameter"><span class="type-annotation">Duration?</span> <span class="parameter-name">minDuration</span>, </span><span id="sdk-for-flutter-navigate-param-maxDuration" class="parameter"><span class="type-annotation">Duration?</span> <span class="parameter-name">maxDuration</span></span>)</span>  
Creates a new instance.

<span class="name"><a href="sdk-for-flutter-navigate-routing-chargingstop-chargingstop-withdefaults">ChargingStop.withDefaults</a></span><span class="signature">()</span>  
Creates a new instance.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-routing-chargingstop-currentinamperes">currentInAmperes</a></span> <span class="signature">↔ double</span>  
The value of rated current of the connector (in A).

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-chargingstop-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-chargingstop-maxduration">maxDuration</a></span> <span class="signature">↔ Duration?</span>  
The maximum duration the user plans to charge at the station, including <a href="sdk-for-flutter-navigate-routing-batteryspecifications-chargingsetupduration">BatterySpecifications.chargingSetupDuration</a>. **Note:** At least one of `min_duration` and `max_duration` is required for a user-planned charging stop. For most use cases, providing at least `min_duration` is recommended.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-chargingstop-minduration">minDuration</a></span> <span class="signature">↔ Duration?</span>  
The minimum duration the user expects to charge at the station, including <a href="sdk-for-flutter-navigate-routing-batteryspecifications-chargingsetupduration">BatterySpecifications.chargingSetupDuration</a>. **Note:** At least one of `min_duration` and `max_duration` is required for a user-planned charging stop. For most use cases, providing at least `min_duration` is recommended.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-chargingstop-powerinkilowatts">powerInKilowatts</a></span> <span class="signature">↔ double</span>  
The value of rated power of the connector (in kW).

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-chargingstop-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-chargingstop-supplytype">supplyType</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-routing-chargingsupplytype">ChargingSupplyType</a>?</span>  
Supply type of the suggested connector.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-chargingstop-voltageinvolts">voltageInVolts</a></span> <span class="signature">↔ double</span>  
The value of rated voltage of the connector (in V).

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-routing-chargingstop-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-chargingstop-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-routing-chargingstop-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
