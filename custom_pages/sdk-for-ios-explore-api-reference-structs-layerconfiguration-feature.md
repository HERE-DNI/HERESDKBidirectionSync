---
title: "Feature Enumeration Reference"
slug: "sdk-for-ios-explore-api-reference-structs-layerconfiguration-feature"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- Feature.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Enum/Feature"></a>
<a title="Feature Enumeration Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="sdk-for-ios-explore-api-reference-..-..-index">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-..-index">heresdk</a>
<img alt="" id="carat" src="../../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-..-core">Core</a>
<img alt="" id="carat" src="../../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-..-structs-layerconfiguration">LayerConfiguration</a>
<img alt="" id="carat" src="../../img/carat.png"/>
        Feature Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public enum Feature : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
<p>Defines a list of possible map data features that can be enabled / disabled.
See <code><a href="../../Structs/SDKOptions.html#/s:7heresdk10SDKOptionsV18layerConfigurationAA05LayerD0Vvp">SDKOptions.layerConfiguration</a></code></p>
<p>Following features are enabled by default:</p>
<ul>
<li><code><a href="../../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO15detailRenderingyA2EmF">LayerConfiguration.Feature.detailRendering</a></code></li>
<li><code><a href="../../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO11landmarks3dyA2EmF">LayerConfiguration.Feature.landmarks3d</a></code></li>
<li><code><a href="../../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO10navigationyA2EmF">LayerConfiguration.Feature.navigation</a></code></li>
<li><code><a href="../../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO13offlineSearchyA2EmF">LayerConfiguration.Feature.offlineSearch</a></code></li>
<li><code><a href="../../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO14offlineRoutingyA2EmF">LayerConfiguration.Feature.offlineRouting</a></code></li>
<li><code><a href="../../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO9renderingyA2EmF">LayerConfiguration.Feature.rendering</a></code></li>
</ul>
<p>All other features are disabled, by default.</p>
<p>Each feature enables a set of OCM layer groups to be downloaded by <code>sdk.maploader.MapDownloader</code>.
Detailed description of each layer group available in the
<a href="https://www.here.com/docs/bundle/optimized-client-map-developer-guide/page/README.html">HERE Optimized Client Map Developer Guide</a></p>
<p>Following features are enabled by default for implicit prefetch:</p>
<ul>
<li><code><a href="../../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO10navigationyA2EmF">LayerConfiguration.Feature.navigation</a></code></li>
</ul>
<p>Implicit prefetch downloads map content for implicit prefetch features within a view port currently showed by MapView.
Explicit prefetching is done using <code>sdk.prefetcher.RoutePrefetcher</code> and <code>sdk.prefetcher.PolygonPrefetcher</code>.</p>
<p>Feature might have more than one layer group predefined to enable full experience. For example,
<code><a href="../../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO10navigationyA2EmF">LayerConfiguration.Feature.navigation</a></code> requires routing attributes, visual-friendly
street names, maneuvers data and ability to interconnect those data sets.</p>
<p>The same map data is useful for different features, for example <code><a href="../../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO9renderingyA2EmF">LayerConfiguration.Feature.rendering</a></code>
uses Places data to present it on the MapView, while <code><a href="../../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO13offlineSearchyA2EmF">LayerConfiguration.Feature.offlineSearch</a></code> uses
the same data to enable discoverability by name or category. Hence, features might have overlapping sets of enabled layer groups.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18LayerConfigurationV7FeatureO15detailRenderingyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/detailRendering"></a>
<a class="token" href="#/s:7heresdk18LayerConfigurationV7FeatureO15detailRenderingyA2EmF">detailRendering</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Additional rendering details like buildings. Only used for the MapView.
When not set, the data will be excluded when downloading offline regions or prefetching areas
that contain such data. However, during online usage such data may still be downloaded into the
cache and shown. Increase of 11-16% is to be expected for map size, in case of enabling this feature.</p>
<p>Feature enables following OCM layer groups:</p>
<ul>
<li>“detailed_rendering”</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case detailRendering</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18LayerConfigurationV7FeatureO10navigationyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/navigation"></a>
<a class="token" href="#/s:7heresdk18LayerConfigurationV7FeatureO10navigationyA2EmF">navigation</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Map data that is used for map matching during navigation. When not set,
navigation may not work properly when being used offline.
Increase of 5-7% is to be expected for map size, but pay attention, that this feature is depended on
other layer groups (e.g. routing), so, in total is takes about 21-29 % of map size.</p>
<p>Feature enables following OCM layer groups:</p>
<ul>
<li>“interop”</li>
<li>“rendering”</li>
<li>“navigation”</li>
<li>“routing”</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case navigation</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18LayerConfigurationV7FeatureO13offlineSearchyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/offlineSearch"></a>
<a class="token" href="#/s:7heresdk18LayerConfigurationV7FeatureO13offlineSearchyA2EmF">offlineSearch</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Map data that is used to search. When not set, the OfflineSearchEngine may not
work properly when being used offline.</p>
<p>Feature enables following OCM layer groups:</p>
<ul>
<li>“rendering”</li>
<li>“routing”</li>
<li>“search”</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case offlineSearch</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18LayerConfigurationV7FeatureO19offlineSearchGlobalyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/offlineSearchGlobal"></a>
<a class="token" href="#/s:7heresdk18LayerConfigurationV7FeatureO19offlineSearchGlobalyA2EmF">offlineSearchGlobal</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Map data used for global search indexing. This feature enables searches
across broader geographic areas and improves both performance and accuracy
by leveraging global search indices.
By default this feature is disabled.</p>
<p>Enables the HERE SDK to use the enhanced offline search algorithm for downloaded map regions when:</p>
<ul>
<li><code>OFFLINE_SEARCH_GLOBAL</code> is included in <code><a href="../../Structs/LayerConfiguration.html#/s:7heresdk18LayerConfigurationV15enabledFeaturesSayAC7FeatureOGvp">LayerConfiguration.enabledFeatures</a></code> and</li>
<li>downloaded map regions contain the required OCM layer groups listed below.</li>
</ul>
<p>Also enables the enhanced offline search algorithm for implicitly prefetched map content when:</p>
<ul>
<li><code>OFFLINE_SEARCH_GLOBAL</code> is included in <code><a href="../../Structs/LayerConfiguration.html#/s:7heresdk18LayerConfigurationV28implicitlyPrefetchedFeaturesSayAC7FeatureOGvp">LayerConfiguration.implicitlyPrefetchedFeatures</a></code> and</li>
<li>downloaded map regions (if present) contain the required OCM layer groups.</li>
</ul>
<p>Both options can be enabled together. However, if enabling the feature for
implicitly prefetched content, it is recommended to also enable it for
downloaded map regions to ensure consistent search behavior.</p>
<p><strong>Important</strong>: After enabling this feature, make sure to update the cached offline maps.
If the cached maps are not updated, the algorithm will either:</p>
<ol>
<li>Fall back to the stable offline search if <code>OFFLINE_SEARCH</code> is still included in <code><a href="../../Structs/LayerConfiguration.html#/s:7heresdk18LayerConfigurationV15enabledFeaturesSayAC7FeatureOGvp">LayerConfiguration.enabledFeatures</a></code>, or</li>
<li>Produce a <code>LAYERS_NOT_DOWNLOADED</code> error if the necessary layers are missing.</li>
</ol>
<p>To prevent excessive map size growth, it is recommended to enable only one of
<code>OFFLINE_SEARCH_GLOBAL</code> or <code>OFFLINE_SEARCH</code> at a time.</p>
<p>Enabling this feature increases storage requirements:</p>
<ul>
<li>Downloaded map region size by ~11–16% when enabled via <code><a href="../../Structs/LayerConfiguration.html#/s:7heresdk18LayerConfigurationV15enabledFeaturesSayAC7FeatureOGvp">LayerConfiguration.enabledFeatures</a></code>.</li>
<li>Map cache size by ~40–140% when enabled via <code><a href="../../Structs/LayerConfiguration.html#/s:7heresdk18LayerConfigurationV28implicitlyPrefetchedFeaturesSayAC7FeatureOGvp">LayerConfiguration.implicitlyPrefetchedFeatures</a></code>
(upper bound occurs for long routes, e.g., Paris → Rome).</li>
</ul>
<p>Feature enables following OCM layer groups:</p>
<ul>
<li>“search_global”</li>
<li>“search_data”</li>
</ul>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case offlineSearchGlobal</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18LayerConfigurationV7FeatureO14offlineRoutingyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/offlineRouting"></a>
<a class="token" href="#/s:7heresdk18LayerConfigurationV7FeatureO14offlineRoutingyA2EmF">offlineRouting</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Map data that is used to calculate routes. When not set, the OfflineRoutingEngine
may not work properly when being used offline.  Increase of 12-16.5% is to be expected for map size, but pay attention,
that this feature is depended on other layer groups (e.g. navigation), so, in total is takes about 33-45 % of map size.</p>
<p>Feature enables following OCM layer groups:</p>
<ul>
<li>“rendering”</li>
<li>“navigation”</li>
<li>“routing”</li>
<li>“interop”</li>
<li>“car_offline_routing”</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case offlineRouting</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18LayerConfigurationV7FeatureO9renderingyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/rendering"></a>
<a class="token" href="#/s:7heresdk18LayerConfigurationV7FeatureO9renderingyA2EmF">rendering</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A basic set of rendering features such as carto POIs. Increase of 16-22% is to be expected for map size, but pay attention,
that this feature is depended on other layer groups (e.g. navigation), so, in total is takes about 21-29 % of map size.</p>
<p>Feature enables following OCM layer groups:</p>
<ul>
<li>“rendering”</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case rendering</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18LayerConfigurationV7FeatureO5truckyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/truck"></a>
<a class="token" href="#/s:7heresdk18LayerConfigurationV7FeatureO5truckyA2EmF">truck</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Map data that is used to calculate truck routes. When not set,
the <code>OfflineRoutingEngine</code> may not work properly when being used to calculate truck routes.
It is also used for map matching during truck navigation and for vehicle restriction
visualization.
When not set, truck navigation may not work properly when being used offline.
Online truck navigation will still work when the device has an online connection.
Increase of 0.7-1.1% is to be expected for map size, in case of enabling this feature.
By default this feature is disabled.</p>
<p>Feature enables following OCM layer groups:</p>
<ul>
<li>“truck”</li>
<li>“long_truck_offline_routing”</li>
<li>“truck_offline_routing”</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case truck</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18LayerConfigurationV7FeatureO11landmarks3dyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/landmarks3d"></a>
<a class="token" href="#/s:7heresdk18LayerConfigurationV7FeatureO11landmarks3dyA2EmF">landmarks3d</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Map data that is used to render 3D landmarks. When not set, the data
will be excluded when downloading offline regions or prefetching areas that contain such data.
When the <code>landmarks</code> <code>MapFeature</code> is set to be visible for a <code><a href="sdk-for-ios-explore-api-reference-..-..-classes-mapscene">MapScene</a></code>, 3D landmarks will still be loaded and
visible during online usage. Increase of 2-3% is to be expected for map size, in case of enabling this feature.</p>
<p>3D landmark rendering is enabled by default in grayscale on normal,
logistics and topo schemes, and in textureless mode on lite schemes. However, when this map data feature is disabled,
the 3D landmark rendering for the above schemes will not work in offline mode with the downloaded map packages.
Feature enables following OCM layer groups:</p>
<ul>
<li>“landmarks”</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case landmarks3d</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18LayerConfigurationV7FeatureO2evyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/ev"></a>
<a class="token" href="#/s:7heresdk18LayerConfigurationV7FeatureO2evyA2EmF">ev</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Offline map data for <code><a href="sdk-for-ios-explore-api-reference-..-..-structs-evchargingstation">EVChargingStation</a></code>.</p>
<p>Feature enables following OCM layer groups:</p>
<ul>
<li>“ev_charging_station_rendering_premium”</li>
<li>“ev_charging_station_search_premium”</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case ev</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18LayerConfigurationV7FeatureO22truckServiceAttributesyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/truckServiceAttributes"></a>
<a class="token" href="#/s:7heresdk18LayerConfigurationV7FeatureO22truckServiceAttributesyA2EmF">truckServiceAttributes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Enables truck related attributes to be returned by Offline Search engine.
Feature enables following OCM layer groups:</p>
<ul>
<li>“truck_service_premium”</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case truckServiceAttributes</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18LayerConfigurationV7FeatureO21fuelStationAttributesyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/fuelStationAttributes"></a>
<a class="token" href="#/s:7heresdk18LayerConfigurationV7FeatureO21fuelStationAttributesyA2EmF">fuelStationAttributes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Enables fuel attributes to be returned by Offline Search engine.</p>
<p>Feature enables following OCM layer groups:</p>
<ul>
<li>“fueling_station_premium”</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case fuelStationAttributes</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18LayerConfigurationV7FeatureO17offlineBusRoutingyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/offlineBusRouting"></a>
<a class="token" href="#/s:7heresdk18LayerConfigurationV7FeatureO17offlineBusRoutingyA2EmF">offlineBusRouting</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Map data that is used to calculate bus routes.
When not set, the <code>OfflineRoutingEngine</code> may not be able to calculate routes with <code><a href="sdk-for-ios-explore-api-reference-..-..-structs-busoptions">BusOptions</a></code>.</p>
<p>Feature enables following OCM layer groups:</p>
<ul>
<li>“bus_offline_routing”</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case offlineBusRouting</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18LayerConfigurationV7FeatureO15junctionView3x4yA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/junctionView3x4"></a>
<a class="token" href="#/s:7heresdk18LayerConfigurationV7FeatureO15junctionView3x4yA2EmF">junctionView3x4</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Map data that provides junction view images and assets with aspect ratio 3x4.
This will also provide common assets that do not depend on specific aspect ratio.
By default this feature is disabled.</p>
<p>Feature enables following OCM layer groups:</p>
<ul>
<li>“junction_view_file_3x4”</li>
<li>“junction_view_asset_3x4”</li>
<li>“junction_view_asset_common”</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case junctionView3x4</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18LayerConfigurationV7FeatureO16junctionView16x9yA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/junctionView16x9"></a>
<a class="token" href="#/s:7heresdk18LayerConfigurationV7FeatureO16junctionView16x9yA2EmF">junctionView16x9</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Map data that provides junction view images and assets with aspect ratio 16x9.
This will also provide common assets that do not depend on specific aspect ratio.
By default this feature is disabled.</p>
<p>Feature enables following OCM layer groups:</p>
<ul>
<li>“junction_view_file_16x9”</li>
<li>“junction_view_asset_16x9”</li>
<li>“junction_view_asset_common”</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case junctionView16x9</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18LayerConfigurationV7FeatureO15junctionSign3x4yA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/junctionSign3x4"></a>
<a class="token" href="#/s:7heresdk18LayerConfigurationV7FeatureO15junctionSign3x4yA2EmF">junctionSign3x4</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Map data that provides junction sign images with aspect ratio 3x4.
By default this feature is disabled.</p>
<p>Feature enables following OCM layer groups:</p>
<ul>
<li>“junction_sign_file_3x4”</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case junctionSign3x4</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18LayerConfigurationV7FeatureO15junctionSign3x5yA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/junctionSign3x5"></a>
<a class="token" href="#/s:7heresdk18LayerConfigurationV7FeatureO15junctionSign3x5yA2EmF">junctionSign3x5</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Map data that provides junction sign images with aspect ratio 3x5.
By default this feature is disabled.</p>
<p>Feature enables following OCM layer groups:</p>
<ul>
<li>“junction_sign_file_3x5”</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case junctionSign3x5</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18LayerConfigurationV7FeatureO15junctionSign4x3yA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/junctionSign4x3"></a>
<a class="token" href="#/s:7heresdk18LayerConfigurationV7FeatureO15junctionSign4x3yA2EmF">junctionSign4x3</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Map data that provides junction sign images with aspect ratio 4x3.
By default this feature is disabled.</p>
<p>Feature enables following OCM layer groups:</p>
<ul>
<li>“junction_sign_file_4x3”</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case junctionSign4x3</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18LayerConfigurationV7FeatureO15junctionSign5x3yA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/junctionSign5x3"></a>
<a class="token" href="#/s:7heresdk18LayerConfigurationV7FeatureO15junctionSign5x3yA2EmF">junctionSign5x3</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Map data that provides junction sign images with aspect ratio 5x3.
By default this feature is disabled.
Feature enables following OCM layer groups:</p>
<ul>
<li>“junction_sign_file_5x3”</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case junctionSign5x3</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18LayerConfigurationV7FeatureO16junctionSign16x9yA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/junctionSign16x9"></a>
<a class="token" href="#/s:7heresdk18LayerConfigurationV7FeatureO16junctionSign16x9yA2EmF">junctionSign16x9</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Map data that provides junction sign images with aspect ratio 16x9.
By default this feature is disabled.</p>
<p>Feature enables following OCM layer groups:</p>
<ul>
<li>“junction_sign_file_16x9”</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case junctionSign16x9</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18LayerConfigurationV7FeatureO7terrainyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/terrain"></a>
<a class="token" href="#/s:7heresdk18LayerConfigurationV7FeatureO7terrainyA2EmF">terrain</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Map data that provides topography information.
The related map feature terrain with mode
hillshade is enabled by default on topo map schemes.
It is disabled by default on all other schemes.</p>
<p>Note that this change has performance implications, with additional data consumption and
impact on rendering frame rate.
If performance is a concern, this feature can be disabled from the application side when
loading the map scene.
However, when this map data feature is disabled,
the terrain rendering for the above schemes will not work in offline mode with the downloaded map packages.
Feature enables following OCM layer groups:</p>
<ul>
<li>“terrain”</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case terrain</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18LayerConfigurationV7FeatureO15detailedTerrainyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/detailedTerrain"></a>
<a class="token" href="#/s:7heresdk18LayerConfigurationV7FeatureO15detailedTerrainyA2EmF">detailedTerrain</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Map data that provides detailed topography information.
By default this feature is disabled.
Feature enables following OCM layer groups:</p>
<ul>
<li>“detailed_terrain”</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case detailedTerrain</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18LayerConfigurationV7FeatureO4adasyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/adas"></a>
<a class="token" href="#/s:7heresdk18LayerConfigurationV7FeatureO4adasyA2EmF">adas</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Map data which provides ADAS information which includes slope,
elevation and curvature information.
By default this feature is disabled.
Feature enables following OCM layer groups:</p>
<ul>
<li>“adas”</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case adas</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18LayerConfigurationV7FeatureO8ehorizonyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/ehorizon"></a>
<a class="token" href="#/s:7heresdk18LayerConfigurationV7FeatureO8ehorizonyA2EmF">ehorizon</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Map data which provides information about the parts of foreign segments in a tile,
where a foreign segment is a segment that is stored in another tile but intersects the current tile.
By default this feature is disabled.
Feature enables following OCM layer groups:</p>
<ul>
<li>“ehorizon”</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case ehorizon</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18LayerConfigurationV7FeatureO10rdsTrafficyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/rdsTraffic"></a>
<a class="token" href="#/s:7heresdk18LayerConfigurationV7FeatureO10rdsTrafficyA2EmF">rdsTraffic</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Map data that provides traffic broadcast functionality using RDS-TMC format.
It should be used when there is no internet connection, so that the routing module can utilize
traffic data coming over the radio channel to build a route in the offline mode.
Feature enables following OCM layer groups:</p>
<ul>
<li>“traffic”</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case rdsTraffic</code></pre>
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



</div>
`
}</HTMLBlock>
