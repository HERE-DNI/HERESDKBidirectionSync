---
title: "CatalogConfiguration (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-core-engine-catalogconfiguration"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- CatalogConfiguration.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.core.engine</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.core.engine.CatalogConfiguration</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">CatalogConfiguration</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Using this class you can configure in the <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdkoptions" title="class in com.here.sdk.core.engine"><code>SDKOptions</code></a>,
 how the <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a> should access, use and store the data for the desired catalog.
 Using this class, you can access default catalogs on the HERE platform and also custom catalogs
 such as for self-hosted or BYOD (bring your own data) use cases.
 For information on how the user can identify a catalog on the HERE platform, see <a href="sdk-for-android-navigate-com-here-sdk-core-engine-desiredcatalog" title="class in com.here.sdk.core.engine"><code>DesiredCatalog</code></a>
 For further information about catalogs and related concepts see <a href="sdk-for-android-navigate-com-here-sdk-core-engine-catalogidentifier" title="class in com.here.sdk.core.engine"><code>CatalogIdentifier</code></a>.
 <strong>Note:</strong>
 This API is only applicable for the Navigate license.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>boolean</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-catalogconfiguration#allowDownload">allowDownload</a></code></div>
<div className="col-last even-row-color">
<div className="block">A flag to indicate if the data for this catalog is allowed to be stored in persistent storage for use with offline maps.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-catalogconfiguration#cacheExpirationPeriod">cacheExpirationPeriod</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Expiration time in seconds for how long the catalog data is retained in the
 map cache before it is removed.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-engine-desiredcatalog" title="class in com.here.sdk.core.engine">DesiredCatalog</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-catalogconfiguration#catalog">catalog</a></code></div>
<div className="col-last even-row-color">
<div className="block">The identifier for the desired catalog to be accessed on the HERE platform.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-catalogconfiguration#patchHrn">patchHrn</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Some catalogs may have additional modifications to their data
 contained in an entirely separate catalog, called the patch catalog.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-engine-catalogconfiguration#%3Cinit%3E(com.here.sdk.core.engine.DesiredCatalog)">CatalogConfiguration</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-engine-desiredcatalog" title="class in com.here.sdk.core.engine">DesiredCatalog</a> catalog)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance.</div>
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
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section className="field-details" id="field-detail">

<ul className="member-list">
<li>
<section className="detail" id="catalog">
<h3>catalog</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-engine-desiredcatalog" title="class in com.here.sdk.core.engine">DesiredCatalog</a></span> <span className="element-name">catalog</span></div>
<div className="block"><p>The identifier for the desired catalog to be accessed on the HERE platform.
 See <a href="sdk-for-android-navigate-com-here-sdk-core-engine-desiredcatalog" title="class in com.here.sdk.core.engine"><code>DesiredCatalog</code></a>.</p></div>
</section>
</li>
<li>
<section className="detail" id="patchHrn">
<h3>patchHrn</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">patchHrn</span></div>
<div className="block"><p>Some catalogs may have additional modifications to their data
 contained in an entirely separate catalog, called the patch catalog.
 This field indicates the HERE Resource Name (HRN) for the patch catalog.
 When this field is present, the catalog's data as referenced by
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-catalogconfiguration#catalog"><code>catalog</code></a> is merged with data from the patch catalog.
 If this field is <code>null</code>, then incremental updates are disabled.</p></div>
</section>
</li>
<li>
<section className="detail" id="cacheExpirationPeriod">
<h3>cacheExpirationPeriod</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></span> <span className="element-name">cacheExpirationPeriod</span></div>
<div className="block"><p>Expiration time in seconds for how long the catalog data is retained in the
 map cache before it is removed. Cache path is specified by <a href="sdk-for-android-navigate-sdkoptions#cachePath"><code>SDKOptions.cachePath</code></a>.
 If not set, the cache will be deleted on a Least Recently Used (LRU) basis.</p></div>
</section>
</li>
<li>
<section className="detail" id="allowDownload">
<h3>allowDownload</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">allowDownload</span></div>
<div className="block"><p>A flag to indicate if the data for this catalog is allowed to be stored in persistent storage for use with offline maps.
 The storage path is specified in <a href="sdk-for-android-navigate-sdkoptions#persistentMapStoragePath"><code>SDKOptions.persistentMapStoragePath</code></a>.
 If set to false, the data is not stored in persistent storage and is only retained in the cache for a limited time (see <a href="sdk-for-android-navigate-com-here-sdk-core-engine-catalogconfiguration#cacheExpirationPeriod"><code>cacheExpirationPeriod</code></a>).
 Defaults to <code>true</code>.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.core.engine.DesiredCatalog)">
<h3>CatalogConfiguration</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">CatalogConfiguration</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-desiredcatalog" title="class in com.here.sdk.core.engine">DesiredCatalog</a> catalog)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>catalog</code> - <p>The identifier for the desired catalog to be accessed on the HERE platform.
 See <a href="sdk-for-android-navigate-com-here-sdk-core-engine-desiredcatalog" title="class in com.here.sdk.core.engine"><code>DesiredCatalog</code></a>.</p></dd>
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
<section className="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">equals</span><wbr/><span className="parameters">(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl className="notes">
<dt>Overrides:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="hashCode()">
<h3>hashCode</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">hashCode</span>()</div>
<dl className="notes">
<dt>Overrides:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getDefault(com.here.sdk.core.engine.CatalogType)">
<h3>getDefault</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-engine-catalogconfiguration" title="class in com.here.sdk.core.engine">CatalogConfiguration</a></span> <span className="element-name">getDefault</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-catalogtype" title="enum class in com.here.sdk.core.engine">CatalogType</a> catalogType)</span></div>
<div className="block"><p>Gets the default catalog configuration for the specified catalog type.
 It uses the catalog version that was the latest at the time when the HERE SDK was built.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>catalogType</code> - <p>Catalog type</p></dd>
<dt>Returns:</dt>
<dd><p>Instance of <a href="sdk-for-android-navigate-com-here-sdk-core-engine-catalogconfiguration" title="class in com.here.sdk.core.engine"><code>CatalogConfiguration</code></a>.</p></dd>
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
