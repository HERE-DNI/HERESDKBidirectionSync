---
title: "OfflineSearchIndexListener (API Reference)"
slug: "sdk-for-android-navigate-navigate-com-here-sdk-search-offlinesearchindexlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- OfflineSearchIndexListener.html -->
<!DOCTYPE HTML>






<div class="flex-box">
<header class="flex-header" role="banner">
<nav role="navigation">
<!-- ========= START OF TOP NAVBAR ======= -->
<div class="top-nav" id="navbar-top">
<div class="skip-nav"><a href="#skip-navbar-top" title="Skip navigation links">Skip navigation links</a></div>
<ul class="nav-list" id="navbar-top-firstrow" title="Navigation">
<li><a href="sdk-for-android-navigate-..-..-..-..-index">Overview</a></li>
<li><a href="sdk-for-android-navigate-package-summary">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="sdk-for-android-navigate-package-tree">Tree</a></li>
<li><a href="sdk-for-android-navigate-..-..-..-..-deprecated-list">Deprecated</a></li>
<li><a href="sdk-for-android-navigate-..-..-..-..-index-all">Index</a></li>
<li><a href="sdk-for-android-navigate-..-..-..-..-help-doc#class">Help</a></li>
</ul>
</div>
<div class="sub-nav">
<div>
<ul class="sub-nav-list">
<li>Summary: </li>
<li>Nested | </li>
<li>Field | </li>
<li>Constr | </li>
<li><a href="#method-summary">Method</a></li>
</ul>
<ul class="sub-nav-list">
<li>Detail: </li>
<li>Field | </li>
<li>Constr | </li>
<li><a href="#method-detail">Method</a></li>
</ul>
</div>

</div>
<!-- ========= END OF TOP NAVBAR ========= -->
<span class="skip-nav" id="skip-navbar-top"></span></nav>
</header>
<div class="flex-content">
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.search</a></div>

</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">OfflineSearchIndexListener</span></div>
<div class="block"><p>Interface to get updates about progress
 of creating persistent map index.
 </p><p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behaviors. Related APIs may change for new releases without a deprecation process.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#onComplete(com.here.sdk.search.OfflineSearchIndex.Error)">onComplete</a><wbr/>(<a href="sdk-for-android-navigate-offlinesearchindex.error" title="enum class in com.here.sdk.search">OfflineSearchIndex.Error</a> error)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Called after index creation or deletion has been completed.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#onProgress(int)">onProgress</a><wbr/>(int percentage)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Called multiple times to indicate the progress of index creation or deletion.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#onStarted(com.here.sdk.search.OfflineSearchIndex.Operation)">onStarted</a><wbr/>(<a href="sdk-for-android-navigate-offlinesearchindex.operation" title="enum class in com.here.sdk.search">OfflineSearchIndex.Operation</a> operation)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Called each time that the indexing has started.</div>
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
<section class="detail" id="onStarted(com.here.sdk.search.OfflineSearchIndex.Operation)">
<h3>onStarted</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onStarted</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-offlinesearchindex.operation" title="enum class in com.here.sdk.search">OfflineSearchIndex.Operation</a> operation)</span></div>
<div class="block"><p>Called each time that the indexing has started. It is triggered by changes to persistent map
 or by calling <code>OfflineSearchEngine.setIndexOptions</code>.
 If a valid index was previously created for the installed regions, no additional indexing
 is performed, so no notifications are sent. In this context, a valid index is the one
 that contains data for the exact versions of the installed map regions. When any of them
 is updated or new regions are downloaded or deleted, the index becomes invalid and is
 automatically rebuilt, as long as indexing has been enabled previously.
 Invoked on the main thread.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>operation</code> - <p>Shows whether the index is being created or removed.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="onProgress(int)">
<h3>onProgress</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onProgress</span><wbr/><span class="parameters">(int percentage)</span></div>
<div class="block"><p>Called multiple times to indicate the progress of index creation or deletion.
 Invoked on the main thread.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>percentage</code> - <p>Represents a percentage of work done.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="onComplete(com.here.sdk.search.OfflineSearchIndex.Error)">
<h3>onComplete</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onComplete</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-offlinesearchindex.error" title="enum class in com.here.sdk.search">OfflineSearchIndex.Error</a> error)</span></div>
<div class="block"><p>Called after index creation or deletion has been completed.
 Invoked on the main thread.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>error</code> - <p>Represents an error in case of a failure.
     It is <code>null</code> for an operation that succeeds.</p></dd>
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
</div>



</div>
`
}</HTMLBlock>
