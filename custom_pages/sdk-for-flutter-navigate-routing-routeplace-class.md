---
title: "RoutePlace class"
slug: "sdk-for-flutter-navigate-routing-routeplace-class"
---

<HTMLBlock>{
`
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
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
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
/sdk-for-flutter-navigate-routing-routeplace-routeplace(/sdk-for-flutter-navigate-routing-routeplacetype type, /sdk-for-flutter-navigate-core-geocoordinates-class mapMatchedCoordinates)
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
/sdk-for-flutter-navigate-routing-routeplace-chargeinkilowatthours
↔ double?
</dt>
<dd>
  Estimated battery charge in kWh for electric vehicles when leaving this place.
Available only if the route was calculated with /sdk-for-flutter-navigate-routing-electricvehicleoptions-ensurereachability = <code>true</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="chargingStation">
/sdk-for-flutter-navigate-routing-routeplace-chargingstation
↔ /sdk-for-flutter-navigate-routing-chargingstation-class?
</dt>
<dd>
  Charging station data for electric vehicles.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="displayCoordinates">
/sdk-for-flutter-navigate-routing-routeplace-displaycoordinates
↔ /sdk-for-flutter-navigate-core-geocoordinates-class?
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
/sdk-for-flutter-navigate-routing-routeplace-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="id">
/sdk-for-flutter-navigate-routing-routeplace-id
↔ String?
</dt>
<dd>
  Identifier of a public transit place if available.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="mapMatchedCoordinates">
/sdk-for-flutter-navigate-routing-routeplace-mapmatchedcoordinates
↔ /sdk-for-flutter-navigate-core-geocoordinates-class
</dt>
<dd>
  Map-matched geographic coordinates.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="name">
/sdk-for-flutter-navigate-routing-routeplace-name
↔ String?
</dt>
<dd>
  Name of a public transit place if available.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="originalCoordinates">
/sdk-for-flutter-navigate-routing-routeplace-originalcoordinates
↔ /sdk-for-flutter-navigate-core-geocoordinates-class?
</dt>
<dd>
  User-defined geographic coordinates. If not available, it means this place
was added during route calculation.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="platform">
/sdk-for-flutter-navigate-routing-routeplace-platform
↔ String?
</dt>
<dd>
  Platform name or number of a public transit place if available.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-routing-routeplace-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="sideOfDestination">
/sdk-for-flutter-navigate-routing-routeplace-sideofdestination
↔ /sdk-for-flutter-navigate-routing-sideofdestination?
</dt>
<dd>
  Side of destination: left, right or undefined.
<code>null</code> for transit sections and for origin points.
<code>UNDEFINED</code> if <code>originalCoordinates</code> are not identified or too close to the road.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="type">
/sdk-for-flutter-navigate-routing-routeplace-type
↔ /sdk-for-flutter-navigate-routing-routeplacetype
</dt>
<dd>
  The type of the route place.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="waypointIndex">
/sdk-for-flutter-navigate-routing-routeplace-waypointindex
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
/sdk-for-flutter-navigate-routing-routeplace-isoffroad(<wbr/>)
    → bool

</dt>
<dd>
  Checks whether the /sdk-for-flutter-navigate-routing-routeplace-class is off-road or not.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-routing-routeplace-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-routing-routeplace-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-routing-routeplace-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
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
`
}</HTMLBlock>
