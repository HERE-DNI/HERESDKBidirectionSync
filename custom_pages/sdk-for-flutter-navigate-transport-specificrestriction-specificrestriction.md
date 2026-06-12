---
title: "SpecificRestriction constructor"
slug: "sdk-for-flutter-navigate-transport-specificrestriction-specificrestriction"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SpecificRestriction.html -->


<div>
<h1>SpecificRestriction constructor</h1></div>

SpecificRestriction(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-transport-restrictiontype">RestrictionType</a> type, </li>
<li><a href="/sdk-for-flutter-navigate-core-integerrange-class">IntegerRange</a> value</li>
</ol>)
    

<p>Creates a new instance.</p>
<ul>
<li><code>type</code> Type of restriction.</li>
<li><code>value</code> Values for which the restriction applies.
Examples:</li>
<li><code>(min, max)</code> → Restriction applies for all values between min and max inclusive.</li>
<li><code>(n, n)</code> → Restriction applies to an exact value.</li>
<li><code>(n, 0)</code> or <code>(n, null)</code> → Restriction applies for values greater than or equal to min (unbounded upper limit).</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">SpecificRestriction(this.type, this.value);</code></pre>

 



</div>
`
}</HTMLBlock>
