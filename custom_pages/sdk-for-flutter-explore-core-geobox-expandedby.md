---
title: "expandedBy method"
slug: "sdk-for-flutter-explore-core-geobox-expandedby"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- expandedBy.html -->


<div>
<h1>expandedBy method</h1></div>

<a href="/sdk-for-flutter-explore-core-geobox-class">GeoBox</a>
expandedBy(<ol class="parameter-list"> <li>double southMeters, </li>
<li>double westMeters, </li>
<li>double northMeters, </li>
<li>double eastMeters, </li>
</ol>)

      

    

<p>Creates a <code>GeoBox</code> which is expanded by a fixed distance.</p>
<p>Throws an InstantiationError if it is not possible to create a valid
<code>GeoBox</code> with the given arguments.</p>
<ul>
<li>
<p><code>southMeters</code> Distance in the south direction in meters to expand the <code>GeoBox</code>.</p>
</li>
<li>
<p><code>westMeters</code> Distance in the west direction in meters to expand the <code>GeoBox</code>.</p>
</li>
<li>
<p><code>northMeters</code> Distance in the north direction in meters to expand the <code>GeoBox</code>.</p>
</li>
<li>
<p><code>eastMeters</code> Distance in the east direction in meters to expand the <code>GeoBox</code>.</p>
</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-explore-core-geobox-class">GeoBox</a>. The expanded <code>GeoBox</code>.</p>
<p>Throws <a href="/sdk-for-flutter-explore-core-errors-instantiationexception-class">InstantiationException</a>. Instantiation error.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">GeoBox expandedBy(double southMeters, double westMeters, double northMeters, double eastMeters) =&gt; $prototype.expandedBy(this, southMeters, westMeters, northMeters, eastMeters);</code></pre>

 



</div>
`
}</HTMLBlock>
