---
title: "Constructors"
slug: "sdk-for-flutter-explore-routing-refreshrouteparameters-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- RefreshRouteParameters-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="routing/RefreshRouteParameters-class.html#constructors">Constructors</a></li>
<li><a href="routing/RefreshRouteParameters/RefreshRouteParameters.withRouteHandleAndSectionPosition.html">withRouteHandleAndSectionPosition</a></li>
<li><a href="routing/RefreshRouteParameters/RefreshRouteParameters.withRouteHandleAndWaypoint.html">withRouteHandleAndWaypoint</a></li>
<li><a href="routing/RefreshRouteParameters/RefreshRouteParameters.withRouteHandleAndWaypointAndSectionPosition.html">withRouteHandleAndWaypointAndSectionPosition</a></li>
<li class="section-title">
<a href="routing/RefreshRouteParameters-class.html#instance-properties">Properties</a>
</li>
<li><a href="routing/RefreshRouteParameters/hashCode.html">hashCode</a></li>
<li><a href="routing/RefreshRouteParameters/routeHandle.html">routeHandle</a></li>
<li class="inherited"><a href="routing/RefreshRouteParameters/runtimeType.html">runtimeType</a></li>
<li><a href="routing/RefreshRouteParameters/startingPoint.html">startingPoint</a></li>
<li><a href="routing/RefreshRouteParameters/startingSectionIndex.html">startingSectionIndex</a></li>
<li><a href="routing/RefreshRouteParameters/traveledDistanceOnStartingSectionInMeters.html">traveledDistanceOnStartingSectionInMeters</a></li>
<li class="section-title inherited"><a href="routing/RefreshRouteParameters-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="routing/RefreshRouteParameters/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="routing/RefreshRouteParameters/toString.html">toString</a></li>
<li class="section-title"><a href="routing/RefreshRouteParameters-class.html#operators">Operators</a></li>
<li><a href="routing/RefreshRouteParameters/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li class="self-crumb">RefreshRouteParameters class</li>
</ol>
<div class="self-name">RefreshRouteParameters</div>
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
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/RefreshRouteParameters-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>RefreshRouteParameters class</h1></div>
<section class="desc markdown">
<p>This class provides the necessary information for refreshing a route from a
specific location on it.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="RefreshRouteParameters.withRouteHandleAndSectionPosition">
<a href="../routing/RefreshRouteParameters/RefreshRouteParameters.withRouteHandleAndSectionPosition.html">/sdk-for-flutter-explore-routing-refreshrouteparameters-refreshrouteparameters-withroutehandleandsectionposition</a>(<a href="../routing/RouteHandle-class.html">/sdk-for-flutter-explore-routing-routehandle-class</a> routeHandle, int startingSectionIndex, int traveledDistanceOnStartingSectionInMeters)
</dt>
<dd>
          Create a new instance of <a href="../routing/RefreshRouteParameters-class.html">/sdk-for-flutter-explore-routing-refreshrouteparameters-class</a> with the point on the section of the route as a new starting point.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="RefreshRouteParameters.withRouteHandleAndWaypoint">
<a href="../routing/RefreshRouteParameters/RefreshRouteParameters.withRouteHandleAndWaypoint.html">/sdk-for-flutter-explore-routing-refreshrouteparameters-refreshrouteparameters-withroutehandleandwaypoint</a>(<a href="../routing/RouteHandle-class.html">/sdk-for-flutter-explore-routing-routehandle-class</a> routeHandle, <a href="../routing/Waypoint-class.html">/sdk-for-flutter-explore-routing-waypoint-class</a> startingPoint)
</dt>
<dd>
          Create a new instance of <a href="../routing/RefreshRouteParameters-class.html">/sdk-for-flutter-explore-routing-refreshrouteparameters-class</a> with the new starting point on the route.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="RefreshRouteParameters.withRouteHandleAndWaypointAndSectionPosition">
<a href="../routing/RefreshRouteParameters/RefreshRouteParameters.withRouteHandleAndWaypointAndSectionPosition.html">/sdk-for-flutter-explore-routing-refreshrouteparameters-refreshrouteparameters-withroutehandleandwaypointandsectionposition</a>(<a href="../routing/RouteHandle-class.html">/sdk-for-flutter-explore-routing-routehandle-class</a> routeHandle, <a href="../routing/Waypoint-class.html">/sdk-for-flutter-explore-routing-waypoint-class</a> startingPoint, int startingSectionIndex, int traveledDistanceOnStartingSectionInMeters)
</dt>
<dd>
          Create a new instance of <a href="../routing/RefreshRouteParameters-class.html">/sdk-for-flutter-explore-routing-refreshrouteparameters-class</a> with the new starting point and the section position on the route.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="hashCode">
<a href="../routing/RefreshRouteParameters/hashCode.html">/sdk-for-flutter-explore-routing-refreshrouteparameters-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="routeHandle">
<a href="../routing/RefreshRouteParameters/routeHandle.html">/sdk-for-flutter-explore-routing-refreshrouteparameters-routehandle</a>
↔ <a href="../routing/RouteHandle-class.html">/sdk-for-flutter-explore-routing-routehandle-class</a>
</dt>
<dd>
  The route handle holding the route to be refreshed.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../routing/RefreshRouteParameters/runtimeType.html">/sdk-for-flutter-explore-routing-refreshrouteparameters-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="startingPoint">
<a href="../routing/RefreshRouteParameters/startingPoint.html">/sdk-for-flutter-explore-routing-refreshrouteparameters-startingpoint</a>
↔ <a href="../routing/Waypoint-class.html">/sdk-for-flutter-explore-routing-waypoint-class</a>?
</dt>
<dd>
  Identify the new starting point of the route. It should be of type <a href="../routing/WaypointType.html">/sdk-for-flutter-explore-routing-waypointtype</a>.
Otherwise, an <a href="../routing/RoutingError.html">/sdk-for-flutter-explore-routing-routingerror</a> error is generated. Moreover, it should be very close to the
original route specified with the <a href="../routing/RouteHandle-class.html">/sdk-for-flutter-explore-routing-routehandle-class</a>. The location of this waypoint may by provided,
for example, by a <code>RouteProgress</code> event. Since the new starting point is expected to be
along the original route, the original route geometry is used to reach the remaining waypoints. The new route
will not include the <a href="../routing/Waypoint-class.html">/sdk-for-flutter-explore-routing-waypoint-class</a> items that lie behind the new starting point (i.e. the path that
was already traveled). Plus, <a href="../routing/Route/lengthInMeters.html">/sdk-for-flutter-explore-routing-route-lengthinmeters</a>, <a href="../routing/Route/duration.html">/sdk-for-flutter-explore-routing-route-duration</a>, and similar
values are from the new starting point to the destination. If the new waypoint is too far off the original
route, the route refresh may fail and an <a href="../routing/RoutingError.html">/sdk-for-flutter-explore-routing-routingerror</a> error is triggered.
In that case, an application may decide to calculate a new route from scratch.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="startingSectionIndex">
<a href="../routing/RefreshRouteParameters/startingSectionIndex.html">/sdk-for-flutter-explore-routing-refreshrouteparameters-startingsectionindex</a>
↔ int?
</dt>
<dd>
  Indicates the index of the last traveled route section. When it is provided, the previous sections are discarded
from the refreshed route and the starting point is searched in the provided section. If the starting point
is not found in that section an <a href="../routing/RoutingError.html">/sdk-for-flutter-explore-routing-routingerror</a> error is triggered.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="traveledDistanceOnStartingSectionInMeters">
<a href="../routing/RefreshRouteParameters/traveledDistanceOnStartingSectionInMeters.html">/sdk-for-flutter-explore-routing-refreshrouteparameters-traveleddistanceonstartingsectioninmeters</a>
↔ int?
</dt>
<dd>
  Provides an indication on how much of the starting section is already traveled. The refresh route function
would ignore the first part of the section. If it is provided with an invalid starting section index, an
<a href="../routing/RoutingError.html">/sdk-for-flutter-explore-routing-routingerror</a> error is generated.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
<a href="../routing/RefreshRouteParameters/noSuchMethod.html">/sdk-for-flutter-explore-routing-refreshrouteparameters-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../routing/RefreshRouteParameters/toString.html">/sdk-for-flutter-explore-routing-refreshrouteparameters-tostring</a>(<wbr/>)
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
<a href="../routing/RefreshRouteParameters/operator_equals.html">/sdk-for-flutter-explore-routing-refreshrouteparameters-operator-equals</a>(<wbr/>Object other)
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
<li class="self-crumb">RefreshRouteParameters class</li>
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
