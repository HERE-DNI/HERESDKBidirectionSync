---
title: "geometry property"
slug: "sdk-for-flutter-navigate-mapview-mappolygon-geometry"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- geometry.html -->


<div>
<h1>geometry property</h1></div>
<section id="getter">

<a href="sdk-for-flutter-navigate-core-geopolygon-class">GeoPolygon</a>
geometry


<p>The geometry of the polygon. Setting a new geometry will update the appearance.
Gets the current geometry of the polygon.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">GeoPolygon get geometry;</code></pre>

</section>
<section id="setter">

void
geometry=(<a href="sdk-for-flutter-navigate-core-geopolygon-class">GeoPolygon</a> value)


<p>The geometry of the polygon. Setting a new geometry will update the appearance.
Sets a new geometry to update the appearance.</p>
<p>The winding order of the vertices can be in clockwise or counter-clockwise order.
It is recomended to provide the outer boundary ordered clockwise and closed.</p>
<p>Note:</p>
<ul>
<li>The polygon shape should not cover more than half of the globe,
otherwise unexpected results may occur.</li>
<li>Polygons which are self-intersecting are not supported and may lead to render
artifacts.</li>
<li>The inner boundaries (holes) specified in the GeoPolygon are ignored.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set geometry(GeoPolygon value);</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
