---
title: "prefetch abstract method"
slug: "sdk-for-flutter-navigate-prefetcher-polygonprefetcher-prefetch"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- prefetch.html -->


<div>
<h1>prefetch abstract method</h1></div>

<a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>
prefetch(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-core-geopolygon-class">GeoPolygon</a> geoPolygon, </li>
<li><a href="sdk-for-flutter-navigate-prefetcher-prefetchstatuslistener-class">PrefetchStatusListener</a> callback</li>
</ol>)

      

    

<p>Prefetches map data for an area bounded by geo polygon.</p>
<p>After the operation is finished <a href="sdk-for-flutter-navigate-prefetcher-prefetchstatuslistener-oncomplete">PrefetchStatusListener.onComplete</a> is
invoked on the main thread. Progress is reported by invocation
of <a href="sdk-for-flutter-navigate-prefetcher-prefetchstatuslistener-onprogress">PrefetchStatusListener.onProgress</a> on the main thread.
If there is not enough space left in the cache to store needed tiles, operation will
fail with <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError.notEnoughSpace</a>. To increase cache size, use
<a href="sdk-for-flutter-navigate-core-engine-sdkoptions-cachesizeinbytes">SDKOptions.cacheSizeInBytes</a> API.</p>
<p>To control list of map content features for area prefetch, use <a href="sdk-for-flutter-navigate-core-engine-layerconfiguration-enabledfeatures">LayerConfiguration.enabledFeatures</a>.</p>
<p>To prefetch map data within user-defined circular area around a given location:</p>
<ol>
<li>Create a GeoCircle using the given location and radius.</li>
<li>Create a GeoPolygon using the GeoCircle.</li>
<li>Pass the afroementioned GeoPolygon to the sdk.prefetcher.PolygonPrefetcher.prefetch API.
Usage:
GeoCircle geoCircle = GeoCircle(location, radius);
GeoPolygon geoPolygon = GeoPolygon.withGeoCircle(geoCircle);</li>
</ol>
<ul>
<li>
<p><code>geoPolygon</code> Area to prefetch map data for.</p>
</li>
<li>
<p><code>callback</code> Callback that is triggered to report progress and the result of prefetch.</p>
</li>
</ul>
<p>Returns <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate execution of the task.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle prefetch(GeoPolygon geoPolygon, PrefetchStatusListener callback);</code></pre>

 



</div>
`
}</HTMLBlock>
