---
title: "prefetchAroundLocationWithRadius abstract method"
slug: "sdk-for-flutter-navigate-prefetcher-routeprefetcher-prefetcharoundlocationwithradius"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- prefetchAroundLocationWithRadius.html -->


<div>
<h1>prefetchAroundLocationWithRadius abstract method</h1></div>

<div>
<ol class="annotation-list">
<li>@Deprecated("Will be removed in v4.27.0. Please use [PolygonPrefetcher.prefetch] instead.")</li>
</ol>
</div>
void
prefetchAroundLocationWithRadius(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a> currentLocation, </li>
<li>double? radiusInMeters</li>
</ol>)

      

    

<p>Prefetches map data within a user-defined circular area around a given location.</p>
<p>The radius, specified in meters, must be between 1 km and 50 km.
If <code>null</code> is passed as the radius, a default value of 2 km is used.
It is recommended to call this method once before starting navigation
to ensure a smooth experience.</p>
<p>To control list of map content features for area prefetch, use <a href="sdk-for-flutter-navigate-core-engine-layerconfiguration-enabledfeatures">LayerConfiguration.enabledFeatures</a>.</p>
<ul>
<li>
<p><code>currentLocation</code> The center of the circle to prefetch data within.</p>
</li>
<li>
<p><code>radiusInMeters</code> The radius of the circle to prefetch data within.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">@Deprecated("Will be removed in v4.27.0. Please use [PolygonPrefetcher.prefetch] instead.")

void prefetchAroundLocationWithRadius(GeoCoordinates currentLocation, double? radiusInMeters);</code></pre>

 



</div>
`
}</HTMLBlock>
