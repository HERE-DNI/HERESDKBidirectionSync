---
title: "SegmentDataLoaderOptions (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloaderoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- SegmentDataLoaderOptions.html -->









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-mapdata-package-summary">com.here.sdk.mapdata</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.mapdata.SegmentDataLoaderOptions</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">SegmentDataLoaderOptions</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Specifies which data should be loaded by the <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> or <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> function.
 </p><p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
 behaviors. Related APIs may change for new releases without a deprecation process.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">

<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#loadAdministrativeRules">loadAdministrativeRules</a></code></div>
<div class="col-last even-row-color">
<div class="block">If it is true, <a href="sdk-for-android-navigate-segmentspandata#getAdministrativeRules()"><code>SegmentSpanData.getAdministrativeRules()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> or <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#loadBaseSpeeds">loadBaseSpeeds</a></code></div>
<div class="col-last odd-row-color">
<div class="block">If it is true, <a href="sdk-for-android-navigate-segmentspandata#getPositiveDirectionBaseSpeedInMetersPerSecond()"><code>SegmentSpanData.getPositiveDirectionBaseSpeedInMetersPerSecond()</code></a>,
 <a href="sdk-for-android-navigate-segmentspandata#getNegativeDirectionBaseSpeedInMetersPerSecond()"><code>SegmentSpanData.getNegativeDirectionBaseSpeedInMetersPerSecond()</code></a> and <a href="sdk-for-android-navigate-segmentspandata#getBaseSpeedInMetersPerSecond()"><code>SegmentSpanData.getBaseSpeedInMetersPerSecond()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> or
 <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.</div>
</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#loadFunctionalRoadClass">loadFunctionalRoadClass</a></code></div>
<div class="col-last even-row-color">
<div class="block">If it is true, the <a href="sdk-for-android-navigate-segmentspandata#getFunctionalRoadClass()"><code>SegmentSpanData.getFunctionalRoadClass()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> or
 <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#loadLocalRoadCharacteristics">loadLocalRoadCharacteristics</a></code></div>
<div class="col-last odd-row-color">
<div class="block">If it is true, <a href="sdk-for-android-navigate-segmentspandata#getLocalRoadCharacteristics()"><code>SegmentSpanData.getLocalRoadCharacteristics()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> or
 <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.</div>
</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#loadRailwayCrossings">loadRailwayCrossings</a></code></div>
<div class="col-last even-row-color">
<div class="block">If it is true, <a href="sdk-for-android-navigate-segmentdata#getRailwayCrossings()"><code>SegmentData.getRailwayCrossings()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> or <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#loadRoadAttributes">loadRoadAttributes</a></code></div>
<div class="col-last odd-row-color">
<div class="block">If it is true, <a href="sdk-for-android-navigate-segmentspandata#getPhysicalAttributes()"><code>SegmentSpanData.getPhysicalAttributes()</code></a> and
 <a href="sdk-for-android-navigate-segmentspandata#getRoadUsages()"><code>SegmentSpanData.getRoadUsages()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> or
 <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.</div>
</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#loadRoadSigns">loadRoadSigns</a></code></div>
<div class="col-last even-row-color">
<div class="block">If it is true, <a href="sdk-for-android-navigate-segmentdata#getRoadSigns()"><code>SegmentData.getRoadSigns()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> or <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#loadSpecialSpeedSituations">loadSpecialSpeedSituations</a></code></div>
<div class="col-last odd-row-color">
<div class="block">If it is true, <a href="sdk-for-android-navigate-segmentspandata#getSpecialSpeedSituations()"><code>SegmentSpanData.getSpecialSpeedSituations()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.</div>
</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#loadSpeedLimits">loadSpeedLimits</a></code></div>
<div class="col-last even-row-color">
<div class="block">If it is true, <a href="sdk-for-android-navigate-segmentspandata#getPositiveDirectionSpeedLimit()"><code>SegmentSpanData.getPositiveDirectionSpeedLimit()</code></a>,
 <a href="sdk-for-android-navigate-segmentspandata#getNegativeDirectionSpeedLimit()"><code>SegmentSpanData.getNegativeDirectionSpeedLimit()</code></a> and <a href="sdk-for-android-navigate-segmentspandata#getSpeedLimit()"><code>SegmentSpanData.getSpeedLimit()</code></a> will be loaded
 when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> or <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#loadStreetNamesAndRoadNumbers">loadStreetNamesAndRoadNumbers</a></code></div>
<div class="col-last odd-row-color">
<div class="block">If it is true, <a href="sdk-for-android-navigate-segmentspandata#getStreetNames()"><code>SegmentSpanData.getStreetNames()</code></a> and <a href="sdk-for-android-navigate-segmentspandata#getRoadNumbers()"><code>SegmentSpanData.getRoadNumbers()</code></a> and will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> or
 <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.</div>
</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#loadTollPoints">loadTollPoints</a></code></div>
<div class="col-last even-row-color">
<div class="block">If it is true, <a href="sdk-for-android-navigate-segmentdata#getTollPoints()"><code>SegmentData.getTollPoints()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#loadTrafficSignals">loadTrafficSignals</a></code></div>
<div class="col-last odd-row-color">
<div class="block">If it is true, <a href="sdk-for-android-navigate-segmentdata#getTrafficSignals()"><code>SegmentData.getTrafficSignals()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> or <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.</div>
</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#loadTransportModesAccess">loadTransportModesAccess</a></code></div>
<div class="col-last even-row-color">
<div class="block">If it is true, <a href="sdk-for-android-navigate-segmentspandata#getAllowedTransportModes()"><code>SegmentSpanData.getAllowedTransportModes()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> or
 <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#loadTravelDirection">loadTravelDirection</a></code></div>
<div class="col-last odd-row-color">
<div class="block">If it is true, the <a href="sdk-for-android-navigate-segmentspandata#getTravelDirection()"><code>SegmentSpanData.getTravelDirection()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> or
 <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.</div>
</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#loadUrban">loadUrban</a></code></div>
<div class="col-last even-row-color">
<div class="block">If it is true, <a href="sdk-for-android-navigate-segmentspandata#isUrban()"><code>SegmentSpanData.isUrban()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#%3Cinit%3E()">SegmentDataLoaderOptions</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#hashCode()">hashCode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">

<ul class="member-list">
<li>
<section class="detail" id="loadTravelDirection">
<h3>loadTravelDirection</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">loadTravelDirection</span></div>
<div class="block"><p>If it is true, the <a href="sdk-for-android-navigate-segmentspandata#getTravelDirection()"><code>SegmentSpanData.getTravelDirection()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> or
 <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.</p></div>
</section>
</li>
<li>
<section class="detail" id="loadFunctionalRoadClass">
<h3>loadFunctionalRoadClass</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">loadFunctionalRoadClass</span></div>
<div class="block"><p>If it is true, the <a href="sdk-for-android-navigate-segmentspandata#getFunctionalRoadClass()"><code>SegmentSpanData.getFunctionalRoadClass()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> or
 <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.</p></div>
</section>
</li>
<li>
<section class="detail" id="loadTransportModesAccess">
<h3>loadTransportModesAccess</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">loadTransportModesAccess</span></div>
<div class="block"><p>If it is true, <a href="sdk-for-android-navigate-segmentspandata#getAllowedTransportModes()"><code>SegmentSpanData.getAllowedTransportModes()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> or
 <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.</p></div>
</section>
</li>
<li>
<section class="detail" id="loadSpeedLimits">
<h3>loadSpeedLimits</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">loadSpeedLimits</span></div>
<div class="block"><p>If it is true, <a href="sdk-for-android-navigate-segmentspandata#getPositiveDirectionSpeedLimit()"><code>SegmentSpanData.getPositiveDirectionSpeedLimit()</code></a>,
 <a href="sdk-for-android-navigate-segmentspandata#getNegativeDirectionSpeedLimit()"><code>SegmentSpanData.getNegativeDirectionSpeedLimit()</code></a> and <a href="sdk-for-android-navigate-segmentspandata#getSpeedLimit()"><code>SegmentSpanData.getSpeedLimit()</code></a> will be loaded
 when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> or <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.</p></div>
</section>
</li>
<li>
<section class="detail" id="loadBaseSpeeds">
<h3>loadBaseSpeeds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">loadBaseSpeeds</span></div>
<div class="block"><p>If it is true, <a href="sdk-for-android-navigate-segmentspandata#getPositiveDirectionBaseSpeedInMetersPerSecond()"><code>SegmentSpanData.getPositiveDirectionBaseSpeedInMetersPerSecond()</code></a>,
 <a href="sdk-for-android-navigate-segmentspandata#getNegativeDirectionBaseSpeedInMetersPerSecond()"><code>SegmentSpanData.getNegativeDirectionBaseSpeedInMetersPerSecond()</code></a> and <a href="sdk-for-android-navigate-segmentspandata#getBaseSpeedInMetersPerSecond()"><code>SegmentSpanData.getBaseSpeedInMetersPerSecond()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> or
 <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.</p></div>
</section>
</li>
<li>
<section class="detail" id="loadLocalRoadCharacteristics">
<h3>loadLocalRoadCharacteristics</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">loadLocalRoadCharacteristics</span></div>
<div class="block"><p>If it is true, <a href="sdk-for-android-navigate-segmentspandata#getLocalRoadCharacteristics()"><code>SegmentSpanData.getLocalRoadCharacteristics()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> or
 <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.</p></div>
</section>
</li>
<li>
<section class="detail" id="loadStreetNamesAndRoadNumbers">
<h3>loadStreetNamesAndRoadNumbers</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">loadStreetNamesAndRoadNumbers</span></div>
<div class="block"><p>If it is true, <a href="sdk-for-android-navigate-segmentspandata#getStreetNames()"><code>SegmentSpanData.getStreetNames()</code></a> and <a href="sdk-for-android-navigate-segmentspandata#getRoadNumbers()"><code>SegmentSpanData.getRoadNumbers()</code></a> and will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> or
 <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.</p></div>
</section>
</li>
<li>
<section class="detail" id="loadRoadAttributes">
<h3>loadRoadAttributes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">loadRoadAttributes</span></div>
<div class="block"><p>If it is true, <a href="sdk-for-android-navigate-segmentspandata#getPhysicalAttributes()"><code>SegmentSpanData.getPhysicalAttributes()</code></a> and
 <a href="sdk-for-android-navigate-segmentspandata#getRoadUsages()"><code>SegmentSpanData.getRoadUsages()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> or
 <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.</p></div>
</section>
</li>
<li>
<section class="detail" id="loadTrafficSignals">
<h3>loadTrafficSignals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">loadTrafficSignals</span></div>
<div class="block"><p>If it is true, <a href="sdk-for-android-navigate-segmentdata#getTrafficSignals()"><code>SegmentData.getTrafficSignals()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> or <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.
 Defaults to <code>false</code>.</p></div>
</section>
</li>
<li>
<section class="detail" id="loadRoadSigns">
<h3>loadRoadSigns</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">loadRoadSigns</span></div>
<div class="block"><p>If it is true, <a href="sdk-for-android-navigate-segmentdata#getRoadSigns()"><code>SegmentData.getRoadSigns()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> or <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.
 Defaults to <code>false</code>.</p></div>
</section>
</li>
<li>
<section class="detail" id="loadAdministrativeRules">
<h3>loadAdministrativeRules</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">loadAdministrativeRules</span></div>
<div class="block"><p>If it is true, <a href="sdk-for-android-navigate-segmentspandata#getAdministrativeRules()"><code>SegmentSpanData.getAdministrativeRules()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> or <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.
 Defaults to <code>false</code>.</p></div>
</section>
</li>
<li>
<section class="detail" id="loadRailwayCrossings">
<h3>loadRailwayCrossings</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">loadRailwayCrossings</span></div>
<div class="block"><p>If it is true, <a href="sdk-for-android-navigate-segmentdata#getRailwayCrossings()"><code>SegmentData.getRailwayCrossings()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> or <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.
 Defaults to <code>false</code>.</p></div>
</section>
</li>
<li>
<section class="detail" id="loadUrban">
<h3>loadUrban</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">loadUrban</span></div>
<div class="block"><p>If it is true, <a href="sdk-for-android-navigate-segmentspandata#isUrban()"><code>SegmentSpanData.isUrban()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.
 Defaults to <code>false</code>.</p></div>
</section>
</li>
<li>
<section class="detail" id="loadSpecialSpeedSituations">
<h3>loadSpecialSpeedSituations</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">loadSpecialSpeedSituations</span></div>
<div class="block"><p>If it is true, <a href="sdk-for-android-navigate-segmentspandata#getSpecialSpeedSituations()"><code>SegmentSpanData.getSpecialSpeedSituations()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.
 <strong>Note:</strong> To get timezone offset and daylight saving time values for TimeRule, [sdk.mapdata.SegmentDataLoaderOptions.load_administrative_rules] must also be set to <code>true</code>.
 Defaults to <code>false</code>.</p></div>
</section>
</li>
<li>
<section class="detail" id="loadTollPoints">
<h3>loadTollPoints</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">loadTollPoints</span></div>
<div class="block"><p>If it is true, <a href="sdk-for-android-navigate-segmentdata#getTollPoints()"><code>SegmentData.getTollPoints()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.
 Defaults to <code>false</code>.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>SegmentDataLoaderOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SegmentDataLoaderOptions</span>()</div>
<div class="block"><p>Creates a new instance.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hashCode()">
<h3>hashCode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
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
