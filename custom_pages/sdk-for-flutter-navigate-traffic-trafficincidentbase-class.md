---
title: "Untitled"
slug: "sdk-for-flutter-navigate-traffic-trafficincidentbase-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TrafficIncidentBase-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-traffic-traffic-library</li>
<li class="self-crumb">TrafficIncidentBase class</li>
</ol>
<div class="self-name">TrafficIncidentBase</div>
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
<div class="main-content" data-above-sidebar="traffic/traffic-library-sidebar.html" data-below-sidebar="traffic/TrafficIncidentBase-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>TrafficIncidentBase class abstract</h1></div>
<section class="desc markdown">
<p>TrafficIncident provides details about a traffic incident.</p>
</section>
<section>
<dl class="dl-horizontal">
<dt>Implementers</dt>
<dd><ul class="comma-separated clazz-relationships">
<li>/sdk-for-flutter-navigate-mapview-picktrafficincidentresult-class</li>
<li>/sdk-for-flutter-navigate-traffic-trafficincident-class</li>
<li>/sdk-for-flutter-navigate-routing-trafficincidentonroute-class</li>
</ul></dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="TrafficIncidentBase">
/sdk-for-flutter-navigate-traffic-trafficincidentbase-trafficincidentbase(/sdk-for-flutter-navigate-traffic-trafficincidentimpact impactGetLambda(), /sdk-for-flutter-navigate-traffic-trafficincidenttype typeGetLambda(), /sdk-for-flutter-navigate-core-localizedtext-class descriptionGetLambda(), DateTime? startTimeGetLambda(), DateTime? endTimeGetLambda())
</dt>
<dd>
          TrafficIncident provides details about a traffic incident.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="description">
/sdk-for-flutter-navigate-traffic-trafficincidentbase-description
→ /sdk-for-flutter-navigate-core-localizedtext-class
</dt>
<dd>
  The human readable description of the incident, possibly with location information.
The description is currently not present in our map data. Therefore, when
accessing the data from a picked carto POI via <code>TrafficIncidentResult</code>, then
always an empty string is returned. This does not apply when using the <code>TrafficEngine</code>.
Gets the human readable description of the incident, possibly with location information.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="endTime">
/sdk-for-flutter-navigate-traffic-trafficincidentbase-endtime
→ DateTime?
</dt>
<dd>
  The time until which the incident is valid, after this time the incident should not be considered.
The value is <code>null</code> if it hasn't been provided by the traffic incidents supplier.
Get the time until which the incident is valid, after this time the incident should not be considered.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-traffic-trafficincidentbase-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="impact">
/sdk-for-flutter-navigate-traffic-trafficincidentbase-impact
→ /sdk-for-flutter-navigate-traffic-trafficincidentimpact
</dt>
<dd>
  The impact of the incident.
The value is /sdk-for-flutter-navigate-traffic-trafficincidentimpact if it hasn't been provided by the traffic incidents supplier.
Gets the impact of the incident.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-traffic-trafficincidentbase-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="startTime">
/sdk-for-flutter-navigate-traffic-trafficincidentbase-starttime
→ DateTime?
</dt>
<dd>
  The time from which the incident is valid, before this time the incident should not be considered.
The value is <code>null</code> if it hasn't been provided by the traffic incidents supplier.
Gets the time from which the incident is valid, before this time the incident should not be considered.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="type">
/sdk-for-flutter-navigate-traffic-trafficincidentbase-type
→ /sdk-for-flutter-navigate-traffic-trafficincidenttype
</dt>
<dd>
  The category of the incident.
The value is /sdk-for-flutter-navigate-traffic-trafficincidenttype if it hasn't been provided by the traffic incidents supplier.
Gets the category of the incident.
  <div class="features">no setter</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-traffic-trafficincidentbase-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-traffic-trafficincidentbase-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-traffic-trafficincidentbase-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-traffic-traffic-library</li>
<li class="self-crumb">TrafficIncidentBase class</li>
</ol>
<h5>traffic library</h5>
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
