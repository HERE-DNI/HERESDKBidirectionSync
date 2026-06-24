---
title: "ElectronicHorizonListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- ElectronicHorizonListener.html -->










<!-- ======== START OF CLASS DATA ======== -->

<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="sdk-for-android-navigate-warnerengine" title="class in com.here.sdk.warner">WarnerEngine</a></code></dd>
</dl>

<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">ElectronicHorizonListener</span></div>
<div class="block"><p>Provides a listener for receiving updates during execution of the <a href="sdk-for-android-navigate-electronichorizonengine#update(com.here.sdk.navigation.MapMatchedLocation)"><code>ElectronicHorizonEngine.update(com.here.sdk.navigation.MapMatchedLocation)</code></a> method.
 </p><p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
 behaviors. Related APIs may change for new releases without a deprecation process.
 </p><p>Offline availability: This property is available online and offline.</p></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonlistener#onElectronicHorizonUpdated(com.here.sdk.electronichorizon.ElectronicHorizonErrorCode,com.here.sdk.electronichorizon.ElectronicHorizonUpdate)">onElectronicHorizonUpdated</a><wbr/>(<a href="sdk-for-android-navigate-electronichorizonerrorcode" title="enum class in com.here.sdk.electronichorizon">ElectronicHorizonErrorCode</a> errorCode,
 <a href="sdk-for-android-navigate-electronichorizonupdate" title="class in com.here.sdk.electronichorizon">ElectronicHorizonUpdate</a> update)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Called whenever the electronic horizon subsystem produces:
 
 a new update,
 an error,
 </div>
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
<section class="detail" id="onElectronicHorizonUpdated(com.here.sdk.electronichorizon.ElectronicHorizonErrorCode,com.here.sdk.electronichorizon.ElectronicHorizonUpdate)">
<h3>onElectronicHorizonUpdated</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onElectronicHorizonUpdated</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-electronichorizonerrorcode" title="enum class in com.here.sdk.electronichorizon">ElectronicHorizonErrorCode</a> errorCode,
 @Nullable
 <a href="sdk-for-android-navigate-electronichorizonupdate" title="class in com.here.sdk.electronichorizon">ElectronicHorizonUpdate</a> update)</span></div>
<div class="block"><p>Called whenever the electronic horizon subsystem produces:
 <ul>
<li>a new update,</li>
<li>an error,</li>
</ul>
</p><p>The client must inspect <code>error_code</code> to determine whether the call
 represents an error or a valid update.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>errorCode</code> - <p>The error associated with the horizon computation.
     <code>null</code> means no error.</p></dd>
<dd><code>update</code> - <p>The update describing the current electronic horizon state.
     May be <code>null</code> if an update could not be produced.
     </p><p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
     behaviors. Related APIs may change for new releases without a deprecation process.</p></dd>
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
