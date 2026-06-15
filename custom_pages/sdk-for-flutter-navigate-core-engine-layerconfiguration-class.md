---
title: "LayerConfiguration class"
slug: "sdk-for-flutter-navigate-core-engine-layerconfiguration-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LayerConfiguration-class.html -->


<div>
<h1>LayerConfiguration class</h1></div>

<p>A class to configure which layers should be enabled or disabled in the OCM map data.</p>
<p>Disabling a layer allows to reduce the amount of data that will be
downloaded or prefetched from the internet, for example, when panning the map view online or when downloading maps for offline use.</p>
<p><code>LayerConfiguration</code> changes made via <a href="sdk-for-flutter-navigate-core-engine-sdkoptions-class">SDKOptions</a> require <code>sdk.maploader.MapUpdater</code> to align previously downloaded content.
To ensure that the changes in <a href="sdk-for-flutter-navigate-core-engine-sdkoptions-class">SDKOptions</a> affect the map data,
it is recommended to trigger a map update. Without calling <code>mapUpdater.updateCatalog(...)</code>,
the adjustments will apply only to future map downloads and will not impact the currently installed map data, either in the cache or in the persisted storage.
Note that calling <code>updateCatalog(...)</code> will
update the version, only when a map update is available in the catalog.</p>
<p><strong>Notes</strong></p>
<ul>
<li>
<p>The <code>LayerConfiguration</code> is only available for the Navigate licenses that contains the offline maps
feature. It has no effect on other license.</p>
</li>
<li>
<p>The <code>LayerConfiguration</code> cannot be set separately for a region, it will be applied globally
for all regions that will be downloaded in the future.</p>
</li>
<li>
<p>It is not possible to specify a separate <code>LayerConfiguration</code> for the map cache and offline maps.
The <code>LayerConfiguration</code> will be always applied to both.</p>
</li>
<li>
<p>If a <code>LayerConfiguration</code> is applied, then only the listed features will be enabled,
all others will be disabled. For example, if you want to
disable only one feature, then all other features need to be present, or they will be also disabled.</p>
</li>
</ul>
<p>The <code>LayerConfiguration</code> controls which content will be subject of</p>
<ul>
<li>map download for features in <code>enabledFeatures()</code>,</li>
<li>explicit prefetching using <code>sdk.prefetcher.RoutePrefetcher</code>, <code>sdk.prefetcher.PolygonPrefetcher</code> and
implicit prefetching, such as when displaying a map view, for features in <code>implicitlyPrefetchedFeatures()</code>.</li>
</ul>


<h2>Constructors</h2>
<ul><li><a href="sdk-for-flutter-navigate-core-engine-layerconfiguration-layerconfiguration">LayerConfiguration</a></li><li><a href="sdk-for-flutter-navigate-core-engine-layerconfiguration-layerconfiguration-withdefaults">LayerConfiguration.withDefaults</a></li><li><a href="sdk-for-flutter-navigate-core-engine-layerconfiguration-layerconfiguration-withdownloadandprefetchfeatures">LayerConfiguration.withDownloadAndPrefetchFeatures</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="sdk-for-flutter-navigate-core-engine-layerconfiguration-enabledfeatures">enabledFeatures</a></li><li><a href="sdk-for-flutter-navigate-core-engine-layerconfiguration-hashcode">hashCode</a></li><li><a href="sdk-for-flutter-navigate-core-engine-layerconfiguration-implicitlyprefetchedfeatures">implicitlyPrefetchedFeatures</a></li><li><a href="sdk-for-flutter-navigate-core-engine-layerconfiguration-runtimetype">runtimeType</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="sdk-for-flutter-navigate-core-engine-layerconfiguration-nosuchmethod">noSuchMethod</a></li><li><a href="sdk-for-flutter-navigate-core-engine-layerconfiguration-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="sdk-for-flutter-navigate-core-engine-layerconfiguration-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>
