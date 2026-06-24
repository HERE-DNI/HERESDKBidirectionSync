---
title: "VenueListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-venue-service-venuelistener"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- VenueListener.html -->










<!-- ======== START OF CLASS DATA ======== -->

<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">VenueListener</span></div>
<div class="block"><p>The interface for listeners for
 venue loading events in <a href="sdk-for-android-navigate-venueservice" title="class in com.here.sdk.venue.service"><code>VenueService</code></a>.</p></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-service-venuelistener#onGetVenueCompleted(int,com.here.sdk.venue.data.VenueModel,boolean,com.here.sdk.venue.style.VenueStyle)">onGetVenueCompleted</a><wbr/>(int venueId,
 <a href="sdk-for-android-navigate-venuemodel" title="class in com.here.sdk.venue.data">VenueModel</a> venueModel,
 boolean online,
 <a href="sdk-for-android-navigate-venuestyle" title="class in com.here.sdk.venue.style">VenueStyle</a> venueStyle)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Called when loading of a venue or its retrieval from the cache is completed.</div>
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
<section class="detail" id="onGetVenueCompleted(int,com.here.sdk.venue.data.VenueModel,boolean,com.here.sdk.venue.style.VenueStyle)">
<h3>onGetVenueCompleted</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onGetVenueCompleted</span><wbr/><span class="parameters">(int venueId,
 @Nullable
 <a href="sdk-for-android-navigate-venuemodel" title="class in com.here.sdk.venue.data">VenueModel</a> venueModel,
 boolean online,
 @Nullable
 <a href="sdk-for-android-navigate-venuestyle" title="class in com.here.sdk.venue.style">VenueStyle</a> venueStyle)</span></div>
<div class="block"><p>Called when loading of a venue or its retrieval from the cache is completed.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>venueId</code> - <p>The id of the venue.</p></dd>
<dd><code>venueModel</code> - <p>The venue model.</p></dd>
<dd><code>online</code> - <p><code>True</code> if a new venue was loaded from the server and <code>false</code> otherwise.</p></dd>
<dd><code>venueStyle</code> - <p>The style associated with the venue.</p></dd>
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
