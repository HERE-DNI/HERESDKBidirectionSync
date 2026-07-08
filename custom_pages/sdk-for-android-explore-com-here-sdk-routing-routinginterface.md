---
title: "RoutingInterface (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-routinginterface"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.routing](sdk-for-android-explore-com-here-sdk-routing-package-summary)

</div>

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

All Known Implementing Classes:  
[`RoutingEngine`](sdk-for-android-explore-com-here-sdk-routing-routingengine "class in com.here.sdk.routing")

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">RoutingInterface</span>

</div>

<div class="block">

Provides the interface for the online and offline routing engines. Note : Clients need to explicitly call dispose() in order to prevent a possible, though unlikely, deadlock on destruction.

</div>

</div>

- <div id="sdk-for-android-explore-method-summary" class="section method-summary">

  <div id="sdk-for-android-explore-method-summary-table">

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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">

      calculateRoute ( List < Waypoint > waypoints, BicycleOptions bicycleOptions, CalculateRouteCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">

      calculateRoute ( List < Waypoint > waypoints, BusOptions busOptions, CalculateRouteCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">

      calculateRoute ( List < Waypoint > waypoints, CarOptions carOptions, CalculateRouteCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">

      calculateRoute ( List < Waypoint > waypoints, EVCarOptions evCarOptions, CalculateRouteCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">

      calculateRoute ( List < Waypoint > waypoints, EVTruckOptions evTruckOptions, CalculateRouteCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">

      calculateRoute ( List < Waypoint > waypoints, PedestrianOptions pedestrianOptions, CalculateRouteCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">

      calculateRoute ( List < Waypoint > waypoints, PrivateBusOptions privateBusOptions, CalculateRouteCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      calculateRoute ( List < Waypoint > waypoints, RoutingOptions options, CalculateRouteCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Asynchronously calculates a route from one point to another, passing through the given waypoints in the given order.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">

      calculateRoute ( List < Waypoint > waypoints, ScooterOptions scooterOptions, CalculateRouteCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">

      calculateRoute ( List < Waypoint > waypoints, TaxiOptions taxiOptions, CalculateRouteCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">

      calculateRoute ( List < Waypoint > waypoints, TruckOptions truckOptions, CalculateRouteCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      dispose ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Cancels pending requests and closes the background worker thread.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      returnToRoute ( Route route, Waypoint startingPoint,
       int lastTraveledSectionIndex,
       int traveledDistanceOnLastSectionInMeters, CalculateRouteCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Asynchronously calculates a new route that leads back to the original route.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-explore-method-detail" class="section method-details">

  - <div id="sdk-for-android-explore-calculateRoute-java-util-List-com-here-sdk-routing-RoutingOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### calculateRoute

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">calculateRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[Waypoint](sdk-for-android-explore-com-here-sdk-routing-waypoint "class in com.here.sdk.routing")\> waypoints, @NonNull [RoutingOptions](sdk-for-android-explore-com-here-sdk-routing-routingoptions "class in com.here.sdk.routing") options, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

    </div>

    <div class="block">

    Asynchronously calculates a route from one point to another, passing through the given waypoints in the given order.

    </div>

    Parameters:  
    `waypoints` -

    The list of waypoints used to calculate the route. The first element marks the starting position, the last marks the destination. Waypoints in between are interpreted as intermediate. An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-com-here-sdk-routing-routingerror#INVALID_PARAMETER) error is generated when the waypoint list contains less than two elements or when the first and the last waypoints are not of type [`WaypointType.STOPOVER`](sdk-for-android-explore-com-here-sdk-routing-waypointtype#STOPOVER).

    `options` -

    Options describing routing options.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-explore-calculateRoute-java-util-List-com-here-sdk-routing-CarOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### calculateRoute

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">calculateRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[Waypoint](sdk-for-android-explore-com-here-sdk-routing-waypoint "class in com.here.sdk.routing")\> waypoints, @NonNull [CarOptions](sdk-for-android-explore-com-here-sdk-routing-caroptions "class in com.here.sdk.routing") carOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

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

    Parameters:  
    `waypoints` -

    The list of waypoints used to calculate the route. The first element marks the starting position, the last marks the destination. Waypoints in between are interpreted as intermediate. An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-com-here-sdk-routing-routingerror#INVALID_PARAMETER) error is generated when the waypoint list contains less than two elements or when the first and the last waypoints are not of type [`WaypointType.STOPOVER`](sdk-for-android-explore-com-here-sdk-routing-waypointtype#STOPOVER).

    `carOptions` -

    Options specific for car route calculation, along with common route options.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-explore-calculateRoute-java-util-List-com-here-sdk-routing-PedestrianOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### calculateRoute

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">calculateRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[Waypoint](sdk-for-android-explore-com-here-sdk-routing-waypoint "class in com.here.sdk.routing")\> waypoints, @NonNull [PedestrianOptions](sdk-for-android-explore-com-here-sdk-routing-pedestrianoptions "class in com.here.sdk.routing") pedestrianOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

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

    Parameters:  
    `waypoints` -

    The list of waypoints used to calculate the route. The first element marks the starting position, the last marks the destination. Waypoints in between are interpreted as intermediate. An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-com-here-sdk-routing-routingerror#INVALID_PARAMETER) error is generated when the waypoint list contains less than two elements or when the first and the last waypoints are not of type [`WaypointType.STOPOVER`](sdk-for-android-explore-com-here-sdk-routing-waypointtype#STOPOVER).

    `pedestrianOptions` -

    Options specific for pedestrian route calculation, along with common route options. Note that [`OptimizationMode.SHORTEST`](sdk-for-android-explore-com-here-sdk-routing-optimizationmode#SHORTEST) is is not supported for pedestrians and converted to [`OptimizationMode.FASTEST`](sdk-for-android-explore-com-here-sdk-routing-optimizationmode#FASTEST) automatically.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-explore-calculateRoute-java-util-List-com-here-sdk-routing-TruckOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### calculateRoute

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">calculateRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[Waypoint](sdk-for-android-explore-com-here-sdk-routing-waypoint "class in com.here.sdk.routing")\> waypoints, @NonNull [TruckOptions](sdk-for-android-explore-com-here-sdk-routing-truckoptions "class in com.here.sdk.routing") truckOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

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

    Parameters:  
    `waypoints` -

    The list of waypoints used to calculate the route. The first element marks the starting position, the last marks the destination. Waypoints in between are interpreted as intermediate. An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-com-here-sdk-routing-routingerror#INVALID_PARAMETER) error is generated when the waypoint list contains less than two elements or when the first and the last waypoints are not of type [`WaypointType.STOPOVER`](sdk-for-android-explore-com-here-sdk-routing-waypointtype#STOPOVER).

    `truckOptions` -

    Options specific for truck route calculation, along with common route options.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-explore-calculateRoute-java-util-List-com-here-sdk-routing-ScooterOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### calculateRoute

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">calculateRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[Waypoint](sdk-for-android-explore-com-here-sdk-routing-waypoint "class in com.here.sdk.routing")\> waypoints, @NonNull [ScooterOptions](sdk-for-android-explore-com-here-sdk-routing-scooteroptions "class in com.here.sdk.routing") scooterOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

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

    Parameters:  
    `waypoints` -

    The list of waypoints used to calculate the route. The first element marks the starting position, the last marks the destination. Waypoints in between are interpreted as intermediate. An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-com-here-sdk-routing-routingerror#INVALID_PARAMETER) error is generated when the waypoint list contains less than two elements or when the first and the last waypoints are not of type [`WaypointType.STOPOVER`](sdk-for-android-explore-com-here-sdk-routing-waypointtype#STOPOVER).

    `scooterOptions` -

    Options specific for scooter route calculation, along with common route options. Note that [`OptimizationMode.SHORTEST`](sdk-for-android-explore-com-here-sdk-routing-optimizationmode#SHORTEST) is is not supported for scooters and converted to [`OptimizationMode.FASTEST`](sdk-for-android-explore-com-here-sdk-routing-optimizationmode#FASTEST) automatically.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-explore-calculateRoute-java-util-List-com-here-sdk-routing-BicycleOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### calculateRoute

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">calculateRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[Waypoint](sdk-for-android-explore-com-here-sdk-routing-waypoint "class in com.here.sdk.routing")\> waypoints, @NonNull [BicycleOptions](sdk-for-android-explore-com-here-sdk-routing-bicycleoptions "class in com.here.sdk.routing") bicycleOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

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

    Parameters:  
    `waypoints` -

    The list of waypoints used to calculate the route. The first element marks the starting position, the last marks the destination. Waypoints in between are interpreted as intermediate. An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-com-here-sdk-routing-routingerror#INVALID_PARAMETER) error is generated when the waypoint list contains less than two elements or when the first and the last waypoints are not of type [`WaypointType.STOPOVER`](sdk-for-android-explore-com-here-sdk-routing-waypointtype#STOPOVER).

    `bicycleOptions` -

    Options specific for bicycle route calculation, along with common route options. Note that [`OptimizationMode.SHORTEST`](sdk-for-android-explore-com-here-sdk-routing-optimizationmode#SHORTEST) is is not supported for bicycles and converted to [`OptimizationMode.FASTEST`](sdk-for-android-explore-com-here-sdk-routing-optimizationmode#FASTEST) automatically.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-explore-calculateRoute-java-util-List-com-here-sdk-routing-TaxiOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### calculateRoute

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">calculateRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[Waypoint](sdk-for-android-explore-com-here-sdk-routing-waypoint "class in com.here.sdk.routing")\> waypoints, @NonNull [TaxiOptions](sdk-for-android-explore-com-here-sdk-routing-taxioptions "class in com.here.sdk.routing") taxiOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

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

    Parameters:  
    `waypoints` -

    The list of waypoints used to calculate the route. The first element marks the starting position, the last marks the destination. Waypoints in between are interpreted as intermediate. An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-com-here-sdk-routing-routingerror#INVALID_PARAMETER) error is generated when the waypoint list contains less than two elements or when the first and the last waypoints are not of type [`WaypointType.STOPOVER`](sdk-for-android-explore-com-here-sdk-routing-waypointtype#STOPOVER).

    `taxiOptions` -

    Options specific for taxi route calculation, along with common route options. Note that [`OptimizationMode.SHORTEST`](sdk-for-android-explore-com-here-sdk-routing-optimizationmode#SHORTEST) is is not supported for taxis and converted to [`OptimizationMode.FASTEST`](sdk-for-android-explore-com-here-sdk-routing-optimizationmode#FASTEST) automatically.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-explore-calculateRoute-java-util-List-com-here-sdk-routing-EVCarOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### calculateRoute

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">calculateRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[Waypoint](sdk-for-android-explore-com-here-sdk-routing-waypoint "class in com.here.sdk.routing")\> waypoints, @NonNull [EVCarOptions](sdk-for-android-explore-com-here-sdk-routing-evcaroptions "class in com.here.sdk.routing") evCarOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

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

    Parameters:  
    `waypoints` -

    The list of waypoints used to calculate the route. The first element marks the starting position, the last marks the destination. Waypoints in between are interpreted as intermediate. An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-com-here-sdk-routing-routingerror#INVALID_PARAMETER) error is generated when the waypoint list contains less than two elements or when the first and the last waypoints are not of type [`WaypointType.STOPOVER`](sdk-for-android-explore-com-here-sdk-routing-waypointtype#STOPOVER).

    `evCarOptions` -

    Options specific for an electric car route calculation, along with common route options.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-explore-calculateRoute-java-util-List-com-here-sdk-routing-EVTruckOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### calculateRoute

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">calculateRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[Waypoint](sdk-for-android-explore-com-here-sdk-routing-waypoint "class in com.here.sdk.routing")\> waypoints, @NonNull [EVTruckOptions](sdk-for-android-explore-com-here-sdk-routing-evtruckoptions "class in com.here.sdk.routing") evTruckOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

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

    Parameters:  
    `waypoints` -

    The list of waypoints used to calculate the route. The first element marks the starting position, the last marks the destination. Waypoints in between are interpreted as intermediate. An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-com-here-sdk-routing-routingerror#INVALID_PARAMETER) error is generated when the waypoint list contains less than two elements or when the first and the last waypoints are not of type [`WaypointType.STOPOVER`](sdk-for-android-explore-com-here-sdk-routing-waypointtype#STOPOVER).

    `evTruckOptions` -

    Options specific for an electric truck route calculation, along with common route options.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-explore-calculateRoute-java-util-List-com-here-sdk-routing-BusOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### calculateRoute

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">calculateRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[Waypoint](sdk-for-android-explore-com-here-sdk-routing-waypoint "class in com.here.sdk.routing")\> waypoints, @NonNull [BusOptions](sdk-for-android-explore-com-here-sdk-routing-busoptions "class in com.here.sdk.routing") busOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

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

    Parameters:  
    `waypoints` -

    The list of waypoints used to calculate the route. The first element marks the starting position, the last marks the destination. Waypoints in between are interpreted as intermediate. An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-com-here-sdk-routing-routingerror#INVALID_PARAMETER) error is generated when the waypoint list contains less than two elements or when the first and the last waypoints are not of type [`WaypointType.STOPOVER`](sdk-for-android-explore-com-here-sdk-routing-waypointtype#STOPOVER).

    `busOptions` -

    Options specific for a bus route calculation, along with common route options.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-explore-calculateRoute-java-util-List-com-here-sdk-routing-PrivateBusOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### calculateRoute

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">calculateRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[Waypoint](sdk-for-android-explore-com-here-sdk-routing-waypoint "class in com.here.sdk.routing")\> waypoints, @NonNull [PrivateBusOptions](sdk-for-android-explore-com-here-sdk-routing-privatebusoptions "class in com.here.sdk.routing") privateBusOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

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

    Parameters:  
    `waypoints` -

    The list of waypoints used to calculate the route. The first element marks the starting position, the last marks the destination. Waypoints in between are interpreted as intermediate. An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-com-here-sdk-routing-routingerror#INVALID_PARAMETER) error is generated when the waypoint list contains less than two elements or when the first and the last waypoints are not of type [`WaypointType.STOPOVER`](sdk-for-android-explore-com-here-sdk-routing-waypointtype#STOPOVER).

    `privateBusOptions` -

    Options specific for a private bus route calculation, along with common route options.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-explore-returnToRoute-com-here-sdk-routing-Route-com-here-sdk-routing-Waypoint-int-int-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### returnToRoute

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">returnToRoute</span><wbr></wbr><span class="parameters">(@NonNull [Route](sdk-for-android-explore-com-here-sdk-routing-route "class in com.here.sdk.routing") route, @NonNull [Waypoint](sdk-for-android-explore-com-here-sdk-routing-waypoint "class in com.here.sdk.routing") startingPoint, int lastTraveledSectionIndex, int traveledDistanceOnLastSectionInMeters, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

    </div>

    <div class="block">

    Asynchronously calculates a new route that leads back to the original route. The part of the original route which was already traveled by the user is ignored. Note: Stopover waypoints are guaranteed to be visited. Pass-through waypoints will be ignored. Additionally, the following route options are ignored: RouteOptions.alternatives , RouteOptions.arrivalTime , and RouteOptions.optimizationMode . Most route options are only applied to the newly calculated part back to the route. An application may use this method to submit a new starting point for a previously calculated route. This method tries to avoid a costly route re-calculation as much as possible. In case returning to the route without re-calculation is not possible, a new route is calculated, while trying to salvage the previous route as much as possible. However, a completely new route containing no part of the previous route is possible, too. Note that this function uses only a limited amount of map data around the new origin. Therefore, it may also work fine with temporarily cached map data. It may also copy some of the original route data into the new route. A typical use case is to await at least 3 RouteDeviation events before calling this method. Or alternatively, wait at least 10 seconds after getting the first deviation event. On top, the user experience can be improved by checking if the vehicle has moved at least 50 meters since calling this method for the last time. Optionally, it may make sense to verify if the vehicle was ever following the route by checking if RouteDeviation.lastLocationOnRoute is set. Note that deviation events are sent each time a deviation is detected, i.e. for each new location update, regardless if the location has changed or not. More information can be found in the Developer Guide in the "Handle route deviations" section.

    </div>

    Parameters:  
    `route` -

    A [`Route`](sdk-for-android-explore-com-here-sdk-routing-route "class in com.here.sdk.routing") calculated using the online or offline route engine. For the offline case, It should not contain an indoor [`Section`](sdk-for-android-explore-com-here-sdk-routing-section "class in com.here.sdk.routing") as such routes will fail. For the online case, it should have [`RouteHandle`](sdk-for-android-explore-com-here-sdk-routing-routehandle "class in com.here.sdk.routing").

    `startingPoint` -

    The current location, for example, provided by a `RouteDeviation` event. The waypoint needs to be of type [`WaypointType.STOPOVER`](sdk-for-android-explore-com-here-sdk-routing-waypointtype#STOPOVER). Otherwise, an [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-com-here-sdk-routing-routingerror#INVALID_PARAMETER) error is generated.

    `lastTraveledSectionIndex` -

    Indicates the index of the last traveled route section. Traveled part of the route won't be reused.

    `traveledDistanceOnLastSectionInMeters` -

    Offset in meter to the last visited position on the route section defined by the last traveled section index.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-explore-dispose" class="section detail">

    ### dispose

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">dispose</span>()

    </div>

    <div class="block">

    Cancels pending requests and closes the background worker thread. Note: This method should be called from main thread.

    </div>

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

