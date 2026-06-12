---
title: "MapArrow constructor"
slug: "sdk-for-flutter-explore-mapview-maparrow-maparrow"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapArrow.html -->


<div>
<h1>MapArrow constructor</h1></div>

MapArrow(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-explore-core-geopolyline-class">GeoPolyline</a> geometry, </li>
<li>double widthInPixels, </li>
<li>Color color</li>
</ol>)
    

<p>Creates a new <code>MapArrow</code> instance.</p>
<p>Altitude component of <code>GeoPolyline</code>'s vertices is ignored.</p>
<ul>
<li>
<p><code>geometry</code> The geometry of the arrow tail. The last coordinate in the list defines the position where the
head of the arrow is located.</p>
</li>
<li>
<p><code>widthInPixels</code> The width of the arrow tail in pixel. Negative values are clamped to 0. The tip is scaled accordingly.</p>
</li>
<li>
<p><code>color</code> The color of the arrow. The alpha channel is ignored, the color is
interpreted as fully opaque.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory MapArrow(GeoPolyline geometry, double widthInPixels, ui.Color color) =&gt; $prototype.$init(geometry, widthInPixels, color);</code></pre>

 



</div>
`
}</HTMLBlock>
