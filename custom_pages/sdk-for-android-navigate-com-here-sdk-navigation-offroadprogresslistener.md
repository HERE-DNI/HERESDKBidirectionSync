---
title: "OffRoadProgressListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-offroadprogresslistener"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- OffRoadProgressListener.html -->










<!-- ======== START OF CLASS DATA ======== -->

<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">OffRoadProgressListener</span></div>
<div class="block"><p>This interface should be implemented in order to
 receive notifications about the current off-road location from <a href="sdk-for-android-navigate-navigator" title="class in com.here.sdk.navigation"><code>Navigator</code></a>.</p></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-navigate-index#onOffRoadProgressUpdated(com.here.sdk.navigation.OffRoadProgress)">onOffRoadProgressUpdated</a><wbr/>(<a href="sdk-for-android-navigate-offroadprogress" title="class in com.here.sdk.navigation">OffRoadProgress</a> offRoadProgress)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Called whenever the current location has been updated and the user is off-road.</div>
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
<section class="detail" id="onOffRoadProgressUpdated(com.here.sdk.navigation.OffRoadProgress)">
<h3>onOffRoadProgressUpdated</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onOffRoadProgressUpdated</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-offroadprogress" title="class in com.here.sdk.navigation">OffRoadProgress</a> offRoadProgress)</span></div>
<div class="block"><p>Called whenever the current location has been updated and the user is off-road. Off-road
 progress events starts after the user has reached the map-matched destination and the current
 location is not map-matched.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>offRoadProgress</code> - <p>The current off-road progress update.</p></dd>
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
