---
title: "RoutingOptions class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-routingoptions-class"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/RoutingOptions-class-sidebar.html">

<div>

# <span class="kind-class">RoutingOptions</span> class

</div>

<div class="section desc markdown">

The options defines how a route should be calculated.

The options are used for all transport modes and engines.

\*\* Electric vehicle specific requirements \*\* Electric vehicle consumption are estimated when at least one consumption model is defined. Currently two models are supported:

- PhysicalConsumptionModel Aside from the values in PhysicalConsumptionModel additionally these values needs to be defined:
  - <a href="sdk-for-flutter-explore-transport-vehiclespecification-currentweightinkilograms">VehicleSpecification.currentWeightInKilograms</a> from <a href="sdk-for-flutter-explore-transport-transportspecification-vehiclespecification">TransportSpecification.vehicleSpecification</a> from <a href="sdk-for-flutter-explore-routing-routingoptions-transportspecification">RoutingOptions.transportSpecification</a>
  - Additionally <a href="sdk-for-flutter-explore-routing-waypoint-currentweightchangeinkilograms">Waypoint.currentWeightChangeInKilograms</a> can be defined.
- EmpiricalConsumptionModel

By setting <a href="sdk-for-flutter-explore-routing-electricvehicleoptions-ensurereachability">ElectricVehicleOptions.ensureReachability</a> the `RoutingEngine` inserts additional charging stations to reach the waypoints. This feature requires setting the <a href="sdk-for-flutter-explore-routing-batteryspecifications-class">BatterySpecifications</a>. By default a vehicle might not reach the waypoint, when the initial charge is not enough to reach all waypoints. See the parameter description below for more details.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-routing-routingoptions-routingoptions">RoutingOptions</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-explore-routing-routingoptions-allowoptions">allowOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-routing-allowoptions-class">AllowOptions</a></span>  
The options explicitly allowed by user for route calculations. By default no options are opt in.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-routingoptions-avoidanceoptions">avoidanceOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-routing-avoidanceoptions-class">AvoidanceOptions</a></span>  
Options to specify restrictions for route calculations. By default no restrictions are applied.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-routingoptions-evoptions">evOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-routing-electricvehicleoptions-class">ElectricVehicleOptions</a>?</span>  
Defines the electric vehicle (EV) related parameters to calculate the consumption and reachability. When no EV options are defined an internal combustion engine is assumed.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-routingoptions-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-routingoptions-maxspeedonsegments">maxSpeedOnSegments</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-routing-maxspeedonsegment-class">MaxSpeedOnSegment</a></span>\></span></span>  
Segments with restriction on maximum <a href="sdk-for-flutter-explore-routing-dynamicspeedinfo-basespeedinmeterspersecond">DynamicSpeedInfo.baseSpeedInMetersPerSecond</a>. **Note** Not used for offline calculations.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-routingoptions-routeoptions">routeOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-routing-routeoptions-class">RouteOptions</a></span>  
Specifies the common route calculation options.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-routingoptions-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-routingoptions-textoptions">textOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-routing-routetextoptions-class">RouteTextOptions</a></span>  
Customize textual content returned from the route calculation, such as localization, format, and unit system.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-routingoptions-tolloptions">tollOptions</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-routing-tolloptions-class">TollOptions</a></span>  
Options to specify how the tolls should be calculated, such as transponders, vehicle category, and emission type. **Note** Not used for offline calculations.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-routingoptions-transportspecification">transportSpecification</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-transport-transportspecification-class">TransportSpecification</a></span>  
Defines the transport specification which contains the transport mode and the vehicle specifications for the transport mode chosen. **Notes:**

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-routing-routingoptions-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-routingoptions-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-routing-routingoptions-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

## Static Methods

<span class="name"><a href="sdk-for-flutter-explore-routing-routingoptions-fromdefaultparameterconfiguration">fromDefaultParameterConfiguration</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-routing-routingoptions-class">RoutingOptions</a></span> </span>  
Returns the default configuration for the transport specification selected in <a href="sdk-for-flutter-explore-core-parameterconfiguration-transportspecification">ParameterConfiguration.transportSpecification</a> from <a href="sdk-for-flutter-explore-core-engine-sdknativeengine-parameterconfig">SDKNativeEngine.parameterConfig</a>.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

