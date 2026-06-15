---
title: "estimateMapDataSize abstract method"
slug: "sdk-for-flutter-navigate-prefetcher-polygonprefetcher-estimatemapdatasize"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- estimateMapDataSize.html -->


<div>
<h1>estimateMapDataSize abstract method</h1></div>

<a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>
estimateMapDataSize(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-core-geopolygon-class">GeoPolygon</a> geoPolygon, </li>
<li><a href="sdk-for-flutter-navigate-prefetcher-mapdatasizelistener-class">MapDataSizeListener</a> callback</li>
</ol>)

      

    

<p>Estimates map data size for the area bounded by geo polygon.</p>
<p>Size for tiles that are already
in the cache will not be included in the final result.</p>
<ul>
<li>
<p><code>geoPolygon</code> Area to estimate map data size for.</p>
</li>
<li>
<p><code>callback</code> Callback that is triggered to report the result of map data size estimation.</p>
</li>
</ul>
<p>Returns <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate execution of the task.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle estimateMapDataSize(GeoPolygon geoPolygon, MapDataSizeListener callback);</code></pre>

 



</div>
`
}</HTMLBlock>
