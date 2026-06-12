---
title: "intersection method"
slug: "sdk-for-flutter-explore-core-geobox-intersection"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- intersection.html -->


<div>
<h1>intersection method</h1></div>

List&lt;<a href="/sdk-for-flutter-explore-core-geobox-class">GeoBox</a>&gt;
intersection(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-explore-core-geobox-class">GeoBox</a> geoBox</li>
</ol>)

      

    

<p>Computes the intersection with the passed <a href="/sdk-for-flutter-explore-core-geobox-class">GeoBox</a>.</p>
<p>The altitude values are ignored.
Limitation: Geo boxes are considered as non-intersecting if they overlap only on a single point, horizontal line or vertical line.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<ul>
<li><code>geoBox</code> Another geo box to check intersection with.</li>
</ul>
<p>Returns <code>List&lt;GeoBox&gt;</code>. It will be empty if there is no overlap.</p>
<p>Otherwise, 1 or more geo boxes covering common area by this and passed <a href="/sdk-for-flutter-explore-core-geobox-class">GeoBox</a>.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;GeoBox&gt; intersection(GeoBox geoBox) =&gt; $prototype.intersection(this, geoBox);</code></pre>

 



</div>
`
}</HTMLBlock>
