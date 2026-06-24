---
title: "RoadTextsListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-roadtextslistener"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- RoadTextsListener.html -->










<!-- ======== START OF CLASS DATA ======== -->

<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">RoadTextsListener</span></div>
<div class="block"><p>This interface
 should be implemented in order to receive textual attributes of the current road.</p></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-roadtextslistener#onRoadTextsUpdated(com.here.sdk.routing.RoadTexts)">onRoadTextsUpdated</a><wbr/>(<a href="sdk-for-android-navigate-roadtexts" title="class in com.here.sdk.routing">RoadTexts</a> roadTexts)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Called whenever any textual attribute of the current road changes, i.e., the current road
 texts differs from the previous one already issued.</div>
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
<section class="detail" id="onRoadTextsUpdated(com.here.sdk.routing.RoadTexts)">
<h3>onRoadTextsUpdated</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onRoadTextsUpdated</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-roadtexts" title="class in com.here.sdk.routing">RoadTexts</a> roadTexts)</span></div>
<div class="block"><p>Called whenever any textual attribute of the current road changes, i.e., the current road
 texts differs from the previous one already issued.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>roadTexts</code> - <p>The object that contains the textual attributes of the current road.</p></dd>
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
