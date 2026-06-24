---
title: "MatchedLocationListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapmatcher-matchedlocationlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- MatchedLocationListener.html -->










<!-- ======== START OF CLASS DATA ======== -->

<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">MatchedLocationListener</span></div>
<div class="block"><p>This interface should be implemented to receive notifications
 about the current location from <a href="sdk-for-android-navigate-mapmatchedlocation" title="class in com.here.sdk.navigation"><code>MapMatchedLocation</code></a>.
 </p><p><strong>Note:</strong> This is a <strong>beta</strong> release of this feature. There may be bugs and unexpected
 behaviors. Related APIs may change in future releases without a deprecation process.</p></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapmatcher-matchedlocationlistener#onMatchedLocationUpdated(com.here.sdk.mapmatcher.MatchedLocation)">onMatchedLocationUpdated</a><wbr/>(<a href="sdk-for-android-navigate-matchedlocation" title="class in com.here.sdk.mapmatcher">MatchedLocation</a> matchedLocation)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Called whenever the current map-matched location has been updated.</div>
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
<section class="detail" id="onMatchedLocationUpdated(com.here.sdk.mapmatcher.MatchedLocation)">
<h3>onMatchedLocationUpdated</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onMatchedLocationUpdated</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-matchedlocation" title="class in com.here.sdk.mapmatcher">MatchedLocation</a> matchedLocation)</span></div>
<div class="block"><p>Called whenever the current map-matched location has been updated.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>matchedLocation</code> - <p>The current matched location update.</p></dd>
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
