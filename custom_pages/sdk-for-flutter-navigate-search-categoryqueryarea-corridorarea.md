---
title: "corridorArea property"
slug: "sdk-for-flutter-navigate-search-categoryqueryarea-corridorarea"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- corridorArea.html -->


<div>
<h1>corridorArea property</h1></div>

<a href="sdk-for-flutter-navigate-core-geocorridor-class">GeoCorridor</a>?
        corridorArea
<div class="features">final</div>


<p>Geographic corridor area in which to provide the most relevant places.
The contained polyline and half-width define the area that will be used in a search query.</p>
<p>When used with <code>SearchEngine</code>, the polyline is compressed and sent.
More complex polylines with large amounts of coordinates and with smaller
half-width may have the less relevant part removed, such as the one far away from the
search center. This usually makes no difference, because there will be enough POIs near
the search center. For use cases where it is important to search the entire polyline,
half-width can be increased or not set.
For example: Route between New York and Chicago with half-width 800 will be added to request
without removing the far away part, but route of the same length (around 360km) between
Milan (Italy) and Konstanz (Germany) will have the far away part removed due to its complexity.</p>
<p>When <a href="sdk-for-flutter-navigate-search-categoryqueryarea-corridorarea">CategoryQueryArea.corridorArea</a> is provided,
<a href="sdk-for-flutter-navigate-search-categoryqueryarea-areacenter">CategoryQueryArea.areaCenter</a> has to be within it, otherwise
<a href="sdk-for-flutter-navigate-search-categoryqueryarea-areacenter">CategoryQueryArea.areaCenter</a> is ignored when searching.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">final GeoCorridor? corridorArea;</code></pre>

 



</div>
`
}</HTMLBlock>
