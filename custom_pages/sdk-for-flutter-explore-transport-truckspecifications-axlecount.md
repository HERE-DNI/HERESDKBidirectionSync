---
title: "axleCount property"
slug: "sdk-for-flutter-explore-transport-truckspecifications-axlecount"
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


<p>Defines total number of axles in the vehicle. The provided value must be greater than or
equal to 2. By default, it is not set.
Route calculation: When not set, possible axle count restrictions will not be
taken into consideration.
Rendering <code>sdk.mapview.TruckProfile</code>: When set, truck restriction icons for an axle count
greater than <a href="sdk-for-flutter-explore-transport-truckspecifications-axlecount">TruckSpecifications.axleCount</a> will not be displayed.
When specifying <a href="sdk-for-flutter-explore-transport-truckspecifications-traileraxlecount">TruckSpecifications.trailerAxleCount</a>, then <a href="sdk-for-flutter-explore-transport-truckspecifications-axlecount">TruckSpecifications.axleCount</a> is required and must be greater than <a href="sdk-for-flutter-explore-transport-truckspecifications-traileraxlecount">TruckSpecifications.trailerAxleCount</a>.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">int? axleCount;</code></pre>

 



</div>
`
}</HTMLBlock>
