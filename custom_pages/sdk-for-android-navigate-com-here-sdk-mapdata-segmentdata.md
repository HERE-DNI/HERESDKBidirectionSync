---
title: "SegmentData (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapdata-segmentdata"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-mapdata-package-summary">com.here.sdk.mapdata</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.mapdata.SegmentData → com.here.NativeBase com.here.sdk.mapdata.SegmentData → com.here.sdk.mapdata.SegmentData

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">SegmentData</span> <span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span>

</div>

<div class="block">

Contains the requested information for a segment Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

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

  `int`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getLengthInMeters ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the length of this segment in meters.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-ocmsegmentid" title="class in com.here.sdk.mapdata">`OCMSegmentId`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getOcmSegmentId ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the OCMSegmentId object representing the the segment.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-core-geopolyline" title="class in com.here.sdk.core">`GeoPolyline`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getPolyline ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the GeoPolyline object representing the polyline of this segment.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-mapdata-railwaycrossing" title="class in com.here.sdk.mapdata">`RailwayCrossing`</a>`>`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getRailwayCrossings ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the list of RailwayCrossing .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsign" title="class in com.here.sdk.navigation">`RoadSign`</a>`>`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getRoadSigns ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the list of RoadSign .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-routing-segmentreference" title="class in com.here.sdk.routing">`SegmentReference`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getSegmentReference ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the SegmentReference object representing the the segment.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspandata" title="class in com.here.sdk.mapdata">`SegmentSpanData`</a>`>`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getSpans ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the list of SegmentSpanData .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-mapdata-tollpoint" title="class in com.here.sdk.mapdata">`TollPoint`</a>`>`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getTollPoints ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the list of TollPoint .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-mapdata-trafficsignal" title="class in com.here.sdk.mapdata">`TrafficSignal`</a>`>`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getTrafficSignals ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the list of TrafficSignal .

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-getOcmSegmentId" class="section detail">

    ### getOcmSegmentId

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-ocmsegmentid" title="class in com.here.sdk.mapdata">OCMSegmentId</a></span> <span class="element-name">getOcmSegmentId</span>()

    </div>

    <div class="block">

    Gets the OCMSegmentId object representing the the segment.

    </div>

    Returns:  
    The <a href="sdk-for-android-navigate-com-here-sdk-mapdata-ocmsegmentid" title="class in com.here.sdk.mapdata">`OCMSegmentId`</a> object representing the segment

    </div>

  - <div id="sdk-for-android-navigate-getSegmentReference" class="section detail">

    ### getSegmentReference

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-segmentreference" title="class in com.here.sdk.routing">SegmentReference</a></span> <span class="element-name">getSegmentReference</span>()

    </div>

    <div class="block">

    Gets the SegmentReference object representing the the segment.

    </div>

    Returns:  
    The <a href="sdk-for-android-navigate-com-here-sdk-routing-segmentreference" title="class in com.here.sdk.routing">`SegmentReference`</a> object representing the segment

    </div>

  - <div id="sdk-for-android-navigate-getPolyline" class="section detail">

    ### getPolyline

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geopolyline" title="class in com.here.sdk.core">GeoPolyline</a></span> <span class="element-name">getPolyline</span>()

    </div>

    <div class="block">

    Gets the GeoPolyline object representing the polyline of this segment.

    </div>

    Returns:  
    The <a href="sdk-for-android-navigate-com-here-sdk-core-geopolyline" title="class in com.here.sdk.core">`GeoPolyline`</a> object representing the polyline of this segment.

    </div>

  - <div id="sdk-for-android-navigate-getLengthInMeters" class="section detail">

    ### getLengthInMeters

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getLengthInMeters</span>()

    </div>

    <div class="block">

    Gets the length of this segment in meters.

    </div>

    Returns:  
    The length of this segment in meters. This information is based on map data. It can differ from the length of [](sdk-for-android-navigate-com-here-sdk-mapdata-segmentdata#getPolyline())

        getPolyline()

    </a> due to approximations of the polyline.

    </p>

    </div>

  - <div id="sdk-for-android-navigate-getSpans" class="section detail">

    ### getSpans

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspandata" title="class in com.here.sdk.mapdata">SegmentSpanData</a>\></span> <span class="element-name">getSpans</span>()

    </div>

    <div class="block">

    Gets the list of SegmentSpanData .

    </div>

    Returns:  
    The list of <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspandata" title="class in com.here.sdk.mapdata">`SegmentSpanData`</a> of the given segment for the requested attributes **Note:** If no span attributes is requested, the list will be empty.

    </div>

  - <div id="sdk-for-android-navigate-getTrafficSignals" class="section detail">

    ### getTrafficSignals

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-mapdata-trafficsignal" title="class in com.here.sdk.mapdata">TrafficSignal</a>\></span> <span class="element-name">getTrafficSignals</span>()

    </div>

    <div class="block">

    Gets the list of TrafficSignal .

    </div>

    Returns:  
    The list of <a href="sdk-for-android-navigate-com-here-sdk-mapdata-trafficsignal" title="class in com.here.sdk.mapdata">`TrafficSignal`</a> of the given segment. Returns an empty list if no data is found. Returns `null` if <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloaderoptions#loadTrafficSignals">`SegmentDataLoaderOptions.loadTrafficSignals`</a> is set to `false`. The <a href="sdk-for-android-navigate-com-here-sdk-mapdata-trafficsignallocation" title="enum class in com.here.sdk.mapdata">`TrafficSignalLocation`</a> indicates the location of a single traffic signal, which can be any combination of left, right and overhead. The <a href="sdk-for-android-navigate-com-here-sdk-mapdata-trafficsignal#offsetInMeters">`TrafficSignal.offsetInMeters`</a> is the location along the segment, while the traffic signal location have details on how the traffic signal is display/deploy in that specific location in the segment.

    </div>

  - <div id="sdk-for-android-navigate-getRoadSigns" class="section detail">

    ### getRoadSigns

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsign" title="class in com.here.sdk.navigation">RoadSign</a>\></span> <span class="element-name">getRoadSigns</span>()

    </div>

    <div class="block">

    Gets the list of RoadSign . Returns null if SegmentDataLoaderOptions.loadRoadSigns is set to false .

    </div>

    Returns:  
    The list of <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsign" title="class in com.here.sdk.navigation">`RoadSign`</a> of the given segment.

    </div>

  - <div id="sdk-for-android-navigate-getRailwayCrossings" class="section detail">

    ### getRailwayCrossings

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-mapdata-railwaycrossing" title="class in com.here.sdk.mapdata">RailwayCrossing</a>\></span> <span class="element-name">getRailwayCrossings</span>()

    </div>

    <div class="block">

    Gets the list of RailwayCrossing .

    </div>

    Returns:  
    The list of <a href="sdk-for-android-navigate-com-here-sdk-mapdata-railwaycrossing" title="class in com.here.sdk.mapdata">`RailwayCrossing`</a> of the given segment. Returns an empty list if no data is found. Returns `null` if <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloaderoptions#loadRailwayCrossings">`SegmentDataLoaderOptions.loadRailwayCrossings`</a> is set to `false`.

    </div>

  - <div id="sdk-for-android-navigate-getTollPoints" class="section detail">

    ### getTollPoints

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-mapdata-tollpoint" title="class in com.here.sdk.mapdata">TollPoint</a>\></span> <span class="element-name">getTollPoints</span>()

    </div>

    <div class="block">

    Gets the list of TollPoint .

    </div>

    Returns:  
    The list of <a href="sdk-for-android-navigate-com-here-sdk-mapdata-tollpoint" title="class in com.here.sdk.mapdata">`TollPoint`</a> of the given segment. Returns an empty list if no data is found. Returns `null` if <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloaderoptions#loadTollPoints">`SegmentDataLoaderOptions.loadTollPoints`</a> is set to `false` or the <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdata" title="class in com.here.sdk.mapdata">`SegmentData`</a> is not initialized using [](sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions))

        SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)

    </a>.

    </p>

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

