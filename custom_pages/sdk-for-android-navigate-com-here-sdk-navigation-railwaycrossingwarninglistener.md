---
title: "RailwayCrossingWarningListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-railwaycrossingwarninglistener"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- RailwayCrossingWarningListener.html -->










<!-- ======== START OF CLASS DATA ======== -->

<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">RailwayCrossingWarningListener</span></div>
<div class="block"><p>This interface
 should be implemented in order to receive railway crossing warnings.
 <strong>Note:</strong> The railway crossing warner can be either a zone warner or a point warner, depending
 on whether the railroad crossing warning is given for a railroad crossing zone or just a point. This
 means that for a railway crossing there will can be either 2 or 3 warnings emitted. In case the railroad
 crossing is a zone warner then 3 warnings will be emitted with the <code>RailwayCrossingWarning.distance_type</code> set to <code>DistanceType.AHEAD</code>,
 <code>DistanceType.REACHED</code> and lastly <code>DistanceType.PASSED</code> when the end of the railway crossing is passed. In
 case the railroad crossing is a point warner then 2 warnings will be emitted with the <code>RailwayCrossingWarning.distance_type</code>
 set to <code>DistanceType.AHEAD</code> and <code>DistanceType.PASSED</code> when the end of the railway crossing is passed.</p></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-navigate-index#onRailwayCrossingWarningUpdated(com.here.sdk.navigation.RailwayCrossingWarning)">onRailwayCrossingWarningUpdated</a><wbr/>(<a href="sdk-for-android-navigate-railwaycrossingwarning" title="class in com.here.sdk.navigation">RailwayCrossingWarning</a> railwayCrossingWarning)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Called whenever a new railway crossing warning is available.</div>
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
<section class="detail" id="onRailwayCrossingWarningUpdated(com.here.sdk.navigation.RailwayCrossingWarning)">
<h3>onRailwayCrossingWarningUpdated</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onRailwayCrossingWarningUpdated</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-railwaycrossingwarning" title="class in com.here.sdk.navigation">RailwayCrossingWarning</a> railwayCrossingWarning)</span></div>
<div class="block"><p>Called whenever a new railway crossing warning is available.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>railwayCrossingWarning</code> - <p>The object that contains details on the railway crossing warning.</p></dd>
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
