---
title: "RoutingInterface (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestroutinginterface"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface RoutingInterface

All Known Implementing Classes:
[`RoutingEngine`](sdk-for-android-explore-api-reference-latestroutingengine "class in com.here.sdk.routing")

------------------------------------------------------------------------
public interface RoutingInterface
Provides the interface for the online and offline routing engines.

**Note**: Clients need to explicitly call [`dispose()`](#dispose()) in order to prevent a possible, though unlikely, deadlock on destruction.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods
  Deprecated Methods

  Modifier and Type

  Method

  Description

  [`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [calculateRoute](#calculateRoute(java.util.List,com.here.sdk.routing.BicycleOptions,com.here.sdk.routing.CalculateRouteCallback))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Waypoint`](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing")`> waypoints, `[`BicycleOptions`](sdk-for-android-explore-api-reference-latestbicycleoptions "class in com.here.sdk.routing")` bicycleOptions, `[`CalculateRouteCallback`](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing")` callback)`

Deprecated.
Will be removed in v4.28.0.

  [`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [calculateRoute](#calculateRoute(java.util.List,com.here.sdk.routing.BusOptions,com.here.sdk.routing.CalculateRouteCallback))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Waypoint`](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing")`> waypoints, `[`BusOptions`](sdk-for-android-explore-api-reference-latestbusoptions "class in com.here.sdk.routing")` busOptions, `[`CalculateRouteCallback`](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing")` callback)`

Deprecated.
Will be removed in v4.28.0.

  [`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [calculateRoute](#calculateRoute(java.util.List,com.here.sdk.routing.CarOptions,com.here.sdk.routing.CalculateRouteCallback))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Waypoint`](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing")`> waypoints, `[`CarOptions`](sdk-for-android-explore-api-reference-latestcaroptions "class in com.here.sdk.routing")` carOptions, `[`CalculateRouteCallback`](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing")` callback)`

Deprecated.
Will be removed in v4.28.0.

  [`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [calculateRoute](#calculateRoute(java.util.List,com.here.sdk.routing.EVCarOptions,com.here.sdk.routing.CalculateRouteCallback))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Waypoint`](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing")`> waypoints, `[`EVCarOptions`](sdk-for-android-explore-api-reference-latestevcaroptions "class in com.here.sdk.routing")` evCarOptions, `[`CalculateRouteCallback`](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing")` callback)`

Deprecated.
Will be removed in v4.28.0.

  [`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [calculateRoute](#calculateRoute(java.util.List,com.here.sdk.routing.EVTruckOptions,com.here.sdk.routing.CalculateRouteCallback))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Waypoint`](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing")`> waypoints, `[`EVTruckOptions`](sdk-for-android-explore-api-reference-latestevtruckoptions "class in com.here.sdk.routing")` evTruckOptions, `[`CalculateRouteCallback`](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing")` callback)`

Deprecated.
Will be removed in v4.28.0.

  [`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [calculateRoute](#calculateRoute(java.util.List,com.here.sdk.routing.PedestrianOptions,com.here.sdk.routing.CalculateRouteCallback))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Waypoint`](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing")`> waypoints, `[`PedestrianOptions`](sdk-for-android-explore-api-reference-latestpedestrianoptions "class in com.here.sdk.routing")` pedestrianOptions, `[`CalculateRouteCallback`](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing")` callback)`

Deprecated.
Will be removed in v4.28.0.

  [`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [calculateRoute](#calculateRoute(java.util.List,com.here.sdk.routing.PrivateBusOptions,com.here.sdk.routing.CalculateRouteCallback))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Waypoint`](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing")`> waypoints, `[`PrivateBusOptions`](sdk-for-android-explore-api-reference-latestprivatebusoptions "class in com.here.sdk.routing")` privateBusOptions, `[`CalculateRouteCallback`](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing")` callback)`

Deprecated.
Will be removed in v4.28.0.

  [`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [calculateRoute](#calculateRoute(java.util.List,com.here.sdk.routing.RoutingOptions,com.here.sdk.routing.CalculateRouteCallback))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Waypoint`](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing")`> waypoints, `[`RoutingOptions`](sdk-for-android-explore-api-reference-latestroutingoptions "class in com.here.sdk.routing")` options, `[`CalculateRouteCallback`](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing")` callback)`

Asynchronously calculates a route from one point to another, passing through the given waypoints in the given order.

[`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [calculateRoute](#calculateRoute(java.util.List,com.here.sdk.routing.ScooterOptions,com.here.sdk.routing.CalculateRouteCallback))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Waypoint`](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing")`> waypoints, `[`ScooterOptions`](sdk-for-android-explore-api-reference-latestscooteroptions "class in com.here.sdk.routing")` scooterOptions, `[`CalculateRouteCallback`](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing")` callback)`

Deprecated.
Will be removed in v4.28.0.

  [`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [calculateRoute](#calculateRoute(java.util.List,com.here.sdk.routing.TaxiOptions,com.here.sdk.routing.CalculateRouteCallback))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Waypoint`](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing")`> waypoints, `[`TaxiOptions`](sdk-for-android-explore-api-reference-latesttaxioptions "class in com.here.sdk.routing")` taxiOptions, `[`CalculateRouteCallback`](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing")` callback)`

Deprecated.
Will be removed in v4.28.0.

  [`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [calculateRoute](#calculateRoute(java.util.List,com.here.sdk.routing.TruckOptions,com.here.sdk.routing.CalculateRouteCallback))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Waypoint`](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing")`> waypoints, `[`TruckOptions`](sdk-for-android-explore-api-reference-latesttruckoptions "class in com.here.sdk.routing")` truckOptions, `[`CalculateRouteCallback`](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing")` callback)`

Deprecated.
Will be removed in v4.28.0.

  `void`

  [dispose](#dispose())`()`

Cancels pending requests and closes the background worker thread.

[`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [returnToRoute](#returnToRoute(com.here.sdk.routing.Route,com.here.sdk.routing.Waypoint,int,int,com.here.sdk.routing.CalculateRouteCallback))`(`[`Route`](sdk-for-android-explore-api-reference-latestroute "class in com.here.sdk.routing")` route, `[`Waypoint`](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing")` startingPoint, int lastTraveledSectionIndex, int traveledDistanceOnLastSectionInMeters, `[`CalculateRouteCallback`](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing")` callback)`

Asynchronously calculates a new route that leads back to the original route.

## Method Details

### calculateRoute

@NonNull [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") calculateRoute(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Waypoint](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing")\> waypoints, @NonNull [RoutingOptions](sdk-for-android-explore-api-reference-latestroutingoptions "class in com.here.sdk.routing") options, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Asynchronously calculates a route from one point to another, passing through the given waypoints in the given order.
Parameters:
    `waypoints` -

    The list of waypoints used to calculate the route. The first element marks the starting position, the last marks the destination. Waypoints in between are interpreted as intermediate.

    An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-api-reference-latestroutingerror#INVALID_PARAMETER) error is generated when the waypoint list contains less than two elements or when the first and the last waypoints are not of type [`WaypointType.STOPOVER`](sdk-for-android-explore-api-reference-latestwaypointtype#STOPOVER).

    `options` -

    Options describing routing options.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### calculateRoute

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @NonNull [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") calculateRoute(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Waypoint](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing")\> waypoints, @NonNull [CarOptions](sdk-for-android-explore-api-reference-latestcaroptions "class in com.here.sdk.routing") carOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Deprecated.
Will be removed in v4.28.0. Use the `calculate_route()` methods with RoutingOptions parameter instead.

Asynchronously calculates a car route from one point to another, passing through the given waypoints in the given order.
Parameters:
    `waypoints` -

    The list of waypoints used to calculate the route. The first element marks the starting position, the last marks the destination. Waypoints in between are interpreted as intermediate.

    An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-api-reference-latestroutingerror#INVALID_PARAMETER) error is generated when the waypoint list contains less than two elements or when the first and the last waypoints are not of type [`WaypointType.STOPOVER`](sdk-for-android-explore-api-reference-latestwaypointtype#STOPOVER).

    `carOptions` -

    Options specific for car route calculation, along with common route options.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### calculateRoute

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @NonNull [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") calculateRoute(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Waypoint](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing")\> waypoints, @NonNull [PedestrianOptions](sdk-for-android-explore-api-reference-latestpedestrianoptions "class in com.here.sdk.routing") pedestrianOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Deprecated.
Will be removed in v4.28.0. Use the `calculate_route()` methods with RoutingOptions parameter instead.

Asynchronously calculates a pedestrian route from one point to another, passing through the given waypoints in the given order.
Parameters:
    `waypoints` -

    The list of waypoints used to calculate the route. The first element marks the starting position, the last marks the destination. Waypoints in between are interpreted as intermediate.

    An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-api-reference-latestroutingerror#INVALID_PARAMETER) error is generated when the waypoint list contains less than two elements or when the first and the last waypoints are not of type [`WaypointType.STOPOVER`](sdk-for-android-explore-api-reference-latestwaypointtype#STOPOVER).

    `pedestrianOptions` -

    Options specific for pedestrian route calculation, along with common route options. Note that [`OptimizationMode.SHORTEST`](sdk-for-android-explore-api-reference-latestoptimizationmode#SHORTEST) is is not supported for pedestrians and converted to [`OptimizationMode.FASTEST`](sdk-for-android-explore-api-reference-latestoptimizationmode#FASTEST) automatically.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### calculateRoute

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @NonNull [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") calculateRoute(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Waypoint](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing")\> waypoints, @NonNull [TruckOptions](sdk-for-android-explore-api-reference-latesttruckoptions "class in com.here.sdk.routing") truckOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Deprecated.
Will be removed in v4.28.0. Use the `calculate_route()` methods with RoutingOptions parameter instead.

Asynchronously calculates a truck route from one point to another, passing through the given waypoints in the given order.
Parameters:
    `waypoints` -

    The list of waypoints used to calculate the route. The first element marks the starting position, the last marks the destination. Waypoints in between are interpreted as intermediate.

    An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-api-reference-latestroutingerror#INVALID_PARAMETER) error is generated when the waypoint list contains less than two elements or when the first and the last waypoints are not of type [`WaypointType.STOPOVER`](sdk-for-android-explore-api-reference-latestwaypointtype#STOPOVER).

    `truckOptions` -

    Options specific for truck route calculation, along with common route options.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### calculateRoute

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @NonNull [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") calculateRoute(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Waypoint](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing")\> waypoints, @NonNull [ScooterOptions](sdk-for-android-explore-api-reference-latestscooteroptions "class in com.here.sdk.routing") scooterOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Deprecated.
Will be removed in v4.28.0. Use the `calculate_route()` methods with RoutingOptions parameter instead.

Asynchronously calculates a scooter route from one point to another, passing through the given waypoints in the given order.
Parameters:
    `waypoints` -

    The list of waypoints used to calculate the route. The first element marks the starting position, the last marks the destination. Waypoints in between are interpreted as intermediate.

    An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-api-reference-latestroutingerror#INVALID_PARAMETER) error is generated when the waypoint list contains less than two elements or when the first and the last waypoints are not of type [`WaypointType.STOPOVER`](sdk-for-android-explore-api-reference-latestwaypointtype#STOPOVER).

    `scooterOptions` -

    Options specific for scooter route calculation, along with common route options. Note that [`OptimizationMode.SHORTEST`](sdk-for-android-explore-api-reference-latestoptimizationmode#SHORTEST) is is not supported for scooters and converted to [`OptimizationMode.FASTEST`](sdk-for-android-explore-api-reference-latestoptimizationmode#FASTEST) automatically.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### calculateRoute

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @NonNull [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") calculateRoute(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Waypoint](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing")\> waypoints, @NonNull [BicycleOptions](sdk-for-android-explore-api-reference-latestbicycleoptions "class in com.here.sdk.routing") bicycleOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Deprecated.
Will be removed in v4.28.0. Use the `calculate_route()` methods with RoutingOptions parameter instead.

Asynchronously calculates a bicycle route from one point to another, passing through the given waypoints in the given order.
Parameters:
    `waypoints` -

    The list of waypoints used to calculate the route. The first element marks the starting position, the last marks the destination. Waypoints in between are interpreted as intermediate.

    An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-api-reference-latestroutingerror#INVALID_PARAMETER) error is generated when the waypoint list contains less than two elements or when the first and the last waypoints are not of type [`WaypointType.STOPOVER`](sdk-for-android-explore-api-reference-latestwaypointtype#STOPOVER).

    `bicycleOptions` -

    Options specific for bicycle route calculation, along with common route options. Note that [`OptimizationMode.SHORTEST`](sdk-for-android-explore-api-reference-latestoptimizationmode#SHORTEST) is is not supported for bicycles and converted to [`OptimizationMode.FASTEST`](sdk-for-android-explore-api-reference-latestoptimizationmode#FASTEST) automatically.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### calculateRoute

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @NonNull [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") calculateRoute(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Waypoint](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing")\> waypoints, @NonNull [TaxiOptions](sdk-for-android-explore-api-reference-latesttaxioptions "class in com.here.sdk.routing") taxiOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Deprecated.
Will be removed in v4.28.0. Use the `calculate_route()` methods with RoutingOptions parameter instead.

Asynchronously calculates a taxi route from one point to another, passing through the given waypoints in the given order.
Parameters:
    `waypoints` -

    The list of waypoints used to calculate the route. The first element marks the starting position, the last marks the destination. Waypoints in between are interpreted as intermediate.

    An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-api-reference-latestroutingerror#INVALID_PARAMETER) error is generated when the waypoint list contains less than two elements or when the first and the last waypoints are not of type [`WaypointType.STOPOVER`](sdk-for-android-explore-api-reference-latestwaypointtype#STOPOVER).

    `taxiOptions` -

    Options specific for taxi route calculation, along with common route options. Note that [`OptimizationMode.SHORTEST`](sdk-for-android-explore-api-reference-latestoptimizationmode#SHORTEST) is is not supported for taxis and converted to [`OptimizationMode.FASTEST`](sdk-for-android-explore-api-reference-latestoptimizationmode#FASTEST) automatically.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### calculateRoute

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @NonNull [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") calculateRoute(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Waypoint](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing")\> waypoints, @NonNull [EVCarOptions](sdk-for-android-explore-api-reference-latestevcaroptions "class in com.here.sdk.routing") evCarOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Deprecated.
Will be removed in v4.28.0. Use the `calculate_route()` methods with RoutingOptions parameter instead.

Asynchronously calculates an electric car route from one point to another, passing through the given waypoints in the given order.
Parameters:
    `waypoints` -

    The list of waypoints used to calculate the route. The first element marks the starting position, the last marks the destination. Waypoints in between are interpreted as intermediate.

    An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-api-reference-latestroutingerror#INVALID_PARAMETER) error is generated when the waypoint list contains less than two elements or when the first and the last waypoints are not of type [`WaypointType.STOPOVER`](sdk-for-android-explore-api-reference-latestwaypointtype#STOPOVER).

    `evCarOptions` -

    Options specific for an electric car route calculation, along with common route options.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### calculateRoute

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @NonNull [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") calculateRoute(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Waypoint](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing")\> waypoints, @NonNull [EVTruckOptions](sdk-for-android-explore-api-reference-latestevtruckoptions "class in com.here.sdk.routing") evTruckOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Deprecated.
Will be removed in v4.28.0. Use the `calculate_route()` methods with RoutingOptions parameter instead.

Asynchronously calculates an electic truck route from one point to another, passing through the given waypoints in the given order.
Parameters:
    `waypoints` -

    The list of waypoints used to calculate the route. The first element marks the starting position, the last marks the destination. Waypoints in between are interpreted as intermediate.

    An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-api-reference-latestroutingerror#INVALID_PARAMETER) error is generated when the waypoint list contains less than two elements or when the first and the last waypoints are not of type [`WaypointType.STOPOVER`](sdk-for-android-explore-api-reference-latestwaypointtype#STOPOVER).

    `evTruckOptions` -

    Options specific for an electric truck route calculation, along with common route options.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### calculateRoute

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @NonNull [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") calculateRoute(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Waypoint](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing")\> waypoints, @NonNull [BusOptions](sdk-for-android-explore-api-reference-latestbusoptions "class in com.here.sdk.routing") busOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Deprecated.
Will be removed in v4.28.0. Use the `calculate_route()` methods with RoutingOptions parameter instead.

Asynchronously calculates a bus route from one point to another, passing through the given waypoints in the given order.
Parameters:
    `waypoints` -

    The list of waypoints used to calculate the route. The first element marks the starting position, the last marks the destination. Waypoints in between are interpreted as intermediate.

    An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-api-reference-latestroutingerror#INVALID_PARAMETER) error is generated when the waypoint list contains less than two elements or when the first and the last waypoints are not of type [`WaypointType.STOPOVER`](sdk-for-android-explore-api-reference-latestwaypointtype#STOPOVER).

    `busOptions` -

    Options specific for a bus route calculation, along with common route options.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### calculateRoute

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @NonNull [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") calculateRoute(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Waypoint](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing")\> waypoints, @NonNull [PrivateBusOptions](sdk-for-android-explore-api-reference-latestprivatebusoptions "class in com.here.sdk.routing") privateBusOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Deprecated.
Will be removed in v4.28.0. Use the `calculate_route()` methods with RoutingOptions parameter instead.

Asynchronously calculates a private bus route from one point to another, passing through the given waypoints in the given order.
Parameters:
    `waypoints` -

    The list of waypoints used to calculate the route. The first element marks the starting position, the last marks the destination. Waypoints in between are interpreted as intermediate.

    An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-api-reference-latestroutingerror#INVALID_PARAMETER) error is generated when the waypoint list contains less than two elements or when the first and the last waypoints are not of type [`WaypointType.STOPOVER`](sdk-for-android-explore-api-reference-latestwaypointtype#STOPOVER).

    `privateBusOptions` -

    Options specific for a private bus route calculation, along with common route options.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### returnToRoute

@NonNull [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") returnToRoute(@NonNull [Route](sdk-for-android-explore-api-reference-latestroute "class in com.here.sdk.routing") route, @NonNull [Waypoint](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing") startingPoint, int lastTraveledSectionIndex, int traveledDistanceOnLastSectionInMeters, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Asynchronously calculates a new route that leads back to the original route. The part of the original route which was already traveled by the user is ignored.

    **Note:** Stopover waypoints are guaranteed to be visited. Pass-through waypoints will be ignored. Additionally, the following route options are ignored: [`RouteOptions.alternatives`](sdk-for-android-explore-api-reference-latestrouteoptions#alternatives), [`RouteOptions.arrivalTime`](sdk-for-android-explore-api-reference-latestrouteoptions#arrivalTime), and [`RouteOptions.optimizationMode`](sdk-for-android-explore-api-reference-latestrouteoptions#optimizationMode). Most route options are only applied to the newly calculated part back to the route.

    An application may use this method to submit a new starting point for a previously calculated route. This method tries to avoid a costly route re-calculation as much as possible. In case returning to the route without re-calculation is not possible, a new route is calculated, while trying to salvage the previous route as much as possible. However, a completely new route containing no part of the previous route is possible, too.

    Note that this function uses only a limited amount of map data around the new origin. Therefore, it may also work fine with temporarily cached map data. It may also copy some of the original route data into the new route.

    A typical use case is to await at least 3 `RouteDeviation` events before calling this method.

    - Or alternatively, wait at least 10 seconds after getting the first deviation event.
    - On top, the user experience can be improved by checking if the vehicle has moved at least 50 meters since calling this method for the last time.
    - Optionally, it may make sense to verify if the vehicle was ever following the route by checking if `RouteDeviation.lastLocationOnRoute` is set.

    Note that deviation events are sent each time a deviation is detected, i.e. for each new location update, regardless if the location has changed or not. More information can be found in the Developer Guide in the "Handle route deviations" section.
Parameters:
    `route` -

    A [`Route`](sdk-for-android-explore-api-reference-latestroute "class in com.here.sdk.routing") calculated using the online or offline route engine. For the offline case, It should not contain an indoor [`Section`](sdk-for-android-explore-api-reference-latestsection "class in com.here.sdk.routing") as such routes will fail. For the online case, it should have [`RouteHandle`](sdk-for-android-explore-api-reference-latestroutehandle "class in com.here.sdk.routing").

    `startingPoint` -

    The current location, for example, provided by a `RouteDeviation` event. The waypoint needs to be of type [`WaypointType.STOPOVER`](sdk-for-android-explore-api-reference-latestwaypointtype#STOPOVER). Otherwise, an [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-api-reference-latestroutingerror#INVALID_PARAMETER) error is generated.

    `lastTraveledSectionIndex` -

    Indicates the index of the last traveled route section. Traveled part of the route won't be reused.

    `traveledDistanceOnLastSectionInMeters` -

    Offset in meter to the last visited position on the route section defined by the last traveled section index.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### dispose

void dispose()

    Cancels pending requests and closes the background worker thread. **Note:** This method should be called from main thread.
