---
title: "CarSpecifications constructor"
slug: "sdk-for-flutter-navigate-transport-carspecifications-carspecifications"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- CarSpecifications.html -->


<div>
<h1>CarSpecifications constructor</h1></div>

CarSpecifications([<ol class="parameter-list"> <li>int? grossWeightInKilograms = null, </li>
<li>int? heightInCentimeters = null, </li>
<li>int? widthInCentimeters = null, </li>
<li>int? lengthInCentimeters = null, </li>
<li>int? axleCount = null, </li>
<li>int? trailerCount = null, </li>
<li>int? trailerAxleCount = null, </li>
</ol>])
    

<p>Creates a new instance.</p>
<ul>
<li><code>grossWeightInKilograms</code> Car weight including trailers and shipped goods in kilograms. The provided value
must be greater than or equal to 0. By default, it is not set.
<strong>Note:</strong>
This parameter is limited to a maximum weight of 4250 kg without trailer and 7550 kg with trailer.</li>
<li><code>heightInCentimeters</code> Car height in centimeters. The provided value must be in the range [0, 5000].
By default, it is not set.</li>
<li><code>widthInCentimeters</code> Car width in centimeters. The provided value must be in the range [0, 5000].
By default, it is not set.</li>
<li><code>lengthInCentimeters</code> Car length in centimeters. The provided value must be in the range [0, 30000].
By default, it is not set.</li>
<li><code>axleCount</code> Defines total number of axles in the vehicle. The provided value must be greater than or
equal to 2. By default, it is not set.
Route calculation: When not set, possible axle count restrictions will not be
taken into consideration.
When specifying <a href="/sdk-for-flutter-navigate-transport-carspecifications-traileraxlecount">CarSpecifications.trailerAxleCount</a>, then <a href="/sdk-for-flutter-navigate-transport-carspecifications-axlecount">CarSpecifications.axleCount</a> is required and must be greater than <a href="/sdk-for-flutter-navigate-transport-carspecifications-traileraxlecount">CarSpecifications.trailerAxleCount</a>.</li>
<li><code>trailerCount</code> Defines number of trailers attached to the vehicle. The provided value must be in the range
[0, 1]. By default, it is not set.
When specifying <a href="/sdk-for-flutter-navigate-transport-carspecifications-traileraxlecount">CarSpecifications.trailerAxleCount</a>, then <a href="/sdk-for-flutter-navigate-transport-carspecifications-trailercount">CarSpecifications.trailerCount</a> is required and must be greater than 0.</li>
<li><code>trailerAxleCount</code> Defines total number of axles across all the trailers attached to the vehicle.
This number is included in <a href="/sdk-for-flutter-navigate-transport-carspecifications-axlecount">CarSpecifications.axleCount</a>, hence <a href="/sdk-for-flutter-navigate-transport-carspecifications-traileraxlecount">CarSpecifications.trailerAxleCount</a> must be less than <a href="/sdk-for-flutter-navigate-transport-carspecifications-axlecount">CarSpecifications.axleCount</a>
and greater than or equal to 1. <a href="/sdk-for-flutter-navigate-transport-carspecifications-axlecount">CarSpecifications.axleCount</a> and <a href="/sdk-for-flutter-navigate-transport-carspecifications-trailercount">CarSpecifications.trailerCount</a> are required to specify <a href="/sdk-for-flutter-navigate-transport-carspecifications-traileraxlecount">CarSpecifications.trailerAxleCount</a>.
By default, it is not set.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">CarSpecifications([int? grossWeightInKilograms = null, int? heightInCentimeters = null, int? widthInCentimeters = null, int? lengthInCentimeters = null, int? axleCount = null, int? trailerCount = null, int? trailerAxleCount = null])
  : grossWeightInKilograms = grossWeightInKilograms, heightInCentimeters = heightInCentimeters, widthInCentimeters = widthInCentimeters, lengthInCentimeters = lengthInCentimeters, axleCount = axleCount, trailerCount = trailerCount, trailerAxleCount = trailerAxleCount;</code></pre>

 



</div>
`
}</HTMLBlock>
