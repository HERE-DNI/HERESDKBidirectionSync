---
title: "CatalogConfiguration (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-engine-catalogconfiguration"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- CatalogConfiguration.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.core.engine.CatalogConfiguration</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">CatalogConfiguration</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Using this class you can configure in the <a href="sdk-for-android-explore-sdkoptions" title="class in com.here.sdk.core.engine"><code>SDKOptions</code></a>,
 how the <a href="sdk-for-android-explore-sdknativeengine" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a> should access, use and store the data for the desired catalog.
 Using this class, you can access default catalogs on the HERE platform and also custom catalogs
 such as for self-hosted or BYOD (bring your own data) use cases.
 For information on how the user can identify a catalog on the HERE platform, see <a href="sdk-for-android-explore-desiredcatalog" title="class in com.here.sdk.core.engine"><code>DesiredCatalog</code></a>
 For further information about catalogs and related concepts see <a href="sdk-for-android-explore-catalogidentifier" title="class in com.here.sdk.core.engine"><code>CatalogIdentifier</code></a>.
 <strong>Note:</strong>
 This API is only applicable for the Navigate license.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">

<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-engine-catalogconfiguration#allowDownload">allowDownload</a></code></div>
<div class="col-last even-row-color">
<div class="block">A flag to indicate if the data for this catalog is allowed to be stored in persistent storage for use with offline maps.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-explore-duration" title="class in com.here.time">Duration</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-engine-catalogconfiguration#cacheExpirationPeriod">cacheExpirationPeriod</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Expiration time in seconds for how long the catalog data is retained in the
 map cache before it is removed.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-explore-desiredcatalog" title="class in com.here.sdk.core.engine">DesiredCatalog</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-engine-catalogconfiguration#catalog">catalog</a></code></div>
<div class="col-last even-row-color">
<div class="block">The identifier for the desired catalog to be accessed on the HERE platform.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-engine-catalogconfiguration#patchHrn">patchHrn</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Some catalogs may have additional modifications to their data
 contained in an entirely separate catalog, called the patch catalog.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-engine-catalogconfiguration#%3Cinit%3E(com.here.sdk.core.engine.DesiredCatalog)">CatalogConfiguration</a><wbr/>(<a href="sdk-for-android-explore-desiredcatalog" title="class in com.here.sdk.core.engine">DesiredCatalog</a> catalog)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-engine-catalogconfiguration#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>

<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-explore-catalogconfiguration" title="class in com.here.sdk.core.engine">CatalogConfiguration</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-engine-catalogconfiguration#getDefault(com.here.sdk.core.engine.CatalogType)">getDefault</a><wbr/>(<a href="sdk-for-android-explore-catalogtype" title="enum class in com.here.sdk.core.engine">CatalogType</a> catalogType)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Gets the default catalog configuration for the specified catalog type.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-engine-catalogconfiguration#hashCode()">hashCode</a>()</code></div>

</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">

<ul class="member-list">
<li>
<section class="detail" id="catalog">
<h3>catalog</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-desiredcatalog" title="class in com.here.sdk.core.engine">DesiredCatalog</a></span> <span class="element-name">catalog</span></div>
<div class="block"><p>The identifier for the desired catalog to be accessed on the HERE platform.
 See <a href="sdk-for-android-explore-desiredcatalog" title="class in com.here.sdk.core.engine"><code>DesiredCatalog</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="patchHrn">
<h3>patchHrn</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">patchHrn</span></div>
<div class="block"><p>Some catalogs may have additional modifications to their data
 contained in an entirely separate catalog, called the patch catalog.
 This field indicates the HERE Resource Name (HRN) for the patch catalog.
 When this field is present, the catalog's data as referenced by
 <a href="sdk-for-android-explore-com-here-sdk-core-engine-catalogconfiguration#catalog"><code>catalog</code></a> is merged with data from the patch catalog.
 If this field is <code>null</code>, then incremental updates are disabled.</p></div>
</section>
</li>
<li>
<section class="detail" id="cacheExpirationPeriod">
<h3>cacheExpirationPeriod</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-duration" title="class in com.here.time">Duration</a></span> <span class="element-name">cacheExpirationPeriod</span></div>
<div class="block"><p>Expiration time in seconds for how long the catalog data is retained in the
 map cache before it is removed. Cache path is specified by <a href="sdk-for-android-explore-sdkoptions#cachePath"><code>SDKOptions.cachePath</code></a>.
 If not set, the cache will be deleted on a Least Recently Used (LRU) basis.</p></div>
</section>
</li>
<li>
<section class="detail" id="allowDownload">
<h3>allowDownload</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">allowDownload</span></div>
<div class="block"><p>A flag to indicate if the data for this catalog is allowed to be stored in persistent storage for use with offline maps.
 The storage path is specified in <a href="sdk-for-android-explore-sdkoptions#persistentMapStoragePath"><code>SDKOptions.persistentMapStoragePath</code></a>.
 If set to false, the data is not stored in persistent storage and is only retained in the cache for a limited time (see <a href="sdk-for-android-explore-com-here-sdk-core-engine-catalogconfiguration#cacheExpirationPeriod"><code>cacheExpirationPeriod</code></a>).
 Defaults to <code>true</code>.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.engine.DesiredCatalog)">
<h3>CatalogConfiguration</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">CatalogConfiguration</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-desiredcatalog" title="class in com.here.sdk.core.engine">DesiredCatalog</a> catalog)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>catalog</code> - <p>The identifier for the desired catalog to be accessed on the HERE platform.
 See <a href="sdk-for-android-explore-desiredcatalog" title="class in com.here.sdk.core.engine"><code>DesiredCatalog</code></a>.</p></dd>
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
<section class="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hashCode()">
<h3>hashCode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDefault(com.here.sdk.core.engine.CatalogType)">
<h3>getDefault</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-catalogconfiguration" title="class in com.here.sdk.core.engine">CatalogConfiguration</a></span> <span class="element-name">getDefault</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-catalogtype" title="enum class in com.here.sdk.core.engine">CatalogType</a> catalogType)</span></div>
<div class="block"><p>Gets the default catalog configuration for the specified catalog type.
 It uses the catalog version that was the latest at the time when the HERE SDK was built.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>catalogType</code> - <p>Catalog type</p></dd>
<dt>Returns:</dt>
<dd><p>Instance of <a href="sdk-for-android-explore-catalogconfiguration" title="class in com.here.sdk.core.engine"><code>CatalogConfiguration</code></a>.</p></dd>
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
