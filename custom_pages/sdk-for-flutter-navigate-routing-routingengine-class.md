---
title: "RoutingEngine class abstract"
slug: "sdk-for-flutter-navigate-routing-routingengine-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RoutingEngine-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="routing/RoutingEngine-class.html#constructors">Constructors</a></li>
<li><a href="routing/RoutingEngine/RoutingEngine.html">RoutingEngine</a></li>
<li><a href="routing/RoutingEngine/RoutingEngine.withConnectionSettings.html">withConnectionSettings</a></li>
<li><a href="routing/RoutingEngine/RoutingEngine.withSdkEngine.html">withSdkEngine</a></li>
<li><a href="routing/RoutingEngine/RoutingEngine.withSdkEngineAndConnectionSettings.html">withSdkEngineAndConnectionSettings</a></li>
<li class="section-title inherited">
<a href="routing/RoutingEngine-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="routing/RoutingInterface/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="routing/RoutingInterface/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="routing/RoutingEngine-class.html#instance-methods">Methods</a></li>
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
<li><a href="routing/RoutingEngine/calculateTrafficOnRoute.html">calculateTrafficOnRoute</a></li>
<li><a href="routing/RoutingEngine/calculateTrafficOnRouteWithCurrentCharge.html">calculateTrafficOnRouteWithCurrentCharge</a></li>
<li class="inherited"><a class="deprecated" href="routing/RoutingInterface/calculateTruckRoute.html">calculateTruckRoute</a></li>
<li><a class="deprecated" href="routing/RoutingEngine/importBicycleRoute.html">importBicycleRoute</a></li>
<li><a class="deprecated" href="routing/RoutingEngine/importBicycleRouteWithStops.html">importBicycleRouteWithStops</a></li>
<li><a class="deprecated" href="routing/RoutingEngine/importBusRoute.html">importBusRoute</a></li>
<li><a class="deprecated" href="routing/RoutingEngine/importBusRouteWithStops.html">importBusRouteWithStops</a></li>
<li><a class="deprecated" href="routing/RoutingEngine/importCarRoute.html">importCarRoute</a></li>
<li><a class="deprecated" href="routing/RoutingEngine/importCarRouteWithStops.html">importCarRouteWithStops</a></li>
<li><a class="deprecated" href="routing/RoutingEngine/importEVCarRoute.html">importEVCarRoute</a></li>
<li><a class="deprecated" href="routing/RoutingEngine/importEVCarRouteWithStops.html">importEVCarRouteWithStops</a></li>
<li><a class="deprecated" href="routing/RoutingEngine/importEVTruckRoute.html">importEVTruckRoute</a></li>
<li><a class="deprecated" href="routing/RoutingEngine/importEVTruckRouteWithStops.html">importEVTruckRouteWithStops</a></li>
<li><a class="deprecated" href="routing/RoutingEngine/importPedestrianRoute.html">importPedestrianRoute</a></li>
<li><a class="deprecated" href="routing/RoutingEngine/importPedestrianRouteWithStops.html">importPedestrianRouteWithStops</a></li>
<li><a class="deprecated" href="routing/RoutingEngine/importPrivateBusRoute.html">importPrivateBusRoute</a></li>
<li><a class="deprecated" href="routing/RoutingEngine/importPrivateBusRouteWithStops.html">importPrivateBusRouteWithStops</a></li>
<li><a class="deprecated" href="routing/RoutingEngine/importRouteFromHandle.html">importRouteFromHandle</a></li>
<li><a href="routing/RoutingEngine/importRouteFromHandleWithRoutingOptions.html">importRouteFromHandleWithRoutingOptions</a></li>
<li><a href="routing/RoutingEngine/importRouteWithRoutingOptions.html">importRouteWithRoutingOptions</a></li>
<li><a href="routing/RoutingEngine/importRouteWithStopsAndRoutingOptions.html">importRouteWithStopsAndRoutingOptions</a></li>
<li><a class="deprecated" href="routing/RoutingEngine/importScooterRoute.html">importScooterRoute</a></li>
<li><a class="deprecated" href="routing/RoutingEngine/importScooterRouteWithStops.html">importScooterRouteWithStops</a></li>
<li><a class="deprecated" href="routing/RoutingEngine/importTaxiRoute.html">importTaxiRoute</a></li>
<li><a class="deprecated" href="routing/RoutingEngine/importTaxiRouteWithStops.html">importTaxiRouteWithStops</a></li>
<li><a class="deprecated" href="routing/RoutingEngine/importTruckRoute.html">importTruckRoute</a></li>
<li><a class="deprecated" href="routing/RoutingEngine/importTruckRouteWithStops.html">importTruckRouteWithStops</a></li>
<li class="inherited"><a href="routing/RoutingInterface/noSuchMethod.html">noSuchMethod</a></li>
<li><a class="deprecated" href="routing/RoutingEngine/refreshRoute.html">refreshRoute</a></li>
<li><a href="routing/RoutingEngine/refreshRouteWithRouteHandleAndRefreshRouteParameters.html">refreshRouteWithRouteHandleAndRefreshRouteParameters</a></li>
<li><a class="deprecated" href="routing/RoutingEngine/refreshRouteWithRouteHandleAndRoutingOptions.html">refreshRouteWithRouteHandleAndRoutingOptions</a></li>
<li><a class="deprecated" href="routing/RoutingEngine/refreshRouteWithTraveledDistance.html">refreshRouteWithTraveledDistance</a></li>
<li><a class="deprecated" href="routing/RoutingEngine/refreshRouteWithTraveledDistanceAndRoutingOptions.html">refreshRouteWithTraveledDistanceAndRoutingOptions</a></li>
<li class="inherited"><a href="routing/RoutingInterface/returnToRouteWithTraveledDistance.html">returnToRouteWithTraveledDistance</a></li>
<li><a href="routing/RoutingEngine/setCustomOption.html">setCustomOption</a></li>
<li class="inherited"><a href="routing/RoutingInterface/toString.html">toString</a></li>
<li class="section-title inherited"><a href="routing/RoutingEngine-class.html#operators">Operators</a></li>
<li class="inherited"><a href="routing/RoutingInterface/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li class="self-crumb">RoutingEngine class</li>
</ol>
<div class="self-name">RoutingEngine</div>
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
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/RoutingEngine-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>RoutingEngine class abstract</h1></div>
<section class="desc markdown">
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
<dt class="callable" id="RoutingEngine">
/sdk-for-flutter-navigate-routing-routingengine-routingengine()
</dt>
<dd>
          Creates a new instance of this class.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="RoutingEngine.withConnectionSettings">
/sdk-for-flutter-navigate-routing-routingengine-routingengine-withconnectionsettings(/sdk-for-flutter-navigate-routing-routingconnectionsettings-class connectionSettings)
</dt>
<dd>
          Creates a new instance of RoutingEngine.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="RoutingEngine.withSdkEngine">
/sdk-for-flutter-navigate-routing-routingengine-routingengine-withsdkengine(/sdk-for-flutter-navigate-core-engine-sdknativeengine-class sdkEngine)
</dt>
<dd>
          Creates a new instance of RoutingEngine.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="RoutingEngine.withSdkEngineAndConnectionSettings">
/sdk-for-flutter-navigate-routing-routingengine-routingengine-withsdkengineandconnectionsettings(/sdk-for-flutter-navigate-core-engine-sdknativeengine-class sdkEngine, /sdk-for-flutter-navigate-routing-routingconnectionsettings-class connectionSettings)
</dt>
<dd>
          Creates a new instance of RoutingEngine.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
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
<dt class="callable" id="calculateTrafficOnRoute">
/sdk-for-flutter-navigate-routing-routingengine-calculatetrafficonroute(<wbr/>/sdk-for-flutter-navigate-routing-route-class route, int lastTraveledSectionIndex, int traveledDistanceOnLastSectionInMeters, /sdk-for-flutter-navigate-routing-calculatetrafficonroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously calculates the traffic along a route starting from the index of the last
traveled route section and an offset (in meters) from the last visited position on the
section.
  

</dd>
<dt class="callable" id="calculateTrafficOnRouteWithCurrentCharge">
/sdk-for-flutter-navigate-routing-routingengine-calculatetrafficonroutewithcurrentcharge(<wbr/>/sdk-for-flutter-navigate-routing-route-class route, int lastTraveledSectionIndex, int traveledDistanceOnLastSectionInMeters, double currentChargeInKilowattHours, /sdk-for-flutter-navigate-routing-calculatetrafficonroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously calculates the traffic along an EV car route starting from the index of the
last traveled route section and an offset in meters from the last visited position on the
section.
  

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
<dt class="callable" id="importBicycleRoute">
/sdk-for-flutter-navigate-routing-routingengine-importbicycleroute(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-core-location-class&gt; locations, /sdk-for-flutter-navigate-routing-bicycleoptions-class bicycleOptions, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously creates a bicycle route from a sequence of geographic coordinates very close to each other.
  

</dd>
<dt class="callable" id="importBicycleRouteWithStops">
/sdk-for-flutter-navigate-routing-routingengine-importbicycleroutewithstops(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-core-location-class&gt; locations, List&lt;<wbr/>/sdk-for-flutter-navigate-routing-routestop-class&gt; routeStops, /sdk-for-flutter-navigate-routing-bicycleoptions-class bicycleOptions, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously creates a bicycle route from a sequence of geographic coordinates very close to each other.
  

</dd>
<dt class="callable" id="importBusRoute">
/sdk-for-flutter-navigate-routing-routingengine-importbusroute(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-core-location-class&gt; locations, /sdk-for-flutter-navigate-routing-busoptions-class busOptions, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously creates a bus route from a sequence of geographic coordinates very close to each other.
  

</dd>
<dt class="callable" id="importBusRouteWithStops">
/sdk-for-flutter-navigate-routing-routingengine-importbusroutewithstops(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-core-location-class&gt; locations, List&lt;<wbr/>/sdk-for-flutter-navigate-routing-routestop-class&gt; routeStops, /sdk-for-flutter-navigate-routing-busoptions-class busOptions, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously creates a bus route from a sequence of geographic coordinates very close to each other.
  

</dd>
<dt class="callable" id="importCarRoute">
/sdk-for-flutter-navigate-routing-routingengine-importcarroute(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-core-location-class&gt; locations, /sdk-for-flutter-navigate-routing-caroptions-class carOptions, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously creates a car route from a sequence of geographic coordinates very close to each other.
  

</dd>
<dt class="callable" id="importCarRouteWithStops">
/sdk-for-flutter-navigate-routing-routingengine-importcarroutewithstops(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-core-location-class&gt; locations, List&lt;<wbr/>/sdk-for-flutter-navigate-routing-routestop-class&gt; routeStops, /sdk-for-flutter-navigate-routing-caroptions-class carOptions, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously creates a car route from a sequence of geographic coordinates very close to each other.
  

</dd>
<dt class="callable" id="importEVCarRoute">
/sdk-for-flutter-navigate-routing-routingengine-importevcarroute(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-core-location-class&gt; locations, /sdk-for-flutter-navigate-routing-evcaroptions-class evCarOptions, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously creates an electric car route from a sequence of geographic coordinates very close to each other.
  

</dd>
<dt class="callable" id="importEVCarRouteWithStops">
/sdk-for-flutter-navigate-routing-routingengine-importevcarroutewithstops(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-core-location-class&gt; locations, List&lt;<wbr/>/sdk-for-flutter-navigate-routing-routestop-class&gt; routeStops, /sdk-for-flutter-navigate-routing-evcaroptions-class evCarOptions, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously creates an electric car route from a sequence of geographic coordinates very close to each other.
  

</dd>
<dt class="callable" id="importEVTruckRoute">
/sdk-for-flutter-navigate-routing-routingengine-importevtruckroute(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-core-location-class&gt; locations, /sdk-for-flutter-navigate-routing-evtruckoptions-class evTruckOptions, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously creates an electric truck route from a sequence of geographic coordinates very close to each other.
  

</dd>
<dt class="callable" id="importEVTruckRouteWithStops">
/sdk-for-flutter-navigate-routing-routingengine-importevtruckroutewithstops(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-core-location-class&gt; locations, List&lt;<wbr/>/sdk-for-flutter-navigate-routing-routestop-class&gt; routeStops, /sdk-for-flutter-navigate-routing-evtruckoptions-class evTruckOptions, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously creates an electric truck route from a sequence of geographic coordinates very close to each other.
  

</dd>
<dt class="callable" id="importPedestrianRoute">
/sdk-for-flutter-navigate-routing-routingengine-importpedestrianroute(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-core-location-class&gt; locations, /sdk-for-flutter-navigate-routing-pedestrianoptions-class pedestrianOptions, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously creates a pedestrian route from a sequence of geographic coordinates very close to each other.
  

</dd>
<dt class="callable" id="importPedestrianRouteWithStops">
/sdk-for-flutter-navigate-routing-routingengine-importpedestrianroutewithstops(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-core-location-class&gt; locations, List&lt;<wbr/>/sdk-for-flutter-navigate-routing-routestop-class&gt; routeStops, /sdk-for-flutter-navigate-routing-pedestrianoptions-class pedestrianOptions, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously creates a pedestrian route from a sequence of geographic coordinates very close to each other.
  

</dd>
<dt class="callable" id="importPrivateBusRoute">
/sdk-for-flutter-navigate-routing-routingengine-importprivatebusroute(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-core-location-class&gt; locations, /sdk-for-flutter-navigate-routing-privatebusoptions-class privateBusOptions, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously creates a private bus route from a sequence of geographic coordinates very close to each other.
  

</dd>
<dt class="callable" id="importPrivateBusRouteWithStops">
/sdk-for-flutter-navigate-routing-routingengine-importprivatebusroutewithstops(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-core-location-class&gt; locations, List&lt;<wbr/>/sdk-for-flutter-navigate-routing-routestop-class&gt; routeStops, /sdk-for-flutter-navigate-routing-privatebusoptions-class privateBusOptions, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously creates a private bus route from a sequence of geographic coordinates very close to each other.
  

</dd>
<dt class="callable" id="importRouteFromHandle">
/sdk-for-flutter-navigate-routing-routingengine-importroutefromhandle(<wbr/>/sdk-for-flutter-navigate-routing-routehandle-class routeHandle, /sdk-for-flutter-navigate-routing-refreshrouteoptions-class refreshRouteOptions, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously recreates a route from the /sdk-for-flutter-navigate-routing-routehandle-class provided, i.e.
  

</dd>
<dt class="callable" id="importRouteFromHandleWithRoutingOptions">
/sdk-for-flutter-navigate-routing-routingengine-importroutefromhandlewithroutingoptions(<wbr/>/sdk-for-flutter-navigate-routing-routehandle-class routeHandle, /sdk-for-flutter-navigate-routing-routingoptions-class options, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously recreates a route from the /sdk-for-flutter-navigate-routing-routehandle-class provided, i.e.
  

</dd>
<dt class="callable" id="importRouteWithRoutingOptions">
/sdk-for-flutter-navigate-routing-routingengine-importroutewithroutingoptions(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-core-location-class&gt; locations, /sdk-for-flutter-navigate-routing-routingoptions-class options, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously creates a route from a sequence of geographic coordinates very close to each other.
  

</dd>
<dt class="callable" id="importRouteWithStopsAndRoutingOptions">
/sdk-for-flutter-navigate-routing-routingengine-importroutewithstopsandroutingoptions(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-core-location-class&gt; locations, List&lt;<wbr/>/sdk-for-flutter-navigate-routing-routestop-class&gt; routeStops, /sdk-for-flutter-navigate-routing-routingoptions-class options, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously creates a route from a sequence of geographic coordinates very close to each other.
  

</dd>
<dt class="callable" id="importScooterRoute">
/sdk-for-flutter-navigate-routing-routingengine-importscooterroute(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-core-location-class&gt; locations, /sdk-for-flutter-navigate-routing-scooteroptions-class scooterOptions, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously creates a scooter route from a sequence of geographic coordinates very close to each other.
  

</dd>
<dt class="callable" id="importScooterRouteWithStops">
/sdk-for-flutter-navigate-routing-routingengine-importscooterroutewithstops(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-core-location-class&gt; locations, List&lt;<wbr/>/sdk-for-flutter-navigate-routing-routestop-class&gt; routeStops, /sdk-for-flutter-navigate-routing-scooteroptions-class scooterOptions, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously creates a scooter route from a sequence of geographic coordinates very close to each other.
  

</dd>
<dt class="callable" id="importTaxiRoute">
/sdk-for-flutter-navigate-routing-routingengine-importtaxiroute(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-core-location-class&gt; locations, /sdk-for-flutter-navigate-routing-taxioptions-class taxiOptions, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously creates a taxi route from a sequence of geographic coordinates very close to each other.
  

</dd>
<dt class="callable" id="importTaxiRouteWithStops">
/sdk-for-flutter-navigate-routing-routingengine-importtaxiroutewithstops(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-core-location-class&gt; locations, List&lt;<wbr/>/sdk-for-flutter-navigate-routing-routestop-class&gt; routeStops, /sdk-for-flutter-navigate-routing-taxioptions-class taxiOptions, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously creates a taxi route from a sequence of geographic coordinates very close to each other.
  

</dd>
<dt class="callable" id="importTruckRoute">
/sdk-for-flutter-navigate-routing-routingengine-importtruckroute(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-core-location-class&gt; locations, /sdk-for-flutter-navigate-routing-truckoptions-class truckOptions, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously creates a truck route from a sequence of geographic coordinates very close to each other.
  

</dd>
<dt class="callable" id="importTruckRouteWithStops">
/sdk-for-flutter-navigate-routing-routingengine-importtruckroutewithstops(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-core-location-class&gt; locations, List&lt;<wbr/>/sdk-for-flutter-navigate-routing-routestop-class&gt; routeStops, /sdk-for-flutter-navigate-routing-truckoptions-class truckOptions, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously creates a truck route from a sequence of geographic coordinates very close to each other.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-routing-routinginterface-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="refreshRoute">
/sdk-for-flutter-navigate-routing-routingengine-refreshroute(<wbr/>/sdk-for-flutter-navigate-routing-routehandle-class routeHandle, /sdk-for-flutter-navigate-routing-waypoint-class startingPoint, /sdk-for-flutter-navigate-routing-refreshrouteoptions-class refreshRouteOptions, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously refreshes a previously calculated route from the provided /sdk-for-flutter-navigate-routing-routehandle-class, updating
the starting point and route metadata based on /sdk-for-flutter-navigate-routing-refreshrouteoptions-class.
  

</dd>
<dt class="callable" id="refreshRouteWithRouteHandleAndRefreshRouteParameters">
/sdk-for-flutter-navigate-routing-routingengine-refreshroutewithroutehandleandrefreshrouteparameters(<wbr/>/sdk-for-flutter-navigate-routing-refreshrouteparameters-class refreshRouteParameters, /sdk-for-flutter-navigate-routing-routingoptions-class routingOptions, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously refreshes a previously calculated route from the provided /sdk-for-flutter-navigate-routing-routehandle-class, updating
the starting point and route metadata based on /sdk-for-flutter-navigate-routing-routingoptions-class.
  

</dd>
<dt class="callable" id="refreshRouteWithRouteHandleAndRoutingOptions">
/sdk-for-flutter-navigate-routing-routingengine-refreshroutewithroutehandleandroutingoptions(<wbr/>/sdk-for-flutter-navigate-routing-routehandle-class routeHandle, /sdk-for-flutter-navigate-routing-waypoint-class startingPoint, /sdk-for-flutter-navigate-routing-routingoptions-class options, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously refreshes a previously calculated route from the provided /sdk-for-flutter-navigate-routing-routehandle-class, updating
the starting point and route metadata based on /sdk-for-flutter-navigate-routing-routingoptions-class.
  

</dd>
<dt class="callable" id="refreshRouteWithTraveledDistance">
/sdk-for-flutter-navigate-routing-routingengine-refreshroutewithtraveleddistance(<wbr/>/sdk-for-flutter-navigate-routing-routehandle-class routeHandle, /sdk-for-flutter-navigate-routing-waypoint-class? startingPoint, int? lastTraveledSectionIndex, int? traveledDistanceOnLastSectionInMeters, /sdk-for-flutter-navigate-routing-refreshrouteoptions-class refreshRouteOptions, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously refreshes a previously calculated route from the provided /sdk-for-flutter-navigate-routing-routehandle-class, updating
the starting point and route metadata based on /sdk-for-flutter-navigate-routing-refreshrouteoptions-class.
  

</dd>
<dt class="callable" id="refreshRouteWithTraveledDistanceAndRoutingOptions">
/sdk-for-flutter-navigate-routing-routingengine-refreshroutewithtraveleddistanceandroutingoptions(<wbr/>/sdk-for-flutter-navigate-routing-routehandle-class routeHandle, /sdk-for-flutter-navigate-routing-waypoint-class? startingPoint, int? lastTraveledSectionIndex, int? traveledDistanceOnLastSectionInMeters, /sdk-for-flutter-navigate-routing-routingoptions-class options, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
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
<dt class="callable" id="setCustomOption">
/sdk-for-flutter-navigate-routing-routingengine-setcustomoption(<wbr/>String name, String? value)
    → /sdk-for-flutter-navigate-routing-routingerror?

</dt>
<dd>
  Sets a custom option for routing backend queries.
  

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
<li class="self-crumb">RoutingEngine class</li>
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
