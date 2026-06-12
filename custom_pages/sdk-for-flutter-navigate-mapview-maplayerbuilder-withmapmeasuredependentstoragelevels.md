---
title: "withMapMeasureDependentStorageLevels abstract method"
slug: "sdk-for-flutter-navigate-mapview-maplayerbuilder-withmapmeasuredependentstoragelevels"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- withMapMeasureDependentStorageLevels.html -->


<div>
<h1>withMapMeasureDependentStorageLevels abstract method</h1></div>

<a href="/sdk-for-flutter-navigate-mapview-maplayerbuilder-class">MapLayerBuilder</a>
withMapMeasureDependentStorageLevels(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-mapview-maplayermapmeasuredependentstoragelevels-class">MapLayerMapMeasureDependentStorageLevels</a> mapLayerMapMeasureDependentStorageLevels</li>
</ol>)

      

    

<p>Applies a mapping from the map measure to the storage level.</p>
<p>This mapping is used by the layer to request data
for the specified storage level corresponding to the map measure from the datasource.
This can be used for example to fine-tune the resolution of raster layers.
Note: When the map camera is significantly tilted, the storage level is further reduced for data towards the horizon.
Note: Mappings that request higher storage levels will lead to an increased number
of requests to the raster tile service.
Providing the map measure to storage level mapping is optional. If not provided, the default mapping will
use a storage level that is for raster layers one and for others three levels lower than the zoom level,
corresponding to an offset of -1 and -3.</p>
<ul>
<li><code>mapLayerMapMeasureDependentStorageLevels</code> The map measure to storage level mapping that should be applied for the layer.</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-navigate-mapview-maplayerbuilder-class">MapLayerBuilder</a>. This class instance.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">MapLayerBuilder withMapMeasureDependentStorageLevels(MapLayerMapMeasureDependentStorageLevels mapLayerMapMeasureDependentStorageLevels);</code></pre>

 



</div>
`
}</HTMLBlock>
