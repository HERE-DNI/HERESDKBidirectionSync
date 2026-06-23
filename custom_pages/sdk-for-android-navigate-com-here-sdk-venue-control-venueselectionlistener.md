---
title: "VenueSelectionListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-venue-control-venueselectionlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- VenueSelectionListener.html -->










<!-- ======== START OF CLASS DATA ======== -->

<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">VenueSelectionListener</span></div>
<div class="block"><p>The interface for listeners for
 the <a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a> selection event. Use the <a href="sdk-for-android-navigate-venuemap" title="class in com.here.sdk.venue.control"><code>VenueMap</code></a>
 to add and remove the <a href="sdk-for-android-navigate-venueselectionlistener" title="interface in com.here.sdk.venue.control"><code>VenueSelectionListener</code></a>.</p></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-navigate-index#onSelectedVenueChanged(com.here.sdk.venue.control.Venue,com.here.sdk.venue.control.Venue)">onSelectedVenueChanged</a><wbr/>(<a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control">Venue</a> deselectedVenue,
 <a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control">Venue</a> selectedVenue)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Indicates that the current selected <a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a> changed.</div>
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
<section class="detail" id="onSelectedVenueChanged(com.here.sdk.venue.control.Venue,com.here.sdk.venue.control.Venue)">
<h3>onSelectedVenueChanged</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onSelectedVenueChanged</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control">Venue</a> deselectedVenue,
 @Nullable
 <a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control">Venue</a> selectedVenue)</span></div>
<div class="block"><p>Indicates that the current selected <a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a> changed.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>deselectedVenue</code> - <p>The <a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a> that was deselected or <code>null</code>
     if there was no selected venue before.</p></dd>
<dd><code>selectedVenue</code> - <p>The <a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a> that was selected or <code>null</code>
     if there was no new selected venue.</p></dd>
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
