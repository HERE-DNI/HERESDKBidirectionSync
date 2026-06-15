---
title: "withStorageLevelOffset static method"
slug: "sdk-for-flutter-navigate-mapview-maplayermapmeasuredependentstoragelevels-withstorageleveloffset"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- withStorageLevelOffset.html -->


<div>
<h1>withStorageLevelOffset static method</h1></div>

<a href="sdk-for-flutter-navigate-mapview-maplayermapmeasuredependentstoragelevels-class">MapLayerMapMeasureDependentStorageLevels</a>
withStorageLevelOffset(<ol class="parameter-list single-line"> <li>int offset</li>
</ol>)

      

    

<p>Creates an instance of <a href="sdk-for-flutter-navigate-mapview-maplayermapmeasuredependentstoragelevels-class">MapLayerMapMeasureDependentStorageLevels</a> with the specified storage level offset.</p>
<p>This creates a map where the storage level is determined by applying an "offset" to the zoom level.
A negative offset results in a storage level lower than the zoom level, while a positive offset increases it.
For example, with an offset of 0, the storage level matches the zoom level directly.
An offset of -1 makes the storage level one less than the zoom level, and so on.
The offset value is clamped to the range of -3 to 3.
Note: The generated mapping adjusts so that when the map camera is significantly tilted,
the storage level is further reduced for data near the horizon.</p>
<ul>
<li><code>offset</code> Defines an offset of storage level from the zoom level.
The value will be clamped to a range of -3 to 3.</li>
</ul>
<p>Returns <a href="sdk-for-flutter-navigate-mapview-maplayermapmeasuredependentstoragelevels-class">MapLayerMapMeasureDependentStorageLevels</a>. MapLayerMapMeasureDependentStorageLevels instance.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static MapLayerMapMeasureDependentStorageLevels withStorageLevelOffset(int offset) =&gt; $prototype.withStorageLevelOffset(offset);</code></pre>

 



</div>
`
}</HTMLBlock>
