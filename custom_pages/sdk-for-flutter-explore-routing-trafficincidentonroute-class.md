---
title: "Constructors"
slug: "sdk-for-flutter-explore-routing-trafficincidentonroute-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- TrafficIncidentOnRoute-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="routing/TrafficIncidentOnRoute-class.html#constructors">Constructors</a></li>
<li><a href="routing/TrafficIncidentOnRoute/TrafficIncidentOnRoute.html">TrafficIncidentOnRoute</a></li>
<li class="section-title">
<a href="routing/TrafficIncidentOnRoute-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="traffic/TrafficIncidentBase/description.html">description</a></li>
<li class="inherited"><a href="traffic/TrafficIncidentBase/endTime.html">endTime</a></li>
<li class="inherited"><a href="traffic/TrafficIncidentBase/hashCode.html">hashCode</a></li>
<li><a href="routing/TrafficIncidentOnRoute/id.html">id</a></li>
<li class="inherited"><a href="traffic/TrafficIncidentBase/impact.html">impact</a></li>
<li class="inherited"><a href="traffic/TrafficIncidentBase/runtimeType.html">runtimeType</a></li>
<li class="inherited"><a href="traffic/TrafficIncidentBase/startTime.html">startTime</a></li>
<li class="inherited"><a href="traffic/TrafficIncidentBase/type.html">type</a></li>
<li class="section-title inherited"><a href="routing/TrafficIncidentOnRoute-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="traffic/TrafficIncidentBase/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="traffic/TrafficIncidentBase/toString.html">toString</a></li>
<li class="section-title inherited"><a href="routing/TrafficIncidentOnRoute-class.html#operators">Operators</a></li>
<li class="inherited"><a href="traffic/TrafficIncidentBase/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li class="self-crumb">TrafficIncidentOnRoute class</li>
</ol>
<div class="self-name">TrafficIncidentOnRoute</div>
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
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/TrafficIncidentOnRoute-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>TrafficIncidentOnRoute class abstract</h1></div>
<section class="desc markdown">
<p>Traffic incidents on a route.</p>
<p>Use <a href="../routing/Section/trafficIncidents.html">/sdk-for-flutter-explore-routing-section-trafficincidents</a> to get a list of incidents on a route section.
Use <a href="../routing/Span/trafficIncidentIndexes.html">/sdk-for-flutter-explore-routing-span-trafficincidentindexes</a> to associate incidents with spans. Each incident takes at least the whole geometry of matching spans.
Also, an incident can take some place out of the built route.</p>
</section>
<section>
<dl class="dl-horizontal">
<dt>Implemented types</dt>
<dd>
<ul class="comma-separated clazz-relationships">
<li><a href="../traffic/TrafficIncidentBase-class.html">/sdk-for-flutter-explore-traffic-trafficincidentbase-class</a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="TrafficIncidentOnRoute">
<a href="../routing/TrafficIncidentOnRoute/TrafficIncidentOnRoute.html">/sdk-for-flutter-explore-routing-trafficincidentonroute-trafficincidentonroute</a>()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="description">
<a href="../traffic/TrafficIncidentBase/description.html">/sdk-for-flutter-explore-traffic-trafficincidentbase-description</a>
→ <a href="../core/LocalizedText-class.html">/sdk-for-flutter-explore-core-localizedtext-class</a>
</dt>
<dd class="inherited">
  The human readable description of the incident, possibly with location information.
The description is currently not present in our map data. Therefore, when
accessing the data from a picked carto POI via <code>TrafficIncidentResult</code>, then
always an empty string is returned. This does not apply when using the <code>TrafficEngine</code>.
Gets the human readable description of the incident, possibly with location information.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="endTime">
<a href="../traffic/TrafficIncidentBase/endTime.html">/sdk-for-flutter-explore-traffic-trafficincidentbase-endtime</a>
→ DateTime?
</dt>
<dd class="inherited">
  The time until which the incident is valid, after this time the incident should not be considered.
The value is <code>null</code> if it hasn't been provided by the traffic incidents supplier.
Get the time until which the incident is valid, after this time the incident should not be considered.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="hashCode">
<a href="../traffic/TrafficIncidentBase/hashCode.html">/sdk-for-flutter-explore-traffic-trafficincidentbase-hashcode</a>
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="id">
<a href="../routing/TrafficIncidentOnRoute/id.html">/sdk-for-flutter-explore-routing-trafficincidentonroute-id</a>
→ String?
</dt>
<dd>
  The unique current identifier for a traffic incident.
The identifier can be changed by the backend due to some events, e.g. changing of
<a href="../traffic/TrafficIncidentBase/endTime.html">/sdk-for-flutter-explore-traffic-trafficincidentbase-endtime</a>. This field will be empty for <code>OfflineRouting</code>.
Gets the unique current identifier for a traffic incident.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="impact">
<a href="../traffic/TrafficIncidentBase/impact.html">/sdk-for-flutter-explore-traffic-trafficincidentbase-impact</a>
→ <a href="../traffic/TrafficIncidentImpact.html">/sdk-for-flutter-explore-traffic-trafficincidentimpact</a>
</dt>
<dd class="inherited">
  The impact of the incident.
The value is <a href="../traffic/TrafficIncidentImpact.html">/sdk-for-flutter-explore-traffic-trafficincidentimpact</a> if it hasn't been provided by the traffic incidents supplier.
Gets the impact of the incident.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../traffic/TrafficIncidentBase/runtimeType.html">/sdk-for-flutter-explore-traffic-trafficincidentbase-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="startTime">
<a href="../traffic/TrafficIncidentBase/startTime.html">/sdk-for-flutter-explore-traffic-trafficincidentbase-starttime</a>
→ DateTime?
</dt>
<dd class="inherited">
  The time from which the incident is valid, before this time the incident should not be considered.
The value is <code>null</code> if it hasn't been provided by the traffic incidents supplier.
Gets the time from which the incident is valid, before this time the incident should not be considered.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="type">
<a href="../traffic/TrafficIncidentBase/type.html">/sdk-for-flutter-explore-traffic-trafficincidentbase-type</a>
→ <a href="../traffic/TrafficIncidentType.html">/sdk-for-flutter-explore-traffic-trafficincidenttype</a>
</dt>
<dd class="inherited">
  The category of the incident.
The value is <a href="../traffic/TrafficIncidentType.html">/sdk-for-flutter-explore-traffic-trafficincidenttype</a> if it hasn't been provided by the traffic incidents supplier.
Gets the category of the incident.
  <div class="features">no setterinherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
<a href="../traffic/TrafficIncidentBase/noSuchMethod.html">/sdk-for-flutter-explore-traffic-trafficincidentbase-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../traffic/TrafficIncidentBase/toString.html">/sdk-for-flutter-explore-traffic-trafficincidentbase-tostring</a>(<wbr/>)
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
<a href="../traffic/TrafficIncidentBase/operator_equals.html">/sdk-for-flutter-explore-traffic-trafficincidentbase-operator-equals</a>(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
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
<li class="self-crumb">TrafficIncidentOnRoute class</li>
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
