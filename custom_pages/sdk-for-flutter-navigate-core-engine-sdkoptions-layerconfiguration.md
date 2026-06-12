---
title: "layerConfiguration property"
slug: "sdk-for-flutter-navigate-core-engine-sdkoptions-layerconfiguration"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- layerConfiguration.html -->


<div>
<h1>layerConfiguration property</h1></div>

<a href="/sdk-for-flutter-navigate-core-engine-layerconfiguration-class">LayerConfiguration</a>
layerConfiguration
<div class="features">getter/setter pair</div>


<p>Defines a list of data features that can be enabled / disabled. Once set to <a href="/sdk-for-flutter-navigate-core-engine-sdkoptions-class">SDKOptions</a> when
a new HERE SDK is constructed, it will affect the map cache and offline maps.
When disabling certain features, less data will be prefetched when the map is rendered. Map
data that was already cached will not be removed until the least recently used strategy (LRU)
applies. That means you cannot remove any content from the map cache by updating the
<a href="/sdk-for-flutter-navigate-core-engine-layerconfiguration-class">LayerConfiguration</a>. However, for new map data, it will be applied.
For offline maps, this <a href="/sdk-for-flutter-navigate-core-engine-layerconfiguration-class">LayerConfiguration</a> can reduce the download size of all regions.
Note that the <a href="/sdk-for-flutter-navigate-core-engine-layerconfiguration-class">LayerConfiguration</a> is applied globally to all regions that will be downloaded
in the future. It will not affect already downloaded regions. Updating a region will also
not update the <a href="/sdk-for-flutter-navigate-core-engine-layerconfiguration-class">LayerConfiguration</a>. Only the <a href="/sdk-for-flutter-navigate-core-engine-layerconfiguration-class">LayerConfiguration</a> will be used that was set
globally when a region was downloaded for the first time. If you want to update the
<a href="/sdk-for-flutter-navigate-core-engine-layerconfiguration-class">LayerConfiguration</a> for an already downloaded region, please delete the region and download it again.</p>
<p>Please also note</p>
<ul>
<li>The <a href="/sdk-for-flutter-navigate-core-engine-layerconfiguration-class">LayerConfiguration</a> is only applicable for the HERE SDK (Navigate) that contains the offline maps
feature. It has no effect on other licenses.</li>
<li>The <a href="/sdk-for-flutter-navigate-core-engine-layerconfiguration-class">LayerConfiguration</a> cannot be set separately for a region, it will be applied globally
for all regions that will be downloaded in the future.</li>
<li>It is not possible to specify a separate <a href="/sdk-for-flutter-navigate-core-engine-layerconfiguration-class">LayerConfiguration</a> for the map cache and offline maps.
The <a href="/sdk-for-flutter-navigate-core-engine-layerconfiguration-class">LayerConfiguration</a> will be always applied to both.</li>
<li>The <a href="/sdk-for-flutter-navigate-core-engine-layerconfiguration-class">LayerConfiguration</a> does affect the map cache when a device has connectivity. Even
when a device has connectivity it will only download the specified layers.</li>
<li>This is a beta feature and thus there can be bugs and unexpected behavior.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">LayerConfiguration layerConfiguration;</code></pre>

 



</div>
`
}</HTMLBlock>
