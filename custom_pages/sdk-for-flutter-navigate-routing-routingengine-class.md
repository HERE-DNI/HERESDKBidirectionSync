---
title: "RoutingEngine class abstract"
slug: "sdk-for-flutter-navigate-routing-routingengine-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RoutingEngine-class.html -->


<div>
<h1>RoutingEngine class abstract</h1></div>

<p>Use the RoutingEngine to calculate a route from A to B with
a number of waypoints in between.</p>
<p>Route calculation is done asynchronously and requires an
online connection. The resulting route contains various
information such as the polyline, route length in meters,
estimated time to traverse along the route and maneuver data.</p>
<p><strong>Note:</strong> The engine does not support an unlimited number of waypoints.
The limit is defined by the HERE backend services and may change. For now,
the maximum number of waypoints should be below 200. This value may change
and it is not guaranteed to be stable. If you need to support very large lists
of waypoints, consider to import a route (see <code>importRoute()</code> method) or use
the <code>OfflineRoutingEngine</code> which supports an unlimited number of waypoints.
The <code>OfflineRoutingEngine</code> is only available for Navigate licence.</p>


<ul><li>Implemented types</li></ul>


<h2>Constructors</h2>
<ul><li><a href="/sdk-for-flutter-navigate-routing-routingengine-routingengine">RoutingEngine</a></li><li><a href="/sdk-for-flutter-navigate-routing-routingengine-routingengine-withconnectionsettings">RoutingEngine.withConnectionSettings</a></li><li><a href="/sdk-for-flutter-navigate-routing-routingengine-routingengine-withsdkengine">RoutingEngine.withSdkEngine</a></li><li><a href="/sdk-for-flutter-navigate-routing-routingengine-routingengine-withsdkengineandconnectionsettings">RoutingEngine.withSdkEngineAndConnectionSettings</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="/sdk-for-flutter-navigate-routing-routinginterface-hashcode">hashCode</a></li><li><a href="/sdk-for-flutter-navigate-routing-routinginterface-runtimetype">runtimeType</a></li></ul>


<h2>Methods</h2>
<ul><li><a class="deprecated" href="/sdk-for-flutter-navigate-routing-routinginterface-calculatebicycleroute">calculateBicycleRoute</a></li><li><a class="deprecated" href="/sdk-for-flutter-navigate-routing-routinginterface-calculatebusroute">calculateBusRoute</a></li><li><a class="deprecated" href="/sdk-for-flutter-navigate-routing-routinginterface-calculatecarroute">calculateCarRoute</a></li><li><a class="deprecated" href="/sdk-for-flutter-navigate-routing-routinginterface-calculateevcarroute">calculateEVCarRoute</a></li><li><a class="deprecated" href="/sdk-for-flutter-navigate-routing-routinginterface-calculateevtruckroute">calculateEVTruckRoute</a></li><li><a class="deprecated" href="/sdk-for-flutter-navigate-routing-routinginterface-calculatepedestrianroute">calculatePedestrianRoute</a></li><li><a class="deprecated" href="/sdk-for-flutter-navigate-routing-routinginterface-calculateprivatebusroute">calculatePrivateBusRoute</a></li><li><a href="/sdk-for-flutter-navigate-routing-routinginterface-calculateroutewithroutingoptions">calculateRouteWithRoutingOptions</a></li><li><a class="deprecated" href="/sdk-for-flutter-navigate-routing-routinginterface-calculatescooterroute">calculateScooterRoute</a></li><li><a class="deprecated" href="/sdk-for-flutter-navigate-routing-routinginterface-calculatetaxiroute">calculateTaxiRoute</a></li><li><a href="/sdk-for-flutter-navigate-routing-routingengine-calculatetrafficonroute">calculateTrafficOnRoute</a></li><li><a href="/sdk-for-flutter-navigate-routing-routingengine-calculatetrafficonroutewithcurrentcharge">calculateTrafficOnRouteWithCurrentCharge</a></li><li><a class="deprecated" href="/sdk-for-flutter-navigate-routing-routinginterface-calculatetruckroute">calculateTruckRoute</a></li><li><a class="deprecated" href="/sdk-for-flutter-navigate-routing-routingengine-importbicycleroute">importBicycleRoute</a></li><li><a class="deprecated" href="/sdk-for-flutter-navigate-routing-routingengine-importbicycleroutewithstops">importBicycleRouteWithStops</a></li><li><a class="deprecated" href="/sdk-for-flutter-navigate-routing-routingengine-importbusroute">importBusRoute</a></li><li><a class="deprecated" href="/sdk-for-flutter-navigate-routing-routingengine-importbusroutewithstops">importBusRouteWithStops</a></li><li><a class="deprecated" href="/sdk-for-flutter-navigate-routing-routingengine-importcarroute">importCarRoute</a></li><li><a class="deprecated" href="/sdk-for-flutter-navigate-routing-routingengine-importcarroutewithstops">importCarRouteWithStops</a></li><li><a class="deprecated" href="/sdk-for-flutter-navigate-routing-routingengine-importevcarroute">importEVCarRoute</a></li><li><a class="deprecated" href="/sdk-for-flutter-navigate-routing-routingengine-importevcarroutewithstops">importEVCarRouteWithStops</a></li><li><a class="deprecated" href="/sdk-for-flutter-navigate-routing-routingengine-importevtruckroute">importEVTruckRoute</a></li><li><a class="deprecated" href="/sdk-for-flutter-navigate-routing-routingengine-importevtruckroutewithstops">importEVTruckRouteWithStops</a></li><li><a class="deprecated" href="/sdk-for-flutter-navigate-routing-routingengine-importpedestrianroute">importPedestrianRoute</a></li><li><a class="deprecated" href="/sdk-for-flutter-navigate-routing-routingengine-importpedestrianroutewithstops">importPedestrianRouteWithStops</a></li><li><a class="deprecated" href="/sdk-for-flutter-navigate-routing-routingengine-importprivatebusroute">importPrivateBusRoute</a></li><li><a class="deprecated" href="/sdk-for-flutter-navigate-routing-routingengine-importprivatebusroutewithstops">importPrivateBusRouteWithStops</a></li><li><a class="deprecated" href="/sdk-for-flutter-navigate-routing-routingengine-importroutefromhandle">importRouteFromHandle</a></li><li><a href="/sdk-for-flutter-navigate-routing-routingengine-importroutefromhandlewithroutingoptions">importRouteFromHandleWithRoutingOptions</a></li><li><a href="/sdk-for-flutter-navigate-routing-routingengine-importroutewithroutingoptions">importRouteWithRoutingOptions</a></li><li><a href="/sdk-for-flutter-navigate-routing-routingengine-importroutewithstopsandroutingoptions">importRouteWithStopsAndRoutingOptions</a></li><li><a class="deprecated" href="/sdk-for-flutter-navigate-routing-routingengine-importscooterroute">importScooterRoute</a></li><li><a class="deprecated" href="/sdk-for-flutter-navigate-routing-routingengine-importscooterroutewithstops">importScooterRouteWithStops</a></li><li><a class="deprecated" href="/sdk-for-flutter-navigate-routing-routingengine-importtaxiroute">importTaxiRoute</a></li><li><a class="deprecated" href="/sdk-for-flutter-navigate-routing-routingengine-importtaxiroutewithstops">importTaxiRouteWithStops</a></li><li><a class="deprecated" href="/sdk-for-flutter-navigate-routing-routingengine-importtruckroute">importTruckRoute</a></li><li><a class="deprecated" href="/sdk-for-flutter-navigate-routing-routingengine-importtruckroutewithstops">importTruckRouteWithStops</a></li><li><a href="/sdk-for-flutter-navigate-routing-routinginterface-nosuchmethod">noSuchMethod</a></li><li><a class="deprecated" href="/sdk-for-flutter-navigate-routing-routingengine-refreshroute">refreshRoute</a></li><li><a href="/sdk-for-flutter-navigate-routing-routingengine-refreshroutewithroutehandleandrefreshrouteparameters">refreshRouteWithRouteHandleAndRefreshRouteParameters</a></li><li><a class="deprecated" href="/sdk-for-flutter-navigate-routing-routingengine-refreshroutewithroutehandleandroutingoptions">refreshRouteWithRouteHandleAndRoutingOptions</a></li><li><a class="deprecated" href="/sdk-for-flutter-navigate-routing-routingengine-refreshroutewithtraveleddistance">refreshRouteWithTraveledDistance</a></li><li><a class="deprecated" href="/sdk-for-flutter-navigate-routing-routingengine-refreshroutewithtraveleddistanceandroutingoptions">refreshRouteWithTraveledDistanceAndRoutingOptions</a></li><li><a href="/sdk-for-flutter-navigate-routing-routinginterface-returntoroutewithtraveleddistance">returnToRouteWithTraveledDistance</a></li><li><a href="/sdk-for-flutter-navigate-routing-routingengine-setcustomoption">setCustomOption</a></li><li><a href="/sdk-for-flutter-navigate-routing-routinginterface-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="/sdk-for-flutter-navigate-routing-routinginterface-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>
