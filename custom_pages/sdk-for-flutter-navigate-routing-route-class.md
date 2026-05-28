---
title: "Route class abstract"
slug: "sdk-for-flutter-navigate-routing-route-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- Route-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="routing/Route-class.html#constructors">Constructors</a></li>
<li><a href="routing/Route/Route.html">Route</a></li>
<li class="section-title">
<a href="routing/Route-class.html#instance-properties">Properties</a>
</li>
<li><a href="routing/Route/boundingBox.html">boundingBox</a></li>
<li><a href="routing/Route/consumptionInKilowattHours.html">consumptionInKilowattHours</a></li>
<li><a href="routing/Route/duration.html">duration</a></li>
<li><a href="routing/Route/geometry.html">geometry</a></li>
<li class="inherited"><a href="routing/Route/hashCode.html">hashCode</a></li>
<li><a href="routing/Route/language.html">language</a></li>
<li><a href="routing/Route/lengthInMeters.html">lengthInMeters</a></li>
<li><a href="routing/Route/optimizationMode.html">optimizationMode</a></li>
<li><a href="routing/Route/railwayCrossings.html">railwayCrossings</a></li>
<li><a href="routing/Route/requestedTransportMode.html">requestedTransportMode</a></li>
<li><a href="routing/Route/routeHandle.html">routeHandle</a></li>
<li><a href="routing/Route/routeLabels.html">routeLabels</a></li>
<li><a href="routing/Route/routingOptions.html">routingOptions</a></li>
<li class="inherited"><a href="routing/Route/runtimeType.html">runtimeType</a></li>
<li><a href="routing/Route/sections.html">sections</a></li>
<li><a href="routing/Route/trafficDelay.html">trafficDelay</a></li>
<li class="section-title inherited"><a href="routing/Route-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="routing/Route/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="routing/Route/toString.html">toString</a></li>
<li class="section-title inherited"><a href="routing/Route-class.html#operators">Operators</a></li>
<li class="inherited"><a href="routing/Route/operator_equals.html">operator ==</a></li>
<li class="section-title"><a href="routing/Route-class.html#static-methods">Static methods</a></li>
<li><a href="routing/Route/deserialize.html">deserialize</a></li>
<li><a href="routing/Route/serialize.html">serialize</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li class="self-crumb">Route class</li>
</ol>
<div class="self-name">Route</div>
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
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/Route-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>Route class abstract</h1></div>
<section class="desc markdown">
<p>A route is a path through a road network over which someone travels.</p>
<p><strong>Note:</strong> Each /sdk-for-flutter-navigate-routing-section-class of a route contains a list of /sdk-for-flutter-navigate-routing-sectionnotice-class objects
that describe <em>potential issues</em> after the route was calculated. If the list is non-empty,
it is recommended to evaluate possible violations against the requested route options and
reject the route if deemed necessary.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="Route">
/sdk-for-flutter-navigate-routing-route-route()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="boundingBox">
/sdk-for-flutter-navigate-routing-route-boundingbox
→ /sdk-for-flutter-navigate-core-geobox-class
</dt>
<dd>
  The closest rectangular area where this route fits in.
Gets the closest rectangular area where this route fits in.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="consumptionInKilowattHours">
/sdk-for-flutter-navigate-routing-route-consumptioninkilowatthours
→ double?
</dt>
<dd>
  Estimated net energy consumption (in kWh) if the transportation mode used for this route
is an electric vehicle. Note that it can be negative due to energy recuperation.
Gets estimated net energy consumption (in kWh) if the transportation mode used for this route
is an electric vehicle. Note that it can be negative due to energy recuperation.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="duration">
/sdk-for-flutter-navigate-routing-route-duration
→ Duration
</dt>
<dd>
  The estimated time in seconds needed to travel along this route, including
real-time traffic delays if available.
Gets the estimated time in seconds needed to travel along this route, including
real-time traffic delays if available.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="geometry">
/sdk-for-flutter-navigate-routing-route-geometry
→ /sdk-for-flutter-navigate-core-geopolyline-class
</dt>
<dd>
  The /sdk-for-flutter-navigate-core-geopolyline-class object representing the polyline of this route. It may not contain the original
coordinates specified in the request for a route.
Gets the /sdk-for-flutter-navigate-core-geopolyline-class object representing the polyline of this route. It may not contain the original
coordinates specified in the request for a route.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-routing-route-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="language">
/sdk-for-flutter-navigate-routing-route-language
→ /sdk-for-flutter-navigate-core-languagecode
</dt>
<dd>
  Indicates the language requested for all textual information related to this route.
Gets the language requested for all textual information related to this route.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="lengthInMeters">
/sdk-for-flutter-navigate-routing-route-lengthinmeters
→ int
</dt>
<dd>
  The length of this route in meters.
Gets the length of this route in meters.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="optimizationMode">
/sdk-for-flutter-navigate-routing-route-optimizationmode
→ /sdk-for-flutter-navigate-routing-optimizationmode
</dt>
<dd>
  The optimization mode requested for route calculation.
Gets the optimization mode requested for route calculation.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="railwayCrossings">
/sdk-for-flutter-navigate-routing-route-railwaycrossings
→ List&lt;<wbr/>/sdk-for-flutter-navigate-routing-routerailwaycrossing-class&gt;
</dt>
<dd>
  Collection of railway crossings along the route.
Railway crossing information is only available for routes created with the online <code>RoutingEngine</code>.
Gets railway crossings.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="requestedTransportMode">
/sdk-for-flutter-navigate-routing-route-requestedtransportmode
→ /sdk-for-flutter-navigate-transport-transportmode
</dt>
<dd>
  The transport mode requested for route calculation.
Gets the transport mode requested for route calculation.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="routeHandle">
/sdk-for-flutter-navigate-routing-route-routehandle
→ /sdk-for-flutter-navigate-routing-routehandle-class?
</dt>
<dd>
  The route handle of this route. Note that it is provided only if
/sdk-for-flutter-navigate-routing-routeoptions-enableroutehandle is set before route calculation.
Gets the route handle of this route. Note that it is provided only if
/sdk-for-flutter-navigate-routing-routeoptions-enableroutehandle is set before route calculation.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="routeLabels">
/sdk-for-flutter-navigate-routing-route-routelabels
→ List&lt;<wbr/>/sdk-for-flutter-navigate-routing-routelabel-class&gt;
</dt>
<dd>
  A collection containing a maximum of 2 <code>RouteLabel</code> instances for the route. It will return an empty list if no labels are available.
The main street names or route numbers through which the route is going to pass that differentiate it from other alternatives routes.
The labels are ordered by importance based on how much time the route spends on each road segment, not by traversal sequence. This helps users quickly identify and distinguish between different route alternatives
when alternative routes have been quested via <code>RouteOptions</code>.
Gets route labels.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="routingOptions">
/sdk-for-flutter-navigate-routing-route-routingoptions
→ /sdk-for-flutter-navigate-routing-routingoptions-class?
</dt>
<dd>
  The set of options used to calculate the route.
Gets the options used to calculate this route.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-routing-route-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="sections">
/sdk-for-flutter-navigate-routing-route-sections
→ List&lt;<wbr/>/sdk-for-flutter-navigate-routing-section-class&gt;
</dt>
<dd>
  The sections that make up this route.
Gets the sections that make up this route.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="trafficDelay">
/sdk-for-flutter-navigate-routing-route-trafficdelay
→ Duration
</dt>
<dd>
  The estimated time in seconds spent in traffic along this route. Negative values
indicate that the route can be traversed faster than usual.
Gets the estimated time in seconds spent in traffic along this route. Negative values
indicate that the route can be traversed faster than usual.
  <div class="features">no setter</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-routing-route-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-routing-route-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-routing-route-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="static-methods">
<h2>Static Methods</h2>
<dl class="callables">
<dt class="callable" id="deserialize">
/sdk-for-flutter-navigate-routing-route-deserialize(<wbr/>Uint8List routeData)
    → /sdk-for-flutter-navigate-routing-route-class?

</dt>
<dd>
  Creates route from the given binary data.
  

</dd>
<dt class="callable" id="serialize">
/sdk-for-flutter-navigate-routing-route-serialize(<wbr/>/sdk-for-flutter-navigate-routing-route-class route)
    → Uint8List?

</dt>
<dd>
  Serializes given route to a binary data.
  

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
<li class="self-crumb">Route class</li>
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
