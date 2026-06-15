---
title: "LayerConfigurationFeature enum"
slug: "sdk-for-flutter-navigate-core-engine-layerconfigurationfeature"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LayerConfigurationFeature.html -->


<div>
<h1>LayerConfigurationFeature enum</h1>
</div>

<p>Defines a list of possible map data features that can be enabled / disabled.</p>
<p>See <a href="sdk-for-flutter-navigate-core-engine-sdkoptions-layerconfiguration">SDKOptions.layerConfiguration</a></p>
<p>Following features are enabled by default:</p>
<ul>
<li><a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature.detailRendering</a></li>
<li><a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature.landmarks3d</a></li>
<li><a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature.navigation</a></li>
<li><a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature.offlineSearch</a></li>
<li><a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature.offlineRouting</a></li>
<li><a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature.rendering</a></li>
</ul>
<p>All other features are disabled, by default.</p>
<p>Each feature enables a set of OCM layer groups to be downloaded by <code>sdk.maploader.MapDownloader</code>.
Detailed description of each layer group available in the
<a href="https://www.here.com/docs/bundle/optimized-client-map-developer-guide/page/README.html">HERE Optimized Client Map Developer Guide</a></p>
<p>Following features are enabled by default for implicit prefetch:</p>
<ul>
<li><a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature.navigation</a></li>
</ul>
<p>Implicit prefetch downloads map content for implicit prefetch features within a view port currently showed by MapView.
Explicit prefetching is done using <code>sdk.prefetcher.RoutePrefetcher</code> and <code>sdk.prefetcher.PolygonPrefetcher</code>.</p>
<p>Feature might have more than one layer group predefined to enable full experience. For example,
<a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature.navigation</a> requires routing attributes, visual-friendly
street names, maneuvers data and ability to interconnect those data sets.</p>
<p>The same map data is useful for different features, for example <a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature.rendering</a>
uses Places data to present it on the MapView, while <a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature.offlineSearch</a> uses
the same data to enable discoverability by name or category. Hence, features might have overlapping sets of enabled layer groups.</p>


<h2>Values</h2>
<ul><li><a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></li><li><a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></li><li><a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></li><li><a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></li><li><a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></li><li><a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></li><li><a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></li><li><a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></li><li><a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></li><li><a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></li><li><a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></li><li><a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></li><li><a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></li><li><a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></li><li><a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></li><li><a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></li><li><a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></li><li><a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></li><li><a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></li><li><a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></li><li><a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></li><li><a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></li><li><a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></li><li><a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature">LayerConfigurationFeature</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature-hashcode">hashCode</a></li><li><a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature-index">index</a></li><li><a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature-runtimetype">runtimeType</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature-nosuchmethod">noSuchMethod</a></li><li><a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature-operator-equals">operator ==</a></li></ul>


<h2>Constants</h2>
<ul><li><a href="sdk-for-flutter-navigate-core-engine-layerconfigurationfeature-values-constant">values</a></li></ul>





</div>
`
}</HTMLBlock>
