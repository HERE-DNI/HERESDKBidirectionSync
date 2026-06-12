---
title: "intersectionGeoBoxes static method"
slug: "sdk-for-flutter-navigate-core-geobox-intersectiongeoboxes"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- intersectionGeoBoxes.html -->


<div>
<h1>intersectionGeoBoxes static method</h1></div>

List&lt;<a href="/sdk-for-flutter-navigate-core-geobox-class">GeoBox</a>&gt;
intersectionGeoBoxes(<ol class="parameter-list single-line"> <li>List&lt;<a href="/sdk-for-flutter-navigate-core-geobox-class">GeoBox</a>&gt; geoBoxes</li>
</ol>)

      

    

<p>Computes intersection of list of <a href="/sdk-for-flutter-navigate-core-geobox-class">GeoBox</a> instances.</p>
<p>The altitude values are ignored.
Limitation: Geo boxes are considered as non-intersecting if they overlap only on a single point, horizontal line or vertical line.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<ul>
<li><code>geoBoxes</code> List of <a href="/sdk-for-flutter-navigate-core-geobox-class">GeoBox</a> instances.</li>
</ul>
<p>Returns <code>List&lt;GeoBox&gt;</code>. It will be empty if there is no overlap between all the passed <a href="/sdk-for-flutter-navigate-core-geobox-class">GeoBox</a> instances.</p>
<p>Otherwise, 1 or more geo boxes covering common area by all the passed <a href="/sdk-for-flutter-navigate-core-geobox-class">GeoBox</a> instances.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static List&lt;GeoBox&gt; intersectionGeoBoxes(List&lt;GeoBox&gt; geoBoxes) =&gt; $prototype.intersectionGeoBoxes(geoBoxes);</code></pre>

 



</div>
`
}</HTMLBlock>
