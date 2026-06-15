---
title: "prefetchGeoCorridor abstract method"
slug: "sdk-for-flutter-navigate-prefetcher-routeprefetcher-prefetchgeocorridor"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- prefetchGeoCorridor.html -->


<div>
<h1>prefetchGeoCorridor abstract method</h1></div>

<a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>
prefetchGeoCorridor(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-core-geocorridor-class">GeoCorridor</a> corridor, </li>
<li><a href="sdk-for-flutter-navigate-prefetcher-prefetchstatuslistener-class">PrefetchStatusListener</a> callback</li>
</ol>)

      

    

<p>Prefetch tiles for a given geo-corridor.</p>
<p>A geo-corridor can easily be created from a route with <a href="sdk-for-flutter-navigate-routing-route-geometry">Route.geometry</a>
so navigation on this route is possible in offline cases.
Please note, tiles will be saved in mutable cache so when there is not enough space to accommodate new
prefetched tiles <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError.notEnoughSpace</a> is returned.
When updating mutable cache, all tiles will be unusable. Please re-download the geoCorridor again.
Please also note, any route calculation may not possible on prefetched tiles.</p>
<p>To control list of map content features for corridor prefetch, use <a href="sdk-for-flutter-navigate-core-engine-layerconfiguration-enabledfeatures">LayerConfiguration.enabledFeatures</a>.</p>
<ul>
<li>
<p><code>corridor</code> indicates <code>GeoCorridor</code> that can be constructed from the route.</p>
</li>
<li>
<p><code>callback</code> is invoked to report progress and the result of prefetch. After operation is
finished, <a href="sdk-for-flutter-navigate-prefetcher-prefetchstatuslistener-oncomplete">PrefetchStatusListener.onComplete</a> is invoked on the main thread. Progress is reported by invocation
of <a href="sdk-for-flutter-navigate-prefetcher-prefetchstatuslistener-onprogress">PrefetchStatusListener.onProgress</a> on the main thread.</p>
</li>
</ul>
<p>Returns <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle prefetchGeoCorridor(GeoCorridor corridor, PrefetchStatusListener callback);</code></pre>

 



</div>
`
}</HTMLBlock>
