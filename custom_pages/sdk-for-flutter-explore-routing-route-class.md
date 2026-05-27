---
title: "Constructors"
slug: "sdk-for-flutter-explore-routing-route-class"
---

<HTMLBlock>
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
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
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
<p><strong>Note:</strong> Each <a href="../routing/Section-class.html">/sdk-for-flutter-explore-routing-section-class</a> of a route contains a list of <a href="../routing/SectionNotice-class.html">/sdk-for-flutter-explore-routing-sectionnotice-class</a> objects
that describe <em>potential issues</em> after the route was calculated. If the list is non-empty,
it is recommended to evaluate possible violations against the requested route options and
reject the route if deemed necessary.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="Route">
<a href="../routing/Route/Route.html">/sdk-for-flutter-explore-routing-route-route</a>()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="boundingBox">
<a href="../routing/Route/boundingBox.html">/sdk-for-flutter-explore-routing-route-boundingbox</a>
→ <a href="../core/GeoBox-class.html">/sdk-for-flutter-explore-core-geobox-class</a>
</dt>
<dd>
  The closest rectangular area where this route fits in.
Gets the closest rectangular area where this route fits in.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="consumptionInKilowattHours">
<a href="../routing/Route/consumptionInKilowattHours.html">/sdk-for-flutter-explore-routing-route-consumptioninkilowatthours</a>
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
<a href="../routing/Route/duration.html">/sdk-for-flutter-explore-routing-route-duration</a>
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
<a href="../routing/Route/geometry.html">/sdk-for-flutter-explore-routing-route-geometry</a>
→ <a href="../core/GeoPolyline-class.html">/sdk-for-flutter-explore-core-geopolyline-class</a>
</dt>
<dd>
  The <a href="../core/GeoPolyline-class.html">/sdk-for-flutter-explore-core-geopolyline-class</a> object representing the polyline of this route. It may not contain the original
coordinates specified in the request for a route.
Gets the <a href="../core/GeoPolyline-class.html">/sdk-for-flutter-explore-core-geopolyline-class</a> object representing the polyline of this route. It may not contain the original
coordinates specified in the request for a route.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="hashCode">
<a href="../routing/Route/hashCode.html">/sdk-for-flutter-explore-routing-route-hashcode</a>
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="language">
<a href="../routing/Route/language.html">/sdk-for-flutter-explore-routing-route-language</a>
→ <a href="../core/LanguageCode.html">/sdk-for-flutter-explore-core-languagecode</a>
</dt>
<dd>
  Indicates the language requested for all textual information related to this route.
Gets the language requested for all textual information related to this route.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="lengthInMeters">
<a href="../routing/Route/lengthInMeters.html">/sdk-for-flutter-explore-routing-route-lengthinmeters</a>
→ int
</dt>
<dd>
  The length of this route in meters.
Gets the length of this route in meters.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="optimizationMode">
<a href="../routing/Route/optimizationMode.html">/sdk-for-flutter-explore-routing-route-optimizationmode</a>
→ <a href="../routing/OptimizationMode.html">/sdk-for-flutter-explore-routing-optimizationmode</a>
</dt>
<dd>
  The optimization mode requested for route calculation.
Gets the optimization mode requested for route calculation.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="railwayCrossings">
<a href="../routing/Route/railwayCrossings.html">/sdk-for-flutter-explore-routing-route-railwaycrossings</a>
→ List&lt;<wbr/><a href="../routing/RouteRailwayCrossing-class.html">/sdk-for-flutter-explore-routing-routerailwaycrossing-class</a>&gt;
</dt>
<dd>
  Collection of railway crossings along the route.
Railway crossing information is only available for routes created with the online <code>RoutingEngine</code>.
Gets railway crossings.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="requestedTransportMode">
<a href="../routing/Route/requestedTransportMode.html">/sdk-for-flutter-explore-routing-route-requestedtransportmode</a>
→ <a href="../transport/TransportMode.html">/sdk-for-flutter-explore-transport-transportmode</a>
</dt>
<dd>
  The transport mode requested for route calculation.
Gets the transport mode requested for route calculation.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="routeHandle">
<a href="../routing/Route/routeHandle.html">/sdk-for-flutter-explore-routing-route-routehandle</a>
→ <a href="../routing/RouteHandle-class.html">/sdk-for-flutter-explore-routing-routehandle-class</a>?
</dt>
<dd>
  The route handle of this route. Note that it is provided only if
<a href="../routing/RouteOptions/enableRouteHandle.html">/sdk-for-flutter-explore-routing-routeoptions-enableroutehandle</a> is set before route calculation.
Gets the route handle of this route. Note that it is provided only if
<a href="../routing/RouteOptions/enableRouteHandle.html">/sdk-for-flutter-explore-routing-routeoptions-enableroutehandle</a> is set before route calculation.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="routeLabels">
<a href="../routing/Route/routeLabels.html">/sdk-for-flutter-explore-routing-route-routelabels</a>
→ List&lt;<wbr/><a href="../routing/RouteLabel-class.html">/sdk-for-flutter-explore-routing-routelabel-class</a>&gt;
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
<a href="../routing/Route/routingOptions.html">/sdk-for-flutter-explore-routing-route-routingoptions</a>
→ <a href="../routing/RoutingOptions-class.html">/sdk-for-flutter-explore-routing-routingoptions-class</a>?
</dt>
<dd>
  The set of options used to calculate the route.
Gets the options used to calculate this route.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../routing/Route/runtimeType.html">/sdk-for-flutter-explore-routing-route-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="sections">
<a href="../routing/Route/sections.html">/sdk-for-flutter-explore-routing-route-sections</a>
→ List&lt;<wbr/><a href="../routing/Section-class.html">/sdk-for-flutter-explore-routing-section-class</a>&gt;
</dt>
<dd>
  The sections that make up this route.
Gets the sections that make up this route.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="trafficDelay">
<a href="../routing/Route/trafficDelay.html">/sdk-for-flutter-explore-routing-route-trafficdelay</a>
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
<a href="../routing/Route/noSuchMethod.html">/sdk-for-flutter-explore-routing-route-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../routing/Route/toString.html">/sdk-for-flutter-explore-routing-route-tostring</a>(<wbr/>)
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
<a href="../routing/Route/operator_equals.html">/sdk-for-flutter-explore-routing-route-operator-equals</a>(<wbr/>Object other)
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
<a href="../routing/Route/deserialize.html">/sdk-for-flutter-explore-routing-route-deserialize</a>(<wbr/>Uint8List routeData)
    → <a href="../routing/Route-class.html">/sdk-for-flutter-explore-routing-route-class</a>?

</dt>
<dd>
  Creates route from the given binary data.
  

</dd>
<dt class="callable" id="serialize">
<a href="../routing/Route/serialize.html">/sdk-for-flutter-explore-routing-route-serialize</a>(<wbr/><a href="../routing/Route-class.html">/sdk-for-flutter-explore-routing-route-class</a> route)
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
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
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
</HTMLBlock>
