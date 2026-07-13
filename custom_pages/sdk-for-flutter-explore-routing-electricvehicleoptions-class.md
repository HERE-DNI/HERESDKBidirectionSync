---
title: "ElectricVehicleOptions class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-electricvehicleoptions-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ElectricVehicleOptions-class.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/ElectricVehicleOptions-class-sidebar.html">

<div>

# <span class="kind-class">ElectricVehicleOptions</span> class

</div>

<div class="section desc markdown">

These options define the parameters of the electric vehicle.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-routing-electricvehicleoptions-electricvehicleoptions">ElectricVehicleOptions</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-explore-routing-electricvehicleoptions-batteryspecifications">batterySpecifications</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-routing-batteryspecifications-class">BatterySpecifications</a>?</span>  
Parameters that describe the electric vehicle's battery. By default, it is set to `null`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-electricvehicleoptions-empiricalconsumptionmodel">empiricalConsumptionModel</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-routing-empiricalconsumptionmodel-class">EmpiricalConsumptionModel</a>?</span>  
Defines the empirical consumption model. The model is used to calculate the energy consumption for the vehicle on a given route. **Note** Only one consumption model is supported per route.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-electricvehicleoptions-ensurereachability">ensureReachability</a></span> <span class="signature">↔ bool</span>  
Ensure that the vehicle does not run out of energy along the way. Requires valid `battery_specifications`. It also requires that <a href="sdk-for-flutter-explore-routing-routeoptions-optimizationmode">RouteOptions.optimizationMode</a> = <a href="sdk-for-flutter-explore-routing-optimizationmode">OptimizationMode.fastest</a>, <a href="sdk-for-flutter-explore-routing-routeoptions-speedcapinmeterspersecond">RouteOptions.speedCapInMetersPerSecond</a> is not set, and <a href="sdk-for-flutter-explore-routing-avoidanceoptions-class">AvoidanceOptions</a> is empty. Otherwise, this object is considered invalid. Setting this flag enables calculation of a route optimized for electric vehicles. Charging stations may be added along the route to ensure that the vehicle does not run out of energy along the way. It is especially useful for longer routes, because after all, charging stations are much less common than petrol stations.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-electricvehicleoptions-evmobilityserviceproviderpreferences">evMobilityServiceProviderPreferences</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-routing-evmobilityserviceproviderpreferences-class">EVMobilityServiceProviderPreferences</a></span>  
Defines the preferred E-Mobility Service Providers. The The E-Mobility Service Provider Partner Ids can be received from <https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-roamings.html> An alternative way to get `partnerId` is the `eMobilityServiceProviders.partnerId` as part of `HERE SDK Search`. Maximum number of E-Mobility Service Providers is limited to 10. By default, all providers are used. **Note** Not yet supported for offline routing.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-electricvehicleoptions-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-electricvehicleoptions-physicalconsumptionmodel">physicalConsumptionModel</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-routing-physicalconsumptionmodel-class">PhysicalConsumptionModel</a>?</span>  
Defines the physical consumption model. The model is used to calculate the energy consumption for the vehicle on a given route. **Note** Only one consumption model is supported per route.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-electricvehicleoptions-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-routing-electricvehicleoptions-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-electricvehicleoptions-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-routing-electricvehicleoptions-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
