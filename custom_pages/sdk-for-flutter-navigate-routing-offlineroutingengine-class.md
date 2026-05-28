---
title: "OfflineRoutingEngine class abstract"
slug: "sdk-for-flutter-navigate-routing-offlineroutingengine-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- OfflineRoutingEngine-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="routing/OfflineRoutingEngine-class.html#constructors">Constructors</a></li>
<li><a href="routing/OfflineRoutingEngine/OfflineRoutingEngine.html">OfflineRoutingEngine</a></li>
<li><a href="routing/OfflineRoutingEngine/OfflineRoutingEngine.withSdkEngine.html">withSdkEngine</a></li>
<li><a href="routing/OfflineRoutingEngine/OfflineRoutingEngine.withSdkEngineAndOptions.html">withSdkEngineAndOptions</a></li>
<li class="section-title">
<a href="routing/OfflineRoutingEngine-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="routing/RoutingInterface/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="routing/RoutingInterface/runtimeType.html">runtimeType</a></li>
<li><a href="routing/OfflineRoutingEngine/trafficDataProvider.html">trafficDataProvider</a></li>
<li class="section-title"><a href="routing/OfflineRoutingEngine-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a class="deprecated" href="routing/RoutingInterface/calculateBicycleRoute.html">calculateBicycleRoute</a></li>
<li class="inherited"><a class="deprecated" href="routing/RoutingInterface/calculateBusRoute.html">calculateBusRoute</a></li>
<li class="inherited"><a class="deprecated" href="routing/RoutingInterface/calculateCarRoute.html">calculateCarRoute</a></li>
<li class="inherited"><a class="deprecated" href="routing/RoutingInterface/calculateEVCarRoute.html">calculateEVCarRoute</a></li>
<li class="inherited"><a class="deprecated" href="routing/RoutingInterface/calculateEVTruckRoute.html">calculateEVTruckRoute</a></li>
<li class="inherited"><a class="deprecated" href="routing/RoutingInterface/calculatePedestrianRoute.html">calculatePedestrianRoute</a></li>
<li class="inherited"><a class="deprecated" href="routing/RoutingInterface/calculatePrivateBusRoute.html">calculatePrivateBusRoute</a></li>
<li class="inherited"><a href="routing/RoutingInterface/calculateRouteWithRoutingOptions.html">calculateRouteWithRoutingOptions</a></li>
<li class="inherited"><a class="deprecated" href="routing/RoutingInterface/calculateScooterRoute.html">calculateScooterRoute</a></li>
<li class="inherited"><a class="deprecated" href="routing/RoutingInterface/calculateTaxiRoute.html">calculateTaxiRoute</a></li>
<li class="inherited"><a class="deprecated" href="routing/RoutingInterface/calculateTruckRoute.html">calculateTruckRoute</a></li>
<li><a href="routing/OfflineRoutingEngine/importFromHandleWithRoutingOptions.html">importFromHandleWithRoutingOptions</a></li>
<li><a class="deprecated" href="routing/OfflineRoutingEngine/importRouteFromHandle.html">importRouteFromHandle</a></li>
<li class="inherited"><a href="routing/RoutingInterface/noSuchMethod.html">noSuchMethod</a></li>
<li><a href="routing/OfflineRoutingEngine/refreshRouteWithRouteHandleAndRefreshRouteParameters.html">refreshRouteWithRouteHandleAndRefreshRouteParameters</a></li>
<li class="inherited"><a href="routing/RoutingInterface/returnToRouteWithTraveledDistance.html">returnToRouteWithTraveledDistance</a></li>
<li><a href="routing/OfflineRoutingEngine/setInternalOption.html">setInternalOption</a></li>
<li class="inherited"><a href="routing/RoutingInterface/toString.html">toString</a></li>
<li class="section-title inherited"><a href="routing/OfflineRoutingEngine-class.html#operators">Operators</a></li>
<li class="inherited"><a href="routing/RoutingInterface/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li class="self-crumb">OfflineRoutingEngine class</li>
</ol>
<div class="self-name">OfflineRoutingEngine</div>
<form class="search navbar-right" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-box" placeholder="Loading search..." type="text"/>
</form>
<div class="toggle" id="theme-button" title="Toggle brightness">
<label for="theme">
<input id="theme" type="checkbox" value="light-theme"/>

        dark_mode
      

        light_mode
      
</label>
</div>
</header>
<main>
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/OfflineRoutingEngine-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>OfflineRoutingEngine class abstract</h1></div>
<section class="desc markdown">
<p>Use this class to calculate a route offline from A to B with
a number of waypoints in between.</p>
<p>Route calculation is done asynchronously, and requires map data that is
available offline. This can be temporarily cached map data or downloaded
offline map data stored in the persisted storage via <code>MapDownloader</code>.
Note that when using the cache there is a risk of missing data and this may
reduce the overall quality of the route or can result in a
/sdk-for-flutter-navigate-routing-routingerror error.</p>
<p>The resulting route contains various information such as the polyline,
route length in meters, estimated time to traverse along the route
and maneuver data, but it does not contain traffic information.</p>
<p>Unlike the <code>RoutingEngine</code> (which requires an online connection), this engine
allows to use an unlimited number of waypoints.</p>
<p>As an alternative to this engine, consider to use the <code>RoutingEngine</code> for online
route calculations to get fresher traffic, maneuver, route handles and street
information, and to use a more elaborate algorithms to calculate the fastest route.</p>
<p>For offline bus routing, enable "OFFLINE_BUS_ROUTING" as feature configuration.
For more details, please look at /sdk-for-flutter-navigate-core-engine-sdkoptions-class. If this feature is not
enabled, the engine may not be able to find bus routes.</p>
<p><strong>Note:</strong> EV routing is available when calculating a route using the /sdk-for-flutter-navigate-routing-routingoptions-class, by setting
the /sdk-for-flutter-navigate-routing-routingoptions-evoptions.</p>
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
</section>
<section>
<dl class="dl-horizontal">
<dt>Implemented types</dt>
<dd>
<ul class="comma-separated clazz-relationships">
<li>/sdk-for-flutter-navigate-routing-routinginterface-class</li>
</ul>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="OfflineRoutingEngine">
/sdk-for-flutter-navigate-routing-offlineroutingengine-offlineroutingengine()
</dt>
<dd>
          Creates a new instance of this class.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="OfflineRoutingEngine.withSdkEngine">
/sdk-for-flutter-navigate-routing-offlineroutingengine-offlineroutingengine-withsdkengine(/sdk-for-flutter-navigate-core-engine-sdknativeengine-class sdkEngine)
</dt>
<dd>
          Creates a new instance of OfflineRoutingEngine.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="OfflineRoutingEngine.withSdkEngineAndOptions">
/sdk-for-flutter-navigate-routing-offlineroutingengine-offlineroutingengine-withsdkengineandoptions(/sdk-for-flutter-navigate-core-engine-sdknativeengine-class sdkEngine, /sdk-for-flutter-navigate-routing-offlineroutingengineoptions-class options)
</dt>
<dd>
          Creates a new instance of OfflineRoutingEngine.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-routing-routinginterface-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-routing-routinginterface-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="trafficDataProvider">
/sdk-for-flutter-navigate-routing-offlineroutingengine-trafficdataprovider
↔ /sdk-for-flutter-navigate-traffic-trafficdataprovider-class?
</dt>
<dd>
  The traffic data provider that gets internal traffic information considering in routing.
If the traffic data provider is <code>null</code>, traffic is not considered in routing.
Gets the traffic data provider that provides internal traffic information considering in routing.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="calculateBicycleRoute">
/sdk-for-flutter-navigate-routing-routinginterface-calculatebicycleroute(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-routing-waypoint-class&gt; waypoints, /sdk-for-flutter-navigate-routing-bicycleoptions-class bicycleOptions, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd class="inherited">
  Asynchronously calculates a bicycle route from one point to another,
passing through the given waypoints in the given order.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="calculateBusRoute">
/sdk-for-flutter-navigate-routing-routinginterface-calculatebusroute(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-routing-waypoint-class&gt; waypoints, /sdk-for-flutter-navigate-routing-busoptions-class busOptions, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd class="inherited">
  Asynchronously calculates a bus route from one point to another,
passing through the given waypoints in the given order.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="calculateCarRoute">
/sdk-for-flutter-navigate-routing-routinginterface-calculatecarroute(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-routing-waypoint-class&gt; waypoints, /sdk-for-flutter-navigate-routing-caroptions-class carOptions, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd class="inherited">
  Asynchronously calculates a car route from one point to another,
passing through the given waypoints in the given order.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="calculateEVCarRoute">
/sdk-for-flutter-navigate-routing-routinginterface-calculateevcarroute(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-routing-waypoint-class&gt; waypoints, /sdk-for-flutter-navigate-routing-evcaroptions-class evCarOptions, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd class="inherited">
  Asynchronously calculates an electric car route from one point to another,
passing through the given waypoints in the given order.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="calculateEVTruckRoute">
/sdk-for-flutter-navigate-routing-routinginterface-calculateevtruckroute(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-routing-waypoint-class&gt; waypoints, /sdk-for-flutter-navigate-routing-evtruckoptions-class evTruckOptions, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd class="inherited">
  Asynchronously calculates an electic truck route from one point to another,
passing through the given waypoints in the given order.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="calculatePedestrianRoute">
/sdk-for-flutter-navigate-routing-routinginterface-calculatepedestrianroute(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-routing-waypoint-class&gt; waypoints, /sdk-for-flutter-navigate-routing-pedestrianoptions-class pedestrianOptions, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd class="inherited">
  Asynchronously calculates a pedestrian route from one point to another,
passing through the given waypoints in the given order.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="calculatePrivateBusRoute">
/sdk-for-flutter-navigate-routing-routinginterface-calculateprivatebusroute(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-routing-waypoint-class&gt; waypoints, /sdk-for-flutter-navigate-routing-privatebusoptions-class privateBusOptions, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd class="inherited">
  Asynchronously calculates a private bus route from one point to another,
passing through the given waypoints in the given order.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="calculateRouteWithRoutingOptions">
/sdk-for-flutter-navigate-routing-routinginterface-calculateroutewithroutingoptions(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-routing-waypoint-class&gt; waypoints, /sdk-for-flutter-navigate-routing-routingoptions-class options, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd class="inherited">
  Asynchronously calculates a route from one point to another,
passing through the given waypoints in the given order.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="calculateScooterRoute">
/sdk-for-flutter-navigate-routing-routinginterface-calculatescooterroute(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-routing-waypoint-class&gt; waypoints, /sdk-for-flutter-navigate-routing-scooteroptions-class scooterOptions, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd class="inherited">
  Asynchronously calculates a scooter route from one point to another,
passing through the given waypoints in the given order.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="calculateTaxiRoute">
/sdk-for-flutter-navigate-routing-routinginterface-calculatetaxiroute(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-routing-waypoint-class&gt; waypoints, /sdk-for-flutter-navigate-routing-taxioptions-class taxiOptions, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd class="inherited">
  Asynchronously calculates a taxi route from one point to another,
passing through the given waypoints in the given order.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="calculateTruckRoute">
/sdk-for-flutter-navigate-routing-routinginterface-calculatetruckroute(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-routing-waypoint-class&gt; waypoints, /sdk-for-flutter-navigate-routing-truckoptions-class truckOptions, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd class="inherited">
  Asynchronously calculates a truck route from one point to another,
passing through the given waypoints in the given order.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="importFromHandleWithRoutingOptions">
/sdk-for-flutter-navigate-routing-offlineroutingengine-importfromhandlewithroutingoptions(<wbr/>/sdk-for-flutter-navigate-routing-routehandle-class routeHandle, /sdk-for-flutter-navigate-routing-routingoptions-class options, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously recreates a route from the /sdk-for-flutter-navigate-routing-routehandle-class provided, i.e.
  

</dd>
<dt class="callable" id="importRouteFromHandle">
/sdk-for-flutter-navigate-routing-offlineroutingengine-importroutefromhandle(<wbr/>/sdk-for-flutter-navigate-routing-routehandle-class routeHandle, /sdk-for-flutter-navigate-routing-refreshrouteoptions-class refreshRouteOptions, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously recreates a route from the /sdk-for-flutter-navigate-routing-routehandle-class provided, i.e.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-routing-routinginterface-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="refreshRouteWithRouteHandleAndRefreshRouteParameters">
/sdk-for-flutter-navigate-routing-offlineroutingengine-refreshroutewithroutehandleandrefreshrouteparameters(<wbr/>/sdk-for-flutter-navigate-routing-refreshrouteparameters-class refreshRouteParameters, /sdk-for-flutter-navigate-routing-routingoptions-class routingOptions, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously refreshes a previously calculated route from the provided /sdk-for-flutter-navigate-routing-routehandle-class, updating
the starting point and route metadata based on /sdk-for-flutter-navigate-routing-routingoptions-class.
  

</dd>
<dt class="callable inherited" id="returnToRouteWithTraveledDistance">
/sdk-for-flutter-navigate-routing-routinginterface-returntoroutewithtraveleddistance(<wbr/>/sdk-for-flutter-navigate-routing-route-class route, /sdk-for-flutter-navigate-routing-waypoint-class startingPoint, int lastTraveledSectionIndex, int traveledDistanceOnLastSectionInMeters, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd class="inherited">
  Asynchronously calculates a new route that leads back to the original route.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="setInternalOption">
/sdk-for-flutter-navigate-routing-offlineroutingengine-setinternaloption(<wbr/>String key, String value)
    → void

</dt>
<dd>
  This method sets internal options that controls offline route calculation behavior.
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-routing-routinginterface-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
/sdk-for-flutter-navigate-routing-routinginterface-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li class="self-crumb">OfflineRoutingEngine class</li>
</ol>
<h5>routing library</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>
</div></div>
</div>
`
}</HTMLBlock>
