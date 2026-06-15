---
title: "grossWeightInKilograms property"
slug: "sdk-for-flutter-explore-transport-vehiclespecification-grossweightinkilograms"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- grossWeightInKilograms.html -->


<div>
<h1>grossWeightInKilograms property</h1></div>

        
        int?
        grossWeightInKilograms
<div class="features">getter/setter pair</div>


<p>Gross truck weight, including trailers and shipped goods when loaded at capacity, specified in
kilograms. The provided value must be greater than or equal to 0. If unspecified,
it will default to <a href="sdk-for-flutter-explore-transport-vehiclespecification-currentweightinkilograms">VehicleSpecification.currentWeightInKilograms</a>.
By default, it is not set.</p>
<p><strong>Notes:</strong></p>
<ul>
<li>Supported in <a href="sdk-for-flutter-explore-transport-transportmode">TransportMode.truck</a>, <a href="sdk-for-flutter-explore-transport-transportmode">TransportMode.bus</a>, <a href="sdk-for-flutter-explore-transport-transportmode">TransportMode.privateBus</a>,
<a href="sdk-for-flutter-explore-transport-transportmode">TransportMode.car</a> (Beta), <a href="sdk-for-flutter-explore-transport-transportmode">TransportMode.taxi</a> (Beta) transport modes.</li>
<li>Maximum weight for a car or taxi <em>without</em> a trailer is 4250 kg.</li>
<li>Maximum weight for a car or taxi <em>with</em> a trailer is 7550 kg.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">int? grossWeightInKilograms;</code></pre>

 



</div>
`
}</HTMLBlock>
