---
title: "CatalogUpdateProgressListener (API Reference)"
slug: "sdk-for-android-navigate-catalogupdateprogresslistener"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- CatalogUpdateProgressListener.html -->
<!DOCTYPE HTML>






<div class="flex-box">
<header class="flex-header" role="banner">
<nav role="navigation">
<!-- ========= START OF TOP NAVBAR ======= -->
<div class="top-nav" id="navbar-top">
<div class="skip-nav"><a href="#skip-navbar-top" title="Skip navigation links">Skip navigation links</a></div>
<ul class="nav-list" id="navbar-top-firstrow" title="Navigation">
<li><a href="sdk-for-android-navigate-index">Overview</a></li>
<li><a href="sdk-for-android-navigate-package-summary">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="sdk-for-android-navigate-package-tree">Tree</a></li>
<li><a href="sdk-for-android-navigate-deprecated-list">Deprecated</a></li>
<li><a href="sdk-for-android-navigate-index-all">Index</a></li>
<li><a href="sdk-for-android-navigate-help-doc#class">Help</a></li>
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.maploader</a></div>

</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">CatalogUpdateProgressListener</span></div>
<div class="block"><p>Interface to get notified on status updates
 when updating catalog, previously downloaded by <a href="sdk-for-android-navigate-mapdownloader" title="class in com.here.sdk.maploader"><code>MapDownloader</code></a>.</p></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#onComplete(com.here.sdk.maploader.MapLoaderError)">onComplete</a><wbr/>(<a href="sdk-for-android-navigate-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a> error)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Called after the update process for all regions has been completed.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#onPause(com.here.sdk.maploader.MapLoaderError)">onPause</a><wbr/>(<a href="sdk-for-android-navigate-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a> error)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Called when update is paused.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#onProgress(com.here.sdk.maploader.RegionId,int)">onProgress</a><wbr/>(<a href="sdk-for-android-navigate-regionid" title="class in com.here.sdk.maploader">RegionId</a> region,
 int percentage)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Called multiple times to indicate the update progress.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#onResume()">onResume</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Called when a paused map update is resumed.</div>
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
<section class="detail" id="onProgress(com.here.sdk.maploader.RegionId,int)">
<h3>onProgress</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onProgress</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-regionid" title="class in com.here.sdk.maploader">RegionId</a> region,
 int percentage)</span></div>
<div class="block"><p>Called multiple times to indicate the update progress.
 Invoked on the main thread.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>region</code> - <p>Represents an id of region status update is related to.</p></dd>
<dd><code>percentage</code> - <p>Represents a percentage of catalog data which has been updated.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="onPause(com.here.sdk.maploader.MapLoaderError)">
<h3>onPause</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onPause</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a> error)</span></div>
<div class="block"><p>Called when update is paused.
 Invoked on the main thread.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>error</code> - <p>Populated when a retryable error is the reason for a pause. A retryable error can happen,
     when, for example, the HERE SDK tries too often to resume a download that was paused due to a lost connection.
     In general, the HERE SDK will try a few times, before the update is paused.
     This error value gives a hint on the reason for the necessary retry operation.
     A paused download can be resumed by the user at a later time.
     It is 'null' when <code>CatalogUpdateTask.pause(boolean)</code> was called by the user.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="onComplete(com.here.sdk.maploader.MapLoaderError)">
<h3>onComplete</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onComplete</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a> error)</span></div>
<div class="block"><p>Called after the update process for all regions has been completed.
 Invoked on the main thread.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>error</code> - <p>Represents an error in case of a failure.
     If an error occurs, the operation cannot be resumed later.
     It is <code>null</code> for an operation that succeeds.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="onResume()">
<h3>onResume</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onResume</span>()</div>
<div class="block"><p>Called when a paused map update is resumed.</p></div>
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
