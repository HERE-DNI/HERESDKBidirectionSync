---
title: "prefetchAroundRouteOnIntervals abstract method"
slug: "sdk-for-flutter-navigate-prefetcher-routeprefetcher-prefetcharoundrouteonintervals"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- prefetchAroundRouteOnIntervals.html -->


<div>
<h1>prefetchAroundRouteOnIntervals abstract method</h1></div>

void
prefetchAroundRouteOnIntervals(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-navigatorinterface-class">NavigatorInterface</a> navigator</li>
</ol>)

      

    

<p>Prefetches map data within a corridor along the route, that is currently set for the
provided <a href="sdk-for-flutter-navigate-navigation-navigatorinterface-class">NavigatorInterface</a> instance.</p>
<p>If no route is set, no data will be prefetched.
The route corridor defaults to a length of 10 km and a width of 5 km.
To prefetch the whole route before navigation has been started see <a href="sdk-for-flutter-navigate-prefetcher-routeprefetcher-prefetchgeocorridor">RoutePrefetcher.prefetchGeoCorridor</a>.
Map data is prefetched only in discrete intervals. Prefetching starts 1 km before reaching the
end of the current corridor. Prefetching happens based on the current map-matched location - as
indicated by the <a href="sdk-for-flutter-navigate-navigation-routeprogress-class">RouteProgress</a> event.
This method should be called right after navigation has started.
In case of default prefetch length first prefetching will start after traveling a distance
of 9 km along the route.</p>
<p>To control list of map content features for prefetch, use <a href="sdk-for-flutter-navigate-core-engine-layerconfiguration-enabledfeatures">LayerConfiguration.enabledFeatures</a>.</p>
<ul>
<li><code>navigator</code> The <a href="sdk-for-flutter-navigate-navigation-navigatorinterface-class">NavigatorInterface</a> to listen for Route Progress to prefetch data ahead.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void prefetchAroundRouteOnIntervals(NavigatorInterface navigator);</code></pre>

 



</div>
`
}</HTMLBlock>
