---
title: "TransitRouteOptions class"
slug: "sdk-for-flutter-navigate-routing-transitrouteoptions-class"
---

<HTMLBlock>{
`
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
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
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
/sdk-for-flutter-navigate-routing-transitrouteoptions-transitrouteoptions()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="alternatives">
/sdk-for-flutter-navigate-routing-transitrouteoptions-alternatives
↔ int
</dt>
<dd>
  Number of alternative routes to return aside from the optimal route.
The provided value must be in the range [0, 6].
By default, it is 0 and only one route is calculated.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="arrivalTime">
/sdk-for-flutter-navigate-routing-transitrouteoptions-arrivaltime
↔ DateTime?
</dt>
<dd>
  Optional time when travel is expected to end.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="changes">
/sdk-for-flutter-navigate-routing-transitrouteoptions-changes
↔ int?
</dt>
<dd>
  Maximum number of changes or transfers allowed in a route.
When it is not set, unlimited number of changes is permitted.
The provided value must be in the range [0, 6].
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="departureTime">
/sdk-for-flutter-navigate-routing-transitrouteoptions-departuretime
↔ DateTime?
</dt>
<dd>
  Optional time when travel is expected to start.
If it is not specified, it is set to the current time.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-routing-transitrouteoptions-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="modeFilter">
/sdk-for-flutter-navigate-routing-transitrouteoptions-modefilter
↔ /sdk-for-flutter-navigate-routing-transitmodefilter
</dt>
<dd>
  Defines inclusion or exclusion of transit modes for route calculation.
By default, the inclusion mode is used.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="modes">
/sdk-for-flutter-navigate-routing-transitrouteoptions-modes
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-routing-transitmode&gt;
</dt>
<dd>
  This list is used to determine which transit modes should be used for route calculation,
/sdk-for-flutter-navigate-routing-transitrouteoptions-modefilter specifies whether this list is an inclusion or an exclusion.
For example, specifying subway and bus transit modes with the include filter, returns only subway
and bus transit modes, and with the exclude filter, returns all the transit modes except subway
and bus. When not set, all the supported transit modes are permitted.
By default, this list is empty.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="pedestrianMaxDistanceInMeters">
/sdk-for-flutter-navigate-routing-transitrouteoptions-pedestrianmaxdistanceinmeters
↔ int
</dt>
<dd>
  Maximum allowed walking distance in meters (e.g. when looking for nearest stations).
The provided value must be in the range [0, 6000].
The default value is 2000 meters.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="pedestrianSpeedInMetersPerSecond">
/sdk-for-flutter-navigate-routing-transitrouteoptions-pedestrianspeedinmeterspersecond
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
/sdk-for-flutter-navigate-routing-transitrouteoptions-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="textOptions">
/sdk-for-flutter-navigate-routing-transitrouteoptions-textoptions
↔ /sdk-for-flutter-navigate-routing-routetextoptions-class
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
/sdk-for-flutter-navigate-routing-transitrouteoptions-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-routing-transitrouteoptions-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-routing-transitrouteoptions-operator-equals(<wbr/>Object other)
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
/sdk-for-flutter-navigate-routing-transitrouteoptions-fromdefaultparameterconfiguration(<wbr/>)
    → /sdk-for-flutter-navigate-routing-transitrouteoptions-class

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
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
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
`
}</HTMLBlock>
