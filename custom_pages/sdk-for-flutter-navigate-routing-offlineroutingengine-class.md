---
title: "OfflineRoutingEngine class abstract"
slug: "sdk-for-flutter-navigate-routing-offlineroutingengine-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- OfflineRoutingEngine-class.html -->


<div>
<h1>OfflineRoutingEngine class abstract</h1></div>

<p>Use this class to calculate a route offline from A to B with
a number of waypoints in between.</p>
<p>Route calculation is done asynchronously, and requires map data that is
available offline. This can be temporarily cached map data or downloaded
offline map data stored in the persisted storage via <code>MapDownloader</code>.
Note that when using the cache there is a risk of missing data and this may
reduce the overall quality of the route or can result in a
<a href="sdk-for-flutter-navigate-routing-routingerror">RoutingError.noRouteFound</a> error.</p>
<p>The resulting route contains various information such as the polyline,
route length in meters, estimated time to traverse along the route
and maneuver data, but it does not contain traffic information.</p>
<p>Unlike the <code>RoutingEngine</code> (which requires an online connection), this engine
allows to use an unlimited number of waypoints.</p>
<p>As an alternative to this engine, consider to use the <code>RoutingEngine</code> for online
route calculations to get fresher traffic, maneuver, route handles and street
information, and to use a more elaborate algorithms to calculate the fastest route.</p>
<p>For offline bus routing, enable "OFFLINE_BUS_ROUTING" as feature configuration.
For more details, please look at <a href="sdk-for-flutter-navigate-core-engine-sdkoptions-class">SDKOptions</a>. If this feature is not
enabled, the engine may not be able to find bus routes.</p>
<p><strong>Note:</strong> EV routing is available when calculating a route using the <a href="sdk-for-flutter-navigate-routing-routingoptions-class">RoutingOptions</a>, by setting
the <a href="sdk-for-flutter-navigate-routing-routingoptions-evoptions">RoutingOptions.evOptions</a>.</p>
<p><strong>Note:</strong> Traffic related information is completely excluded.
No historic traffic patterns are taking into consideration for the ETA.
Currently blocked or closed roads or roads with traffic incident are not considered offline, i.e.
the road may pass through such road.
Only seasonal road closures are considered based on the departure time, if given.
Traffic information is only considered for online route calculation with the <code>RoutingEngine</code>.</p>
<p><strong>Note:</strong> Route handles produced by this engine are not compatible with those created by
the <code>RoutingEngine</code>. Importing, refreshing, or returning to a route via a route
handle is supported only when the route was calculated with the same engine. However,
this engine supports returning to a route calculated with the <code>RoutingEngine</code> when
the route object is provided.</p>


<ul><li>Implemented types</li></ul>


<h2>Constructors</h2>
<ul><li><a href="sdk-for-flutter-navigate-routing-offlineroutingengine-offlineroutingengine">OfflineRoutingEngine</a></li><li><a href="sdk-for-flutter-navigate-routing-offlineroutingengine-offlineroutingengine-withsdkengine">OfflineRoutingEngine.withSdkEngine</a></li><li><a href="sdk-for-flutter-navigate-routing-offlineroutingengine-offlineroutingengine-withsdkengineandoptions">OfflineRoutingEngine.withSdkEngineAndOptions</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="sdk-for-flutter-navigate-routing-routinginterface-hashcode">hashCode</a></li><li><a href="sdk-for-flutter-navigate-routing-routinginterface-runtimetype">runtimeType</a></li><li><a href="sdk-for-flutter-navigate-routing-offlineroutingengine-trafficdataprovider">trafficDataProvider</a></li></ul>


<h2>Methods</h2>
<ul><li><a class="deprecated" href="sdk-for-flutter-navigate-routing-routinginterface-calculatebicycleroute">calculateBicycleRoute</a></li><li><a class="deprecated" href="sdk-for-flutter-navigate-routing-routinginterface-calculatebusroute">calculateBusRoute</a></li><li><a class="deprecated" href="sdk-for-flutter-navigate-routing-routinginterface-calculatecarroute">calculateCarRoute</a></li><li><a class="deprecated" href="sdk-for-flutter-navigate-routing-routinginterface-calculateevcarroute">calculateEVCarRoute</a></li><li><a class="deprecated" href="sdk-for-flutter-navigate-routing-routinginterface-calculateevtruckroute">calculateEVTruckRoute</a></li><li><a class="deprecated" href="sdk-for-flutter-navigate-routing-routinginterface-calculatepedestrianroute">calculatePedestrianRoute</a></li><li><a class="deprecated" href="sdk-for-flutter-navigate-routing-routinginterface-calculateprivatebusroute">calculatePrivateBusRoute</a></li><li><a href="sdk-for-flutter-navigate-routing-routinginterface-calculateroutewithroutingoptions">calculateRouteWithRoutingOptions</a></li><li><a class="deprecated" href="sdk-for-flutter-navigate-routing-routinginterface-calculatescooterroute">calculateScooterRoute</a></li><li><a class="deprecated" href="sdk-for-flutter-navigate-routing-routinginterface-calculatetaxiroute">calculateTaxiRoute</a></li><li><a class="deprecated" href="sdk-for-flutter-navigate-routing-routinginterface-calculatetruckroute">calculateTruckRoute</a></li><li><a href="sdk-for-flutter-navigate-routing-offlineroutingengine-importfromhandlewithroutingoptions">importFromHandleWithRoutingOptions</a></li><li><a class="deprecated" href="sdk-for-flutter-navigate-routing-offlineroutingengine-importroutefromhandle">importRouteFromHandle</a></li><li><a href="sdk-for-flutter-navigate-routing-routinginterface-nosuchmethod">noSuchMethod</a></li><li><a href="sdk-for-flutter-navigate-routing-offlineroutingengine-refreshroutewithroutehandleandrefreshrouteparameters">refreshRouteWithRouteHandleAndRefreshRouteParameters</a></li><li><a href="sdk-for-flutter-navigate-routing-routinginterface-returntoroutewithtraveleddistance">returnToRouteWithTraveledDistance</a></li><li><a href="sdk-for-flutter-navigate-routing-offlineroutingengine-setinternaloption">setInternalOption</a></li><li><a href="sdk-for-flutter-navigate-routing-routinginterface-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="sdk-for-flutter-navigate-routing-routinginterface-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>
