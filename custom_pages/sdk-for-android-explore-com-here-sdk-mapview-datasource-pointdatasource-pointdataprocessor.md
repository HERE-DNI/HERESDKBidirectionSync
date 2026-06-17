---
title: "PointDataSource.PointDataProcessor (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-datasource-pointdatasource-pointdataprocessor"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- PointDataSource.PointDataProcessor.html -->
<!DOCTYPE HTML>









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-package-summary">com.here.sdk.mapview.datasource</a></div>

</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-pointdatasource" title="class in com.here.sdk.mapview.datasource">PointDataSource</a></dd>
</dl>
<dl class="notes">
<dt>Functional Interface:</dt>
<dd>This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.</dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html" title="class or interface in java.lang">@FunctionalInterface</a>
</span><span class="modifiers">public static interface </span><span class="element-name type-name-label">PointDataSource.PointDataProcessor</span></div>
<div class="block"><p>Called for each point, allowing inspection, removal or update of coordinates and attributes.</p></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#process(com.here.sdk.mapview.datasource.PointDataAccessor)">process</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-pointdataaccessor" title="class in com.here.sdk.mapview.datasource">PointDataAccessor</a> pointAccessor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Called for each point, allowing inspection, removal or update of coordinates and attributes.</div>
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
<section class="detail" id="process(com.here.sdk.mapview.datasource.PointDataAccessor)">
<h3>process</h3>
<div class="member-signature"><span class="return-type">boolean</span> <span class="element-name">process</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-pointdataaccessor" title="class in com.here.sdk.mapview.datasource">PointDataAccessor</a> pointAccessor)</span></div>
<div class="block"><p>Called for each point, allowing inspection, removal or update of coordinates and attributes.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pointAccessor</code> - <p>the point data accessor.</p></dd>
<dt>Returns:</dt>
<dd><p>value indicating the result of the processing.</p></dd>
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
