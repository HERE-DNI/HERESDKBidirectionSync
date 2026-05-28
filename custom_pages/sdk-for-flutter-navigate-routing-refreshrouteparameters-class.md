---
title: "RefreshRouteParameters class"
slug: "sdk-for-flutter-navigate-routing-refreshrouteparameters-class"
---

<HTMLBlock>{
`
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
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
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
/sdk-for-flutter-navigate-routing-refreshrouteparameters-refreshrouteparameters-withroutehandleandsectionposition(/sdk-for-flutter-navigate-routing-routehandle-class routeHandle, int startingSectionIndex, int traveledDistanceOnStartingSectionInMeters)
</dt>
<dd>
          Create a new instance of /sdk-for-flutter-navigate-routing-refreshrouteparameters-class with the point on the section of the route as a new starting point.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="RefreshRouteParameters.withRouteHandleAndWaypoint">
/sdk-for-flutter-navigate-routing-refreshrouteparameters-refreshrouteparameters-withroutehandleandwaypoint(/sdk-for-flutter-navigate-routing-routehandle-class routeHandle, /sdk-for-flutter-navigate-routing-waypoint-class startingPoint)
</dt>
<dd>
          Create a new instance of /sdk-for-flutter-navigate-routing-refreshrouteparameters-class with the new starting point on the route.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="RefreshRouteParameters.withRouteHandleAndWaypointAndSectionPosition">
/sdk-for-flutter-navigate-routing-refreshrouteparameters-refreshrouteparameters-withroutehandleandwaypointandsectionposition(/sdk-for-flutter-navigate-routing-routehandle-class routeHandle, /sdk-for-flutter-navigate-routing-waypoint-class startingPoint, int startingSectionIndex, int traveledDistanceOnStartingSectionInMeters)
</dt>
<dd>
          Create a new instance of /sdk-for-flutter-navigate-routing-refreshrouteparameters-class with the new starting point and the section position on the route.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-routing-refreshrouteparameters-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="routeHandle">
/sdk-for-flutter-navigate-routing-refreshrouteparameters-routehandle
↔ /sdk-for-flutter-navigate-routing-routehandle-class
</dt>
<dd>
  The route handle holding the route to be refreshed.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-routing-refreshrouteparameters-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="startingPoint">
/sdk-for-flutter-navigate-routing-refreshrouteparameters-startingpoint
↔ /sdk-for-flutter-navigate-routing-waypoint-class?
</dt>
<dd>
  Identify the new starting point of the route. It should be of type /sdk-for-flutter-navigate-routing-waypointtype.
Otherwise, an /sdk-for-flutter-navigate-routing-routingerror error is generated. Moreover, it should be very close to the
original route specified with the /sdk-for-flutter-navigate-routing-routehandle-class. The location of this waypoint may by provided,
for example, by a <code>RouteProgress</code> event. Since the new starting point is expected to be
along the original route, the original route geometry is used to reach the remaining waypoints. The new route
will not include the /sdk-for-flutter-navigate-routing-waypoint-class items that lie behind the new starting point (i.e. the path that
was already traveled). Plus, /sdk-for-flutter-navigate-routing-route-lengthinmeters, /sdk-for-flutter-navigate-routing-route-duration, and similar
values are from the new starting point to the destination. If the new waypoint is too far off the original
route, the route refresh may fail and an /sdk-for-flutter-navigate-routing-routingerror error is triggered.
In that case, an application may decide to calculate a new route from scratch.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="startingSectionIndex">
/sdk-for-flutter-navigate-routing-refreshrouteparameters-startingsectionindex
↔ int?
</dt>
<dd>
  Indicates the index of the last traveled route section. When it is provided, the previous sections are discarded
from the refreshed route and the starting point is searched in the provided section. If the starting point
is not found in that section an /sdk-for-flutter-navigate-routing-routingerror error is triggered.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="traveledDistanceOnStartingSectionInMeters">
/sdk-for-flutter-navigate-routing-refreshrouteparameters-traveleddistanceonstartingsectioninmeters
↔ int?
</dt>
<dd>
  Provides an indication on how much of the starting section is already traveled. The refresh route function
would ignore the first part of the section. If it is provided with an invalid starting section index, an
/sdk-for-flutter-navigate-routing-routingerror error is generated.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-routing-refreshrouteparameters-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-routing-refreshrouteparameters-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-routing-refreshrouteparameters-operator-equals(<wbr/>Object other)
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
`
}</HTMLBlock>
