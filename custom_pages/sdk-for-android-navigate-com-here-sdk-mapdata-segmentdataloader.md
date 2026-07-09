---
title: "SegmentDataLoader (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloader"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-mapdata-package-summary">com.here.sdk.mapdata</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.mapdata.SegmentDataLoader → com.here.NativeBase com.here.sdk.mapdata.SegmentDataLoader → com.here.sdk.mapdata.SegmentDataLoader

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">SegmentDataLoader</span> <span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span>

</div>

<div class="block">

Provides the interface for the access to the segments data available in the local OCM map. Please be aware that the methods within this class load map data synchronously. In the event of absent data in the disk cache, the data will be retrieved from the remote server. To mitigate the potential freezing of the calling thread, it is advisable to proactively prefetch map data around the working area. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

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

      SegmentDataLoader ()

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance of this class.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      SegmentDataLoader ( SDKNativeEngine sdkEngine)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new instance of this class.

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

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<byte[]>`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      downloadFile ( List < FileReference > fileReferences, DownloadingFileOptions downloadingOptions)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Synchronously load the optional image providing guidance of a directed or non directed segment.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-mapdata-ocmsegmentid" title="class in com.here.sdk.mapdata">`OCMSegmentId`</a>`>`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getSegmentsAroundCoordinates ( GeoCoordinates coordinates,
       double radiusInMeters)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Loads the segments around a certain coordinates.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdata" title="class in com.here.sdk.mapdata">`SegmentData`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      loadData ( OCMSegmentId segment, SegmentDataLoaderOptions options)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Synchronously load the data for the given map segment.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdata" title="class in com.here.sdk.mapdata">`SegmentData`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      loadDirectedSegmentData ( DirectedOCMSegmentId segment, SegmentDataLoaderOptions options)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Synchronously load the data for the given map directed segment.

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

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init" class="section detail">

    ### SegmentDataLoader

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">SegmentDataLoader</span>() throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span>

    </div>

    <div class="block">

    Creates a new instance of this class.

    </div>

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">`InstantiationErrorException`</a> -

    Indicates what went wrong when the instantiation was attempted.

    </div>

  - <div id="sdk-for-android-navigate-init-com-here-sdk-core-engine-SDKNativeEngine" class="section detail">

    ### SegmentDataLoader

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">SegmentDataLoader</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</span> throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span>

    </div>

    <div class="block">

    Creates a new instance of this class.

    </div>

    Parameters:  
    `sdkEngine` -

    A SDKEngine instance.

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">`InstantiationErrorException`</a> -

    Indicates what went wrong when the instantiation was attempted.

    </div>

  </div>

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-getSegmentsAroundCoordinates-com-here-sdk-core-GeoCoordinates-double" class="section detail">

    ### getSegmentsAroundCoordinates

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-mapdata-ocmsegmentid" title="class in com.here.sdk.mapdata">OCMSegmentId</a>\></span> <span class="element-name">getSegmentsAroundCoordinates</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates, double radiusInMeters)</span> throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-mapdataloaderexception" title="class in com.here.sdk.mapdata">MapDataLoaderException</a></span>

    </div>

    <div class="block">

    Loads the segments around a certain coordinates. Returns an empty list in case no segments could be found around the coordinates.

    </div>

    Parameters:  
    `coordinates` -

    The location to explore

    `radiusInMeters` -

    The radius of the search. Only values between 1m and 5000m are accepted.

    Returns:  
    The list of segments around the given position. The segments are sorted by distance from the point. Throws if it's not possible to return list of a list of segments.

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-mapdata-mapdataloaderexception" title="class in com.here.sdk.mapdata">`MapDataLoaderException`</a> -

    Specifies reason, why list of a list of segments is not returned.

    </div>

  - <div id="sdk-for-android-navigate-loadData-com-here-sdk-mapdata-OCMSegmentId-com-here-sdk-mapdata-SegmentDataLoaderOptions" class="section detail">

    ### loadData

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdata" title="class in com.here.sdk.mapdata">SegmentData</a></span> <span class="element-name">loadData</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapdata-ocmsegmentid" title="class in com.here.sdk.mapdata">OCMSegmentId</a> segment, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloaderoptions" title="class in com.here.sdk.mapdata">SegmentDataLoaderOptions</a> options)</span> throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-mapdataloaderexception" title="class in com.here.sdk.mapdata">MapDataLoaderException</a></span>

    </div>

    <div class="block">

    Synchronously load the data for the given map segment.

    </div>

    Parameters:  
    `segment` -

    The segment to load.

    `options` -

    Request options

    Returns:  
    Requested data of a segment.

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-mapdata-mapdataloaderexception" title="class in com.here.sdk.mapdata">`MapDataLoaderException`</a> -

    Specifies reason, why list of data of a segment is not returned.

    </div>

  - <div id="sdk-for-android-navigate-loadDirectedSegmentData-com-here-sdk-mapdata-DirectedOCMSegmentId-com-here-sdk-mapdata-SegmentDataLoaderOptions" class="section detail">

    ### loadDirectedSegmentData

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdata" title="class in com.here.sdk.mapdata">SegmentData</a></span> <span class="element-name">loadDirectedSegmentData</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapdata-directedocmsegmentid" title="class in com.here.sdk.mapdata">DirectedOCMSegmentId</a> segment, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloaderoptions" title="class in com.here.sdk.mapdata">SegmentDataLoaderOptions</a> options)</span> throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-mapdataloaderexception" title="class in com.here.sdk.mapdata">MapDataLoaderException</a></span>

    </div>

    <div class="block">

    Synchronously load the data for the given map directed segment.

    </div>

    Parameters:  
    `segment` -

    The directed segment to load.

    `options` -

    Request options

    Returns:  
    Requested data of a segment.

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-mapdata-mapdataloaderexception" title="class in com.here.sdk.mapdata">`MapDataLoaderException`</a> -

    Specifies reason, why list of data of a segment is not returned.

    </div>

  - <div id="sdk-for-android-navigate-downloadFile-java-util-List-com-here-sdk-mapdata-DownloadingFileOptions" class="section detail">

    ### downloadFile

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<byte\[\]\></span> <span class="element-name">downloadFile</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-mapdata-filereference" title="class in com.here.sdk.mapdata">FileReference</a>\> fileReferences, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapdata-downloadingfileoptions" title="class in com.here.sdk.mapdata">DownloadingFileOptions</a> downloadingOptions)</span> throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-mapdataloaderexception" title="class in com.here.sdk.mapdata">MapDataLoaderException</a></span>

    </div>

    <div class="block">

    Synchronously load the optional image providing guidance of a directed or non directed segment.

    </div>

    Parameters:  
    `fileReferences` -

    Provides information for a file reference.

    `downloadingOptions` -

    Provides information regarding downloading configuration.

    Returns:  
    Requested data of a segment.

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-mapdata-mapdataloaderexception" title="class in com.here.sdk.mapdata">`MapDataLoaderException`</a> -

    Specifies reason, why list of data of a segment is not returned.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

