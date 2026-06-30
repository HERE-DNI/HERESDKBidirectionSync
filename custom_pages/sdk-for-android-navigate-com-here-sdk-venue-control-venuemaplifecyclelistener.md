---
title: "VenueMapLifecycleListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-venue-control-venuemaplifecyclelistener"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- VenueMapLifecycleListener.html -->










<!-- ======== START OF CLASS DATA ======== -->

<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">VenueMapLifecycleListener</span></div>
<div class="block"><p>The interface for listeners for
 the <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a> lifecycle events. Use the <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venuemap" title="class in com.here.sdk.venue.control"><code>VenueMap</code></a>
 to add and remove the <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venuemaplifecyclelistener" title="interface in com.here.sdk.venue.control"><code>VenueMapLifecycleListener</code></a>.</p></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-control-venuemaplifecyclelistener#onVenueAdded(com.here.sdk.venue.control.Venue)">onVenueAdded</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control">Venue</a> venue)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Indicates that a <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a> was added to the <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venuemap" title="class in com.here.sdk.venue.control"><code>VenueMap</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-control-venuemaplifecyclelistener#onVenueRemoved(java.lang.String)">onVenueRemoved</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> venueIdentifier)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Indicates that a <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a> was removed from the <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venuemap" title="class in com.here.sdk.venue.control"><code>VenueMap</code></a>.</div>
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
<section class="detail" id="onVenueAdded(com.here.sdk.venue.control.Venue)">
<h3>onVenueAdded</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onVenueAdded</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control">Venue</a> venue)</span></div>
<div class="block"><p>Indicates that a <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a> was added to the <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venuemap" title="class in com.here.sdk.venue.control"><code>VenueMap</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>venue</code> - <p>The created <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="onVenueRemoved(java.lang.String)">
<h3>onVenueRemoved</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onVenueRemoved</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> venueIdentifier)</span></div>
<div class="block"><p>Indicates that a <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a> was removed from the <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venuemap" title="class in com.here.sdk.venue.control"><code>VenueMap</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>venueIdentifier</code> - <p>The destroyed venue id, that can be obtained from the <a href="sdk-for-android-navigate-venuemodel#getId()"><code>VenueModel.getId()</code></a>.</p></dd>
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
