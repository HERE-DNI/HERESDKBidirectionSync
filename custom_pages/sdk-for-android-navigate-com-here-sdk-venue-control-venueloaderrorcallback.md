---
title: "VenueLoadErrorCallback (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-venue-control-venueloaderrorcallback"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- VenueLoadErrorCallback.html -->






<div class="flex-box">

<div class="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.venue.control</a></div>

</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Functional Interface:</dt>
<dd>This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.</dd>
</dl>

<div class="type-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html" title="class or interface in java.lang">@FunctionalInterface</a>
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">VenueLoadErrorCallback</span></div>
<div class="block"><p>A method which is called on the main thread when <a href="sdk-for-android-navigate-venuemap#selectVenueAsync(java.lang.String,com.here.sdk.venue.control.VenueLoadErrorCallback)"><code>VenueMap.selectVenueAsync(String, VenueLoadErrorCallback)</code></a> has been completed.</p></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-control-venueloaderrorcallback#onVenueLoadError(com.here.sdk.venue.control.VenueErrorCode)">onVenueLoadError</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-venue-control-venueerrorcode" title="enum class in com.here.sdk.venue.control">VenueErrorCode</a> error)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">A method which is called on the main thread when <a href="sdk-for-android-navigate-venuemap#selectVenueAsync(java.lang.String,com.here.sdk.venue.control.VenueLoadErrorCallback)"><code>VenueMap.selectVenueAsync(String, VenueLoadErrorCallback)</code></a> has been completed.</div>
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
<section class="detail" id="onVenueLoadError(com.here.sdk.venue.control.VenueErrorCode)">
<h3>onVenueLoadError</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onVenueLoadError</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-venue-control-venueerrorcode" title="enum class in com.here.sdk.venue.control">VenueErrorCode</a> error)</span></div>
<div class="block"><p>A method which is called on the main thread when <a href="sdk-for-android-navigate-venuemap#selectVenueAsync(java.lang.String,com.here.sdk.venue.control.VenueLoadErrorCallback)"><code>VenueMap.selectVenueAsync(String, VenueLoadErrorCallback)</code></a> has been completed.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>error</code> - <p>Represents an error in case of a failure. It is <code>null</code> for an operation that succeeds.</p></dd>
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
