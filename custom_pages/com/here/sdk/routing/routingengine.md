---
title: "RoutingEngine (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestroutingengine"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class RoutingEngine

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.routing.RoutingEngine
All Implemented Interfaces:
[`RoutingInterface`](sdk-for-android-explore-api-reference-latestroutinginterface "interface in com.here.sdk.routing")

------------------------------------------------------------------------
public final class RoutingEngine extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here") implements [RoutingInterface](sdk-for-android-explore-api-reference-latestroutinginterface "interface in com.here.sdk.routing")
Use the RoutingEngine to calculate a route from A to B with a number of waypoints in between.

Route calculation is done asynchronously and requires an online connection. The resulting route contains various information such as the polyline, route length in meters, estimated time to traverse along the route and maneuver data.

**Note:** The engine does not support an unlimited number of waypoints. The limit is defined by the HERE backend services and may change. For now, the maximum number of waypoints should be below 200. This value may change and it is not guaranteed to be stable. If you need to support very large lists of waypoints, consider to import a route (see `importRoute()` method) or use the `OfflineRoutingEngine` which supports an unlimited number of waypoints. The `OfflineRoutingEngine` is only available for Navigate licence.

## Constructor Summary

Constructors

Constructor

  Description

  [RoutingEngine](#%3Cinit%3E())`()`

Creates a new instance of this class.

[RoutingEngine](#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine))`(`[`SDKNativeEngine`](sdk-for-android-explore-api-reference-latestsdknativeengine "class in com.here.sdk.core.engine")` sdkEngine)`

Creates a new instance of RoutingEngine.

[RoutingEngine](#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.routing.RoutingConnectionSettings))`(`[`SDKNativeEngine`](sdk-for-android-explore-api-reference-latestsdknativeengine "class in com.here.sdk.core.engine")` sdkEngine, `[`RoutingConnectionSettings`](sdk-for-android-explore-api-reference-latestroutingconnectionsettings "class in com.here.sdk.routing")` connectionSettings)`

Creates a new instance of RoutingEngine.

[RoutingEngine](#%3Cinit%3E(com.here.sdk.routing.RoutingConnectionSettings))`(`[`RoutingConnectionSettings`](sdk-for-android-explore-api-reference-latestroutingconnectionsettings "class in com.here.sdk.routing")` connectionSettings)`

Creates a new instance of RoutingEngine.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods
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

  [`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [calculateTrafficOnRoute](#calculateTrafficOnRoute(com.here.sdk.routing.Route,int,int,double,com.here.sdk.routing.CalculateTrafficOnRouteCallback))`(`[`Route`](sdk-for-android-explore-api-reference-latestroute "class in com.here.sdk.routing")` route, int lastTraveledSectionIndex, int traveledDistanceOnLastSectionInMeters, double currentChargeInKilowattHours, `[`CalculateTrafficOnRouteCallback`](sdk-for-android-explore-api-reference-latestcalculatetrafficonroutecallback "interface in com.here.sdk.routing")` callback)`

Asynchronously calculates the traffic along an EV car route starting from the index of the last traveled route section and an offset in meters from the last visited position on the section.

[`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [calculateTrafficOnRoute](#calculateTrafficOnRoute(com.here.sdk.routing.Route,int,int,com.here.sdk.routing.CalculateTrafficOnRouteCallback))`(`[`Route`](sdk-for-android-explore-api-reference-latestroute "class in com.here.sdk.routing")` route, int lastTraveledSectionIndex, int traveledDistanceOnLastSectionInMeters, `[`CalculateTrafficOnRouteCallback`](sdk-for-android-explore-api-reference-latestcalculatetrafficonroutecallback "interface in com.here.sdk.routing")` callback)`

Asynchronously calculates the traffic along a route starting from the index of the last traveled route section and an offset (in meters) from the last visited position on the section.

`void`

  [dispose](#dispose())`()`

Cancels pending requests and closes the background worker thread.

[`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [importRoute](#importRoute(com.here.sdk.routing.RouteHandle,com.here.sdk.routing.RefreshRouteOptions,com.here.sdk.routing.CalculateRouteCallback))`(`[`RouteHandle`](sdk-for-android-explore-api-reference-latestroutehandle "class in com.here.sdk.routing")` routeHandle, `[`RefreshRouteOptions`](sdk-for-android-explore-api-reference-latestrefreshrouteoptions "class in com.here.sdk.routing")` refreshRouteOptions, `[`CalculateRouteCallback`](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing")` callback)`

Deprecated.
Will be removed in v4.28.0.

  [`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [importRoute](#importRoute(com.here.sdk.routing.RouteHandle,com.here.sdk.routing.RoutingOptions,com.here.sdk.routing.CalculateRouteCallback))`(`[`RouteHandle`](sdk-for-android-explore-api-reference-latestroutehandle "class in com.here.sdk.routing")` routeHandle, `[`RoutingOptions`](sdk-for-android-explore-api-reference-latestroutingoptions "class in com.here.sdk.routing")` options, `[`CalculateRouteCallback`](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing")` callback)`

Asynchronously recreates a route from the [`RouteHandle`](sdk-for-android-explore-api-reference-latestroutehandle "class in com.here.sdk.routing") provided, i.e.

[`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [importRoute](#importRoute(java.util.List,com.here.sdk.routing.BicycleOptions,com.here.sdk.routing.CalculateRouteCallback))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Location`](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core")`> locations, `[`BicycleOptions`](sdk-for-android-explore-api-reference-latestbicycleoptions "class in com.here.sdk.routing")` bicycleOptions, `[`CalculateRouteCallback`](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing")` callback)`

Deprecated.
Will be removed in v4.28.0.

  [`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [importRoute](#importRoute(java.util.List,com.here.sdk.routing.BusOptions,com.here.sdk.routing.CalculateRouteCallback))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Location`](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core")`> locations, `[`BusOptions`](sdk-for-android-explore-api-reference-latestbusoptions "class in com.here.sdk.routing")` busOptions, `[`CalculateRouteCallback`](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing")` callback)`

Deprecated.
Will be removed in v4.28.0.

  [`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [importRoute](#importRoute(java.util.List,com.here.sdk.routing.CarOptions,com.here.sdk.routing.CalculateRouteCallback))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Location`](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core")`> locations, `[`CarOptions`](sdk-for-android-explore-api-reference-latestcaroptions "class in com.here.sdk.routing")` carOptions, `[`CalculateRouteCallback`](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing")` callback)`

Deprecated.
Will be removed in v4.28.0.

  [`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [importRoute](#importRoute(java.util.List,com.here.sdk.routing.EVCarOptions,com.here.sdk.routing.CalculateRouteCallback))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Location`](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core")`> locations, `[`EVCarOptions`](sdk-for-android-explore-api-reference-latestevcaroptions "class in com.here.sdk.routing")` evCarOptions, `[`CalculateRouteCallback`](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing")` callback)`

Deprecated.
Will be removed in v4.28.0.

  [`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [importRoute](#importRoute(java.util.List,com.here.sdk.routing.EVTruckOptions,com.here.sdk.routing.CalculateRouteCallback))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Location`](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core")`> locations, `[`EVTruckOptions`](sdk-for-android-explore-api-reference-latestevtruckoptions "class in com.here.sdk.routing")` evTruckOptions, `[`CalculateRouteCallback`](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing")` callback)`

Deprecated.
Will be removed in v4.28.0.

  [`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [importRoute](#importRoute(java.util.List,com.here.sdk.routing.PedestrianOptions,com.here.sdk.routing.CalculateRouteCallback))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Location`](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core")`> locations, `[`PedestrianOptions`](sdk-for-android-explore-api-reference-latestpedestrianoptions "class in com.here.sdk.routing")` pedestrianOptions, `[`CalculateRouteCallback`](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing")` callback)`

Deprecated.
Will be removed in v4.28.0.

  [`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [importRoute](#importRoute(java.util.List,com.here.sdk.routing.PrivateBusOptions,com.here.sdk.routing.CalculateRouteCallback))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Location`](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core")`> locations, `[`PrivateBusOptions`](sdk-for-android-explore-api-reference-latestprivatebusoptions "class in com.here.sdk.routing")` privateBusOptions, `[`CalculateRouteCallback`](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing")` callback)`

Deprecated.
Will be removed in v4.28.0.

  [`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [importRoute](#importRoute(java.util.List,com.here.sdk.routing.RoutingOptions,com.here.sdk.routing.CalculateRouteCallback))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Location`](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core")`> locations, `[`RoutingOptions`](sdk-for-android-explore-api-reference-latestroutingoptions "class in com.here.sdk.routing")` options, `[`CalculateRouteCallback`](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing")` callback)`

Asynchronously creates a route from a sequence of geographic coordinates very close to each other.

[`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [importRoute](#importRoute(java.util.List,com.here.sdk.routing.ScooterOptions,com.here.sdk.routing.CalculateRouteCallback))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Location`](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core")`> locations, `[`ScooterOptions`](sdk-for-android-explore-api-reference-latestscooteroptions "class in com.here.sdk.routing")` scooterOptions, `[`CalculateRouteCallback`](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing")` callback)`

Deprecated.
Will be removed in v4.28.0.

  [`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [importRoute](#importRoute(java.util.List,com.here.sdk.routing.TaxiOptions,com.here.sdk.routing.CalculateRouteCallback))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Location`](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core")`> locations, `[`TaxiOptions`](sdk-for-android-explore-api-reference-latesttaxioptions "class in com.here.sdk.routing")` taxiOptions, `[`CalculateRouteCallback`](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing")` callback)`

Deprecated.
Will be removed in v4.28.0.

  [`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [importRoute](#importRoute(java.util.List,com.here.sdk.routing.TruckOptions,com.here.sdk.routing.CalculateRouteCallback))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Location`](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core")`> locations, `[`TruckOptions`](sdk-for-android-explore-api-reference-latesttruckoptions "class in com.here.sdk.routing")` truckOptions, `[`CalculateRouteCallback`](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing")` callback)`

Deprecated.
Will be removed in v4.28.0.

  [`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [importRoute](#importRoute(java.util.List,java.util.List,com.here.sdk.routing.BicycleOptions,com.here.sdk.routing.CalculateRouteCallback))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Location`](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core")`> locations, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`RouteStop`](sdk-for-android-explore-api-reference-latestroutestop "class in com.here.sdk.routing")`> routeStops, `[`BicycleOptions`](sdk-for-android-explore-api-reference-latestbicycleoptions "class in com.here.sdk.routing")` bicycleOptions, `[`CalculateRouteCallback`](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing")` callback)`

Deprecated.
Will be removed in v4.28.0.

  [`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [importRoute](#importRoute(java.util.List,java.util.List,com.here.sdk.routing.BusOptions,com.here.sdk.routing.CalculateRouteCallback))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Location`](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core")`> locations, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`RouteStop`](sdk-for-android-explore-api-reference-latestroutestop "class in com.here.sdk.routing")`> routeStops, `[`BusOptions`](sdk-for-android-explore-api-reference-latestbusoptions "class in com.here.sdk.routing")` busOptions, `[`CalculateRouteCallback`](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing")` callback)`

Deprecated.
Will be removed in v4.28.0.

  [`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [importRoute](#importRoute(java.util.List,java.util.List,com.here.sdk.routing.CarOptions,com.here.sdk.routing.CalculateRouteCallback))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Location`](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core")`> locations, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`RouteStop`](sdk-for-android-explore-api-reference-latestroutestop "class in com.here.sdk.routing")`> routeStops, `[`CarOptions`](sdk-for-android-explore-api-reference-latestcaroptions "class in com.here.sdk.routing")` carOptions, `[`CalculateRouteCallback`](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing")` callback)`

Deprecated.
Will be removed in v4.28.0.

  [`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [importRoute](#importRoute(java.util.List,java.util.List,com.here.sdk.routing.EVCarOptions,com.here.sdk.routing.CalculateRouteCallback))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Location`](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core")`> locations, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`RouteStop`](sdk-for-android-explore-api-reference-latestroutestop "class in com.here.sdk.routing")`> routeStops, `[`EVCarOptions`](sdk-for-android-explore-api-reference-latestevcaroptions "class in com.here.sdk.routing")` evCarOptions, `[`CalculateRouteCallback`](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing")` callback)`

Deprecated.
Will be removed in v4.28.0.

  [`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [importRoute](#importRoute(java.util.List,java.util.List,com.here.sdk.routing.EVTruckOptions,com.here.sdk.routing.CalculateRouteCallback))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Location`](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core")`> locations, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`RouteStop`](sdk-for-android-explore-api-reference-latestroutestop "class in com.here.sdk.routing")`> routeStops, `[`EVTruckOptions`](sdk-for-android-explore-api-reference-latestevtruckoptions "class in com.here.sdk.routing")` evTruckOptions, `[`CalculateRouteCallback`](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing")` callback)`

Deprecated.
Will be removed in v4.28.0.

  [`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [importRoute](#importRoute(java.util.List,java.util.List,com.here.sdk.routing.PedestrianOptions,com.here.sdk.routing.CalculateRouteCallback))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Location`](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core")`> locations, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`RouteStop`](sdk-for-android-explore-api-reference-latestroutestop "class in com.here.sdk.routing")`> routeStops, `[`PedestrianOptions`](sdk-for-android-explore-api-reference-latestpedestrianoptions "class in com.here.sdk.routing")` pedestrianOptions, `[`CalculateRouteCallback`](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing")` callback)`

Deprecated.
Will be removed in v4.28.0.

  [`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [importRoute](#importRoute(java.util.List,java.util.List,com.here.sdk.routing.PrivateBusOptions,com.here.sdk.routing.CalculateRouteCallback))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Location`](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core")`> locations, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`RouteStop`](sdk-for-android-explore-api-reference-latestroutestop "class in com.here.sdk.routing")`> routeStops, `[`PrivateBusOptions`](sdk-for-android-explore-api-reference-latestprivatebusoptions "class in com.here.sdk.routing")` privateBusOptions, `[`CalculateRouteCallback`](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing")` callback)`

Deprecated.
Will be removed in v4.28.0.

  [`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [importRoute](#importRoute(java.util.List,java.util.List,com.here.sdk.routing.RoutingOptions,com.here.sdk.routing.CalculateRouteCallback))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Location`](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core")`> locations, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`RouteStop`](sdk-for-android-explore-api-reference-latestroutestop "class in com.here.sdk.routing")`> routeStops, `[`RoutingOptions`](sdk-for-android-explore-api-reference-latestroutingoptions "class in com.here.sdk.routing")` options, `[`CalculateRouteCallback`](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing")` callback)`

Asynchronously creates a route from a sequence of geographic coordinates very close to each other.

[`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [importRoute](#importRoute(java.util.List,java.util.List,com.here.sdk.routing.ScooterOptions,com.here.sdk.routing.CalculateRouteCallback))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Location`](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core")`> locations, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`RouteStop`](sdk-for-android-explore-api-reference-latestroutestop "class in com.here.sdk.routing")`> routeStops, `[`ScooterOptions`](sdk-for-android-explore-api-reference-latestscooteroptions "class in com.here.sdk.routing")` scooterOptions, `[`CalculateRouteCallback`](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing")` callback)`

Deprecated.
Will be removed in v4.28.0.

  [`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [importRoute](#importRoute(java.util.List,java.util.List,com.here.sdk.routing.TaxiOptions,com.here.sdk.routing.CalculateRouteCallback))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Location`](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core")`> locations, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`RouteStop`](sdk-for-android-explore-api-reference-latestroutestop "class in com.here.sdk.routing")`> routeStops, `[`TaxiOptions`](sdk-for-android-explore-api-reference-latesttaxioptions "class in com.here.sdk.routing")` taxiOptions, `[`CalculateRouteCallback`](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing")` callback)`

Deprecated.
Will be removed in v4.28.0.

  [`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [importRoute](#importRoute(java.util.List,java.util.List,com.here.sdk.routing.TruckOptions,com.here.sdk.routing.CalculateRouteCallback))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Location`](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core")`> locations, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`RouteStop`](sdk-for-android-explore-api-reference-latestroutestop "class in com.here.sdk.routing")`> routeStops, `[`TruckOptions`](sdk-for-android-explore-api-reference-latesttruckoptions "class in com.here.sdk.routing")` truckOptions, `[`CalculateRouteCallback`](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing")` callback)`

Deprecated.
Will be removed in v4.28.0.

  [`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [refreshRoute](#refreshRoute(com.here.sdk.routing.RouteHandle,com.here.sdk.routing.Waypoint,com.here.sdk.routing.RefreshRouteOptions,com.here.sdk.routing.CalculateRouteCallback))`(`[`RouteHandle`](sdk-for-android-explore-api-reference-latestroutehandle "class in com.here.sdk.routing")` routeHandle, `[`Waypoint`](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing")` startingPoint, `[`RefreshRouteOptions`](sdk-for-android-explore-api-reference-latestrefreshrouteoptions "class in com.here.sdk.routing")` refreshRouteOptions, `[`CalculateRouteCallback`](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing")` callback)`

Deprecated.
Will be removed in v4.28.0.

  [`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [refreshRoute](#refreshRoute(com.here.sdk.routing.RouteHandle,com.here.sdk.routing.Waypoint,com.here.sdk.routing.RoutingOptions,com.here.sdk.routing.CalculateRouteCallback))`(`[`RouteHandle`](sdk-for-android-explore-api-reference-latestroutehandle "class in com.here.sdk.routing")` routeHandle, `[`Waypoint`](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing")` startingPoint, `[`RoutingOptions`](sdk-for-android-explore-api-reference-latestroutingoptions "class in com.here.sdk.routing")` options, `[`CalculateRouteCallback`](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing")` callback)`

Asynchronously refreshes a previously calculated route from the provided [`RouteHandle`](sdk-for-android-explore-api-reference-latestroutehandle "class in com.here.sdk.routing"), updating the starting point and route metadata based on [`RoutingOptions`](sdk-for-android-explore-api-reference-latestroutingoptions "class in com.here.sdk.routing").

[`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [refreshRoute](#refreshRoute(com.here.sdk.routing.RouteHandle,com.here.sdk.routing.Waypoint,java.lang.Integer,java.lang.Integer,com.here.sdk.routing.RefreshRouteOptions,com.here.sdk.routing.CalculateRouteCallback))`(`[`RouteHandle`](sdk-for-android-explore-api-reference-latestroutehandle "class in com.here.sdk.routing")` routeHandle, `[`Waypoint`](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing")` startingPoint, `[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)` lastTraveledSectionIndex, `[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)` traveledDistanceOnLastSectionInMeters, `[`RefreshRouteOptions`](sdk-for-android-explore-api-reference-latestrefreshrouteoptions "class in com.here.sdk.routing")` refreshRouteOptions, `[`CalculateRouteCallback`](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing")` callback)`

Deprecated.
Will be removed in v4.28.0.

  [`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [refreshRoute](#refreshRoute(com.here.sdk.routing.RouteHandle,com.here.sdk.routing.Waypoint,java.lang.Integer,java.lang.Integer,com.here.sdk.routing.RoutingOptions,com.here.sdk.routing.CalculateRouteCallback))`(`[`RouteHandle`](sdk-for-android-explore-api-reference-latestroutehandle "class in com.here.sdk.routing")` routeHandle, `[`Waypoint`](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing")` startingPoint, `[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)` lastTraveledSectionIndex, `[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)` traveledDistanceOnLastSectionInMeters, `[`RoutingOptions`](sdk-for-android-explore-api-reference-latestroutingoptions "class in com.here.sdk.routing")` options, `[`CalculateRouteCallback`](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing")` callback)`

Asynchronously refreshes a previously calculated route from the provided [`RouteHandle`](sdk-for-android-explore-api-reference-latestroutehandle "class in com.here.sdk.routing"), updating the starting point and route metadata based on [`RoutingOptions`](sdk-for-android-explore-api-reference-latestroutingoptions "class in com.here.sdk.routing").

[`TaskHandle`](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading")

  [returnToRoute](#returnToRoute(com.here.sdk.routing.Route,com.here.sdk.routing.Waypoint,int,int,com.here.sdk.routing.CalculateRouteCallback))`(`[`Route`](sdk-for-android-explore-api-reference-latestroute "class in com.here.sdk.routing")` route, `[`Waypoint`](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing")` startingPoint, int lastTraveledSectionIndex, int traveledDistanceOnLastSectionInMeters, `[`CalculateRouteCallback`](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing")` callback)`

Asynchronously calculates a new route that leads back to the original route.

[`RoutingError`](sdk-for-android-explore-api-reference-latestroutingerror "enum class in com.here.sdk.routing")

  [setCustomOption](#setCustomOption(java.lang.String,java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` value)`

Sets a custom option for routing backend queries.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - ()" class="section detail">

### RoutingEngine

public RoutingEngine() throws [InstantiationErrorException](sdk-for-android-explore-api-reference-latestinstantiationerrorexception "class in com.here.sdk.core.errors")

    Creates a new instance of this class.
Throws:
    [`InstantiationErrorException`](sdk-for-android-explore-api-reference-latestinstantiationerrorexception "class in com.here.sdk.core.errors") -

    Indicates what went wrong when the instantiation was attempted.
- (com.here.sdk.core.engine.SDKNativeEngine)" class="section detail">

### RoutingEngine

public RoutingEngine(@NonNull [SDKNativeEngine](sdk-for-android-explore-api-reference-latestsdknativeengine "class in com.here.sdk.core.engine") sdkEngine) throws [InstantiationErrorException](sdk-for-android-explore-api-reference-latestinstantiationerrorexception "class in com.here.sdk.core.errors")

    Creates a new instance of RoutingEngine.
Parameters:
    `sdkEngine` -

    An SDKEngine instance.

    Throws:
    [`InstantiationErrorException`](sdk-for-android-explore-api-reference-latestinstantiationerrorexception "class in com.here.sdk.core.errors") -

    Indicates what went wrong when the instantiation was attempted.
- (com.here.sdk.routing.RoutingConnectionSettings)" class="section detail">

### RoutingEngine

public RoutingEngine(@NonNull [RoutingConnectionSettings](sdk-for-android-explore-api-reference-latestroutingconnectionsettings "class in com.here.sdk.routing") connectionSettings) throws [InstantiationErrorException](sdk-for-android-explore-api-reference-latestinstantiationerrorexception "class in com.here.sdk.core.errors")

    Creates a new instance of RoutingEngine.
Parameters:
    `connectionSettings` -

    Settings for the route calculation.

    Throws:
    [`InstantiationErrorException`](sdk-for-android-explore-api-reference-latestinstantiationerrorexception "class in com.here.sdk.core.errors") -

    Indicates what went wrong when the instantiation was attempted.
- (com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.routing.RoutingConnectionSettings)" class="section detail">

### RoutingEngine

public RoutingEngine(@NonNull [SDKNativeEngine](sdk-for-android-explore-api-reference-latestsdknativeengine "class in com.here.sdk.core.engine") sdkEngine, @NonNull [RoutingConnectionSettings](sdk-for-android-explore-api-reference-latestroutingconnectionsettings "class in com.here.sdk.routing") connectionSettings) throws [InstantiationErrorException](sdk-for-android-explore-api-reference-latestinstantiationerrorexception "class in com.here.sdk.core.errors")

    Creates a new instance of RoutingEngine.
Parameters:
    `sdkEngine` -

    An SDKEngine instance.

    `connectionSettings` -

    Settings for the route calculation.

    Throws:
    [`InstantiationErrorException`](sdk-for-android-explore-api-reference-latestinstantiationerrorexception "class in com.here.sdk.core.errors") -

    Indicates what went wrong when the instantiation was attempted.

## Method Details

### refreshRoute

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") refreshRoute(@NonNull [RouteHandle](sdk-for-android-explore-api-reference-latestroutehandle "class in com.here.sdk.routing") routeHandle, @NonNull [Waypoint](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing") startingPoint, @NonNull [RefreshRouteOptions](sdk-for-android-explore-api-reference-latestrefreshrouteoptions "class in com.here.sdk.routing") refreshRouteOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Deprecated.
Will be removed in v4.28.0. Use the `refresh_route()` methods with RoutingOptions parameter instead.

Asynchronously refreshes a previously calculated route from the provided [`RouteHandle`](sdk-for-android-explore-api-reference-latestroutehandle "class in com.here.sdk.routing"), updating the starting point and route metadata based on [`RefreshRouteOptions`](sdk-for-android-explore-api-reference-latestrefreshrouteoptions "class in com.here.sdk.routing"). The route shape from the new starting point to the destination remains unchanged, and only metadata such as arrival time and traffic delays are updated. If you only want to refresh the contained traffic information or retrieve updated ETA duration, consider using [`calculateTrafficOnRoute(Route, int, int, double, CalculateTrafficOnRouteCallback)`](#calculateTrafficOnRoute(com.here.sdk.routing.Route,int,int,double,com.here.sdk.routing.CalculateTrafficOnRouteCallback)) instead.

    Calling this method will trigger a new "HERE Routing" transaction, for example, if you are using the [Base Plan](https://www.here.com/get-started/pricing).
Parameters:
    `routeHandle` -

    The route handle holding the route to be refreshed.

    `startingPoint` -

    Updates the starting point of the route. It should be of type [`WaypointType.STOPOVER`](sdk-for-android-explore-api-reference-latestwaypointtype#STOPOVER). Otherwise, an [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-api-reference-latestroutingerror#INVALID_PARAMETER) error is generated. Moreover, it should be very close to the original route specified with the [`RouteHandle`](sdk-for-android-explore-api-reference-latestroutehandle "class in com.here.sdk.routing"). Since the new starting point is expected to be along the original route, the original route geometry is used to reach the remaining waypoints. The new route will not include the [`Waypoint`](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing") items that lie behind the new starting point (i.e. the path that was already travelled). Plus, [`Route.getLengthInMeters()`](sdk-for-android-explore-api-reference-latestroute#getLengthInMeters()) and [`Route.getDuration()`](sdk-for-android-explore-api-reference-latestroute#getDuration()) values are from the new starting point to the destination. If the new waypoint is too far off the original route, the route refresh may fail and an [`RoutingError.COULD_NOT_MATCH_ORIGIN`](sdk-for-android-explore-api-reference-latestroutingerror#COULD_NOT_MATCH_ORIGIN) error is triggered. In that case, an application may decide to calculate a new route from scratch.

    `refreshRouteOptions` -

    Options to refresh the route.

    `callback` -

    Callback object that will be invoked after refreshing the route. It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### refreshRoute

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") refreshRoute(@NonNull [RouteHandle](sdk-for-android-explore-api-reference-latestroutehandle "class in com.here.sdk.routing") routeHandle, @Nullable [Waypoint](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing") startingPoint, @Nullable [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) lastTraveledSectionIndex, @Nullable [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) traveledDistanceOnLastSectionInMeters, @NonNull [RefreshRouteOptions](sdk-for-android-explore-api-reference-latestrefreshrouteoptions "class in com.here.sdk.routing") refreshRouteOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Deprecated.
Will be removed in v4.28.0. Use the `refresh_route()` methods with RoutingOptions parameter instead.

Asynchronously refreshes a previously calculated route from the provided [`RouteHandle`](sdk-for-android-explore-api-reference-latestroutehandle "class in com.here.sdk.routing"), updating the starting point and route metadata based on [`RefreshRouteOptions`](sdk-for-android-explore-api-reference-latestrefreshrouteoptions "class in com.here.sdk.routing"). The route shape from the new starting point to the destination remains unchanged, and only metadata such as arrival time and traffic delays are updated. If you only want to refresh the contained traffic information, consider to use [`calculateTrafficOnRoute(Route, int, int, double, CalculateTrafficOnRouteCallback)`](#calculateTrafficOnRoute(com.here.sdk.routing.Route,int,int,double,com.here.sdk.routing.CalculateTrafficOnRouteCallback)) instead.

    Calling this method will trigger a new "HERE Routing" transaction, for example, if you are using the [Base Plan](https://www.here.com/get-started/pricing).
Parameters:
    `routeHandle` -

    The route handle holding the route to be refreshed.

    `startingPoint` -

    Updates the starting point of the route. It should be of type [`WaypointType.STOPOVER`](sdk-for-android-explore-api-reference-latestwaypointtype#STOPOVER). Otherwise, an [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-api-reference-latestroutingerror#INVALID_PARAMETER) error is generated. Moreover, it should be very close to the original route specified with the [`RouteHandle`](sdk-for-android-explore-api-reference-latestroutehandle "class in com.here.sdk.routing"). Since the new starting point is expected to be along the original route, the original route geometry is used to reach the remaining waypoints. The new route will not include the [`Waypoint`](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing") items that lie behind the new starting point (i.e. the path that was already travelled). Plus, [`Route.getLengthInMeters()`](sdk-for-android-explore-api-reference-latestroute#getLengthInMeters()) and [`Route.getDuration()`](sdk-for-android-explore-api-reference-latestroute#getDuration()) values are from the new starting point to the destination. If the new waypoint is too far off the original route, the route refresh may fail and an [`RoutingError.COULD_NOT_MATCH_ORIGIN`](sdk-for-android-explore-api-reference-latestroutingerror#COULD_NOT_MATCH_ORIGIN) error is triggered. In that case, an application may decide to calculate a new route from scratch.

    `lastTraveledSectionIndex` -

    Indicates the index of the last traveled route section. Traveled part of the route won't be reused.

    `traveledDistanceOnLastSectionInMeters` -

    Offset in meter to the last visited position on the route section defined by the last traveled section index.

    `refreshRouteOptions` -

    Options to refresh the route.

    `callback` -

    Callback object that will be invoked after refreshing the route. It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### refreshRoute

@NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") refreshRoute(@NonNull [RouteHandle](sdk-for-android-explore-api-reference-latestroutehandle "class in com.here.sdk.routing") routeHandle, @Nullable [Waypoint](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing") startingPoint, @Nullable [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) lastTraveledSectionIndex, @Nullable [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html) traveledDistanceOnLastSectionInMeters, @NonNull [RoutingOptions](sdk-for-android-explore-api-reference-latestroutingoptions "class in com.here.sdk.routing") options, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Asynchronously refreshes a previously calculated route from the provided [`RouteHandle`](sdk-for-android-explore-api-reference-latestroutehandle "class in com.here.sdk.routing"), updating the starting point and route metadata based on [`RoutingOptions`](sdk-for-android-explore-api-reference-latestroutingoptions "class in com.here.sdk.routing"). The route shape from the new starting point to the destination remains unchanged, and only metadata such as arrival time and traffic delays are updated. If you only want to refresh the contained traffic information, consider to use [`calculateTrafficOnRoute(Route, int, int, double, CalculateTrafficOnRouteCallback)`](#calculateTrafficOnRoute(com.here.sdk.routing.Route,int,int,double,com.here.sdk.routing.CalculateTrafficOnRouteCallback)) instead.

    Calling this method will trigger a new "HERE Routing" transaction, for example, if you are using the [Base Plan](https://www.here.com/get-started/pricing).
Parameters:
    `routeHandle` -

    The route handle holding the route to be refreshed.

    `startingPoint` -

    Updates the starting point of the route. It should be of type [`WaypointType.STOPOVER`](sdk-for-android-explore-api-reference-latestwaypointtype#STOPOVER). Otherwise, an [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-api-reference-latestroutingerror#INVALID_PARAMETER) error is generated. Moreover, it should be very close to the original route specified with the [`RouteHandle`](sdk-for-android-explore-api-reference-latestroutehandle "class in com.here.sdk.routing"). Since the new starting point is expected to be along the original route, the original route geometry is used to reach the remaining waypoints. The new route will not include the [`Waypoint`](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing") items that lie behind the new starting point (i.e. the path that was already traveled). Plus, [`Route.getLengthInMeters()`](sdk-for-android-explore-api-reference-latestroute#getLengthInMeters()) and [`Route.getDuration()`](sdk-for-android-explore-api-reference-latestroute#getDuration()) values are from the new starting point to the destination. If the new waypoint is too far off the original route, the route refresh may fail and an [`RoutingError.COULD_NOT_MATCH_ORIGIN`](sdk-for-android-explore-api-reference-latestroutingerror#COULD_NOT_MATCH_ORIGIN) error is triggered. In that case, an application may decide to calculate a new route from scratch.

    `lastTraveledSectionIndex` -

    Indicates the index of the last traveled route section. Traveled part of the route won't be reused.

    `traveledDistanceOnLastSectionInMeters` -

    Offset in meter to the last visited position on the route section defined by the last traveled section index.

    `options` -

    The options define the vehicle and route options to calculate the route.

    `callback` -

    Callback object that will be invoked after refreshing the route. It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### refreshRoute

@NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") refreshRoute(@NonNull [RouteHandle](sdk-for-android-explore-api-reference-latestroutehandle "class in com.here.sdk.routing") routeHandle, @NonNull [Waypoint](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing") startingPoint, @NonNull [RoutingOptions](sdk-for-android-explore-api-reference-latestroutingoptions "class in com.here.sdk.routing") options, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Asynchronously refreshes a previously calculated route from the provided [`RouteHandle`](sdk-for-android-explore-api-reference-latestroutehandle "class in com.here.sdk.routing"), updating the starting point and route metadata based on [`RoutingOptions`](sdk-for-android-explore-api-reference-latestroutingoptions "class in com.here.sdk.routing"). The route shape from the new starting point to the destination remains unchanged, and only metadata such as arrival time and traffic delays are updated. If you only want to refresh the contained traffic information, consider to use [`calculateTrafficOnRoute(Route, int, int, double, CalculateTrafficOnRouteCallback)`](#calculateTrafficOnRoute(com.here.sdk.routing.Route,int,int,double,com.here.sdk.routing.CalculateTrafficOnRouteCallback)) instead.

    Calling this method will trigger a new "HERE Routing" transaction, for example, if you are using the [Base Plan](https://www.here.com/get-started/pricing).
Parameters:
    `routeHandle` -

    The route handle holding the route to be refreshed.

    `startingPoint` -

    Updates the starting point of the route. It should be of type [`WaypointType.STOPOVER`](sdk-for-android-explore-api-reference-latestwaypointtype#STOPOVER). Otherwise, an [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-api-reference-latestroutingerror#INVALID_PARAMETER) error is generated. Moreover, it should be very close to the original route specified with the [`RouteHandle`](sdk-for-android-explore-api-reference-latestroutehandle "class in com.here.sdk.routing"). Since the new starting point is expected to be along the original route, the original route geometry is used to reach the remaining waypoints. The new route will not include the [`Waypoint`](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing") items that lie behind the new starting point (i.e. the path that was already traveled). Plus, [`Route.getLengthInMeters()`](sdk-for-android-explore-api-reference-latestroute#getLengthInMeters()) and [`Route.getDuration()`](sdk-for-android-explore-api-reference-latestroute#getDuration()) values are from the new starting point to the destination. If the new waypoint is too far off the original route, the route refresh may fail and an [`RoutingError.COULD_NOT_MATCH_ORIGIN`](sdk-for-android-explore-api-reference-latestroutingerror#COULD_NOT_MATCH_ORIGIN) error is triggered. In that case, an application may decide to calculate a new route from scratch.

    `options` -

    The options define the vehicle and route options to calculate the route.

    `callback` -

    Callback object that will be invoked after refreshing the route. It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### importRoute

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") importRoute(@NonNull [RouteHandle](sdk-for-android-explore-api-reference-latestroutehandle "class in com.here.sdk.routing") routeHandle, @NonNull [RefreshRouteOptions](sdk-for-android-explore-api-reference-latestrefreshrouteoptions "class in com.here.sdk.routing") refreshRouteOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Deprecated.
Will be removed in v4.28.0. Use the `import_route()` methods with RoutingOptions parameter instead.

Asynchronously recreates a route from the [`RouteHandle`](sdk-for-android-explore-api-reference-latestroutehandle "class in com.here.sdk.routing") provided, i.e. refreshes a previously calculated route, with the specified [`RefreshRouteOptions`](sdk-for-android-explore-api-reference-latestrefreshrouteoptions "class in com.here.sdk.routing").

    A route handle can be invalid when the map data changes that is used by the HERE backend to recreate the route. This happens regularly. Therefore, the route handle is not meant to be persisted for a longer time. Instead, a possible use case can be to plan a route with another HERE service. For example, a HERE REST API that allows to calculate a route on a desktop. Then this route can be transferred via the handle to a mobile device for further use with the HERE SDK.
Parameters:
    `routeHandle` -

    The route handle holding the route to be refreshed.

    `refreshRouteOptions` -

    The options define the vehicle and route options to calculate the route. **Note** An \[sdk.routing.RoutingError.INVALID_PARAMETER\] is generated when the \[sdk.routing.ElectricVehicleOptions.ensure_reachability\] option is set to `true`.

    `callback` -

    Callback object that will be invoked after refreshing the route. It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### importRoute

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") importRoute(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Location](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core")\> locations, @NonNull [CarOptions](sdk-for-android-explore-api-reference-latestcaroptions "class in com.here.sdk.routing") carOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Deprecated.
Will be removed in v4.28.0. Use the `import_route()` methods with RoutingOptions parameter instead.

Asynchronously creates a car route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.

    **Note:** Any restrictions applied to a transport type or provided options will be discarded and reported as violations in [`Section.getSectionNotices()`](sdk-for-android-explore-api-reference-latestsection#getSectionNotices()) .
Parameters:
    `locations` -

    The list of locations used to calculate the route. Note that only the [`Location.coordinates`](sdk-for-android-explore-api-reference-latestlocation#coordinates) of a location are used to import the route.

    An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-api-reference-latestroutingerror#INVALID_PARAMETER) error is generated when the location list size is not in the range \[2,50000\].

    `carOptions` -

    Options specific for car route calculation, along with common route options.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### importRoute

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") importRoute(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Location](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core")\> locations, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[RouteStop](sdk-for-android-explore-api-reference-latestroutestop "class in com.here.sdk.routing")\> routeStops, @NonNull [PedestrianOptions](sdk-for-android-explore-api-reference-latestpedestrianoptions "class in com.here.sdk.routing") pedestrianOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Deprecated.
Will be removed in v4.28.0. Use the `import_route()` methods with RoutingOptions parameter instead.

Asynchronously creates a pedestrian route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.

    **Note:** Any restrictions applied to a transport type or provided options will be discarded and reported as violations in [`Section.getSectionNotices()`](sdk-for-android-explore-api-reference-latestsection#getSectionNotices()) .
Parameters:
    `locations` -

    The list of locations used to calculate the route. Note that only the [`Location.coordinates`](sdk-for-android-explore-api-reference-latestlocation#coordinates) of a location are used to import the route.

    An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-api-reference-latestroutingerror#INVALID_PARAMETER) error is generated when the location list size is not in the range \[2,50000\].

    `routeStops` -

    The list of RouteStop's which contains index of location from locations list used for route stop and duration in seconds spent on stop.

    An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-api-reference-latestroutingerror#INVALID_PARAMETER) error is generated when the route stops list size is not in the range \[1,locations.size()-2\], any of location_index is \< 1 or location_indexes are not unique.

    `pedestrianOptions` -

    Options specific for pedestrian route calculation, along with common route options. Note that [`OptimizationMode.SHORTEST`](sdk-for-android-explore-api-reference-latestoptimizationmode#SHORTEST) is not supported for pedestrians and converted to [`OptimizationMode.FASTEST`](sdk-for-android-explore-api-reference-latestoptimizationmode#FASTEST) automatically.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### importRoute

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") importRoute(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Location](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core")\> locations, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[RouteStop](sdk-for-android-explore-api-reference-latestroutestop "class in com.here.sdk.routing")\> routeStops, @NonNull [BicycleOptions](sdk-for-android-explore-api-reference-latestbicycleoptions "class in com.here.sdk.routing") bicycleOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Deprecated.
Will be removed in v4.28.0. Use the `import_route()` methods with RoutingOptions parameter instead.

Asynchronously creates a bicycle route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.

    **Note:** Any restrictions applied to a transport type or provided options will be discarded and reported as violations in [`Section.getSectionNotices()`](sdk-for-android-explore-api-reference-latestsection#getSectionNotices()) .
Parameters:
    `locations` -

    The list of locations used to calculate the route. Note that only the [`Location.coordinates`](sdk-for-android-explore-api-reference-latestlocation#coordinates) of a location are used to import the route.

    An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-api-reference-latestroutingerror#INVALID_PARAMETER) error is generated when the location list size is not in the range \[2,50000\].

    `routeStops` -

    The list of RouteStop's which contains index of location from locations list used for route stop and duration in seconds spent on stop.

    An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-api-reference-latestroutingerror#INVALID_PARAMETER) error is generated when the route stops list size is not in the range \[1,locations.size()-2\], any of location_index is \< 1 or location_indexes are not unique.

    `bicycleOptions` -

    Options specific for bicycle route calculation, along with common route options.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### importRoute

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") importRoute(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Location](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core")\> locations, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[RouteStop](sdk-for-android-explore-api-reference-latestroutestop "class in com.here.sdk.routing")\> routeStops, @NonNull [ScooterOptions](sdk-for-android-explore-api-reference-latestscooteroptions "class in com.here.sdk.routing") scooterOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Deprecated.
Will be removed in v4.28.0. Use the `import_route()` methods with RoutingOptions parameter instead.

Asynchronously creates a scooter route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.

    **Note:** Any restrictions applied to a transport type or provided options will be discarded and reported as violations in [`Section.getSectionNotices()`](sdk-for-android-explore-api-reference-latestsection#getSectionNotices()) .
Parameters:
    `locations` -

    The list of locations used to calculate the route. Note that only the [`Location.coordinates`](sdk-for-android-explore-api-reference-latestlocation#coordinates) of a location are used to import the route.

    An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-api-reference-latestroutingerror#INVALID_PARAMETER) error is generated when the location list size is not in the range \[2,50000\].

    `routeStops` -

    The list of RouteStop's which contains index of location from locations list used for route stop and duration in seconds spent on stop.

    An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-api-reference-latestroutingerror#INVALID_PARAMETER) error is generated when the route stops list size is not in the range \[1,locations.size()-2\], any of location_index is \< 1 or location_indexes are not unique.

    `scooterOptions` -

    Options specific for scooter route calculation, along with common route options. Note that [`OptimizationMode.SHORTEST`](sdk-for-android-explore-api-reference-latestoptimizationmode#SHORTEST) is not supported for scooters and converted to [`OptimizationMode.FASTEST`](sdk-for-android-explore-api-reference-latestoptimizationmode#FASTEST) automatically.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### importRoute

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") importRoute(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Location](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core")\> locations, @NonNull [PedestrianOptions](sdk-for-android-explore-api-reference-latestpedestrianoptions "class in com.here.sdk.routing") pedestrianOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Deprecated.
Will be removed in v4.28.0. Use the `import_route()` methods with RoutingOptions parameter instead.

Asynchronously creates a pedestrian route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.

    **Note:** Any restrictions applied to a transport type or provided options will be discarded and reported as violations in [`Section.getSectionNotices()`](sdk-for-android-explore-api-reference-latestsection#getSectionNotices()) .
Parameters:
    `locations` -

    The list of locations used to calculate the route. Note that only the [`Location.coordinates`](sdk-for-android-explore-api-reference-latestlocation#coordinates) of a location are used to import the route.

    An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-api-reference-latestroutingerror#INVALID_PARAMETER) error is generated when the location list size is not in the range \[2,50000\].

    `pedestrianOptions` -

    Options specific for pedestrian route calculation, along with common route options. Note that [`OptimizationMode.SHORTEST`](sdk-for-android-explore-api-reference-latestoptimizationmode#SHORTEST) is not supported for pedestrians and converted to [`OptimizationMode.FASTEST`](sdk-for-android-explore-api-reference-latestoptimizationmode#FASTEST) automatically.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### importRoute

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") importRoute(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Location](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core")\> locations, @NonNull [BicycleOptions](sdk-for-android-explore-api-reference-latestbicycleoptions "class in com.here.sdk.routing") bicycleOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Deprecated.
Will be removed in v4.28.0. Use the `import_route()` methods with RoutingOptions parameter instead.

Asynchronously creates a bicycle route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.

    **Note:** Any restrictions applied to a transport type or provided options will be discarded and reported as violations in [`Section.getSectionNotices()`](sdk-for-android-explore-api-reference-latestsection#getSectionNotices()) .
Parameters:
    `locations` -

    The list of locations used to calculate the route. Note that only the [`Location.coordinates`](sdk-for-android-explore-api-reference-latestlocation#coordinates) of a location are used to import the route.

    An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-api-reference-latestroutingerror#INVALID_PARAMETER) error is generated when the location list size is not in the range \[2,50000\].

    `bicycleOptions` -

    Options specific for bicycle route calculation, along with common route options.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### importRoute

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") importRoute(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Location](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core")\> locations, @NonNull [ScooterOptions](sdk-for-android-explore-api-reference-latestscooteroptions "class in com.here.sdk.routing") scooterOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Deprecated.
Will be removed in v4.28.0. Use the `import_route()` methods with RoutingOptions parameter instead.

Asynchronously creates a scooter route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.

    **Note:** Any restrictions applied to a transport type or provided options will be discarded and reported as violations in [`Section.getSectionNotices()`](sdk-for-android-explore-api-reference-latestsection#getSectionNotices()) .
Parameters:
    `locations` -

    The list of locations used to calculate the route. Note that only the [`Location.coordinates`](sdk-for-android-explore-api-reference-latestlocation#coordinates) of a location are used to import the route.

    An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-api-reference-latestroutingerror#INVALID_PARAMETER) error is generated when the location list size is not in the range \[2,50000\].

    `scooterOptions` -

    Options specific for scooter route calculation, along with common route options. Note that [`OptimizationMode.SHORTEST`](sdk-for-android-explore-api-reference-latestoptimizationmode#SHORTEST) is not supported for scooters and converted to [`OptimizationMode.FASTEST`](sdk-for-android-explore-api-reference-latestoptimizationmode#FASTEST) automatically.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### importRoute

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") importRoute(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Location](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core")\> locations, @NonNull [TruckOptions](sdk-for-android-explore-api-reference-latesttruckoptions "class in com.here.sdk.routing") truckOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Deprecated.
Will be removed in v4.28.0. Use the `import_route()` methods with RoutingOptions parameter instead.

Asynchronously creates a truck route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.

    **Note:** Any restrictions applied to a transport type or provided options will be discarded and reported as violations in [`Section.getSectionNotices()`](sdk-for-android-explore-api-reference-latestsection#getSectionNotices()) .
Parameters:
    `locations` -

    The list of locations used to calculate the route. Note that only the [`Location.coordinates`](sdk-for-android-explore-api-reference-latestlocation#coordinates) of a location are used to import the route.

    An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-api-reference-latestroutingerror#INVALID_PARAMETER) error is generated when the location list size is not in the range \[2,50000\].

    `truckOptions` -

    Options specific for truck route calculation, along with common route options.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### importRoute

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") importRoute(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Location](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core")\> locations, @NonNull [TaxiOptions](sdk-for-android-explore-api-reference-latesttaxioptions "class in com.here.sdk.routing") taxiOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Deprecated.
Will be removed in v4.28.0. Use the `import_route()` methods with RoutingOptions parameter instead.

Asynchronously creates a taxi route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.

    **Note:** Any restrictions applied to a transport type or provided options will be discarded and reported as violations in [`Section.getSectionNotices()`](sdk-for-android-explore-api-reference-latestsection#getSectionNotices()) .
Parameters:
    `locations` -

    The list of locations used to calculate the route. Note that only the [`Location.coordinates`](sdk-for-android-explore-api-reference-latestlocation#coordinates) of a location are used to import the route.

    An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-api-reference-latestroutingerror#INVALID_PARAMETER) error is generated when the location list size is not in the range \[2,50000\].

    `taxiOptions` -

    Options specific for taxi route calculation, along with common route options. Note that [`OptimizationMode.SHORTEST`](sdk-for-android-explore-api-reference-latestoptimizationmode#SHORTEST) is not supported for taxis and converted to [`OptimizationMode.FASTEST`](sdk-for-android-explore-api-reference-latestoptimizationmode#FASTEST) automatically.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### importRoute

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") importRoute(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Location](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core")\> locations, @NonNull [BusOptions](sdk-for-android-explore-api-reference-latestbusoptions "class in com.here.sdk.routing") busOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Deprecated.
Will be removed in v4.28.0. Use the `import_route()` methods with RoutingOptions parameter instead.

Asynchronously creates a bus route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.

    **Note:** Any restrictions applied to a transport type or provided options will be discarded and reported as violations in [`Section.getSectionNotices()`](sdk-for-android-explore-api-reference-latestsection#getSectionNotices()) .
Parameters:
    `locations` -

    The list of locations used to calculate the route. Note that only the [`Location.coordinates`](sdk-for-android-explore-api-reference-latestlocation#coordinates) of a location are used to import the route.

    An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-api-reference-latestroutingerror#INVALID_PARAMETER) error is generated when the location list size is not in the range \[2,50000\].

    `busOptions` -

    Options specific for bus route calculation, along with common route options.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### importRoute

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") importRoute(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Location](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core")\> locations, @NonNull [PrivateBusOptions](sdk-for-android-explore-api-reference-latestprivatebusoptions "class in com.here.sdk.routing") privateBusOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Deprecated.
Will be removed in v4.28.0. Use the `import_route()` methods with RoutingOptions parameter instead.

Asynchronously creates a private bus route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or anyway geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.

    **Note:** Any restrictions applied to a transport type or provided options will be discarded and reported as violations in [`Section.getSectionNotices()`](sdk-for-android-explore-api-reference-latestsection#getSectionNotices()) .
Parameters:
    `locations` -

    The list of locations used to calculate the route. Note that only the [`Location.coordinates`](sdk-for-android-explore-api-reference-latestlocation#coordinates) of a location are used to import the route.

    An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-api-reference-latestroutingerror#INVALID_PARAMETER) error is generated when the location list size is not in the range \[2,50000\].

    `privateBusOptions` -

    Options specific for private bus route calculation, along with common route options.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### importRoute

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") importRoute(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Location](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core")\> locations, @NonNull [EVCarOptions](sdk-for-android-explore-api-reference-latestevcaroptions "class in com.here.sdk.routing") evCarOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Deprecated.
Will be removed in v4.28.0. Use the `import_route()` methods with RoutingOptions parameter instead.

Asynchronously creates an electric car route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.

    **Note:** Any restrictions applied to a transport type or provided options will be discarded and reported as violations in [`Section.getSectionNotices()`](sdk-for-android-explore-api-reference-latestsection#getSectionNotices()) .
Parameters:
    `locations` -

    The list of locations used to calculate the route. Note that only the [`Location.coordinates`](sdk-for-android-explore-api-reference-latestlocation#coordinates) of a location are used to import the route.

    An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-api-reference-latestroutingerror#INVALID_PARAMETER) error is generated when the location list size is not in the range \[2,50000\].

    `evCarOptions` -

    Options specific for an electric car route calculation, along with common route options. **Note** An \[sdk.routing.RoutingError.INVALID_PARAMETER\] is generated when the \[sdk.routing.EVCarOptions.ensure_reachability\] option is set to `true`.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### importRoute

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") importRoute(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Location](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core")\> locations, @NonNull [EVTruckOptions](sdk-for-android-explore-api-reference-latestevtruckoptions "class in com.here.sdk.routing") evTruckOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Deprecated.
Will be removed in v4.28.0. Use the `import_route()` methods with RoutingOptions parameter instead.

Asynchronously creates an electric truck route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.

    **Note:** Any restrictions applied to a transport type or provided options will be discarded and reported as violations in [`Section.getSectionNotices()`](sdk-for-android-explore-api-reference-latestsection#getSectionNotices()) .
Parameters:
    `locations` -

    The list of locations used to calculate the route. Note that only the [`Location.coordinates`](sdk-for-android-explore-api-reference-latestlocation#coordinates) of a location are used to import the route.

    An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-api-reference-latestroutingerror#INVALID_PARAMETER) error is generated when the location list size is not in the range \[2,50000\].

    `evTruckOptions` -

    Options specific for an electric truck route calculation, along with common route options.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### importRoute

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") importRoute(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Location](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core")\> locations, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[RouteStop](sdk-for-android-explore-api-reference-latestroutestop "class in com.here.sdk.routing")\> routeStops, @NonNull [CarOptions](sdk-for-android-explore-api-reference-latestcaroptions "class in com.here.sdk.routing") carOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Deprecated.
Will be removed in v4.28.0. Use the `import_route()` methods with RoutingOptions parameter instead.

Asynchronously creates a car route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.

    **Note:** Any restrictions applied to a transport type or provided options will be discarded and reported as violations in [`Section.getSectionNotices()`](sdk-for-android-explore-api-reference-latestsection#getSectionNotices()) .
Parameters:
    `locations` -

    The list of locations used to calculate the route. Note that only the [`Location.coordinates`](sdk-for-android-explore-api-reference-latestlocation#coordinates) of a location are used to import the route.

    An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-api-reference-latestroutingerror#INVALID_PARAMETER) error is generated when the location list size is not in the range \[2,50000\].

    `routeStops` -

    The list of RouteStop's which contains index of location from locations list used for route stop and duration in seconds spent on stop.

    An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-api-reference-latestroutingerror#INVALID_PARAMETER) error is generated when the route stops list size is not in the range \[1,locations.size()-2\], any of location_index is \< 1 or location_indexes are not unique.

    `carOptions` -

    Options specific for car route calculation, along with common route options.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### importRoute

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") importRoute(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Location](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core")\> locations, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[RouteStop](sdk-for-android-explore-api-reference-latestroutestop "class in com.here.sdk.routing")\> routeStops, @NonNull [TruckOptions](sdk-for-android-explore-api-reference-latesttruckoptions "class in com.here.sdk.routing") truckOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Deprecated.
Will be removed in v4.28.0. Use the `import_route()` methods with RoutingOptions parameter instead.

Asynchronously creates a truck route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.

    **Note:** Any restrictions applied to a transport type or provided options will be discarded and reported as violations in [`Section.getSectionNotices()`](sdk-for-android-explore-api-reference-latestsection#getSectionNotices()) .
Parameters:
    `locations` -

    The list of locations used to calculate the route. Note that only the [`Location.coordinates`](sdk-for-android-explore-api-reference-latestlocation#coordinates) of a location are used to import the route.

    An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-api-reference-latestroutingerror#INVALID_PARAMETER) error is generated when the location list size is not in the range \[2,50000\].

    `routeStops` -

    The list of RouteStop's which contains index of location from locations list used for route stop and duration in seconds spent on stop.

    An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-api-reference-latestroutingerror#INVALID_PARAMETER) error is generated when the route stops list size is not in the range \[1,locations.size()-2\], any of location_index is \< 1 or location_indexes are not unique.

    `truckOptions` -

    Options specific for truck route calculation, along with common route options.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### importRoute

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") importRoute(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Location](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core")\> locations, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[RouteStop](sdk-for-android-explore-api-reference-latestroutestop "class in com.here.sdk.routing")\> routeStops, @NonNull [TaxiOptions](sdk-for-android-explore-api-reference-latesttaxioptions "class in com.here.sdk.routing") taxiOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Deprecated.
Will be removed in v4.28.0. Use the `import_route()` methods with RoutingOptions parameter instead.

Asynchronously creates a taxi route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.

    **Note:** Any restrictions applied to a transport type or provided options will be discarded and reported as violations in [`Section.getSectionNotices()`](sdk-for-android-explore-api-reference-latestsection#getSectionNotices()) .
Parameters:
    `locations` -

    The list of locations used to calculate the route. Note that only the [`Location.coordinates`](sdk-for-android-explore-api-reference-latestlocation#coordinates) of a location are used to import the route.

    An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-api-reference-latestroutingerror#INVALID_PARAMETER) error is generated when the location list size is not in the range \[2,50000\].

    `routeStops` -

    The list of RouteStop's which contains index of location from locations list used for route stop and duration in seconds spent on stop.

    An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-api-reference-latestroutingerror#INVALID_PARAMETER) error is generated when the route stops list size is not in the range \[1,locations.size()-2\], any of location_index is \< 1 or location_indexes are not unique.

    `taxiOptions` -

    Options specific for taxi route calculation, along with common route options. Note that [`OptimizationMode.SHORTEST`](sdk-for-android-explore-api-reference-latestoptimizationmode#SHORTEST) is not supported for taxis and converted to [`OptimizationMode.FASTEST`](sdk-for-android-explore-api-reference-latestoptimizationmode#FASTEST) automatically.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### importRoute

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") importRoute(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Location](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core")\> locations, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[RouteStop](sdk-for-android-explore-api-reference-latestroutestop "class in com.here.sdk.routing")\> routeStops, @NonNull [BusOptions](sdk-for-android-explore-api-reference-latestbusoptions "class in com.here.sdk.routing") busOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Deprecated.
Will be removed in v4.28.0. Use the `import_route()` methods with RoutingOptions parameter instead.

Asynchronously creates a bus route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.

    **Note:** Any restrictions applied to a transport type or provided options will be discarded and reported as violations in [`Section.getSectionNotices()`](sdk-for-android-explore-api-reference-latestsection#getSectionNotices()) .
Parameters:
    `locations` -

    The list of locations used to calculate the route. Note that only the [`Location.coordinates`](sdk-for-android-explore-api-reference-latestlocation#coordinates) of a location are used to import the route.

    An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-api-reference-latestroutingerror#INVALID_PARAMETER) error is generated when the location list size is not in the range \[2,50000\].

    `routeStops` -

    The list of RouteStop's which contains index of location from locations list used for route stop and duration in seconds spent on stop.

    An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-api-reference-latestroutingerror#INVALID_PARAMETER) error is generated when the route stops list size is not in the range \[1,locations.size()-2\], any of location_index is \< 1 or location_indexes are not unique.

    `busOptions` -

    Options specific for bus route calculation, along with common route options.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### importRoute

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") importRoute(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Location](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core")\> locations, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[RouteStop](sdk-for-android-explore-api-reference-latestroutestop "class in com.here.sdk.routing")\> routeStops, @NonNull [PrivateBusOptions](sdk-for-android-explore-api-reference-latestprivatebusoptions "class in com.here.sdk.routing") privateBusOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Deprecated.
Will be removed in v4.28.0. Use the `import_route()` methods with RoutingOptions parameter instead.

Asynchronously creates a private bus route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or anyway geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.

    **Note:** Any restrictions applied to a transport type or provided options will be discarded and reported as violations in [`Section.getSectionNotices()`](sdk-for-android-explore-api-reference-latestsection#getSectionNotices()) .
Parameters:
    `locations` -

    The list of locations used to calculate the route. Note that only the [`Location.coordinates`](sdk-for-android-explore-api-reference-latestlocation#coordinates) of a location are used to import the route.

    An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-api-reference-latestroutingerror#INVALID_PARAMETER) error is generated when the location list size is not in the range \[2,50000\].

    `routeStops` -

    The list of RouteStop's which contains index of location from locations list used for route stop and duration in seconds spent on stop.

    An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-api-reference-latestroutingerror#INVALID_PARAMETER) error is generated when the route stops list size is not in the range \[1,locations.size()-2\], any of location_index is \< 1 or location_indexes are not unique.

    `privateBusOptions` -

    Options specific for private bus route calculation, along with common route options.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### importRoute

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") importRoute(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Location](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core")\> locations, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[RouteStop](sdk-for-android-explore-api-reference-latestroutestop "class in com.here.sdk.routing")\> routeStops, @NonNull [EVCarOptions](sdk-for-android-explore-api-reference-latestevcaroptions "class in com.here.sdk.routing") evCarOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Deprecated.
Will be removed in v4.28.0. Use the `import_route()` methods with RoutingOptions parameter instead.

Asynchronously creates an electric car route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.

    **Note:** Any restrictions applied to a transport type or provided options will be discarded and reported as violations in [`Section.getSectionNotices()`](sdk-for-android-explore-api-reference-latestsection#getSectionNotices()) .
Parameters:
    `locations` -

    The list of locations used to calculate the route. Note that only the [`Location.coordinates`](sdk-for-android-explore-api-reference-latestlocation#coordinates) of a location are used to import the route.

    An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-api-reference-latestroutingerror#INVALID_PARAMETER) error is generated when the location list size is not in the range \[2,50000\].

    `routeStops` -

    The list of RouteStop's which contains index of location from locations list used for route stop and duration in seconds spent on stop.

    An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-api-reference-latestroutingerror#INVALID_PARAMETER) error is generated when the route stops list size is not in the range \[1,locations.size()-2\], any of location_index is \< 1 or location_indexes are not unique.

    `evCarOptions` -

    Options specific for an electric car route calculation, along with common route options. **Note** An \[sdk.routing.RoutingError.INVALID_PARAMETER\] is generated when the \[sdk.routing.EVCarOptions.ensure_reachability\] option is set to `true`.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### importRoute

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") importRoute(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Location](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core")\> locations, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[RouteStop](sdk-for-android-explore-api-reference-latestroutestop "class in com.here.sdk.routing")\> routeStops, @NonNull [EVTruckOptions](sdk-for-android-explore-api-reference-latestevtruckoptions "class in com.here.sdk.routing") evTruckOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Deprecated.
Will be removed in v4.28.0. Use the `import_route()` methods with RoutingOptions parameter instead.

Asynchronously creates an electric truck route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.

    **Note:** Any restrictions applied to a transport type or provided options will be discarded and reported as violations in [`Section.getSectionNotices()`](sdk-for-android-explore-api-reference-latestsection#getSectionNotices()) .
Parameters:
    `locations` -

    The list of locations used to calculate the route. Note that only the [`Location.coordinates`](sdk-for-android-explore-api-reference-latestlocation#coordinates) of a location are used to import the route.

    An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-api-reference-latestroutingerror#INVALID_PARAMETER) error is generated when the location list size is not in the range \[2,50000\].

    `routeStops` -

    The list of RouteStop's which contains index of location from locations list used for route stop and duration in seconds spent on stop.

    An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-api-reference-latestroutingerror#INVALID_PARAMETER) error is generated when the route stops list size is not in the range \[1,locations.size()-2\], any of location_index is \< 1 or location_indexes are not unique.

    `evTruckOptions` -

    Options specific for an electric truck route calculation, along with common route options.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### importRoute

@NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") importRoute(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Location](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core")\> locations, @NonNull [RoutingOptions](sdk-for-android-explore-api-reference-latestroutingoptions "class in com.here.sdk.routing") options, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Asynchronously creates a route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.

    **Note:** Any restrictions applied to a transport type or provided options will be discarded and reported as violations in [`Section.getSectionNotices()`](sdk-for-android-explore-api-reference-latestsection#getSectionNotices()).
Parameters:
    `locations` -

    The list of locations used to calculate the route. Note that only the [`Location.coordinates`](sdk-for-android-explore-api-reference-latestlocation#coordinates) of a location are used to import the route.

    An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-api-reference-latestroutingerror#INVALID_PARAMETER) error is generated when the location list size is not in the range \[2,50000\].

    `options` -

    The options define the vehicle and route options to calculate the route.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### importRoute

@NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") importRoute(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Location](sdk-for-android-explore-api-reference-latestlocation "class in com.here.sdk.core")\> locations, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[RouteStop](sdk-for-android-explore-api-reference-latestroutestop "class in com.here.sdk.routing")\> routeStops, @NonNull [RoutingOptions](sdk-for-android-explore-api-reference-latestroutingoptions "class in com.here.sdk.routing") options, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Asynchronously creates a route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.

    **Note:** Any restrictions applied to a transport type or provided options will be discarded and reported as violations in [`Section.getSectionNotices()`](sdk-for-android-explore-api-reference-latestsection#getSectionNotices()) .
Parameters:
    `locations` -

    The list of locations used to calculate the route. Note that only the [`Location.coordinates`](sdk-for-android-explore-api-reference-latestlocation#coordinates) of a location are used to import the route.

    An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-api-reference-latestroutingerror#INVALID_PARAMETER) error is generated when the location list size is not in the range \[2,50000\].

    `routeStops` -

    The list of RouteStop's which contains index of location from locations list used for route stop and duration in seconds spent on stop.

    An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-api-reference-latestroutingerror#INVALID_PARAMETER) error is generated when the route stops list size is not in the range \[1,locations.size()-2\], any of location_index is \< 1 or location_indexes are not unique.

    `options` -

    The options define the vehicle and route options to calculate the route.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### importRoute

@NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") importRoute(@NonNull [RouteHandle](sdk-for-android-explore-api-reference-latestroutehandle "class in com.here.sdk.routing") routeHandle, @NonNull [RoutingOptions](sdk-for-android-explore-api-reference-latestroutingoptions "class in com.here.sdk.routing") options, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Asynchronously recreates a route from the [`RouteHandle`](sdk-for-android-explore-api-reference-latestroutehandle "class in com.here.sdk.routing") provided, i.e. refreshes a previously calculated route, with the specified [`RoutingOptions`](sdk-for-android-explore-api-reference-latestroutingoptions "class in com.here.sdk.routing").

    A route handle can be invalid when the map data changes that is used by the HERE sdk to recreate the route. This happens regularly. Therefore, the route handle is not meant to be persisted for a longer time.
Parameters:
    `routeHandle` -

    The route handle holding the route to be refreshed.

    `options` -

    The options define the vehicle and route options to calculate the route.

    `callback` -

    Callback object that will be invoked after refreshing the route. It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### calculateTrafficOnRoute

@NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") calculateTrafficOnRoute(@NonNull [Route](sdk-for-android-explore-api-reference-latestroute "class in com.here.sdk.routing") route, int lastTraveledSectionIndex, int traveledDistanceOnLastSectionInMeters, @NonNull [CalculateTrafficOnRouteCallback](sdk-for-android-explore-api-reference-latestcalculatetrafficonroutecallback "interface in com.here.sdk.routing") callback)

    Asynchronously calculates the traffic along a route starting from the index of the last traveled route section and an offset (in meters) from the last visited position on the section. Call this when only the contained traffic information or the latest ETA duration is needed. This can be called periodically to retrieve updated ETA values during navigation.

    **Note:** Calling this method will trigger a new "HERE Traffic" transaction, for example, if you are using the [Base Plan](https://www.here.com/get-started/pricing).
Parameters:
    `route` -

    A [`Route`](sdk-for-android-explore-api-reference-latestroute "class in com.here.sdk.routing") calculated using the online routing engine. Its [`RouteHandle`](sdk-for-android-explore-api-reference-latestroutehandle "class in com.here.sdk.routing") and the original route calculation options will be used to compute the traffic on the route. The original route remains untouched.

    `lastTraveledSectionIndex` -

    Indicates the index of the last traveled route section. Traveled part of the route won't be reused.

    `traveledDistanceOnLastSectionInMeters` -

    Offset, in meters, to the last visited position on the route section defined by the last traveled section index.

    `callback` -

    Callback object that will be invoked after route traffic has been calculated. It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### calculateTrafficOnRoute

@NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") calculateTrafficOnRoute(@NonNull [Route](sdk-for-android-explore-api-reference-latestroute "class in com.here.sdk.routing") route, int lastTraveledSectionIndex, int traveledDistanceOnLastSectionInMeters, double currentChargeInKilowattHours, @NonNull [CalculateTrafficOnRouteCallback](sdk-for-android-explore-api-reference-latestcalculatetrafficonroutecallback "interface in com.here.sdk.routing") callback)

    Asynchronously calculates the traffic along an EV car route starting from the index of the last traveled route section and an offset in meters from the last visited position on the section. The field [`TrafficOnSpan.consumptionInKilowattHours`](sdk-for-android-explore-api-reference-latesttrafficonspan#consumptionInKilowattHours) will contain the power consumption in kilowatt-hours (kWh) necessary to traverse the span, and [`RoutePlace.chargeInKilowattHours`](sdk-for-android-explore-api-reference-latestrouteplace#chargeInKilowattHours), inside [`TrafficOnSection.departurePlace`](sdk-for-android-explore-api-reference-latesttrafficonsection#departurePlace) and [`TrafficOnSection.arrivalPlace`](sdk-for-android-explore-api-reference-latesttrafficonsection#arrivalPlace), the estimated battery charge in kilowatt-hours (kWh) when leaving/arriving to a section. **Note:** Only EV cars are supported.
Parameters:
    `route` -

    A [`Route`](sdk-for-android-explore-api-reference-latestroute "class in com.here.sdk.routing") calculated using the online routing engine. Its [`RouteHandle`](sdk-for-android-explore-api-reference-latestroutehandle "class in com.here.sdk.routing") and the original route calculation options, along with EV related information like [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing"), will be used to compute the traffic on the route. The original route remains untouched.

    `lastTraveledSectionIndex` -

    Indicates the index of the last traveled route section. Traveled part of the route won't be reused.

    `traveledDistanceOnLastSectionInMeters` -

    Offset, in meters, to the last visited position on the route section defined by the last traveled section index.

    `currentChargeInKilowattHours` -

    Charge level of the vehicle's battery at the current location (in kWh). It must be non-negative and less than or equal to the value of [`BatterySpecifications.totalCapacityInKilowattHours`](sdk-for-android-explore-api-reference-latestbatteryspecifications#totalCapacityInKilowattHours), otherwise the [`BatterySpecifications`](sdk-for-android-explore-api-reference-latestbatteryspecifications "class in com.here.sdk.routing") instance is considered invalid. Sets [`BatterySpecifications.initialChargeInKilowattHours`](sdk-for-android-explore-api-reference-latestbatteryspecifications#initialChargeInKilowattHours) to the given value.

    `callback` -

    Callback object that will be invoked after route traffic has been calculated. It is always invoked on the main thread.

    Returns:
    Handle that will be used to manipulate the execution of the task.

### setCustomOption

@Nullable public [RoutingError](sdk-for-android-explore-api-reference-latestroutingerror "enum class in com.here.sdk.routing") setCustomOption(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name, @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) value)

    Sets a custom option for routing backend queries. The custom option is applied to all the queries that `RoutingEngine` performs. For a complete list of available parameter names and their valid values, refer to [HERE Routing API v8](https://www.here.com/docs/bundle/routing-api-v8-api-reference/page/index.html). **Note:** It's easy to set a wrong option that makes queries invalid, so make sure you read and understand the backend documentation.
Parameters:
    `name` -

    An option name. If the engine already has an option with the same name, the option will be overwritten. The option name must be a non-empty string.

    `value` -

    An option value. If the value is `null`, the option will be removed. The option value must be a non-empty string.

    Returns:
    An optional error of setting the option. It's `null` if the option has been set successfully. It's `RoutingError.INVALID_PARAMETER` if the input name and/or value haven't passed internal validation.

### calculateRoute

@NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") calculateRoute(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Waypoint](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing")\> waypoints, @NonNull [RoutingOptions](sdk-for-android-explore-api-reference-latestroutingoptions "class in com.here.sdk.routing") options, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Asynchronously calculates a route from one point to another, passing through the given waypoints in the given order.
Specified by:
    [`calculateRoute`](sdk-for-android-explore-api-reference-latestroutinginterface#calculateRoute(java.util.List,com.here.sdk.routing.RoutingOptions,com.here.sdk.routing.CalculateRouteCallback)) in interface [`RoutingInterface`](sdk-for-android-explore-api-reference-latestroutinginterface "interface in com.here.sdk.routing")

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

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") calculateRoute(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Waypoint](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing")\> waypoints, @NonNull [CarOptions](sdk-for-android-explore-api-reference-latestcaroptions "class in com.here.sdk.routing") carOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Deprecated.
Will be removed in v4.28.0. Use the `calculate_route()` methods with RoutingOptions parameter instead.

Asynchronously calculates a car route from one point to another, passing through the given waypoints in the given order.
Specified by:
    [`calculateRoute`](sdk-for-android-explore-api-reference-latestroutinginterface#calculateRoute(java.util.List,com.here.sdk.routing.CarOptions,com.here.sdk.routing.CalculateRouteCallback)) in interface [`RoutingInterface`](sdk-for-android-explore-api-reference-latestroutinginterface "interface in com.here.sdk.routing")

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

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") calculateRoute(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Waypoint](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing")\> waypoints, @NonNull [PedestrianOptions](sdk-for-android-explore-api-reference-latestpedestrianoptions "class in com.here.sdk.routing") pedestrianOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Deprecated.
Will be removed in v4.28.0. Use the `calculate_route()` methods with RoutingOptions parameter instead.

Asynchronously calculates a pedestrian route from one point to another, passing through the given waypoints in the given order.
Specified by:
    [`calculateRoute`](sdk-for-android-explore-api-reference-latestroutinginterface#calculateRoute(java.util.List,com.here.sdk.routing.PedestrianOptions,com.here.sdk.routing.CalculateRouteCallback)) in interface [`RoutingInterface`](sdk-for-android-explore-api-reference-latestroutinginterface "interface in com.here.sdk.routing")

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

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") calculateRoute(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Waypoint](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing")\> waypoints, @NonNull [TruckOptions](sdk-for-android-explore-api-reference-latesttruckoptions "class in com.here.sdk.routing") truckOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Deprecated.
Will be removed in v4.28.0. Use the `calculate_route()` methods with RoutingOptions parameter instead.

Asynchronously calculates a truck route from one point to another, passing through the given waypoints in the given order.
Specified by:
    [`calculateRoute`](sdk-for-android-explore-api-reference-latestroutinginterface#calculateRoute(java.util.List,com.here.sdk.routing.TruckOptions,com.here.sdk.routing.CalculateRouteCallback)) in interface [`RoutingInterface`](sdk-for-android-explore-api-reference-latestroutinginterface "interface in com.here.sdk.routing")

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

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") calculateRoute(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Waypoint](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing")\> waypoints, @NonNull [ScooterOptions](sdk-for-android-explore-api-reference-latestscooteroptions "class in com.here.sdk.routing") scooterOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Deprecated.
Will be removed in v4.28.0. Use the `calculate_route()` methods with RoutingOptions parameter instead.

Asynchronously calculates a scooter route from one point to another, passing through the given waypoints in the given order.
Specified by:
    [`calculateRoute`](sdk-for-android-explore-api-reference-latestroutinginterface#calculateRoute(java.util.List,com.here.sdk.routing.ScooterOptions,com.here.sdk.routing.CalculateRouteCallback)) in interface [`RoutingInterface`](sdk-for-android-explore-api-reference-latestroutinginterface "interface in com.here.sdk.routing")

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

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") calculateRoute(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Waypoint](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing")\> waypoints, @NonNull [BicycleOptions](sdk-for-android-explore-api-reference-latestbicycleoptions "class in com.here.sdk.routing") bicycleOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Deprecated.
Will be removed in v4.28.0. Use the `calculate_route()` methods with RoutingOptions parameter instead.

Asynchronously calculates a bicycle route from one point to another, passing through the given waypoints in the given order.
Specified by:
    [`calculateRoute`](sdk-for-android-explore-api-reference-latestroutinginterface#calculateRoute(java.util.List,com.here.sdk.routing.BicycleOptions,com.here.sdk.routing.CalculateRouteCallback)) in interface [`RoutingInterface`](sdk-for-android-explore-api-reference-latestroutinginterface "interface in com.here.sdk.routing")

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

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") calculateRoute(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Waypoint](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing")\> waypoints, @NonNull [TaxiOptions](sdk-for-android-explore-api-reference-latesttaxioptions "class in com.here.sdk.routing") taxiOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Deprecated.
Will be removed in v4.28.0. Use the `calculate_route()` methods with RoutingOptions parameter instead.

Asynchronously calculates a taxi route from one point to another, passing through the given waypoints in the given order.
Specified by:
    [`calculateRoute`](sdk-for-android-explore-api-reference-latestroutinginterface#calculateRoute(java.util.List,com.here.sdk.routing.TaxiOptions,com.here.sdk.routing.CalculateRouteCallback)) in interface [`RoutingInterface`](sdk-for-android-explore-api-reference-latestroutinginterface "interface in com.here.sdk.routing")

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

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") calculateRoute(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Waypoint](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing")\> waypoints, @NonNull [EVCarOptions](sdk-for-android-explore-api-reference-latestevcaroptions "class in com.here.sdk.routing") evCarOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Deprecated.
Will be removed in v4.28.0. Use the `calculate_route()` methods with RoutingOptions parameter instead.

Asynchronously calculates an electric car route from one point to another, passing through the given waypoints in the given order.
Specified by:
    [`calculateRoute`](sdk-for-android-explore-api-reference-latestroutinginterface#calculateRoute(java.util.List,com.here.sdk.routing.EVCarOptions,com.here.sdk.routing.CalculateRouteCallback)) in interface [`RoutingInterface`](sdk-for-android-explore-api-reference-latestroutinginterface "interface in com.here.sdk.routing")

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

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") calculateRoute(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Waypoint](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing")\> waypoints, @NonNull [EVTruckOptions](sdk-for-android-explore-api-reference-latestevtruckoptions "class in com.here.sdk.routing") evTruckOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Deprecated.
Will be removed in v4.28.0. Use the `calculate_route()` methods with RoutingOptions parameter instead.

Asynchronously calculates an electic truck route from one point to another, passing through the given waypoints in the given order.
Specified by:
    [`calculateRoute`](sdk-for-android-explore-api-reference-latestroutinginterface#calculateRoute(java.util.List,com.here.sdk.routing.EVTruckOptions,com.here.sdk.routing.CalculateRouteCallback)) in interface [`RoutingInterface`](sdk-for-android-explore-api-reference-latestroutinginterface "interface in com.here.sdk.routing")

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

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") calculateRoute(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Waypoint](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing")\> waypoints, @NonNull [BusOptions](sdk-for-android-explore-api-reference-latestbusoptions "class in com.here.sdk.routing") busOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Deprecated.
Will be removed in v4.28.0. Use the `calculate_route()` methods with RoutingOptions parameter instead.

Asynchronously calculates a bus route from one point to another, passing through the given waypoints in the given order.
Specified by:
    [`calculateRoute`](sdk-for-android-explore-api-reference-latestroutinginterface#calculateRoute(java.util.List,com.here.sdk.routing.BusOptions,com.here.sdk.routing.CalculateRouteCallback)) in interface [`RoutingInterface`](sdk-for-android-explore-api-reference-latestroutinginterface "interface in com.here.sdk.routing")

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

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html) @NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") calculateRoute(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Waypoint](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing")\> waypoints, @NonNull [PrivateBusOptions](sdk-for-android-explore-api-reference-latestprivatebusoptions "class in com.here.sdk.routing") privateBusOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Deprecated.
Will be removed in v4.28.0. Use the `calculate_route()` methods with RoutingOptions parameter instead.

Asynchronously calculates a private bus route from one point to another, passing through the given waypoints in the given order.
Specified by:
    [`calculateRoute`](sdk-for-android-explore-api-reference-latestroutinginterface#calculateRoute(java.util.List,com.here.sdk.routing.PrivateBusOptions,com.here.sdk.routing.CalculateRouteCallback)) in interface [`RoutingInterface`](sdk-for-android-explore-api-reference-latestroutinginterface "interface in com.here.sdk.routing")

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

@NonNull public [TaskHandle](sdk-for-android-explore-api-reference-latesttaskhandle "interface in com.here.sdk.core.threading") returnToRoute(@NonNull [Route](sdk-for-android-explore-api-reference-latestroute "class in com.here.sdk.routing") route, @NonNull [Waypoint](sdk-for-android-explore-api-reference-latestwaypoint "class in com.here.sdk.routing") startingPoint, int lastTraveledSectionIndex, int traveledDistanceOnLastSectionInMeters, @NonNull [CalculateRouteCallback](sdk-for-android-explore-api-reference-latestcalculateroutecallback "interface in com.here.sdk.routing") callback)

    Asynchronously calculates a new route that leads back to the original route. The part of the original route which was already traveled by the user is ignored.

    **Note:** Stopover waypoints are guaranteed to be visited. Pass-through waypoints will be ignored. Additionally, the following route options are ignored: [`RouteOptions.alternatives`](sdk-for-android-explore-api-reference-latestrouteoptions#alternatives), [`RouteOptions.arrivalTime`](sdk-for-android-explore-api-reference-latestrouteoptions#arrivalTime), and [`RouteOptions.optimizationMode`](sdk-for-android-explore-api-reference-latestrouteoptions#optimizationMode). Most route options are only applied to the newly calculated part back to the route.

    An application may use this method to submit a new starting point for a previously calculated route. This method tries to avoid a costly route re-calculation as much as possible. In case returning to the route without re-calculation is not possible, a new route is calculated, while trying to salvage the previous route as much as possible. However, a completely new route containing no part of the previous route is possible, too.

    Note that this function uses only a limited amount of map data around the new origin. Therefore, it may also work fine with temporarily cached map data. It may also copy some of the original route data into the new route.

    A typical use case is to await at least 3 `RouteDeviation` events before calling this method.

    - Or alternatively, wait at least 10 seconds after getting the first deviation event.
    - On top, the user experience can be improved by checking if the vehicle has moved at least 50 meters since calling this method for the last time.
    - Optionally, it may make sense to verify if the vehicle was ever following the route by checking if `RouteDeviation.lastLocationOnRoute` is set.

    Note that deviation events are sent each time a deviation is detected, i.e. for each new location update, regardless if the location has changed or not. More information can be found in the Developer Guide in the "Handle route deviations" section.
Specified by:
    [`returnToRoute`](sdk-for-android-explore-api-reference-latestroutinginterface#returnToRoute(com.here.sdk.routing.Route,com.here.sdk.routing.Waypoint,int,int,com.here.sdk.routing.CalculateRouteCallback)) in interface [`RoutingInterface`](sdk-for-android-explore-api-reference-latestroutinginterface "interface in com.here.sdk.routing")

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

public void dispose()

    Cancels pending requests and closes the background worker thread. **Note:** This method should be called from main thread.
Specified by:
    [`dispose`](sdk-for-android-explore-api-reference-latestroutinginterface#dispose()) in interface [`RoutingInterface`](sdk-for-android-explore-api-reference-latestroutinginterface "interface in com.here.sdk.routing")
