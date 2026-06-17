---
title: "RasterDataSourceConfiguration.Cache (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-datasource-rasterdatasourceconfiguration-cache"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- RasterDataSourceConfiguration.Cache.html -->
<!DOCTYPE HTML>









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-package-summary">com.here.sdk.mapview.datasource</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.mapview.datasource.RasterDataSourceConfiguration.Cache</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-rasterdatasourceconfiguration" title="class in com.here.sdk.mapview.datasource">RasterDataSourceConfiguration</a></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public static final class </span><span class="element-name type-name-label">RasterDataSourceConfiguration.Cache</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Configuration of a local data cache.</p></div>
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
<div class="col-first even-row-color"><code>long</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#diskSize">diskSize</a></code></div>
<div class="col-last even-row-color">
<div class="block">The maximum size to use on disk for the cache, in bytes.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#path">path</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The path to the directory to use for the cache.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#%3Cinit%3E(java.lang.String)">Cache</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> path)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs a Cache object from the provided path and a default cache size of 32 MiB.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#%3Cinit%3E(java.lang.String,long)">Cache</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> path,
 long diskSize)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructs a Cache object from the provided path and cache size.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="path">
<h3>path</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">path</span></div>
<div class="block"><p>The path to the directory to use for the cache. By default, the map gets initialized with a
 data path which can be fetched from <code>SDKOptions.cachePath</code>. The cache will be relative to this path,
 unless an absolute path is provided. The cache can be stored in an internal/external storage as long
 as the app has read/write permissions.
 Empty string means the data path will be used for caching.
 If the provided path, either as absolute path or as relative path is invalid,
 then caching will be disabled.
 There is no contraint regarding the existence of the path. If the path does not exist
 but is valid, it will be created.</p></div>
</section>
</li>
<li>
<section class="detail" id="diskSize">
<h3>diskSize</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">diskSize</span></div>
<div class="block"><p>The maximum size to use on disk for the cache, in bytes. Default is 32 MiB.
 This cache is independent from the map cache as defined via <code>SDKOptions</code>.
 Its size is only limited by the total device storage capacity.</p></div>
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
<section class="detail" id="&lt;init&gt;(java.lang.String)">
<h3>Cache</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Cache</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> path)</span></div>
<div class="block"><p>Constructs a Cache object from the provided path and a default cache size of 32 MiB.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>path</code> - <p>The path to the directory to use for the cache. By default, the map gets initialized with a
 data path which can be fetched from <code>SDKOptions.cachePath</code>. The cache will be relative to this path,
 unless an absolute path is provided. The cache can be stored in an internal/external storage as long
 as the app has read/write permissions.
 Empty string means the data path will be used for caching.
 If the provided path, either as absolute path or as relative path is invalid,
 then caching will be disabled.
 There is no contraint regarding the existence of the path. If the path does not exist
 but is valid, it will be created.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,long)">
<h3>Cache</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Cache</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> path,
 long diskSize)</span></div>
<div class="block"><p>Constructs a Cache object from the provided path and cache size.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>path</code> - <p>The path to the directory to use for the cache. By default, the map gets initialized with a
 data path which can be fetched from <code>SDKOptions.cachePath</code>. The cache will be relative to this path,
 unless an absolute path is provided. The cache can be stored in an internal/external storage as long
 as the app has read/write permissions.
 Empty string means the data path will be used for caching.
 If the provided path, either as absolute path or as relative path is invalid,
 then caching will be disabled.
 There is no contraint regarding the existence of the path. If the path does not exist
 but is valid, it will be created.</p></dd>
<dd><code>diskSize</code> - <p>The maximum size to use on disk for the cache, in bytes. Default is 32 MiB.
 This cache is independent from the map cache as defined via <code>SDKOptions</code>.
 Its size is only limited by the total device storage capacity.</p></dd>
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
