---
title: "com.here.sdk.electronichorizon (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-electronichorizon-package-summary"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- package-summary.html -->









<main role="main">
<div class="header">

</div>
<hr/>
<div class="package-signature">package <span class="element-name">com.here.sdk.electronichorizon</span></div>
<section class="summary">
<ul class="summary-list">
<li>
<div id="class-summary">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="class-summary.tabpanel" aria-selected="true" class="active-table-tab" id="class-summary-tab0" onclick="show('class-summary', 'class-summary', 2)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Classes and Interfaces</button><button aria-controls="class-summary.tabpanel" aria-selected="false" class="table-tab" id="class-summary-tab1" onclick="show('class-summary', 'class-summary-tab1', 2)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Interfaces</button><button aria-controls="class-summary.tabpanel" aria-selected="false" class="table-tab" id="class-summary-tab2" onclick="show('class-summary', 'class-summary-tab2', 2)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Classes</button><button aria-controls="class-summary.tabpanel" aria-selected="false" class="table-tab" id="class-summary-tab3" onclick="show('class-summary', 'class-summary-tab3', 2)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Enum Classes</button></div>
<div aria-labelledby="class-summary-tab0" id="class-summary.tabpanel" role="tabpanel">
<div class="summary-table two-column-summary">
<div class="table-header col-first">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-navigate-electronichorizon" title="class in com.here.sdk.electronichorizon">ElectronicHorizon</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">A class containing the full set of available paths
 predicted for the current vehicle state.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab3"><a href="sdk-for-android-navigate-electronichorizondataloadedstatus" title="enum class in com.here.sdk.electronichorizon">ElectronicHorizonDataLoadedStatus</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab3">
<div class="block">Represents the status of data that was loaded by <a href="sdk-for-android-navigate-electronichorizondataloader" title="class in com.here.sdk.electronichorizon"><code>ElectronicHorizonDataLoader</code></a>.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-navigate-electronichorizondataloader" title="class in com.here.sdk.electronichorizon">ElectronicHorizonDataLoader</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">Loads map data for segments that belong to the <a href="sdk-for-android-navigate-electronichorizonengine" title="class in com.here.sdk.electronichorizon"><code>ElectronicHorizonEngine</code></a> paths.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab3"><a href="sdk-for-android-navigate-electronichorizondataloadererrorcode" title="enum class in com.here.sdk.electronichorizon">ElectronicHorizonDataLoaderErrorCode</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab3">
<div class="block">Represents error codes that describe the result of the <a href="sdk-for-android-navigate-electronichorizondataloader#getSegment(com.here.sdk.mapdata.DirectedOCMSegmentId)"><code>ElectronicHorizonDataLoader.getSegment(com.here.sdk.mapdata.DirectedOCMSegmentId)</code></a> method.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-navigate-electronichorizondataloaderresult" title="class in com.here.sdk.electronichorizon">ElectronicHorizonDataLoaderResult</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">Represents the result of a data loading operation performed by <a href="sdk-for-android-navigate-electronichorizondataloader" title="class in com.here.sdk.electronichorizon"><code>ElectronicHorizonDataLoader</code></a>.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab1"><a href="sdk-for-android-navigate-electronichorizondataloaderstatuslistener" title="interface in com.here.sdk.electronichorizon">ElectronicHorizonDataLoaderStatusListener</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab1">
<div class="block">Provides a listener for status updates from the <a href="sdk-for-android-navigate-electronichorizondataloader#loadData(com.here.sdk.electronichorizon.ElectronicHorizonUpdate)"><code>ElectronicHorizonDataLoader.loadData(com.here.sdk.electronichorizon.ElectronicHorizonUpdate)</code></a> method.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-navigate-electronichorizonengine" title="class in com.here.sdk.electronichorizon">ElectronicHorizonEngine</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">Provides an electronic horizon engine that continuously predicts
 the road network ahead of the vehicle by using detailed map data, including road topography that is
 currently out of sight.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab3"><a href="sdk-for-android-navigate-electronichorizonerrorcode" title="enum class in com.here.sdk.electronichorizon">ElectronicHorizonErrorCode</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab3">
<div class="block">Represents error codes that describe the result of the <a href="sdk-for-android-navigate-electronichorizonengine#update(com.here.sdk.navigation.MapMatchedLocation)"><code>ElectronicHorizonEngine.update(com.here.sdk.navigation.MapMatchedLocation)</code></a> method.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab1"><a href="sdk-for-android-navigate-electronichorizonlistener" title="interface in com.here.sdk.electronichorizon">ElectronicHorizonListener</a></div>
<div class="col-last even-row-color class-summary class-summary-tab1">
<div class="block">Provides a listener for receiving updates during execution of the <a href="sdk-for-android-navigate-electronichorizonengine#update(com.here.sdk.navigation.MapMatchedLocation)"><code>ElectronicHorizonEngine.update(com.here.sdk.navigation.MapMatchedLocation)</code></a> method.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-navigate-electronichorizonoptions" title="class in com.here.sdk.electronichorizon">ElectronicHorizonOptions</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">Provides options to configure <a href="sdk-for-android-navigate-electronichorizonengine" title="class in com.here.sdk.electronichorizon"><code>ElectronicHorizonEngine</code></a>.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-navigate-electronichorizonpath" title="class in com.here.sdk.electronichorizon">ElectronicHorizonPath</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">Represents a single electronic horizon path.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-navigate-electronichorizonposition" title="class in com.here.sdk.electronichorizon">ElectronicHorizonPosition</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">Provides a position on an electronic horizon path with a reference to the current item in the <a href="sdk-for-android-navigate-electronichorizon" title="class in com.here.sdk.electronichorizon"><code>ElectronicHorizon</code></a>.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-navigate-electronichorizonsegment" title="class in com.here.sdk.electronichorizon">ElectronicHorizonSegment</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">Represents a segment in an <a href="sdk-for-android-navigate-electronichorizonpath" title="class in com.here.sdk.electronichorizon"><code>ElectronicHorizonPath</code></a>.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-navigate-electronichorizonsegmentchanges" title="class in com.here.sdk.electronichorizon">ElectronicHorizonSegmentChanges</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">A class describing the set of changes in horizon segments
 between two consecutive updates.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-navigate-electronichorizonsegmentid" title="class in com.here.sdk.electronichorizon">ElectronicHorizonSegmentId</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">Identifies a segment in an <a href="sdk-for-android-navigate-electronichorizonpath" title="class in com.here.sdk.electronichorizon"><code>ElectronicHorizonPath</code></a>.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-navigate-electronichorizonupdate" title="class in com.here.sdk.electronichorizon">ElectronicHorizonUpdate</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">A class representing a full update delivered via <a href="sdk-for-android-navigate-electronichorizonlistener" title="interface in com.here.sdk.electronichorizon"><code>ElectronicHorizonListener</code></a> notifications.</div>
</div>
</div>
</div>
</div>
</li>
</ul>
</section>
</main>





</div>
`
}</HTMLBlock>
