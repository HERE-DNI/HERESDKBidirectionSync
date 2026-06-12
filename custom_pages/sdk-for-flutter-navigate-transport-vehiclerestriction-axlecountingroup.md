---
title: "axleCountInGroup property"
slug: "sdk-for-flutter-navigate-transport-vehiclerestriction-axlecountingroup"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- axleCountInGroup.html -->


<div>
<h1>axleCountInGroup property</h1></div>

<a href="/sdk-for-flutter-navigate-core-integerrange-class">IntegerRange</a>?
        axleCountInGroup
<div class="features">getter/setter pair</div>


<p>Number of axles in a group for which the current restriction applies.
<code>axleCountInGroup</code> is a set of axles close together: single, tandem (2), triple (3), etc.
Can be used in conjunction with <a href="/sdk-for-flutter-navigate-transport-restrictiontype">RestrictionType.weightPerAxleGroup</a>
to specify restriction based on weight per axle group.
The <code>axleCountInGroup</code> considers number of axles in a specific axle group (usually rear axles on the truck or trailer).
This can be used to limit weight for a tandem/triple rear axle group.
If the upper limit of the <code>axleCountInGroup</code> range is 0 or <code>null</code> then it means the restriction applies
for values &gt;= lower limit, i.e. the upper limit of range if infinite or unbound.
Examples:</p>
<ul>
<li>(1,1) → Restriction applies to single axle group.</li>
<li>(2,2) → Restriction applies to tandem axle group.</li>
<li>(2,4) → Restriction applies to any axle group from 2 to 4 axles.</li>
<li>(2,0) → Restriction applies to axle groups with 2 or more axles.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">IntegerRange? axleCountInGroup;</code></pre>

 



</div>
`
}</HTMLBlock>
