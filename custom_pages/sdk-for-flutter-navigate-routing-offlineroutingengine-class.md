---
title: "OfflineRoutingEngine class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-offlineroutingengine-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/OfflineRoutingEngine-class-sidebar.html">

<div>

# <span class="kind-class">OfflineRoutingEngine</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Use this class to calculate a route offline from A to B with a number of waypoints in between.

Route calculation is done asynchronously, and requires map data that is available offline. This can be temporarily cached map data or downloaded offline map data stored in the persisted storage via `MapDownloader`. Note that when using the cache there is a risk of missing data and this may reduce the overall quality of the route or can result in a <a href="sdk-for-flutter-navigate-routing-routingerror">RoutingError.noRouteFound</a> error.

The resulting route contains various information such as the polyline, route length in meters, estimated time to traverse along the route and maneuver data, but it does not contain traffic information.

Unlike the `RoutingEngine` (which requires an online connection), this engine allows to use an unlimited number of waypoints.

As an alternative to this engine, consider to use the `RoutingEngine` for online route calculations to get fresher traffic, maneuver, route handles and street information, and to use a more elaborate algorithms to calculate the fastest route.

For offline bus routing, enable "OFFLINE_BUS_ROUTING" as feature configuration. For more details, please look at <a href="sdk-for-flutter-navigate-core-engine-sdkoptions-class">SDKOptions</a>. If this feature is not enabled, the engine may not be able to find bus routes.

**Note:** EV routing is available when calculating a route using the <a href="sdk-for-flutter-navigate-routing-routingoptions-class">RoutingOptions</a>, by setting the <a href="sdk-for-flutter-navigate-routing-routingoptions-evoptions">RoutingOptions.evOptions</a>.

**Note:** Traffic related information is completely excluded. No historic traffic patterns are taking into consideration for the ETA. Currently blocked or closed roads or roads with traffic incident are not considered offline, i.e. the road may pass through such road. Only seasonal road closures are considered based on the departure time, if given. Traffic information is only considered for online route calculation with the `RoutingEngine`.

**Note:** Route handles produced by this engine are not compatible with those created by the `RoutingEngine`. Importing, refreshing, or returning to a route via a route handle is supported only when the route was calculated with the same engine. However, this engine supports returning to a route calculated with the `RoutingEngine` when the route object is provided.

</div>

<div class="section">

Implemented types  
- <a href="sdk-for-flutter-navigate-routing-routinginterface-class">RoutingInterface</a>

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-routing-offlineroutingengine-offlineroutingengine">OfflineRoutingEngine</a></span><span class="signature">()</span>  
Creates a new instance of this class.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-offlineroutingengine-offlineroutingengine-withsdkengine">OfflineRoutingEngine.withSdkEngine</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withSdkEngine-param-sdkEngine" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a></span> <span class="parameter-name">sdkEngine</span></span>)</span>  
Creates a new instance of OfflineRoutingEngine.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-offlineroutingengine-offlineroutingengine-withsdkengineandoptions">OfflineRoutingEngine.withSdkEngineAndOptions</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withSdkEngineAndOptions-param-sdkEngine" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a></span> <span class="parameter-name">sdkEngine</span>, </span><span id="sdk-for-flutter-navigate-withSdkEngineAndOptions-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-offlineroutingengineoptions-class">OfflineRoutingEngineOptions</a></span> <span class="parameter-name">options</span></span>)</span>  
Creates a new instance of OfflineRoutingEngine.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-routing-routinginterface-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-routinginterface-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-offlineroutingengine-trafficdataprovider">trafficDataProvider</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-traffic-trafficdataprovider-class">TrafficDataProvider</a>?</span>  
The traffic data provider that gets internal traffic information considering in routing. If the traffic data provider is `null`, traffic is not considered in routing. Gets the traffic data provider that provides internal traffic information considering in routing.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name deprecated"><a href="sdk-for-flutter-navigate-routing-routinginterface-calculatebicycleroute" class="deprecated">calculateBicycleRoute</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-calculateBicycleRoute-param-waypoints" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-waypoint-class">Waypoint</a></span>\></span></span> <span class="parameter-name">waypoints</span>, </span><span id="sdk-for-flutter-navigate-calculateBicycleRoute-param-bicycleOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-bicycleoptions-class" class="deprecated">BicycleOptions</a></span> <span class="parameter-name">bicycleOptions</span>, </span><span id="sdk-for-flutter-navigate-calculateBicycleRoute-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-calculateroutecallback">CalculateRouteCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Asynchronously calculates a bicycle route from one point to another, passing through the given waypoints in the given order.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name deprecated"><a href="sdk-for-flutter-navigate-routing-routinginterface-calculatebusroute" class="deprecated">calculateBusRoute</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-calculateBusRoute-param-waypoints" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-waypoint-class">Waypoint</a></span>\></span></span> <span class="parameter-name">waypoints</span>, </span><span id="sdk-for-flutter-navigate-calculateBusRoute-param-busOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-busoptions-class" class="deprecated">BusOptions</a></span> <span class="parameter-name">busOptions</span>, </span><span id="sdk-for-flutter-navigate-calculateBusRoute-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-calculateroutecallback">CalculateRouteCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Asynchronously calculates a bus route from one point to another, passing through the given waypoints in the given order.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name deprecated"><a href="sdk-for-flutter-navigate-routing-routinginterface-calculatecarroute" class="deprecated">calculateCarRoute</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-calculateCarRoute-param-waypoints" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-waypoint-class">Waypoint</a></span>\></span></span> <span class="parameter-name">waypoints</span>, </span><span id="sdk-for-flutter-navigate-calculateCarRoute-param-carOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-caroptions-class" class="deprecated">CarOptions</a></span> <span class="parameter-name">carOptions</span>, </span><span id="sdk-for-flutter-navigate-calculateCarRoute-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-calculateroutecallback">CalculateRouteCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Asynchronously calculates a car route from one point to another, passing through the given waypoints in the given order.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name deprecated"><a href="sdk-for-flutter-navigate-routing-routinginterface-calculateevcarroute" class="deprecated">calculateEVCarRoute</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-calculateEVCarRoute-param-waypoints" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-waypoint-class">Waypoint</a></span>\></span></span> <span class="parameter-name">waypoints</span>, </span><span id="sdk-for-flutter-navigate-calculateEVCarRoute-param-evCarOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-evcaroptions-class" class="deprecated">EVCarOptions</a></span> <span class="parameter-name">evCarOptions</span>, </span><span id="sdk-for-flutter-navigate-calculateEVCarRoute-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-calculateroutecallback">CalculateRouteCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Asynchronously calculates an electric car route from one point to another, passing through the given waypoints in the given order.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name deprecated"><a href="sdk-for-flutter-navigate-routing-routinginterface-calculateevtruckroute" class="deprecated">calculateEVTruckRoute</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-calculateEVTruckRoute-param-waypoints" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-waypoint-class">Waypoint</a></span>\></span></span> <span class="parameter-name">waypoints</span>, </span><span id="sdk-for-flutter-navigate-calculateEVTruckRoute-param-evTruckOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-evtruckoptions-class" class="deprecated">EVTruckOptions</a></span> <span class="parameter-name">evTruckOptions</span>, </span><span id="sdk-for-flutter-navigate-calculateEVTruckRoute-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-calculateroutecallback">CalculateRouteCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Asynchronously calculates an electic truck route from one point to another, passing through the given waypoints in the given order.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name deprecated"><a href="sdk-for-flutter-navigate-routing-routinginterface-calculatepedestrianroute" class="deprecated">calculatePedestrianRoute</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-calculatePedestrianRoute-param-waypoints" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-waypoint-class">Waypoint</a></span>\></span></span> <span class="parameter-name">waypoints</span>, </span><span id="sdk-for-flutter-navigate-calculatePedestrianRoute-param-pedestrianOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-pedestrianoptions-class" class="deprecated">PedestrianOptions</a></span> <span class="parameter-name">pedestrianOptions</span>, </span><span id="sdk-for-flutter-navigate-calculatePedestrianRoute-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-calculateroutecallback">CalculateRouteCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Asynchronously calculates a pedestrian route from one point to another, passing through the given waypoints in the given order.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name deprecated"><a href="sdk-for-flutter-navigate-routing-routinginterface-calculateprivatebusroute" class="deprecated">calculatePrivateBusRoute</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-calculatePrivateBusRoute-param-waypoints" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-waypoint-class">Waypoint</a></span>\></span></span> <span class="parameter-name">waypoints</span>, </span><span id="sdk-for-flutter-navigate-calculatePrivateBusRoute-param-privateBusOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-privatebusoptions-class" class="deprecated">PrivateBusOptions</a></span> <span class="parameter-name">privateBusOptions</span>, </span><span id="sdk-for-flutter-navigate-calculatePrivateBusRoute-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-calculateroutecallback">CalculateRouteCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Asynchronously calculates a private bus route from one point to another, passing through the given waypoints in the given order.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-routinginterface-calculateroutewithroutingoptions">calculateRouteWithRoutingOptions</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-calculateRouteWithRoutingOptions-param-waypoints" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-waypoint-class">Waypoint</a></span>\></span></span> <span class="parameter-name">waypoints</span>, </span><span id="sdk-for-flutter-navigate-calculateRouteWithRoutingOptions-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-routingoptions-class">RoutingOptions</a></span> <span class="parameter-name">options</span>, </span><span id="sdk-for-flutter-navigate-calculateRouteWithRoutingOptions-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-calculateroutecallback">CalculateRouteCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Asynchronously calculates a route from one point to another, passing through the given waypoints in the given order.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name deprecated"><a href="sdk-for-flutter-navigate-routing-routinginterface-calculatescooterroute" class="deprecated">calculateScooterRoute</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-calculateScooterRoute-param-waypoints" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-waypoint-class">Waypoint</a></span>\></span></span> <span class="parameter-name">waypoints</span>, </span><span id="sdk-for-flutter-navigate-calculateScooterRoute-param-scooterOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-scooteroptions-class" class="deprecated">ScooterOptions</a></span> <span class="parameter-name">scooterOptions</span>, </span><span id="sdk-for-flutter-navigate-calculateScooterRoute-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-calculateroutecallback">CalculateRouteCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Asynchronously calculates a scooter route from one point to another, passing through the given waypoints in the given order.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name deprecated"><a href="sdk-for-flutter-navigate-routing-routinginterface-calculatetaxiroute" class="deprecated">calculateTaxiRoute</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-calculateTaxiRoute-param-waypoints" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-waypoint-class">Waypoint</a></span>\></span></span> <span class="parameter-name">waypoints</span>, </span><span id="sdk-for-flutter-navigate-calculateTaxiRoute-param-taxiOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-taxioptions-class" class="deprecated">TaxiOptions</a></span> <span class="parameter-name">taxiOptions</span>, </span><span id="sdk-for-flutter-navigate-calculateTaxiRoute-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-calculateroutecallback">CalculateRouteCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Asynchronously calculates a taxi route from one point to another, passing through the given waypoints in the given order.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name deprecated"><a href="sdk-for-flutter-navigate-routing-routinginterface-calculatetruckroute" class="deprecated">calculateTruckRoute</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-calculateTruckRoute-param-waypoints" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-waypoint-class">Waypoint</a></span>\></span></span> <span class="parameter-name">waypoints</span>, </span><span id="sdk-for-flutter-navigate-calculateTruckRoute-param-truckOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-truckoptions-class" class="deprecated">TruckOptions</a></span> <span class="parameter-name">truckOptions</span>, </span><span id="sdk-for-flutter-navigate-calculateTruckRoute-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-calculateroutecallback">CalculateRouteCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Asynchronously calculates a truck route from one point to another, passing through the given waypoints in the given order.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-offlineroutingengine-importfromhandlewithroutingoptions">importFromHandleWithRoutingOptions</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-importFromHandleWithRoutingOptions-param-routeHandle" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-routehandle-class">RouteHandle</a></span> <span class="parameter-name">routeHandle</span>, </span><span id="sdk-for-flutter-navigate-importFromHandleWithRoutingOptions-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-routingoptions-class">RoutingOptions</a></span> <span class="parameter-name">options</span>, </span><span id="sdk-for-flutter-navigate-importFromHandleWithRoutingOptions-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-calculateroutecallback">CalculateRouteCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Asynchronously recreates a route from the <a href="sdk-for-flutter-navigate-routing-routehandle-class">RouteHandle</a> provided, i.e.

<span class="name deprecated"><a href="sdk-for-flutter-navigate-routing-offlineroutingengine-importroutefromhandle" class="deprecated">importRouteFromHandle</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-importRouteFromHandle-param-routeHandle" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-routehandle-class">RouteHandle</a></span> <span class="parameter-name">routeHandle</span>, </span><span id="sdk-for-flutter-navigate-importRouteFromHandle-param-refreshRouteOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-refreshrouteoptions-class" class="deprecated">RefreshRouteOptions</a></span> <span class="parameter-name">refreshRouteOptions</span>, </span><span id="sdk-for-flutter-navigate-importRouteFromHandle-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-calculateroutecallback">CalculateRouteCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Asynchronously recreates a route from the <a href="sdk-for-flutter-navigate-routing-routehandle-class">RouteHandle</a> provided, i.e.

<span class="name"><a href="sdk-for-flutter-navigate-routing-routinginterface-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-offlineroutingengine-refreshroutewithroutehandleandrefreshrouteparameters">refreshRouteWithRouteHandleAndRefreshRouteParameters</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-refreshRouteWithRouteHandleAndRefreshRouteParameters-param-refreshRouteParameters" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-refreshrouteparameters-class">RefreshRouteParameters</a></span> <span class="parameter-name">refreshRouteParameters</span>, </span><span id="sdk-for-flutter-navigate-refreshRouteWithRouteHandleAndRefreshRouteParameters-param-routingOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-routingoptions-class">RoutingOptions</a></span> <span class="parameter-name">routingOptions</span>, </span><span id="sdk-for-flutter-navigate-refreshRouteWithRouteHandleAndRefreshRouteParameters-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-calculateroutecallback">CalculateRouteCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Asynchronously refreshes a previously calculated route from the provided <a href="sdk-for-flutter-navigate-routing-routehandle-class">RouteHandle</a>, updating the starting point and route metadata based on <a href="sdk-for-flutter-navigate-routing-routingoptions-class">RoutingOptions</a>.

<span class="name"><a href="sdk-for-flutter-navigate-routing-routinginterface-returntoroutewithtraveleddistance">returnToRouteWithTraveledDistance</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-returnToRouteWithTraveledDistance-param-route" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-route-class">Route</a></span> <span class="parameter-name">route</span>, </span><span id="sdk-for-flutter-navigate-returnToRouteWithTraveledDistance-param-startingPoint" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-waypoint-class">Waypoint</a></span> <span class="parameter-name">startingPoint</span>, </span><span id="sdk-for-flutter-navigate-returnToRouteWithTraveledDistance-param-lastTraveledSectionIndex" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">lastTraveledSectionIndex</span>, </span><span id="sdk-for-flutter-navigate-returnToRouteWithTraveledDistance-param-traveledDistanceOnLastSectionInMeters" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">traveledDistanceOnLastSectionInMeters</span>, </span><span id="sdk-for-flutter-navigate-returnToRouteWithTraveledDistance-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-calculateroutecallback">CalculateRouteCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Asynchronously calculates a new route that leads back to the original route.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-offlineroutingengine-setinternaloption">setInternalOption</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setInternalOption-param-key" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">key</span>, </span><span id="sdk-for-flutter-navigate-setInternalOption-param-value" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">value</span></span>) <span class="returntype parameter">→ void</span> </span>  
This method sets internal options that controls offline route calculation behavior.

<span class="name"><a href="sdk-for-flutter-navigate-routing-routinginterface-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-routing-routinginterface-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

