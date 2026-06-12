---
title: "details property"
slug: "sdk-for-flutter-navigate-routing-violatedrestriction-details"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- details.html -->


<div>
<h1>details property</h1></div>

<a href="/sdk-for-flutter-navigate-routing-violatedrestrictiondetails-class">ViolatedRestrictionDetails</a>?
        details
<div class="features">getter/setter pair</div>


<p>The detailed information of restriction depending on the specific violation.
For time dependent restriction or transport mode restriction, this property will be null.
For vehicle restriction, the corresponding member will be set, for example, if the vehicle violates the maximum
allowed gross weight for a specific route, the max_gross_weight_in_kilograms will be set with the maximum allowed
gross weight for this route.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">ViolatedRestrictionDetails? details;</code></pre>

 



</div>
`
}</HTMLBlock>
