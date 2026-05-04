---
title: "RefreshRouteOptions (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestrefreshrouteoptions"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class RefreshRouteOptions

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.routing.RefreshRouteOptions
------------------------------------------------------------------------
[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) public final class RefreshRouteOptions extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Deprecated.
Will be removed in v4.28.0. Use the `RoutingOptions` class instead.
The options to specify how to refresh an already calculated route identified by a [`RouteHandle`](sdk-for-android-explore-api-reference-latestroutehandle "class in com.here.sdk.routing"). All the options that may result in a new route shape are ignored as no new route is calculated. Instead, only the data that accompanies a route, such as traffic information, can be refreshed. Therefore, the following route options are ignored: [`RouteOptions.alternatives`](sdk-for-android-explore-api-reference-latestrouteoptions#alternatives), [`RouteOptions.arrivalTime`](sdk-for-android-explore-api-reference-latestrouteoptions#arrivalTime), and [`RouteOptions.optimizationMode`](sdk-for-android-explore-api-reference-latestrouteoptions#optimizationMode). If new [`AvoidanceOptions`](sdk-for-android-explore-api-reference-latestavoidanceoptions "class in com.here.sdk.routing") are specified, they are ignored as well and instead new [`SectionNotice`](sdk-for-android-explore-api-reference-latestsectionnotice "class in com.here.sdk.routing")'s are generated that indicate where the requested [`AvoidanceOptions`](sdk-for-android-explore-api-reference-latestavoidanceoptions "class in com.here.sdk.routing") are violated. Note that when [`EVCarOptions.ensureReachability`](sdk-for-android-explore-api-reference-latestevcaroptions#ensureReachability) is set to true, the route refresh request will fail as this option is incompatible with a fixed route shape. If any of the ignored options are important, consider calculating a new route instead.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

## Constructor Summary

Constructors

Constructor

  Description

  [RefreshRouteOptions](#%3Cinit%3E(com.here.sdk.routing.BicycleOptions))`(`[`BicycleOptions`](sdk-for-android-explore-api-reference-latestbicycleoptions "class in com.here.sdk.routing")` bicycleOptions)`

Deprecated.

  Constructs a RefreshRouteOptions object with [`BicycleOptions`](sdk-for-android-explore-api-reference-latestbicycleoptions "class in com.here.sdk.routing").

[RefreshRouteOptions](#%3Cinit%3E(com.here.sdk.routing.BusOptions))`(`[`BusOptions`](sdk-for-android-explore-api-reference-latestbusoptions "class in com.here.sdk.routing")` busOptions)`

Deprecated.

  Constructs a RefreshRouteOptions object with [`BusOptions`](sdk-for-android-explore-api-reference-latestbusoptions "class in com.here.sdk.routing").

[RefreshRouteOptions](#%3Cinit%3E(com.here.sdk.routing.CarOptions))`(`[`CarOptions`](sdk-for-android-explore-api-reference-latestcaroptions "class in com.here.sdk.routing")` carOptions)`

Deprecated.

  Constructs a RefreshRouteOptions object with [`CarOptions`](sdk-for-android-explore-api-reference-latestcaroptions "class in com.here.sdk.routing").

[RefreshRouteOptions](#%3Cinit%3E(com.here.sdk.routing.EVCarOptions))`(`[`EVCarOptions`](sdk-for-android-explore-api-reference-latestevcaroptions "class in com.here.sdk.routing")` evCarOptions)`

Deprecated.

  Constructs a RefreshRouteOptions object with [`EVCarOptions`](sdk-for-android-explore-api-reference-latestevcaroptions "class in com.here.sdk.routing").

[RefreshRouteOptions](#%3Cinit%3E(com.here.sdk.routing.EVTruckOptions))`(`[`EVTruckOptions`](sdk-for-android-explore-api-reference-latestevtruckoptions "class in com.here.sdk.routing")` evTruckOptions)`

Deprecated.

  Constructs a RefreshRouteOptions object with [`EVTruckOptions`](sdk-for-android-explore-api-reference-latestevtruckoptions "class in com.here.sdk.routing").

[RefreshRouteOptions](#%3Cinit%3E(com.here.sdk.routing.PedestrianOptions))`(`[`PedestrianOptions`](sdk-for-android-explore-api-reference-latestpedestrianoptions "class in com.here.sdk.routing")` pedestrianOptions)`

Deprecated.

  Constructs a RefreshRouteOptions object with [`PedestrianOptions`](sdk-for-android-explore-api-reference-latestpedestrianoptions "class in com.here.sdk.routing").

[RefreshRouteOptions](#%3Cinit%3E(com.here.sdk.routing.PrivateBusOptions))`(`[`PrivateBusOptions`](sdk-for-android-explore-api-reference-latestprivatebusoptions "class in com.here.sdk.routing")` privateBusOptions)`

Deprecated.

  Constructs a RefreshRouteOptions object with [`PrivateBusOptions`](sdk-for-android-explore-api-reference-latestprivatebusoptions "class in com.here.sdk.routing").

[RefreshRouteOptions](#%3Cinit%3E(com.here.sdk.routing.ScooterOptions))`(`[`ScooterOptions`](sdk-for-android-explore-api-reference-latestscooteroptions "class in com.here.sdk.routing")` scooterOptions)`

Deprecated.

  Constructs a RefreshRouteOptions object with [`ScooterOptions`](sdk-for-android-explore-api-reference-latestscooteroptions "class in com.here.sdk.routing").

[RefreshRouteOptions](#%3Cinit%3E(com.here.sdk.routing.TaxiOptions))`(`[`TaxiOptions`](sdk-for-android-explore-api-reference-latesttaxioptions "class in com.here.sdk.routing")` taxiOptions)`

Deprecated.

  Constructs a RefreshRouteOptions object with [`TaxiOptions`](sdk-for-android-explore-api-reference-latesttaxioptions "class in com.here.sdk.routing").

[RefreshRouteOptions](#%3Cinit%3E(com.here.sdk.routing.TruckOptions))`(`[`TruckOptions`](sdk-for-android-explore-api-reference-latesttruckoptions "class in com.here.sdk.routing")` truckOptions)`

Deprecated.

  Constructs a RefreshRouteOptions object with [`TruckOptions`](sdk-for-android-explore-api-reference-latesttruckoptions "class in com.here.sdk.routing").

[RefreshRouteOptions](#%3Cinit%3E(com.here.sdk.transport.TransportMode))`(`[`TransportMode`](sdk-for-android-explore-api-reference-latesttransportmode "enum class in com.here.sdk.transport")` transportMode)`

Deprecated.

  Constructs a RefreshRouteOptions object with [`TransportMode`](sdk-for-android-explore-api-reference-latesttransportmode "enum class in com.here.sdk.transport").

## Method Summary

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - (com.here.sdk.transport.TransportMode)" class="section detail">

### RefreshRouteOptions

public RefreshRouteOptions(@NonNull [TransportMode](sdk-for-android-explore-api-reference-latesttransportmode "enum class in com.here.sdk.transport") transportMode)

    Deprecated.

    Constructs a RefreshRouteOptions object with [`TransportMode`](sdk-for-android-explore-api-reference-latesttransportmode "enum class in com.here.sdk.transport").
Parameters:
    `transportMode` -

    Updates the transport mode for the route.
- (com.here.sdk.routing.CarOptions)" class="section detail">

### RefreshRouteOptions

public RefreshRouteOptions(@NonNull [CarOptions](sdk-for-android-explore-api-reference-latestcaroptions "class in com.here.sdk.routing") carOptions)

    Deprecated.

    Constructs a RefreshRouteOptions object with [`CarOptions`](sdk-for-android-explore-api-reference-latestcaroptions "class in com.here.sdk.routing").
Parameters:
    `carOptions` -

    Converts the route to a car route, if a different transport mode was used for the [`RouteHandle`](sdk-for-android-explore-api-reference-latestroutehandle "class in com.here.sdk.routing"). Note that in case this is not possible, an [`RoutingError.NO_ROUTE_FOUND`](sdk-for-android-explore-api-reference-latestroutingerror#NO_ROUTE_FOUND) error will be triggered.
- (com.here.sdk.routing.TruckOptions)" class="section detail">

### RefreshRouteOptions

public RefreshRouteOptions(@NonNull [TruckOptions](sdk-for-android-explore-api-reference-latesttruckoptions "class in com.here.sdk.routing") truckOptions)

    Deprecated.

    Constructs a RefreshRouteOptions object with [`TruckOptions`](sdk-for-android-explore-api-reference-latesttruckoptions "class in com.here.sdk.routing").
Parameters:
    `truckOptions` -

    Converts the route to a truck route, if a different transport mode was used for the [`RouteHandle`](sdk-for-android-explore-api-reference-latestroutehandle "class in com.here.sdk.routing"). Note that in case this is not possible, an [`RoutingError.NO_ROUTE_FOUND`](sdk-for-android-explore-api-reference-latestroutingerror#NO_ROUTE_FOUND) error will be triggered.
- (com.here.sdk.routing.PedestrianOptions)" class="section detail">

### RefreshRouteOptions

public RefreshRouteOptions(@NonNull [PedestrianOptions](sdk-for-android-explore-api-reference-latestpedestrianoptions "class in com.here.sdk.routing") pedestrianOptions)

    Deprecated.

    Constructs a RefreshRouteOptions object with [`PedestrianOptions`](sdk-for-android-explore-api-reference-latestpedestrianoptions "class in com.here.sdk.routing").
Parameters:
    `pedestrianOptions` -

    Converts the route to a pedestrian route, if a different transport mode was used for the [`RouteHandle`](sdk-for-android-explore-api-reference-latestroutehandle "class in com.here.sdk.routing"). Note that in case this is not possible, an [`RoutingError.NO_ROUTE_FOUND`](sdk-for-android-explore-api-reference-latestroutingerror#NO_ROUTE_FOUND) error will be triggered.
- (com.here.sdk.routing.ScooterOptions)" class="section detail">

### RefreshRouteOptions

public RefreshRouteOptions(@NonNull [ScooterOptions](sdk-for-android-explore-api-reference-latestscooteroptions "class in com.here.sdk.routing") scooterOptions)

    Deprecated.

    Constructs a RefreshRouteOptions object with [`ScooterOptions`](sdk-for-android-explore-api-reference-latestscooteroptions "class in com.here.sdk.routing").
Parameters:
    `scooterOptions` -

    Converts the route to a scooter route, if a different transport mode was used for the [`RouteHandle`](sdk-for-android-explore-api-reference-latestroutehandle "class in com.here.sdk.routing"). Note that in case this is not possible, an [`RoutingError.NO_ROUTE_FOUND`](sdk-for-android-explore-api-reference-latestroutingerror#NO_ROUTE_FOUND) error will be triggered.
- (com.here.sdk.routing.TaxiOptions)" class="section detail">

### RefreshRouteOptions

public RefreshRouteOptions(@NonNull [TaxiOptions](sdk-for-android-explore-api-reference-latesttaxioptions "class in com.here.sdk.routing") taxiOptions)

    Deprecated.

    Constructs a RefreshRouteOptions object with [`TaxiOptions`](sdk-for-android-explore-api-reference-latesttaxioptions "class in com.here.sdk.routing").
Parameters:
    `taxiOptions` -

    Converts the route to a taxi route, if a different transport mode was used for the [`RouteHandle`](sdk-for-android-explore-api-reference-latestroutehandle "class in com.here.sdk.routing"). Note that in case this is not possible, an [`RoutingError.NO_ROUTE_FOUND`](sdk-for-android-explore-api-reference-latestroutingerror#NO_ROUTE_FOUND) error will be triggered.
- (com.here.sdk.routing.EVCarOptions)" class="section detail">

### RefreshRouteOptions

public RefreshRouteOptions(@NonNull [EVCarOptions](sdk-for-android-explore-api-reference-latestevcaroptions "class in com.here.sdk.routing") evCarOptions)

    Deprecated.

    Constructs a RefreshRouteOptions object with [`EVCarOptions`](sdk-for-android-explore-api-reference-latestevcaroptions "class in com.here.sdk.routing").
Parameters:
    `evCarOptions` -

    Converts the route to an electric car route, if a different transport mode was used for the [`RouteHandle`](sdk-for-android-explore-api-reference-latestroutehandle "class in com.here.sdk.routing"). Note that in case this is not possible, an [`RoutingError.NO_ROUTE_FOUND`](sdk-for-android-explore-api-reference-latestroutingerror#NO_ROUTE_FOUND) error will be triggered.
- (com.here.sdk.routing.EVTruckOptions)" class="section detail">

### RefreshRouteOptions

public RefreshRouteOptions(@NonNull [EVTruckOptions](sdk-for-android-explore-api-reference-latestevtruckoptions "class in com.here.sdk.routing") evTruckOptions)

    Deprecated.

    Constructs a RefreshRouteOptions object with [`EVTruckOptions`](sdk-for-android-explore-api-reference-latestevtruckoptions "class in com.here.sdk.routing").
Parameters:
    `evTruckOptions` -

    Converts the route to an electric truck route, if a different transport mode was used for the [`RouteHandle`](sdk-for-android-explore-api-reference-latestroutehandle "class in com.here.sdk.routing"). Note that in case this is not possible, an [`RoutingError.NO_ROUTE_FOUND`](sdk-for-android-explore-api-reference-latestroutingerror#NO_ROUTE_FOUND) error will be triggered.
- (com.here.sdk.routing.BicycleOptions)" class="section detail">

### RefreshRouteOptions

public RefreshRouteOptions(@NonNull [BicycleOptions](sdk-for-android-explore-api-reference-latestbicycleoptions "class in com.here.sdk.routing") bicycleOptions)

    Deprecated.

    Constructs a RefreshRouteOptions object with [`BicycleOptions`](sdk-for-android-explore-api-reference-latestbicycleoptions "class in com.here.sdk.routing").
Parameters:
    `bicycleOptions` -

    Converts the route to a bicycle route, if a different transport mode was used for the [`RouteHandle`](sdk-for-android-explore-api-reference-latestroutehandle "class in com.here.sdk.routing"). Note that in case this is not possible, an [`RoutingError.NO_ROUTE_FOUND`](sdk-for-android-explore-api-reference-latestroutingerror#NO_ROUTE_FOUND) error will be triggered.
- (com.here.sdk.routing.BusOptions)" class="section detail">

### RefreshRouteOptions

public RefreshRouteOptions(@NonNull [BusOptions](sdk-for-android-explore-api-reference-latestbusoptions "class in com.here.sdk.routing") busOptions)

    Deprecated.

    Constructs a RefreshRouteOptions object with [`BusOptions`](sdk-for-android-explore-api-reference-latestbusoptions "class in com.here.sdk.routing").
Parameters:
    `busOptions` -

    Converts the route to a bus route, if a different transport mode was used for the [`RouteHandle`](sdk-for-android-explore-api-reference-latestroutehandle "class in com.here.sdk.routing"). Note that in case this is not possible, an [`RoutingError.NO_ROUTE_FOUND`](sdk-for-android-explore-api-reference-latestroutingerror#NO_ROUTE_FOUND) error will be triggered.
- (com.here.sdk.routing.PrivateBusOptions)" class="section detail">

### RefreshRouteOptions

public RefreshRouteOptions(@NonNull [PrivateBusOptions](sdk-for-android-explore-api-reference-latestprivatebusoptions "class in com.here.sdk.routing") privateBusOptions)

    Deprecated.

    Constructs a RefreshRouteOptions object with [`PrivateBusOptions`](sdk-for-android-explore-api-reference-latestprivatebusoptions "class in com.here.sdk.routing").
Parameters:
    `privateBusOptions` -

    Converts the route to a private bus route, if a different transport mode was used for the [`RouteHandle`](sdk-for-android-explore-api-reference-latestroutehandle "class in com.here.sdk.routing"). Note that in case this is not possible, an [`RoutingError.NO_ROUTE_FOUND`](sdk-for-android-explore-api-reference-latestroutingerror#NO_ROUTE_FOUND) error will be triggered.
