---
title: "RoutePlace class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-routeplace-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/RoutePlace-class-sidebar.html">

<div>

# <span class="kind-class">RoutePlace</span> class

</div>

<div class="section desc markdown">

The location information.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-routing-routeplace-routeplace">RoutePlace</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-type" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-routeplacetype">RoutePlaceType</a></span> <span class="parameter-name">type</span>, </span><span id="sdk-for-flutter-navigate-param-mapMatchedCoordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">mapMatchedCoordinates</span></span>)</span>  
Creates a new instance.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-routing-routeplace-chargeinkilowatthours">chargeInKilowattHours</a></span> <span class="signature">↔ double?</span>  
Estimated battery charge in kWh for electric vehicles when leaving this place. Available only if the route was calculated with <a href="sdk-for-flutter-navigate-routing-electricvehicleoptions-ensurereachability">ElectricVehicleOptions.ensureReachability</a> = `true`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-routeplace-chargingstation">chargingStation</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-routing-chargingstation-class">ChargingStation</a>?</span>  
Charging station data for electric vehicles.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-routeplace-displaycoordinates">displayCoordinates</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a>?</span>  
Location of the Points of Interest (PoI) to be displayed in the visualization. In the map data, PoI have a set of display coordinates as well as a set of access/routing coordinates. While the access/routing coordinates specify the nearest accessible road network location that can be apart from actual location of the PoI, the display coordinates specify the location of the PoI to be displayed accurately in the visualization.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-routeplace-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-routeplace-id">id</a></span> <span class="signature">↔ String?</span>  
Identifier of a public transit place if available.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-routeplace-mapmatchedcoordinates">mapMatchedCoordinates</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span>  
Map-matched geographic coordinates.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-routeplace-name">name</a></span> <span class="signature">↔ String?</span>  
Name of a public transit place if available.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-routeplace-originalcoordinates">originalCoordinates</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a>?</span>  
User-defined geographic coordinates. If not available, it means this place was added during route calculation.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-routeplace-platform">platform</a></span> <span class="signature">↔ String?</span>  
Platform name or number of a public transit place if available.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-routeplace-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-routeplace-sideofdestination">sideOfDestination</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-routing-sideofdestination">SideOfDestination</a>?</span>  
Side of destination: left, right or undefined. `null` for transit sections and for origin points. `UNDEFINED` if `originalCoordinates` are not identified or too close to the road.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-routeplace-type">type</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-routing-routeplacetype">RoutePlaceType</a></span>  
The type of the route place.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-routeplace-waypointindex">waypointIndex</a></span> <span class="signature">↔ int?</span>  
If available, this index corresponds to the waypoint in the original user-defined waypoint list. Otherwise, this waypoint was added during route calculation by the system.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-routing-routeplace-isoffroad">isOffRoad</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ bool</span> </span>  
Checks whether the <a href="sdk-for-flutter-navigate-routing-routeplace-class">RoutePlace</a> is off-road or not.

<span class="name"><a href="sdk-for-flutter-navigate-routing-routeplace-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-routeplace-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-routing-routeplace-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

