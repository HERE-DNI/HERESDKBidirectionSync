---
title: "RoutePrefetcher (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-prefetcher-routeprefetcher"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-prefetcher-package-summary">com.here.sdk.prefetcher</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.prefetcher.RoutePrefetcher → com.here.NativeBase com.here.sdk.prefetcher.RoutePrefetcher → com.here.sdk.prefetcher.RoutePrefetcher

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">RoutePrefetcher</span> <span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span>

</div>

<div class="block">

Supports downloading of map data - in advance - into the cache to optimize temporary offline use cases that rely on cached map data. This allows scenarios such as navigation to work in a specific area reliably even though the network might be offline at that time. Please note, this class puts data in the map cache, which has its own size constraints, and extensive usage may start evicting old cached data. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

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

      RoutePrefetcher ( SDKNativeEngine sdkEngine)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a RoutePrefetcher instance for a given SDKNativeEngine .

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

  `int`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getPrefetchCorridorLengthMeters ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the length of the corridor along the route in front of the car which will be used to prefetch data.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

      prefetchAroundLocationWithRadius ( GeoCoordinates currentLocation, Double radiusInMeters)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.27.0.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      prefetchAroundRouteOnIntervals ( NavigatorInterface navigator)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Prefetches map data within a corridor along the route, that is currently set for the provided NavigatorInterface instance.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">`TaskHandle`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      prefetchGeoCorridor ( GeoCorridor corridor, PrefetchStatusListener callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Prefetch tiles for a given geo-corridor.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setPrefetchCorridorLengthMeters (int value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the length of the corridor along the route in front of the car which will be used to prefetch data.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      stopPrefetchAroundRoute ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Stops listening NavigatorInterface passed to prefetchAroundRouteOnIntervals(com.here.sdk.navigation.NavigatorInterface) for route progress events and stops prefetching data along the current route.

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

    ### RoutePrefetcher

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RoutePrefetcher</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</span>

    </div>

    <div class="block">

    Creates a RoutePrefetcher instance for a given SDKNativeEngine .

    </div>

    Parameters:  
    `sdkEngine` -

    Instance of an existing SDKEngine.

    </div>

  </div>

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-prefetchAroundLocationWithRadius-com-here-sdk-core-GeoCoordinates-java-lang-Double" class="section detail">

    ### prefetchAroundLocationWithRadius

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> </span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">prefetchAroundLocationWithRadius</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> currentLocation, @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a> radiusInMeters)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.27.0. Please use [](sdk-for-android-navigate-com-here-sdk-prefetcher-polygonprefetcher#prefetch(com.here.sdk.core.GeoPolygon,com.here.sdk.prefetcher.PrefetchStatusListener))

        PolygonPrefetcher.prefetch(com.here.sdk.core.GeoPolygon, com.here.sdk.prefetcher.PrefetchStatusListener)

    </a> instead.
    </p>

    </div>

    </div>

    <div class="block">

    Prefetches map data within a user-defined circular area around a given location. The radius, specified in meters, must be between 1 km and 50 km. If null is passed as the radius, a default value of 2 km is used. It is recommended to call this method once before starting navigation to ensure a smooth experience. To control list of map content features for area prefetch, use LayerConfiguration.enabledFeatures .

    </div>

    Parameters:  
    `currentLocation` -

    The center of the circle to prefetch data within.

    `radiusInMeters` -

    The radius of the circle to prefetch data within.

    </div>

  - <div id="sdk-for-android-navigate-prefetchAroundRouteOnIntervals-com-here-sdk-navigation-NavigatorInterface" class="section detail">

    ### prefetchAroundRouteOnIntervals

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">prefetchAroundRouteOnIntervals</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">NavigatorInterface</a> navigator)</span>

    </div>

    <div class="block">

    Prefetches map data within a corridor along the route, that is currently set for the provided NavigatorInterface instance. If no route is set, no data will be prefetched. The route corridor defaults to a length of 10 km and a width of 5 km. To prefetch the whole route before navigation has been started see prefetchGeoCorridor(com.here.sdk.core.GeoCorridor, com.here.sdk.prefetcher.PrefetchStatusListener) . Map data is prefetched only in discrete intervals. Prefetching starts 1 km before reaching the end of the current corridor. Prefetching happens based on the current map-matched location - as indicated by the RouteProgress event. This method should be called right after navigation has started. In case of default prefetch length first prefetching will start after traveling a distance of 9 km along the route. To control list of map content features for prefetch, use LayerConfiguration.enabledFeatures .

    </div>

    Parameters:  
    `navigator` -

    The <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigatorinterface" title="interface in com.here.sdk.navigation">`NavigatorInterface`</a> to listen for Route Progress to prefetch data ahead.

    </div>

  - <div id="sdk-for-android-navigate-stopPrefetchAroundRoute" class="section detail">

    ### stopPrefetchAroundRoute

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">stopPrefetchAroundRoute</span>()

    </div>

    <div class="block">

    Stops listening NavigatorInterface passed to prefetchAroundRouteOnIntervals(com.here.sdk.navigation.NavigatorInterface) for route progress events and stops prefetching data along the current route.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-prefetchGeoCorridor-com-here-sdk-core-GeoCorridor-com-here-sdk-prefetcher-PrefetchStatusListener" class="section detail">

    ### prefetchGeoCorridor

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">prefetchGeoCorridor</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-geocorridor" title="class in com.here.sdk.core">GeoCorridor</a> corridor, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-prefetcher-prefetchstatuslistener" title="interface in com.here.sdk.prefetcher">PrefetchStatusListener</a> callback)</span>

    </div>

    <div class="block">

    Prefetch tiles for a given geo-corridor. A geo-corridor can easily be created from a route with Route.getGeometry() so navigation on this route is possible in offline cases. Please note, tiles will be saved in mutable cache so when there is not enough space to accommodate new prefetched tiles MapLoaderError.NOT_ENOUGH_SPACE is returned. When updating mutable cache, all tiles will be unusable. Please re-download the geoCorridor again. Please also note, any route calculation may not possible on prefetched tiles. To control list of map content features for corridor prefetch, use LayerConfiguration.enabledFeatures .

    </div>

    Parameters:  
    `corridor` -

    indicates `GeoCorridor` that can be constructed from the route.

    `callback` -

    is invoked to report progress and the result of prefetch. After operation is finished, [](sdk-for-android-navigate-com-here-sdk-prefetcher-prefetchstatuslistener#onComplete(com.here.sdk.maploader.MapLoaderError))

        PrefetchStatusListener.onComplete(com.here.sdk.maploader.MapLoaderError)

    </a> is invoked on the main thread. Progress is reported by invocation of [](sdk-for-android-navigate-com-here-sdk-prefetcher-prefetchstatuslistener#onProgress(int))

        PrefetchStatusListener.onProgress(int)

    </a> on the main thread.

    </p>

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-navigate-getPrefetchCorridorLengthMeters" class="section detail">

    ### getPrefetchCorridorLengthMeters

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getPrefetchCorridorLengthMeters</span>()

    </div>

    <div class="block">

    Gets the length of the corridor along the route in front of the car which will be used to prefetch data. Upper limit for length is 50000 meters, when the requested length is greater than upper limit, then 50000 meters set. Lower limit for length is 1000 meters, when the requested length is less than lower limit, then 1000 meters set. The route corridor has a default length of 10 km and a width of 5 km.

    </div>

    Returns:  
    The length of the corridor along the route in front of the car which will be used to prefetch data.

    </div>

  - <div id="sdk-for-android-navigate-setPrefetchCorridorLengthMeters-int" class="section detail">

    ### setPrefetchCorridorLengthMeters

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPrefetchCorridorLengthMeters</span><wbr></wbr><span class="parameters">(int value)</span>

    </div>

    <div class="block">

    Sets the length of the corridor along the route in front of the car which will be used to prefetch data. Upper limit for length is 50000 meters, when the requested length is greater than upper limit, then 50000 meters set. Lower limit for length is 1000 meters, when the requested length is less than lower limit, then 1000 meters set. The route corridor has a default length of 10 km and a width of 5 km.

    </div>

    Parameters:  
    `value` -

    The length of the corridor along the route in front of the car which will be used to prefetch data.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

