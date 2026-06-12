---
title: "axleCount property"
slug: "sdk-for-flutter-explore-transport-vehiclespecification-axlecount"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- axleCount.html -->


<div>
<h1>axleCount property</h1></div>

        
        int?
        axleCount
<div class="features">getter/setter pair</div>


<p>Defines total number of axles in the vehicle. The provided value must be greater than or equal to 2.
By default, it is not set.
Route calculation: When not set, possible axle count restrictions will not be taken into consideration.
Rendering: When set, truck restriction icons for an axle count greater than <a href="/sdk-for-flutter-explore-transport-vehiclespecification-axlecount">VehicleSpecification.axleCount</a> will not be displayed.
When specifying <a href="/sdk-for-flutter-explore-transport-vehiclespecification-traileraxlecount">VehicleSpecification.trailerAxleCount</a>, then <a href="/sdk-for-flutter-explore-transport-vehiclespecification-axlecount">VehicleSpecification.axleCount</a> is required and must be greater than <a href="/sdk-for-flutter-explore-transport-vehiclespecification-traileraxlecount">VehicleSpecification.trailerAxleCount</a>.</p>
<p><strong>Note:</strong> Supported in <a href="/sdk-for-flutter-explore-transport-transportmode">TransportMode.truck</a>, <a href="/sdk-for-flutter-explore-transport-transportmode">TransportMode.bus</a>, <a href="/sdk-for-flutter-explore-transport-transportmode">TransportMode.privateBus</a>,
<a href="/sdk-for-flutter-explore-transport-transportmode">TransportMode.car</a> (Beta), <a href="/sdk-for-flutter-explore-transport-transportmode">TransportMode.taxi</a> (Beta) transport modes.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">int? axleCount;</code></pre>

 



</div>
`
}</HTMLBlock>
