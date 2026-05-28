---
title: "TrafficOnSpan class"
slug: "sdk-for-flutter-navigate-routing-trafficonspan-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TrafficOnSpan-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="routing/TrafficOnSpan-class.html#constructors">Constructors</a></li>
<li><a href="routing/TrafficOnSpan/TrafficOnSpan.html">TrafficOnSpan</a></li>
<li class="section-title">
<a href="routing/TrafficOnSpan-class.html#instance-properties">Properties</a>
</li>
<li><a href="routing/TrafficOnSpan/baseSpeedInMetersPerSecond.html">baseSpeedInMetersPerSecond</a></li>
<li><a href="routing/TrafficOnSpan/consumptionInKilowattHours.html">consumptionInKilowattHours</a></li>
<li><a href="routing/TrafficOnSpan/duration.html">duration</a></li>
<li><a href="routing/TrafficOnSpan/hashCode.html">hashCode</a></li>
<li><a href="routing/TrafficOnSpan/incidentIndices.html">incidentIndices</a></li>
<li><a href="routing/TrafficOnSpan/jamFactor.html">jamFactor</a></li>
<li><a href="routing/TrafficOnSpan/lengthInMeters.html">lengthInMeters</a></li>
<li class="inherited"><a href="routing/TrafficOnSpan/runtimeType.html">runtimeType</a></li>
<li><a href="routing/TrafficOnSpan/trafficDelay.html">trafficDelay</a></li>
<li><a href="routing/TrafficOnSpan/trafficSectionPolylineOffset.html">trafficSectionPolylineOffset</a></li>
<li><a href="routing/TrafficOnSpan/trafficSpeedInMetersPerSecond.html">trafficSpeedInMetersPerSecond</a></li>
<li class="section-title inherited"><a href="routing/TrafficOnSpan-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="routing/TrafficOnSpan/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="routing/TrafficOnSpan/toString.html">toString</a></li>
<li class="section-title"><a href="routing/TrafficOnSpan-class.html#operators">Operators</a></li>
<li><a href="routing/TrafficOnSpan/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li class="self-crumb">TrafficOnSpan class</li>
</ol>
<div class="self-name">TrafficOnSpan</div>
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
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/TrafficOnSpan-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>TrafficOnSpan class</h1></div>
<section class="desc markdown">
<p>Traffic information of a span along a route.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="TrafficOnSpan">
/sdk-for-flutter-navigate-routing-trafficonspan-trafficonspan()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="baseSpeedInMetersPerSecond">
/sdk-for-flutter-navigate-routing-trafficonspan-basespeedinmeterspersecond
↔ double
</dt>
<dd>
  The speed, in meters per second, without taking traffic into consideration.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="consumptionInKilowattHours">
/sdk-for-flutter-navigate-routing-trafficonspan-consumptioninkilowatthours
↔ double?
</dt>
<dd>
  The power consumption in kilowatt-hours (kWh) necessary to traverse the span.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="duration">
/sdk-for-flutter-navigate-routing-trafficonspan-duration
↔ Duration
</dt>
<dd>
  The time duration necessary to traverse the traffic span. This duration takes also into
consideration the delays caused by the traffic.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-routing-trafficonspan-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="incidentIndices">
/sdk-for-flutter-navigate-routing-trafficonspan-incidentindices
↔ List&lt;<wbr/>int&gt;
</dt>
<dd>
  The indices of traffic incidents from the field /sdk-for-flutter-navigate-routing-trafficonsection-trafficincidents.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="jamFactor">
/sdk-for-flutter-navigate-routing-trafficonspan-jamfactor
↔ double
</dt>
<dd>
  The traffic jam factor shows the traffic condition in a numeric way. It is a
value in the range [0.0, 10.0]. A large jamFactor value means more traffic jam
in general. Specifically, 0.0 means free traffic and 10.0 means stationary traffic.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="lengthInMeters">
/sdk-for-flutter-navigate-routing-trafficonspan-lengthinmeters
↔ double
</dt>
<dd>
  Length of the traffic span, in meters.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-routing-trafficonspan-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="trafficDelay">
/sdk-for-flutter-navigate-routing-trafficonspan-trafficdelay
↔ Duration
</dt>
<dd>
  The estimated extra time in seconds spent due to traffic delays along this traffic span.
Negative values indicate that the traffic span can be traversed faster than usual.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="trafficSectionPolylineOffset">
/sdk-for-flutter-navigate-routing-trafficonspan-trafficsectionpolylineoffset
↔ int
</dt>
<dd>
  Index over /sdk-for-flutter-navigate-routing-trafficonsection-geometry where this span starts.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="trafficSpeedInMetersPerSecond">
/sdk-for-flutter-navigate-routing-trafficonspan-trafficspeedinmeterspersecond
↔ double
</dt>
<dd>
  The speed, in meters per second, considering traffic.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-routing-trafficonspan-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-routing-trafficonspan-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-routing-trafficonspan-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">TrafficOnSpan class</li>
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
