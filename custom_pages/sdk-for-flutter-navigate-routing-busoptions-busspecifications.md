---
title: "busSpecifications property"
slug: "sdk-for-flutter-navigate-routing-busoptions-busspecifications"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- busSpecifications.html -->


<div>
<h1>busSpecifications property</h1></div>

<a class="deprecated" href="sdk-for-flutter-navigate-transport-busspecifications-class">BusSpecifications</a>
busSpecifications
<div class="features">getter/setter pair</div>


<p>Detailed bus specifications such as dimensions and weight.</p>
<p><strong>Note:</strong> Some members of <code>bus_specifications</code> have limited value range.</p>
<ul>
<li><a href="sdk-for-flutter-navigate-transport-busspecifications-grossweightinkilograms">BusSpecifications.grossWeightInKilograms</a> must not be negative.</li>
<li><a href="sdk-for-flutter-navigate-transport-busspecifications-heightincentimeters">BusSpecifications.heightInCentimeters</a> must be in the range [0, 5000].</li>
<li><a href="sdk-for-flutter-navigate-transport-busspecifications-widthincentimeters">BusSpecifications.widthInCentimeters</a> must be in the range [0, 5000].</li>
<li><a href="sdk-for-flutter-navigate-transport-busspecifications-lengthincentimeters">BusSpecifications.lengthInCentimeters</a> must be in the range [0, 30000].
The validation of the range is done in the method that takes <code>BusOptions</code> as parameter.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">BusSpecifications busSpecifications;</code></pre>

 



</div>
`
}</HTMLBlock>
