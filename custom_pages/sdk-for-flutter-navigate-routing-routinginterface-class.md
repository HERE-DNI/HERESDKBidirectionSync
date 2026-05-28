---
title: "RoutingInterface class abstract"
slug: "sdk-for-flutter-navigate-routing-routinginterface-class"
---

<HTMLBlock>{
`
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
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
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
<li>/sdk-for-flutter-navigate-routing-offlineroutingengine-class</li>
<li>/sdk-for-flutter-navigate-routing-routingengine-class</li>
</ul></dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="RoutingInterface">
/sdk-for-flutter-navigate-routing-routinginterface-routinginterface(/sdk-for-flutter-navigate-core-threading-taskhandle-class calculateRouteWithRoutingOptionsLambda(List&lt;<wbr/>/sdk-for-flutter-navigate-routing-waypoint-class&gt;, /sdk-for-flutter-navigate-routing-routingoptions-class, /sdk-for-flutter-navigate-routing-calculateroutecallback ), /sdk-for-flutter-navigate-core-threading-taskhandle-class calculateCarRouteLambda(List&lt;<wbr/>/sdk-for-flutter-navigate-routing-waypoint-class&gt;, /sdk-for-flutter-navigate-routing-caroptions-class, /sdk-for-flutter-navigate-routing-calculateroutecallback ), /sdk-for-flutter-navigate-core-threading-taskhandle-class calculatePedestrianRouteLambda(List&lt;<wbr/>/sdk-for-flutter-navigate-routing-waypoint-class&gt;, /sdk-for-flutter-navigate-routing-pedestrianoptions-class, /sdk-for-flutter-navigate-routing-calculateroutecallback ), /sdk-for-flutter-navigate-core-threading-taskhandle-class calculateTruckRouteLambda(List&lt;<wbr/>/sdk-for-flutter-navigate-routing-waypoint-class&gt;, /sdk-for-flutter-navigate-routing-truckoptions-class, /sdk-for-flutter-navigate-routing-calculateroutecallback ), /sdk-for-flutter-navigate-core-threading-taskhandle-class calculateScooterRouteLambda(List&lt;<wbr/>/sdk-for-flutter-navigate-routing-waypoint-class&gt;, /sdk-for-flutter-navigate-routing-scooteroptions-class, /sdk-for-flutter-navigate-routing-calculateroutecallback ), /sdk-for-flutter-navigate-core-threading-taskhandle-class calculateBicycleRouteLambda(List&lt;<wbr/>/sdk-for-flutter-navigate-routing-waypoint-class&gt;, /sdk-for-flutter-navigate-routing-bicycleoptions-class, /sdk-for-flutter-navigate-routing-calculateroutecallback ), /sdk-for-flutter-navigate-core-threading-taskhandle-class calculateTaxiRouteLambda(List&lt;<wbr/>/sdk-for-flutter-navigate-routing-waypoint-class&gt;, /sdk-for-flutter-navigate-routing-taxioptions-class, /sdk-for-flutter-navigate-routing-calculateroutecallback ), /sdk-for-flutter-navigate-core-threading-taskhandle-class calculateEVCarRouteLambda(List&lt;<wbr/>/sdk-for-flutter-navigate-routing-waypoint-class&gt;, /sdk-for-flutter-navigate-routing-evcaroptions-class, /sdk-for-flutter-navigate-routing-calculateroutecallback ), /sdk-for-flutter-navigate-core-threading-taskhandle-class calculateEVTruckRouteLambda(List&lt;<wbr/>/sdk-for-flutter-navigate-routing-waypoint-class&gt;, /sdk-for-flutter-navigate-routing-evtruckoptions-class, /sdk-for-flutter-navigate-routing-calculateroutecallback ), /sdk-for-flutter-navigate-core-threading-taskhandle-class calculateBusRouteLambda(List&lt;<wbr/>/sdk-for-flutter-navigate-routing-waypoint-class&gt;, /sdk-for-flutter-navigate-routing-busoptions-class, /sdk-for-flutter-navigate-routing-calculateroutecallback ), /sdk-for-flutter-navigate-core-threading-taskhandle-class calculatePrivateBusRouteLambda(List&lt;<wbr/>/sdk-for-flutter-navigate-routing-waypoint-class&gt;, /sdk-for-flutter-navigate-routing-privatebusoptions-class, /sdk-for-flutter-navigate-routing-calculateroutecallback ), /sdk-for-flutter-navigate-core-threading-taskhandle-class returnToRouteWithTraveledDistanceLambda(/sdk-for-flutter-navigate-routing-route-class, /sdk-for-flutter-navigate-routing-waypoint-class, int, int, /sdk-for-flutter-navigate-routing-calculateroutecallback ))
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
<dt class="callable" id="calculateBicycleRoute">
/sdk-for-flutter-navigate-routing-routinginterface-calculatebicycleroute(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-routing-waypoint-class&gt; waypoints, /sdk-for-flutter-navigate-routing-bicycleoptions-class bicycleOptions, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously calculates a bicycle route from one point to another,
passing through the given waypoints in the given order.
  

</dd>
<dt class="callable" id="calculateBusRoute">
/sdk-for-flutter-navigate-routing-routinginterface-calculatebusroute(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-routing-waypoint-class&gt; waypoints, /sdk-for-flutter-navigate-routing-busoptions-class busOptions, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously calculates a bus route from one point to another,
passing through the given waypoints in the given order.
  

</dd>
<dt class="callable" id="calculateCarRoute">
/sdk-for-flutter-navigate-routing-routinginterface-calculatecarroute(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-routing-waypoint-class&gt; waypoints, /sdk-for-flutter-navigate-routing-caroptions-class carOptions, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously calculates a car route from one point to another,
passing through the given waypoints in the given order.
  

</dd>
<dt class="callable" id="calculateEVCarRoute">
/sdk-for-flutter-navigate-routing-routinginterface-calculateevcarroute(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-routing-waypoint-class&gt; waypoints, /sdk-for-flutter-navigate-routing-evcaroptions-class evCarOptions, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously calculates an electric car route from one point to another,
passing through the given waypoints in the given order.
  

</dd>
<dt class="callable" id="calculateEVTruckRoute">
/sdk-for-flutter-navigate-routing-routinginterface-calculateevtruckroute(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-routing-waypoint-class&gt; waypoints, /sdk-for-flutter-navigate-routing-evtruckoptions-class evTruckOptions, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously calculates an electic truck route from one point to another,
passing through the given waypoints in the given order.
  

</dd>
<dt class="callable" id="calculatePedestrianRoute">
/sdk-for-flutter-navigate-routing-routinginterface-calculatepedestrianroute(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-routing-waypoint-class&gt; waypoints, /sdk-for-flutter-navigate-routing-pedestrianoptions-class pedestrianOptions, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously calculates a pedestrian route from one point to another,
passing through the given waypoints in the given order.
  

</dd>
<dt class="callable" id="calculatePrivateBusRoute">
/sdk-for-flutter-navigate-routing-routinginterface-calculateprivatebusroute(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-routing-waypoint-class&gt; waypoints, /sdk-for-flutter-navigate-routing-privatebusoptions-class privateBusOptions, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously calculates a private bus route from one point to another,
passing through the given waypoints in the given order.
  

</dd>
<dt class="callable" id="calculateRouteWithRoutingOptions">
/sdk-for-flutter-navigate-routing-routinginterface-calculateroutewithroutingoptions(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-routing-waypoint-class&gt; waypoints, /sdk-for-flutter-navigate-routing-routingoptions-class options, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously calculates a route from one point to another,
passing through the given waypoints in the given order.
  

</dd>
<dt class="callable" id="calculateScooterRoute">
/sdk-for-flutter-navigate-routing-routinginterface-calculatescooterroute(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-routing-waypoint-class&gt; waypoints, /sdk-for-flutter-navigate-routing-scooteroptions-class scooterOptions, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously calculates a scooter route from one point to another,
passing through the given waypoints in the given order.
  

</dd>
<dt class="callable" id="calculateTaxiRoute">
/sdk-for-flutter-navigate-routing-routinginterface-calculatetaxiroute(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-routing-waypoint-class&gt; waypoints, /sdk-for-flutter-navigate-routing-taxioptions-class taxiOptions, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously calculates a taxi route from one point to another,
passing through the given waypoints in the given order.
  

</dd>
<dt class="callable" id="calculateTruckRoute">
/sdk-for-flutter-navigate-routing-routinginterface-calculatetruckroute(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-routing-waypoint-class&gt; waypoints, /sdk-for-flutter-navigate-routing-truckoptions-class truckOptions, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously calculates a truck route from one point to another,
passing through the given waypoints in the given order.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-routing-routinginterface-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="returnToRouteWithTraveledDistance">
/sdk-for-flutter-navigate-routing-routinginterface-returntoroutewithtraveleddistance(<wbr/>/sdk-for-flutter-navigate-routing-route-class route, /sdk-for-flutter-navigate-routing-waypoint-class startingPoint, int lastTraveledSectionIndex, int traveledDistanceOnLastSectionInMeters, /sdk-for-flutter-navigate-routing-calculateroutecallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Asynchronously calculates a new route that leads back to the original route.
  

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
`
}</HTMLBlock>
