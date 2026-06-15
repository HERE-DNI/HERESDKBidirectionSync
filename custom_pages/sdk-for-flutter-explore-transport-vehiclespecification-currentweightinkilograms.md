---
title: "currentWeightInKilograms property"
slug: "sdk-for-flutter-explore-transport-vehiclespecification-currentweightinkilograms"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- currentWeightInKilograms.html -->


<div>
<h1>currentWeightInKilograms property</h1></div>

        
        int?
        currentWeightInKilograms
<div class="features">getter/setter pair</div>


<p>Current truck weight, including trailers and shipped goods currently loaded, specified in
kilograms. The provided value must be greater than or equal to 0. If unspecified,
it will default to <a href="sdk-for-flutter-explore-transport-vehiclespecification-grossweightinkilograms">VehicleSpecification.grossWeightInKilograms</a>.
By default, it is not set.</p>
<p><strong>Notes:</strong></p>
<ul>
<li>Supported in <a href="sdk-for-flutter-explore-transport-transportmode">TransportMode.truck</a>, <a href="sdk-for-flutter-explore-transport-transportmode">TransportMode.bus</a>, <a href="sdk-for-flutter-explore-transport-transportmode">TransportMode.privateBus</a>,
<a href="sdk-for-flutter-explore-transport-transportmode">TransportMode.car</a> (Beta), <a href="sdk-for-flutter-explore-transport-transportmode">TransportMode.taxi</a> (Beta) transport modes.</li>
<li>Maximum weight for a car or taxi <em>without</em> a trailer is 5000 kg.</li>
<li>Maximum weight for a car or taxi <em>with</em> a trailer is 8500 kg.</li>
<li>A route request with <a href="sdk-for-flutter-explore-transport-vehiclespecification-currentweightinkilograms">VehicleSpecification.currentWeightInKilograms</a> above <a href="sdk-for-flutter-explore-transport-vehiclespecification-grossweightinkilograms">VehicleSpecification.grossWeightInKilograms</a> may result in
non-compliant or invalid routes.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">int? currentWeightInKilograms;</code></pre>

 



</div>
`
}</HTMLBlock>
