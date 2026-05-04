---
title: "Deprecated List (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestdeprecated-list"
hidden: false
---

# Deprecated API

## Contents

- [Classes](#class)
- [Enum Classes](#enum-class)
- [Fields](#field)
- [Methods](#method)
- [Constructors](#constructor)
- [Enum Constants](#enum-constant)

Deprecated Classes

Class

  Description

  [com.here.sdk.routing.BicycleOptions](sdk-for-android-explore-api-reference-latestbicycleoptions "class in com.here.sdk.routing")

Will be removed in v4.28.0. Use `RoutingOptions` class instead.

[com.here.sdk.routing.BusOptions](sdk-for-android-explore-api-reference-latestbusoptions "class in com.here.sdk.routing")

Will be removed in v4.28.0. Use `RoutingOptions` class instead.

[com.here.sdk.routing.CarOptions](sdk-for-android-explore-api-reference-latestcaroptions "class in com.here.sdk.routing")

Will be removed in v4.28.0. Use `RoutingOptions` class instead.

[com.here.sdk.routing.EVCarOptions](sdk-for-android-explore-api-reference-latestevcaroptions "class in com.here.sdk.routing")

Will be removed in v4.28.0. Use `RoutingOptions` class instead.

[com.here.sdk.routing.EVTruckOptions](sdk-for-android-explore-api-reference-latestevtruckoptions "class in com.here.sdk.routing")

Will be removed in v4.28.0. Use `RoutingOptions` class instead.

[com.here.sdk.routing.PedestrianOptions](sdk-for-android-explore-api-reference-latestpedestrianoptions "class in com.here.sdk.routing")

Will be removed in v4.28.0. Use `RoutingOptions` class instead.

[com.here.sdk.routing.PrivateBusOptions](sdk-for-android-explore-api-reference-latestprivatebusoptions "class in com.here.sdk.routing")

Will be removed in v4.28.0. Use `RoutingOptions` class instead.

[com.here.sdk.routing.RefreshRouteOptions](sdk-for-android-explore-api-reference-latestrefreshrouteoptions "class in com.here.sdk.routing")

Will be removed in v4.28.0. Use the `RoutingOptions` class instead.

[com.here.sdk.routing.ScooterOptions](sdk-for-android-explore-api-reference-latestscooteroptions "class in com.here.sdk.routing")

Will be removed in v4.28.0. Use `RoutingOptions` class instead.

[com.here.sdk.routing.TaxiOptions](sdk-for-android-explore-api-reference-latesttaxioptions "class in com.here.sdk.routing")

Will be removed in v4.28.0. Use `RoutingOptions` class instead.

[com.here.sdk.routing.TruckOptions](sdk-for-android-explore-api-reference-latesttruckoptions "class in com.here.sdk.routing")

Will be removed in v4.28.0. Use `RoutingOptions` class instead.

<!-- -->

Deprecated Enum Classes

Enum Class

  Description

  [com.here.sdk.transport.TruckType](sdk-for-android-explore-api-reference-latesttrucktype "enum class in com.here.sdk.transport")

Will be removed in v4.27.0. Use `TruckCategory` instead.

<!-- -->

Deprecated Fields

Field

  Description

  [com.here.sdk.routing.IsolineOptions.carOptions](sdk-for-android-explore-api-reference-latestisolineoptions#carOptions)

Will be removed in v4.28.0. Use the `routing_options` instead.

[com.here.sdk.routing.IsolineOptions.evCarOptions](sdk-for-android-explore-api-reference-latestisolineoptions#evCarOptions)

Will be removed in v4.28.0. Use the `routing_options` instead.

[com.here.sdk.routing.IsolineOptions.evTruckOptions](sdk-for-android-explore-api-reference-latestisolineoptions#evTruckOptions)

Will be removed in v4.28.0. Use the `routing_options` instead.

[com.here.sdk.routing.IsolineOptions.truckOptions](sdk-for-android-explore-api-reference-latestisolineoptions#truckOptions)

Will be removed in v4.28.0. Use the `routing_options` instead.

[com.here.sdk.routing.ViolatedRestriction.Details.forbiddenTruckType](sdk-for-android-explore-api-reference-latestviolatedrestriction-details#forbiddenTruckType)

Will be removed in v4.27.0. Use `forbidden_truck_category` instead.

[com.here.sdk.search.PlaceCategory.SIGHTS_LANDMARK_ATTACTION](sdk-for-android-explore-api-reference-latestplacecategory#SIGHTS_LANDMARK_ATTACTION)

Will be removed in v4.26.0. Please use SIGHTS_LANDMARK_ATTRACTION instead.

[com.here.sdk.transport.VehicleSpecification.truckType](sdk-for-android-explore-api-reference-latestvehiclespecification#truckType)

Will be removed in v4.27.0. Use `VehicleSpecification.truckCategory` instead.

<!-- -->

Deprecated Methods

Method

  Description

  [com.here.sdk.core.engine.LockingProcess.destroyLockingProcess(SDKOptions, long)](sdk-for-android-explore-api-reference-latestlockingprocess#destroyLockingProcess(com.here.sdk.core.engine.SDKOptions,long))

Will be removed in v4.27.0, use [`LockingProcess.destroyLockingProcess(android.content.Context, SDKOptions, long)`](sdk-for-android-explore-api-reference-latestlockingprocess#destroyLockingProcess(android.content.Context,com.here.sdk.core.engine.SDKOptions,long)) instead.

[com.here.sdk.core.engine.LockingProcess.getLockingProcessId(SDKOptions)](sdk-for-android-explore-api-reference-latestlockingprocess#getLockingProcessId(com.here.sdk.core.engine.SDKOptions))

Will be removed in v4.27.0, use [`LockingProcess.getLockingProcessId(android.content.Context, SDKOptions)`](sdk-for-android-explore-api-reference-latestlockingprocess#getLockingProcessId(android.content.Context,com.here.sdk.core.engine.SDKOptions)) instead.

[com.here.sdk.mapview.LocationIndicator.setMarker3dModel(MapMarker3DModel, double, LocationIndicator.MarkerType)](sdk-for-android-explore-api-reference-latestlocationindicator#setMarker3dModel(com.here.sdk.mapview.MapMarker3DModel,double,com.here.sdk.mapview.LocationIndicator.MarkerType))

Will be removed in v4.27.0. Please use the overloaded method with [`RenderSize.Unit`](sdk-for-android-explore-api-reference-latestrendersize-unit "enum class in com.here.sdk.mapview") instead.

[com.here.sdk.mapview.MapCameraKeyframeTrack.lookAtDistance(List\<ScalarKeyframe\>, Easing, KeyframeInterpolationMode)](sdk-for-android-explore-api-reference-latestmapcamerakeyframetrack#lookAtDistance(java.util.List,com.here.sdk.animation.Easing,com.here.sdk.animation.KeyframeInterpolationMode))

Will be removed in v4.27.0. Use , Easing, KeyframeInterpolationMode) instead.

[com.here.sdk.mapview.MapSurface.setSurface(Context, Surface, int, int)](sdk-for-android-explore-api-reference-latestmapsurface#setSurface(android.content.Context,android.view.Surface,int,int))

Will be removed in v4.26.0. Please use attachSurface.

[com.here.sdk.mapview.MapSurface.setSurface(Context, Surface, int, int, MapSurface.RenderListener)](sdk-for-android-explore-api-reference-latestmapsurface#setSurface(android.content.Context,android.view.Surface,int,int,com.here.sdk.mapview.MapSurface.RenderListener))

Will be removed in v4.26.0. Please use attachSurface.

[com.here.sdk.routing.RoutingEngine.calculateRoute(List\<Waypoint\>, BicycleOptions, CalculateRouteCallback)](sdk-for-android-explore-api-reference-latestroutingengine#calculateRoute(java.util.List,com.here.sdk.routing.BicycleOptions,com.here.sdk.routing.CalculateRouteCallback))

Will be removed in v4.28.0. Use the `calculate_route()` methods with RoutingOptions parameter instead.

[com.here.sdk.routing.RoutingEngine.calculateRoute(List\<Waypoint\>, BusOptions, CalculateRouteCallback)](sdk-for-android-explore-api-reference-latestroutingengine#calculateRoute(java.util.List,com.here.sdk.routing.BusOptions,com.here.sdk.routing.CalculateRouteCallback))

Will be removed in v4.28.0. Use the `calculate_route()` methods with RoutingOptions parameter instead.

[com.here.sdk.routing.RoutingEngine.calculateRoute(List\<Waypoint\>, CarOptions, CalculateRouteCallback)](sdk-for-android-explore-api-reference-latestroutingengine#calculateRoute(java.util.List,com.here.sdk.routing.CarOptions,com.here.sdk.routing.CalculateRouteCallback))

Will be removed in v4.28.0. Use the `calculate_route()` methods with RoutingOptions parameter instead.

[com.here.sdk.routing.RoutingEngine.calculateRoute(List\<Waypoint\>, EVCarOptions, CalculateRouteCallback)](sdk-for-android-explore-api-reference-latestroutingengine#calculateRoute(java.util.List,com.here.sdk.routing.EVCarOptions,com.here.sdk.routing.CalculateRouteCallback))

Will be removed in v4.28.0. Use the `calculate_route()` methods with RoutingOptions parameter instead.

[com.here.sdk.routing.RoutingEngine.calculateRoute(List\<Waypoint\>, EVTruckOptions, CalculateRouteCallback)](sdk-for-android-explore-api-reference-latestroutingengine#calculateRoute(java.util.List,com.here.sdk.routing.EVTruckOptions,com.here.sdk.routing.CalculateRouteCallback))

Will be removed in v4.28.0. Use the `calculate_route()` methods with RoutingOptions parameter instead.

[com.here.sdk.routing.RoutingEngine.calculateRoute(List\<Waypoint\>, PedestrianOptions, CalculateRouteCallback)](sdk-for-android-explore-api-reference-latestroutingengine#calculateRoute(java.util.List,com.here.sdk.routing.PedestrianOptions,com.here.sdk.routing.CalculateRouteCallback))

Will be removed in v4.28.0. Use the `calculate_route()` methods with RoutingOptions parameter instead.

[com.here.sdk.routing.RoutingEngine.calculateRoute(List\<Waypoint\>, PrivateBusOptions, CalculateRouteCallback)](sdk-for-android-explore-api-reference-latestroutingengine#calculateRoute(java.util.List,com.here.sdk.routing.PrivateBusOptions,com.here.sdk.routing.CalculateRouteCallback))

Will be removed in v4.28.0. Use the `calculate_route()` methods with RoutingOptions parameter instead.

[com.here.sdk.routing.RoutingEngine.calculateRoute(List\<Waypoint\>, ScooterOptions, CalculateRouteCallback)](sdk-for-android-explore-api-reference-latestroutingengine#calculateRoute(java.util.List,com.here.sdk.routing.ScooterOptions,com.here.sdk.routing.CalculateRouteCallback))

Will be removed in v4.28.0. Use the `calculate_route()` methods with RoutingOptions parameter instead.

[com.here.sdk.routing.RoutingEngine.calculateRoute(List\<Waypoint\>, TaxiOptions, CalculateRouteCallback)](sdk-for-android-explore-api-reference-latestroutingengine#calculateRoute(java.util.List,com.here.sdk.routing.TaxiOptions,com.here.sdk.routing.CalculateRouteCallback))

Will be removed in v4.28.0. Use the `calculate_route()` methods with RoutingOptions parameter instead.

[com.here.sdk.routing.RoutingEngine.calculateRoute(List\<Waypoint\>, TruckOptions, CalculateRouteCallback)](sdk-for-android-explore-api-reference-latestroutingengine#calculateRoute(java.util.List,com.here.sdk.routing.TruckOptions,com.here.sdk.routing.CalculateRouteCallback))

Will be removed in v4.28.0. Use the `calculate_route()` methods with RoutingOptions parameter instead.

[com.here.sdk.routing.RoutingEngine.importRoute(RouteHandle, RefreshRouteOptions, CalculateRouteCallback)](sdk-for-android-explore-api-reference-latestroutingengine#importRoute(com.here.sdk.routing.RouteHandle,com.here.sdk.routing.RefreshRouteOptions,com.here.sdk.routing.CalculateRouteCallback))

Will be removed in v4.28.0. Use the `import_route()` methods with RoutingOptions parameter instead.

[com.here.sdk.routing.RoutingEngine.importRoute(List\<Location\>, BicycleOptions, CalculateRouteCallback)](sdk-for-android-explore-api-reference-latestroutingengine#importRoute(java.util.List,com.here.sdk.routing.BicycleOptions,com.here.sdk.routing.CalculateRouteCallback))

Will be removed in v4.28.0. Use the `import_route()` methods with RoutingOptions parameter instead.

[com.here.sdk.routing.RoutingEngine.importRoute(List\<Location\>, BusOptions, CalculateRouteCallback)](sdk-for-android-explore-api-reference-latestroutingengine#importRoute(java.util.List,com.here.sdk.routing.BusOptions,com.here.sdk.routing.CalculateRouteCallback))

Will be removed in v4.28.0. Use the `import_route()` methods with RoutingOptions parameter instead.

[com.here.sdk.routing.RoutingEngine.importRoute(List\<Location\>, CarOptions, CalculateRouteCallback)](sdk-for-android-explore-api-reference-latestroutingengine#importRoute(java.util.List,com.here.sdk.routing.CarOptions,com.here.sdk.routing.CalculateRouteCallback))

Will be removed in v4.28.0. Use the `import_route()` methods with RoutingOptions parameter instead.

[com.here.sdk.routing.RoutingEngine.importRoute(List\<Location\>, EVCarOptions, CalculateRouteCallback)](sdk-for-android-explore-api-reference-latestroutingengine#importRoute(java.util.List,com.here.sdk.routing.EVCarOptions,com.here.sdk.routing.CalculateRouteCallback))

Will be removed in v4.28.0. Use the `import_route()` methods with RoutingOptions parameter instead.

[com.here.sdk.routing.RoutingEngine.importRoute(List\<Location\>, EVTruckOptions, CalculateRouteCallback)](sdk-for-android-explore-api-reference-latestroutingengine#importRoute(java.util.List,com.here.sdk.routing.EVTruckOptions,com.here.sdk.routing.CalculateRouteCallback))

Will be removed in v4.28.0. Use the `import_route()` methods with RoutingOptions parameter instead.

[com.here.sdk.routing.RoutingEngine.importRoute(List\<Location\>, PedestrianOptions, CalculateRouteCallback)](sdk-for-android-explore-api-reference-latestroutingengine#importRoute(java.util.List,com.here.sdk.routing.PedestrianOptions,com.here.sdk.routing.CalculateRouteCallback))

Will be removed in v4.28.0. Use the `import_route()` methods with RoutingOptions parameter instead.

[com.here.sdk.routing.RoutingEngine.importRoute(List\<Location\>, PrivateBusOptions, CalculateRouteCallback)](sdk-for-android-explore-api-reference-latestroutingengine#importRoute(java.util.List,com.here.sdk.routing.PrivateBusOptions,com.here.sdk.routing.CalculateRouteCallback))

Will be removed in v4.28.0. Use the `import_route()` methods with RoutingOptions parameter instead.

[com.here.sdk.routing.RoutingEngine.importRoute(List\<Location\>, ScooterOptions, CalculateRouteCallback)](sdk-for-android-explore-api-reference-latestroutingengine#importRoute(java.util.List,com.here.sdk.routing.ScooterOptions,com.here.sdk.routing.CalculateRouteCallback))

Will be removed in v4.28.0. Use the `import_route()` methods with RoutingOptions parameter instead.

[com.here.sdk.routing.RoutingEngine.importRoute(List\<Location\>, TaxiOptions, CalculateRouteCallback)](sdk-for-android-explore-api-reference-latestroutingengine#importRoute(java.util.List,com.here.sdk.routing.TaxiOptions,com.here.sdk.routing.CalculateRouteCallback))

Will be removed in v4.28.0. Use the `import_route()` methods with RoutingOptions parameter instead.

[com.here.sdk.routing.RoutingEngine.importRoute(List\<Location\>, TruckOptions, CalculateRouteCallback)](sdk-for-android-explore-api-reference-latestroutingengine#importRoute(java.util.List,com.here.sdk.routing.TruckOptions,com.here.sdk.routing.CalculateRouteCallback))

Will be removed in v4.28.0. Use the `import_route()` methods with RoutingOptions parameter instead.

[com.here.sdk.routing.RoutingEngine.importRoute(List\<Location\>, List\<RouteStop\>, BicycleOptions, CalculateRouteCallback)](sdk-for-android-explore-api-reference-latestroutingengine#importRoute(java.util.List,java.util.List,com.here.sdk.routing.BicycleOptions,com.here.sdk.routing.CalculateRouteCallback))

Will be removed in v4.28.0. Use the `import_route()` methods with RoutingOptions parameter instead.

[com.here.sdk.routing.RoutingEngine.importRoute(List\<Location\>, List\<RouteStop\>, BusOptions, CalculateRouteCallback)](sdk-for-android-explore-api-reference-latestroutingengine#importRoute(java.util.List,java.util.List,com.here.sdk.routing.BusOptions,com.here.sdk.routing.CalculateRouteCallback))

Will be removed in v4.28.0. Use the `import_route()` methods with RoutingOptions parameter instead.

[com.here.sdk.routing.RoutingEngine.importRoute(List\<Location\>, List\<RouteStop\>, CarOptions, CalculateRouteCallback)](sdk-for-android-explore-api-reference-latestroutingengine#importRoute(java.util.List,java.util.List,com.here.sdk.routing.CarOptions,com.here.sdk.routing.CalculateRouteCallback))

Will be removed in v4.28.0. Use the `import_route()` methods with RoutingOptions parameter instead.

[com.here.sdk.routing.RoutingEngine.importRoute(List\<Location\>, List\<RouteStop\>, EVCarOptions, CalculateRouteCallback)](sdk-for-android-explore-api-reference-latestroutingengine#importRoute(java.util.List,java.util.List,com.here.sdk.routing.EVCarOptions,com.here.sdk.routing.CalculateRouteCallback))

Will be removed in v4.28.0. Use the `import_route()` methods with RoutingOptions parameter instead.

[com.here.sdk.routing.RoutingEngine.importRoute(List\<Location\>, List\<RouteStop\>, EVTruckOptions, CalculateRouteCallback)](sdk-for-android-explore-api-reference-latestroutingengine#importRoute(java.util.List,java.util.List,com.here.sdk.routing.EVTruckOptions,com.here.sdk.routing.CalculateRouteCallback))

Will be removed in v4.28.0. Use the `import_route()` methods with RoutingOptions parameter instead.

[com.here.sdk.routing.RoutingEngine.importRoute(List\<Location\>, List\<RouteStop\>, PedestrianOptions, CalculateRouteCallback)](sdk-for-android-explore-api-reference-latestroutingengine#importRoute(java.util.List,java.util.List,com.here.sdk.routing.PedestrianOptions,com.here.sdk.routing.CalculateRouteCallback))

Will be removed in v4.28.0. Use the `import_route()` methods with RoutingOptions parameter instead.

[com.here.sdk.routing.RoutingEngine.importRoute(List\<Location\>, List\<RouteStop\>, PrivateBusOptions, CalculateRouteCallback)](sdk-for-android-explore-api-reference-latestroutingengine#importRoute(java.util.List,java.util.List,com.here.sdk.routing.PrivateBusOptions,com.here.sdk.routing.CalculateRouteCallback))

Will be removed in v4.28.0. Use the `import_route()` methods with RoutingOptions parameter instead.

[com.here.sdk.routing.RoutingEngine.importRoute(List\<Location\>, List\<RouteStop\>, ScooterOptions, CalculateRouteCallback)](sdk-for-android-explore-api-reference-latestroutingengine#importRoute(java.util.List,java.util.List,com.here.sdk.routing.ScooterOptions,com.here.sdk.routing.CalculateRouteCallback))

Will be removed in v4.28.0. Use the `import_route()` methods with RoutingOptions parameter instead.

[com.here.sdk.routing.RoutingEngine.importRoute(List\<Location\>, List\<RouteStop\>, TaxiOptions, CalculateRouteCallback)](sdk-for-android-explore-api-reference-latestroutingengine#importRoute(java.util.List,java.util.List,com.here.sdk.routing.TaxiOptions,com.here.sdk.routing.CalculateRouteCallback))

Will be removed in v4.28.0. Use the `import_route()` methods with RoutingOptions parameter instead.

[com.here.sdk.routing.RoutingEngine.importRoute(List\<Location\>, List\<RouteStop\>, TruckOptions, CalculateRouteCallback)](sdk-for-android-explore-api-reference-latestroutingengine#importRoute(java.util.List,java.util.List,com.here.sdk.routing.TruckOptions,com.here.sdk.routing.CalculateRouteCallback))

Will be removed in v4.28.0. Use the `import_route()` methods with RoutingOptions parameter instead.

[com.here.sdk.routing.RoutingEngine.refreshRoute(RouteHandle, Waypoint, RefreshRouteOptions, CalculateRouteCallback)](sdk-for-android-explore-api-reference-latestroutingengine#refreshRoute(com.here.sdk.routing.RouteHandle,com.here.sdk.routing.Waypoint,com.here.sdk.routing.RefreshRouteOptions,com.here.sdk.routing.CalculateRouteCallback))

Will be removed in v4.28.0. Use the `refresh_route()` methods with RoutingOptions parameter instead.

[com.here.sdk.routing.RoutingEngine.refreshRoute(RouteHandle, Waypoint, Integer, Integer, RefreshRouteOptions, CalculateRouteCallback)](sdk-for-android-explore-api-reference-latestroutingengine#refreshRoute(com.here.sdk.routing.RouteHandle,com.here.sdk.routing.Waypoint,java.lang.Integer,java.lang.Integer,com.here.sdk.routing.RefreshRouteOptions,com.here.sdk.routing.CalculateRouteCallback))

Will be removed in v4.28.0. Use the `refresh_route()` methods with RoutingOptions parameter instead.

[com.here.sdk.routing.RoutingInterface.calculateRoute(List\<Waypoint\>, BicycleOptions, CalculateRouteCallback)](sdk-for-android-explore-api-reference-latestroutinginterface#calculateRoute(java.util.List,com.here.sdk.routing.BicycleOptions,com.here.sdk.routing.CalculateRouteCallback))

Will be removed in v4.28.0. Use the `calculate_route()` methods with RoutingOptions parameter instead.

[com.here.sdk.routing.RoutingInterface.calculateRoute(List\<Waypoint\>, BusOptions, CalculateRouteCallback)](sdk-for-android-explore-api-reference-latestroutinginterface#calculateRoute(java.util.List,com.here.sdk.routing.BusOptions,com.here.sdk.routing.CalculateRouteCallback))

Will be removed in v4.28.0. Use the `calculate_route()` methods with RoutingOptions parameter instead.

[com.here.sdk.routing.RoutingInterface.calculateRoute(List\<Waypoint\>, CarOptions, CalculateRouteCallback)](sdk-for-android-explore-api-reference-latestroutinginterface#calculateRoute(java.util.List,com.here.sdk.routing.CarOptions,com.here.sdk.routing.CalculateRouteCallback))

Will be removed in v4.28.0. Use the `calculate_route()` methods with RoutingOptions parameter instead.

[com.here.sdk.routing.RoutingInterface.calculateRoute(List\<Waypoint\>, EVCarOptions, CalculateRouteCallback)](sdk-for-android-explore-api-reference-latestroutinginterface#calculateRoute(java.util.List,com.here.sdk.routing.EVCarOptions,com.here.sdk.routing.CalculateRouteCallback))

Will be removed in v4.28.0. Use the `calculate_route()` methods with RoutingOptions parameter instead.

[com.here.sdk.routing.RoutingInterface.calculateRoute(List\<Waypoint\>, EVTruckOptions, CalculateRouteCallback)](sdk-for-android-explore-api-reference-latestroutinginterface#calculateRoute(java.util.List,com.here.sdk.routing.EVTruckOptions,com.here.sdk.routing.CalculateRouteCallback))

Will be removed in v4.28.0. Use the `calculate_route()` methods with RoutingOptions parameter instead.

[com.here.sdk.routing.RoutingInterface.calculateRoute(List\<Waypoint\>, PedestrianOptions, CalculateRouteCallback)](sdk-for-android-explore-api-reference-latestroutinginterface#calculateRoute(java.util.List,com.here.sdk.routing.PedestrianOptions,com.here.sdk.routing.CalculateRouteCallback))

Will be removed in v4.28.0. Use the `calculate_route()` methods with RoutingOptions parameter instead.

[com.here.sdk.routing.RoutingInterface.calculateRoute(List\<Waypoint\>, PrivateBusOptions, CalculateRouteCallback)](sdk-for-android-explore-api-reference-latestroutinginterface#calculateRoute(java.util.List,com.here.sdk.routing.PrivateBusOptions,com.here.sdk.routing.CalculateRouteCallback))

Will be removed in v4.28.0. Use the `calculate_route()` methods with RoutingOptions parameter instead.

[com.here.sdk.routing.RoutingInterface.calculateRoute(List\<Waypoint\>, ScooterOptions, CalculateRouteCallback)](sdk-for-android-explore-api-reference-latestroutinginterface#calculateRoute(java.util.List,com.here.sdk.routing.ScooterOptions,com.here.sdk.routing.CalculateRouteCallback))

Will be removed in v4.28.0. Use the `calculate_route()` methods with RoutingOptions parameter instead.

[com.here.sdk.routing.RoutingInterface.calculateRoute(List\<Waypoint\>, TaxiOptions, CalculateRouteCallback)](sdk-for-android-explore-api-reference-latestroutinginterface#calculateRoute(java.util.List,com.here.sdk.routing.TaxiOptions,com.here.sdk.routing.CalculateRouteCallback))

Will be removed in v4.28.0. Use the `calculate_route()` methods with RoutingOptions parameter instead.

[com.here.sdk.routing.RoutingInterface.calculateRoute(List\<Waypoint\>, TruckOptions, CalculateRouteCallback)](sdk-for-android-explore-api-reference-latestroutinginterface#calculateRoute(java.util.List,com.here.sdk.routing.TruckOptions,com.here.sdk.routing.CalculateRouteCallback))

Will be removed in v4.28.0. Use the `calculate_route()` methods with RoutingOptions parameter instead.

<!-- -->

Deprecated Constructors

Constructor

  Description

  [com.here.sdk.routing.IsolineOptions(IsolineOptions.Calculation, CarOptions)](sdk-for-android-explore-api-reference-latestisolineoptions#%3Cinit%3E(com.here.sdk.routing.IsolineOptions.Calculation,com.here.sdk.routing.CarOptions))

Will be removed in v4.28.0. Use the constructor with `RoutingOptions` parameter instead.

[com.here.sdk.routing.IsolineOptions(IsolineOptions.Calculation, EVCarOptions)](sdk-for-android-explore-api-reference-latestisolineoptions#%3Cinit%3E(com.here.sdk.routing.IsolineOptions.Calculation,com.here.sdk.routing.EVCarOptions))

Will be removed in v4.28.0. Use the constructor with `RoutingOptions` parameter instead.

[com.here.sdk.routing.IsolineOptions(IsolineOptions.Calculation, EVTruckOptions)](sdk-for-android-explore-api-reference-latestisolineoptions#%3Cinit%3E(com.here.sdk.routing.IsolineOptions.Calculation,com.here.sdk.routing.EVTruckOptions))

Will be removed in v4.28.0. Use the constructor with `RoutingOptions` parameter instead.

[com.here.sdk.routing.IsolineOptions(IsolineOptions.Calculation, TruckOptions)](sdk-for-android-explore-api-reference-latestisolineoptions#%3Cinit%3E(com.here.sdk.routing.IsolineOptions.Calculation,com.here.sdk.routing.TruckOptions))

Will be removed in v4.28.0. Use the constructor with `RoutingOptions` parameter instead.

<!-- -->

Deprecated Enum Constants

Enum Constant

  Description

  [com.here.sdk.routing.ChargingConnectorType.TESLA](sdk-for-android-explore-api-reference-latestchargingconnectortype#TESLA)

Will be removed in v4.28.0, use [`ChargingConnectorType.SAE_J3400`](sdk-for-android-explore-api-reference-latestchargingconnectortype#SAE_J3400) instead.
