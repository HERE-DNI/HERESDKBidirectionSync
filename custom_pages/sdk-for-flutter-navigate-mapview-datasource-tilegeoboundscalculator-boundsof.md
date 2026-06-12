---
title: "boundsOf abstract method"
slug: "sdk-for-flutter-navigate-mapview-datasource-tilegeoboundscalculator-boundsof"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- boundsOf.html -->


<div>
<h1>boundsOf abstract method</h1></div>

<a href="/sdk-for-flutter-navigate-core-geobox-class">GeoBox</a>
boundsOf(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-mapview-datasource-tilekey-class">TileKey</a> tileKey</li>
</ol>)

      

    

<p>Computes the geodetic bounds (as <a href="/sdk-for-flutter-navigate-core-geobox-class">GeoBox</a>) for a tile identified by <a href="/sdk-for-flutter-navigate-mapview-datasource-tilekey-class">TileKey</a>.</p>
<ul>
<li><code>tileKey</code> <a href="/sdk-for-flutter-navigate-mapview-datasource-tilekey-class">TileKey</a> to compute geodetic bounds for.
The geodetic bounds would be calculated relative to the tiling scheme
provided at this <a href="/sdk-for-flutter-navigate-mapview-datasource-tilegeoboundscalculator-class">TileGeoBoundsCalculator</a> instance creation.</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-navigate-core-geobox-class">GeoBox</a>. The geodetic bounds of tile identified by given <a href="/sdk-for-flutter-navigate-mapview-datasource-tilekey-class">TileKey</a>.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">GeoBox boundsOf(TileKey tileKey);</code></pre>

 



</div>
`
}</HTMLBlock>
