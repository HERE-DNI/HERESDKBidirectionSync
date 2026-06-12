---
title: "transportSpecification property"
slug: "sdk-for-flutter-navigate-routing-routingoptions-transportspecification"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- transportSpecification.html -->


<div>
<h1>transportSpecification property</h1></div>

<a href="/sdk-for-flutter-navigate-transport-transportspecification-class">TransportSpecification</a>
transportSpecification
<div class="features">getter/setter pair</div>


<p>Defines the transport specification which contains the transport mode and the vehicle specifications
for the transport mode chosen.
<strong>Notes:</strong></p>
<ul>
<li>The transport mode <a href="/sdk-for-flutter-navigate-transport-transportmode">TransportMode.publicTransit</a> is not supported.</li>
<li>By default all vehicle specifications from <a href="/sdk-for-flutter-navigate-routing-routingoptions-transportspecification">RoutingOptions.transportSpecification</a> are set to <code>null</code> and the
<a href="/sdk-for-flutter-navigate-transport-transportspecification-transportmode">TransportSpecification.transportMode</a> from <a href="/sdk-for-flutter-navigate-routing-routingoptions-transportspecification">RoutingOptions.transportSpecification</a> is set to <a href="/sdk-for-flutter-navigate-transport-transportmode">TransportMode.car</a>.</li>
<li>A route can be calculated with only the <a href="/sdk-for-flutter-navigate-transport-transportspecification-transportmode">TransportSpecification.transportMode</a> from <a href="/sdk-for-flutter-navigate-routing-routingoptions-transportspecification">RoutingOptions.transportSpecification</a> set.</li>
<li>It is highly recommended to define the <a href="/sdk-for-flutter-navigate-transport-truckcategory">TruckCategory</a> that is being used in <a href="/sdk-for-flutter-navigate-transport-vehiclespecification-truckcategory">VehicleSpecification.truckCategory</a> from
<a href="/sdk-for-flutter-navigate-transport-transportspecification-vehiclespecification">TransportSpecification.vehicleSpecification</a> from <a href="/sdk-for-flutter-navigate-routing-routingoptions-transportspecification">RoutingOptions.transportSpecification</a>, if the
<a href="/sdk-for-flutter-navigate-transport-transportspecification-transportmode">TransportSpecification.transportMode</a> from <a href="/sdk-for-flutter-navigate-routing-routingoptions-transportspecification">RoutingOptions.transportSpecification</a> is set to <a href="/sdk-for-flutter-navigate-transport-transportmode">TransportMode.truck</a>.</li>
<li>The <a href="/sdk-for-flutter-navigate-transport-vehiclespecification-occupancy">VehicleSpecification.occupancy</a> from <a href="/sdk-for-flutter-navigate-transport-transportspecification-vehiclespecification">TransportSpecification.vehicleSpecification</a> won't have effect
if HOV and/or HOT lane usage is not allowed using <a href="/sdk-for-flutter-navigate-routing-evtruckoptions-allowoptions">EVTruckOptions.allowOptions</a>.</li>
<li>The <a href="/sdk-for-flutter-navigate-transport-pedestrianspecification-walkingspeedinmeterspersecond">PedestrianSpecification.walkingSpeedInMetersPerSecond</a> from <a href="/sdk-for-flutter-navigate-transport-transportspecification-pedestrianspecification">TransportSpecification.pedestrianSpecification</a>
if present, will be used by the service as the walking speed for pedestrian routing. It influences the duration of walking
along the route. The provided value must be in the range [0.5, 2.0]. When the value is outside this
range, an invalid parameter error is raised. Refer to <a href="/sdk-for-flutter-navigate-routing-routingerror">RoutingError</a> for details. The
default speed is 1 meter per second.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TransportSpecification transportSpecification;</code></pre>

 



</div>
`
}</HTMLBlock>
