---
title: "PolygonPrefetcher (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-prefetcher-polygonprefetcher"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- PolygonPrefetcher.html -->
<!DOCTYPE HTML>









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-package-summary">com.here.sdk.prefetcher</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.prefetcher.PolygonPrefetcher</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">PolygonPrefetcher</span>
<span class="extends-implements">extends <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Supports downloading of map data - in advance - into the cache to optimize temporary offline
 use cases that rely on cached map data.
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine)">PolygonPrefetcher</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a PolygonPrefetcher instance for a given <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-sdknativeengine" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a>.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#estimateMapDataSize(com.here.sdk.core.GeoPolygon,com.here.sdk.prefetcher.MapDataSizeListener)">estimateMapDataSize</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-geopolygon" title="class in com.here.sdk.core">GeoPolygon</a> geoPolygon,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-mapdatasizelistener" title="interface in com.here.sdk.prefetcher">MapDataSizeListener</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Estimates map data size for the area bounded by geo polygon.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#prefetch(com.here.sdk.core.GeoPolygon,com.here.sdk.prefetcher.PrefetchStatusListener)">prefetch</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-geopolygon" title="class in com.here.sdk.core">GeoPolygon</a> geoPolygon,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-prefetchstatuslistener" title="interface in com.here.sdk.prefetcher">PrefetchStatusListener</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Prefetches map data for an area bounded by geo polygon.</div>
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
<h3>PolygonPrefetcher</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">PolygonPrefetcher</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</span></div>
<div class="block"><p>Creates a PolygonPrefetcher instance for a given <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-sdknativeengine" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a>.</p></div>
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
<section class="detail" id="prefetch(com.here.sdk.core.GeoPolygon,com.here.sdk.prefetcher.PrefetchStatusListener)">
<h3>prefetch</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">prefetch</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-geopolygon" title="class in com.here.sdk.core">GeoPolygon</a> geoPolygon,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-prefetchstatuslistener" title="interface in com.here.sdk.prefetcher">PrefetchStatusListener</a> callback)</span></div>
<div class="block"><p>Prefetches map data for an area bounded by geo polygon.
 After the operation is finished <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-prefetchstatuslistener#onComplete(com.here.sdk.maploader.MapLoaderError)"><code>PrefetchStatusListener.onComplete(com.here.sdk.maploader.MapLoaderError)</code></a> is
 invoked on the main thread. Progress is reported by invocation
 of <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-prefetchstatuslistener#onProgress(int)"><code>PrefetchStatusListener.onProgress(int)</code></a> on the main thread.
 If there is not enough space left in the cache to store needed tiles, operation will
 fail with <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-maploadererror#NOT_ENOUGH_SPACE"><code>MapLoaderError.NOT_ENOUGH_SPACE</code></a>. To increase cache size, use
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-sdkoptions#cacheSizeInBytes"><code>SDKOptions.cacheSizeInBytes</code></a> API.
 </p><p>To control list of map content features for area prefetch, use <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-layerconfiguration#enabledFeatures"><code>LayerConfiguration.enabledFeatures</code></a>.
 </p><p>To prefetch map data within user-defined circular area around a given location:
 <ol>
<li>Create a GeoCircle using the given location and radius.</li>
<li>Create a GeoPolygon using the GeoCircle.</li>
<li>Pass the afroementioned GeoPolygon to the sdk.prefetcher.PolygonPrefetcher.prefetch API.
 Usage:
 GeoCircle geoCircle = GeoCircle(location, radius);
 GeoPolygon geoPolygon = GeoPolygon.withGeoCircle(geoCircle);</li>
</ol></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>geoPolygon</code> - <p>Area to prefetch map data for.</p></dd>
<dd><code>callback</code> - <p>Callback that is triggered to report progress and the result of prefetch.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="estimateMapDataSize(com.here.sdk.core.GeoPolygon,com.here.sdk.prefetcher.MapDataSizeListener)">
<h3>estimateMapDataSize</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">estimateMapDataSize</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-geopolygon" title="class in com.here.sdk.core">GeoPolygon</a> geoPolygon,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-mapdatasizelistener" title="interface in com.here.sdk.prefetcher">MapDataSizeListener</a> callback)</span></div>
<div class="block"><p>Estimates map data size for the area bounded by geo polygon. Size for tiles that are already
 in the cache will not be included in the final result.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>geoPolygon</code> - <p>Area to estimate map data size for.</p></dd>
<dd><code>callback</code> - <p>Callback that is triggered to report the result of map data size estimation.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate execution of the task.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>





</div>
`
}</HTMLBlock>
