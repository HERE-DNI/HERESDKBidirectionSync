---
title: "CatalogVersionHint (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-core-engine-catalogversionhint"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- CatalogVersionHint.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.core.engine</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.core.engine.CatalogVersionHint</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">CatalogVersionHint</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>This is a class for capturing user's intent for the
 desired catalog version to use in <a href="sdk-for-android-navigate-com-here-sdk-core-engine-desiredcatalog" title="class in com.here.sdk.core.engine"><code>DesiredCatalog</code></a> class.
 You can request a specific or latest version of a catalog by calling the
 static functions <a href="sdk-for-android-navigate-com-here-sdk-core-engine-catalogversionhint#specific(long)"><code>specific(long)</code></a> and
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-catalogversionhint#latest(boolean)"><code>latest(boolean)</code></a> respectively. The HERE platform will make the
 best effort to provide an appropriate version for the catalog based on this
 version hint.
 Please take note that for the API <a href="sdk-for-android-navigate-com-here-sdk-core-engine-catalogversionhint#specific(long)"><code>specific(long)</code></a> to function properly,
 it is essential that the mutable and persistent storage should be cleaned.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
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
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="specific(long)">
<h3>specific</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-engine-catalogversionhint" title="class in com.here.sdk.core.engine">CatalogVersionHint</a></span> <span className="element-name">specific</span><wbr/><span className="parameters">(long version)</span></div>
<div className="block"><p>This static method is used when you are interested in a
 specific version of a catalog, that you want to specify manually.
 To ensure proper functioning of this API, it is essential to clean the mutable and persistent storage.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>version</code> - <p>An integer value indicating the version of catalog desired.
     If the desired version does not exist, the HERE platform will make the
     best effort to provide an appropriate version or result in error logs
     about invalid version.</p></dd>
<dt>Returns:</dt>
<dd><p>Instance of <a href="sdk-for-android-navigate-com-here-sdk-core-engine-catalogversionhint" title="class in com.here.sdk.core.engine"><code>CatalogVersionHint</code></a> with specified version.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="latest(boolean)">
<h3>latest</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-engine-catalogversionhint" title="class in com.here.sdk.core.engine">CatalogVersionHint</a></span> <span className="element-name">latest</span><wbr/><span className="parameters">(boolean ignoreCachedData)</span></div>
<div className="block"><p>This static method can be called when you are interested in getting the most latest version of
 a catalog when initializing the HERE SDK with <code>SDKOptions</code> where you can specify the
 catalog(s) you want to use. In effect, this will auto-update the cached map data on each
 start, if possible. Use this only when you have no installed <code>Regions</code>. Since this affects
 only the map data cache, calling this at initialization time has no or only a very limited
 effect on the start-up time.
 In order to auto-update cached OCM-based map data, such as for the HERE SDK (Navigate), use the
 default HRN value: "hrn:here:data::olp-here:ocm" in your <code>DesiredCatalog</code>. Note that the
 HERE SDK (Explore) cannot be used with such settings and the
 initialization of the HERE SDK may fail - since it is based on a different map
 format.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>ignoreCachedData</code> - <p>A flag to specify handling of any cached data present on a device when
     trying to update the map version.
     If set to true, the HERE SDK will auto-update to the latest catalog version when no installed
     <code>Regions</code> are present. If present, this call will have no effect - use <code>updateCatalog()</code>
     via <code>MapUpdater</code> instead to update all map data to the latest version.
     Note that cached data present on a device - for example, data in the map cache or data cached
     by <code>PrefetchAroundLocationWithRadius</code> or <code>PrefetchAroundRouteOnIntervals</code> - will be become obsolete if
     a newer map version is available. Such data will be evicted using a LRU strategy over time.
     If set to false, the HERE SDK will auto-update to use the latest version, only
     when there is no cached map data at all (for example, at first install or after
     clearing the cache) <em>and</em> no installed map data. Otherwise, this call will have no effect.</p></dd>
<dt>Returns:</dt>
<dd><p>Instance of <a href="sdk-for-android-navigate-com-here-sdk-core-engine-catalogversionhint" title="class in com.here.sdk.core.engine"><code>CatalogVersionHint</code></a>.</p></dd>
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
