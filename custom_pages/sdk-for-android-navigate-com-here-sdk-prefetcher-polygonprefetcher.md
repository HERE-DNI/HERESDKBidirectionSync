---
title: "PolygonPrefetcher (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-prefetcher-polygonprefetcher"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-prefetcher-package-summary">com.here.sdk.prefetcher</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.prefetcher.PolygonPrefetcher → com.here.NativeBase com.here.sdk.prefetcher.PolygonPrefetcher → com.here.sdk.prefetcher.PolygonPrefetcher

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">PolygonPrefetcher</span> <span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span>

</div>

<div class="block">

Supports downloading of map data - in advance - into the cache to optimize temporary offline use cases that rely on cached map data. Please note, this class puts data in the map cache, which has its own size constraints, and extensive usage may start evicting old cached data. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

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

      PolygonPrefetcher ( SDKNativeEngine sdkEngine)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a PolygonPrefetcher instance for a given SDKNativeEngine .

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

  <a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">`TaskHandle`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      estimateMapDataSize ( GeoPolygon geoPolygon, MapDataSizeListener callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Estimates map data size for the area bounded by geo polygon.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">`TaskHandle`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      prefetch ( GeoPolygon geoPolygon, PrefetchStatusListener callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Prefetches map data for an area bounded by geo polygon.

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

  - <div id="sdk-for-android-navigate-init-com-here-sdk-core-engine-SDKNativeEngine" class="section detail">

    ### PolygonPrefetcher

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">PolygonPrefetcher</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</span>

    </div>

    <div class="block">

    Creates a PolygonPrefetcher instance for a given SDKNativeEngine .

    </div>

    Parameters:  
    `sdkEngine` -

    Instance of an existing SDKEngine.

    </div>

  </div>

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-prefetch-com-here-sdk-core-GeoPolygon-com-here-sdk-prefetcher-PrefetchStatusListener" class="section detail">

    ### prefetch

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">prefetch</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-geopolygon" title="class in com.here.sdk.core">GeoPolygon</a> geoPolygon, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-prefetcher-prefetchstatuslistener" title="interface in com.here.sdk.prefetcher">PrefetchStatusListener</a> callback)</span>

    </div>

    <div class="block">

    Prefetches map data for an area bounded by geo polygon. After the operation is finished PrefetchStatusListener.onComplete(com.here.sdk.maploader.MapLoaderError) is invoked on the main thread. Progress is reported by invocation of PrefetchStatusListener.onProgress(int) on the main thread. If there is not enough space left in the cache to store needed tiles, operation will fail with MapLoaderError.NOT_ENOUGH_SPACE . To increase cache size, use SDKOptions.cacheSizeInBytes API. To control list of map content features for area prefetch, use LayerConfiguration.enabledFeatures . To prefetch map data within user-defined circular area around a given location: Create a GeoCircle using the given location and radius. Create a GeoPolygon using the GeoCircle. Pass the afroementioned GeoPolygon to the sdk.prefetcher.PolygonPrefetcher.prefetch API. Usage: GeoCircle geoCircle = GeoCircle(location, radius); GeoPolygon geoPolygon = GeoPolygon.withGeoCircle(geoCircle);

    </div>

    Parameters:  
    `geoPolygon` -

    Area to prefetch map data for.

    `callback` -

    Callback that is triggered to report progress and the result of prefetch.

    Returns:  
    Handle that will be used to manipulate execution of the task.

    </div>

  - <div id="sdk-for-android-navigate-estimateMapDataSize-com-here-sdk-core-GeoPolygon-com-here-sdk-prefetcher-MapDataSizeListener" class="section detail">

    ### estimateMapDataSize

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">estimateMapDataSize</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-geopolygon" title="class in com.here.sdk.core">GeoPolygon</a> geoPolygon, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-prefetcher-mapdatasizelistener" title="interface in com.here.sdk.prefetcher">MapDataSizeListener</a> callback)</span>

    </div>

    <div class="block">

    Estimates map data size for the area bounded by geo polygon. Size for tiles that are already in the cache will not be included in the final result.

    </div>

    Parameters:  
    `geoPolygon` -

    Area to estimate map data size for.

    `callback` -

    Callback that is triggered to report the result of map data size estimation.

    Returns:  
    Handle that will be used to manipulate execution of the task.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

