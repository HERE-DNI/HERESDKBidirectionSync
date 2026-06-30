---
title: "InterpolatedLocationListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-interpolatedlocationlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- InterpolatedLocationListener.html -->










<!-- ======== START OF CLASS DATA ======== -->

<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">InterpolatedLocationListener</span></div>
<div class="block"><p>This interface should be implemented
 in order to receive interpolated locations. The interpolated locations are only provided between
 <a href="sdk-for-android-navigate-visualnavigator#startRendering(com.here.sdk.mapview.MapViewBase)"><code>VisualNavigator.startRendering(com.here.sdk.mapview.MapViewBase)</code></a> and <a href="sdk-for-android-navigate-visualnavigator#stopRendering()"><code>VisualNavigator.stopRendering()</code></a> calls and the application
 is not running in the background.</p></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-interpolatedlocationlistener#onInterpolatedLocationUpdated(com.here.sdk.core.Location)">onInterpolatedLocationUpdated</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-location" title="class in com.here.sdk.core">Location</a> location)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Called whenever a new interpolated location is calculated, usually several times per second.</div>
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
<section class="detail" id="onInterpolatedLocationUpdated(com.here.sdk.core.Location)">
<h3>onInterpolatedLocationUpdated</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onInterpolatedLocationUpdated</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-location" title="class in com.here.sdk.core">Location</a> location)</span></div>
<div class="block"><p>Called whenever a new interpolated location is calculated, usually several times per second.
 The interpolated locations are only provided between <a href="sdk-for-android-navigate-visualnavigator#startRendering(com.here.sdk.mapview.MapViewBase)"><code>VisualNavigator.startRendering(com.here.sdk.mapview.MapViewBase)</code></a> and
 <a href="sdk-for-android-navigate-visualnavigator#stopRendering()"><code>VisualNavigator.stopRendering()</code></a> calls and the application is not running in the background.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>location</code> - <p>The interpolated location.</p></dd>
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
