---
title: "weightPerAxleInKilograms property"
slug: "sdk-for-flutter-explore-transport-vehiclespecification-weightperaxleinkilograms"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- weightPerAxleInKilograms.html -->


<div>
<h1>weightPerAxleInKilograms property</h1></div>

        
        int?
        weightPerAxleInKilograms
<div class="features">getter/setter pair</div>


<p>Heaviest weight per axle, regardless of axle type or axle group.
It is evaluated against all axle weight restrictions, including single axle and tandem axle weight restrictions.
The provided value must be greater or equal to 0.
By default, it is not set.</p>
<p><strong>Notes:</strong></p>
<ul>
<li><a href="/sdk-for-flutter-explore-transport-vehiclespecification-weightperaxleinkilograms">VehicleSpecification.weightPerAxleInKilograms</a> and <a href="/sdk-for-flutter-explore-transport-vehiclespecification-weightperaxlegroup">VehicleSpecification.weightPerAxleGroup</a> are incompatible.
When available for your edition, if both attributes are set, during online <code>RoutingEngine</code> an <code>RoutingError.INVALID_PARAMETER</code>
error is generated. Otherwise, when offline <code>RoutingEngine</code> is in place, both parameters are evaluated and the
maximum value between them will be used.</li>
<li>Supported in <a href="/sdk-for-flutter-explore-transport-transportmode">TransportMode.truck</a>, <a href="/sdk-for-flutter-explore-transport-transportmode">TransportMode.bus</a>, <a href="/sdk-for-flutter-explore-transport-transportmode">TransportMode.privateBus</a>,
<a href="/sdk-for-flutter-explore-transport-transportmode">TransportMode.car</a> (Beta), <a href="/sdk-for-flutter-explore-transport-transportmode">TransportMode.taxi</a> (Beta) transport modes.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">int? weightPerAxleInKilograms;</code></pre>

 



</div>
`
}</HTMLBlock>
