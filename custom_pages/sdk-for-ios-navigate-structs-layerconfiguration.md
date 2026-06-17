---
title: "LayerConfiguration"
slug: "sdk-for-ios-navigate-structs-layerconfiguration"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/LayerConfiguration"></a>
<a title="LayerConfiguration Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-index">heresdk</a>

<a href="sdk-for-ios-navigate-core">Core</a>

        LayerConfiguration Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>LayerConfiguration</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">LayerConfiguration</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>A class to configure which layers should be enabled or disabled in the OCM map data.
Disabling a layer allows to reduce the amount of data that will be
downloaded or prefetched from the internet, for example, when panning the map view online or when downloading maps for offline use.</p>
<p><code>LayerConfiguration</code> changes made via <code><a href="sdk-for-ios-navigate-structs-sdkoptions">SDKOptions</a></code> require <code>sdk.maploader.MapUpdater</code> to align previously downloaded content.
To ensure that the changes in <code><a href="sdk-for-ios-navigate-structs-sdkoptions">SDKOptions</a></code> affect the map data,
it is recommended to trigger a map update. Without calling <code>mapUpdater.updateCatalog(...)</code>,
the adjustments will apply only to future map downloads and will not impact the currently installed map data, either in the cache or in the persisted storage.
Note that calling <code>updateCatalog(...)</code> will
update the version, only when a map update is available in the catalog.</p>
<p><strong>Notes</strong></p>
<ul>
<li><p>The <code>LayerConfiguration</code> is only available for the Navigate licenses that contains the offline maps
feature. It has no effect on other license.</p></li>
<li><p>The <code>LayerConfiguration</code> cannot be set separately for a region, it will be applied globally
for all regions that will be downloaded in the future.</p></li>
<li><p>It is not possible to specify a separate <code>LayerConfiguration</code> for the map cache and offline maps.
The <code>LayerConfiguration</code> will be always applied to both.</p></li>
<li><p>If a <code>LayerConfiguration</code> is applied, then only the listed features will be enabled,
all others will be disabled. For example, if you want to
disable only one feature, then all other features need to be present, or they will be also disabled.</p></li>
</ul>
<p>The <code>LayerConfiguration</code> controls which content will be subject of</p>
<ul>
<li>map download for features in <code>enabledFeatures()</code>,</li>
<li>explicit prefetching using <code>sdk.prefetcher.RoutePrefetcher</code>, <code>sdk.prefetcher.PolygonPrefetcher</code> and
implicit prefetching, such as when displaying a map view, for features in <code>implicitlyPrefetchedFeatures()</code>.</li>
</ul>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18LayerConfigurationV15enabledFeaturesSayAC7FeatureOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/enabledFeatures"></a>
<a class="token" href="#/s:7heresdk18LayerConfigurationV15enabledFeaturesSayAC7FeatureOGvp">enabledFeatures</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies feature configuration for enabling list of features enabled for map download.
Empty list disables map download, as no map content specified for download in this case.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">enabledFeatures</span><span class="p">:</span> <span class="p">[</span><span class="kt">LayerConfiguration</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-structs-layerconfiguration-feature">Feature</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18LayerConfigurationV28implicitlyPrefetchedFeaturesSayAC7FeatureOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/implicitlyPrefetchedFeatures"></a>
<a class="token" href="#/s:7heresdk18LayerConfigurationV28implicitlyPrefetchedFeaturesSayAC7FeatureOGvp">implicitlyPrefetchedFeatures</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies the list of features enabled for implicit and explicit map prefetch.
Implicit map prefetch will download map content for implicit prefetch features when showing a map in the MapView.</p>
<p>Allows to specify an empty list, effectively disabling implicit prefetching. In this case,
the system will prioritize minimal network usage, at the cost of reduced offline map availability.
When disabling certain implicitly prefetched features, less data will be prefetched when the map is rendered. Map
data that was already cached will not be removed until the least recently used strategy (LRU)
applies. That means you cannot remove any content from the map cache by updating the
<code>LayerConfiguration</code>. However, for new map data, it will be applied.</p>
<p>By default the list contains:</p>
<ul>
<li><code><a href="../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO10navigationyA2EmF">LayerConfiguration.Feature.navigation</a></code></li>
</ul>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">implicitlyPrefetchedFeatures</span><span class="p">:</span> <span class="p">[</span><span class="kt">LayerConfiguration</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-structs-layerconfiguration-feature">Feature</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18LayerConfigurationV15enabledFeaturesACSayAC7FeatureOG_tcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(enabledFeatures:)"></a>
<a class="token" href="#/s:7heresdk18LayerConfigurationV15enabledFeaturesACSayAC7FeatureOG_tcfc">init(enabledFeatures:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Initializes both, <code>enabled_features</code> and <code>implicitly_prefetched_features</code> with value passed to constructor.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">enabledFeatures</span><span class="p">:</span> <span class="p">[</span><span class="kt">LayerConfiguration</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-structs-layerconfiguration-feature">Feature</a></span><span class="p">])</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>enabledFeatures</em>
</code>
</td>
<td>
<div>
<p>List of map features to downloader through <code><a href="sdk-for-ios-navigate-classes-mapdownloader">MapDownloader</a></code>, and implicitly prefetch when using <code><a href="sdk-for-ios-navigate-classes-mapview">MapView</a></code></p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18LayerConfigurationV7FeatureO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/Feature"></a>
<a class="token" href="#/s:7heresdk18LayerConfigurationV7FeatureO">Feature</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines a list of possible map data features that can be enabled / disabled.
See <code><a href="../Structs/SDKOptions.html#/s:7heresdk10SDKOptionsV18layerConfigurationAA05LayerD0Vvp">SDKOptions.layerConfiguration</a></code></p>
<p>Following features are enabled by default:</p>
<ul>
<li><code><a href="../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO15detailRenderingyA2EmF">LayerConfiguration.Feature.detailRendering</a></code></li>
<li><code><a href="../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO11landmarks3dyA2EmF">LayerConfiguration.Feature.landmarks3d</a></code></li>
<li><code><a href="../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO10navigationyA2EmF">LayerConfiguration.Feature.navigation</a></code></li>
<li><code><a href="../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO13offlineSearchyA2EmF">LayerConfiguration.Feature.offlineSearch</a></code></li>
<li><code><a href="../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO14offlineRoutingyA2EmF">LayerConfiguration.Feature.offlineRouting</a></code></li>
<li><code><a href="../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO9renderingyA2EmF">LayerConfiguration.Feature.rendering</a></code></li>
</ul>
<p>All other features are disabled, by default.</p>
<p>Each feature enables a set of OCM layer groups to be downloaded by <code>sdk.maploader.MapDownloader</code>.
Detailed description of each layer group available in the
<a href="https://www.here.com/docs/bundle/optimized-client-map-developer-guide/page/README.html">HERE Optimized Client Map Developer Guide</a></p>
<p>Following features are enabled by default for implicit prefetch:</p>
<ul>
<li><code><a href="../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO10navigationyA2EmF">LayerConfiguration.Feature.navigation</a></code></li>
</ul>
<p>Implicit prefetch downloads map content for implicit prefetch features within a view port currently showed by MapView.
Explicit prefetching is done using <code>sdk.prefetcher.RoutePrefetcher</code> and <code>sdk.prefetcher.PolygonPrefetcher</code>.</p>
<p>Feature might have more than one layer group predefined to enable full experience. For example,
<code><a href="../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO10navigationyA2EmF">LayerConfiguration.Feature.navigation</a></code> requires routing attributes, visual-friendly
street names, maneuvers data and ability to interconnect those data sets.</p>
<p>The same map data is useful for different features, for example <code><a href="../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO9renderingyA2EmF">LayerConfiguration.Feature.rendering</a></code>
uses Places data to present it on the MapView, while <code><a href="../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO13offlineSearchyA2EmF">LayerConfiguration.Feature.offlineSearch</a></code> uses
the same data to enable discoverability by name or category. Hence, features might have overlapping sets of enabled layer groups.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-layerconfiguration-feature">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">Feature</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
</ul>
</div>
</section>
</section>
<section id="footer">
<p>© 2026 <a class="link" href="" rel="external noopener" target="_blank"></a>. All rights reserved. (Last updated: 2026-04-14)</p>
<p>Generated by <a class="link" href="https://github.com/realm/jazzy" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a class="link" href="https://realm.io" rel="external noopener" target="_blank">Realm</a> project.</p>
</section>
</article>
</div>
</body>
</html>

`
} </HTMLBlock>
