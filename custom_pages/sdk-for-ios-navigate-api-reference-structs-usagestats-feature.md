---
title: "sdk-for-ios-navigate-api-reference-structs-usagestats-feature"
slug: "sdk-for-ios-navigate-api-reference-structs-usagestats-feature"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Enum/Feature"></a>
<a title="Feature Enumeration Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-core">Core</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-structs-usagestats">UsageStats</a>
<img alt="" id="carat" src="/carat.png"/>
        Feature Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>Feature</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">Feature</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
<p>Represents the feature enum associated with the gathered usage stats.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10UsageStatsV7FeatureO17detailedRenderingyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/detailedRendering"></a>
<a class="token" href="#/s:7heresdk10UsageStatsV7FeatureO17detailedRenderingyA2EmF">detailedRendering</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents network traffic statistics for online usage corresponding to the
<code><a href="../../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO15detailRenderingyA2EmF">LayerConfiguration.Feature.detailRendering</a></code> layer configuration.
Counted when data for the corresponding layer is requested by the application
by performing one of the following actions:</p>
<ul>
<li>Pan the map view to areas that have not been cached, prefetched or installed before.</li>
<li>Use <code><a href="sdk-for-ios-navigate-api-reference-classes-mapdownloader">MapDownloader</a></code> to download and install a <code><a href="sdk-for-ios-navigate-api-reference-structs-region">Region</a></code>.</li>
<li>Prefetch map data into the map cache with the <code><a href="sdk-for-ios-navigate-api-reference-classes-routeprefetcher">RoutePrefetcher</a></code> for areas that
have not been cached, prefetched or installed before.
Note that you can enable or disable this feature by calling:
<code>LayerConfiguration.enabledFeatures(..) or LayerConfiguration.implicitlyPrefetchedFeatures()</code>.</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">detailedRendering</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10UsageStatsV7FeatureO11evRenderingyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/evRendering"></a>
<a class="token" href="#/s:7heresdk10UsageStatsV7FeatureO11evRenderingyA2EmF">evRendering</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents network traffic statistics for online usage corresponding to the
“ev_charging_station_rendering_premium” layer group, enabled with <code><a href="../../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO2evyA2EmF">LayerConfiguration.Feature.ev</a></code>.
Note, that <code><a href="../../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO2evyA2EmF">LayerConfiguration.Feature.ev</a></code> also enables “ev_charging_station_search_premium” layer group,
which is represented with [UsageStats.Feature.EV_SEARCH].
Counted when data for the corresponding layer is requested by the application
by performing one of the following actions:</p>
<ul>
<li>Pan the map view to areas that have not been cached, prefetched or installed before.</li>
<li>Use <code><a href="sdk-for-ios-navigate-api-reference-classes-mapdownloader">MapDownloader</a></code> to download and install a <code><a href="sdk-for-ios-navigate-api-reference-structs-region">Region</a></code>.</li>
<li>Prefetch map data into the map cache with the <code><a href="sdk-for-ios-navigate-api-reference-classes-routeprefetcher">RoutePrefetcher</a></code> for areas that
have not been cached, prefetched or installed before.
As of now, this layer cannot be turned off.</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">evRendering</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10UsageStatsV7FeatureO8evSearchyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/evSearch"></a>
<a class="token" href="#/s:7heresdk10UsageStatsV7FeatureO8evSearchyA2EmF">evSearch</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents network traffic statistics for online usage corresponding to the
“ev_charging_station_search_premium” layer group, enabled with <code><a href="../../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO2evyA2EmF">LayerConfiguration.Feature.ev</a></code>.
Note, that <code><a href="../../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO2evyA2EmF">LayerConfiguration.Feature.ev</a></code> also enables “ev_charging_station_rendering_premium” layer group,
which is represented with [UsageStats.Feature.EV_RENDERING].
Counted when data for the corresponding layer is requested by the application
by performing one of the following actions:</p>
<ul>
<li>Pan the map view to areas that have not been cached, prefetched or installed before.</li>
<li>Use <code><a href="sdk-for-ios-navigate-api-reference-classes-mapdownloader">MapDownloader</a></code> to download and install a <code><a href="sdk-for-ios-navigate-api-reference-structs-region">Region</a></code>.</li>
<li>Prefetch map data into the map cache with the <code><a href="sdk-for-ios-navigate-api-reference-classes-routeprefetcher">RoutePrefetcher</a></code> for areas that
have not been cached, prefetched or installed before.
As of now, this layer cannot be turned off.</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">evSearch</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10UsageStatsV7FeatureO10navigationyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/navigation"></a>
<a class="token" href="#/s:7heresdk10UsageStatsV7FeatureO10navigationyA2EmF">navigation</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents network traffic statistics for online usage corresponding to the “adas”, “ehorizon”, “interop”, “isa” OCM layers.
In addition, it is also tracking the following layer configurations:</p>
<ul>
<li><code><a href="../../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO10navigationyA2EmF">LayerConfiguration.Feature.navigation</a></code></li>
<li><code><a href="../../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO15junctionView3x4yA2EmF">LayerConfiguration.Feature.junctionView3x4</a></code></li>
<li><code><a href="../../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO16junctionView16x9yA2EmF">LayerConfiguration.Feature.junctionView16x9</a></code></li>
<li><code><a href="../../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO15junctionSign3x4yA2EmF">LayerConfiguration.Feature.junctionSign3x4</a></code></li>
<li><code><a href="../../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO15junctionSign3x5yA2EmF">LayerConfiguration.Feature.junctionSign3x5</a></code></li>
<li><code><a href="../../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO15junctionSign4x3yA2EmF">LayerConfiguration.Feature.junctionSign4x3</a></code></li>
<li><code><a href="../../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO15junctionSign5x3yA2EmF">LayerConfiguration.Feature.junctionSign5x3</a></code></li>
<li><code><a href="../../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO16junctionSign16x9yA2EmF">LayerConfiguration.Feature.junctionSign16x9</a></code>
Counted when data for the corresponding layer is requested by the application
by performing one of the following actions:</li>
<li>Pan the map view to areas that have not been cached, prefetched or installed before.</li>
<li>Use <code><a href="sdk-for-ios-navigate-api-reference-classes-mapdownloader">MapDownloader</a></code> to download and install a <code><a href="sdk-for-ios-navigate-api-reference-structs-region">Region</a></code>.</li>
<li>Prefetch map data into the map cache with the <code><a href="sdk-for-ios-navigate-api-reference-classes-routeprefetcher">RoutePrefetcher</a></code> for areas that
have not been cached, prefetched or installed before.</li>
<li>Using online navigation when the requested data is not cached, prefetched, or installed before.
As of now, the above listed OCM layers cannot be turned off except for those that are exposed as layer configuration.</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">navigation</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10UsageStatsV7FeatureO6placesyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/places"></a>
<a class="token" href="#/s:7heresdk10UsageStatsV7FeatureO6placesyA2EmF">places</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents network traffic statistics for places search.
This is legacy statistic which is now replaced by <code><a href="../../Structs/UsageStats/Feature.html#/s:7heresdk10UsageStatsV7FeatureO12searchOnlineyA2EmF">UsageStats.Feature.searchOnline</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">places</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10UsageStatsV7FeatureO10rdsTrafficyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/rdsTraffic"></a>
<a class="token" href="#/s:7heresdk10UsageStatsV7FeatureO10rdsTrafficyA2EmF">rdsTraffic</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents network traffic statistics for online usage corresponding to the
<code><a href="../../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO10rdsTrafficyA2EmF">LayerConfiguration.Feature.rdsTraffic</a></code> layer configuration.
Counted when data for the corresponding layer is requested by the application
by performing one of the following actions:</p>
<ul>
<li>Pan the map view to areas that have not been cached, prefetched or installed before.</li>
<li>Use <code><a href="sdk-for-ios-navigate-api-reference-classes-mapdownloader">MapDownloader</a></code> to download and install a <code><a href="sdk-for-ios-navigate-api-reference-structs-region">Region</a></code>.</li>
<li>Prefetch map data into the map cache with the <code><a href="sdk-for-ios-navigate-api-reference-classes-routeprefetcher">RoutePrefetcher</a></code> for areas that
have not been cached, prefetched or installed before.
Note that you can enable or disable this feature by calling:
<code>LayerConfiguration.enabledFeatures(..) or LayerConfiguration.implicitlyPrefetchedFeatures()</code>.</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">rdsTraffic</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10UsageStatsV7FeatureO9renderingyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/rendering"></a>
<a class="token" href="#/s:7heresdk10UsageStatsV7FeatureO9renderingyA2EmF">rendering</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents network traffic statistics for online usage corresponding to the
<code><a href="../../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO9renderingyA2EmF">LayerConfiguration.Feature.rendering</a></code> layer configuration.
Counted when data for the corresponding layer is requested by the application
by performing one of the following actions:</p>
<ul>
<li>Pan the map view to areas that have not been cached, prefetched or installed before.</li>
<li>Use <code><a href="sdk-for-ios-navigate-api-reference-classes-mapdownloader">MapDownloader</a></code> to download and install a <code><a href="sdk-for-ios-navigate-api-reference-structs-region">Region</a></code>.</li>
<li>Prefetch map data into the map cache with the <code><a href="sdk-for-ios-navigate-api-reference-classes-routeprefetcher">RoutePrefetcher</a></code> for areas that
have not been cached, prefetched or installed before.
Note that you can enable or disable this feature by calling:
<code>LayerConfiguration.enabledFeatures(..) or LayerConfiguration.implicitlyPrefetchedFeatures()</code>.</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">rendering</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10UsageStatsV7FeatureO6routeryA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/router"></a>
<a class="token" href="#/s:7heresdk10UsageStatsV7FeatureO6routeryA2EmF">router</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents network traffic statistics for online usage corresponding to the
<code><a href="sdk-for-ios-navigate-api-reference-classes-routingengine">RoutingEngine</a></code>.
Includes the following transaction counts and APIs:</p>
<ul>
<li><strong>Routing Car, Bicycle, Pedestrian</strong> with HRN <code>hrn:here:service::olp-here:routing-8:base</code> counted with the use of
<code>RoutingEngine with CarOptions,BicycleOptions or PedestrianOptions</code>.</li>
<li><strong>Routing Scooter</strong> with HRN <code>hrn:here:service::olp-here:routing-8:scooter</code> counted with the use of <code>RoutingEngine with ScooterOptions</code></li>
<li><strong>Routing Taxi</strong> with HRN <code>hrn:here:service::olp-here:routing-8:taxi</code> counted with the use of <code>RoutingEngine with TaxiOptions</code></li>
<li><strong>Routing Truck</strong> with HRN <code>hrn:here:service::olp-here:routing-8:truck</code> counted with the use of <code>RoutingEngine with TruckOptions</code></li>
<li><strong>Time-Aware Routing</strong> with HRN <code>hrn:here:service::olp-here:routing-8:traffic</code> counted with the use of
<code>RouteOptions with arrivalTime or departureTime</code></li>
<li><strong>Routing EV</strong> with HRN <code>hrn:here:service::olp-here:routing-8:ev</code> counted with the use of <code>RoutingEngine with EVTRuckOptions
or EVCarOptions and evCarOptions.ensureReachability =</code>true<code>.</code></li>
<li><strong>Route Import</strong> with HRN <code>hrn:here:service::olp-here:routing-8:import</code> counted with the use of <code>RoutingEngine.importRoutes(...)</code></li>
<li><strong>Toll Cost</strong> with HRN <code>hrn:here:service::olp-here:routing-8:tolls</code> counted with the use of <code>RoutingEngine with RouteOptions.enableTolls</code></li>
<li><strong>Routing Bus</strong> with HRN <code>hrn:here:service::olp-here:routing-8:bus</code> counted with the use of <code>RoutingEngine with BusOptions</code></li>
<li><strong>Isoline Routing</strong> with HRN <code>hrn:here:service::olp-here:isoline-routing-8</code> counted with the use of <code>RoutingEngine with IsolineOptions</code></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">router</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10UsageStatsV7FeatureO7routingyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/routing"></a>
<a class="token" href="#/s:7heresdk10UsageStatsV7FeatureO7routingyA2EmF">routing</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents network traffic statistics for online usage corresponding to the
following layer configurations:</p>
<ul>
<li><code><a href="../../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO14offlineRoutingyA2EmF">LayerConfiguration.Feature.offlineRouting</a></code></li>
<li><code><a href="../../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO17offlineBusRoutingyA2EmF">LayerConfiguration.Feature.offlineBusRouting</a></code>
Counted when data for the corresponding layer is requested by the application
by performing one of the following actions:</li>
<li>Pan the map view to areas that have not been cached, prefetched or installed before.</li>
<li>Use <code><a href="sdk-for-ios-navigate-api-reference-classes-mapdownloader">MapDownloader</a></code> to download and install a <code><a href="sdk-for-ios-navigate-api-reference-structs-region">Region</a></code>.</li>
<li>Prefetch map data into the map cache with the <code><a href="sdk-for-ios-navigate-api-reference-classes-routeprefetcher">RoutePrefetcher</a></code> for areas that
have not been cached, prefetched or installed before.
Note that you can enable or disable this feature by calling:
<code>LayerConfiguration.enabledFeatures(..) or LayerConfiguration.implicitlyPrefetchedFeatures()</code>.</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">routing</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10UsageStatsV7FeatureO10satellitesyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/satellites"></a>
<a class="token" href="#/s:7heresdk10UsageStatsV7FeatureO10satellitesyA2EmF">satellites</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents network traffic statistics to show satellite map scheme.
This includes a <strong>Raster Tile Base</strong> transaction count with HRN <code>hrn:here:service::olp-here:rendering-raster-tiles-3:base</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">satellites</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10UsageStatsV7FeatureO6searchyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/search"></a>
<a class="token" href="#/s:7heresdk10UsageStatsV7FeatureO6searchyA2EmF">search</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents network traffic statistics for online usage corresponding to the
“search”, “ev_charging_station_search_premium”, “fueling_station_premium” OCM layers.
Counted when data for the corresponding layer is requested by the application
by performing one of the following actions:</p>
<ul>
<li>Pan the map view to areas that have not been cached, prefetched or installed before.</li>
<li>Use <code><a href="sdk-for-ios-navigate-api-reference-classes-mapdownloader">MapDownloader</a></code> to download and install a <code><a href="sdk-for-ios-navigate-api-reference-structs-region">Region</a></code>.</li>
<li>Prefetch map data into the map cache with the <code><a href="sdk-for-ios-navigate-api-reference-classes-routeprefetcher">RoutePrefetcher</a></code> for areas that
have not been cached, prefetched or installed before.
As of now, these layers cannot be turned off.</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">search</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10UsageStatsV7FeatureO12searchOnlineyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/searchOnline"></a>
<a class="token" href="#/s:7heresdk10UsageStatsV7FeatureO12searchOnlineyA2EmF">searchOnline</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents network traffic statistics for online usage corresponding to the <code><a href="sdk-for-ios-navigate-api-reference-classes-searchengine">SearchEngine</a></code>.
Includes the following transaction counts and APIs:</p>
<ul>
<li><strong>Discover/Search</strong> with HRN <code>hrn:here:service::olp-here:search-opensearch-1</code> counted with the use of <code>SearchEngine textquery search</code></li>
<li><strong>Geocode &amp; Reverse Geocode</strong> with HRN <code>hrn:here:service::olp-here:geocode-7</code> counted with the use of <code>SearchEngine addressQuery &amp;
GeoCoordinates search</code></li>
<li><strong>Autosuggest</strong> with HRN <code>hrn:here:service::olp-here:search-autosuggest-7</code> counted with the use of <code>SearchEngine suggest</code></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">searchOnline</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10UsageStatsV7FeatureO7transityA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/transit"></a>
<a class="token" href="#/s:7heresdk10UsageStatsV7FeatureO7transityA2EmF">transit</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents network traffic statistics for online usage corresponding to the
“transit” OCM layer.
Counted when data for the corresponding layer is requested by the application
by performing one of the following actions:</p>
<ul>
<li>Pan the map view to areas that have not been cached, prefetched or installed before.</li>
<li>Use <code><a href="sdk-for-ios-navigate-api-reference-classes-mapdownloader">MapDownloader</a></code> to download and install a <code><a href="sdk-for-ios-navigate-api-reference-structs-region">Region</a></code>.</li>
<li>Prefetch map data into the map cache with the <code><a href="sdk-for-ios-navigate-api-reference-classes-routeprefetcher">RoutePrefetcher</a></code> for areas that
have not been cached, prefetched or installed before.
As of now, this layer cannot be turned off.</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">transit</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10UsageStatsV7FeatureO20transitRoutingEngineyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/transitRoutingEngine"></a>
<a class="token" href="#/s:7heresdk10UsageStatsV7FeatureO20transitRoutingEngineyA2EmF">transitRoutingEngine</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents network traffic statistics for online usage corresponding to the <code><a href="sdk-for-ios-navigate-api-reference-classes-transitroutingengine">TransitRoutingEngine</a></code>.
This includes a <strong>Public Transit</strong> transaction count with HRN: <code>hrn:here:service::olp-here:transit-8</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">transitRoutingEngine</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10UsageStatsV7FeatureO7trafficyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/traffic"></a>
<a class="token" href="#/s:7heresdk10UsageStatsV7FeatureO7trafficyA2EmF">traffic</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents network traffic statistics for online usage corresponding to the
calls of <code><a href="sdk-for-ios-navigate-api-reference-classes-trafficengine">TrafficEngine</a></code>. All calls to <code><a href="sdk-for-ios-navigate-api-reference-classes-trafficengine">TrafficEngine</a></code> result in transaction counts for
HRN <code>hrn:here:service::olp-here:traffic-api-7:standard</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">traffic</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10UsageStatsV7FeatureO18trafficVectorTilesyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/trafficVectorTiles"></a>
<a class="token" href="#/s:7heresdk10UsageStatsV7FeatureO18trafficVectorTilesyA2EmF">trafficVectorTiles</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents network traffic statistics for traffic vector tiles.
This includes a <strong>Traffic vector tile</strong> transaction count with HRN: <code>hrn:here:service::olp-here:traffic-vector-tiles-2</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">trafficVectorTiles</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10UsageStatsV7FeatureO5truckyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/truck"></a>
<a class="token" href="#/s:7heresdk10UsageStatsV7FeatureO5truckyA2EmF">truck</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents network traffic statistics for online usage corresponding to the
<code><a href="../../Structs/LayerConfiguration/Feature.html#/s:7heresdk18LayerConfigurationV7FeatureO5truckyA2EmF">LayerConfiguration.Feature.truck</a></code> layer configuration.
Counted when data for the corresponding layer is requested by the application
by performing one of the following actions:</p>
<ul>
<li>Pan the map view to areas that have not been cached, prefetched or installed before.</li>
<li>Use <code><a href="sdk-for-ios-navigate-api-reference-classes-mapdownloader">MapDownloader</a></code> to download and install a <code><a href="sdk-for-ios-navigate-api-reference-structs-region">Region</a></code>.</li>
<li>Prefetch map data into the map cache with the <code><a href="sdk-for-ios-navigate-api-reference-classes-routeprefetcher">RoutePrefetcher</a></code> for areas that
have not been cached, prefetched or installed before.
Note that you can enable or disable this feature by calling:
<code>LayerConfiguration.enabledFeatures(..) or LayerConfiguration.implicitlyPrefetchedFeatures()</code>.</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">truck</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10UsageStatsV7FeatureO11vectorTilesyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/vectorTiles"></a>
<a class="token" href="#/s:7heresdk10UsageStatsV7FeatureO11vectorTilesyA2EmF">vectorTiles</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents network traffic statistics for online usage corresponding to the vector tiles.
This includes a <strong>Vector tile</strong> transaction count with HRN: <code>hrn:here:service::olp-here:rendering-vector-tiles-2</code>.
This statistic is only counted for the HERE SDK (Explore) when showing the map view.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">vectorTiles</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10UsageStatsV7FeatureO5otheryA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/other"></a>
<a class="token" href="#/s:7heresdk10UsageStatsV7FeatureO5otheryA2EmF">other</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents network traffic statistics for feature that doesn’t fit into other categories.
Some examples include:</p>
<ul>
<li>Authentication</li>
<li>Analytics</li>
<li>Any feature not mapped in the existing list.</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">other</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10UsageStatsV7FeatureO11positioningyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/positioning"></a>
<a class="token" href="#/s:7heresdk10UsageStatsV7FeatureO11positioningyA2EmF">positioning</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents network traffic statistics for Here Positioning.
This includes a <strong>Network Positioning</strong> transaction count with HRN <code>hrn:here:service::olp-here:positioning-2</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">positioning</span></code></pre>
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
}</HTMLBlock>
