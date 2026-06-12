---
title: "axleCount property"
slug: "sdk-for-flutter-navigate-transport-vehiclerestriction-axlecount"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- axleCount.html -->


<div>
<h1>axleCount property</h1></div>

<a href="/sdk-for-flutter-navigate-core-integerrange-class">IntegerRange</a>?
        axleCount
<div class="features">getter/setter pair</div>


<p>The axle count for which the current restriction applies.
Can be used in conjunction with <a href="/sdk-for-flutter-navigate-transport-restrictiontype">RestrictionType.weightPerAxleCount</a>
to specify restriction based on weight per number of axles.
The <code>axleCount</code> considers total number of axles on the whole vehicle (truck + trailers).
This can be used to limit the weight per axle for the whole truck.
If <code>axleCount</code> is null, the restriction is general and applies regardless of axle count.
If the upper limit of the <code>axleCount</code> range is 0 or <code>null</code> then it means the restriction applies
for values &gt;= lower limit, i.e. the upper limit of range if infinite or unbound.
When a user taps the icon, the allowed <code>axleCount</code> range can be retrieved directly
from <code>VehicleRestriction.axleCount</code>.
Examples:</p>
<ul>
<li>(2,2) → Restriction applies to vehicles with exactly 2 axles.</li>
<li>(2,4) → Restriction applies to vehicles with 2, 3, or 4 axles.</li>
<li>(2, 0) → Restriction applies to vehicles with 2 or more axles (equivalent to 2...∞)</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">IntegerRange? axleCount;</code></pre>

 



</div>
`
}</HTMLBlock>
