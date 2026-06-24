---
title: "ElectronicHorizonDataLoaderStatusListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizondataloaderstatuslistener"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- ElectronicHorizonDataLoaderStatusListener.html -->










<!-- ======== START OF CLASS DATA ======== -->

<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">ElectronicHorizonDataLoaderStatusListener</span></div>
<div class="block"><p>Provides a listener for status updates from the <a href="sdk-for-android-navigate-electronichorizondataloader#loadData(com.here.sdk.electronichorizon.ElectronicHorizonUpdate)"><code>ElectronicHorizonDataLoader.loadData(com.here.sdk.electronichorizon.ElectronicHorizonUpdate)</code></a> method.
 The listener receives the current state for different levels of the paths as <a href="sdk-for-android-navigate-electronichorizondataloadedstatus" title="enum class in com.here.sdk.electronichorizon"><code>ElectronicHorizonDataLoadedStatus</code></a>.
 </p><p>Note: This is a <strong>beta</strong> release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizondataloaderstatuslistener#onElectronicHorizonDataLoaderStatusUpdated(java.util.Map)">onElectronicHorizonDataLoaderStatusUpdated</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>,<wbr/><a href="sdk-for-android-navigate-electronichorizondataloadedstatus" title="enum class in com.here.sdk.electronichorizon">ElectronicHorizonDataLoadedStatus</a>&gt; electronicHorizonDataLoaderStatuses)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Called whenever there is a change in the status of the loaded data from <a href="sdk-for-android-navigate-electronichorizondataloader" title="class in com.here.sdk.electronichorizon"><code>ElectronicHorizonDataLoader</code></a>.</div>
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
<section class="detail" id="onElectronicHorizonDataLoaderStatusUpdated(java.util.Map)">
<h3>onElectronicHorizonDataLoaderStatusUpdated</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onElectronicHorizonDataLoaderStatusUpdated</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>,<wbr/><a href="sdk-for-android-navigate-electronichorizondataloadedstatus" title="enum class in com.here.sdk.electronichorizon">ElectronicHorizonDataLoadedStatus</a>&gt; electronicHorizonDataLoaderStatuses)</span></div>
<div class="block"><p>Called whenever there is a change in the status of the loaded data from <a href="sdk-for-android-navigate-electronichorizondataloader" title="class in com.here.sdk.electronichorizon"><code>ElectronicHorizonDataLoader</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>electronicHorizonDataLoaderStatuses</code> - <p>The updated statuses of the loaded data from <a href="sdk-for-android-navigate-electronichorizondataloader" title="class in com.here.sdk.electronichorizon"><code>ElectronicHorizonDataLoader</code></a>.
     The key is the level of a <code>ElectronicHorizonPath</code>, the value is the current status.</p></dd>
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
