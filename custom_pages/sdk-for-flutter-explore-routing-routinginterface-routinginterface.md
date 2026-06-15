---
title: "RoutingInterface constructor"
slug: "sdk-for-flutter-explore-routing-routinginterface-routinginterface"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RoutingInterface.html -->


<div>
<h1>RoutingInterface constructor</h1></div>

RoutingInterface(<ol class="parameter-list"> <li><a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a> calculateRouteWithRoutingOptionsLambda(<ol class="parameter-list single-line"> <li>List&lt;<a href="sdk-for-flutter-explore-routing-waypoint-class">Waypoint</a>&gt;, </li>
<li><a href="sdk-for-flutter-explore-routing-routingoptions-class">RoutingOptions</a>, </li>
<li><a href="sdk-for-flutter-explore-routing-calculateroutecallback">CalculateRouteCallback</a> </li>
</ol>), </li>
<li><a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a> calculateCarRouteLambda(<ol class="parameter-list single-line"> <li>List&lt;<a href="sdk-for-flutter-explore-routing-waypoint-class">Waypoint</a>&gt;, </li>
<li><a class="deprecated" href="sdk-for-flutter-explore-routing-caroptions-class">CarOptions</a>, </li>
<li><a href="sdk-for-flutter-explore-routing-calculateroutecallback">CalculateRouteCallback</a> </li>
</ol>), </li>
<li><a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a> calculatePedestrianRouteLambda(<ol class="parameter-list single-line"> <li>List&lt;<a href="sdk-for-flutter-explore-routing-waypoint-class">Waypoint</a>&gt;, </li>
<li><a class="deprecated" href="sdk-for-flutter-explore-routing-pedestrianoptions-class">PedestrianOptions</a>, </li>
<li><a href="sdk-for-flutter-explore-routing-calculateroutecallback">CalculateRouteCallback</a> </li>
</ol>), </li>
<li><a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a> calculateTruckRouteLambda(<ol class="parameter-list single-line"> <li>List&lt;<a href="sdk-for-flutter-explore-routing-waypoint-class">Waypoint</a>&gt;, </li>
<li><a class="deprecated" href="sdk-for-flutter-explore-routing-truckoptions-class">TruckOptions</a>, </li>
<li><a href="sdk-for-flutter-explore-routing-calculateroutecallback">CalculateRouteCallback</a> </li>
</ol>), </li>
<li><a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a> calculateScooterRouteLambda(<ol class="parameter-list single-line"> <li>List&lt;<a href="sdk-for-flutter-explore-routing-waypoint-class">Waypoint</a>&gt;, </li>
<li><a class="deprecated" href="sdk-for-flutter-explore-routing-scooteroptions-class">ScooterOptions</a>, </li>
<li><a href="sdk-for-flutter-explore-routing-calculateroutecallback">CalculateRouteCallback</a> </li>
</ol>), </li>
<li><a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a> calculateBicycleRouteLambda(<ol class="parameter-list single-line"> <li>List&lt;<a href="sdk-for-flutter-explore-routing-waypoint-class">Waypoint</a>&gt;, </li>
<li><a class="deprecated" href="sdk-for-flutter-explore-routing-bicycleoptions-class">BicycleOptions</a>, </li>
<li><a href="sdk-for-flutter-explore-routing-calculateroutecallback">CalculateRouteCallback</a> </li>
</ol>), </li>
<li><a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a> calculateTaxiRouteLambda(<ol class="parameter-list single-line"> <li>List&lt;<a href="sdk-for-flutter-explore-routing-waypoint-class">Waypoint</a>&gt;, </li>
<li><a class="deprecated" href="sdk-for-flutter-explore-routing-taxioptions-class">TaxiOptions</a>, </li>
<li><a href="sdk-for-flutter-explore-routing-calculateroutecallback">CalculateRouteCallback</a> </li>
</ol>), </li>
<li><a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a> calculateEVCarRouteLambda(<ol class="parameter-list single-line"> <li>List&lt;<a href="sdk-for-flutter-explore-routing-waypoint-class">Waypoint</a>&gt;, </li>
<li><a class="deprecated" href="sdk-for-flutter-explore-routing-evcaroptions-class">EVCarOptions</a>, </li>
<li><a href="sdk-for-flutter-explore-routing-calculateroutecallback">CalculateRouteCallback</a> </li>
</ol>), </li>
<li><a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a> calculateEVTruckRouteLambda(<ol class="parameter-list single-line"> <li>List&lt;<a href="sdk-for-flutter-explore-routing-waypoint-class">Waypoint</a>&gt;, </li>
<li><a class="deprecated" href="sdk-for-flutter-explore-routing-evtruckoptions-class">EVTruckOptions</a>, </li>
<li><a href="sdk-for-flutter-explore-routing-calculateroutecallback">CalculateRouteCallback</a> </li>
</ol>), </li>
<li><a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a> calculateBusRouteLambda(<ol class="parameter-list single-line"> <li>List&lt;<a href="sdk-for-flutter-explore-routing-waypoint-class">Waypoint</a>&gt;, </li>
<li><a class="deprecated" href="sdk-for-flutter-explore-routing-busoptions-class">BusOptions</a>, </li>
<li><a href="sdk-for-flutter-explore-routing-calculateroutecallback">CalculateRouteCallback</a> </li>
</ol>), </li>
<li><a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a> calculatePrivateBusRouteLambda(<ol class="parameter-list single-line"> <li>List&lt;<a href="sdk-for-flutter-explore-routing-waypoint-class">Waypoint</a>&gt;, </li>
<li><a class="deprecated" href="sdk-for-flutter-explore-routing-privatebusoptions-class">PrivateBusOptions</a>, </li>
<li><a href="sdk-for-flutter-explore-routing-calculateroutecallback">CalculateRouteCallback</a> </li>
</ol>), </li>
<li><a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a> returnToRouteWithTraveledDistanceLambda(<ol class="parameter-list"> <li><a href="sdk-for-flutter-explore-routing-route-class">Route</a>, </li>
<li><a href="sdk-for-flutter-explore-routing-waypoint-class">Waypoint</a>, </li>
<li>int, </li>
<li>int, </li>
<li><a href="sdk-for-flutter-explore-routing-calculateroutecallback">CalculateRouteCallback</a> , </li>
</ol>), </li>
</ol>)
    

<p>Provides the abstract class for the online and offline
routing engines.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory RoutingInterface(
  TaskHandle Function(List&lt;Waypoint&gt;, RoutingOptions, CalculateRouteCallback) calculateRouteWithRoutingOptionsLambda,
  TaskHandle Function(List&lt;Waypoint&gt;, CarOptions, CalculateRouteCallback) calculateCarRouteLambda,
  TaskHandle Function(List&lt;Waypoint&gt;, PedestrianOptions, CalculateRouteCallback) calculatePedestrianRouteLambda,
  TaskHandle Function(List&lt;Waypoint&gt;, TruckOptions, CalculateRouteCallback) calculateTruckRouteLambda,
  TaskHandle Function(List&lt;Waypoint&gt;, ScooterOptions, CalculateRouteCallback) calculateScooterRouteLambda,
  TaskHandle Function(List&lt;Waypoint&gt;, BicycleOptions, CalculateRouteCallback) calculateBicycleRouteLambda,
  TaskHandle Function(List&lt;Waypoint&gt;, TaxiOptions, CalculateRouteCallback) calculateTaxiRouteLambda,
  TaskHandle Function(List&lt;Waypoint&gt;, EVCarOptions, CalculateRouteCallback) calculateEVCarRouteLambda,
  TaskHandle Function(List&lt;Waypoint&gt;, EVTruckOptions, CalculateRouteCallback) calculateEVTruckRouteLambda,
  TaskHandle Function(List&lt;Waypoint&gt;, BusOptions, CalculateRouteCallback) calculateBusRouteLambda,
  TaskHandle Function(List&lt;Waypoint&gt;, PrivateBusOptions, CalculateRouteCallback) calculatePrivateBusRouteLambda,
  TaskHandle Function(Route, Waypoint, int, int, CalculateRouteCallback) returnToRouteWithTraveledDistanceLambda,

) =&gt; RoutingInterface$Lambdas(
  calculateRouteWithRoutingOptionsLambda,
  calculateCarRouteLambda,
  calculatePedestrianRouteLambda,
  calculateTruckRouteLambda,
  calculateScooterRouteLambda,
  calculateBicycleRouteLambda,
  calculateTaxiRouteLambda,
  calculateEVCarRouteLambda,
  calculateEVTruckRouteLambda,
  calculateBusRouteLambda,
  calculatePrivateBusRouteLambda,
  returnToRouteWithTraveledDistanceLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
