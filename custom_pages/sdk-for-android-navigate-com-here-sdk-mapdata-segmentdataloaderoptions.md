---
title: "SegmentDataLoaderOptions (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloaderoptions"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- SegmentDataLoaderOptions.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapdata</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.mapdata.SegmentDataLoaderOptions</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">SegmentDataLoaderOptions</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Specifies which data should be loaded by the <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> or <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> function.
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
 behaviors. Related APIs may change for new releases without a deprecation process.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>boolean</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloaderoptions#loadAdministrativeRules">loadAdministrativeRules</a></code></div>
<div className="col-last even-row-color">
<div className="block">If it is true, <a href="sdk-for-android-navigate-segmentspandata#getAdministrativeRules()"><code>SegmentSpanData.getAdministrativeRules()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> or <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.</div>
</div>
<div className="col-first odd-row-color"><code>boolean</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloaderoptions#loadBaseSpeeds">loadBaseSpeeds</a></code></div>
<div className="col-last odd-row-color">
<div className="block">If it is true, <a href="sdk-for-android-navigate-segmentspandata#getPositiveDirectionBaseSpeedInMetersPerSecond()"><code>SegmentSpanData.getPositiveDirectionBaseSpeedInMetersPerSecond()</code></a>,
 <a href="sdk-for-android-navigate-segmentspandata#getNegativeDirectionBaseSpeedInMetersPerSecond()"><code>SegmentSpanData.getNegativeDirectionBaseSpeedInMetersPerSecond()</code></a> and <a href="sdk-for-android-navigate-segmentspandata#getBaseSpeedInMetersPerSecond()"><code>SegmentSpanData.getBaseSpeedInMetersPerSecond()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> or
 <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.</div>
</div>
<div className="col-first even-row-color"><code>boolean</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloaderoptions#loadFunctionalRoadClass">loadFunctionalRoadClass</a></code></div>
<div className="col-last even-row-color">
<div className="block">If it is true, the <a href="sdk-for-android-navigate-segmentspandata#getFunctionalRoadClass()"><code>SegmentSpanData.getFunctionalRoadClass()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> or
 <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.</div>
</div>
<div className="col-first odd-row-color"><code>boolean</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloaderoptions#loadLocalRoadCharacteristics">loadLocalRoadCharacteristics</a></code></div>
<div className="col-last odd-row-color">
<div className="block">If it is true, <a href="sdk-for-android-navigate-segmentspandata#getLocalRoadCharacteristics()"><code>SegmentSpanData.getLocalRoadCharacteristics()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> or
 <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.</div>
</div>
<div className="col-first even-row-color"><code>boolean</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloaderoptions#loadRailwayCrossings">loadRailwayCrossings</a></code></div>
<div className="col-last even-row-color">
<div className="block">If it is true, <a href="sdk-for-android-navigate-segmentdata#getRailwayCrossings()"><code>SegmentData.getRailwayCrossings()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> or <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.</div>
</div>
<div className="col-first odd-row-color"><code>boolean</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloaderoptions#loadRoadAttributes">loadRoadAttributes</a></code></div>
<div className="col-last odd-row-color">
<div className="block">If it is true, <a href="sdk-for-android-navigate-segmentspandata#getPhysicalAttributes()"><code>SegmentSpanData.getPhysicalAttributes()</code></a> and
 <a href="sdk-for-android-navigate-segmentspandata#getRoadUsages()"><code>SegmentSpanData.getRoadUsages()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> or
 <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.</div>
</div>
<div className="col-first even-row-color"><code>boolean</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloaderoptions#loadRoadSigns">loadRoadSigns</a></code></div>
<div className="col-last even-row-color">
<div className="block">If it is true, <a href="sdk-for-android-navigate-segmentdata#getRoadSigns()"><code>SegmentData.getRoadSigns()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> or <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.</div>
</div>
<div className="col-first odd-row-color"><code>boolean</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloaderoptions#loadSpecialSpeedSituations">loadSpecialSpeedSituations</a></code></div>
<div className="col-last odd-row-color">
<div className="block">If it is true, <a href="sdk-for-android-navigate-segmentspandata#getSpecialSpeedSituations()"><code>SegmentSpanData.getSpecialSpeedSituations()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.</div>
</div>
<div className="col-first even-row-color"><code>boolean</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloaderoptions#loadSpeedLimits">loadSpeedLimits</a></code></div>
<div className="col-last even-row-color">
<div className="block">If it is true, <a href="sdk-for-android-navigate-segmentspandata#getPositiveDirectionSpeedLimit()"><code>SegmentSpanData.getPositiveDirectionSpeedLimit()</code></a>,
 <a href="sdk-for-android-navigate-segmentspandata#getNegativeDirectionSpeedLimit()"><code>SegmentSpanData.getNegativeDirectionSpeedLimit()</code></a> and <a href="sdk-for-android-navigate-segmentspandata#getSpeedLimit()"><code>SegmentSpanData.getSpeedLimit()</code></a> will be loaded
 when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> or <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.</div>
</div>
<div className="col-first odd-row-color"><code>boolean</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloaderoptions#loadStreetNamesAndRoadNumbers">loadStreetNamesAndRoadNumbers</a></code></div>
<div className="col-last odd-row-color">
<div className="block">If it is true, <a href="sdk-for-android-navigate-segmentspandata#getStreetNames()"><code>SegmentSpanData.getStreetNames()</code></a> and <a href="sdk-for-android-navigate-segmentspandata#getRoadNumbers()"><code>SegmentSpanData.getRoadNumbers()</code></a> and will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> or
 <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.</div>
</div>
<div className="col-first even-row-color"><code>boolean</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloaderoptions#loadTollPoints">loadTollPoints</a></code></div>
<div className="col-last even-row-color">
<div className="block">If it is true, <a href="sdk-for-android-navigate-segmentdata#getTollPoints()"><code>SegmentData.getTollPoints()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.</div>
</div>
<div className="col-first odd-row-color"><code>boolean</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloaderoptions#loadTrafficSignals">loadTrafficSignals</a></code></div>
<div className="col-last odd-row-color">
<div className="block">If it is true, <a href="sdk-for-android-navigate-segmentdata#getTrafficSignals()"><code>SegmentData.getTrafficSignals()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> or <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.</div>
</div>
<div className="col-first even-row-color"><code>boolean</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloaderoptions#loadTransportModesAccess">loadTransportModesAccess</a></code></div>
<div className="col-last even-row-color">
<div className="block">If it is true, <a href="sdk-for-android-navigate-segmentspandata#getAllowedTransportModes()"><code>SegmentSpanData.getAllowedTransportModes()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> or
 <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.</div>
</div>
<div className="col-first odd-row-color"><code>boolean</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloaderoptions#loadTravelDirection">loadTravelDirection</a></code></div>
<div className="col-last odd-row-color">
<div className="block">If it is true, the <a href="sdk-for-android-navigate-segmentspandata#getTravelDirection()"><code>SegmentSpanData.getTravelDirection()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> or
 <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.</div>
</div>
<div className="col-first even-row-color"><code>boolean</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloaderoptions#loadUrban">loadUrban</a></code></div>
<div className="col-last even-row-color">
<div className="block">If it is true, <a href="sdk-for-android-navigate-segmentspandata#isUrban()"><code>SegmentSpanData.isUrban()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloaderoptions#%3Cinit%3E()">SegmentDataLoaderOptions</a>()</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section className="field-details" id="field-detail">

<ul className="member-list">
<li>
<section className="detail" id="loadTravelDirection">
<h3>loadTravelDirection</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">loadTravelDirection</span></div>
<div className="block"><p>If it is true, the <a href="sdk-for-android-navigate-segmentspandata#getTravelDirection()"><code>SegmentSpanData.getTravelDirection()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> or
 <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.</p></div>
</section>
</li>
<li>
<section className="detail" id="loadFunctionalRoadClass">
<h3>loadFunctionalRoadClass</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">loadFunctionalRoadClass</span></div>
<div className="block"><p>If it is true, the <a href="sdk-for-android-navigate-segmentspandata#getFunctionalRoadClass()"><code>SegmentSpanData.getFunctionalRoadClass()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> or
 <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.</p></div>
</section>
</li>
<li>
<section className="detail" id="loadTransportModesAccess">
<h3>loadTransportModesAccess</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">loadTransportModesAccess</span></div>
<div className="block"><p>If it is true, <a href="sdk-for-android-navigate-segmentspandata#getAllowedTransportModes()"><code>SegmentSpanData.getAllowedTransportModes()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> or
 <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.</p></div>
</section>
</li>
<li>
<section className="detail" id="loadSpeedLimits">
<h3>loadSpeedLimits</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">loadSpeedLimits</span></div>
<div className="block"><p>If it is true, <a href="sdk-for-android-navigate-segmentspandata#getPositiveDirectionSpeedLimit()"><code>SegmentSpanData.getPositiveDirectionSpeedLimit()</code></a>,
 <a href="sdk-for-android-navigate-segmentspandata#getNegativeDirectionSpeedLimit()"><code>SegmentSpanData.getNegativeDirectionSpeedLimit()</code></a> and <a href="sdk-for-android-navigate-segmentspandata#getSpeedLimit()"><code>SegmentSpanData.getSpeedLimit()</code></a> will be loaded
 when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> or <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.</p></div>
</section>
</li>
<li>
<section className="detail" id="loadBaseSpeeds">
<h3>loadBaseSpeeds</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">loadBaseSpeeds</span></div>
<div className="block"><p>If it is true, <a href="sdk-for-android-navigate-segmentspandata#getPositiveDirectionBaseSpeedInMetersPerSecond()"><code>SegmentSpanData.getPositiveDirectionBaseSpeedInMetersPerSecond()</code></a>,
 <a href="sdk-for-android-navigate-segmentspandata#getNegativeDirectionBaseSpeedInMetersPerSecond()"><code>SegmentSpanData.getNegativeDirectionBaseSpeedInMetersPerSecond()</code></a> and <a href="sdk-for-android-navigate-segmentspandata#getBaseSpeedInMetersPerSecond()"><code>SegmentSpanData.getBaseSpeedInMetersPerSecond()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> or
 <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.</p></div>
</section>
</li>
<li>
<section className="detail" id="loadLocalRoadCharacteristics">
<h3>loadLocalRoadCharacteristics</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">loadLocalRoadCharacteristics</span></div>
<div className="block"><p>If it is true, <a href="sdk-for-android-navigate-segmentspandata#getLocalRoadCharacteristics()"><code>SegmentSpanData.getLocalRoadCharacteristics()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> or
 <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.</p></div>
</section>
</li>
<li>
<section className="detail" id="loadStreetNamesAndRoadNumbers">
<h3>loadStreetNamesAndRoadNumbers</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">loadStreetNamesAndRoadNumbers</span></div>
<div className="block"><p>If it is true, <a href="sdk-for-android-navigate-segmentspandata#getStreetNames()"><code>SegmentSpanData.getStreetNames()</code></a> and <a href="sdk-for-android-navigate-segmentspandata#getRoadNumbers()"><code>SegmentSpanData.getRoadNumbers()</code></a> and will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> or
 <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.</p></div>
</section>
</li>
<li>
<section className="detail" id="loadRoadAttributes">
<h3>loadRoadAttributes</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">loadRoadAttributes</span></div>
<div className="block"><p>If it is true, <a href="sdk-for-android-navigate-segmentspandata#getPhysicalAttributes()"><code>SegmentSpanData.getPhysicalAttributes()</code></a> and
 <a href="sdk-for-android-navigate-segmentspandata#getRoadUsages()"><code>SegmentSpanData.getRoadUsages()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> or
 <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.</p></div>
</section>
</li>
<li>
<section className="detail" id="loadTrafficSignals">
<h3>loadTrafficSignals</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">loadTrafficSignals</span></div>
<div className="block"><p>If it is true, <a href="sdk-for-android-navigate-segmentdata#getTrafficSignals()"><code>SegmentData.getTrafficSignals()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> or <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.
 Defaults to <code>false</code>.</p></div>
</section>
</li>
<li>
<section className="detail" id="loadRoadSigns">
<h3>loadRoadSigns</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">loadRoadSigns</span></div>
<div className="block"><p>If it is true, <a href="sdk-for-android-navigate-segmentdata#getRoadSigns()"><code>SegmentData.getRoadSigns()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> or <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.
 Defaults to <code>false</code>.</p></div>
</section>
</li>
<li>
<section className="detail" id="loadAdministrativeRules">
<h3>loadAdministrativeRules</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">loadAdministrativeRules</span></div>
<div className="block"><p>If it is true, <a href="sdk-for-android-navigate-segmentspandata#getAdministrativeRules()"><code>SegmentSpanData.getAdministrativeRules()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> or <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.
 Defaults to <code>false</code>.</p></div>
</section>
</li>
<li>
<section className="detail" id="loadRailwayCrossings">
<h3>loadRailwayCrossings</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">loadRailwayCrossings</span></div>
<div className="block"><p>If it is true, <a href="sdk-for-android-navigate-segmentdata#getRailwayCrossings()"><code>SegmentData.getRailwayCrossings()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> or <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.
 Defaults to <code>false</code>.</p></div>
</section>
</li>
<li>
<section className="detail" id="loadUrban">
<h3>loadUrban</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">loadUrban</span></div>
<div className="block"><p>If it is true, <a href="sdk-for-android-navigate-segmentspandata#isUrban()"><code>SegmentSpanData.isUrban()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.
 Defaults to <code>false</code>.</p></div>
</section>
</li>
<li>
<section className="detail" id="loadSpecialSpeedSituations">
<h3>loadSpecialSpeedSituations</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">loadSpecialSpeedSituations</span></div>
<div className="block"><p>If it is true, <a href="sdk-for-android-navigate-segmentspandata#getSpecialSpeedSituations()"><code>SegmentSpanData.getSpecialSpeedSituations()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.
 <strong>Note:</strong> To get timezone offset and daylight saving time values for TimeRule, [sdk.mapdata.SegmentDataLoaderOptions.load_administrative_rules] must also be set to <code>true</code>.
 Defaults to <code>false</code>.</p></div>
</section>
</li>
<li>
<section className="detail" id="loadTollPoints">
<h3>loadTollPoints</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">loadTollPoints</span></div>
<div className="block"><p>If it is true, <a href="sdk-for-android-navigate-segmentdata#getTollPoints()"><code>SegmentData.getTollPoints()</code></a> will be loaded when <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a> is called.
 Defaults to <code>false</code>.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;()">
<h3>SegmentDataLoaderOptions</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">SegmentDataLoaderOptions</span>()</div>
<div className="block"><p>Creates a new instance.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">equals</span><wbr/><span className="parameters">(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl className="notes">
<dt>Overrides:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="hashCode()">
<h3>hashCode</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">hashCode</span>()</div>
<dl className="notes">
<dt>Overrides:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
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
