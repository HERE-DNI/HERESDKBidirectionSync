---
title: "RasterDataSourceListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourcelistener"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- RasterDataSourceListener.html -->










<!-- ======== START OF CLASS DATA ======== -->

<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">RasterDataSourceListener</span></div>
<div class="block"><p>Listener for RasterDataSource events.</p></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourcelistener#onRasterDataSourceError(com.here.sdk.mapview.datasource.RasterDataSourceError)">onRasterDataSourceError</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceerror" title="enum class in com.here.sdk.mapview.datasource">RasterDataSourceError</a> dataSourceError)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The method to call on the listener when a data source error occurs.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourcelistener#onRasterDataSourceReady()">onRasterDataSourceReady</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The method to call on the listener when data source is ready to use.</div>
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
<section class="detail" id="onRasterDataSourceReady()">
<h3>onRasterDataSourceReady</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onRasterDataSourceReady</span>()</div>
<div class="block"><p>The method to call on the listener when data source is ready to use.</p></div>
</section>
</li>
<li>
<section class="detail" id="onRasterDataSourceError(com.here.sdk.mapview.datasource.RasterDataSourceError)">
<h3>onRasterDataSourceError</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onRasterDataSourceError</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-datasource-rasterdatasourceerror" title="enum class in com.here.sdk.mapview.datasource">RasterDataSourceError</a> dataSourceError)</span></div>
<div class="block"><p>The method to call on the listener when a data source error occurs.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>dataSourceError</code> - <p>a data source error.</p></dd>
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
