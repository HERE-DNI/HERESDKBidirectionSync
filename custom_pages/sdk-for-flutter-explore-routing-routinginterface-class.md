---
title: "Constructors"
slug: "sdk-for-flutter-explore-routing-routinginterface-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- RoutingInterface-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="routing/RoutingInterface-class.html#constructors">Constructors</a></li>
<li><a href="routing/RoutingInterface/RoutingInterface.html">RoutingInterface</a></li>
<li class="section-title inherited">
<a href="routing/RoutingInterface-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="routing/RoutingInterface/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="routing/RoutingInterface/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="routing/RoutingInterface-class.html#instance-methods">Methods</a></li>
<li><a class="deprecated" href="routing/RoutingInterface/calculateBicycleRoute.html">calculateBicycleRoute</a></li>
<li><a class="deprecated" href="routing/RoutingInterface/calculateBusRoute.html">calculateBusRoute</a></li>
<li><a class="deprecated" href="routing/RoutingInterface/calculateCarRoute.html">calculateCarRoute</a></li>
<li><a class="deprecated" href="routing/RoutingInterface/calculateEVCarRoute.html">calculateEVCarRoute</a></li>
<li><a class="deprecated" href="routing/RoutingInterface/calculateEVTruckRoute.html">calculateEVTruckRoute</a></li>
<li><a class="deprecated" href="routing/RoutingInterface/calculatePedestrianRoute.html">calculatePedestrianRoute</a></li>
<li><a class="deprecated" href="routing/RoutingInterface/calculatePrivateBusRoute.html">calculatePrivateBusRoute</a></li>
<li><a href="routing/RoutingInterface/calculateRouteWithRoutingOptions.html">calculateRouteWithRoutingOptions</a></li>
<li><a class="deprecated" href="routing/RoutingInterface/calculateScooterRoute.html">calculateScooterRoute</a></li>
<li><a class="deprecated" href="routing/RoutingInterface/calculateTaxiRoute.html">calculateTaxiRoute</a></li>
<li><a class="deprecated" href="routing/RoutingInterface/calculateTruckRoute.html">calculateTruckRoute</a></li>
<li class="inherited"><a href="routing/RoutingInterface/noSuchMethod.html">noSuchMethod</a></li>
<li><a href="routing/RoutingInterface/returnToRouteWithTraveledDistance.html">returnToRouteWithTraveledDistance</a></li>
<li class="inherited"><a href="routing/RoutingInterface/toString.html">toString</a></li>
<li class="section-title inherited"><a href="routing/RoutingInterface-class.html#operators">Operators</a></li>
<li class="inherited"><a href="routing/RoutingInterface/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li class="self-crumb">RoutingInterface class</li>
</ol>
<div class="self-name">RoutingInterface</div>
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
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/RoutingInterface-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>RoutingInterface class abstract</h1></div>
<section class="desc markdown">
<p>Provides the abstract class for the online and offline
routing engines.</p>
</section>
<section>
<dl class="dl-horizontal">
<dt>Implementers</dt>
<dd><ul class="comma-separated clazz-relationships">
<li><a href="../routing/RoutingEngine-class.html">/sdk-for-flutter-explore-routing-routingengine-class</a></li>
</ul></dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="RoutingInterface">
<a href="../routing/RoutingInterface/RoutingInterface.html">/sdk-for-flutter-explore-routing-routinginterface-routinginterface</a>(<a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a> calculateRouteWithRoutingOptionsLambda(List&lt;<wbr/><a href="../routing/Waypoint-class.html">/sdk-for-flutter-explore-routing-waypoint-class</a>&gt;, <a href="../routing/RoutingOptions-class.html">/sdk-for-flutter-explore-routing-routingoptions-class</a>, <a href="../routing/CalculateRouteCallback.html">/sdk-for-flutter-explore-routing-calculateroutecallback</a> ), <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a> calculateCarRouteLambda(List&lt;<wbr/><a href="../routing/Waypoint-class.html">/sdk-for-flutter-explore-routing-waypoint-class</a>&gt;, <a class="deprecated" href="../routing/CarOptions-class.html">/sdk-for-flutter-explore-routing-caroptions-class</a>, <a href="../routing/CalculateRouteCallback.html">/sdk-for-flutter-explore-routing-calculateroutecallback</a> ), <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a> calculatePedestrianRouteLambda(List&lt;<wbr/><a href="../routing/Waypoint-class.html">/sdk-for-flutter-explore-routing-waypoint-class</a>&gt;, <a class="deprecated" href="../routing/PedestrianOptions-class.html">/sdk-for-flutter-explore-routing-pedestrianoptions-class</a>, <a href="../routing/CalculateRouteCallback.html">/sdk-for-flutter-explore-routing-calculateroutecallback</a> ), <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a> calculateTruckRouteLambda(List&lt;<wbr/><a href="../routing/Waypoint-class.html">/sdk-for-flutter-explore-routing-waypoint-class</a>&gt;, <a class="deprecated" href="../routing/TruckOptions-class.html">/sdk-for-flutter-explore-routing-truckoptions-class</a>, <a href="../routing/CalculateRouteCallback.html">/sdk-for-flutter-explore-routing-calculateroutecallback</a> ), <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a> calculateScooterRouteLambda(List&lt;<wbr/><a href="../routing/Waypoint-class.html">/sdk-for-flutter-explore-routing-waypoint-class</a>&gt;, <a class="deprecated" href="../routing/ScooterOptions-class.html">/sdk-for-flutter-explore-routing-scooteroptions-class</a>, <a href="../routing/CalculateRouteCallback.html">/sdk-for-flutter-explore-routing-calculateroutecallback</a> ), <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a> calculateBicycleRouteLambda(List&lt;<wbr/><a href="../routing/Waypoint-class.html">/sdk-for-flutter-explore-routing-waypoint-class</a>&gt;, <a class="deprecated" href="../routing/BicycleOptions-class.html">/sdk-for-flutter-explore-routing-bicycleoptions-class</a>, <a href="../routing/CalculateRouteCallback.html">/sdk-for-flutter-explore-routing-calculateroutecallback</a> ), <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a> calculateTaxiRouteLambda(List&lt;<wbr/><a href="../routing/Waypoint-class.html">/sdk-for-flutter-explore-routing-waypoint-class</a>&gt;, <a class="deprecated" href="../routing/TaxiOptions-class.html">/sdk-for-flutter-explore-routing-taxioptions-class</a>, <a href="../routing/CalculateRouteCallback.html">/sdk-for-flutter-explore-routing-calculateroutecallback</a> ), <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a> calculateEVCarRouteLambda(List&lt;<wbr/><a href="../routing/Waypoint-class.html">/sdk-for-flutter-explore-routing-waypoint-class</a>&gt;, <a class="deprecated" href="../routing/EVCarOptions-class.html">/sdk-for-flutter-explore-routing-evcaroptions-class</a>, <a href="../routing/CalculateRouteCallback.html">/sdk-for-flutter-explore-routing-calculateroutecallback</a> ), <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a> calculateEVTruckRouteLambda(List&lt;<wbr/><a href="../routing/Waypoint-class.html">/sdk-for-flutter-explore-routing-waypoint-class</a>&gt;, <a class="deprecated" href="../routing/EVTruckOptions-class.html">/sdk-for-flutter-explore-routing-evtruckoptions-class</a>, <a href="../routing/CalculateRouteCallback.html">/sdk-for-flutter-explore-routing-calculateroutecallback</a> ), <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a> calculateBusRouteLambda(List&lt;<wbr/><a href="../routing/Waypoint-class.html">/sdk-for-flutter-explore-routing-waypoint-class</a>&gt;, <a class="deprecated" href="../routing/BusOptions-class.html">/sdk-for-flutter-explore-routing-busoptions-class</a>, <a href="../routing/CalculateRouteCallback.html">/sdk-for-flutter-explore-routing-calculateroutecallback</a> ), <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a> calculatePrivateBusRouteLambda(List&lt;<wbr/><a href="../routing/Waypoint-class.html">/sdk-for-flutter-explore-routing-waypoint-class</a>&gt;, <a class="deprecated" href="../routing/PrivateBusOptions-class.html">/sdk-for-flutter-explore-routing-privatebusoptions-class</a>, <a href="../routing/CalculateRouteCallback.html">/sdk-for-flutter-explore-routing-calculateroutecallback</a> ), <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a> returnToRouteWithTraveledDistanceLambda(<a href="../routing/Route-class.html">/sdk-for-flutter-explore-routing-route-class</a>, <a href="../routing/Waypoint-class.html">/sdk-for-flutter-explore-routing-waypoint-class</a>, int, int, <a href="../routing/CalculateRouteCallback.html">/sdk-for-flutter-explore-routing-calculateroutecallback</a> ))
</dt>
<dd>
          Provides the abstract class for the online and offline
routing engines.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
<a href="../routing/RoutingInterface/hashCode.html">/sdk-for-flutter-explore-routing-routinginterface-hashcode</a>
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../routing/RoutingInterface/runtimeType.html">/sdk-for-flutter-explore-routing-routinginterface-runtimetype</a>
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
<dt class="callable" id="calculateBicycleRoute">
<a class="deprecated" href="../routing/RoutingInterface/calculateBicycleRoute.html">/sdk-for-flutter-explore-routing-routinginterface-calculatebicycleroute</a>(<wbr/>List&lt;<wbr/><a href="../routing/Waypoint-class.html">/sdk-for-flutter-explore-routing-waypoint-class</a>&gt; waypoints, <a class="deprecated" href="../routing/BicycleOptions-class.html">/sdk-for-flutter-explore-routing-bicycleoptions-class</a> bicycleOptions, <a href="../routing/CalculateRouteCallback.html">/sdk-for-flutter-explore-routing-calculateroutecallback</a> callback)
    → <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
</dt>
<dd>
  Asynchronously calculates a bicycle route from one point to another,
passing through the given waypoints in the given order.
  

</dd>
<dt class="callable" id="calculateBusRoute">
<a class="deprecated" href="../routing/RoutingInterface/calculateBusRoute.html">/sdk-for-flutter-explore-routing-routinginterface-calculatebusroute</a>(<wbr/>List&lt;<wbr/><a href="../routing/Waypoint-class.html">/sdk-for-flutter-explore-routing-waypoint-class</a>&gt; waypoints, <a class="deprecated" href="../routing/BusOptions-class.html">/sdk-for-flutter-explore-routing-busoptions-class</a> busOptions, <a href="../routing/CalculateRouteCallback.html">/sdk-for-flutter-explore-routing-calculateroutecallback</a> callback)
    → <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
</dt>
<dd>
  Asynchronously calculates a bus route from one point to another,
passing through the given waypoints in the given order.
  

</dd>
<dt class="callable" id="calculateCarRoute">
<a class="deprecated" href="../routing/RoutingInterface/calculateCarRoute.html">/sdk-for-flutter-explore-routing-routinginterface-calculatecarroute</a>(<wbr/>List&lt;<wbr/><a href="../routing/Waypoint-class.html">/sdk-for-flutter-explore-routing-waypoint-class</a>&gt; waypoints, <a class="deprecated" href="../routing/CarOptions-class.html">/sdk-for-flutter-explore-routing-caroptions-class</a> carOptions, <a href="../routing/CalculateRouteCallback.html">/sdk-for-flutter-explore-routing-calculateroutecallback</a> callback)
    → <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
</dt>
<dd>
  Asynchronously calculates a car route from one point to another,
passing through the given waypoints in the given order.
  

</dd>
<dt class="callable" id="calculateEVCarRoute">
<a class="deprecated" href="../routing/RoutingInterface/calculateEVCarRoute.html">/sdk-for-flutter-explore-routing-routinginterface-calculateevcarroute</a>(<wbr/>List&lt;<wbr/><a href="../routing/Waypoint-class.html">/sdk-for-flutter-explore-routing-waypoint-class</a>&gt; waypoints, <a class="deprecated" href="../routing/EVCarOptions-class.html">/sdk-for-flutter-explore-routing-evcaroptions-class</a> evCarOptions, <a href="../routing/CalculateRouteCallback.html">/sdk-for-flutter-explore-routing-calculateroutecallback</a> callback)
    → <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
</dt>
<dd>
  Asynchronously calculates an electric car route from one point to another,
passing through the given waypoints in the given order.
  

</dd>
<dt class="callable" id="calculateEVTruckRoute">
<a class="deprecated" href="../routing/RoutingInterface/calculateEVTruckRoute.html">/sdk-for-flutter-explore-routing-routinginterface-calculateevtruckroute</a>(<wbr/>List&lt;<wbr/><a href="../routing/Waypoint-class.html">/sdk-for-flutter-explore-routing-waypoint-class</a>&gt; waypoints, <a class="deprecated" href="../routing/EVTruckOptions-class.html">/sdk-for-flutter-explore-routing-evtruckoptions-class</a> evTruckOptions, <a href="../routing/CalculateRouteCallback.html">/sdk-for-flutter-explore-routing-calculateroutecallback</a> callback)
    → <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
</dt>
<dd>
  Asynchronously calculates an electic truck route from one point to another,
passing through the given waypoints in the given order.
  

</dd>
<dt class="callable" id="calculatePedestrianRoute">
<a class="deprecated" href="../routing/RoutingInterface/calculatePedestrianRoute.html">/sdk-for-flutter-explore-routing-routinginterface-calculatepedestrianroute</a>(<wbr/>List&lt;<wbr/><a href="../routing/Waypoint-class.html">/sdk-for-flutter-explore-routing-waypoint-class</a>&gt; waypoints, <a class="deprecated" href="../routing/PedestrianOptions-class.html">/sdk-for-flutter-explore-routing-pedestrianoptions-class</a> pedestrianOptions, <a href="../routing/CalculateRouteCallback.html">/sdk-for-flutter-explore-routing-calculateroutecallback</a> callback)
    → <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
</dt>
<dd>
  Asynchronously calculates a pedestrian route from one point to another,
passing through the given waypoints in the given order.
  

</dd>
<dt class="callable" id="calculatePrivateBusRoute">
<a class="deprecated" href="../routing/RoutingInterface/calculatePrivateBusRoute.html">/sdk-for-flutter-explore-routing-routinginterface-calculateprivatebusroute</a>(<wbr/>List&lt;<wbr/><a href="../routing/Waypoint-class.html">/sdk-for-flutter-explore-routing-waypoint-class</a>&gt; waypoints, <a class="deprecated" href="../routing/PrivateBusOptions-class.html">/sdk-for-flutter-explore-routing-privatebusoptions-class</a> privateBusOptions, <a href="../routing/CalculateRouteCallback.html">/sdk-for-flutter-explore-routing-calculateroutecallback</a> callback)
    → <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
</dt>
<dd>
  Asynchronously calculates a private bus route from one point to another,
passing through the given waypoints in the given order.
  

</dd>
<dt class="callable" id="calculateRouteWithRoutingOptions">
<a href="../routing/RoutingInterface/calculateRouteWithRoutingOptions.html">/sdk-for-flutter-explore-routing-routinginterface-calculateroutewithroutingoptions</a>(<wbr/>List&lt;<wbr/><a href="../routing/Waypoint-class.html">/sdk-for-flutter-explore-routing-waypoint-class</a>&gt; waypoints, <a href="../routing/RoutingOptions-class.html">/sdk-for-flutter-explore-routing-routingoptions-class</a> options, <a href="../routing/CalculateRouteCallback.html">/sdk-for-flutter-explore-routing-calculateroutecallback</a> callback)
    → <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
</dt>
<dd>
  Asynchronously calculates a route from one point to another,
passing through the given waypoints in the given order.
  

</dd>
<dt class="callable" id="calculateScooterRoute">
<a class="deprecated" href="../routing/RoutingInterface/calculateScooterRoute.html">/sdk-for-flutter-explore-routing-routinginterface-calculatescooterroute</a>(<wbr/>List&lt;<wbr/><a href="../routing/Waypoint-class.html">/sdk-for-flutter-explore-routing-waypoint-class</a>&gt; waypoints, <a class="deprecated" href="../routing/ScooterOptions-class.html">/sdk-for-flutter-explore-routing-scooteroptions-class</a> scooterOptions, <a href="../routing/CalculateRouteCallback.html">/sdk-for-flutter-explore-routing-calculateroutecallback</a> callback)
    → <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
</dt>
<dd>
  Asynchronously calculates a scooter route from one point to another,
passing through the given waypoints in the given order.
  

</dd>
<dt class="callable" id="calculateTaxiRoute">
<a class="deprecated" href="../routing/RoutingInterface/calculateTaxiRoute.html">/sdk-for-flutter-explore-routing-routinginterface-calculatetaxiroute</a>(<wbr/>List&lt;<wbr/><a href="../routing/Waypoint-class.html">/sdk-for-flutter-explore-routing-waypoint-class</a>&gt; waypoints, <a class="deprecated" href="../routing/TaxiOptions-class.html">/sdk-for-flutter-explore-routing-taxioptions-class</a> taxiOptions, <a href="../routing/CalculateRouteCallback.html">/sdk-for-flutter-explore-routing-calculateroutecallback</a> callback)
    → <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
</dt>
<dd>
  Asynchronously calculates a taxi route from one point to another,
passing through the given waypoints in the given order.
  

</dd>
<dt class="callable" id="calculateTruckRoute">
<a class="deprecated" href="../routing/RoutingInterface/calculateTruckRoute.html">/sdk-for-flutter-explore-routing-routinginterface-calculatetruckroute</a>(<wbr/>List&lt;<wbr/><a href="../routing/Waypoint-class.html">/sdk-for-flutter-explore-routing-waypoint-class</a>&gt; waypoints, <a class="deprecated" href="../routing/TruckOptions-class.html">/sdk-for-flutter-explore-routing-truckoptions-class</a> truckOptions, <a href="../routing/CalculateRouteCallback.html">/sdk-for-flutter-explore-routing-calculateroutecallback</a> callback)
    → <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
</dt>
<dd>
  Asynchronously calculates a truck route from one point to another,
passing through the given waypoints in the given order.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
<a href="../routing/RoutingInterface/noSuchMethod.html">/sdk-for-flutter-explore-routing-routinginterface-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="returnToRouteWithTraveledDistance">
<a href="../routing/RoutingInterface/returnToRouteWithTraveledDistance.html">/sdk-for-flutter-explore-routing-routinginterface-returntoroutewithtraveleddistance</a>(<wbr/><a href="../routing/Route-class.html">/sdk-for-flutter-explore-routing-route-class</a> route, <a href="../routing/Waypoint-class.html">/sdk-for-flutter-explore-routing-waypoint-class</a> startingPoint, int lastTraveledSectionIndex, int traveledDistanceOnLastSectionInMeters, <a href="../routing/CalculateRouteCallback.html">/sdk-for-flutter-explore-routing-calculateroutecallback</a> callback)
    → <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
</dt>
<dd>
  Asynchronously calculates a new route that leads back to the original route.
  

</dd>
<dt class="callable inherited" id="toString">
<a href="../routing/RoutingInterface/toString.html">/sdk-for-flutter-explore-routing-routinginterface-tostring</a>(<wbr/>)
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
<a href="../routing/RoutingInterface/operator_equals.html">/sdk-for-flutter-explore-routing-routinginterface-operator-equals</a>(<wbr/>Object other)
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
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li class="self-crumb">RoutingInterface class</li>
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
</HTMLBlock>
