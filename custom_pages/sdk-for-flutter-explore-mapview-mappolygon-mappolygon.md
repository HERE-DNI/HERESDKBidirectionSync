---
title: "MapPolygon constructor"
slug: "sdk-for-flutter-explore-mapview-mappolygon-mappolygon"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapPolygon.html -->


<div>
<h1>MapPolygon constructor</h1></div>

MapPolygon(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-explore-core-geopolygon-class">GeoPolygon</a> geometry, </li>
<li>Color color</li>
</ol>)
    

<p>Creates a new MapPolygon instance with outline visualization disabled and containing the geometry passed in.</p>
<p>The winding order of the vertices can be in clockwise or counter-clockwise order.
It is recomended to provide the outer boundary ordered clockwise and closed.</p>
<p>Note:</p>
<ul>
<li>
<p>The polygon shape should not cover more than half of the globe,
otherwise unexpected results may occur.</p>
</li>
<li>
<p>Polygons which are self-intersecting are not supported and may lead to render
artifacts.</p>
</li>
<li>
<p>The inner boundaries (holes) specified in the GeoPolygon are ignored.</p>
</li>
<li>
<p><code>geometry</code> The list of vertices representing the outer boundary of polygon.</p>
</li>
<li>
<p><code>color</code> The fill color for the polygon</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory MapPolygon(GeoPolygon geometry, ui.Color color) =&gt; $prototype.$init(geometry, color);</code></pre>

 



</div>
`
}</HTMLBlock>
