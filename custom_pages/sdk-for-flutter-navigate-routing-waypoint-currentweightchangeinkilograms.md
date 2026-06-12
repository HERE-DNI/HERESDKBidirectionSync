---
title: "currentWeightChangeInKilograms property"
slug: "sdk-for-flutter-navigate-routing-waypoint-currentweightchangeinkilograms"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- currentWeightChangeInKilograms.html -->


<div>
<h1>currentWeightChangeInKilograms property</h1></div>

        
        int?
        currentWeightChangeInKilograms
<div class="features">getter/setter pair</div>


<p>Changes the value of <code>vehicle[currentWeight]</code> by this value.
Enables the support of scenarios where the vehicle takes additional cargo or unloads its cargo along the route.
Changes to the configuration of the vehicle, such as adding a trailer, aren't supported.
Relative value in kilograms. Available range: from -40000 to 40000 (inclusive).
<strong>Note:</strong></p>
<ul>
<li>A route request with this parameter requires to set <a href="/sdk-for-flutter-navigate-transport-vehiclespecification-currentweightinkilograms">VehicleSpecification.currentWeightInKilograms</a> and
<a href="/sdk-for-flutter-navigate-transport-vehiclespecification-grossweightinkilograms">VehicleSpecification.grossWeightInKilograms</a>.</li>
<li>This feature is supported in transport modes of <a href="/sdk-for-flutter-navigate-transport-transportmode">TransportMode.car</a>, <a href="/sdk-for-flutter-navigate-transport-transportmode">TransportMode.taxi</a>, or
<a href="/sdk-for-flutter-navigate-transport-transportmode">TransportMode.truck</a>.</li>
</ul>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">int? currentWeightChangeInKilograms;</code></pre>

 



</div>
`
}</HTMLBlock>
