---
title: "MapIdleListener (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapidlelistener"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- MapIdleListener.html -->









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-com-here-sdk-mapview-package-summary">com.here.sdk.mapview</a></div>

</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">MapIdleListener</span></div>
<div class="block"><p>Used to detect when the map becomes idle or busy.
 </p><p>Map is considered busy when its state changes (for example as a result of camera manipulation)
 and/or when it requires a redraw (for example, as a result of map data being downloaded).
 </p><p>Map is considered idle when current state is fully rendered and no further
 redraws are necessary.</p></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-explore-index#onMapBusy()">onMapBusy</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Called when map becomes invalidated and is about to be updated.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-explore-index#onMapIdle()">onMapIdle</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Called when map finishes all state updates.</div>
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
<section class="detail" id="onMapBusy()">
<h3>onMapBusy</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onMapBusy</span>()</div>
<div class="block"><p>Called when map becomes invalidated and is about to be updated. One or more
 redraws will happen afterwards, until <a href="sdk-for-android-explore-index#onMapIdle()"><code>onMapIdle()</code></a> is called.</p></div>
</section>
</li>
<li>
<section class="detail" id="onMapIdle()">
<h3>onMapIdle</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onMapIdle</span>()</div>
<div class="block"><p>Called when map finishes all state updates. No state changes or redraws
 will happen aftrwards until <a href="sdk-for-android-explore-index#onMapBusy()"><code>onMapBusy()</code></a> is called.</p></div>
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
