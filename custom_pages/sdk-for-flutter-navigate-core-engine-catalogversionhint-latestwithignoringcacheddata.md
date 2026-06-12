---
title: "latestWithIgnoringCachedData static method"
slug: "sdk-for-flutter-navigate-core-engine-catalogversionhint-latestwithignoringcacheddata"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- latestWithIgnoringCachedData.html -->


<div>
<h1>latestWithIgnoringCachedData static method</h1></div>

<a href="/sdk-for-flutter-navigate-core-engine-catalogversionhint-class">CatalogVersionHint</a>
latestWithIgnoringCachedData(<ol class="parameter-list single-line"> <li>bool ignoreCachedData</li>
</ol>)

      

    

<p>This static method can be called when you are interested in getting the most latest version of
a catalog when initializing the HERE SDK with <code>SDKOptions</code> where you can specify the
catalog(s) you want to use.</p>
<p>In effect, this will auto-update the cached map data on each
start, if possible. Use this only when you have no installed <code>Regions</code>. Since this affects
only the map data cache, calling this at initialization time has no or only a very limited
effect on the start-up time.</p>
<p>In order to auto-update cached OCM-based map data, such as for the HERE SDK (Navigate), use the
default HRN value: "hrn:here:data::olp-here:ocm" in your <code>DesiredCatalog</code>. Note that the
HERE SDK (Explore) cannot be used with such settings and the
initialization of the HERE SDK may fail - since it is based on a different map
format.</p>
<ul>
<li><code>ignoreCachedData</code> A flag to specify handling of any cached data present on a device when
trying to update the map version.
If set to true, the HERE SDK will auto-update to the latest catalog version when no installed
<code>Regions</code> are present. If present, this call will have no effect - use <code>updateCatalog()</code>
via <code>MapUpdater</code> instead to update all map data to the latest version.
Note that cached data present on a device - for example, data in the map cache or data cached
by <code>PrefetchAroundLocationWithRadius</code> or <code>PrefetchAroundRouteOnIntervals</code> - will be become obsolete if
a newer map version is available. Such data will be evicted using a LRU strategy over time.
If set to false, the HERE SDK will auto-update to use the latest version, only
when there is no cached map data at all (for example, at first install or after
clearing the cache) <em>and</em> no installed map data. Otherwise, this call will have no effect.</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-navigate-core-engine-catalogversionhint-class">CatalogVersionHint</a>. Instance of <a href="/sdk-for-flutter-navigate-core-engine-catalogversionhint-class">CatalogVersionHint</a>.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static CatalogVersionHint latestWithIgnoringCachedData(bool ignoreCachedData) =&gt; $prototype.latestWithIgnoringCachedData(ignoreCachedData);</code></pre>

 



</div>
`
}</HTMLBlock>
