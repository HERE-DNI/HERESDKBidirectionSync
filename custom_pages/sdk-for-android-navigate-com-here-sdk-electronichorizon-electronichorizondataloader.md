---
title: "ElectronicHorizonDataLoader (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizondataloader"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-package-summary">com.here.sdk.electronichorizon</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.electronichorizon.ElectronicHorizonDataLoader → com.here.NativeBase com.here.sdk.electronichorizon.ElectronicHorizonDataLoader → com.here.sdk.electronichorizon.ElectronicHorizonDataLoader

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">ElectronicHorizonDataLoader</span> <span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span>

</div>

<div class="block">

Loads map data for segments that belong to the ElectronicHorizonEngine paths. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process. Offline availability: This property is available online and offline.

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

      ElectronicHorizonDataLoader ( SDKNativeEngine sdkEngine, SegmentDataLoaderOptions options,
       int segmentDataCacheSize)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance of ElectronicHorizonDataLoader .

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

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      addElectronicHorizonDataLoaderStatusListener ( ElectronicHorizonDataLoaderStatusListener electronicHorizonListener)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Adds an ElectronicHorizonDataLoaderStatusListener to the subscription list.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizondataloaderresult" title="class in com.here.sdk.electronichorizon">`ElectronicHorizonDataLoaderResult`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getSegment ( DirectedOCMSegmentId segmentId)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Returns loaded data for the given segment identifier.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      loadData ( ElectronicHorizonUpdate electronicHorizonUpdate)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Requests data for all added segments and removes cached data for segments that are not part of the horizon anymore.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      removeElectronicHorizonDataLoaderStatusListener ( ElectronicHorizonDataLoaderStatusListener electronicHorizonListener)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Removes an ElectronicHorizonDataLoaderStatusListener from the subscription list.

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

  - <div id="sdk-for-android-navigate-init-com-here-sdk-core-engine-SDKNativeEngine-com-here-sdk-mapdata-SegmentDataLoaderOptions-int" class="section detail">

    ### ElectronicHorizonDataLoader

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">ElectronicHorizonDataLoader</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloaderoptions" title="class in com.here.sdk.mapdata">SegmentDataLoaderOptions</a> options, int segmentDataCacheSize)</span> throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span>

    </div>

    <div class="block">

    Creates a new instance of ElectronicHorizonDataLoader . The constructor accepts options to configure the data loader. For more information, see SegmentDataLoaderOptions . The cache size limits the number of segments that the loader can keep in memory at the same time.

    </div>

    Parameters:  
    `sdkEngine` -

    The <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">`SDKNativeEngine`</a> instance that provides shared services, such as networking and map data.

    `options` -

    The <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloaderoptions" title="class in com.here.sdk.mapdata">`SegmentDataLoaderOptions`</a> instance that configures how segment data is requested.

    `segmentDataCacheSize` -

    The maximum number of segments that the loader can cache.

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">`InstantiationErrorException`</a> -

    <a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">`InstantiationErrorException`</a> If the data loader cannot be created.

    </div>

  </div>

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-loadData-com-here-sdk-electronichorizon-ElectronicHorizonUpdate" class="section detail">

    ### loadData

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">loadData</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonupdate" title="class in com.here.sdk.electronichorizon">ElectronicHorizonUpdate</a> electronicHorizonUpdate)</span>

    </div>

    <div class="block">

    Requests data for all added segments and removes cached data for segments that are not part of the horizon anymore.

    </div>

    Parameters:  
    `electronicHorizonUpdate` -

    The update that contains the segments to add to the cache and the segments to remove from the cache.

    </div>

  - <div id="sdk-for-android-navigate-getSegment-com-here-sdk-mapdata-DirectedOCMSegmentId" class="section detail">

    ### getSegment

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizondataloaderresult" title="class in com.here.sdk.electronichorizon">ElectronicHorizonDataLoaderResult</a></span> <span class="element-name">getSegment</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapdata-directedocmsegmentid" title="class in com.here.sdk.mapdata">DirectedOCMSegmentId</a> segmentId)</span>

    </div>

    <div class="block">

    Returns loaded data for the given segment identifier. The result contains either the loaded data or an error code.

    </div>

    Parameters:  
    `segmentId` -

    The segment identifier for which to return the loaded data from the cache.

    Returns:  
    The result object that contains either the loaded segment data or an error code.

    </div>

  - <div id="sdk-for-android-navigate-addElectronicHorizonDataLoaderStatusListener-com-here-sdk-electronichorizon-ElectronicHorizonDataLoaderStatusListener" class="section detail">

    ### addElectronicHorizonDataLoaderStatusListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addElectronicHorizonDataLoaderStatusListener</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizondataloaderstatuslistener" title="interface in com.here.sdk.electronichorizon">ElectronicHorizonDataLoaderStatusListener</a> electronicHorizonListener)</span>

    </div>

    <div class="block">

    Adds an ElectronicHorizonDataLoaderStatusListener to the subscription list.

    </div>

    Parameters:  
    `electronicHorizonListener` -

    The listener that receives data loader status updates.

    </div>

  - <div id="sdk-for-android-navigate-removeElectronicHorizonDataLoaderStatusListener-com-here-sdk-electronichorizon-ElectronicHorizonDataLoaderStatusListener" class="section detail">

    ### removeElectronicHorizonDataLoaderStatusListener

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeElectronicHorizonDataLoaderStatusListener</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizondataloaderstatuslistener" title="interface in com.here.sdk.electronichorizon">ElectronicHorizonDataLoaderStatusListener</a> electronicHorizonListener)</span>

    </div>

    <div class="block">

    Removes an ElectronicHorizonDataLoaderStatusListener from the subscription list.

    </div>

    Parameters:  
    `electronicHorizonListener` -

    The listener that should no longer receive data loader status updates.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

