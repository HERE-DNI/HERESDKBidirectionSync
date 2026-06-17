---
title: "RoadAttributesListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-roadattributeslistener"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- RoadAttributesListener.html -->
<!DOCTYPE HTML>









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">RoadAttributesListener</span></div>
<div class="block"><p>This interface
 should be implemented in order to receive attributes of the current road.</p></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#onRoadAttributesUpdated(com.here.sdk.navigation.RoadAttributes)">onRoadAttributesUpdated</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-roadattributes" title="class in com.here.sdk.navigation">RoadAttributes</a> roadAttributes)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Called whenever any attribute of the current road changes.</div>
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
<section class="detail" id="onRoadAttributesUpdated(com.here.sdk.navigation.RoadAttributes)">
<h3>onRoadAttributesUpdated</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onRoadAttributesUpdated</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-roadattributes" title="class in com.here.sdk.navigation">RoadAttributes</a> roadAttributes)</span></div>
<div class="block"><p>Called whenever any attribute of the current road changes. It's guaranteed to
 be called at least once for the first road the user is traveling on.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>roadAttributes</code> - <p>The object that contains attributes of the current road.</p></dd>
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
