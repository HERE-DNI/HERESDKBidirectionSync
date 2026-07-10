---
title: "SegmentDataLoaderOptions (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloaderoptions"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-mapdata-package-summary">com.here.sdk.mapdata</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.mapdata.SegmentDataLoaderOptions → com.here.sdk.mapdata.SegmentDataLoaderOptions

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">SegmentDataLoaderOptions</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Specifies which data should be loaded by the SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) or SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) function. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

</div>

- <div id="sdk-for-android-navigate-field-summary" class="section field-summary">

  <div class="caption">

  Fields

  </div>

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Field

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  `boolean`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloaderoptions#loadAdministrativeRules" class="member-name-link"><code>loadAdministrativeRules</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  If it is true, SegmentSpanData.getAdministrativeRules() will be loaded when SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) or SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) is called.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `boolean`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloaderoptions#loadBaseSpeeds" class="member-name-link"><code>loadBaseSpeeds</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  If it is true, SegmentSpanData.getPositiveDirectionBaseSpeedInMetersPerSecond() , SegmentSpanData.getNegativeDirectionBaseSpeedInMetersPerSecond() and SegmentSpanData.getBaseSpeedInMetersPerSecond() will be loaded when SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) or SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) is called.

  </div>

  </div>

  <div class="col-first even-row-color">

  `boolean`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloaderoptions#loadFunctionalRoadClass" class="member-name-link"><code>loadFunctionalRoadClass</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  If it is true, the SegmentSpanData.getFunctionalRoadClass() will be loaded when SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) or SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) is called.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `boolean`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloaderoptions#loadLocalRoadCharacteristics" class="member-name-link"><code>loadLocalRoadCharacteristics</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  If it is true, SegmentSpanData.getLocalRoadCharacteristics() will be loaded when SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) or SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) is called.

  </div>

  </div>

  <div class="col-first even-row-color">

  `boolean`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloaderoptions#loadRailwayCrossings" class="member-name-link"><code>loadRailwayCrossings</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  If it is true, SegmentData.getRailwayCrossings() will be loaded when SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) or SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) is called.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `boolean`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloaderoptions#loadRoadAttributes" class="member-name-link"><code>loadRoadAttributes</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  If it is true, SegmentSpanData.getPhysicalAttributes() and SegmentSpanData.getRoadUsages() will be loaded when SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) or SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) is called.

  </div>

  </div>

  <div class="col-first even-row-color">

  `boolean`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloaderoptions#loadRoadSigns" class="member-name-link"><code>loadRoadSigns</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  If it is true, SegmentData.getRoadSigns() will be loaded when SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) or SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) is called.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `boolean`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloaderoptions#loadSpecialSpeedSituations" class="member-name-link"><code>loadSpecialSpeedSituations</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  If it is true, SegmentSpanData.getSpecialSpeedSituations() will be loaded when SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) is called.

  </div>

  </div>

  <div class="col-first even-row-color">

  `boolean`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloaderoptions#loadSpeedLimits" class="member-name-link"><code>loadSpeedLimits</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  If it is true, SegmentSpanData.getPositiveDirectionSpeedLimit() , SegmentSpanData.getNegativeDirectionSpeedLimit() and SegmentSpanData.getSpeedLimit() will be loaded when SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) or SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) is called.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `boolean`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloaderoptions#loadStreetNamesAndRoadNumbers" class="member-name-link"><code>loadStreetNamesAndRoadNumbers</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  If it is true, SegmentSpanData.getStreetNames() and SegmentSpanData.getRoadNumbers() and will be loaded when SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) or SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) is called.

  </div>

  </div>

  <div class="col-first even-row-color">

  `boolean`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloaderoptions#loadTollPoints" class="member-name-link"><code>loadTollPoints</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  If it is true, SegmentData.getTollPoints() will be loaded when SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) is called.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `boolean`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloaderoptions#loadTrafficSignals" class="member-name-link"><code>loadTrafficSignals</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  If it is true, SegmentData.getTrafficSignals() will be loaded when SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) or SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) is called.

  </div>

  </div>

  <div class="col-first even-row-color">

  `boolean`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloaderoptions#loadTransportModesAccess" class="member-name-link"><code>loadTransportModesAccess</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  If it is true, SegmentSpanData.getAllowedTransportModes() will be loaded when SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) or SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) is called.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `boolean`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloaderoptions#loadTravelDirection" class="member-name-link"><code>loadTravelDirection</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  If it is true, the SegmentSpanData.getTravelDirection() will be loaded when SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) or SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) is called.

  </div>

  </div>

  <div class="col-first even-row-color">

  `boolean`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloaderoptions#loadUrban" class="member-name-link"><code>loadUrban</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  If it is true, SegmentSpanData.isUrban() will be loaded when SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) is called.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-summary" class="section constructor-summary">

  <div class="caption">

  Constructors

  </div>

  <div class="summary-table two-column-summary">

  <div class="table-header col-first">

  Constructor

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-constructor-name even-row-color">

      SegmentDataLoaderOptions ()

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-navigate-method-summary" class="section method-summary">

  <div id="sdk-for-android-navigate-method-summary-table">

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Method

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      equals ( Object obj)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      hashCode ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-field-detail" class="section field-details">

  - <div id="sdk-for-android-navigate-loadTravelDirection" class="section detail">

    ### loadTravelDirection

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">loadTravelDirection</span>

    </div>

    <div class="block">

    If it is true, the SegmentSpanData.getTravelDirection() will be loaded when SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) or SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) is called.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-loadFunctionalRoadClass" class="section detail">

    ### loadFunctionalRoadClass

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">loadFunctionalRoadClass</span>

    </div>

    <div class="block">

    If it is true, the SegmentSpanData.getFunctionalRoadClass() will be loaded when SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) or SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) is called.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-loadTransportModesAccess" class="section detail">

    ### loadTransportModesAccess

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">loadTransportModesAccess</span>

    </div>

    <div class="block">

    If it is true, SegmentSpanData.getAllowedTransportModes() will be loaded when SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) or SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) is called.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-loadSpeedLimits" class="section detail">

    ### loadSpeedLimits

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">loadSpeedLimits</span>

    </div>

    <div class="block">

    If it is true, SegmentSpanData.getPositiveDirectionSpeedLimit() , SegmentSpanData.getNegativeDirectionSpeedLimit() and SegmentSpanData.getSpeedLimit() will be loaded when SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) or SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) is called.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-loadBaseSpeeds" class="section detail">

    ### loadBaseSpeeds

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">loadBaseSpeeds</span>

    </div>

    <div class="block">

    If it is true, SegmentSpanData.getPositiveDirectionBaseSpeedInMetersPerSecond() , SegmentSpanData.getNegativeDirectionBaseSpeedInMetersPerSecond() and SegmentSpanData.getBaseSpeedInMetersPerSecond() will be loaded when SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) or SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) is called.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-loadLocalRoadCharacteristics" class="section detail">

    ### loadLocalRoadCharacteristics

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">loadLocalRoadCharacteristics</span>

    </div>

    <div class="block">

    If it is true, SegmentSpanData.getLocalRoadCharacteristics() will be loaded when SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) or SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) is called.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-loadStreetNamesAndRoadNumbers" class="section detail">

    ### loadStreetNamesAndRoadNumbers

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">loadStreetNamesAndRoadNumbers</span>

    </div>

    <div class="block">

    If it is true, SegmentSpanData.getStreetNames() and SegmentSpanData.getRoadNumbers() and will be loaded when SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) or SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) is called.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-loadRoadAttributes" class="section detail">

    ### loadRoadAttributes

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">loadRoadAttributes</span>

    </div>

    <div class="block">

    If it is true, SegmentSpanData.getPhysicalAttributes() and SegmentSpanData.getRoadUsages() will be loaded when SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) or SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) is called.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-loadTrafficSignals" class="section detail">

    ### loadTrafficSignals

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">loadTrafficSignals</span>

    </div>

    <div class="block">

    If it is true, SegmentData.getTrafficSignals() will be loaded when SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) or SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) is called. Defaults to false .

    </div>

    </div>

  - <div id="sdk-for-android-navigate-loadRoadSigns" class="section detail">

    ### loadRoadSigns

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">loadRoadSigns</span>

    </div>

    <div class="block">

    If it is true, SegmentData.getRoadSigns() will be loaded when SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) or SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) is called. Defaults to false .

    </div>

    </div>

  - <div id="sdk-for-android-navigate-loadAdministrativeRules" class="section detail">

    ### loadAdministrativeRules

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">loadAdministrativeRules</span>

    </div>

    <div class="block">

    If it is true, SegmentSpanData.getAdministrativeRules() will be loaded when SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) or SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) is called. Defaults to false .

    </div>

    </div>

  - <div id="sdk-for-android-navigate-loadRailwayCrossings" class="section detail">

    ### loadRailwayCrossings

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">loadRailwayCrossings</span>

    </div>

    <div class="block">

    If it is true, SegmentData.getRailwayCrossings() will be loaded when SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) or SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) is called. Defaults to false .

    </div>

    </div>

  - <div id="sdk-for-android-navigate-loadUrban" class="section detail">

    ### loadUrban

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">loadUrban</span>

    </div>

    <div class="block">

    If it is true, SegmentSpanData.isUrban() will be loaded when SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) is called. Defaults to false .

    </div>

    </div>

  - <div id="sdk-for-android-navigate-loadSpecialSpeedSituations" class="section detail">

    ### loadSpecialSpeedSituations

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">loadSpecialSpeedSituations</span>

    </div>

    <div class="block">

    If it is true, SegmentSpanData.getSpecialSpeedSituations() will be loaded when SegmentDataLoader.loadData(com.here.sdk.mapdata.OCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) is called. Note: To get timezone offset and daylight saving time values for TimeRule, \[sdk.mapdata.SegmentDataLoaderOptions.load_administrative_rules\] must also be set to true . Defaults to false .

    </div>

    </div>

  - <div id="sdk-for-android-navigate-loadTollPoints" class="section detail">

    ### loadTollPoints

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">loadTollPoints</span>

    </div>

    <div class="block">

    If it is true, SegmentData.getTollPoints() will be loaded when SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions) is called. Defaults to false .

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init" class="section detail">

    ### SegmentDataLoaderOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">SegmentDataLoaderOptions</span>()

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-equals-java-lang-Object" class="section detail">

    ### equals

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr></wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a> obj)</span>

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="sdk-for-android-navigate-hashCode" class="section detail">

    ### hashCode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

