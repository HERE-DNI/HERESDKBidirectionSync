---
title: "sdk-for-ios-navigate-api-reference-classes-routeprefetcher"
slug: "sdk-for-ios-navigate-api-reference-classes-routeprefetcher"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/RoutePrefetcher"></a>
<a title="RoutePrefetcher Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-routing">Routing</a>
<img alt="" id="carat" src="/carat.png"/>
        RoutePrefetcher Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>RoutePrefetcher</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">RoutePrefetcher</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">RoutePrefetcher</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">RoutePrefetcher</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Supports downloading of map data - in advance - into the cache to optimize temporary offline
use cases that rely on cached map data. This allows scenarios such as navigation to work in a
specific area reliably even though the network might be offline at that time.
Please note, this class puts data in the map cache, which has its own size constraints,
and extensive usage may start evicting old cached data.
Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15RoutePrefetcherCyAcA15SDKNativeEngineCcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:)"></a>
<a class="token" href="#/s:7heresdk15RoutePrefetcherCyAcA15SDKNativeEngineCcfc">init(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a RoutePrefetcher instance for a given <code><a href="sdk-for-ios-navigate-api-reference-classes-sdknativeengine">SDKNativeEngine</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="n">_</span> <span class="nv">sdkEngine</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-sdknativeengine">SDKNativeEngine</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>sdkEngine</em>
</code>
</td>
<td>
<div>
<p>Instance of an existing SDKEngine.</p>
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
<a name="/s:7heresdk15RoutePrefetcherC28prefetchCorridorLengthMeterss5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/prefetchCorridorLengthMeters"></a>
<a class="token" href="#/s:7heresdk15RoutePrefetcherC28prefetchCorridorLengthMeterss5Int32Vvp">prefetchCorridorLengthMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The length of the corridor along the route in front of the car which will be used to prefetch data.
Upper limit for length is 50000 meters, when the requested length is greater than upper limit, then 50000 meters set.
Lower limit for length is 1000 meters, when the requested length is less than lower limit, then 1000 meters set.
The route corridor has a default length of 10 km and a width of 5 km.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">prefetchCorridorLengthMeters</span><span class="p">:</span> <span class="kt">Int32</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15RoutePrefetcherC32prefetchAroundLocationWithRadius07currentF014radiusInMetersyAA14GeoCoordinatesV_SdSgtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/prefetchAroundLocationWithRadius(currentLocation:radiusInMeters:)"></a>
<a class="token" href="#/s:7heresdk15RoutePrefetcherC32prefetchAroundLocationWithRadius07currentF014radiusInMetersyAA14GeoCoordinatesV_SdSgtF">prefetchAroundLocationWithRadius(currentLocation:<wbr/>radiusInMeters:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Prefetches map data within a user-defined circular area around a given location.
The radius, specified in meters, must be between 1 km and 50 km.
If <code>nil</code> is passed as the radius, a default value of 2 km is used.
It is recommended to call this method once before starting navigation
to ensure a smooth experience.</p>
<p>To control list of map content features for area prefetch, use <code><a href="../Structs/LayerConfiguration.html#/s:7heresdk18LayerConfigurationV15enabledFeaturesSayAC7FeatureOGvp">LayerConfiguration.enabledFeatures</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.27.0. Please use PolygonPrefetcher.prefetch(...﹚ instead.")</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">prefetchAroundLocationWithRadius</span><span class="p">(</span><span class="nv">currentLocation</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">,</span> <span class="nv">radiusInMeters</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>currentLocation</em>
</code>
</td>
<td>
<div>
<p>The center of the circle to prefetch data within.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>radiusInMeters</em>
</code>
</td>
<td>
<div>
<p>The radius of the circle to prefetch data within.</p>
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
<a name="/s:7heresdk15RoutePrefetcherC014prefetchAroundB11OnIntervals9navigatoryAA17NavigatorProtocol_p_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/prefetchAroundRouteOnIntervals(navigator:)"></a>
<a class="token" href="#/s:7heresdk15RoutePrefetcherC014prefetchAroundB11OnIntervals9navigatoryAA17NavigatorProtocol_p_tF">prefetchAroundRouteOnIntervals(navigator:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Prefetches map data within a corridor along the route, that is currently set for the
provided <code><a href="sdk-for-ios-navigate-api-reference-protocols-navigatorprotocol">NavigatorProtocol</a></code> instance. If no route is set, no data will be prefetched.
The route corridor defaults to a length of 10 km and a width of 5 km.
To prefetch the whole route before navigation has been started see <code><a href="../Classes/RoutePrefetcher.html#/s:7heresdk15RoutePrefetcherC19prefetchGeoCorridor8corridor8callbackAA10TaskHandle_pAA0eF0V_AA22PrefetchStatusListener_ptF">RoutePrefetcher.prefetchGeoCorridor(...)</a></code>.
Map data is prefetched only in discrete intervals. Prefetching starts 1 km before reaching the
end of the current corridor. Prefetching happens based on the current map-matched location - as
indicated by the <code><a href="sdk-for-ios-navigate-api-reference-structs-routeprogress">RouteProgress</a></code> event.
This method should be called right after navigation has started.
In case of default prefetch length first prefetching will start after traveling a distance
of 9 km along the route.</p>
<p>To control list of map content features for prefetch, use <code><a href="../Structs/LayerConfiguration.html#/s:7heresdk18LayerConfigurationV15enabledFeaturesSayAC7FeatureOGvp">LayerConfiguration.enabledFeatures</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">prefetchAroundRouteOnIntervals</span><span class="p">(</span><span class="nv">navigator</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-navigatorprotocol">NavigatorProtocol</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>navigator</em>
</code>
</td>
<td>
<div>
<p>The <code><a href="sdk-for-ios-navigate-api-reference-protocols-navigatorprotocol">NavigatorProtocol</a></code> to listen for Route Progress to prefetch data ahead.</p>
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
<a name="/s:7heresdk15RoutePrefetcherC018stopPrefetchAroundB0yyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/stopPrefetchAroundRoute()"></a>
<a class="token" href="#/s:7heresdk15RoutePrefetcherC018stopPrefetchAroundB0yyF">stopPrefetchAroundRoute()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Stops listening <code><a href="sdk-for-ios-navigate-api-reference-protocols-navigatorprotocol">NavigatorProtocol</a></code> passed to <code><a href="../Classes/RoutePrefetcher.html#/s:7heresdk15RoutePrefetcherC014prefetchAroundB11OnIntervals9navigatoryAA17NavigatorProtocol_p_tF">RoutePrefetcher.prefetchAroundRouteOnIntervals(...)</a></code>
for route progress events and stops prefetching data along the current route.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">stopPrefetchAroundRoute</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15RoutePrefetcherC19prefetchGeoCorridor8corridor8callbackAA10TaskHandle_pAA0eF0V_AA22PrefetchStatusListener_ptF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/prefetchGeoCorridor(corridor:callback:)"></a>
<a class="token" href="#/s:7heresdk15RoutePrefetcherC19prefetchGeoCorridor8corridor8callbackAA10TaskHandle_pAA0eF0V_AA22PrefetchStatusListener_ptF">prefetchGeoCorridor(corridor:<wbr/>callback:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Prefetch tiles for a given geo-corridor. A geo-corridor can easily be created from a route with <code><a href="../Classes/Route.html#/s:7heresdk5RouteC8geometryAA11GeoPolylineVvp">Route.geometry</a></code>
so navigation on this route is possible in offline cases.
Please note, tiles will be saved in mutable cache so when there is not enough space to accommodate new
prefetched tiles <code><a href="../Enums/MapLoaderError.html#/s:7heresdk14MapLoaderErrorO14notEnoughSpaceyA2CmF">MapLoaderError.notEnoughSpace</a></code> is returned.
When updating mutable cache, all tiles will be unusable. Please re-download the geoCorridor again.
Please also note, any route calculation may not possible on prefetched tiles.</p>
<p>To control list of map content features for corridor prefetch, use <code><a href="../Structs/LayerConfiguration.html#/s:7heresdk18LayerConfigurationV15enabledFeaturesSayAC7FeatureOGvp">LayerConfiguration.enabledFeatures</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">prefetchGeoCorridor</span><span class="p">(</span><span class="nv">corridor</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geocorridor">GeoCorridor</a></span><span class="p">,</span> <span class="nv">callback</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-prefetchstatuslistener">PrefetchStatusListener</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>corridor</em>
</code>
</td>
<td>
<div>
<p>indicates <code><a href="sdk-for-ios-navigate-api-reference-structs-geocorridor">GeoCorridor</a></code> that can be constructed from the route.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>callback</em>
</code>
</td>
<td>
<div>
<p>is invoked to report progress and the result of prefetch. After operation is
finished, <code>onComplete(...)</code> is invoked on the main thread. Progress is reported by invocation
of <code>onProgress(...)</code> on the main thread.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Handle that will be used to manipulate the execution of the task.</p>
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
