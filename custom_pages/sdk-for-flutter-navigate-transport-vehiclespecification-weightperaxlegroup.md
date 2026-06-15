---
title: "weightPerAxleGroup property"
slug: "sdk-for-flutter-navigate-transport-vehiclespecification-weightperaxlegroup"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- weightPerAxleGroup.html -->


<div>
<h1>weightPerAxleGroup property</h1></div>

<a href="sdk-for-flutter-navigate-transport-weightperaxlegroup-class">WeightPerAxleGroup</a>?
        weightPerAxleGroup
<div class="features">getter/setter pair</div>


<p>Allows specification of axle weights in a more fine-grained way than <a href="sdk-for-flutter-navigate-transport-vehiclespecification-weightperaxleinkilograms">VehicleSpecification.weightPerAxleInKilograms</a>.
This is relevant in countries with signs and regulations that specify different limits for different axle
groups, like the USA and Sweden.
By default is not set.</p>
<p><strong>Notes:</strong></p>
<ul>
<li><a href="sdk-for-flutter-navigate-transport-vehiclespecification-weightperaxleinkilograms">VehicleSpecification.weightPerAxleInKilograms</a> and <a href="sdk-for-flutter-navigate-transport-vehiclespecification-weightperaxlegroup">VehicleSpecification.weightPerAxleGroup</a> are incompatible.
When available for your edition, if both attributes are set, during online <code>RoutingEngine</code> an <code>RoutingError.INVALID_PARAMETER</code>
error is generated. Otherwise, when offline <code>RoutingEngine</code> is in place, both parameters are evaluated and
the maximum value between them will be used.</li>
<li>Supported in <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.truck</a>, <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.bus</a>, <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.privateBus</a>,
<a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.car</a> (Beta), <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.taxi</a> (Beta) transport modes.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">WeightPerAxleGroup? weightPerAxleGroup;</code></pre>

 



</div>
`
}</HTMLBlock>
