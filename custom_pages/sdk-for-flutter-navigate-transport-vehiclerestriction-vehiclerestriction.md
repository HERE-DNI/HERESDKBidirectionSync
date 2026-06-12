---
title: "VehicleRestriction constructor"
slug: "sdk-for-flutter-navigate-transport-vehiclerestriction-vehiclerestriction"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- VehicleRestriction.html -->


<div>
<h1>VehicleRestriction constructor</h1></div>

VehicleRestriction(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-transport-specificrestriction-class">SpecificRestriction</a>? restriction</li>
</ol>)
    

<p>Creates an unconditional restriction.</p>
<ul>
<li><code>restriction</code> A <code>SpecificRestriction</code> defines what type of restriction applies (weight, height, etc.)
and the range of allowed values.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">VehicleRestriction(this.restriction)
    : hazmatRestriction = null, timeRestriction = null, appliesToDelivery = true, weather = null, truckCategory = null, trailerCount = null, axleCount = null, axleCountInGroup = null;</code></pre>

 



</div>
`
}</HTMLBlock>
