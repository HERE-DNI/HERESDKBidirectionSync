---
title: "LowSpeedZoneWarningListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-lowspeedzonewarninglistener"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- LowSpeedZoneWarningListener.html -->










<!-- ======== START OF CLASS DATA ======== -->

<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">LowSpeedZoneWarningListener</span></div>
<div class="block"><p>This interface should be implemented in order to receive low speed zone warnings.
 <strong>Note:</strong> This is currently available <em>only</em> for Japan.
 The low speed zone warner is a zone warner, which means that for a low speed zone there will <em>always</em>
 be 3 warnings emitted, with the <code>LowSpeedZoneWarning.distance_type</code> set to <code>DistanceType.AHEAD</code>, <code>DistanceType.REACHED</code>
 and lastly <code>DistanceType.PASSED</code> when the end of the low speed zone is passed.</p></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-lowspeedzonewarninglistener#onLowSpeedZoneWarningUpdated(com.here.sdk.navigation.LowSpeedZoneWarning)">onLowSpeedZoneWarningUpdated</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-navigation-lowspeedzonewarning" title="class in com.here.sdk.navigation">LowSpeedZoneWarning</a> lowSpeedZoneWarning)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Called whenever a new low speed zone warning is available.</div>
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
<section class="detail" id="onLowSpeedZoneWarningUpdated(com.here.sdk.navigation.LowSpeedZoneWarning)">
<h3>onLowSpeedZoneWarningUpdated</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onLowSpeedZoneWarningUpdated</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-lowspeedzonewarning" title="class in com.here.sdk.navigation">LowSpeedZoneWarning</a> lowSpeedZoneWarning)</span></div>
<div class="block"><p>Called whenever a new low speed zone warning is available.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>lowSpeedZoneWarning</code> - <p>The object that contains details on the low speed zone warning.</p></dd>
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
