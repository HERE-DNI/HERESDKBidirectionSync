---
title: "MapDataSizeListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-prefetcher-mapdatasizelistener"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- MapDataSizeListener.html -->










<!-- ======== START OF CLASS DATA ======== -->

<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">MapDataSizeListener</span></div>
<div class="block"><p>Interface to get the result of map data size
 estimation.</p></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-navigate-index#onSizeEstimated(com.here.sdk.maploader.MapLoaderError,com.here.sdk.prefetcher.MapDataSize)">onSizeEstimated</a><wbr/>(<a href="sdk-for-android-navigate-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a> error,
 <a href="sdk-for-android-navigate-mapdatasize" title="class in com.here.sdk.prefetcher">MapDataSize</a> dataSize)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Called after map data size estimation has been completed either with success or with error.</div>
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
<section class="detail" id="onSizeEstimated(com.here.sdk.maploader.MapLoaderError,com.here.sdk.prefetcher.MapDataSize)">
<h3>onSizeEstimated</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onSizeEstimated</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a> error,
 @Nullable
 <a href="sdk-for-android-navigate-mapdatasize" title="class in com.here.sdk.prefetcher">MapDataSize</a> dataSize)</span></div>
<div class="block"><p>Called after map data size estimation has been completed either with success or with error.
 Invoked on the main thread.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>error</code> - <p>Represents an error in case of a failure. If the operation was successful,
     <code>null</code> is returned.</p></dd>
<dd><code>dataSize</code> - <p>Represents the map data size. In case of failure,
     <code>null</code> is returned.</p></dd>
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
