---
title: "Constructors"
slug: "sdk-for-flutter-explore-routing-transitrouteoptions-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- TransitRouteOptions-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="routing/TransitRouteOptions-class.html#constructors">Constructors</a></li>
<li><a href="routing/TransitRouteOptions/TransitRouteOptions.html">TransitRouteOptions</a></li>
<li class="section-title">
<a href="routing/TransitRouteOptions-class.html#instance-properties">Properties</a>
</li>
<li><a href="routing/TransitRouteOptions/alternatives.html">alternatives</a></li>
<li><a href="routing/TransitRouteOptions/arrivalTime.html">arrivalTime</a></li>
<li><a href="routing/TransitRouteOptions/changes.html">changes</a></li>
<li><a href="routing/TransitRouteOptions/departureTime.html">departureTime</a></li>
<li><a href="routing/TransitRouteOptions/hashCode.html">hashCode</a></li>
<li><a href="routing/TransitRouteOptions/modeFilter.html">modeFilter</a></li>
<li><a href="routing/TransitRouteOptions/modes.html">modes</a></li>
<li><a href="routing/TransitRouteOptions/pedestrianMaxDistanceInMeters.html">pedestrianMaxDistanceInMeters</a></li>
<li><a href="routing/TransitRouteOptions/pedestrianSpeedInMetersPerSecond.html">pedestrianSpeedInMetersPerSecond</a></li>
<li class="inherited"><a href="routing/TransitRouteOptions/runtimeType.html">runtimeType</a></li>
<li><a href="routing/TransitRouteOptions/textOptions.html">textOptions</a></li>
<li class="section-title inherited"><a href="routing/TransitRouteOptions-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="routing/TransitRouteOptions/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="routing/TransitRouteOptions/toString.html">toString</a></li>
<li class="section-title"><a href="routing/TransitRouteOptions-class.html#operators">Operators</a></li>
<li><a href="routing/TransitRouteOptions/operator_equals.html">operator ==</a></li>
<li class="section-title"><a href="routing/TransitRouteOptions-class.html#static-methods">Static methods</a></li>
<li><a href="routing/TransitRouteOptions/fromDefaultParameterConfiguration.html">fromDefaultParameterConfiguration</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li class="self-crumb">TransitRouteOptions class</li>
</ol>
<div class="self-name">TransitRouteOptions</div>
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
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/TransitRouteOptions-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>TransitRouteOptions class</h1></div>
<section class="desc markdown">
<p>All the options to specify how a public transit route should be calculated.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="TransitRouteOptions">
<a href="../routing/TransitRouteOptions/TransitRouteOptions.html">/sdk-for-flutter-explore-routing-transitrouteoptions-transitrouteoptions</a>()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="alternatives">
<a href="../routing/TransitRouteOptions/alternatives.html">/sdk-for-flutter-explore-routing-transitrouteoptions-alternatives</a>
↔ int
</dt>
<dd>
  Number of alternative routes to return aside from the optimal route.
The provided value must be in the range [0, 6].
By default, it is 0 and only one route is calculated.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="arrivalTime">
<a href="../routing/TransitRouteOptions/arrivalTime.html">/sdk-for-flutter-explore-routing-transitrouteoptions-arrivaltime</a>
↔ DateTime?
</dt>
<dd>
  Optional time when travel is expected to end.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="changes">
<a href="../routing/TransitRouteOptions/changes.html">/sdk-for-flutter-explore-routing-transitrouteoptions-changes</a>
↔ int?
</dt>
<dd>
  Maximum number of changes or transfers allowed in a route.
When it is not set, unlimited number of changes is permitted.
The provided value must be in the range [0, 6].
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="departureTime">
<a href="../routing/TransitRouteOptions/departureTime.html">/sdk-for-flutter-explore-routing-transitrouteoptions-departuretime</a>
↔ DateTime?
</dt>
<dd>
  Optional time when travel is expected to start.
If it is not specified, it is set to the current time.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
<a href="../routing/TransitRouteOptions/hashCode.html">/sdk-for-flutter-explore-routing-transitrouteoptions-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="modeFilter">
<a href="../routing/TransitRouteOptions/modeFilter.html">/sdk-for-flutter-explore-routing-transitrouteoptions-modefilter</a>
↔ <a href="../routing/TransitModeFilter.html">/sdk-for-flutter-explore-routing-transitmodefilter</a>
</dt>
<dd>
  Defines inclusion or exclusion of transit modes for route calculation.
By default, the inclusion mode is used.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="modes">
<a href="../routing/TransitRouteOptions/modes.html">/sdk-for-flutter-explore-routing-transitrouteoptions-modes</a>
↔ List&lt;<wbr/><a href="../routing/TransitMode.html">/sdk-for-flutter-explore-routing-transitmode</a>&gt;
</dt>
<dd>
  This list is used to determine which transit modes should be used for route calculation,
<a href="../routing/TransitRouteOptions/modeFilter.html">/sdk-for-flutter-explore-routing-transitrouteoptions-modefilter</a> specifies whether this list is an inclusion or an exclusion.
For example, specifying subway and bus transit modes with the include filter, returns only subway
and bus transit modes, and with the exclude filter, returns all the transit modes except subway
and bus. When not set, all the supported transit modes are permitted.
By default, this list is empty.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="pedestrianMaxDistanceInMeters">
<a href="../routing/TransitRouteOptions/pedestrianMaxDistanceInMeters.html">/sdk-for-flutter-explore-routing-transitrouteoptions-pedestrianmaxdistanceinmeters</a>
↔ int
</dt>
<dd>
  Maximum allowed walking distance in meters (e.g. when looking for nearest stations).
The provided value must be in the range [0, 6000].
The default value is 2000 meters.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="pedestrianSpeedInMetersPerSecond">
<a href="../routing/TransitRouteOptions/pedestrianSpeedInMetersPerSecond.html">/sdk-for-flutter-explore-routing-transitrouteoptions-pedestrianspeedinmeterspersecond</a>
↔ double
</dt>
<dd>
  Walking speed in meters per second. Influences the duration of walking segments from origin to a station,
from a station to destination and in-between the stations (e.g. if transfer is needed).
The provided value must be in the range [0.5, 2.0].
The default value is 1.0 mps.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../routing/TransitRouteOptions/runtimeType.html">/sdk-for-flutter-explore-routing-transitrouteoptions-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="textOptions">
<a href="../routing/TransitRouteOptions/textOptions.html">/sdk-for-flutter-explore-routing-transitrouteoptions-textoptions</a>
↔ <a href="../routing/RouteTextOptions-class.html">/sdk-for-flutter-explore-routing-routetextoptions-class</a>
</dt>
<dd>
  Customize textual content returned from the route calculation, such
as localization, format, and unit system.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
<a href="../routing/TransitRouteOptions/noSuchMethod.html">/sdk-for-flutter-explore-routing-transitrouteoptions-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../routing/TransitRouteOptions/toString.html">/sdk-for-flutter-explore-routing-transitrouteoptions-tostring</a>(<wbr/>)
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
<a href="../routing/TransitRouteOptions/operator_equals.html">/sdk-for-flutter-explore-routing-transitrouteoptions-operator-equals</a>(<wbr/>Object other)
    → bool

</dt>
<dd>
  The equality operator.
  

</dd>
</dl>
</section>
<section class="summary offset-anchor" id="static-methods">
<h2>Static Methods</h2>
<dl class="callables">
<dt class="callable" id="fromDefaultParameterConfiguration">
<a href="../routing/TransitRouteOptions/fromDefaultParameterConfiguration.html">/sdk-for-flutter-explore-routing-transitrouteoptions-fromdefaultparameterconfiguration</a>(<wbr/>)
    → <a href="../routing/TransitRouteOptions-class.html">/sdk-for-flutter-explore-routing-transitrouteoptions-class</a>
</dt>
<dd>
  Returns TransitRouteOptions instance with default values used in SDK.
  

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
<li class="self-crumb">TransitRouteOptions class</li>
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
