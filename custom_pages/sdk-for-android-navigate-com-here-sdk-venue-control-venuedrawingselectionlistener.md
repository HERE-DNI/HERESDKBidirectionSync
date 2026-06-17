---
title: "VenueDrawingSelectionListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-venue-control-venuedrawingselectionlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- VenueDrawingSelectionListener.html -->
<!DOCTYPE HTML>









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-package-summary">com.here.sdk.venue.control</a></div>

</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">VenueDrawingSelectionListener</span></div>
<div class="block"><p>The interface for listeners for
 the <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-venuedrawing" title="class in com.here.sdk.venue.data"><code>VenueDrawing</code></a> selection event. Use the <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-venuemap" title="class in com.here.sdk.venue.control"><code>VenueMap</code></a>
 to add and remove the <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-venuedrawingselectionlistener" title="interface in com.here.sdk.venue.control"><code>VenueDrawingSelectionListener</code></a>.</p></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#onDrawingSelected(com.here.sdk.venue.control.Venue,com.here.sdk.venue.data.VenueDrawing,com.here.sdk.venue.data.VenueDrawing)">onDrawingSelected</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control">Venue</a> venue,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-venuedrawing" title="class in com.here.sdk.venue.data">VenueDrawing</a> deselectedDrawing,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-venuedrawing" title="class in com.here.sdk.venue.data">VenueDrawing</a> selectedDrawing)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Indicates that new <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-venuedrawing" title="class in com.here.sdk.venue.data"><code>VenueDrawing</code></a> has been selected.</div>
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
<section class="detail" id="onDrawingSelected(com.here.sdk.venue.control.Venue,com.here.sdk.venue.data.VenueDrawing,com.here.sdk.venue.data.VenueDrawing)">
<h3>onDrawingSelected</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onDrawingSelected</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control">Venue</a> venue,
 @Nullable
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-venuedrawing" title="class in com.here.sdk.venue.data">VenueDrawing</a> deselectedDrawing,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-venuedrawing" title="class in com.here.sdk.venue.data">VenueDrawing</a> selectedDrawing)</span></div>
<div class="block"><p>Indicates that new <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-venuedrawing" title="class in com.here.sdk.venue.data"><code>VenueDrawing</code></a> has been selected.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>venue</code> - <p>The <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a> where a selected drawing was changed.</p></dd>
<dd><code>deselectedDrawing</code> - <p>The previously selected <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-venuedrawing" title="class in com.here.sdk.venue.data"><code>VenueDrawing</code></a> object or <code>null</code>
     if there was no selected drawing before.</p></dd>
<dd><code>selectedDrawing</code> - <p>The new selected <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-venuedrawing" title="class in com.here.sdk.venue.data"><code>VenueDrawing</code></a> object.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>





</div>
`
}</HTMLBlock>
