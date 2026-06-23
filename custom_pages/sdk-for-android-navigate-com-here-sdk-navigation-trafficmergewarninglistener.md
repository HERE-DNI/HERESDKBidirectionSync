---
title: "TrafficMergeWarningListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-trafficmergewarninglistener"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- TrafficMergeWarningListener.html -->










<!-- ======== START OF CLASS DATA ======== -->

<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">TrafficMergeWarningListener</span></div>
<div class="block"><p>This interface
 should be implemented in order to receive traffic merge warnings.
 <strong>Note:</strong> The traffic merge warner is a point warner, which means that for a traffic merge there will <em>always</em> be
 2 warnings emitted, with the <code>TrafficMergeWarning.distance_type</code> set to <code>DistanceType.AHEAD</code> and <code>DistanceType.PASSED</code>
 which is given when the location of the traffic merge is reached.
 A <code>TrafficMergeWarning</code> will not be given until the previous warning of that type has been passed.
 For example, a route with <code>TrafficMergeWarning</code> 120 meters and <code>TrafficMergeWarning</code> 160 meters ahead,
 the first <code>TrafficMergeWarning.distance_to_traffic_merge_in_meters</code> is 120 meters
 and the next <code>TrafficMergeWarning.distance_to_traffic_merge_in_meters</code> is then 40 meters,
 since that is the distance between the first and second warnings.</p></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-navigate-index#onTrafficMergeWarningUpdated(com.here.sdk.navigation.TrafficMergeWarning)">onTrafficMergeWarningUpdated</a><wbr/>(<a href="sdk-for-android-navigate-trafficmergewarning" title="class in com.here.sdk.navigation">TrafficMergeWarning</a> trafficMergeWarning)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Called whenever a new traffic merge warning is available.</div>
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
<section class="detail" id="onTrafficMergeWarningUpdated(com.here.sdk.navigation.TrafficMergeWarning)">
<h3>onTrafficMergeWarningUpdated</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onTrafficMergeWarningUpdated</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-trafficmergewarning" title="class in com.here.sdk.navigation">TrafficMergeWarning</a> trafficMergeWarning)</span></div>
<div class="block"><p>Called whenever a new traffic merge warning is available.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>trafficMergeWarning</code> - <p>The object that contains details on the traffic merge warning.</p></dd>
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
