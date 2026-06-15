---
title: "CategoryQueryArea.withCorridorAndCenter constructor"
slug: "sdk-for-flutter-navigate-search-categoryqueryarea-categoryqueryarea-withcorridorandcenter"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- CategoryQueryArea.withCorridorAndCenter.html -->


<div>
<h1>CategoryQueryArea.withCorridorAndCenter constructor</h1></div>

CategoryQueryArea.withCorridorAndCenter(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-core-geocorridor-class">GeoCorridor</a> corridorArea, </li>
<li><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a> areaCenter</li>
</ol>)
    

<p>Constructs a new instance of this class from provided parameters.</p>
<p>The given corridor and center define the area that will be used in the search query.</p>
<p>When used with <code>SearchEngine</code>, the polyline is compressed and sent.
More complex polylines with large amounts of coordinates and with smaller
half-width may have the less relevant part removed, such as the one far away from the
search center. This usually makes no difference, because there will be enough POIs near
the search center. For use cases where it is important to search the entire polyline,
half-width can be increased or not set.
For example: Route between New York and Chicago with half-width 800 will be added to request
without removing the far away part, but route of the same length (around 360km) between
Milan (Italy) and Konstanz (Germany) will have the far away part removed due to its complexity.</p>
<p>The area center has to be within the corridor, otherwise it is ignored.</p>
<ul>
<li>
<p><code>corridorArea</code> Geographic corridor area in which to provide the most relevant places.</p>
</li>
<li>
<p><code>areaCenter</code> Geographic coordinates of the prioritized area center.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory CategoryQueryArea.withCorridorAndCenter(GeoCorridor corridorArea, GeoCoordinates areaCenter) =&gt; $prototype.withCorridorAndCenter(corridorArea, areaCenter);</code></pre>

 



</div>
`
}</HTMLBlock>
