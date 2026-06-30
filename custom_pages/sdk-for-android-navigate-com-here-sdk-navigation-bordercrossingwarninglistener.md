---
title: "BorderCrossingWarningListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarninglistener"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- BorderCrossingWarningListener.html -->






<div class="flex-box">

<div class="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">BorderCrossingWarningListener</span></div>
<div class="block"><p>This interface
 should be implemented in order to receive border crossing warnings for country and state borders.
 <strong>Note:</strong> The border crossing warner is a point warner, which means that for a border crossing there will <em>always</em> be
 2 warnings emitted, with the [BorderCrossingWarning.distance_type] set to <a href="sdk-for-android-navigate-distancetype#AHEAD"><code>DistanceType.AHEAD</code></a> and <a href="sdk-for-android-navigate-distancetype#PASSED"><code>DistanceType.PASSED</code></a>
 which is given when the location of the border crossing is reached.
 A <a href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarning" title="class in com.here.sdk.navigation"><code>BorderCrossingWarning</code></a> will not be given until the previous warning of that type has been passed.
 For example, a route with <a href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarning" title="class in com.here.sdk.navigation"><code>BorderCrossingWarning</code></a> 120 meters and <a href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarning" title="class in com.here.sdk.navigation"><code>BorderCrossingWarning</code></a> 160 meters ahead,
 the first [BorderCrossingWarning.distance_to_border_crossing_in_meters] is 120 meters
 and the next [BorderCrossingWarning.distance_to_border_crossing_in_meters] is then 40 meters,
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarninglistener#onBorderCrossingWarningUpdated(com.here.sdk.navigation.BorderCrossingWarning)">onBorderCrossingWarningUpdated</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarning" title="class in com.here.sdk.navigation">BorderCrossingWarning</a> borderCrossingWarning)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Called whenever a new border crossing warning is available.</div>
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
<section class="detail" id="onBorderCrossingWarningUpdated(com.here.sdk.navigation.BorderCrossingWarning)">
<h3>onBorderCrossingWarningUpdated</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onBorderCrossingWarningUpdated</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarning" title="class in com.here.sdk.navigation">BorderCrossingWarning</a> borderCrossingWarning)</span></div>
<div class="block"><p>Called whenever a new border crossing warning is available.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>borderCrossingWarning</code> - <p>The object that contains details on the border crossing warning.</p></dd>
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
</div>



</div>
`
}</HTMLBlock>
