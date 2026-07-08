---
title: "RoutingEngine (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-routingengine"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.routing](sdk-for-android-explore-com-here-sdk-routing-package-summary)

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.routing.RoutingEngine → com.here.NativeBase com.here.sdk.routing.RoutingEngine → com.here.sdk.routing.RoutingEngine

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

All Implemented Interfaces:  
[`RoutingInterface`](sdk-for-android-explore-com-here-sdk-routing-routinginterface "interface in com.here.sdk.routing")

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">RoutingEngine</span> <span class="extends-implements">extends [NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here") implements [RoutingInterface](sdk-for-android-explore-com-here-sdk-routing-routinginterface "interface in com.here.sdk.routing")</span>

</div>

<div class="block">

Use the RoutingEngine to calculate a route from A to B with a number of waypoints in between. Route calculation is done asynchronously and requires an online connection. The resulting route contains various information such as the polyline, route length in meters, estimated time to traverse along the route and maneuver data. Note: The engine does not support an unlimited number of waypoints. The limit is defined by the HERE backend services and may change. For now, the maximum number of waypoints should be below 200. This value may change and it is not guaranteed to be stable. If you need to support very large lists of waypoints, consider to import a route (see importRoute() method) or use the OfflineRoutingEngine which supports an unlimited number of waypoints. The OfflineRoutingEngine is only available for Navigate licence.

</div>

</div>

- <div id="sdk-for-android-explore-constructor-summary" class="section constructor-summary">

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

      RoutingEngine ()

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance of this class.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      RoutingEngine ( SDKNativeEngine sdkEngine)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new instance of RoutingEngine.

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      RoutingEngine ( SDKNativeEngine sdkEngine, RoutingConnectionSettings connectionSettings)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance of RoutingEngine.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      RoutingEngine ( RoutingConnectionSettings connectionSettings)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new instance of RoutingEngine.

  </div>

  </div>

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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

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

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

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

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

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

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

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

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

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

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

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

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

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

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

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

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

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

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

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

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

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

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      calculateTrafficOnRoute ( Route route,
       int lastTraveledSectionIndex,
       int traveledDistanceOnLastSectionInMeters,
       double currentChargeInKilowattHours, CalculateTrafficOnRouteCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Asynchronously calculates the traffic along an EV car route starting from the index of the last traveled route section and an offset in meters from the last visited position on the section.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      calculateTrafficOnRoute ( Route route,
       int lastTraveledSectionIndex,
       int traveledDistanceOnLastSectionInMeters, CalculateTrafficOnRouteCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Asynchronously calculates the traffic along a route starting from the index of the last traveled route section and an offset (in meters) from the last visited position on the section.

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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

      importRoute ( RouteHandle routeHandle, RefreshRouteOptions refreshRouteOptions, CalculateRouteCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      importRoute ( RouteHandle routeHandle, RoutingOptions options, CalculateRouteCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Asynchronously recreates a route from the RouteHandle provided, i.e.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

      importRoute ( List < Location > locations, BicycleOptions bicycleOptions, CalculateRouteCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

      importRoute ( List < Location > locations, BusOptions busOptions, CalculateRouteCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

      importRoute ( List < Location > locations, CarOptions carOptions, CalculateRouteCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

      importRoute ( List < Location > locations, EVCarOptions evCarOptions, CalculateRouteCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

      importRoute ( List < Location > locations, EVTruckOptions evTruckOptions, CalculateRouteCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

      importRoute ( List < Location > locations, PedestrianOptions pedestrianOptions, CalculateRouteCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

      importRoute ( List < Location > locations, PrivateBusOptions privateBusOptions, CalculateRouteCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      importRoute ( List < Location > locations, RoutingOptions options, CalculateRouteCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Asynchronously creates a route from a sequence of geographic coordinates very close to each other.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

      importRoute ( List < Location > locations, ScooterOptions scooterOptions, CalculateRouteCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

      importRoute ( List < Location > locations, TaxiOptions taxiOptions, CalculateRouteCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

      importRoute ( List < Location > locations, TruckOptions truckOptions, CalculateRouteCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

      importRoute ( List < Location > locations, List < RouteStop > routeStops, BicycleOptions bicycleOptions, CalculateRouteCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

      importRoute ( List < Location > locations, List < RouteStop > routeStops, BusOptions busOptions, CalculateRouteCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

      importRoute ( List < Location > locations, List < RouteStop > routeStops, CarOptions carOptions, CalculateRouteCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

      importRoute ( List < Location > locations, List < RouteStop > routeStops, EVCarOptions evCarOptions, CalculateRouteCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

      importRoute ( List < Location > locations, List < RouteStop > routeStops, EVTruckOptions evTruckOptions, CalculateRouteCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

      importRoute ( List < Location > locations, List < RouteStop > routeStops, PedestrianOptions pedestrianOptions, CalculateRouteCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

      importRoute ( List < Location > locations, List < RouteStop > routeStops, PrivateBusOptions privateBusOptions, CalculateRouteCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      importRoute ( List < Location > locations, List < RouteStop > routeStops, RoutingOptions options, CalculateRouteCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Asynchronously creates a route from a sequence of geographic coordinates very close to each other.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

      importRoute ( List < Location > locations, List < RouteStop > routeStops, ScooterOptions scooterOptions, CalculateRouteCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

      importRoute ( List < Location > locations, List < RouteStop > routeStops, TaxiOptions taxiOptions, CalculateRouteCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

      importRoute ( List < Location > locations, List < RouteStop > routeStops, TruckOptions truckOptions, CalculateRouteCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      refreshRoute ( RefreshRouteParameters refreshRouteParameters, RoutingOptions routingOptions, CalculateRouteCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Asynchronously refreshes a previously calculated route from the provided RouteHandle , updating the starting point and route metadata based on RoutingOptions .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

      refreshRoute ( RouteHandle routeHandle, Waypoint startingPoint, RefreshRouteOptions refreshRouteOptions, CalculateRouteCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

      refreshRoute ( RouteHandle routeHandle, Waypoint startingPoint, RoutingOptions options, CalculateRouteCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

      refreshRoute ( RouteHandle routeHandle, Waypoint startingPoint, Integer lastTraveledSectionIndex, Integer traveledDistanceOnLastSectionInMeters, RefreshRouteOptions refreshRouteOptions, CalculateRouteCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

      refreshRoute ( RouteHandle routeHandle, Waypoint startingPoint, Integer lastTraveledSectionIndex, Integer traveledDistanceOnLastSectionInMeters, RoutingOptions options, CalculateRouteCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated. Will be removed in v4.28.0.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      returnToRoute ( Route route, Waypoint startingPoint,
       int lastTraveledSectionIndex,
       int traveledDistanceOnLastSectionInMeters, CalculateRouteCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Asynchronously calculates a new route that leads back to the original route.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`RoutingError`](sdk-for-android-explore-com-here-sdk-routing-routingerror "enum class in com.here.sdk.routing")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setCustomOption ( String name, String value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets a custom option for routing backend queries.

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

- <div id="sdk-for-android-explore-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-explore-init" class="section detail">

    ### RoutingEngine

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RoutingEngine</span>() throws <span class="exceptions">[InstantiationErrorException](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors")</span>

    </div>

    <div class="block">

    Creates a new instance of this class.

    </div>

    Throws:  
    [`InstantiationErrorException`](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors") -

    Indicates what went wrong when the instantiation was attempted.

    </div>

  - <div id="sdk-for-android-explore-init-com-here-sdk-core-engine-SDKNativeEngine" class="section detail">

    ### RoutingEngine

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RoutingEngine</span><wbr></wbr><span class="parameters">(@NonNull [SDKNativeEngine](sdk-for-android-explore-com-here-sdk-core-engine-sdknativeengine "class in com.here.sdk.core.engine") sdkEngine)</span> throws <span class="exceptions">[InstantiationErrorException](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors")</span>

    </div>

    <div class="block">

    Creates a new instance of RoutingEngine.

    </div>

    Parameters:  
    `sdkEngine` -

    An SDKEngine instance.

    Throws:  
    [`InstantiationErrorException`](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors") -

    Indicates what went wrong when the instantiation was attempted.

    </div>

  - <div id="sdk-for-android-explore-init-com-here-sdk-routing-RoutingConnectionSettings" class="section detail">

    ### RoutingEngine

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RoutingEngine</span><wbr></wbr><span class="parameters">(@NonNull [RoutingConnectionSettings](sdk-for-android-explore-com-here-sdk-routing-routingconnectionsettings "class in com.here.sdk.routing") connectionSettings)</span> throws <span class="exceptions">[InstantiationErrorException](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors")</span>

    </div>

    <div class="block">

    Creates a new instance of RoutingEngine.

    </div>

    Parameters:  
    `connectionSettings` -

    Settings for the route calculation.

    Throws:  
    [`InstantiationErrorException`](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors") -

    Indicates what went wrong when the instantiation was attempted.

    </div>

  - <div id="sdk-for-android-explore-init-com-here-sdk-core-engine-SDKNativeEngine-com-here-sdk-routing-RoutingConnectionSettings" class="section detail">

    ### RoutingEngine

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RoutingEngine</span><wbr></wbr><span class="parameters">(@NonNull [SDKNativeEngine](sdk-for-android-explore-com-here-sdk-core-engine-sdknativeengine "class in com.here.sdk.core.engine") sdkEngine, @NonNull [RoutingConnectionSettings](sdk-for-android-explore-com-here-sdk-routing-routingconnectionsettings "class in com.here.sdk.routing") connectionSettings)</span> throws <span class="exceptions">[InstantiationErrorException](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors")</span>

    </div>

    <div class="block">

    Creates a new instance of RoutingEngine.

    </div>

    Parameters:  
    `sdkEngine` -

    An SDKEngine instance.

    `connectionSettings` -

    Settings for the route calculation.

    Throws:  
    [`InstantiationErrorException`](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors") -

    Indicates what went wrong when the instantiation was attempted.

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail" class="section method-details">

  - <div id="sdk-for-android-explore-refreshRoute-com-here-sdk-routing-RouteHandle-com-here-sdk-routing-Waypoint-com-here-sdk-routing-RefreshRouteOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### refreshRoute

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">refreshRoute</span><wbr></wbr><span class="parameters">(@NonNull [RouteHandle](sdk-for-android-explore-com-here-sdk-routing-routehandle "class in com.here.sdk.routing") routeHandle, @NonNull [Waypoint](sdk-for-android-explore-com-here-sdk-routing-waypoint "class in com.here.sdk.routing") startingPoint, @NonNull [RefreshRouteOptions](sdk-for-android-explore-com-here-sdk-routing-refreshrouteoptions "class in com.here.sdk.routing") refreshRouteOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use the

        refresh_route()

    methods with RoutingOptions parameter instead.
    </p>

    </div>

    </div>

    <div class="block">

    Asynchronously refreshes a previously calculated route from the provided RouteHandle , updating the starting point and route metadata based on RefreshRouteOptions . The route shape from the new starting point to the destination remains unchanged, and only metadata such as arrival time and traffic delays are updated. If you only want to refresh the contained traffic information or retrieve updated ETA duration, consider using calculateTrafficOnRoute(Route, int, int, double, CalculateTrafficOnRouteCallback) instead. Calling this method will trigger a new "HERE Routing" transaction, for example, if you are using the Base Plan .

    </div>

    Parameters:  
    `routeHandle` -

    The route handle holding the route to be refreshed.

    `startingPoint` -

    Updates the starting point of the route. It should be of type [`WaypointType.STOPOVER`](sdk-for-android-explore-com-here-sdk-routing-waypointtype#STOPOVER). Otherwise, an [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-com-here-sdk-routing-routingerror#INVALID_PARAMETER) error is generated. Moreover, it should be very close to the original route specified with the [`RouteHandle`](sdk-for-android-explore-com-here-sdk-routing-routehandle "class in com.here.sdk.routing"). Since the new starting point is expected to be along the original route, the original route geometry is used to reach the remaining waypoints. The new route will not include the [`Waypoint`](sdk-for-android-explore-com-here-sdk-routing-waypoint "class in com.here.sdk.routing") items that lie behind the new starting point (i.e. the path that was already travelled). Plus, [](sdk-for-android-explore-com-here-sdk-routing-route#getLengthInMeters())

        Route.getLengthInMeters()

    </a> and [](sdk-for-android-explore-com-here-sdk-routing-route#getDuration())

        Route.getDuration()

    </a> values are from the new starting point to the destination. If the new waypoint is too far off the original route, the route refresh may fail and an [`RoutingError.COULD_NOT_MATCH_ORIGIN`](sdk-for-android-explore-com-here-sdk-routing-routingerror#COULD_NOT_MATCH_ORIGIN) error is triggered. In that case, an application may decide to calculate a new route from scratch.

    </p>

    `refreshRouteOptions` -

    Options to refresh the route.

    `callback` -

    Callback object that will be invoked after refreshing the route. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-explore-refreshRoute-com-here-sdk-routing-RouteHandle-com-here-sdk-routing-Waypoint-java-lang-Integer-java-lang-Integer-com-here-sdk-routing-RefreshRouteOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### refreshRoute

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">refreshRoute</span><wbr></wbr><span class="parameters">(@NonNull [RouteHandle](sdk-for-android-explore-com-here-sdk-routing-routehandle "class in com.here.sdk.routing") routeHandle, @Nullable [Waypoint](sdk-for-android-explore-com-here-sdk-routing-waypoint "class in com.here.sdk.routing") startingPoint, @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang">Integer</a> lastTraveledSectionIndex, @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang">Integer</a> traveledDistanceOnLastSectionInMeters, @NonNull [RefreshRouteOptions](sdk-for-android-explore-com-here-sdk-routing-refreshrouteoptions "class in com.here.sdk.routing") refreshRouteOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use the

        refresh_route()

    methods with RoutingOptions parameter instead.
    </p>

    </div>

    </div>

    <div class="block">

    Asynchronously refreshes a previously calculated route from the provided RouteHandle , updating the starting point and route metadata based on RefreshRouteOptions . The route shape from the new starting point to the destination remains unchanged, and only metadata such as arrival time and traffic delays are updated. If you only want to refresh the contained traffic information, consider to use calculateTrafficOnRoute(Route, int, int, double, CalculateTrafficOnRouteCallback) instead. Calling this method will trigger a new "HERE Routing" transaction, for example, if you are using the Base Plan .

    </div>

    Parameters:  
    `routeHandle` -

    The route handle holding the route to be refreshed.

    `startingPoint` -

    Updates the starting point of the route. It should be of type [`WaypointType.STOPOVER`](sdk-for-android-explore-com-here-sdk-routing-waypointtype#STOPOVER). Otherwise, an [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-com-here-sdk-routing-routingerror#INVALID_PARAMETER) error is generated. Moreover, it should be very close to the original route specified with the [`RouteHandle`](sdk-for-android-explore-com-here-sdk-routing-routehandle "class in com.here.sdk.routing"). Since the new starting point is expected to be along the original route, the original route geometry is used to reach the remaining waypoints. The new route will not include the [`Waypoint`](sdk-for-android-explore-com-here-sdk-routing-waypoint "class in com.here.sdk.routing") items that lie behind the new starting point (i.e. the path that was already travelled). Plus, [](sdk-for-android-explore-com-here-sdk-routing-route#getLengthInMeters())

        Route.getLengthInMeters()

    </a> and [](sdk-for-android-explore-com-here-sdk-routing-route#getDuration())

        Route.getDuration()

    </a> values are from the new starting point to the destination. If the new waypoint is too far off the original route, the route refresh may fail and an [`RoutingError.COULD_NOT_MATCH_ORIGIN`](sdk-for-android-explore-com-here-sdk-routing-routingerror#COULD_NOT_MATCH_ORIGIN) error is triggered. In that case, an application may decide to calculate a new route from scratch.

    </p>

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

    </div>

  - <div id="sdk-for-android-explore-refreshRoute-com-here-sdk-routing-RouteHandle-com-here-sdk-routing-Waypoint-java-lang-Integer-java-lang-Integer-com-here-sdk-routing-RoutingOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### refreshRoute

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">refreshRoute</span><wbr></wbr><span class="parameters">(@NonNull [RouteHandle](sdk-for-android-explore-com-here-sdk-routing-routehandle "class in com.here.sdk.routing") routeHandle, @Nullable [Waypoint](sdk-for-android-explore-com-here-sdk-routing-waypoint "class in com.here.sdk.routing") startingPoint, @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang">Integer</a> lastTraveledSectionIndex, @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" class="external-link" title="class or interface in java.lang">Integer</a> traveledDistanceOnLastSectionInMeters, @NonNull [RoutingOptions](sdk-for-android-explore-com-here-sdk-routing-routingoptions "class in com.here.sdk.routing") options, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use the

        refresh_route()

    methods with RefreshRouteParameters parameter instead.
    </p>

    </div>

    </div>

    <div class="block">

    Asynchronously refreshes a previously calculated route from the provided RouteHandle , updating the starting point and route metadata based on RoutingOptions . The route shape from the new starting point to the destination remains unchanged, and only metadata such as arrival time and traffic delays are updated. If you only want to refresh the contained traffic information, consider to use calculateTrafficOnRoute(Route, int, int, double, CalculateTrafficOnRouteCallback) instead. Calling this method will trigger a new "HERE Routing" transaction, for example, if you are using the Base Plan .

    </div>

    Parameters:  
    `routeHandle` -

    The route handle holding the route to be refreshed.

    `startingPoint` -

    Updates the starting point of the route. It should be of type [`WaypointType.STOPOVER`](sdk-for-android-explore-com-here-sdk-routing-waypointtype#STOPOVER). Otherwise, an [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-com-here-sdk-routing-routingerror#INVALID_PARAMETER) error is generated. Moreover, it should be very close to the original route specified with the [`RouteHandle`](sdk-for-android-explore-com-here-sdk-routing-routehandle "class in com.here.sdk.routing"). Since the new starting point is expected to be along the original route, the original route geometry is used to reach the remaining waypoints. The new route will not include the [`Waypoint`](sdk-for-android-explore-com-here-sdk-routing-waypoint "class in com.here.sdk.routing") items that lie behind the new starting point (i.e. the path that was already traveled). Plus, [](sdk-for-android-explore-com-here-sdk-routing-route#getLengthInMeters())

        Route.getLengthInMeters()

    </a> and [](sdk-for-android-explore-com-here-sdk-routing-route#getDuration())

        Route.getDuration()

    </a> values are from the new starting point to the destination. If the new waypoint is too far off the original route, the route refresh may fail and an [`RoutingError.COULD_NOT_MATCH_ORIGIN`](sdk-for-android-explore-com-here-sdk-routing-routingerror#COULD_NOT_MATCH_ORIGIN) error is triggered. In that case, an application may decide to calculate a new route from scratch.

    </p>

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

    </div>

  - <div id="sdk-for-android-explore-refreshRoute-com-here-sdk-routing-RouteHandle-com-here-sdk-routing-Waypoint-com-here-sdk-routing-RoutingOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### refreshRoute

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">refreshRoute</span><wbr></wbr><span class="parameters">(@NonNull [RouteHandle](sdk-for-android-explore-com-here-sdk-routing-routehandle "class in com.here.sdk.routing") routeHandle, @NonNull [Waypoint](sdk-for-android-explore-com-here-sdk-routing-waypoint "class in com.here.sdk.routing") startingPoint, @NonNull [RoutingOptions](sdk-for-android-explore-com-here-sdk-routing-routingoptions "class in com.here.sdk.routing") options, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use the

        refresh_route()

    methods with RefreshRouteParameters parameter instead.
    </p>

    </div>

    </div>

    <div class="block">

    Asynchronously refreshes a previously calculated route from the provided RouteHandle , updating the starting point and route metadata based on RoutingOptions . The route shape from the new starting point to the destination remains unchanged, and only metadata such as arrival time and traffic delays are updated. If you only want to refresh the contained traffic information, consider to use calculateTrafficOnRoute(Route, int, int, double, CalculateTrafficOnRouteCallback) instead. Calling this method will trigger a new "HERE Routing" transaction, for example, if you are using the Base Plan .

    </div>

    Parameters:  
    `routeHandle` -

    The route handle holding the route to be refreshed.

    `startingPoint` -

    Updates the starting point of the route. It should be of type [`WaypointType.STOPOVER`](sdk-for-android-explore-com-here-sdk-routing-waypointtype#STOPOVER). Otherwise, an [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-com-here-sdk-routing-routingerror#INVALID_PARAMETER) error is generated. Moreover, it should be very close to the original route specified with the [`RouteHandle`](sdk-for-android-explore-com-here-sdk-routing-routehandle "class in com.here.sdk.routing"). Since the new starting point is expected to be along the original route, the original route geometry is used to reach the remaining waypoints. The new route will not include the [`Waypoint`](sdk-for-android-explore-com-here-sdk-routing-waypoint "class in com.here.sdk.routing") items that lie behind the new starting point (i.e. the path that was already traveled). Plus, [](sdk-for-android-explore-com-here-sdk-routing-route#getLengthInMeters())

        Route.getLengthInMeters()

    </a> and [](sdk-for-android-explore-com-here-sdk-routing-route#getDuration())

        Route.getDuration()

    </a> values are from the new starting point to the destination. If the new waypoint is too far off the original route, the route refresh may fail and an [`RoutingError.COULD_NOT_MATCH_ORIGIN`](sdk-for-android-explore-com-here-sdk-routing-routingerror#COULD_NOT_MATCH_ORIGIN) error is triggered. In that case, an application may decide to calculate a new route from scratch.

    </p>

    `options` -

    The options define the vehicle and route options to calculate the route.

    `callback` -

    Callback object that will be invoked after refreshing the route. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-explore-refreshRoute-com-here-sdk-routing-RefreshRouteParameters-com-here-sdk-routing-RoutingOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### refreshRoute

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">refreshRoute</span><wbr></wbr><span class="parameters">(@NonNull [RefreshRouteParameters](sdk-for-android-explore-com-here-sdk-routing-refreshrouteparameters "class in com.here.sdk.routing") refreshRouteParameters, @NonNull [RoutingOptions](sdk-for-android-explore-com-here-sdk-routing-routingoptions "class in com.here.sdk.routing") routingOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

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

  - <div id="sdk-for-android-explore-importRoute-com-here-sdk-routing-RouteHandle-com-here-sdk-routing-RefreshRouteOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### importRoute

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">importRoute</span><wbr></wbr><span class="parameters">(@NonNull [RouteHandle](sdk-for-android-explore-com-here-sdk-routing-routehandle "class in com.here.sdk.routing") routeHandle, @NonNull [RefreshRouteOptions](sdk-for-android-explore-com-here-sdk-routing-refreshrouteoptions "class in com.here.sdk.routing") refreshRouteOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use the

        import_route()

    methods with RoutingOptions parameter instead.
    </p>

    </div>

    </div>

    <div class="block">

    Asynchronously recreates a route from the RouteHandle provided, i.e. refreshes a previously calculated route, with the specified RefreshRouteOptions . A route handle can be invalid when the map data changes that is used by the HERE backend to recreate the route. This happens regularly. Therefore, the route handle is not meant to be persisted for a longer time. Instead, a possible use case can be to plan a route with another HERE service. For example, a HERE REST API that allows to calculate a route on a desktop. Then this route can be transferred via the handle to a mobile device for further use with the HERE SDK.

    </div>

    Parameters:  
    `routeHandle` -

    The route handle holding the route to be refreshed.

    `refreshRouteOptions` -

    The options define the vehicle and route options to calculate the route. **Note** An \[sdk.routing.RoutingError.INVALID_PARAMETER\] is generated when the \[sdk.routing.ElectricVehicleOptions.ensure_reachability\] option is set to `true`.

    `callback` -

    Callback object that will be invoked after refreshing the route. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-explore-importRoute-java-util-List-com-here-sdk-routing-CarOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### importRoute

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">importRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[Location](sdk-for-android-explore-com-here-sdk-core-location "class in com.here.sdk.core")\> locations, @NonNull [CarOptions](sdk-for-android-explore-com-here-sdk-routing-caroptions "class in com.here.sdk.routing") carOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use the

        import_route()

    methods with RoutingOptions parameter instead.
    </p>

    </div>

    </div>

    <div class="block">

    Asynchronously creates a car route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error. Note: Any restrictions applied to a transport type or provided options will be discarded and reported as violations in Section.getSectionNotices() .

    </div>

    Parameters:  
    `locations` -

    The list of locations used to calculate the route. Note that only the [`Location.coordinates`](sdk-for-android-explore-com-here-sdk-core-location#coordinates) of a location are used to import the route. An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-com-here-sdk-routing-routingerror#INVALID_PARAMETER) error is generated when the location list size is not in the range \[2,50000\].

    `carOptions` -

    Options specific for car route calculation, along with common route options.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-explore-importRoute-java-util-List-java-util-List-com-here-sdk-routing-PedestrianOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### importRoute

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">importRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[Location](sdk-for-android-explore-com-here-sdk-core-location "class in com.here.sdk.core")\> locations, @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[RouteStop](sdk-for-android-explore-com-here-sdk-routing-routestop "class in com.here.sdk.routing")\> routeStops, @NonNull [PedestrianOptions](sdk-for-android-explore-com-here-sdk-routing-pedestrianoptions "class in com.here.sdk.routing") pedestrianOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use the

        import_route()

    methods with RoutingOptions parameter instead.
    </p>

    </div>

    </div>

    <div class="block">

    Asynchronously creates a pedestrian route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error. Note: Any restrictions applied to a transport type or provided options will be discarded and reported as violations in Section.getSectionNotices() .

    </div>

    Parameters:  
    `locations` -

    The list of locations used to calculate the route. Note that only the [`Location.coordinates`](sdk-for-android-explore-com-here-sdk-core-location#coordinates) of a location are used to import the route. An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-com-here-sdk-routing-routingerror#INVALID_PARAMETER) error is generated when the location list size is not in the range \[2,50000\].

    `routeStops` -

    The list of RouteStop's which contains index of location from locations list used for route stop and duration in seconds spent on stop. An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-com-here-sdk-routing-routingerror#INVALID_PARAMETER) error is generated when the route stops list size is not in the range \[1,locations.size()-2\], any of location_index is \< 1 or location_indexes are not unique.

    `pedestrianOptions` -

    Options specific for pedestrian route calculation, along with common route options. Note that [`OptimizationMode.SHORTEST`](sdk-for-android-explore-com-here-sdk-routing-optimizationmode#SHORTEST) is not supported for pedestrians and converted to [`OptimizationMode.FASTEST`](sdk-for-android-explore-com-here-sdk-routing-optimizationmode#FASTEST) automatically.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-explore-importRoute-java-util-List-java-util-List-com-here-sdk-routing-BicycleOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### importRoute

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">importRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[Location](sdk-for-android-explore-com-here-sdk-core-location "class in com.here.sdk.core")\> locations, @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[RouteStop](sdk-for-android-explore-com-here-sdk-routing-routestop "class in com.here.sdk.routing")\> routeStops, @NonNull [BicycleOptions](sdk-for-android-explore-com-here-sdk-routing-bicycleoptions "class in com.here.sdk.routing") bicycleOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use the

        import_route()

    methods with RoutingOptions parameter instead.
    </p>

    </div>

    </div>

    <div class="block">

    Asynchronously creates a bicycle route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error. Note: Any restrictions applied to a transport type or provided options will be discarded and reported as violations in Section.getSectionNotices() .

    </div>

    Parameters:  
    `locations` -

    The list of locations used to calculate the route. Note that only the [`Location.coordinates`](sdk-for-android-explore-com-here-sdk-core-location#coordinates) of a location are used to import the route. An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-com-here-sdk-routing-routingerror#INVALID_PARAMETER) error is generated when the location list size is not in the range \[2,50000\].

    `routeStops` -

    The list of RouteStop's which contains index of location from locations list used for route stop and duration in seconds spent on stop. An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-com-here-sdk-routing-routingerror#INVALID_PARAMETER) error is generated when the route stops list size is not in the range \[1,locations.size()-2\], any of location_index is \< 1 or location_indexes are not unique.

    `bicycleOptions` -

    Options specific for bicycle route calculation, along with common route options.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-explore-importRoute-java-util-List-java-util-List-com-here-sdk-routing-ScooterOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### importRoute

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">importRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[Location](sdk-for-android-explore-com-here-sdk-core-location "class in com.here.sdk.core")\> locations, @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[RouteStop](sdk-for-android-explore-com-here-sdk-routing-routestop "class in com.here.sdk.routing")\> routeStops, @NonNull [ScooterOptions](sdk-for-android-explore-com-here-sdk-routing-scooteroptions "class in com.here.sdk.routing") scooterOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use the

        import_route()

    methods with RoutingOptions parameter instead.
    </p>

    </div>

    </div>

    <div class="block">

    Asynchronously creates a scooter route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error. Note: Any restrictions applied to a transport type or provided options will be discarded and reported as violations in Section.getSectionNotices() .

    </div>

    Parameters:  
    `locations` -

    The list of locations used to calculate the route. Note that only the [`Location.coordinates`](sdk-for-android-explore-com-here-sdk-core-location#coordinates) of a location are used to import the route. An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-com-here-sdk-routing-routingerror#INVALID_PARAMETER) error is generated when the location list size is not in the range \[2,50000\].

    `routeStops` -

    The list of RouteStop's which contains index of location from locations list used for route stop and duration in seconds spent on stop. An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-com-here-sdk-routing-routingerror#INVALID_PARAMETER) error is generated when the route stops list size is not in the range \[1,locations.size()-2\], any of location_index is \< 1 or location_indexes are not unique.

    `scooterOptions` -

    Options specific for scooter route calculation, along with common route options. Note that [`OptimizationMode.SHORTEST`](sdk-for-android-explore-com-here-sdk-routing-optimizationmode#SHORTEST) is not supported for scooters and converted to [`OptimizationMode.FASTEST`](sdk-for-android-explore-com-here-sdk-routing-optimizationmode#FASTEST) automatically.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-explore-importRoute-java-util-List-com-here-sdk-routing-PedestrianOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### importRoute

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">importRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[Location](sdk-for-android-explore-com-here-sdk-core-location "class in com.here.sdk.core")\> locations, @NonNull [PedestrianOptions](sdk-for-android-explore-com-here-sdk-routing-pedestrianoptions "class in com.here.sdk.routing") pedestrianOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use the

        import_route()

    methods with RoutingOptions parameter instead.
    </p>

    </div>

    </div>

    <div class="block">

    Asynchronously creates a pedestrian route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error. Note: Any restrictions applied to a transport type or provided options will be discarded and reported as violations in Section.getSectionNotices() .

    </div>

    Parameters:  
    `locations` -

    The list of locations used to calculate the route. Note that only the [`Location.coordinates`](sdk-for-android-explore-com-here-sdk-core-location#coordinates) of a location are used to import the route. An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-com-here-sdk-routing-routingerror#INVALID_PARAMETER) error is generated when the location list size is not in the range \[2,50000\].

    `pedestrianOptions` -

    Options specific for pedestrian route calculation, along with common route options. Note that [`OptimizationMode.SHORTEST`](sdk-for-android-explore-com-here-sdk-routing-optimizationmode#SHORTEST) is not supported for pedestrians and converted to [`OptimizationMode.FASTEST`](sdk-for-android-explore-com-here-sdk-routing-optimizationmode#FASTEST) automatically.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-explore-importRoute-java-util-List-com-here-sdk-routing-BicycleOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### importRoute

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">importRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[Location](sdk-for-android-explore-com-here-sdk-core-location "class in com.here.sdk.core")\> locations, @NonNull [BicycleOptions](sdk-for-android-explore-com-here-sdk-routing-bicycleoptions "class in com.here.sdk.routing") bicycleOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use the

        import_route()

    methods with RoutingOptions parameter instead.
    </p>

    </div>

    </div>

    <div class="block">

    Asynchronously creates a bicycle route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error. Note: Any restrictions applied to a transport type or provided options will be discarded and reported as violations in Section.getSectionNotices() .

    </div>

    Parameters:  
    `locations` -

    The list of locations used to calculate the route. Note that only the [`Location.coordinates`](sdk-for-android-explore-com-here-sdk-core-location#coordinates) of a location are used to import the route. An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-com-here-sdk-routing-routingerror#INVALID_PARAMETER) error is generated when the location list size is not in the range \[2,50000\].

    `bicycleOptions` -

    Options specific for bicycle route calculation, along with common route options.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-explore-importRoute-java-util-List-com-here-sdk-routing-ScooterOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### importRoute

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">importRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[Location](sdk-for-android-explore-com-here-sdk-core-location "class in com.here.sdk.core")\> locations, @NonNull [ScooterOptions](sdk-for-android-explore-com-here-sdk-routing-scooteroptions "class in com.here.sdk.routing") scooterOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use the

        import_route()

    methods with RoutingOptions parameter instead.
    </p>

    </div>

    </div>

    <div class="block">

    Asynchronously creates a scooter route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error. Note: Any restrictions applied to a transport type or provided options will be discarded and reported as violations in Section.getSectionNotices() .

    </div>

    Parameters:  
    `locations` -

    The list of locations used to calculate the route. Note that only the [`Location.coordinates`](sdk-for-android-explore-com-here-sdk-core-location#coordinates) of a location are used to import the route. An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-com-here-sdk-routing-routingerror#INVALID_PARAMETER) error is generated when the location list size is not in the range \[2,50000\].

    `scooterOptions` -

    Options specific for scooter route calculation, along with common route options. Note that [`OptimizationMode.SHORTEST`](sdk-for-android-explore-com-here-sdk-routing-optimizationmode#SHORTEST) is not supported for scooters and converted to [`OptimizationMode.FASTEST`](sdk-for-android-explore-com-here-sdk-routing-optimizationmode#FASTEST) automatically.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-explore-importRoute-java-util-List-com-here-sdk-routing-TruckOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### importRoute

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">importRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[Location](sdk-for-android-explore-com-here-sdk-core-location "class in com.here.sdk.core")\> locations, @NonNull [TruckOptions](sdk-for-android-explore-com-here-sdk-routing-truckoptions "class in com.here.sdk.routing") truckOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use the

        import_route()

    methods with RoutingOptions parameter instead.
    </p>

    </div>

    </div>

    <div class="block">

    Asynchronously creates a truck route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error. Note: Any restrictions applied to a transport type or provided options will be discarded and reported as violations in Section.getSectionNotices() .

    </div>

    Parameters:  
    `locations` -

    The list of locations used to calculate the route. Note that only the [`Location.coordinates`](sdk-for-android-explore-com-here-sdk-core-location#coordinates) of a location are used to import the route. An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-com-here-sdk-routing-routingerror#INVALID_PARAMETER) error is generated when the location list size is not in the range \[2,50000\].

    `truckOptions` -

    Options specific for truck route calculation, along with common route options.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-explore-importRoute-java-util-List-com-here-sdk-routing-TaxiOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### importRoute

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">importRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[Location](sdk-for-android-explore-com-here-sdk-core-location "class in com.here.sdk.core")\> locations, @NonNull [TaxiOptions](sdk-for-android-explore-com-here-sdk-routing-taxioptions "class in com.here.sdk.routing") taxiOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use the

        import_route()

    methods with RoutingOptions parameter instead.
    </p>

    </div>

    </div>

    <div class="block">

    Asynchronously creates a taxi route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error. Note: Any restrictions applied to a transport type or provided options will be discarded and reported as violations in Section.getSectionNotices() .

    </div>

    Parameters:  
    `locations` -

    The list of locations used to calculate the route. Note that only the [`Location.coordinates`](sdk-for-android-explore-com-here-sdk-core-location#coordinates) of a location are used to import the route. An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-com-here-sdk-routing-routingerror#INVALID_PARAMETER) error is generated when the location list size is not in the range \[2,50000\].

    `taxiOptions` -

    Options specific for taxi route calculation, along with common route options. Note that [`OptimizationMode.SHORTEST`](sdk-for-android-explore-com-here-sdk-routing-optimizationmode#SHORTEST) is not supported for taxis and converted to [`OptimizationMode.FASTEST`](sdk-for-android-explore-com-here-sdk-routing-optimizationmode#FASTEST) automatically.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-explore-importRoute-java-util-List-com-here-sdk-routing-BusOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### importRoute

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">importRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[Location](sdk-for-android-explore-com-here-sdk-core-location "class in com.here.sdk.core")\> locations, @NonNull [BusOptions](sdk-for-android-explore-com-here-sdk-routing-busoptions "class in com.here.sdk.routing") busOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use the

        import_route()

    methods with RoutingOptions parameter instead.
    </p>

    </div>

    </div>

    <div class="block">

    Asynchronously creates a bus route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error. Note: Any restrictions applied to a transport type or provided options will be discarded and reported as violations in Section.getSectionNotices() .

    </div>

    Parameters:  
    `locations` -

    The list of locations used to calculate the route. Note that only the [`Location.coordinates`](sdk-for-android-explore-com-here-sdk-core-location#coordinates) of a location are used to import the route. An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-com-here-sdk-routing-routingerror#INVALID_PARAMETER) error is generated when the location list size is not in the range \[2,50000\].

    `busOptions` -

    Options specific for bus route calculation, along with common route options.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-explore-importRoute-java-util-List-com-here-sdk-routing-PrivateBusOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### importRoute

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">importRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[Location](sdk-for-android-explore-com-here-sdk-core-location "class in com.here.sdk.core")\> locations, @NonNull [PrivateBusOptions](sdk-for-android-explore-com-here-sdk-routing-privatebusoptions "class in com.here.sdk.routing") privateBusOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use the

        import_route()

    methods with RoutingOptions parameter instead.
    </p>

    </div>

    </div>

    <div class="block">

    Asynchronously creates a private bus route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or anyway geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error. Note: Any restrictions applied to a transport type or provided options will be discarded and reported as violations in Section.getSectionNotices() .

    </div>

    Parameters:  
    `locations` -

    The list of locations used to calculate the route. Note that only the [`Location.coordinates`](sdk-for-android-explore-com-here-sdk-core-location#coordinates) of a location are used to import the route. An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-com-here-sdk-routing-routingerror#INVALID_PARAMETER) error is generated when the location list size is not in the range \[2,50000\].

    `privateBusOptions` -

    Options specific for private bus route calculation, along with common route options.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-explore-importRoute-java-util-List-com-here-sdk-routing-EVCarOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### importRoute

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">importRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[Location](sdk-for-android-explore-com-here-sdk-core-location "class in com.here.sdk.core")\> locations, @NonNull [EVCarOptions](sdk-for-android-explore-com-here-sdk-routing-evcaroptions "class in com.here.sdk.routing") evCarOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use the

        import_route()

    methods with RoutingOptions parameter instead.
    </p>

    </div>

    </div>

    <div class="block">

    Asynchronously creates an electric car route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error. Note: Any restrictions applied to a transport type or provided options will be discarded and reported as violations in Section.getSectionNotices() .

    </div>

    Parameters:  
    `locations` -

    The list of locations used to calculate the route. Note that only the [`Location.coordinates`](sdk-for-android-explore-com-here-sdk-core-location#coordinates) of a location are used to import the route. An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-com-here-sdk-routing-routingerror#INVALID_PARAMETER) error is generated when the location list size is not in the range \[2,50000\].

    `evCarOptions` -

    Options specific for an electric car route calculation, along with common route options. **Note** An \[sdk.routing.RoutingError.INVALID_PARAMETER\] is generated when the \[sdk.routing.EVCarOptions.ensure_reachability\] option is set to `true`.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-explore-importRoute-java-util-List-com-here-sdk-routing-EVTruckOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### importRoute

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">importRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[Location](sdk-for-android-explore-com-here-sdk-core-location "class in com.here.sdk.core")\> locations, @NonNull [EVTruckOptions](sdk-for-android-explore-com-here-sdk-routing-evtruckoptions "class in com.here.sdk.routing") evTruckOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use the

        import_route()

    methods with RoutingOptions parameter instead.
    </p>

    </div>

    </div>

    <div class="block">

    Asynchronously creates an electric truck route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error. Note: Any restrictions applied to a transport type or provided options will be discarded and reported as violations in Section.getSectionNotices() .

    </div>

    Parameters:  
    `locations` -

    The list of locations used to calculate the route. Note that only the [`Location.coordinates`](sdk-for-android-explore-com-here-sdk-core-location#coordinates) of a location are used to import the route. An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-com-here-sdk-routing-routingerror#INVALID_PARAMETER) error is generated when the location list size is not in the range \[2,50000\].

    `evTruckOptions` -

    Options specific for an electric truck route calculation, along with common route options.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-explore-importRoute-java-util-List-java-util-List-com-here-sdk-routing-CarOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### importRoute

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">importRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[Location](sdk-for-android-explore-com-here-sdk-core-location "class in com.here.sdk.core")\> locations, @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[RouteStop](sdk-for-android-explore-com-here-sdk-routing-routestop "class in com.here.sdk.routing")\> routeStops, @NonNull [CarOptions](sdk-for-android-explore-com-here-sdk-routing-caroptions "class in com.here.sdk.routing") carOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use the

        import_route()

    methods with RoutingOptions parameter instead.
    </p>

    </div>

    </div>

    <div class="block">

    Asynchronously creates a car route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error. Note: Any restrictions applied to a transport type or provided options will be discarded and reported as violations in Section.getSectionNotices() .

    </div>

    Parameters:  
    `locations` -

    The list of locations used to calculate the route. Note that only the [`Location.coordinates`](sdk-for-android-explore-com-here-sdk-core-location#coordinates) of a location are used to import the route. An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-com-here-sdk-routing-routingerror#INVALID_PARAMETER) error is generated when the location list size is not in the range \[2,50000\].

    `routeStops` -

    The list of RouteStop's which contains index of location from locations list used for route stop and duration in seconds spent on stop. An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-com-here-sdk-routing-routingerror#INVALID_PARAMETER) error is generated when the route stops list size is not in the range \[1,locations.size()-2\], any of location_index is \< 1 or location_indexes are not unique.

    `carOptions` -

    Options specific for car route calculation, along with common route options.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-explore-importRoute-java-util-List-java-util-List-com-here-sdk-routing-TruckOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### importRoute

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">importRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[Location](sdk-for-android-explore-com-here-sdk-core-location "class in com.here.sdk.core")\> locations, @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[RouteStop](sdk-for-android-explore-com-here-sdk-routing-routestop "class in com.here.sdk.routing")\> routeStops, @NonNull [TruckOptions](sdk-for-android-explore-com-here-sdk-routing-truckoptions "class in com.here.sdk.routing") truckOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use the

        import_route()

    methods with RoutingOptions parameter instead.
    </p>

    </div>

    </div>

    <div class="block">

    Asynchronously creates a truck route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error. Note: Any restrictions applied to a transport type or provided options will be discarded and reported as violations in Section.getSectionNotices() .

    </div>

    Parameters:  
    `locations` -

    The list of locations used to calculate the route. Note that only the [`Location.coordinates`](sdk-for-android-explore-com-here-sdk-core-location#coordinates) of a location are used to import the route. An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-com-here-sdk-routing-routingerror#INVALID_PARAMETER) error is generated when the location list size is not in the range \[2,50000\].

    `routeStops` -

    The list of RouteStop's which contains index of location from locations list used for route stop and duration in seconds spent on stop. An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-com-here-sdk-routing-routingerror#INVALID_PARAMETER) error is generated when the route stops list size is not in the range \[1,locations.size()-2\], any of location_index is \< 1 or location_indexes are not unique.

    `truckOptions` -

    Options specific for truck route calculation, along with common route options.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-explore-importRoute-java-util-List-java-util-List-com-here-sdk-routing-TaxiOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### importRoute

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">importRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[Location](sdk-for-android-explore-com-here-sdk-core-location "class in com.here.sdk.core")\> locations, @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[RouteStop](sdk-for-android-explore-com-here-sdk-routing-routestop "class in com.here.sdk.routing")\> routeStops, @NonNull [TaxiOptions](sdk-for-android-explore-com-here-sdk-routing-taxioptions "class in com.here.sdk.routing") taxiOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use the

        import_route()

    methods with RoutingOptions parameter instead.
    </p>

    </div>

    </div>

    <div class="block">

    Asynchronously creates a taxi route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error. Note: Any restrictions applied to a transport type or provided options will be discarded and reported as violations in Section.getSectionNotices() .

    </div>

    Parameters:  
    `locations` -

    The list of locations used to calculate the route. Note that only the [`Location.coordinates`](sdk-for-android-explore-com-here-sdk-core-location#coordinates) of a location are used to import the route. An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-com-here-sdk-routing-routingerror#INVALID_PARAMETER) error is generated when the location list size is not in the range \[2,50000\].

    `routeStops` -

    The list of RouteStop's which contains index of location from locations list used for route stop and duration in seconds spent on stop. An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-com-here-sdk-routing-routingerror#INVALID_PARAMETER) error is generated when the route stops list size is not in the range \[1,locations.size()-2\], any of location_index is \< 1 or location_indexes are not unique.

    `taxiOptions` -

    Options specific for taxi route calculation, along with common route options. Note that [`OptimizationMode.SHORTEST`](sdk-for-android-explore-com-here-sdk-routing-optimizationmode#SHORTEST) is not supported for taxis and converted to [`OptimizationMode.FASTEST`](sdk-for-android-explore-com-here-sdk-routing-optimizationmode#FASTEST) automatically.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-explore-importRoute-java-util-List-java-util-List-com-here-sdk-routing-BusOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### importRoute

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">importRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[Location](sdk-for-android-explore-com-here-sdk-core-location "class in com.here.sdk.core")\> locations, @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[RouteStop](sdk-for-android-explore-com-here-sdk-routing-routestop "class in com.here.sdk.routing")\> routeStops, @NonNull [BusOptions](sdk-for-android-explore-com-here-sdk-routing-busoptions "class in com.here.sdk.routing") busOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use the

        import_route()

    methods with RoutingOptions parameter instead.
    </p>

    </div>

    </div>

    <div class="block">

    Asynchronously creates a bus route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error. Note: Any restrictions applied to a transport type or provided options will be discarded and reported as violations in Section.getSectionNotices() .

    </div>

    Parameters:  
    `locations` -

    The list of locations used to calculate the route. Note that only the [`Location.coordinates`](sdk-for-android-explore-com-here-sdk-core-location#coordinates) of a location are used to import the route. An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-com-here-sdk-routing-routingerror#INVALID_PARAMETER) error is generated when the location list size is not in the range \[2,50000\].

    `routeStops` -

    The list of RouteStop's which contains index of location from locations list used for route stop and duration in seconds spent on stop. An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-com-here-sdk-routing-routingerror#INVALID_PARAMETER) error is generated when the route stops list size is not in the range \[1,locations.size()-2\], any of location_index is \< 1 or location_indexes are not unique.

    `busOptions` -

    Options specific for bus route calculation, along with common route options.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-explore-importRoute-java-util-List-java-util-List-com-here-sdk-routing-PrivateBusOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### importRoute

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">importRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[Location](sdk-for-android-explore-com-here-sdk-core-location "class in com.here.sdk.core")\> locations, @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[RouteStop](sdk-for-android-explore-com-here-sdk-routing-routestop "class in com.here.sdk.routing")\> routeStops, @NonNull [PrivateBusOptions](sdk-for-android-explore-com-here-sdk-routing-privatebusoptions "class in com.here.sdk.routing") privateBusOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use the

        import_route()

    methods with RoutingOptions parameter instead.
    </p>

    </div>

    </div>

    <div class="block">

    Asynchronously creates a private bus route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or anyway geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error. Note: Any restrictions applied to a transport type or provided options will be discarded and reported as violations in Section.getSectionNotices() .

    </div>

    Parameters:  
    `locations` -

    The list of locations used to calculate the route. Note that only the [`Location.coordinates`](sdk-for-android-explore-com-here-sdk-core-location#coordinates) of a location are used to import the route. An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-com-here-sdk-routing-routingerror#INVALID_PARAMETER) error is generated when the location list size is not in the range \[2,50000\].

    `routeStops` -

    The list of RouteStop's which contains index of location from locations list used for route stop and duration in seconds spent on stop. An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-com-here-sdk-routing-routingerror#INVALID_PARAMETER) error is generated when the route stops list size is not in the range \[1,locations.size()-2\], any of location_index is \< 1 or location_indexes are not unique.

    `privateBusOptions` -

    Options specific for private bus route calculation, along with common route options.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-explore-importRoute-java-util-List-java-util-List-com-here-sdk-routing-EVCarOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### importRoute

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">importRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[Location](sdk-for-android-explore-com-here-sdk-core-location "class in com.here.sdk.core")\> locations, @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[RouteStop](sdk-for-android-explore-com-here-sdk-routing-routestop "class in com.here.sdk.routing")\> routeStops, @NonNull [EVCarOptions](sdk-for-android-explore-com-here-sdk-routing-evcaroptions "class in com.here.sdk.routing") evCarOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use the

        import_route()

    methods with RoutingOptions parameter instead.
    </p>

    </div>

    </div>

    <div class="block">

    Asynchronously creates an electric car route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error. Note: Any restrictions applied to a transport type or provided options will be discarded and reported as violations in Section.getSectionNotices() .

    </div>

    Parameters:  
    `locations` -

    The list of locations used to calculate the route. Note that only the [`Location.coordinates`](sdk-for-android-explore-com-here-sdk-core-location#coordinates) of a location are used to import the route. An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-com-here-sdk-routing-routingerror#INVALID_PARAMETER) error is generated when the location list size is not in the range \[2,50000\].

    `routeStops` -

    The list of RouteStop's which contains index of location from locations list used for route stop and duration in seconds spent on stop. An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-com-here-sdk-routing-routingerror#INVALID_PARAMETER) error is generated when the route stops list size is not in the range \[1,locations.size()-2\], any of location_index is \< 1 or location_indexes are not unique.

    `evCarOptions` -

    Options specific for an electric car route calculation, along with common route options. **Note** An \[sdk.routing.RoutingError.INVALID_PARAMETER\] is generated when the \[sdk.routing.EVCarOptions.ensure_reachability\] option is set to `true`.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-explore-importRoute-java-util-List-java-util-List-com-here-sdk-routing-EVTruckOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### importRoute

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">importRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[Location](sdk-for-android-explore-com-here-sdk-core-location "class in com.here.sdk.core")\> locations, @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[RouteStop](sdk-for-android-explore-com-here-sdk-routing-routestop "class in com.here.sdk.routing")\> routeStops, @NonNull [EVTruckOptions](sdk-for-android-explore-com-here-sdk-routing-evtruckoptions "class in com.here.sdk.routing") evTruckOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Will be removed in v4.28.0. Use the

        import_route()

    methods with RoutingOptions parameter instead.
    </p>

    </div>

    </div>

    <div class="block">

    Asynchronously creates an electric truck route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error. Note: Any restrictions applied to a transport type or provided options will be discarded and reported as violations in Section.getSectionNotices() .

    </div>

    Parameters:  
    `locations` -

    The list of locations used to calculate the route. Note that only the [`Location.coordinates`](sdk-for-android-explore-com-here-sdk-core-location#coordinates) of a location are used to import the route. An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-com-here-sdk-routing-routingerror#INVALID_PARAMETER) error is generated when the location list size is not in the range \[2,50000\].

    `routeStops` -

    The list of RouteStop's which contains index of location from locations list used for route stop and duration in seconds spent on stop. An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-com-here-sdk-routing-routingerror#INVALID_PARAMETER) error is generated when the route stops list size is not in the range \[1,locations.size()-2\], any of location_index is \< 1 or location_indexes are not unique.

    `evTruckOptions` -

    Options specific for an electric truck route calculation, along with common route options.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-explore-importRoute-java-util-List-com-here-sdk-routing-RoutingOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### importRoute

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">importRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[Location](sdk-for-android-explore-com-here-sdk-core-location "class in com.here.sdk.core")\> locations, @NonNull [RoutingOptions](sdk-for-android-explore-com-here-sdk-routing-routingoptions "class in com.here.sdk.routing") options, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

    </div>

    <div class="block">

    Asynchronously creates a route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error. Note: Any restrictions applied to a transport type or provided options will be discarded and reported as violations in Section.getSectionNotices() .

    </div>

    Parameters:  
    `locations` -

    The list of locations used to calculate the route. Note that only the [`Location.coordinates`](sdk-for-android-explore-com-here-sdk-core-location#coordinates) of a location are used to import the route. An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-com-here-sdk-routing-routingerror#INVALID_PARAMETER) error is generated when the location list size is not in the range \[2,50000\].

    `options` -

    The options define the vehicle and route options to calculate the route.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-explore-importRoute-java-util-List-java-util-List-com-here-sdk-routing-RoutingOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### importRoute

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">importRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[Location](sdk-for-android-explore-com-here-sdk-core-location "class in com.here.sdk.core")\> locations, @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[RouteStop](sdk-for-android-explore-com-here-sdk-routing-routestop "class in com.here.sdk.routing")\> routeStops, @NonNull [RoutingOptions](sdk-for-android-explore-com-here-sdk-routing-routingoptions "class in com.here.sdk.routing") options, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

    </div>

    <div class="block">

    Asynchronously creates a route from a sequence of geographic coordinates very close to each other. The route shape will be kept as close as possible to the one provided. For best results please use 1Hz GPS data, or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error. Note: Any restrictions applied to a transport type or provided options will be discarded and reported as violations in Section.getSectionNotices() .

    </div>

    Parameters:  
    `locations` -

    The list of locations used to calculate the route. Note that only the [`Location.coordinates`](sdk-for-android-explore-com-here-sdk-core-location#coordinates) of a location are used to import the route. An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-com-here-sdk-routing-routingerror#INVALID_PARAMETER) error is generated when the location list size is not in the range \[2,50000\].

    `routeStops` -

    The list of RouteStop's which contains index of location from locations list used for route stop and duration in seconds spent on stop. An [`RoutingError.INVALID_PARAMETER`](sdk-for-android-explore-com-here-sdk-routing-routingerror#INVALID_PARAMETER) error is generated when the route stops list size is not in the range \[1,locations.size()-2\], any of location_index is \< 1 or location_indexes are not unique.

    `options` -

    The options define the vehicle and route options to calculate the route.

    `callback` -

    Callback object that will be invoked after route calculation. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-explore-importRoute-com-here-sdk-routing-RouteHandle-com-here-sdk-routing-RoutingOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### importRoute

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">importRoute</span><wbr></wbr><span class="parameters">(@NonNull [RouteHandle](sdk-for-android-explore-com-here-sdk-routing-routehandle "class in com.here.sdk.routing") routeHandle, @NonNull [RoutingOptions](sdk-for-android-explore-com-here-sdk-routing-routingoptions "class in com.here.sdk.routing") options, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

    </div>

    <div class="block">

    Asynchronously recreates a route from the RouteHandle provided, i.e. refreshes a previously calculated route, with the specified RoutingOptions . A route handle can be invalid when the map data changes that is used by the HERE sdk to recreate the route. This happens regularly. Therefore, the route handle is not meant to be persisted for a longer time.

    </div>

    Parameters:  
    `routeHandle` -

    The route handle holding the route to be refreshed.

    `options` -

    The options define the vehicle and route options to calculate the route.

    `callback` -

    Callback object that will be invoked after refreshing the route. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-explore-calculateTrafficOnRoute-com-here-sdk-routing-Route-int-int-com-here-sdk-routing-CalculateTrafficOnRouteCallback" class="section detail">

    ### calculateTrafficOnRoute

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">calculateTrafficOnRoute</span><wbr></wbr><span class="parameters">(@NonNull [Route](sdk-for-android-explore-com-here-sdk-routing-route "class in com.here.sdk.routing") route, int lastTraveledSectionIndex, int traveledDistanceOnLastSectionInMeters, @NonNull [CalculateTrafficOnRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculatetrafficonroutecallback "interface in com.here.sdk.routing") callback)</span>

    </div>

    <div class="block">

    Asynchronously calculates the traffic along a route starting from the index of the last traveled route section and an offset (in meters) from the last visited position on the section. Call this when only the contained traffic information or the latest ETA duration is needed. This can be called periodically to retrieve updated ETA values during navigation. Note: Calling this method will trigger a new "HERE Traffic" transaction, for example, if you are using the Base Plan .

    </div>

    Parameters:  
    `route` -

    A [`Route`](sdk-for-android-explore-com-here-sdk-routing-route "class in com.here.sdk.routing") calculated using the online routing engine. Its [`RouteHandle`](sdk-for-android-explore-com-here-sdk-routing-routehandle "class in com.here.sdk.routing") and the original route calculation options will be used to compute the traffic on the route. The original route remains untouched.

    `lastTraveledSectionIndex` -

    Indicates the index of the last traveled route section. Traveled part of the route won't be reused.

    `traveledDistanceOnLastSectionInMeters` -

    Offset, in meters, to the last visited position on the route section defined by the last traveled section index.

    `callback` -

    Callback object that will be invoked after route traffic has been calculated. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-explore-calculateTrafficOnRoute-com-here-sdk-routing-Route-int-int-double-com-here-sdk-routing-CalculateTrafficOnRouteCallback" class="section detail">

    ### calculateTrafficOnRoute

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">calculateTrafficOnRoute</span><wbr></wbr><span class="parameters">(@NonNull [Route](sdk-for-android-explore-com-here-sdk-routing-route "class in com.here.sdk.routing") route, int lastTraveledSectionIndex, int traveledDistanceOnLastSectionInMeters, double currentChargeInKilowattHours, @NonNull [CalculateTrafficOnRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculatetrafficonroutecallback "interface in com.here.sdk.routing") callback)</span>

    </div>

    <div class="block">

    Asynchronously calculates the traffic along an EV car route starting from the index of the last traveled route section and an offset in meters from the last visited position on the section. The field TrafficOnSpan.consumptionInKilowattHours will contain the power consumption in kilowatt-hours (kWh) necessary to traverse the span, and RoutePlace.chargeInKilowattHours , inside TrafficOnSection.departurePlace and TrafficOnSection.arrivalPlace , the estimated battery charge in kilowatt-hours (kWh) when leaving/arriving to a section. Note: Only EV cars are supported.

    </div>

    Parameters:  
    `route` -

    A [`Route`](sdk-for-android-explore-com-here-sdk-routing-route "class in com.here.sdk.routing") calculated using the online routing engine. Its [`RouteHandle`](sdk-for-android-explore-com-here-sdk-routing-routehandle "class in com.here.sdk.routing") and the original route calculation options, along with EV related information like [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing"), will be used to compute the traffic on the route. The original route remains untouched.

    `lastTraveledSectionIndex` -

    Indicates the index of the last traveled route section. Traveled part of the route won't be reused.

    `traveledDistanceOnLastSectionInMeters` -

    Offset, in meters, to the last visited position on the route section defined by the last traveled section index.

    `currentChargeInKilowattHours` -

    Charge level of the vehicle's battery at the current location (in kWh). It must be non-negative and less than or equal to the value of [`BatterySpecifications.totalCapacityInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#totalCapacityInKilowattHours), otherwise the [`BatterySpecifications`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications "class in com.here.sdk.routing") instance is considered invalid. Sets [`BatterySpecifications.initialChargeInKilowattHours`](sdk-for-android-explore-com-here-sdk-routing-batteryspecifications#initialChargeInKilowattHours) to the given value.

    `callback` -

    Callback object that will be invoked after route traffic has been calculated. It is always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="sdk-for-android-explore-setCustomOption-java-lang-String-java-lang-String" class="section detail">

    ### setCustomOption

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type">[RoutingError](sdk-for-android-explore-com-here-sdk-routing-routingerror "enum class in com.here.sdk.routing")</span> <span class="element-name">setCustomOption</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> name, @Nullable <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> value)</span>

    </div>

    <div class="block">

    Sets a custom option for routing backend queries. The custom option is applied to all the queries that RoutingEngine performs. For a complete list of available parameter names and their valid values, refer to HERE Routing API v8 . Note: It's easy to set a wrong option that makes queries invalid, so make sure you read and understand the backend documentation.

    </div>

    Parameters:  
    `name` -

    An option name. If the engine already has an option with the same name, the option will be overwritten. The option name must be a non-empty string.

    `value` -

    An option value. If the value is `null`, the option will be removed. The option value must be a non-empty string.

    Returns:  
    An optional error of setting the option. It's `null` if the option has been set successfully. It's `RoutingError.INVALID_PARAMETER` if the input name and/or value haven't passed internal validation.

    </div>

  - <div id="sdk-for-android-explore-calculateRoute-java-util-List-com-here-sdk-routing-RoutingOptions-com-here-sdk-routing-CalculateRouteCallback" class="section detail">

    ### calculateRoute

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">calculateRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[Waypoint](sdk-for-android-explore-com-here-sdk-routing-waypoint "class in com.here.sdk.routing")\> waypoints, @NonNull [RoutingOptions](sdk-for-android-explore-com-here-sdk-routing-routingoptions "class in com.here.sdk.routing") options, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

    </div>

    <div class="block">

    Asynchronously calculates a route from one point to another, passing through the given waypoints in the given order.

    </div>

    Specified by:  
    [`calculateRoute`](sdk-for-android-explore-com-here-sdk-routing-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.RoutingOptions,com.here.sdk.routing.CalculateRouteCallback)) in interface [`RoutingInterface`](sdk-for-android-explore-com-here-sdk-routing-routinginterface "interface in com.here.sdk.routing")

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

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">calculateRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[Waypoint](sdk-for-android-explore-com-here-sdk-routing-waypoint "class in com.here.sdk.routing")\> waypoints, @NonNull [CarOptions](sdk-for-android-explore-com-here-sdk-routing-caroptions "class in com.here.sdk.routing") carOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

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
    [`calculateRoute`](sdk-for-android-explore-com-here-sdk-routing-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.CarOptions,com.here.sdk.routing.CalculateRouteCallback)) in interface [`RoutingInterface`](sdk-for-android-explore-com-here-sdk-routing-routinginterface "interface in com.here.sdk.routing")

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

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">calculateRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[Waypoint](sdk-for-android-explore-com-here-sdk-routing-waypoint "class in com.here.sdk.routing")\> waypoints, @NonNull [PedestrianOptions](sdk-for-android-explore-com-here-sdk-routing-pedestrianoptions "class in com.here.sdk.routing") pedestrianOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

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
    [`calculateRoute`](sdk-for-android-explore-com-here-sdk-routing-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.PedestrianOptions,com.here.sdk.routing.CalculateRouteCallback)) in interface [`RoutingInterface`](sdk-for-android-explore-com-here-sdk-routing-routinginterface "interface in com.here.sdk.routing")

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

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">calculateRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[Waypoint](sdk-for-android-explore-com-here-sdk-routing-waypoint "class in com.here.sdk.routing")\> waypoints, @NonNull [TruckOptions](sdk-for-android-explore-com-here-sdk-routing-truckoptions "class in com.here.sdk.routing") truckOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

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
    [`calculateRoute`](sdk-for-android-explore-com-here-sdk-routing-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.TruckOptions,com.here.sdk.routing.CalculateRouteCallback)) in interface [`RoutingInterface`](sdk-for-android-explore-com-here-sdk-routing-routinginterface "interface in com.here.sdk.routing")

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

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">calculateRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[Waypoint](sdk-for-android-explore-com-here-sdk-routing-waypoint "class in com.here.sdk.routing")\> waypoints, @NonNull [ScooterOptions](sdk-for-android-explore-com-here-sdk-routing-scooteroptions "class in com.here.sdk.routing") scooterOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

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
    [`calculateRoute`](sdk-for-android-explore-com-here-sdk-routing-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.ScooterOptions,com.here.sdk.routing.CalculateRouteCallback)) in interface [`RoutingInterface`](sdk-for-android-explore-com-here-sdk-routing-routinginterface "interface in com.here.sdk.routing")

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

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">calculateRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[Waypoint](sdk-for-android-explore-com-here-sdk-routing-waypoint "class in com.here.sdk.routing")\> waypoints, @NonNull [BicycleOptions](sdk-for-android-explore-com-here-sdk-routing-bicycleoptions "class in com.here.sdk.routing") bicycleOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

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
    [`calculateRoute`](sdk-for-android-explore-com-here-sdk-routing-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.BicycleOptions,com.here.sdk.routing.CalculateRouteCallback)) in interface [`RoutingInterface`](sdk-for-android-explore-com-here-sdk-routing-routinginterface "interface in com.here.sdk.routing")

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

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">calculateRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[Waypoint](sdk-for-android-explore-com-here-sdk-routing-waypoint "class in com.here.sdk.routing")\> waypoints, @NonNull [TaxiOptions](sdk-for-android-explore-com-here-sdk-routing-taxioptions "class in com.here.sdk.routing") taxiOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

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
    [`calculateRoute`](sdk-for-android-explore-com-here-sdk-routing-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.TaxiOptions,com.here.sdk.routing.CalculateRouteCallback)) in interface [`RoutingInterface`](sdk-for-android-explore-com-here-sdk-routing-routinginterface "interface in com.here.sdk.routing")

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

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">calculateRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[Waypoint](sdk-for-android-explore-com-here-sdk-routing-waypoint "class in com.here.sdk.routing")\> waypoints, @NonNull [EVCarOptions](sdk-for-android-explore-com-here-sdk-routing-evcaroptions "class in com.here.sdk.routing") evCarOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

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
    [`calculateRoute`](sdk-for-android-explore-com-here-sdk-routing-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.EVCarOptions,com.here.sdk.routing.CalculateRouteCallback)) in interface [`RoutingInterface`](sdk-for-android-explore-com-here-sdk-routing-routinginterface "interface in com.here.sdk.routing")

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

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">calculateRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[Waypoint](sdk-for-android-explore-com-here-sdk-routing-waypoint "class in com.here.sdk.routing")\> waypoints, @NonNull [EVTruckOptions](sdk-for-android-explore-com-here-sdk-routing-evtruckoptions "class in com.here.sdk.routing") evTruckOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

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
    [`calculateRoute`](sdk-for-android-explore-com-here-sdk-routing-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.EVTruckOptions,com.here.sdk.routing.CalculateRouteCallback)) in interface [`RoutingInterface`](sdk-for-android-explore-com-here-sdk-routing-routinginterface "interface in com.here.sdk.routing")

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

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">calculateRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[Waypoint](sdk-for-android-explore-com-here-sdk-routing-waypoint "class in com.here.sdk.routing")\> waypoints, @NonNull [BusOptions](sdk-for-android-explore-com-here-sdk-routing-busoptions "class in com.here.sdk.routing") busOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

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
    [`calculateRoute`](sdk-for-android-explore-com-here-sdk-routing-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.BusOptions,com.here.sdk.routing.CalculateRouteCallback)) in interface [`RoutingInterface`](sdk-for-android-explore-com-here-sdk-routing-routinginterface "interface in com.here.sdk.routing")

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

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> @NonNull </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">calculateRoute</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<[Waypoint](sdk-for-android-explore-com-here-sdk-routing-waypoint "class in com.here.sdk.routing")\> waypoints, @NonNull [PrivateBusOptions](sdk-for-android-explore-com-here-sdk-routing-privatebusoptions "class in com.here.sdk.routing") privateBusOptions, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

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
    [`calculateRoute`](sdk-for-android-explore-com-here-sdk-routing-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.PrivateBusOptions,com.here.sdk.routing.CalculateRouteCallback)) in interface [`RoutingInterface`](sdk-for-android-explore-com-here-sdk-routing-routinginterface "interface in com.here.sdk.routing")

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

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">returnToRoute</span><wbr></wbr><span class="parameters">(@NonNull [Route](sdk-for-android-explore-com-here-sdk-routing-route "class in com.here.sdk.routing") route, @NonNull [Waypoint](sdk-for-android-explore-com-here-sdk-routing-waypoint "class in com.here.sdk.routing") startingPoint, int lastTraveledSectionIndex, int traveledDistanceOnLastSectionInMeters, @NonNull [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

    </div>

    <div class="block">

    Asynchronously calculates a new route that leads back to the original route. The part of the original route which was already traveled by the user is ignored. Note: Stopover waypoints are guaranteed to be visited. Pass-through waypoints will be ignored. Additionally, the following route options are ignored: RouteOptions.alternatives , RouteOptions.arrivalTime , and RouteOptions.optimizationMode . Most route options are only applied to the newly calculated part back to the route. An application may use this method to submit a new starting point for a previously calculated route. This method tries to avoid a costly route re-calculation as much as possible. In case returning to the route without re-calculation is not possible, a new route is calculated, while trying to salvage the previous route as much as possible. However, a completely new route containing no part of the previous route is possible, too. Note that this function uses only a limited amount of map data around the new origin. Therefore, it may also work fine with temporarily cached map data. It may also copy some of the original route data into the new route. A typical use case is to await at least 3 RouteDeviation events before calling this method. Or alternatively, wait at least 10 seconds after getting the first deviation event. On top, the user experience can be improved by checking if the vehicle has moved at least 50 meters since calling this method for the last time. Optionally, it may make sense to verify if the vehicle was ever following the route by checking if RouteDeviation.lastLocationOnRoute is set. Note that deviation events are sent each time a deviation is detected, i.e. for each new location update, regardless if the location has changed or not. More information can be found in the Developer Guide in the "Handle route deviations" section.

    </div>

    Specified by:  
    [`returnToRoute`](sdk-for-android-explore-com-here-sdk-routing-routinginterface#returnToRoute(com.here.sdk.routing.Route,com.here.sdk.routing.Waypoint,int,int,com.here.sdk.routing.CalculateRouteCallback)) in interface [`RoutingInterface`](sdk-for-android-explore-com-here-sdk-routing-routinginterface "interface in com.here.sdk.routing")

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

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">dispose</span>()

    </div>

    <div class="block">

    Cancels pending requests and closes the background worker thread. Note: This method should be called from main thread.

    </div>

    Specified by:  
    [`dispose`](sdk-for-android-explore-com-here-sdk-routing-routinginterface#dispose()) in interface [`RoutingInterface`](sdk-for-android-explore-com-here-sdk-routing-routinginterface "interface in com.here.sdk.routing")

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

