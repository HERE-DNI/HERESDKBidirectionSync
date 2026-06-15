---
title: "MapPolygon.withOutlineColorAndOutlineWidthInPixels constructor"
slug: "sdk-for-flutter-navigate-mapview-mappolygon-mappolygon-withoutlinecolorandoutlinewidthinpixels"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapPolygon.withOutlineColorAndOutlineWidthInPixels.html -->


<div>
<h1>MapPolygon.withOutlineColorAndOutlineWidthInPixels constructor</h1></div>

MapPolygon.withOutlineColorAndOutlineWidthInPixels(<ol class="parameter-list"> <li><a href="sdk-for-flutter-navigate-core-geopolygon-class">GeoPolygon</a> geometry, </li>
<li>Color color, </li>
<li>Color outlineColor, </li>
<li>double outlineWidthInPixels, </li>
</ol>)
    

<p>Creates a new MapPolygon instance with outline visualization enabled and containing the geometry passed in.</p>
<p>Transparent outlines are not supported. Any color with transparency (alpha value other than 1)
will be rendered as fully opaque by interpreting the alpha value as 1.</p>
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
<p><code>color</code> The fill color for the polygon.</p>
</li>
<li>
<p><code>outlineColor</code> The color of the polygon outline, alpha channel is ignored and treated as 1.</p>
</li>
<li>
<p><code>outlineWidthInPixels</code> The width of the polygon outline (in pixels). Negative values are clamped to 0.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory MapPolygon.withOutlineColorAndOutlineWidthInPixels(GeoPolygon geometry, ui.Color color, ui.Color outlineColor, double outlineWidthInPixels) =&gt; $prototype.withOutlineColorAndOutlineWidthInPixels(geometry, color, outlineColor, outlineWidthInPixels);</code></pre>

 



</div>
`
}</HTMLBlock>
