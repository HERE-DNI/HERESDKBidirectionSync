---
title: "Untitled"
slug: "sdk-for-flutter-explore-routing-trafficincidentonroute-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TrafficIncidentOnRoute-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-routing-routing-library</li>
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
<p>Use /sdk-for-flutter-explore-routing-section-trafficincidents to get a list of incidents on a route section.
Use /sdk-for-flutter-explore-routing-span-trafficincidentindexes to associate incidents with spans. Each incident takes at least the whole geometry of matching spans.
Also, an incident can take some place out of the built route.</p>
</section>
<section>
<dl class="dl-horizontal">
<dt>Implemented types</dt>
<dd>
<ul class="comma-separated clazz-relationships">
<li>/sdk-for-flutter-explore-traffic-trafficincidentbase-class</li>
</ul>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="TrafficIncidentOnRoute">
/sdk-for-flutter-explore-routing-trafficincidentonroute-trafficincidentonroute()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="description">
/sdk-for-flutter-explore-traffic-trafficincidentbase-description
→ /sdk-for-flutter-explore-core-localizedtext-class
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
/sdk-for-flutter-explore-traffic-trafficincidentbase-endtime
→ DateTime?
</dt>
<dd class="inherited">
  The time until which the incident is valid, after this time the incident should not be considered.
The value is <code>null</code> if it hasn't been provided by the traffic incidents supplier.
Get the time until which the incident is valid, after this time the incident should not be considered.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-explore-traffic-trafficincidentbase-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="id">
/sdk-for-flutter-explore-routing-trafficincidentonroute-id
→ String?
</dt>
<dd>
  The unique current identifier for a traffic incident.
The identifier can be changed by the backend due to some events, e.g. changing of
/sdk-for-flutter-explore-traffic-trafficincidentbase-endtime. This field will be empty for <code>OfflineRouting</code>.
Gets the unique current identifier for a traffic incident.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="impact">
/sdk-for-flutter-explore-traffic-trafficincidentbase-impact
→ /sdk-for-flutter-explore-traffic-trafficincidentimpact
</dt>
<dd class="inherited">
  The impact of the incident.
The value is /sdk-for-flutter-explore-traffic-trafficincidentimpact if it hasn't been provided by the traffic incidents supplier.
Gets the impact of the incident.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-traffic-trafficincidentbase-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="startTime">
/sdk-for-flutter-explore-traffic-trafficincidentbase-starttime
→ DateTime?
</dt>
<dd class="inherited">
  The time from which the incident is valid, before this time the incident should not be considered.
The value is <code>null</code> if it hasn't been provided by the traffic incidents supplier.
Gets the time from which the incident is valid, before this time the incident should not be considered.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="type">
/sdk-for-flutter-explore-traffic-trafficincidentbase-type
→ /sdk-for-flutter-explore-traffic-trafficincidenttype
</dt>
<dd class="inherited">
  The category of the incident.
The value is /sdk-for-flutter-explore-traffic-trafficincidenttype if it hasn't been provided by the traffic incidents supplier.
Gets the category of the incident.
  <div class="features">no setterinherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-explore-traffic-trafficincidentbase-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-traffic-trafficincidentbase-tostring(<wbr/>)
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
/sdk-for-flutter-explore-traffic-trafficincidentbase-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-routing-routing-library</li>
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



</div>
`
}</HTMLBlock>
