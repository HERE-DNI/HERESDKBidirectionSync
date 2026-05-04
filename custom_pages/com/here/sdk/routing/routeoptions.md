---
title: "RouteOptions (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestrouteoptions"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class RouteOptions

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.RouteOptions
------------------------------------------------------------------------
public final class RouteOptions extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
The options to specify how the route will be calculated.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `int`

  [alternatives](#alternatives)

Maximum number of alternative routes that will be calculated, in addition to the best one.

[Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html)

  [arrivalTime](#arrivalTime)

Optional time when travel is expected to end.

[Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html)

  [departureTime](#departureTime)

Optional time when travel is expected to start.

`boolean`

  [enableRouteHandle](#enableRouteHandle)

A flag that indicates whether the resulting route should contain a [`RouteHandle`](sdk-for-android-explore-api-reference-latestroutehandle "class in com.here.sdk.routing").

`boolean`

  [enableRouteLabels](#enableRouteLabels)

Specifies whether route labels should be included in the route response.

`boolean`

  [enableTolls](#enableTolls)

A flag that indicates whether the resulting route [`Section.getTolls()`](sdk-for-android-explore-api-reference-latestsection#getTolls()) properties should contain tolls data.

[`OptimizationMode`](sdk-for-android-explore-api-reference-latestoptimizationmode "enum class in com.here.sdk.routing")

  [optimizationMode](#optimizationMode)

The optimization mode to be used for route calculation.

`boolean`

  [optimizeWaypointsOrder](#optimizeWaypointsOrder)

A flag that indicates whether the order of waypoints that is passed to `calculateRoute()` should be optimized in the best order.

[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)

  [speedCapInMetersPerSecond](#speedCapInMetersPerSecond)

Specifies the maximum speed in meters per second, which the user wishes not to exceed.

[`TrafficOptimizationMode`](sdk-for-android-explore-api-reference-latesttrafficoptimizationmode "enum class in com.here.sdk.routing")

  [trafficOptimizationMode](#trafficOptimizationMode)

The traffic optimization mode to be used for route calculation.

## Constructor Summary

Constructors

Constructor

  Description

  [RouteOptions](#%3Cinit%3E())`()`

Creates a new instance.

[RouteOptions](#%3Cinit%3E(com.here.sdk.routing.OptimizationMode))`(`[`OptimizationMode`](sdk-for-android-explore-api-reference-latestoptimizationmode "enum class in com.here.sdk.routing")` optimizationMode)`

Creates a new instance.

[RouteOptions](#%3Cinit%3E(com.here.sdk.routing.OptimizationMode,int))`(`[`OptimizationMode`](sdk-for-android-explore-api-reference-latestoptimizationmode "enum class in com.here.sdk.routing")` optimizationMode, int alternatives)`

Creates a new instance.

[RouteOptions](#%3Cinit%3E(com.here.sdk.routing.OptimizationMode,int,java.util.Date))`(`[`OptimizationMode`](sdk-for-android-explore-api-reference-latestoptimizationmode "enum class in com.here.sdk.routing")` optimizationMode, int alternatives, `[Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html)` departureTime)`

Creates a new instance.

[RouteOptions](#%3Cinit%3E(com.here.sdk.routing.OptimizationMode,int,java.util.Date,java.util.Date))`(`[`OptimizationMode`](sdk-for-android-explore-api-reference-latestoptimizationmode "enum class in com.here.sdk.routing")` optimizationMode, int alternatives, `[Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html)` departureTime, `[Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html)` arrivalTime)`

Creates a new instance.

[RouteOptions](#%3Cinit%3E(com.here.sdk.routing.OptimizationMode,int,java.util.Date,java.util.Date,java.lang.Double))`(`[`OptimizationMode`](sdk-for-android-explore-api-reference-latestoptimizationmode "enum class in com.here.sdk.routing")` optimizationMode, int alternatives, `[Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html)` departureTime, `[Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html)` arrivalTime, `[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)` speedCapInMetersPerSecond)`

Creates a new instance.

[RouteOptions](#%3Cinit%3E(com.here.sdk.routing.OptimizationMode,int,java.util.Date,java.util.Date,java.lang.Double,boolean))`(`[`OptimizationMode`](sdk-for-android-explore-api-reference-latestoptimizationmode "enum class in com.here.sdk.routing")` optimizationMode, int alternatives, `[Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html)` departureTime, `[Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html)` arrivalTime, `[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)` speedCapInMetersPerSecond, boolean enableRouteHandle)`

Creates a new instance.

[RouteOptions](#%3Cinit%3E(com.here.sdk.routing.OptimizationMode,int,java.util.Date,java.util.Date,java.lang.Double,boolean,com.here.sdk.routing.TrafficOptimizationMode))`(`[`OptimizationMode`](sdk-for-android-explore-api-reference-latestoptimizationmode "enum class in com.here.sdk.routing")` optimizationMode, int alternatives, `[Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html)` departureTime, `[Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html)` arrivalTime, `[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)` speedCapInMetersPerSecond, boolean enableRouteHandle, `[`TrafficOptimizationMode`](sdk-for-android-explore-api-reference-latesttrafficoptimizationmode "enum class in com.here.sdk.routing")` trafficOptimizationMode)`

Creates a new instance.

[RouteOptions](#%3Cinit%3E(com.here.sdk.routing.OptimizationMode,int,java.util.Date,java.util.Date,java.lang.Double,boolean,com.here.sdk.routing.TrafficOptimizationMode,boolean))`(`[`OptimizationMode`](sdk-for-android-explore-api-reference-latestoptimizationmode "enum class in com.here.sdk.routing")` optimizationMode, int alternatives, `[Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html)` departureTime, `[Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html)` arrivalTime, `[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)` speedCapInMetersPerSecond, boolean enableRouteHandle, `[`TrafficOptimizationMode`](sdk-for-android-explore-api-reference-latesttrafficoptimizationmode "enum class in com.here.sdk.routing")` trafficOptimizationMode, boolean enableTolls)`

Creates a new instance.

[RouteOptions](#%3Cinit%3E(com.here.sdk.routing.OptimizationMode,int,java.util.Date,java.util.Date,java.lang.Double,boolean,com.here.sdk.routing.TrafficOptimizationMode,boolean,boolean))`(`[`OptimizationMode`](sdk-for-android-explore-api-reference-latestoptimizationmode "enum class in com.here.sdk.routing")` optimizationMode, int alternatives, `[Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html)` departureTime, `[Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html)` arrivalTime, `[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)` speedCapInMetersPerSecond, boolean enableRouteHandle, `[`TrafficOptimizationMode`](sdk-for-android-explore-api-reference-latesttrafficoptimizationmode "enum class in com.here.sdk.routing")` trafficOptimizationMode, boolean enableTolls, boolean optimizeWaypointsOrder)`

Creates a new instance.

[RouteOptions](#%3Cinit%3E(com.here.sdk.routing.OptimizationMode,int,java.util.Date,java.util.Date,java.lang.Double,boolean,com.here.sdk.routing.TrafficOptimizationMode,boolean,boolean,boolean))`(`[`OptimizationMode`](sdk-for-android-explore-api-reference-latestoptimizationmode "enum class in com.here.sdk.routing")` optimizationMode, int alternatives, `[Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html)` departureTime, `[Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html)` arrivalTime, `[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)` speedCapInMetersPerSecond, boolean enableRouteHandle, `[`TrafficOptimizationMode`](sdk-for-android-explore-api-reference-latesttrafficoptimizationmode "enum class in com.here.sdk.routing")` trafficOptimizationMode, boolean enableTolls, boolean optimizeWaypointsOrder, boolean enableRouteLabels)`

Creates a new instance.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `boolean`

  [equals](#equals(java.lang.Object))`(`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)` obj)`

  `int`

  [hashCode](#hashCode())`()`

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### optimizationMode

@NonNull public [OptimizationMode](sdk-for-android-explore-api-reference-latestoptimizationmode "enum class in com.here.sdk.routing") optimizationMode

    The optimization mode to be used for route calculation. By default, it is [`OptimizationMode.FASTEST`](sdk-for-android-explore-api-reference-latestoptimizationmode#FASTEST).

### alternatives

public int alternatives

    Maximum number of alternative routes that will be calculated, in addition to the best one. The provided value must be in the range \[0, 6\]. Alternative routes can be unavailable, thus they are not guaranteed to be returned. The order of routes is from the best to the worst, as evaluated by the route calculation algorithm and according to the given input parameters. Defaults to 0, which means there are no alternatives, i.e. only the best route is returned. Must be 0 for isoline calculation.

### departureTime

@Nullable public [Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html) departureTime

    Optional time when travel is expected to start. Traffic speed and incidents shall be taken into account in the calculation of the route, per [`trafficOptimizationMode`](#trafficOptimizationMode). By default, the time is not set. If the time is not set, the current time will be used internally, i.e. now. Therefore, by default, a time-aware route request is initiated including traffic.

    **Note**:

    - Both departure time and [`arrivalTime`](#arrivalTime) cannot be set at the same time.
    - This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00

### arrivalTime

@Nullable public [Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html) arrivalTime

    Optional time when travel is expected to end. Traffic speed and incidents shall be taken into account in the calculation of the route, per [`trafficOptimizationMode`](#trafficOptimizationMode). By default, the time is not set. If the time is not set, the current time will be used internally, to predict the arrival time. Therefore, by default, a time-aware route request is initiated including traffic.

    **Note**:

    - Both [`departureTime`](#departureTime) and arrival time cannot be set at the same time.
    - This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00

### speedCapInMetersPerSecond

@Nullable public [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) speedCapInMetersPerSecond

    Specifies the maximum speed in meters per second, which the user wishes not to exceed. The valid range is \[1, 70\] meters per second. Note that it is valid only for [`TransportMode.CAR`](sdk-for-android-explore-api-reference-latesttransportmode#CAR), [`TransportMode.TRUCK`](sdk-for-android-explore-api-reference-latesttransportmode#TRUCK) and [`TransportMode.SCOOTER`](sdk-for-android-explore-api-reference-latesttransportmode#SCOOTER) transport modes. For car, truck and scooter transport modes, it will affect [`Route.getDuration()`](sdk-for-android-explore-api-reference-latestroute#getDuration()) of the route. Only for scooter transport mode, it may affect the route geometry. Defaults to `null`, which means that no speed cap is set.

### enableRouteHandle

public boolean enableRouteHandle

    A flag that indicates whether the resulting route should contain a [`RouteHandle`](sdk-for-android-explore-api-reference-latestroutehandle "class in com.here.sdk.routing"). Defaults to `false`. Note that a `RouteHandle` generated by the online `RoutingEngine` is not compatible with the `OfflineRoutingEngine` and vice versa.

### trafficOptimizationMode

@NonNull public [TrafficOptimizationMode](sdk-for-android-explore-api-reference-latesttrafficoptimizationmode "enum class in com.here.sdk.routing") trafficOptimizationMode

    The traffic optimization mode to be used for route calculation. By default, it is [`TrafficOptimizationMode.TIME_DEPENDENT`](sdk-for-android-explore-api-reference-latesttrafficoptimizationmode#TIME_DEPENDENT), which enables traffic-aware routing.

### enableTolls

public boolean enableTolls

    A flag that indicates whether the resulting route [`Section.getTolls()`](sdk-for-android-explore-api-reference-latestsection#getTolls()) properties should contain tolls data. Defaults to `false`.

    **Note:** When a route calculation request asks tolls, a pricing scheme with higher rates might be applied. Consult your HERE representative to get more information on the related pricing schemes.

    **Note:** For users of the `OfflineRoutingEngine` this is a beta release of this feature, so there could be a few bugs and unexpected behaviors. The `OfflineRoutingEngine` is only available for the Navigate license. For users of the `RoutingEngine` the feature is stable.

### optimizeWaypointsOrder

public boolean optimizeWaypointsOrder

    A flag that indicates whether the order of waypoints that is passed to `calculateRoute()` should be optimized in the best order. The best order is calculated by the same metrics that are used during regular calculation, e.g. [`OptimizationMode`](sdk-for-android-explore-api-reference-latestoptimizationmode "enum class in com.here.sdk.routing"). The starting and destination [`Waypoint`](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing") are not reordered. If the whole number of waypoints is fewer than 4 - the flag doesn't affect the resulting route (nothing to optimize). The resulting order of waypoints can be identified by their waypoint indices in the route sections (see [`Route.getSections()`](sdk-for-android-explore-api-reference-latestroute#getSections()), [`Section.getDeparturePlace()`](sdk-for-android-explore-api-reference-latestsection#getDeparturePlace()), [`Section.getArrivalPlace()`](sdk-for-android-explore-api-reference-latestsection#getArrivalPlace()), [`RoutePlace.waypointIndex`](sdk-for-android-explore-api-reference-latestrouteplace#waypointIndex)). Currently, the waypoints order optimization is available only when using the `OfflineRoutingEngine` (only available for the Navigate license). Defaults to `false`.

### enableRouteLabels

public boolean enableRouteLabels

    Specifies whether route labels should be included in the route response. Route labels identify major highways or road names along the route. By default, this is set to `false`.

## Constructor Details

  - ()" class="section detail">

### RouteOptions

public RouteOptions()

    Creates a new instance.

  - (com.here.sdk.routing.OptimizationMode)" class="section detail">

### RouteOptions

public RouteOptions(@NonNull [OptimizationMode](sdk-for-android-explore-api-reference-latestoptimizationmode "enum class in com.here.sdk.routing") optimizationMode)

    Creates a new instance.
Parameters:
    `optimizationMode` -

    The optimization mode to be used for route calculation. By default, it is [`OptimizationMode.FASTEST`](sdk-for-android-explore-api-reference-latestoptimizationmode#FASTEST).
- (com.here.sdk.routing.OptimizationMode,int)" class="section detail">

### RouteOptions

public RouteOptions(@NonNull [OptimizationMode](sdk-for-android-explore-api-reference-latestoptimizationmode "enum class in com.here.sdk.routing") optimizationMode, int alternatives)

    Creates a new instance.
Parameters:
    `optimizationMode` -

    The optimization mode to be used for route calculation. By default, it is [`OptimizationMode.FASTEST`](sdk-for-android-explore-api-reference-latestoptimizationmode#FASTEST).

    `alternatives` -

    Maximum number of alternative routes that will be calculated, in addition to the best one. The provided value must be in the range \[0, 6\]. Alternative routes can be unavailable, thus they are not guaranteed to be returned. The order of routes is from the best to the worst, as evaluated by the route calculation algorithm and according to the given input parameters. Defaults to 0, which means there are no alternatives, i.e. only the best route is returned. Must be 0 for isoline calculation.
- (com.here.sdk.routing.OptimizationMode,int,java.util.Date)" class="section detail">

### RouteOptions

public RouteOptions(@NonNull [OptimizationMode](sdk-for-android-explore-api-reference-latestoptimizationmode "enum class in com.here.sdk.routing") optimizationMode, int alternatives, @Nullable [Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html) departureTime)

    Creates a new instance.
Parameters:
    `optimizationMode` -

    The optimization mode to be used for route calculation. By default, it is [`OptimizationMode.FASTEST`](sdk-for-android-explore-api-reference-latestoptimizationmode#FASTEST).

    `alternatives` -

    Maximum number of alternative routes that will be calculated, in addition to the best one. The provided value must be in the range \[0, 6\]. Alternative routes can be unavailable, thus they are not guaranteed to be returned. The order of routes is from the best to the worst, as evaluated by the route calculation algorithm and according to the given input parameters. Defaults to 0, which means there are no alternatives, i.e. only the best route is returned. Must be 0 for isoline calculation.

    `departureTime` -

    Optional time when travel is expected to start. Traffic speed and incidents shall be taken into account in the calculation of the route, per [`trafficOptimizationMode`](#trafficOptimizationMode). By default, the time is not set. If the time is not set, the current time will be used internally, i.e. now. Therefore, by default, a time-aware route request is initiated including traffic.

    **Note**:

    - Both departure time and [`arrivalTime`](#arrivalTime) cannot be set at the same time.
    - This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00
- (com.here.sdk.routing.OptimizationMode,int,java.util.Date,java.util.Date)" class="section detail">

### RouteOptions

public RouteOptions(@NonNull [OptimizationMode](sdk-for-android-explore-api-reference-latestoptimizationmode "enum class in com.here.sdk.routing") optimizationMode, int alternatives, @Nullable [Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html) departureTime, @Nullable [Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html) arrivalTime)

    Creates a new instance.
Parameters:
    `optimizationMode` -

    The optimization mode to be used for route calculation. By default, it is [`OptimizationMode.FASTEST`](sdk-for-android-explore-api-reference-latestoptimizationmode#FASTEST).

    `alternatives` -

    Maximum number of alternative routes that will be calculated, in addition to the best one. The provided value must be in the range \[0, 6\]. Alternative routes can be unavailable, thus they are not guaranteed to be returned. The order of routes is from the best to the worst, as evaluated by the route calculation algorithm and according to the given input parameters. Defaults to 0, which means there are no alternatives, i.e. only the best route is returned. Must be 0 for isoline calculation.

    `departureTime` -

    Optional time when travel is expected to start. Traffic speed and incidents shall be taken into account in the calculation of the route, per [`trafficOptimizationMode`](#trafficOptimizationMode). By default, the time is not set. If the time is not set, the current time will be used internally, i.e. now. Therefore, by default, a time-aware route request is initiated including traffic.

    **Note**:

    - Both departure time and [`arrivalTime`](#arrivalTime) cannot be set at the same time.
    - This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00

    `arrivalTime` -

    Optional time when travel is expected to end. Traffic speed and incidents shall be taken into account in the calculation of the route, per [`trafficOptimizationMode`](#trafficOptimizationMode). By default, the time is not set. If the time is not set, the current time will be used internally, to predict the arrival time. Therefore, by default, a time-aware route request is initiated including traffic.

    **Note**:

    - Both [`departureTime`](#departureTime) and arrival time cannot be set at the same time.
    - This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00
- (com.here.sdk.routing.OptimizationMode,int,java.util.Date,java.util.Date,java.lang.Double)" class="section detail">

### RouteOptions

public RouteOptions(@NonNull [OptimizationMode](sdk-for-android-explore-api-reference-latestoptimizationmode "enum class in com.here.sdk.routing") optimizationMode, int alternatives, @Nullable [Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html) departureTime, @Nullable [Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html) arrivalTime, @Nullable [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) speedCapInMetersPerSecond)

    Creates a new instance.
Parameters:
    `optimizationMode` -

    The optimization mode to be used for route calculation. By default, it is [`OptimizationMode.FASTEST`](sdk-for-android-explore-api-reference-latestoptimizationmode#FASTEST).

    `alternatives` -

    Maximum number of alternative routes that will be calculated, in addition to the best one. The provided value must be in the range \[0, 6\]. Alternative routes can be unavailable, thus they are not guaranteed to be returned. The order of routes is from the best to the worst, as evaluated by the route calculation algorithm and according to the given input parameters. Defaults to 0, which means there are no alternatives, i.e. only the best route is returned. Must be 0 for isoline calculation.

    `departureTime` -

    Optional time when travel is expected to start. Traffic speed and incidents shall be taken into account in the calculation of the route, per [`trafficOptimizationMode`](#trafficOptimizationMode). By default, the time is not set. If the time is not set, the current time will be used internally, i.e. now. Therefore, by default, a time-aware route request is initiated including traffic.

    **Note**:

    - Both departure time and [`arrivalTime`](#arrivalTime) cannot be set at the same time.
    - This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00

    `arrivalTime` -

    Optional time when travel is expected to end. Traffic speed and incidents shall be taken into account in the calculation of the route, per [`trafficOptimizationMode`](#trafficOptimizationMode). By default, the time is not set. If the time is not set, the current time will be used internally, to predict the arrival time. Therefore, by default, a time-aware route request is initiated including traffic.

    **Note**:

    - Both [`departureTime`](#departureTime) and arrival time cannot be set at the same time.
    - This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00

    `speedCapInMetersPerSecond` -

    Specifies the maximum speed in meters per second, which the user wishes not to exceed. The valid range is \[1, 70\] meters per second. Note that it is valid only for [`TransportMode.CAR`](sdk-for-android-explore-api-reference-latesttransportmode#CAR), [`TransportMode.TRUCK`](sdk-for-android-explore-api-reference-latesttransportmode#TRUCK) and [`TransportMode.SCOOTER`](sdk-for-android-explore-api-reference-latesttransportmode#SCOOTER) transport modes. For car, truck and scooter transport modes, it will affect [`Route.getDuration()`](sdk-for-android-explore-api-reference-latestroute#getDuration()) of the route. Only for scooter transport mode, it may affect the route geometry. Defaults to `null`, which means that no speed cap is set.
- (com.here.sdk.routing.OptimizationMode,int,java.util.Date,java.util.Date,java.lang.Double,boolean)" class="section detail">

### RouteOptions

public RouteOptions(@NonNull [OptimizationMode](sdk-for-android-explore-api-reference-latestoptimizationmode "enum class in com.here.sdk.routing") optimizationMode, int alternatives, @Nullable [Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html) departureTime, @Nullable [Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html) arrivalTime, @Nullable [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) speedCapInMetersPerSecond, boolean enableRouteHandle)

    Creates a new instance.
Parameters:
    `optimizationMode` -

    The optimization mode to be used for route calculation. By default, it is [`OptimizationMode.FASTEST`](sdk-for-android-explore-api-reference-latestoptimizationmode#FASTEST).

    `alternatives` -

    Maximum number of alternative routes that will be calculated, in addition to the best one. The provided value must be in the range \[0, 6\]. Alternative routes can be unavailable, thus they are not guaranteed to be returned. The order of routes is from the best to the worst, as evaluated by the route calculation algorithm and according to the given input parameters. Defaults to 0, which means there are no alternatives, i.e. only the best route is returned. Must be 0 for isoline calculation.

    `departureTime` -

    Optional time when travel is expected to start. Traffic speed and incidents shall be taken into account in the calculation of the route, per [`trafficOptimizationMode`](#trafficOptimizationMode). By default, the time is not set. If the time is not set, the current time will be used internally, i.e. now. Therefore, by default, a time-aware route request is initiated including traffic.

    **Note**:

    - Both departure time and [`arrivalTime`](#arrivalTime) cannot be set at the same time.
    - This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00

    `arrivalTime` -

    Optional time when travel is expected to end. Traffic speed and incidents shall be taken into account in the calculation of the route, per [`trafficOptimizationMode`](#trafficOptimizationMode). By default, the time is not set. If the time is not set, the current time will be used internally, to predict the arrival time. Therefore, by default, a time-aware route request is initiated including traffic.

    **Note**:

    - Both [`departureTime`](#departureTime) and arrival time cannot be set at the same time.
    - This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00

    `speedCapInMetersPerSecond` -

    Specifies the maximum speed in meters per second, which the user wishes not to exceed. The valid range is \[1, 70\] meters per second. Note that it is valid only for [`TransportMode.CAR`](sdk-for-android-explore-api-reference-latesttransportmode#CAR), [`TransportMode.TRUCK`](sdk-for-android-explore-api-reference-latesttransportmode#TRUCK) and [`TransportMode.SCOOTER`](sdk-for-android-explore-api-reference-latesttransportmode#SCOOTER) transport modes. For car, truck and scooter transport modes, it will affect [`Route.getDuration()`](sdk-for-android-explore-api-reference-latestroute#getDuration()) of the route. Only for scooter transport mode, it may affect the route geometry. Defaults to `null`, which means that no speed cap is set.

    `enableRouteHandle` -

    A flag that indicates whether the resulting route should contain a [`RouteHandle`](sdk-for-android-explore-api-reference-latestroutehandle "class in com.here.sdk.routing"). Defaults to `false`. Note that a `RouteHandle` generated by the online `RoutingEngine` is not compatible with the `OfflineRoutingEngine` and vice versa.
- (com.here.sdk.routing.OptimizationMode,int,java.util.Date,java.util.Date,java.lang.Double,boolean,com.here.sdk.routing.TrafficOptimizationMode)" class="section detail">

### RouteOptions

public RouteOptions(@NonNull [OptimizationMode](sdk-for-android-explore-api-reference-latestoptimizationmode "enum class in com.here.sdk.routing") optimizationMode, int alternatives, @Nullable [Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html) departureTime, @Nullable [Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html) arrivalTime, @Nullable [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) speedCapInMetersPerSecond, boolean enableRouteHandle, @NonNull [TrafficOptimizationMode](sdk-for-android-explore-api-reference-latesttrafficoptimizationmode "enum class in com.here.sdk.routing") trafficOptimizationMode)

    Creates a new instance.
Parameters:
    `optimizationMode` -

    The optimization mode to be used for route calculation. By default, it is [`OptimizationMode.FASTEST`](sdk-for-android-explore-api-reference-latestoptimizationmode#FASTEST).

    `alternatives` -

    Maximum number of alternative routes that will be calculated, in addition to the best one. The provided value must be in the range \[0, 6\]. Alternative routes can be unavailable, thus they are not guaranteed to be returned. The order of routes is from the best to the worst, as evaluated by the route calculation algorithm and according to the given input parameters. Defaults to 0, which means there are no alternatives, i.e. only the best route is returned. Must be 0 for isoline calculation.

    `departureTime` -

    Optional time when travel is expected to start. Traffic speed and incidents shall be taken into account in the calculation of the route, per [`trafficOptimizationMode`](#trafficOptimizationMode). By default, the time is not set. If the time is not set, the current time will be used internally, i.e. now. Therefore, by default, a time-aware route request is initiated including traffic.

    **Note**:

    - Both departure time and [`arrivalTime`](#arrivalTime) cannot be set at the same time.
    - This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00

    `arrivalTime` -

    Optional time when travel is expected to end. Traffic speed and incidents shall be taken into account in the calculation of the route, per [`trafficOptimizationMode`](#trafficOptimizationMode). By default, the time is not set. If the time is not set, the current time will be used internally, to predict the arrival time. Therefore, by default, a time-aware route request is initiated including traffic.

    **Note**:

    - Both [`departureTime`](#departureTime) and arrival time cannot be set at the same time.
    - This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00

    `speedCapInMetersPerSecond` -

    Specifies the maximum speed in meters per second, which the user wishes not to exceed. The valid range is \[1, 70\] meters per second. Note that it is valid only for [`TransportMode.CAR`](sdk-for-android-explore-api-reference-latesttransportmode#CAR), [`TransportMode.TRUCK`](sdk-for-android-explore-api-reference-latesttransportmode#TRUCK) and [`TransportMode.SCOOTER`](sdk-for-android-explore-api-reference-latesttransportmode#SCOOTER) transport modes. For car, truck and scooter transport modes, it will affect [`Route.getDuration()`](sdk-for-android-explore-api-reference-latestroute#getDuration()) of the route. Only for scooter transport mode, it may affect the route geometry. Defaults to `null`, which means that no speed cap is set.

    `enableRouteHandle` -

    A flag that indicates whether the resulting route should contain a [`RouteHandle`](sdk-for-android-explore-api-reference-latestroutehandle "class in com.here.sdk.routing"). Defaults to `false`. Note that a `RouteHandle` generated by the online `RoutingEngine` is not compatible with the `OfflineRoutingEngine` and vice versa.

    `trafficOptimizationMode` -

    The traffic optimization mode to be used for route calculation. By default, it is [`TrafficOptimizationMode.TIME_DEPENDENT`](sdk-for-android-explore-api-reference-latesttrafficoptimizationmode#TIME_DEPENDENT), which enables traffic-aware routing.
- (com.here.sdk.routing.OptimizationMode,int,java.util.Date,java.util.Date,java.lang.Double,boolean,com.here.sdk.routing.TrafficOptimizationMode,boolean)" class="section detail">

### RouteOptions

public RouteOptions(@NonNull [OptimizationMode](sdk-for-android-explore-api-reference-latestoptimizationmode "enum class in com.here.sdk.routing") optimizationMode, int alternatives, @Nullable [Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html) departureTime, @Nullable [Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html) arrivalTime, @Nullable [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) speedCapInMetersPerSecond, boolean enableRouteHandle, @NonNull [TrafficOptimizationMode](sdk-for-android-explore-api-reference-latesttrafficoptimizationmode "enum class in com.here.sdk.routing") trafficOptimizationMode, boolean enableTolls)

    Creates a new instance.
Parameters:
    `optimizationMode` -

    The optimization mode to be used for route calculation. By default, it is [`OptimizationMode.FASTEST`](sdk-for-android-explore-api-reference-latestoptimizationmode#FASTEST).

    `alternatives` -

    Maximum number of alternative routes that will be calculated, in addition to the best one. The provided value must be in the range \[0, 6\]. Alternative routes can be unavailable, thus they are not guaranteed to be returned. The order of routes is from the best to the worst, as evaluated by the route calculation algorithm and according to the given input parameters. Defaults to 0, which means there are no alternatives, i.e. only the best route is returned. Must be 0 for isoline calculation.

    `departureTime` -

    Optional time when travel is expected to start. Traffic speed and incidents shall be taken into account in the calculation of the route, per [`trafficOptimizationMode`](#trafficOptimizationMode). By default, the time is not set. If the time is not set, the current time will be used internally, i.e. now. Therefore, by default, a time-aware route request is initiated including traffic.

    **Note**:

    - Both departure time and [`arrivalTime`](#arrivalTime) cannot be set at the same time.
    - This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00

    `arrivalTime` -

    Optional time when travel is expected to end. Traffic speed and incidents shall be taken into account in the calculation of the route, per [`trafficOptimizationMode`](#trafficOptimizationMode). By default, the time is not set. If the time is not set, the current time will be used internally, to predict the arrival time. Therefore, by default, a time-aware route request is initiated including traffic.

    **Note**:

    - Both [`departureTime`](#departureTime) and arrival time cannot be set at the same time.
    - This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00

    `speedCapInMetersPerSecond` -

    Specifies the maximum speed in meters per second, which the user wishes not to exceed. The valid range is \[1, 70\] meters per second. Note that it is valid only for [`TransportMode.CAR`](sdk-for-android-explore-api-reference-latesttransportmode#CAR), [`TransportMode.TRUCK`](sdk-for-android-explore-api-reference-latesttransportmode#TRUCK) and [`TransportMode.SCOOTER`](sdk-for-android-explore-api-reference-latesttransportmode#SCOOTER) transport modes. For car, truck and scooter transport modes, it will affect [`Route.getDuration()`](sdk-for-android-explore-api-reference-latestroute#getDuration()) of the route. Only for scooter transport mode, it may affect the route geometry. Defaults to `null`, which means that no speed cap is set.

    `enableRouteHandle` -

    A flag that indicates whether the resulting route should contain a [`RouteHandle`](sdk-for-android-explore-api-reference-latestroutehandle "class in com.here.sdk.routing"). Defaults to `false`. Note that a `RouteHandle` generated by the online `RoutingEngine` is not compatible with the `OfflineRoutingEngine` and vice versa.

    `trafficOptimizationMode` -

    The traffic optimization mode to be used for route calculation. By default, it is [`TrafficOptimizationMode.TIME_DEPENDENT`](sdk-for-android-explore-api-reference-latesttrafficoptimizationmode#TIME_DEPENDENT), which enables traffic-aware routing.

    `enableTolls` -

    A flag that indicates whether the resulting route [`Section.getTolls()`](sdk-for-android-explore-api-reference-latestsection#getTolls()) properties should contain tolls data. Defaults to `false`.

    **Note:** When a route calculation request asks tolls, a pricing scheme with higher rates might be applied. Consult your HERE representative to get more information on the related pricing schemes.

    **Note:** For users of the `OfflineRoutingEngine` this is a beta release of this feature, so there could be a few bugs and unexpected behaviors. The `OfflineRoutingEngine` is only available for the Navigate license. For users of the `RoutingEngine` the feature is stable.
- (com.here.sdk.routing.OptimizationMode,int,java.util.Date,java.util.Date,java.lang.Double,boolean,com.here.sdk.routing.TrafficOptimizationMode,boolean,boolean)" class="section detail">

### RouteOptions

public RouteOptions(@NonNull [OptimizationMode](sdk-for-android-explore-api-reference-latestoptimizationmode "enum class in com.here.sdk.routing") optimizationMode, int alternatives, @Nullable [Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html) departureTime, @Nullable [Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html) arrivalTime, @Nullable [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) speedCapInMetersPerSecond, boolean enableRouteHandle, @NonNull [TrafficOptimizationMode](sdk-for-android-explore-api-reference-latesttrafficoptimizationmode "enum class in com.here.sdk.routing") trafficOptimizationMode, boolean enableTolls, boolean optimizeWaypointsOrder)

    Creates a new instance.
Parameters:
    `optimizationMode` -

    The optimization mode to be used for route calculation. By default, it is [`OptimizationMode.FASTEST`](sdk-for-android-explore-api-reference-latestoptimizationmode#FASTEST).

    `alternatives` -

    Maximum number of alternative routes that will be calculated, in addition to the best one. The provided value must be in the range \[0, 6\]. Alternative routes can be unavailable, thus they are not guaranteed to be returned. The order of routes is from the best to the worst, as evaluated by the route calculation algorithm and according to the given input parameters. Defaults to 0, which means there are no alternatives, i.e. only the best route is returned. Must be 0 for isoline calculation.

    `departureTime` -

    Optional time when travel is expected to start. Traffic speed and incidents shall be taken into account in the calculation of the route, per [`trafficOptimizationMode`](#trafficOptimizationMode). By default, the time is not set. If the time is not set, the current time will be used internally, i.e. now. Therefore, by default, a time-aware route request is initiated including traffic.

    **Note**:

    - Both departure time and [`arrivalTime`](#arrivalTime) cannot be set at the same time.
    - This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00

    `arrivalTime` -

    Optional time when travel is expected to end. Traffic speed and incidents shall be taken into account in the calculation of the route, per [`trafficOptimizationMode`](#trafficOptimizationMode). By default, the time is not set. If the time is not set, the current time will be used internally, to predict the arrival time. Therefore, by default, a time-aware route request is initiated including traffic.

    **Note**:

    - Both [`departureTime`](#departureTime) and arrival time cannot be set at the same time.
    - This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00

    `speedCapInMetersPerSecond` -

    Specifies the maximum speed in meters per second, which the user wishes not to exceed. The valid range is \[1, 70\] meters per second. Note that it is valid only for [`TransportMode.CAR`](sdk-for-android-explore-api-reference-latesttransportmode#CAR), [`TransportMode.TRUCK`](sdk-for-android-explore-api-reference-latesttransportmode#TRUCK) and [`TransportMode.SCOOTER`](sdk-for-android-explore-api-reference-latesttransportmode#SCOOTER) transport modes. For car, truck and scooter transport modes, it will affect [`Route.getDuration()`](sdk-for-android-explore-api-reference-latestroute#getDuration()) of the route. Only for scooter transport mode, it may affect the route geometry. Defaults to `null`, which means that no speed cap is set.

    `enableRouteHandle` -

    A flag that indicates whether the resulting route should contain a [`RouteHandle`](sdk-for-android-explore-api-reference-latestroutehandle "class in com.here.sdk.routing"). Defaults to `false`. Note that a `RouteHandle` generated by the online `RoutingEngine` is not compatible with the `OfflineRoutingEngine` and vice versa.

    `trafficOptimizationMode` -

    The traffic optimization mode to be used for route calculation. By default, it is [`TrafficOptimizationMode.TIME_DEPENDENT`](sdk-for-android-explore-api-reference-latesttrafficoptimizationmode#TIME_DEPENDENT), which enables traffic-aware routing.

    `enableTolls` -

    A flag that indicates whether the resulting route [`Section.getTolls()`](sdk-for-android-explore-api-reference-latestsection#getTolls()) properties should contain tolls data. Defaults to `false`.

    **Note:** When a route calculation request asks tolls, a pricing scheme with higher rates might be applied. Consult your HERE representative to get more information on the related pricing schemes.

    **Note:** For users of the `OfflineRoutingEngine` this is a beta release of this feature, so there could be a few bugs and unexpected behaviors. The `OfflineRoutingEngine` is only available for the Navigate license. For users of the `RoutingEngine` the feature is stable.

    `optimizeWaypointsOrder` -

    A flag that indicates whether the order of waypoints that is passed to `calculateRoute()` should be optimized in the best order. The best order is calculated by the same metrics that are used during regular calculation, e.g. [`OptimizationMode`](sdk-for-android-explore-api-reference-latestoptimizationmode "enum class in com.here.sdk.routing"). The starting and destination [`Waypoint`](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing") are not reordered. If the whole number of waypoints is fewer than 4 - the flag doesn't affect the resulting route (nothing to optimize). The resulting order of waypoints can be identified by their waypoint indices in the route sections (see [`Route.getSections()`](sdk-for-android-explore-api-reference-latestroute#getSections()), [`Section.getDeparturePlace()`](sdk-for-android-explore-api-reference-latestsection#getDeparturePlace()), [`Section.getArrivalPlace()`](sdk-for-android-explore-api-reference-latestsection#getArrivalPlace()), [`RoutePlace.waypointIndex`](sdk-for-android-explore-api-reference-latestrouteplace#waypointIndex)). Currently, the waypoints order optimization is available only when using the `OfflineRoutingEngine` (only available for the Navigate license). Defaults to `false`.
- (com.here.sdk.routing.OptimizationMode,int,java.util.Date,java.util.Date,java.lang.Double,boolean,com.here.sdk.routing.TrafficOptimizationMode,boolean,boolean,boolean)" class="section detail">

### RouteOptions

public RouteOptions(@NonNull [OptimizationMode](sdk-for-android-explore-api-reference-latestoptimizationmode "enum class in com.here.sdk.routing") optimizationMode, int alternatives, @Nullable [Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html) departureTime, @Nullable [Date](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html) arrivalTime, @Nullable [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) speedCapInMetersPerSecond, boolean enableRouteHandle, @NonNull [TrafficOptimizationMode](sdk-for-android-explore-api-reference-latesttrafficoptimizationmode "enum class in com.here.sdk.routing") trafficOptimizationMode, boolean enableTolls, boolean optimizeWaypointsOrder, boolean enableRouteLabels)

    Creates a new instance.
Parameters:
    `optimizationMode` -

    The optimization mode to be used for route calculation. By default, it is [`OptimizationMode.FASTEST`](sdk-for-android-explore-api-reference-latestoptimizationmode#FASTEST).

    `alternatives` -

    Maximum number of alternative routes that will be calculated, in addition to the best one. The provided value must be in the range \[0, 6\]. Alternative routes can be unavailable, thus they are not guaranteed to be returned. The order of routes is from the best to the worst, as evaluated by the route calculation algorithm and according to the given input parameters. Defaults to 0, which means there are no alternatives, i.e. only the best route is returned. Must be 0 for isoline calculation.

    `departureTime` -

    Optional time when travel is expected to start. Traffic speed and incidents shall be taken into account in the calculation of the route, per [`trafficOptimizationMode`](#trafficOptimizationMode). By default, the time is not set. If the time is not set, the current time will be used internally, i.e. now. Therefore, by default, a time-aware route request is initiated including traffic.

    **Note**:

    - Both departure time and [`arrivalTime`](#arrivalTime) cannot be set at the same time.
    - This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00

    `arrivalTime` -

    Optional time when travel is expected to end. Traffic speed and incidents shall be taken into account in the calculation of the route, per [`trafficOptimizationMode`](#trafficOptimizationMode). By default, the time is not set. If the time is not set, the current time will be used internally, to predict the arrival time. Therefore, by default, a time-aware route request is initiated including traffic.

    **Note**:

    - Both [`departureTime`](#departureTime) and arrival time cannot be set at the same time.
    - This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00

    `speedCapInMetersPerSecond` -

    Specifies the maximum speed in meters per second, which the user wishes not to exceed. The valid range is \[1, 70\] meters per second. Note that it is valid only for [`TransportMode.CAR`](sdk-for-android-explore-api-reference-latesttransportmode#CAR), [`TransportMode.TRUCK`](sdk-for-android-explore-api-reference-latesttransportmode#TRUCK) and [`TransportMode.SCOOTER`](sdk-for-android-explore-api-reference-latesttransportmode#SCOOTER) transport modes. For car, truck and scooter transport modes, it will affect [`Route.getDuration()`](sdk-for-android-explore-api-reference-latestroute#getDuration()) of the route. Only for scooter transport mode, it may affect the route geometry. Defaults to `null`, which means that no speed cap is set.

    `enableRouteHandle` -

    A flag that indicates whether the resulting route should contain a [`RouteHandle`](sdk-for-android-explore-api-reference-latestroutehandle "class in com.here.sdk.routing"). Defaults to `false`. Note that a `RouteHandle` generated by the online `RoutingEngine` is not compatible with the `OfflineRoutingEngine` and vice versa.

    `trafficOptimizationMode` -

    The traffic optimization mode to be used for route calculation. By default, it is [`TrafficOptimizationMode.TIME_DEPENDENT`](sdk-for-android-explore-api-reference-latesttrafficoptimizationmode#TIME_DEPENDENT), which enables traffic-aware routing.

    `enableTolls` -

    A flag that indicates whether the resulting route [`Section.getTolls()`](sdk-for-android-explore-api-reference-latestsection#getTolls()) properties should contain tolls data. Defaults to `false`.

    **Note:** When a route calculation request asks tolls, a pricing scheme with higher rates might be applied. Consult your HERE representative to get more information on the related pricing schemes.

    **Note:** For users of the `OfflineRoutingEngine` this is a beta release of this feature, so there could be a few bugs and unexpected behaviors. The `OfflineRoutingEngine` is only available for the Navigate license. For users of the `RoutingEngine` the feature is stable.

    `optimizeWaypointsOrder` -

    A flag that indicates whether the order of waypoints that is passed to `calculateRoute()` should be optimized in the best order. The best order is calculated by the same metrics that are used during regular calculation, e.g. [`OptimizationMode`](sdk-for-android-explore-api-reference-latestoptimizationmode "enum class in com.here.sdk.routing"). The starting and destination [`Waypoint`](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing") are not reordered. If the whole number of waypoints is fewer than 4 - the flag doesn't affect the resulting route (nothing to optimize). The resulting order of waypoints can be identified by their waypoint indices in the route sections (see [`Route.getSections()`](sdk-for-android-explore-api-reference-latestroute#getSections()), [`Section.getDeparturePlace()`](sdk-for-android-explore-api-reference-latestsection#getDeparturePlace()), [`Section.getArrivalPlace()`](sdk-for-android-explore-api-reference-latestsection#getArrivalPlace()), [`RoutePlace.waypointIndex`](sdk-for-android-explore-api-reference-latestrouteplace#waypointIndex)). Currently, the waypoints order optimization is available only when using the `OfflineRoutingEngine` (only available for the Navigate license). Defaults to `false`.

    `enableRouteLabels` -

    Specifies whether route labels should be included in the route response. Route labels identify major highways or road names along the route. By default, this is set to `false`.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
