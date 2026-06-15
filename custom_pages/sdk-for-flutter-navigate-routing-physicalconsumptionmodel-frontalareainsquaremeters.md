---
title: "frontalAreaInSquareMeters property"
slug: "sdk-for-flutter-navigate-routing-physicalconsumptionmodel-frontalareainsquaremeters"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- frontalAreaInSquareMeters.html -->


<div>
<h1>frontalAreaInSquareMeters property</h1></div>

        
        double
        frontalAreaInSquareMeters
<div class="features">getter/setter pair</div>


<p>Frontal area represents the total cross section area of the vehicle as viewed from the front, specified in square meters.
Physical consumption model is using this value in combination with <code>airDragCoefficient</code> to calculate the consumption caused by air resistance.
As fallback <a href="sdk-for-flutter-navigate-transport-vehiclespecification-widthincentimeters">VehicleSpecification.widthInCentimeters</a> and <a href="sdk-for-flutter-navigate-transport-vehiclespecification-heightincentimeters">VehicleSpecification.heightInCentimeters</a> are used.</p>
<p>This parameter is used to provide a more accurate consumption prediction for electric vehicles.</p>
<p>In the range from 0.5 to 50</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">double frontalAreaInSquareMeters;</code></pre>

 



</div>
`
}</HTMLBlock>
