---
title: "RoutePrefetcher (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-prefetcher-routeprefetcher"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- RoutePrefetcher.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.prefetcher.RoutePrefetcher</div>
</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">RoutePrefetcher</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Supports downloading of map data - in advance - into the cache to optimize temporary offline
 use cases that rely on cached map data. This allows scenarios such as navigation to work in a
 specific area reliably even though the network might be offline at that time.
 Please note, this class puts data in the map cache, which has its own size constraints,
 and extensive usage may start evicting old cached data.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-prefetcher-routeprefetcher#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine)">RoutePrefetcher</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a RoutePrefetcher instance for a given <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a>.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-prefetcher-routeprefetcher#getPrefetchCorridorLengthMeters()">getPrefetchCorridorLengthMeters</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the length of the corridor along the route in front of the car which will be used to prefetch data.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-prefetcher-routeprefetcher#prefetchAroundLocationWithRadius(com.here.sdk.core.GeoCoordinates,java.lang.Double)">prefetchAroundLocationWithRadius</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> currentLocation,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> radiusInMeters)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.27.0.</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-prefetcher-routeprefetcher#prefetchAroundRouteOnIntervals(com.here.sdk.navigation.NavigatorInterface)">prefetchAroundRouteOnIntervals</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a> navigator)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Prefetches map data within a corridor along the route, that is currently set for the
 provided <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation"><code>NavigatorInterface</code></a> instance.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-prefetcher-routeprefetcher#prefetchGeoCorridor(com.here.sdk.core.GeoCorridor,com.here.sdk.prefetcher.PrefetchStatusListener)">prefetchGeoCorridor</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-geocorridor" title="class in com.here.sdk.core">GeoCorridor</a> corridor,
 <a href="sdk-for-android-navigate-com-here-sdk-prefetcher-prefetchstatuslistener" title="interface in com.here.sdk.prefetcher">PrefetchStatusListener</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Prefetch tiles for a given geo-corridor.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-prefetcher-routeprefetcher#setPrefetchCorridorLengthMeters(int)">setPrefetchCorridorLengthMeters</a><wbr/>(int value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the length of the corridor along the route in front of the car which will be used to prefetch data.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-prefetcher-routeprefetcher#stopPrefetchAroundRoute()">stopPrefetchAroundRoute</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Stops listening <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation"><code>NavigatorInterface</code></a> passed to <a href="sdk-for-android-navigate-com-here-sdk-prefetcher-routeprefetcher#prefetchAroundRouteOnIntervals(com.here.sdk.navigation.NavigatorInterface)"><code>prefetchAroundRouteOnIntervals(com.here.sdk.navigation.NavigatorInterface)</code></a>
 for route progress events and stops prefetching data along the current route.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.engine.SDKNativeEngine)">
<h3>RoutePrefetcher</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RoutePrefetcher</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</span></div>
<div class="block"><p>Creates a RoutePrefetcher instance for a given <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sdkEngine</code> - <p>Instance of an existing SDKEngine.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="prefetchAroundLocationWithRadius(com.here.sdk.core.GeoCoordinates,java.lang.Double)">
<h3>prefetchAroundLocationWithRadius</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">prefetchAroundLocationWithRadius</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> currentLocation,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> radiusInMeters)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.27.0. Please use <a href="sdk-for-android-navigate-polygonprefetcher#prefetch(com.here.sdk.core.GeoPolygon,com.here.sdk.prefetcher.PrefetchStatusListener)"><code>PolygonPrefetcher.prefetch(com.here.sdk.core.GeoPolygon, com.here.sdk.prefetcher.PrefetchStatusListener)</code></a> instead.</p></div>
</div>
<div class="block"><p>Prefetches map data within a user-defined circular area around a given location.
 The radius, specified in meters, must be between 1 km and 50 km.
 If <code>null</code> is passed as the radius, a default value of 2 km is used.
 It is recommended to call this method once before starting navigation
 to ensure a smooth experience.
 To control list of map content features for area prefetch, use <a href="sdk-for-android-navigate-layerconfiguration#enabledFeatures"><code>LayerConfiguration.enabledFeatures</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>currentLocation</code> - <p>The center of the circle to prefetch data within.</p></dd>
<dd><code>radiusInMeters</code> - <p>The radius of the circle to prefetch data within.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="prefetchAroundRouteOnIntervals(com.here.sdk.navigation.NavigatorInterface)">
<h3>prefetchAroundRouteOnIntervals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">prefetchAroundRouteOnIntervals</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a> navigator)</span></div>
<div class="block"><p>Prefetches map data within a corridor along the route, that is currently set for the
 provided <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation"><code>NavigatorInterface</code></a> instance. If no route is set, no data will be prefetched.
 The route corridor defaults to a length of 10 km and a width of 5 km.
 To prefetch the whole route before navigation has been started see <a href="sdk-for-android-navigate-com-here-sdk-prefetcher-routeprefetcher#prefetchGeoCorridor(com.here.sdk.core.GeoCorridor,com.here.sdk.prefetcher.PrefetchStatusListener)"><code>prefetchGeoCorridor(com.here.sdk.core.GeoCorridor, com.here.sdk.prefetcher.PrefetchStatusListener)</code></a>.
 Map data is prefetched only in discrete intervals. Prefetching starts 1 km before reaching the
 end of the current corridor. Prefetching happens based on the current map-matched location - as
 indicated by the <a href="sdk-for-android-navigate-com-here-sdk-navigation-routeprogress" title="class in com.here.sdk.navigation"><code>RouteProgress</code></a> event.
 This method should be called right after navigation has started.
 In case of default prefetch length first prefetching will start after traveling a distance
 of 9 km along the route.
 To control list of map content features for prefetch, use <a href="sdk-for-android-navigate-layerconfiguration#enabledFeatures"><code>LayerConfiguration.enabledFeatures</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>navigator</code> - <p>The <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation"><code>NavigatorInterface</code></a> to listen for Route Progress to prefetch data ahead.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="stopPrefetchAroundRoute()">
<h3>stopPrefetchAroundRoute</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">stopPrefetchAroundRoute</span>()</div>
<div class="block"><p>Stops listening <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation"><code>NavigatorInterface</code></a> passed to <a href="sdk-for-android-navigate-com-here-sdk-prefetcher-routeprefetcher#prefetchAroundRouteOnIntervals(com.here.sdk.navigation.NavigatorInterface)"><code>prefetchAroundRouteOnIntervals(com.here.sdk.navigation.NavigatorInterface)</code></a>
 for route progress events and stops prefetching data along the current route.</p></div>
</section>
</li>
<li>
<section class="detail" id="prefetchGeoCorridor(com.here.sdk.core.GeoCorridor,com.here.sdk.prefetcher.PrefetchStatusListener)">
<h3>prefetchGeoCorridor</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">prefetchGeoCorridor</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocorridor" title="class in com.here.sdk.core">GeoCorridor</a> corridor,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-prefetcher-prefetchstatuslistener" title="interface in com.here.sdk.prefetcher">PrefetchStatusListener</a> callback)</span></div>
<div class="block"><p>Prefetch tiles for a given geo-corridor. A geo-corridor can easily be created from a route with <a href="sdk-for-android-navigate-route#getGeometry()"><code>Route.getGeometry()</code></a>
 so navigation on this route is possible in offline cases.
 Please note, tiles will be saved in mutable cache so when there is not enough space to accommodate new
 prefetched tiles <a href="sdk-for-android-navigate-maploadererror#NOT_ENOUGH_SPACE"><code>MapLoaderError.NOT_ENOUGH_SPACE</code></a> is returned.
 When updating mutable cache, all tiles will be unusable. Please re-download the geoCorridor again.
 Please also note, any route calculation may not possible on prefetched tiles.
 To control list of map content features for corridor prefetch, use <a href="sdk-for-android-navigate-layerconfiguration#enabledFeatures"><code>LayerConfiguration.enabledFeatures</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>corridor</code> - <p>indicates <code>GeoCorridor</code> that can be constructed from the route.</p></dd>
<dd><code>callback</code> - <p>is invoked to report progress and the result of prefetch. After operation is
     finished, <a href="sdk-for-android-navigate-prefetchstatuslistener#onComplete(com.here.sdk.maploader.MapLoaderError)"><code>PrefetchStatusListener.onComplete(com.here.sdk.maploader.MapLoaderError)</code></a> is invoked on the main thread. Progress is reported by invocation
     of <a href="sdk-for-android-navigate-prefetchstatuslistener#onProgress(int)"><code>PrefetchStatusListener.onProgress(int)</code></a> on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPrefetchCorridorLengthMeters()">
<h3>getPrefetchCorridorLengthMeters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getPrefetchCorridorLengthMeters</span>()</div>
<div class="block"><p>Gets the length of the corridor along the route in front of the car which will be used to prefetch data.
 Upper limit for length is 50000 meters, when the requested length is greater than upper limit, then 50000 meters set.
 Lower limit for length is 1000 meters, when the requested length is less than lower limit, then 1000 meters set.
 The route corridor has a default length of 10 km and a width of 5 km.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The length of the corridor along the route in front of the car which will be used to prefetch data.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPrefetchCorridorLengthMeters(int)">
<h3>setPrefetchCorridorLengthMeters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPrefetchCorridorLengthMeters</span><wbr/><span class="parameters">(int value)</span></div>
<div class="block"><p>Sets the length of the corridor along the route in front of the car which will be used to prefetch data.
 Upper limit for length is 50000 meters, when the requested length is greater than upper limit, then 50000 meters set.
 Lower limit for length is 1000 meters, when the requested length is less than lower limit, then 1000 meters set.
 The route corridor has a default length of 10 km and a width of 5 km.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The length of the corridor along the route in front of the car which will be used to prefetch data.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->






</div>
`
}</HTMLBlock>
