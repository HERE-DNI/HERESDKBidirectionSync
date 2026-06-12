---
title: "trailerAxleCount property"
slug: "sdk-for-flutter-navigate-transport-truckspecifications-traileraxlecount"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- trailerAxleCount.html -->


<div>
<h1>trailerAxleCount property</h1></div>

        
        int?
        trailerAxleCount
<div class="features">getter/setter pair</div>


<p>Defines total number of axles across all the trailers attached to the vehicle.
This number is included in <a href="/sdk-for-flutter-navigate-transport-truckspecifications-axlecount">TruckSpecifications.axleCount</a>, hence <a href="/sdk-for-flutter-navigate-transport-truckspecifications-traileraxlecount">TruckSpecifications.trailerAxleCount</a> must be less than <a href="/sdk-for-flutter-navigate-transport-truckspecifications-axlecount">TruckSpecifications.axleCount</a>
and greater than or equal to 1. <a href="/sdk-for-flutter-navigate-transport-truckspecifications-axlecount">TruckSpecifications.axleCount</a> and <a href="/sdk-for-flutter-navigate-transport-truckspecifications-trailercount">TruckSpecifications.trailerCount</a> are required to specify <a href="/sdk-for-flutter-navigate-transport-truckspecifications-traileraxlecount">TruckSpecifications.trailerAxleCount</a>.
By default, it is not set.
Note: This parameter is currently used only for the calculation of tolls in regions where it is applicable.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">int? trailerAxleCount;</code></pre>

 



</div>
`
}</HTMLBlock>
