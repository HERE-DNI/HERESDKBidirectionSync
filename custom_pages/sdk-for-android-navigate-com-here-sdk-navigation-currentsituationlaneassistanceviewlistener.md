---
title: "CurrentSituationLaneAssistanceViewListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-currentsituationlaneassistanceviewlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- CurrentSituationLaneAssistanceViewListener.html -->










<!-- ======== START OF CLASS DATA ======== -->

<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">CurrentSituationLaneAssistanceViewListener</span></div>
<div class="block"><p>This interface should be
 implemented in order to receive notifications on <a href="sdk-for-android-navigate-currentsituationlaneassistanceview" title="class in com.here.sdk.navigation"><code>CurrentSituationLaneAssistanceView</code></a>.
 </p><p>The current situation lane assistance view notifications describe the lane information at the current location.
 </p><p>A new notification is evaluated with each location update. A notification is only sent when there is a change
 in lane data, such as a new upcoming lane.
 </p><p>This event is supported both with a route during turn-by-turn navigation and without a route in tracking mode.
 During turn-by-turn navigation, the event additionally indicates which lanes help the driver stay on the route
 to reach the destination.
 However, the event does not indicate which exact lane the user is currently driving in.
 The listener works for offline mode as well.
 </p><p><strong>Note:</strong>
<ul>
<li>Lane information is not available for all roads. It's mostly available for roads with painted turn directions.</li>
<li>This is a <strong>beta</strong> release of this feature, so there could be a few bugs and unexpected
 behaviors. Related APIs may change for new releases without a deprecation process.</li>
</ul></p></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-navigate-index#onCurrentSituationLaneAssistanceViewUpdate(com.here.sdk.navigation.CurrentSituationLaneAssistanceView)">onCurrentSituationLaneAssistanceViewUpdate</a><wbr/>(<a href="sdk-for-android-navigate-currentsituationlaneassistanceview" title="class in com.here.sdk.navigation">CurrentSituationLaneAssistanceView</a> lanes)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">The callback to be called.</div>
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
<section class="detail" id="onCurrentSituationLaneAssistanceViewUpdate(com.here.sdk.navigation.CurrentSituationLaneAssistanceView)">
<h3>onCurrentSituationLaneAssistanceViewUpdate</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onCurrentSituationLaneAssistanceViewUpdate</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-currentsituationlaneassistanceview" title="class in com.here.sdk.navigation">CurrentSituationLaneAssistanceView</a> lanes)</span></div>
<div class="block"><p>The callback to be called.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>lanes</code> - <p>Lane information on the road the user is currently driving on.</p></dd>
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
