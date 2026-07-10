---
title: "OfflineRoutingEngine (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-routing-offlineroutingengine"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-routing-package-summary">com.here.sdk.routing</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.routing.OfflineRoutingEngine → com.here.NativeBase com.here.sdk.routing.OfflineRoutingEngine → com.here.sdk.routing.OfflineRoutingEngine

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

All Implemented Interfaces:  
<a href="sdk-for-android-navigate-com-here-sdk-routing-routinginterface" title="interface in com.here.sdk.routing">`RoutingInterface`</a>

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">OfflineRoutingEngine</span> <span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a> implements <a href="sdk-for-android-navigate-com-here-sdk-routing-routinginterface" title="interface in com.here.sdk.routing">RoutingInterface</a></span>

</div>

<div class="block">

Use this class to calculate a route offline from A to B with a number of waypoints in between. Route calculation is done asynchronously, and requires map data that is available offline. This can be temporarily cached map data or downloaded offline map data stored in the persisted storage via MapDownloader . Note that when using the cache there is a risk of missing data and this may reduce the overall quality of the route or can result in a RoutingError.NO_ROUTE_FOUND error. The resulting route contains various information such as the polyline, route length in meters, estimated time to traverse along the route and maneuver data, but it does not contain traffic information. Unlike the RoutingEngine (which requires an online connection), this engine allows to use an unlimited number of waypoints. As an alternative to this engine, consider to use the RoutingEngine for online route calculations to get fresher traffic, maneuver, route handles and street information, and to use a more elaborate algorithms to calculate the fastest route. For offline bus routing, enable "OFFLINE_BUS_ROUTING" as feature configuration. For more details, please look at SDKOptions . If this feature is not enabled, the engine may not be able to find bus routes. Note: EV routing is available when calculating a route using the RoutingOptions , by setting the RoutingOptions.evOptions . Note: Traffic related information is completely excluded. No historic traffic patterns are taking into consideration for the ETA. Currently blocked or closed roads or roads with traffic incident are not considered offline, i.e. the road may pass through such road. Only seasonal road closures are considered based on the departure time, if given. Traffic information is only considered for online route calculation with the RoutingEngine . Note: Route handles produced by this engine are not compatible with those created by the RoutingEngine . Importing, refreshing, or returning to a route via a route handle is supported only when the route was calculated with the same engine. However, this engine supports returning to a route calculated with the RoutingEngine when the route object is provided.

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

      OfflineRoutingEngine ()

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance of this class.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      OfflineRoutingEngine ( SDKNativeEngine sdkEngine)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new instance of OfflineRoutingEngine.

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      OfflineRoutingEngine ( SDKNativeEngine sdkEngine, OfflineRoutingEngineOptions options)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance of OfflineRoutingEngine.

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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">`TaskHandle`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

      calculateRoute ( List < Waypoint > waypoints, BicycleOptions bicycleOptions, CalculateRouteCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">`TaskHandle`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

      calculateRoute ( List < Waypoint > waypoints, BusOptions busOptions, CalculateRouteCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">`TaskHandle`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

      calculateRoute ( List < Waypoint > waypoints, CarOptions carOptions, CalculateRouteCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">`TaskHandle`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

      calculateRoute ( List < Waypoint > waypoints, EVCarOptions evCarOptions, CalculateRouteCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">`TaskHandle`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

      calculateRoute ( List < Waypoint > waypoints, EVTruckOptions evTruckOptions, CalculateRouteCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">`TaskHandle`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

      calculateRoute ( List < Waypoint > waypoints, PedestrianOptions pedestrianOptions, CalculateRouteCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">`TaskHandle`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

      calculateRoute ( List < Waypoint > waypoints, PrivateBusOptions privateBusOptions, CalculateRouteCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">`TaskHandle`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      calculateRoute ( List < Waypoint > waypoints, RoutingOptions options, CalculateRouteCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Asynchronously calculates a route from one point to another, passing through the given waypoints in the given order.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">`TaskHandle`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

      calculateRoute ( List < Waypoint > waypoints, ScooterOptions scooterOptions, CalculateRouteCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">`TaskHandle`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

      calculateRoute ( List < Waypoint > waypoints, TaxiOptions taxiOptions, CalculateRouteCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">`TaskHandle`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

      calculateRoute ( List < Waypoint > waypoints, TruckOptions truckOptions, CalculateRouteCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      dispose ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Cancels pending requests and closes the background worker thread.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficdataprovider" title="class in com.here.sdk.traffic">`TrafficDataProvider`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getTrafficDataProvider ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the traffic data provider that provides internal traffic information considering in routing.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">`TaskHandle`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

      importRoute ( RouteHandle routeHandle, RefreshRouteOptions refreshRouteOptions, CalculateRouteCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">`TaskHandle`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      importRoute ( RouteHandle routeHandle, RoutingOptions options, CalculateRouteCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Asynchronously recreates a route from the RouteHandle provided, i.e.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">`TaskHandle`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      refreshRoute ( RefreshRouteParameters refreshRouteParameters, RoutingOptions routingOptions, CalculateRouteCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Asynchronously refreshes a previously calculated route from the provided RouteHandle , updating the starting point and route metadata based on RoutingOptions .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">`TaskHandle`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      returnToRoute ( Route route, Waypoint startingPoint,
       int lastTraveledSectionIndex,
       int traveledDistanceOnLastSectionInMeters, CalculateRouteCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Asynchronously calculates a new route that leads back to the original route.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setInternalOption ( String key, String value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  This method sets internal options that controls offline route calculation behavior.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setTrafficDataProvider ( TrafficDataProvider value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the traffic data provider that provides internal traffic information considering in routing.

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

    ### OfflineRoutingEngine

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">OfflineRoutingEngine</span>() throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span>

    </div>

    <div class="block">

    Creates a new instance of this class.

    </div>

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">`InstantiationErrorException`</a> -

    Indicates what went wrong when the instantiation was attempted.

    </div>

  - <div id="sdk-for-android-navigate-init-com-here-sdk-core-engine-SDKNativeEngine" class="section detail">

    ### OfflineRoutingEngine

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">OfflineRoutingEngine</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</span> throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span>

    </div>

    <div class="block">

    Creates a new instance of OfflineRoutingEngine.

    </div>

    Parameters:  
    `sdkEngine` -

    An SDKEngine instance.

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">`InstantiationErrorException`</a> -

    Indicates what went wrong when the instantiation was attempted.

    </div>

  - <div id="sdk-for-android-navigate-init-com-here-sdk-core-engine-SDKNativeEngine-com-here-sdk-routing-OfflineRoutingEngineOptions" class="section detail">

    ### OfflineRoutingEngine

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">OfflineRoutingEngine</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-offlineroutingengineoptions" title="class in com.here.sdk.routing">OfflineRoutingEngineOptions</a> options)</span> throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span>

    </div>

    <div class="block">

    Creates a new instance of OfflineRoutingEngine.

    </div>

    Parameters:  
    `sdkEngine` -

    An SDKEngine instance.

    `options` -

    Options to configure offline routing engine.

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">`InstantiationErrorException`</a> -

    Indicates what went wrong when the instantiation was attempted.

    </div>

  </div>

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-refreshRoute-com-here-sdk-routing-RefreshRouteParameters-com-here-sdk-routing-RoutingOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### refreshRoute

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">refreshRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-refreshrouteparameters" title="class in com.here.sdk.routing">RefreshRouteParameters</a> refreshRouteParameters, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-routingoptions" title="class in com.here.sdk.routing">RoutingOptions</a> routingOptions, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span>

    </div>

    <div class="block">

    Asynchronously refreshes a previously calculated route from the provided RouteHandle , updating the starting point and route metadata based on RoutingOptions . The route shape from the new starting point to the destination remains unchanged, and only metadata such as arrival time and traffic delays are updated.

    </div>

    Parameters:  
    `refreshRouteParameters` -

    The parameters used to refresh the route

    `routingOptions` -

    The options define the vehicle and route options used to calculate the route.

    `callback` -

    Callback object that will be invoked after refreshing the route. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-navigate-importRoute-com-here-sdk-routing-RouteHandle-com-here-sdk-routing-RefreshRouteOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### importRoute

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">importRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-routehandle" title="class in com.here.sdk.routing">RouteHandle</a> routeHandle, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-refreshrouteoptions" title="class in com.here.sdk.routing">RefreshRouteOptions</a> refreshRouteOptions, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use the

        import_route()

    method with RoutingOptions parameter instead.
    </p>

    </div>

    </div>

    <div class="block">

    Asynchronously recreates a route from the RouteHandle provided, i.e. refreshes a previously calculated route, with the specified RefreshRouteOptions . A route handle can be invalid when the map data changes that is used by the HERE sdk to recreate the route. This happens regularly. Therefore, the route handle is not meant to be persisted for a longer time.

    </div>

    Parameters:  
    `routeHandle` -

    The route handle holding the route to be refreshed.

    `refreshRouteOptions` -

    Options to import the route from handle.

    `callback` -

    Callback object that will be invoked after refreshing the route. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-navigate-importRoute-com-here-sdk-routing-RouteHandle-com-here-sdk-routing-RoutingOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### importRoute

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">importRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-routehandle" title="class in com.here.sdk.routing">RouteHandle</a> routeHandle, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-routingoptions" title="class in com.here.sdk.routing">RoutingOptions</a> options, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span>

    </div>

    <div class="block">

    Asynchronously recreates a route from the RouteHandle provided, i.e. refreshes a previously calculated route, with the specified RefreshRouteOptions . A route handle can be invalid when the map data changes that is used by the HERE sdk to recreate the route. This happens regularly. Therefore, the route handle is not meant to be persisted for a longer time.

    </div>

    Parameters:  
    `routeHandle` -

    The route handle holding the route to be refreshed.

    `options` -

    Options to import the route from handle.

    `callback` -

    Callback object that will be invoked after refreshing the route. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-navigate-setInternalOption-java-lang-String-java-lang-String" class="section detail">

    ### setInternalOption

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setInternalOption</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> key, @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> value)</span>

    </div>

    <div class="block">

    This method sets internal options that controls offline route calculation behavior. Unsupported options will be logged as warnings. Undocumented options can change their meaning without going through deprecation process.

    </div>

    Parameters:  
    `key` -

    Option name

    `value` -

    New option value

    </div>

  - <div id="sdk-for-android-navigate-getTrafficDataProvider" class="section detail">

    ### getTrafficDataProvider

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficdataprovider" title="class in com.here.sdk.traffic">TrafficDataProvider</a></span> <span class="element-name">getTrafficDataProvider</span>()

    </div>

    <div class="block">

    Gets the traffic data provider that provides internal traffic information considering in routing. If the traffic data provider is null , traffic is not considered in routing.

    </div>

    Returns:  
    The traffic data provider that gets internal traffic information considering in routing.

    </div>

  - <div id="sdk-for-android-navigate-setTrafficDataProvider-com-here-sdk-traffic-TrafficDataProvider" class="section detail">

    ### setTrafficDataProvider

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTrafficDataProvider</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficdataprovider" title="class in com.here.sdk.traffic">TrafficDataProvider</a> value)</span>

    </div>

    <div class="block">

    Sets the traffic data provider that provides internal traffic information considering in routing. If the traffic data provider is null , traffic is not considered in routing.

    </div>

    Parameters:  
    `value` -

    The traffic data provider that gets internal traffic information considering in routing.

    </div>

  - <div id="sdk-for-android-navigate-calculateRoute-java-util-List-com-here-sdk-routing-RoutingOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### calculateRoute

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">calculateRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-routing-waypoint" title="class in com.here.sdk.routing">Waypoint</a>\> waypoints, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-routingoptions" title="class in com.here.sdk.routing">RoutingOptions</a> options, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span>

    </div>

    <div class="block">

    Asynchronously calculates a route from one point to another, passing through the given waypoints in the given order.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-routing-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.RoutingOptions,com.here.sdk.routing.CalculateRouteCallback">`calculateRoute`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-routing-routinginterface" title="interface in com.here.sdk.routing">`RoutingInterface`</a>

    Parameters:  
    `waypoints` -

    The list of waypoints used to calculate the route. The first element marks the starting position, the last marks the destination. Waypoints in between are interpreted as intermediate. An <a href="sdk-for-android-navigate-com-here-sdk-routing-routingerror#INVALID_PARAMETER">`RoutingError.INVALID_PARAMETER`</a> error is generated when the waypoint list contains less than two elements or when the first and the last waypoints are not of type <a href="sdk-for-android-navigate-com-here-sdk-routing-waypointtype#STOPOVER">`WaypointType.STOPOVER`</a>.

    `options` -

    Options describing routing options.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-navigate-calculateRoute-java-util-List-com-here-sdk-routing-CarOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### calculateRoute

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">calculateRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-routing-waypoint" title="class in com.here.sdk.routing">Waypoint</a>\> waypoints, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-caroptions" title="class in com.here.sdk.routing">CarOptions</a> carOptions, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use the

        calculate_route()

    methods with RoutingOptions parameter instead.
    </p>

    </div>

    </div>

    <div class="block">

    Asynchronously calculates a car route from one point to another, passing through the given waypoints in the given order.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-routing-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.CarOptions,com.here.sdk.routing.CalculateRouteCallback">`calculateRoute`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-routing-routinginterface" title="interface in com.here.sdk.routing">`RoutingInterface`</a>

    Parameters:  
    `waypoints` -

    The list of waypoints used to calculate the route. The first element marks the starting position, the last marks the destination. Waypoints in between are interpreted as intermediate. An <a href="sdk-for-android-navigate-com-here-sdk-routing-routingerror#INVALID_PARAMETER">`RoutingError.INVALID_PARAMETER`</a> error is generated when the waypoint list contains less than two elements or when the first and the last waypoints are not of type <a href="sdk-for-android-navigate-com-here-sdk-routing-waypointtype#STOPOVER">`WaypointType.STOPOVER`</a>.

    `carOptions` -

    Options specific for car route calculation, along with common route options.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-navigate-calculateRoute-java-util-List-com-here-sdk-routing-PedestrianOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### calculateRoute

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">calculateRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-routing-waypoint" title="class in com.here.sdk.routing">Waypoint</a>\> waypoints, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-pedestrianoptions" title="class in com.here.sdk.routing">PedestrianOptions</a> pedestrianOptions, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use the

        calculate_route()

    methods with RoutingOptions parameter instead.
    </p>

    </div>

    </div>

    <div class="block">

    Asynchronously calculates a pedestrian route from one point to another, passing through the given waypoints in the given order.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-routing-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.PedestrianOptions,com.here.sdk.routing.CalculateRouteCallback">`calculateRoute`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-routing-routinginterface" title="interface in com.here.sdk.routing">`RoutingInterface`</a>

    Parameters:  
    `waypoints` -

    The list of waypoints used to calculate the route. The first element marks the starting position, the last marks the destination. Waypoints in between are interpreted as intermediate. An <a href="sdk-for-android-navigate-com-here-sdk-routing-routingerror#INVALID_PARAMETER">`RoutingError.INVALID_PARAMETER`</a> error is generated when the waypoint list contains less than two elements or when the first and the last waypoints are not of type <a href="sdk-for-android-navigate-com-here-sdk-routing-waypointtype#STOPOVER">`WaypointType.STOPOVER`</a>.

    `pedestrianOptions` -

    Options specific for pedestrian route calculation, along with common route options. Note that <a href="sdk-for-android-navigate-com-here-sdk-routing-optimizationmode#SHORTEST">`OptimizationMode.SHORTEST`</a> is is not supported for pedestrians and converted to <a href="sdk-for-android-navigate-com-here-sdk-routing-optimizationmode#FASTEST">`OptimizationMode.FASTEST`</a> automatically.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-navigate-calculateRoute-java-util-List-com-here-sdk-routing-TruckOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### calculateRoute

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">calculateRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-routing-waypoint" title="class in com.here.sdk.routing">Waypoint</a>\> waypoints, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-truckoptions" title="class in com.here.sdk.routing">TruckOptions</a> truckOptions, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use the

        calculate_route()

    methods with RoutingOptions parameter instead.
    </p>

    </div>

    </div>

    <div class="block">

    Asynchronously calculates a truck route from one point to another, passing through the given waypoints in the given order.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-routing-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.TruckOptions,com.here.sdk.routing.CalculateRouteCallback">`calculateRoute`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-routing-routinginterface" title="interface in com.here.sdk.routing">`RoutingInterface`</a>

    Parameters:  
    `waypoints` -

    The list of waypoints used to calculate the route. The first element marks the starting position, the last marks the destination. Waypoints in between are interpreted as intermediate. An <a href="sdk-for-android-navigate-com-here-sdk-routing-routingerror#INVALID_PARAMETER">`RoutingError.INVALID_PARAMETER`</a> error is generated when the waypoint list contains less than two elements or when the first and the last waypoints are not of type <a href="sdk-for-android-navigate-com-here-sdk-routing-waypointtype#STOPOVER">`WaypointType.STOPOVER`</a>.

    `truckOptions` -

    Options specific for truck route calculation, along with common route options.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-navigate-calculateRoute-java-util-List-com-here-sdk-routing-ScooterOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### calculateRoute

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">calculateRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-routing-waypoint" title="class in com.here.sdk.routing">Waypoint</a>\> waypoints, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-scooteroptions" title="class in com.here.sdk.routing">ScooterOptions</a> scooterOptions, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use the

        calculate_route()

    methods with RoutingOptions parameter instead.
    </p>

    </div>

    </div>

    <div class="block">

    Asynchronously calculates a scooter route from one point to another, passing through the given waypoints in the given order.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-routing-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.ScooterOptions,com.here.sdk.routing.CalculateRouteCallback">`calculateRoute`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-routing-routinginterface" title="interface in com.here.sdk.routing">`RoutingInterface`</a>

    Parameters:  
    `waypoints` -

    The list of waypoints used to calculate the route. The first element marks the starting position, the last marks the destination. Waypoints in between are interpreted as intermediate. An <a href="sdk-for-android-navigate-com-here-sdk-routing-routingerror#INVALID_PARAMETER">`RoutingError.INVALID_PARAMETER`</a> error is generated when the waypoint list contains less than two elements or when the first and the last waypoints are not of type <a href="sdk-for-android-navigate-com-here-sdk-routing-waypointtype#STOPOVER">`WaypointType.STOPOVER`</a>.

    `scooterOptions` -

    Options specific for scooter route calculation, along with common route options. Note that <a href="sdk-for-android-navigate-com-here-sdk-routing-optimizationmode#SHORTEST">`OptimizationMode.SHORTEST`</a> is is not supported for scooters and converted to <a href="sdk-for-android-navigate-com-here-sdk-routing-optimizationmode#FASTEST">`OptimizationMode.FASTEST`</a> automatically.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-navigate-calculateRoute-java-util-List-com-here-sdk-routing-BicycleOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### calculateRoute

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">calculateRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-routing-waypoint" title="class in com.here.sdk.routing">Waypoint</a>\> waypoints, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-bicycleoptions" title="class in com.here.sdk.routing">BicycleOptions</a> bicycleOptions, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use the

        calculate_route()

    methods with RoutingOptions parameter instead.
    </p>

    </div>

    </div>

    <div class="block">

    Asynchronously calculates a bicycle route from one point to another, passing through the given waypoints in the given order.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-routing-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.BicycleOptions,com.here.sdk.routing.CalculateRouteCallback">`calculateRoute`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-routing-routinginterface" title="interface in com.here.sdk.routing">`RoutingInterface`</a>

    Parameters:  
    `waypoints` -

    The list of waypoints used to calculate the route. The first element marks the starting position, the last marks the destination. Waypoints in between are interpreted as intermediate. An <a href="sdk-for-android-navigate-com-here-sdk-routing-routingerror#INVALID_PARAMETER">`RoutingError.INVALID_PARAMETER`</a> error is generated when the waypoint list contains less than two elements or when the first and the last waypoints are not of type <a href="sdk-for-android-navigate-com-here-sdk-routing-waypointtype#STOPOVER">`WaypointType.STOPOVER`</a>.

    `bicycleOptions` -

    Options specific for bicycle route calculation, along with common route options. Note that <a href="sdk-for-android-navigate-com-here-sdk-routing-optimizationmode#SHORTEST">`OptimizationMode.SHORTEST`</a> is is not supported for bicycles and converted to <a href="sdk-for-android-navigate-com-here-sdk-routing-optimizationmode#FASTEST">`OptimizationMode.FASTEST`</a> automatically.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-navigate-calculateRoute-java-util-List-com-here-sdk-routing-TaxiOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### calculateRoute

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">calculateRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-routing-waypoint" title="class in com.here.sdk.routing">Waypoint</a>\> waypoints, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-taxioptions" title="class in com.here.sdk.routing">TaxiOptions</a> taxiOptions, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use the

        calculate_route()

    methods with RoutingOptions parameter instead.
    </p>

    </div>

    </div>

    <div class="block">

    Asynchronously calculates a taxi route from one point to another, passing through the given waypoints in the given order.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-routing-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.TaxiOptions,com.here.sdk.routing.CalculateRouteCallback">`calculateRoute`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-routing-routinginterface" title="interface in com.here.sdk.routing">`RoutingInterface`</a>

    Parameters:  
    `waypoints` -

    The list of waypoints used to calculate the route. The first element marks the starting position, the last marks the destination. Waypoints in between are interpreted as intermediate. An <a href="sdk-for-android-navigate-com-here-sdk-routing-routingerror#INVALID_PARAMETER">`RoutingError.INVALID_PARAMETER`</a> error is generated when the waypoint list contains less than two elements or when the first and the last waypoints are not of type <a href="sdk-for-android-navigate-com-here-sdk-routing-waypointtype#STOPOVER">`WaypointType.STOPOVER`</a>.

    `taxiOptions` -

    Options specific for taxi route calculation, along with common route options. Note that <a href="sdk-for-android-navigate-com-here-sdk-routing-optimizationmode#SHORTEST">`OptimizationMode.SHORTEST`</a> is is not supported for taxis and converted to <a href="sdk-for-android-navigate-com-here-sdk-routing-optimizationmode#FASTEST">`OptimizationMode.FASTEST`</a> automatically.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-navigate-calculateRoute-java-util-List-com-here-sdk-routing-EVCarOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### calculateRoute

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">calculateRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-routing-waypoint" title="class in com.here.sdk.routing">Waypoint</a>\> waypoints, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-evcaroptions" title="class in com.here.sdk.routing">EVCarOptions</a> evCarOptions, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use the

        calculate_route()

    methods with RoutingOptions parameter instead.
    </p>

    </div>

    </div>

    <div class="block">

    Asynchronously calculates an electric car route from one point to another, passing through the given waypoints in the given order.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-routing-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.EVCarOptions,com.here.sdk.routing.CalculateRouteCallback">`calculateRoute`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-routing-routinginterface" title="interface in com.here.sdk.routing">`RoutingInterface`</a>

    Parameters:  
    `waypoints` -

    The list of waypoints used to calculate the route. The first element marks the starting position, the last marks the destination. Waypoints in between are interpreted as intermediate. An <a href="sdk-for-android-navigate-com-here-sdk-routing-routingerror#INVALID_PARAMETER">`RoutingError.INVALID_PARAMETER`</a> error is generated when the waypoint list contains less than two elements or when the first and the last waypoints are not of type <a href="sdk-for-android-navigate-com-here-sdk-routing-waypointtype#STOPOVER">`WaypointType.STOPOVER`</a>.

    `evCarOptions` -

    Options specific for an electric car route calculation, along with common route options.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-navigate-calculateRoute-java-util-List-com-here-sdk-routing-EVTruckOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### calculateRoute

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">calculateRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-routing-waypoint" title="class in com.here.sdk.routing">Waypoint</a>\> waypoints, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-evtruckoptions" title="class in com.here.sdk.routing">EVTruckOptions</a> evTruckOptions, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use the

        calculate_route()

    methods with RoutingOptions parameter instead.
    </p>

    </div>

    </div>

    <div class="block">

    Asynchronously calculates an electic truck route from one point to another, passing through the given waypoints in the given order.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-routing-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.EVTruckOptions,com.here.sdk.routing.CalculateRouteCallback">`calculateRoute`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-routing-routinginterface" title="interface in com.here.sdk.routing">`RoutingInterface`</a>

    Parameters:  
    `waypoints` -

    The list of waypoints used to calculate the route. The first element marks the starting position, the last marks the destination. Waypoints in between are interpreted as intermediate. An <a href="sdk-for-android-navigate-com-here-sdk-routing-routingerror#INVALID_PARAMETER">`RoutingError.INVALID_PARAMETER`</a> error is generated when the waypoint list contains less than two elements or when the first and the last waypoints are not of type <a href="sdk-for-android-navigate-com-here-sdk-routing-waypointtype#STOPOVER">`WaypointType.STOPOVER`</a>.

    `evTruckOptions` -

    Options specific for an electric truck route calculation, along with common route options.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-navigate-calculateRoute-java-util-List-com-here-sdk-routing-BusOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### calculateRoute

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">calculateRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-routing-waypoint" title="class in com.here.sdk.routing">Waypoint</a>\> waypoints, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-busoptions" title="class in com.here.sdk.routing">BusOptions</a> busOptions, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use the

        calculate_route()

    methods with RoutingOptions parameter instead.
    </p>

    </div>

    </div>

    <div class="block">

    Asynchronously calculates a bus route from one point to another, passing through the given waypoints in the given order.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-routing-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.BusOptions,com.here.sdk.routing.CalculateRouteCallback">`calculateRoute`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-routing-routinginterface" title="interface in com.here.sdk.routing">`RoutingInterface`</a>

    Parameters:  
    `waypoints` -

    The list of waypoints used to calculate the route. The first element marks the starting position, the last marks the destination. Waypoints in between are interpreted as intermediate. An <a href="sdk-for-android-navigate-com-here-sdk-routing-routingerror#INVALID_PARAMETER">`RoutingError.INVALID_PARAMETER`</a> error is generated when the waypoint list contains less than two elements or when the first and the last waypoints are not of type <a href="sdk-for-android-navigate-com-here-sdk-routing-waypointtype#STOPOVER">`WaypointType.STOPOVER`</a>.

    `busOptions` -

    Options specific for a bus route calculation, along with common route options.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-navigate-calculateRoute-java-util-List-com-here-sdk-routing-PrivateBusOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### calculateRoute

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">calculateRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-routing-waypoint" title="class in com.here.sdk.routing">Waypoint</a>\> waypoints, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-privatebusoptions" title="class in com.here.sdk.routing">PrivateBusOptions</a> privateBusOptions, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use the

        calculate_route()

    methods with RoutingOptions parameter instead.
    </p>

    </div>

    </div>

    <div class="block">

    Asynchronously calculates a private bus route from one point to another, passing through the given waypoints in the given order.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-routing-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.PrivateBusOptions,com.here.sdk.routing.CalculateRouteCallback">`calculateRoute`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-routing-routinginterface" title="interface in com.here.sdk.routing">`RoutingInterface`</a>

    Parameters:  
    `waypoints` -

    The list of waypoints used to calculate the route. The first element marks the starting position, the last marks the destination. Waypoints in between are interpreted as intermediate. An <a href="sdk-for-android-navigate-com-here-sdk-routing-routingerror#INVALID_PARAMETER">`RoutingError.INVALID_PARAMETER`</a> error is generated when the waypoint list contains less than two elements or when the first and the last waypoints are not of type <a href="sdk-for-android-navigate-com-here-sdk-routing-waypointtype#STOPOVER">`WaypointType.STOPOVER`</a>.

    `privateBusOptions` -

    Options specific for a private bus route calculation, along with common route options.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-navigate-returnToRoute-com-here-sdk-routing-Route-com-here-sdk-routing-Waypoint-int-int-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### returnToRoute

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">returnToRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-route" title="class in com.here.sdk.routing">Route</a> route, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-waypoint" title="class in com.here.sdk.routing">Waypoint</a> startingPoint, int lastTraveledSectionIndex, int traveledDistanceOnLastSectionInMeters, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-routing-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span>

    </div>

    <div class="block">

    Asynchronously calculates a new route that leads back to the original route. The part of the original route which was already traveled by the user is ignored. Note: Stopover waypoints are guaranteed to be visited. Pass-through waypoints will be ignored. Additionally, the following route options are ignored: RouteOptions.alternatives , RouteOptions.arrivalTime , and RouteOptions.optimizationMode . Most route options are only applied to the newly calculated part back to the route. An application may use this method to submit a new starting point for a previously calculated route. This method tries to avoid a costly route re-calculation as much as possible. In case returning to the route without re-calculation is not possible, a new route is calculated, while trying to salvage the previous route as much as possible. However, a completely new route containing no part of the previous route is possible, too. Note that this function uses only a limited amount of map data around the new origin. Therefore, it may also work fine with temporarily cached map data. It may also copy some of the original route data into the new route. A typical use case is to await at least 3 RouteDeviation events before calling this method. Or alternatively, wait at least 10 seconds after getting the first deviation event. On top, the user experience can be improved by checking if the vehicle has moved at least 50 meters since calling this method for the last time. Optionally, it may make sense to verify if the vehicle was ever following the route by checking if RouteDeviation.lastLocationOnRoute is set. Note that deviation events are sent each time a deviation is detected, i.e. for each new location update, regardless if the location has changed or not. More information can be found in the Developer Guide in the "Handle route deviations" section.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-routing-routinginterface#returnToRoute(com.here.sdk.routing.Route,com.here.sdk.routing.Waypoint,int,int,com.here.sdk.routing.CalculateRouteCallback">`returnToRoute`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-routing-routinginterface" title="interface in com.here.sdk.routing">`RoutingInterface`</a>

    Parameters:  
    `route` -

    A <a href="sdk-for-android-navigate-com-here-sdk-routing-route" title="class in com.here.sdk.routing">`Route`</a> calculated using the online or offline route engine. For the offline case, It should not contain an indoor <a href="sdk-for-android-navigate-com-here-sdk-routing-section" title="class in com.here.sdk.routing">`Section`</a> as such routes will fail. For the online case, it should have <a href="sdk-for-android-navigate-com-here-sdk-routing-routehandle" title="class in com.here.sdk.routing">`RouteHandle`</a>.

    `startingPoint` -

    The current location, for example, provided by a `RouteDeviation` event. The waypoint needs to be of type <a href="sdk-for-android-navigate-com-here-sdk-routing-waypointtype#STOPOVER">`WaypointType.STOPOVER`</a>. Otherwise, an <a href="sdk-for-android-navigate-com-here-sdk-routing-routingerror#INVALID_PARAMETER">`RoutingError.INVALID_PARAMETER`</a> error is generated.

    `lastTraveledSectionIndex` -

    Indicates the index of the last traveled route section. Traveled part of the route won't be reused.

    `traveledDistanceOnLastSectionInMeters` -

    Offset in meter to the last visited position on the route section defined by the last traveled section index.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-navigate-dispose" class="section detail">

    ### dispose

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">dispose</span>()

    </div>

    <div class="block">

    Cancels pending requests and closes the background worker thread. Note: This method should be called from main thread.

    </div>

    Specified by:  
    <a href="sdk-for-android-navigate-com-here-sdk-routing-routinginterface#dispose(">`dispose`</a>) in interface <a href="sdk-for-android-navigate-com-here-sdk-routing-routinginterface" title="interface in com.here.sdk.routing">`RoutingInterface`</a>

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

