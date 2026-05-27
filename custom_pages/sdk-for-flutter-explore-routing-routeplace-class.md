---
title: "Constructors"
slug: "sdk-for-flutter-explore-routing-routeplace-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- RoutePlace-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="routing/RoutePlace-class.html#constructors">Constructors</a></li>
<li><a href="routing/RoutePlace/RoutePlace.html">RoutePlace</a></li>
<li class="section-title">
<a href="routing/RoutePlace-class.html#instance-properties">Properties</a>
</li>
<li><a href="routing/RoutePlace/chargeInKilowattHours.html">chargeInKilowattHours</a></li>
<li><a href="routing/RoutePlace/chargingStation.html">chargingStation</a></li>
<li><a href="routing/RoutePlace/displayCoordinates.html">displayCoordinates</a></li>
<li><a href="routing/RoutePlace/hashCode.html">hashCode</a></li>
<li><a href="routing/RoutePlace/id.html">id</a></li>
<li><a href="routing/RoutePlace/mapMatchedCoordinates.html">mapMatchedCoordinates</a></li>
<li><a href="routing/RoutePlace/name.html">name</a></li>
<li><a href="routing/RoutePlace/originalCoordinates.html">originalCoordinates</a></li>
<li><a href="routing/RoutePlace/platform.html">platform</a></li>
<li class="inherited"><a href="routing/RoutePlace/runtimeType.html">runtimeType</a></li>
<li><a href="routing/RoutePlace/sideOfDestination.html">sideOfDestination</a></li>
<li><a href="routing/RoutePlace/type.html">type</a></li>
<li><a href="routing/RoutePlace/waypointIndex.html">waypointIndex</a></li>
<li class="section-title"><a href="routing/RoutePlace-class.html#instance-methods">Methods</a></li>
<li><a href="routing/RoutePlace/isOffRoad.html">isOffRoad</a></li>
<li class="inherited"><a href="routing/RoutePlace/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="routing/RoutePlace/toString.html">toString</a></li>
<li class="section-title"><a href="routing/RoutePlace-class.html#operators">Operators</a></li>
<li><a href="routing/RoutePlace/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li class="self-crumb">RoutePlace class</li>
</ol>
<div class="self-name">RoutePlace</div>
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
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/RoutePlace-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>RoutePlace class</h1></div>
<section class="desc markdown">
<p>The location information.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="RoutePlace">
<a href="../routing/RoutePlace/RoutePlace.html">/sdk-for-flutter-explore-routing-routeplace-routeplace</a>(<a href="../routing/RoutePlaceType.html">/sdk-for-flutter-explore-routing-routeplacetype</a> type, <a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a> mapMatchedCoordinates)
</dt>
<dd>
          Creates a new instance.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="chargeInKilowattHours">
<a href="../routing/RoutePlace/chargeInKilowattHours.html">/sdk-for-flutter-explore-routing-routeplace-chargeinkilowatthours</a>
↔ double?
</dt>
<dd>
  Estimated battery charge in kWh for electric vehicles when leaving this place.
Available only if the route was calculated with <a href="../routing/ElectricVehicleOptions/ensureReachability.html">/sdk-for-flutter-explore-routing-electricvehicleoptions-ensurereachability</a> = <code>true</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="chargingStation">
<a href="../routing/RoutePlace/chargingStation.html">/sdk-for-flutter-explore-routing-routeplace-chargingstation</a>
↔ <a href="../routing/ChargingStation-class.html">/sdk-for-flutter-explore-routing-chargingstation-class</a>?
</dt>
<dd>
  Charging station data for electric vehicles.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="displayCoordinates">
<a href="../routing/RoutePlace/displayCoordinates.html">/sdk-for-flutter-explore-routing-routeplace-displaycoordinates</a>
↔ <a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a>?
</dt>
<dd>
  Location of the Points of Interest (PoI) to be displayed in the visualization.
In the map data, PoI have a set of display coordinates as well as a set of access/routing coordinates.
While the access/routing coordinates specify the nearest accessible road network location
that can be apart from actual location of the PoI,
the display coordinates specify the location of the PoI to be displayed accurately in the visualization.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
<a href="../routing/RoutePlace/hashCode.html">/sdk-for-flutter-explore-routing-routeplace-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="id">
<a href="../routing/RoutePlace/id.html">/sdk-for-flutter-explore-routing-routeplace-id</a>
↔ String?
</dt>
<dd>
  Identifier of a public transit place if available.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="mapMatchedCoordinates">
<a href="../routing/RoutePlace/mapMatchedCoordinates.html">/sdk-for-flutter-explore-routing-routeplace-mapmatchedcoordinates</a>
↔ <a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a>
</dt>
<dd>
  Map-matched geographic coordinates.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="name">
<a href="../routing/RoutePlace/name.html">/sdk-for-flutter-explore-routing-routeplace-name</a>
↔ String?
</dt>
<dd>
  Name of a public transit place if available.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="originalCoordinates">
<a href="../routing/RoutePlace/originalCoordinates.html">/sdk-for-flutter-explore-routing-routeplace-originalcoordinates</a>
↔ <a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a>?
</dt>
<dd>
  User-defined geographic coordinates. If not available, it means this place
was added during route calculation.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="platform">
<a href="../routing/RoutePlace/platform.html">/sdk-for-flutter-explore-routing-routeplace-platform</a>
↔ String?
</dt>
<dd>
  Platform name or number of a public transit place if available.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../routing/RoutePlace/runtimeType.html">/sdk-for-flutter-explore-routing-routeplace-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="sideOfDestination">
<a href="../routing/RoutePlace/sideOfDestination.html">/sdk-for-flutter-explore-routing-routeplace-sideofdestination</a>
↔ <a href="../routing/SideOfDestination.html">/sdk-for-flutter-explore-routing-sideofdestination</a>?
</dt>
<dd>
  Side of destination: left, right or undefined.
<code>null</code> for transit sections and for origin points.
<code>UNDEFINED</code> if <code>originalCoordinates</code> are not identified or too close to the road.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="type">
<a href="../routing/RoutePlace/type.html">/sdk-for-flutter-explore-routing-routeplace-type</a>
↔ <a href="../routing/RoutePlaceType.html">/sdk-for-flutter-explore-routing-routeplacetype</a>
</dt>
<dd>
  The type of the route place.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="waypointIndex">
<a href="../routing/RoutePlace/waypointIndex.html">/sdk-for-flutter-explore-routing-routeplace-waypointindex</a>
↔ int?
</dt>
<dd>
  If available, this index corresponds to the waypoint in the original
user-defined waypoint list. Otherwise, this waypoint was added during
route calculation by the system.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="isOffRoad">
<a href="../routing/RoutePlace/isOffRoad.html">/sdk-for-flutter-explore-routing-routeplace-isoffroad</a>(<wbr/>)
    → bool

</dt>
<dd>
  Checks whether the <a href="../routing/RoutePlace-class.html">/sdk-for-flutter-explore-routing-routeplace-class</a> is off-road or not.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
<a href="../routing/RoutePlace/noSuchMethod.html">/sdk-for-flutter-explore-routing-routeplace-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../routing/RoutePlace/toString.html">/sdk-for-flutter-explore-routing-routeplace-tostring</a>(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable" id="operator ==">
<a href="../routing/RoutePlace/operator_equals.html">/sdk-for-flutter-explore-routing-routeplace-operator-equals</a>(<wbr/>Object other)
    → bool

</dt>
<dd>
  The equality operator.
  

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
<li class="self-crumb">RoutePlace class</li>
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
