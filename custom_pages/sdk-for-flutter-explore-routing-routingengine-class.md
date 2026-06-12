---
title: "RoutingEngine class abstract"
slug: "sdk-for-flutter-explore-routing-routingengine-class"
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
<ul><li><a href="/sdk-for-flutter-explore-routing-routingengine-routingengine">RoutingEngine</a></li><li><a href="/sdk-for-flutter-explore-routing-routingengine-routingengine-withconnectionsettings">RoutingEngine.withConnectionSettings</a></li><li><a href="/sdk-for-flutter-explore-routing-routingengine-routingengine-withsdkengine">RoutingEngine.withSdkEngine</a></li><li><a href="/sdk-for-flutter-explore-routing-routingengine-routingengine-withsdkengineandconnectionsettings">RoutingEngine.withSdkEngineAndConnectionSettings</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="/sdk-for-flutter-explore-routing-routinginterface-hashcode">hashCode</a></li><li><a href="/sdk-for-flutter-explore-routing-routinginterface-runtimetype">runtimeType</a></li></ul>


<h2>Methods</h2>
<ul><li><a class="deprecated" href="/sdk-for-flutter-explore-routing-routinginterface-calculatebicycleroute">calculateBicycleRoute</a></li><li><a class="deprecated" href="/sdk-for-flutter-explore-routing-routinginterface-calculatebusroute">calculateBusRoute</a></li><li><a class="deprecated" href="/sdk-for-flutter-explore-routing-routinginterface-calculatecarroute">calculateCarRoute</a></li><li><a class="deprecated" href="/sdk-for-flutter-explore-routing-routinginterface-calculateevcarroute">calculateEVCarRoute</a></li><li><a class="deprecated" href="/sdk-for-flutter-explore-routing-routinginterface-calculateevtruckroute">calculateEVTruckRoute</a></li><li><a class="deprecated" href="/sdk-for-flutter-explore-routing-routinginterface-calculatepedestrianroute">calculatePedestrianRoute</a></li><li><a class="deprecated" href="/sdk-for-flutter-explore-routing-routinginterface-calculateprivatebusroute">calculatePrivateBusRoute</a></li><li><a href="/sdk-for-flutter-explore-routing-routinginterface-calculateroutewithroutingoptions">calculateRouteWithRoutingOptions</a></li><li><a class="deprecated" href="/sdk-for-flutter-explore-routing-routinginterface-calculatescooterroute">calculateScooterRoute</a></li><li><a class="deprecated" href="/sdk-for-flutter-explore-routing-routinginterface-calculatetaxiroute">calculateTaxiRoute</a></li><li><a href="/sdk-for-flutter-explore-routing-routingengine-calculatetrafficonroute">calculateTrafficOnRoute</a></li><li><a href="/sdk-for-flutter-explore-routing-routingengine-calculatetrafficonroutewithcurrentcharge">calculateTrafficOnRouteWithCurrentCharge</a></li><li><a class="deprecated" href="/sdk-for-flutter-explore-routing-routinginterface-calculatetruckroute">calculateTruckRoute</a></li><li><a class="deprecated" href="/sdk-for-flutter-explore-routing-routingengine-importbicycleroute">importBicycleRoute</a></li><li><a class="deprecated" href="/sdk-for-flutter-explore-routing-routingengine-importbicycleroutewithstops">importBicycleRouteWithStops</a></li><li><a class="deprecated" href="/sdk-for-flutter-explore-routing-routingengine-importbusroute">importBusRoute</a></li><li><a class="deprecated" href="/sdk-for-flutter-explore-routing-routingengine-importbusroutewithstops">importBusRouteWithStops</a></li><li><a class="deprecated" href="/sdk-for-flutter-explore-routing-routingengine-importcarroute">importCarRoute</a></li><li><a class="deprecated" href="/sdk-for-flutter-explore-routing-routingengine-importcarroutewithstops">importCarRouteWithStops</a></li><li><a class="deprecated" href="/sdk-for-flutter-explore-routing-routingengine-importevcarroute">importEVCarRoute</a></li><li><a class="deprecated" href="/sdk-for-flutter-explore-routing-routingengine-importevcarroutewithstops">importEVCarRouteWithStops</a></li><li><a class="deprecated" href="/sdk-for-flutter-explore-routing-routingengine-importevtruckroute">importEVTruckRoute</a></li><li><a class="deprecated" href="/sdk-for-flutter-explore-routing-routingengine-importevtruckroutewithstops">importEVTruckRouteWithStops</a></li><li><a class="deprecated" href="/sdk-for-flutter-explore-routing-routingengine-importpedestrianroute">importPedestrianRoute</a></li><li><a class="deprecated" href="/sdk-for-flutter-explore-routing-routingengine-importpedestrianroutewithstops">importPedestrianRouteWithStops</a></li><li><a class="deprecated" href="/sdk-for-flutter-explore-routing-routingengine-importprivatebusroute">importPrivateBusRoute</a></li><li><a class="deprecated" href="/sdk-for-flutter-explore-routing-routingengine-importprivatebusroutewithstops">importPrivateBusRouteWithStops</a></li><li><a class="deprecated" href="/sdk-for-flutter-explore-routing-routingengine-importroutefromhandle">importRouteFromHandle</a></li><li><a href="/sdk-for-flutter-explore-routing-routingengine-importroutefromhandlewithroutingoptions">importRouteFromHandleWithRoutingOptions</a></li><li><a href="/sdk-for-flutter-explore-routing-routingengine-importroutewithroutingoptions">importRouteWithRoutingOptions</a></li><li><a href="/sdk-for-flutter-explore-routing-routingengine-importroutewithstopsandroutingoptions">importRouteWithStopsAndRoutingOptions</a></li><li><a class="deprecated" href="/sdk-for-flutter-explore-routing-routingengine-importscooterroute">importScooterRoute</a></li><li><a class="deprecated" href="/sdk-for-flutter-explore-routing-routingengine-importscooterroutewithstops">importScooterRouteWithStops</a></li><li><a class="deprecated" href="/sdk-for-flutter-explore-routing-routingengine-importtaxiroute">importTaxiRoute</a></li><li><a class="deprecated" href="/sdk-for-flutter-explore-routing-routingengine-importtaxiroutewithstops">importTaxiRouteWithStops</a></li><li><a class="deprecated" href="/sdk-for-flutter-explore-routing-routingengine-importtruckroute">importTruckRoute</a></li><li><a class="deprecated" href="/sdk-for-flutter-explore-routing-routingengine-importtruckroutewithstops">importTruckRouteWithStops</a></li><li><a href="/sdk-for-flutter-explore-routing-routinginterface-nosuchmethod">noSuchMethod</a></li><li><a class="deprecated" href="/sdk-for-flutter-explore-routing-routingengine-refreshroute">refreshRoute</a></li><li><a href="/sdk-for-flutter-explore-routing-routingengine-refreshroutewithroutehandleandrefreshrouteparameters">refreshRouteWithRouteHandleAndRefreshRouteParameters</a></li><li><a class="deprecated" href="/sdk-for-flutter-explore-routing-routingengine-refreshroutewithroutehandleandroutingoptions">refreshRouteWithRouteHandleAndRoutingOptions</a></li><li><a class="deprecated" href="/sdk-for-flutter-explore-routing-routingengine-refreshroutewithtraveleddistance">refreshRouteWithTraveledDistance</a></li><li><a class="deprecated" href="/sdk-for-flutter-explore-routing-routingengine-refreshroutewithtraveleddistanceandroutingoptions">refreshRouteWithTraveledDistanceAndRoutingOptions</a></li><li><a href="/sdk-for-flutter-explore-routing-routinginterface-returntoroutewithtraveleddistance">returnToRouteWithTraveledDistance</a></li><li><a href="/sdk-for-flutter-explore-routing-routingengine-setcustomoption">setCustomOption</a></li><li><a href="/sdk-for-flutter-explore-routing-routinginterface-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="/sdk-for-flutter-explore-routing-routinginterface-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>
