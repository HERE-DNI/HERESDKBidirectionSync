---
title: "RoutingOptions class"
slug: "sdk-for-flutter-explore-routing-routingoptions-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RoutingOptions-class.html -->


<div>
<h1>RoutingOptions class</h1></div>

<p>The options defines how a route should be calculated.</p>
<p>The options are used for all transport modes and engines.</p>
<p>** Electric vehicle specific requirements **
Electric vehicle consumption are estimated when at least one consumption model is defined.
Currently two models are supported:</p>
<ul>
<li>PhysicalConsumptionModel
Aside from the values in PhysicalConsumptionModel additionally these values needs to be defined:
<ul>
<li><a href="/sdk-for-flutter-explore-transport-vehiclespecification-currentweightinkilograms">VehicleSpecification.currentWeightInKilograms</a> from <a href="/sdk-for-flutter-explore-transport-transportspecification-vehiclespecification">TransportSpecification.vehicleSpecification</a>
from <a href="/sdk-for-flutter-explore-routing-routingoptions-transportspecification">RoutingOptions.transportSpecification</a></li>
<li>Additionally <a href="/sdk-for-flutter-explore-routing-waypoint-currentweightchangeinkilograms">Waypoint.currentWeightChangeInKilograms</a> can be defined.</li>
</ul>
</li>
<li>EmpiricalConsumptionModel</li>
</ul>
<p>By setting <a href="/sdk-for-flutter-explore-routing-electricvehicleoptions-ensurereachability">ElectricVehicleOptions.ensureReachability</a> the <code>RoutingEngine</code> inserts additional charging stations
to reach the waypoints.
This feature requires setting the <a href="/sdk-for-flutter-explore-routing-batteryspecifications-class">BatterySpecifications</a>.
By default a vehicle might not reach the waypoint, when the initial charge is not enough to reach all waypoints.
See the parameter description below for more details.</p>


<h2>Constructors</h2>
<ul><li><a href="/sdk-for-flutter-explore-routing-routingoptions-routingoptions">RoutingOptions</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="/sdk-for-flutter-explore-routing-routingoptions-allowoptions">allowOptions</a></li><li><a href="/sdk-for-flutter-explore-routing-routingoptions-avoidanceoptions">avoidanceOptions</a></li><li><a href="/sdk-for-flutter-explore-routing-routingoptions-evoptions">evOptions</a></li><li><a href="/sdk-for-flutter-explore-routing-routingoptions-hashcode">hashCode</a></li><li><a href="/sdk-for-flutter-explore-routing-routingoptions-maxspeedonsegments">maxSpeedOnSegments</a></li><li><a href="/sdk-for-flutter-explore-routing-routingoptions-routeoptions">routeOptions</a></li><li><a href="/sdk-for-flutter-explore-routing-routingoptions-runtimetype">runtimeType</a></li><li><a href="/sdk-for-flutter-explore-routing-routingoptions-textoptions">textOptions</a></li><li><a href="/sdk-for-flutter-explore-routing-routingoptions-tolloptions">tollOptions</a></li><li><a href="/sdk-for-flutter-explore-routing-routingoptions-transportspecification">transportSpecification</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="/sdk-for-flutter-explore-routing-routingoptions-nosuchmethod">noSuchMethod</a></li><li><a href="/sdk-for-flutter-explore-routing-routingoptions-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="/sdk-for-flutter-explore-routing-routingoptions-operator-equals">operator ==</a></li></ul>


<h2>Static Methods</h2>
<ul><li><a href="/sdk-for-flutter-explore-routing-routingoptions-fromdefaultparameterconfiguration">fromDefaultParameterConfiguration</a></li></ul>

 



</div>
`
}</HTMLBlock>
