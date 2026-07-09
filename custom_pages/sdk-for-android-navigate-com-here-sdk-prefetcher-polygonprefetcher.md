---
title: "PolygonPrefetcher (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-prefetcher-polygonprefetcher"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- PolygonPrefetcher.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.prefetcher</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.prefetcher.PolygonPrefetcher</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">PolygonPrefetcher</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Supports downloading of map data - in advance - into the cache to optimize temporary offline
 use cases that rely on cached map data.
 Please note, this class puts data in the map cache, which has its own size constraints,
 and extensive usage may start evicting old cached data.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-prefetcher-polygonprefetcher#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine)">PolygonPrefetcher</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a PolygonPrefetcher instance for a given <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a>.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.core.engine.SDKNativeEngine)">
<h3>PolygonPrefetcher</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">PolygonPrefetcher</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</span></div>
<div className="block"><p>Creates a PolygonPrefetcher instance for a given <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a>.</p></div>
<dl className="notes">
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
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="prefetch(com.here.sdk.core.GeoPolygon,com.here.sdk.prefetcher.PrefetchStatusListener)">
<h3>prefetch</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">prefetch</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geopolygon" title="class in com.here.sdk.core">GeoPolygon</a> geoPolygon,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-prefetcher-prefetchstatuslistener" title="interface in com.here.sdk.prefetcher">PrefetchStatusListener</a> callback)</span></div>
<div className="block"><p>Prefetches map data for an area bounded by geo polygon.
 After the operation is finished <a href="sdk-for-android-navigate-prefetchstatuslistener#onComplete(com.here.sdk.maploader.MapLoaderError)"><code>PrefetchStatusListener.onComplete(com.here.sdk.maploader.MapLoaderError)</code></a> is
 invoked on the main thread. Progress is reported by invocation
 of <a href="sdk-for-android-navigate-prefetchstatuslistener#onProgress(int)"><code>PrefetchStatusListener.onProgress(int)</code></a> on the main thread.
 If there is not enough space left in the cache to store needed tiles, operation will
 fail with <a href="sdk-for-android-navigate-maploadererror#NOT_ENOUGH_SPACE"><code>MapLoaderError.NOT_ENOUGH_SPACE</code></a>. To increase cache size, use
 <a href="sdk-for-android-navigate-sdkoptions#cacheSizeInBytes"><code>SDKOptions.cacheSizeInBytes</code></a> API.
 To control list of map content features for area prefetch, use <a href="sdk-for-android-navigate-layerconfiguration#enabledFeatures"><code>LayerConfiguration.enabledFeatures</code></a>.
 To prefetch map data within user-defined circular area around a given location:
 <ol>
<li>Create a GeoCircle using the given location and radius.</li>
<li>Create a GeoPolygon using the GeoCircle.</li>
<li>Pass the afroementioned GeoPolygon to the sdk.prefetcher.PolygonPrefetcher.prefetch API.
 Usage:
 GeoCircle geoCircle = GeoCircle(location, radius);
 GeoPolygon geoPolygon = GeoPolygon.withGeoCircle(geoCircle);</li>
</ol></p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>geoPolygon</code> - <p>Area to prefetch map data for.</p></dd>
<dd><code>callback</code> - <p>Callback that is triggered to report progress and the result of prefetch.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="estimateMapDataSize(com.here.sdk.core.GeoPolygon,com.here.sdk.prefetcher.MapDataSizeListener)">
<h3>estimateMapDataSize</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">estimateMapDataSize</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geopolygon" title="class in com.here.sdk.core">GeoPolygon</a> geoPolygon,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-prefetcher-mapdatasizelistener" title="interface in com.here.sdk.prefetcher">MapDataSizeListener</a> callback)</span></div>
<div className="block"><p>Estimates map data size for the area bounded by geo polygon. Size for tiles that are already
 in the cache will not be included in the final result.</p></div>
<dl className="notes">
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

</div>
</div>



</div>
`
}</HTMLBlock>
