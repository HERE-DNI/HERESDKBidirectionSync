---
title: "calculateTrafficOnRouteWithCurrentCharge abstract method"
slug: "sdk-for-flutter-explore-routing-routingengine-calculatetrafficonroutewithcurrentcharge"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- calculateTrafficOnRouteWithCurrentCharge.html -->


<div>
<h1>calculateTrafficOnRouteWithCurrentCharge abstract method</h1></div>

<a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>
calculateTrafficOnRouteWithCurrentCharge(<ol class="parameter-list"> <li><a href="sdk-for-flutter-explore-routing-route-class">Route</a> route, </li>
<li>int lastTraveledSectionIndex, </li>
<li>int traveledDistanceOnLastSectionInMeters, </li>
<li>double currentChargeInKilowattHours, </li>
<li><a href="sdk-for-flutter-explore-routing-calculatetrafficonroutecallback">CalculateTrafficOnRouteCallback</a> callback, </li>
</ol>)

      

    

<p>Asynchronously calculates the traffic along an EV car route starting from the index of the
last traveled route section and an offset in meters from the last visited position on the
section.</p>
<p>The field <a href="sdk-for-flutter-explore-routing-trafficonspan-consumptioninkilowatthours">TrafficOnSpan.consumptionInKilowattHours</a> will contain the power consumption
in kilowatt-hours (kWh) necessary to traverse the span, and
<a href="sdk-for-flutter-explore-routing-routeplace-chargeinkilowatthours">RoutePlace.chargeInKilowattHours</a>, inside <a href="sdk-for-flutter-explore-routing-trafficonsection-departureplace">TrafficOnSection.departurePlace</a> and
<a href="sdk-for-flutter-explore-routing-trafficonsection-arrivalplace">TrafficOnSection.arrivalPlace</a>, the estimated battery charge in kilowatt-hours (kWh) when
leaving/arriving to a section.
<strong>Note:</strong> Only EV cars are supported.</p>
<ul>
<li>
<p><code>route</code> A <a href="sdk-for-flutter-explore-routing-route-class">Route</a> calculated using the online routing engine. Its
<a href="sdk-for-flutter-explore-routing-routehandle-class">RouteHandle</a> and the original route calculation options, along with EV
related information like <a href="sdk-for-flutter-explore-routing-batteryspecifications-class">BatterySpecifications</a>, will be used to
compute the traffic on the route. The original route remains untouched.</p>
</li>
<li>
<p><code>lastTraveledSectionIndex</code> Indicates the index of the last traveled route section. Traveled part of the route won't
be reused.</p>
</li>
<li>
<p><code>traveledDistanceOnLastSectionInMeters</code> Offset, in meters, to the last visited position on the route section defined by the last
traveled section index.</p>
</li>
<li>
<p><code>currentChargeInKilowattHours</code> Charge level of the vehicle's battery at the current location (in kWh).
It must be non-negative and less than or equal to the value of
<a href="sdk-for-flutter-explore-routing-batteryspecifications-totalcapacityinkilowatthours">BatterySpecifications.totalCapacityInKilowattHours</a>,
otherwise the <a href="sdk-for-flutter-explore-routing-batteryspecifications-class">BatterySpecifications</a> instance is considered invalid.
Sets <a href="sdk-for-flutter-explore-routing-batteryspecifications-initialchargeinkilowatthours">BatterySpecifications.initialChargeInKilowattHours</a> to the given value.</p>
</li>
<li>
<p><code>callback</code> Callback object that will be invoked after route traffic has been calculated.
It is always invoked on the main thread.</p>
</li>
</ul>
<p>Returns <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle calculateTrafficOnRouteWithCurrentCharge(Route route, int lastTraveledSectionIndex, int traveledDistanceOnLastSectionInMeters, double currentChargeInKilowattHours, CalculateTrafficOnRouteCallback callback);</code></pre>

 



</div>
`
}</HTMLBlock>
