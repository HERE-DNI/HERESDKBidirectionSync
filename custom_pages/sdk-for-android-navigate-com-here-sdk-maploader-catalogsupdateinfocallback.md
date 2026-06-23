---
title: "CatalogsUpdateInfoCallback (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-maploader-catalogsupdateinfocallback"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- CatalogsUpdateInfoCallback.html -->










<!-- ======== START OF CLASS DATA ======== -->

<section class="class-description" id="class-description">
<dl class="notes">
<dt>Functional Interface:</dt>
<dd>This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.</dd>
</dl>

<div class="type-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html" title="class or interface in java.lang">@FunctionalInterface</a>
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">CatalogsUpdateInfoCallback</span></div>
<div class="block"><p>This method will be called on the main thread when <a href="sdk-for-android-navigate-mapupdater#retrieveCatalogsUpdateInfo(com.here.sdk.maploader.CatalogsUpdateInfoCallback)"><code>MapUpdater.retrieveCatalogsUpdateInfo(com.here.sdk.maploader.CatalogsUpdateInfoCallback)</code></a> has been completed.
 The first parameter indicates an error in case of a failure. The second parameter contains the results.
 Both parameters cannot be <code>null</code> at the same time - or not <code>null</code> at the same time.
 An empty <code>CatalogUpdateInfo</code> list  represent no map updates.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-navigate-index#apply(com.here.sdk.maploader.MapLoaderError,java.util.List)">apply</a><wbr/>(<a href="sdk-for-android-navigate-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a> error,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-catalogupdateinfo" title="class in com.here.sdk.maploader">CatalogUpdateInfo</a>&gt; catalogs)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">This method will be called on the main thread when <a href="sdk-for-android-navigate-mapupdater#retrieveCatalogsUpdateInfo(com.here.sdk.maploader.CatalogsUpdateInfoCallback)"><code>MapUpdater.retrieveCatalogsUpdateInfo(com.here.sdk.maploader.CatalogsUpdateInfoCallback)</code></a> has been completed.</div>
</div>
</div>
</div>
</div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="apply(com.here.sdk.maploader.MapLoaderError,java.util.List)">
<h3>apply</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">apply</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a> error,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-catalogupdateinfo" title="class in com.here.sdk.maploader">CatalogUpdateInfo</a>&gt; catalogs)</span></div>
<div class="block"><p>This method will be called on the main thread when <a href="sdk-for-android-navigate-mapupdater#retrieveCatalogsUpdateInfo(com.here.sdk.maploader.CatalogsUpdateInfoCallback)"><code>MapUpdater.retrieveCatalogsUpdateInfo(com.here.sdk.maploader.CatalogsUpdateInfoCallback)</code></a> has been completed.
 The first parameter indicates an error in case of a failure. The second parameter contains the results.
 Both parameters cannot be <code>null</code> at the same time - or not <code>null</code> at the same time.
 An empty <code>CatalogUpdateInfo</code> list  represent no map updates.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>error</code> - <p>Represents an error in case of a failure. It is <code>null</code> for an operation that succeeds.</p></dd>
<dd><code>catalogs</code> - <p>Represents a list of all catalogs that can be updated. It is <code>null</code> in case of an error.</p></dd>
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
