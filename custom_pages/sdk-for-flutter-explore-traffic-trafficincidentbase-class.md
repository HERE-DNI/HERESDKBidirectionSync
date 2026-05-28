---
title: "TrafficIncidentBase class abstract"
slug: "sdk-for-flutter-explore-traffic-trafficincidentbase-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TrafficIncidentBase-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="traffic/TrafficIncidentBase-class.html#constructors">Constructors</a></li>
<li><a href="traffic/TrafficIncidentBase/TrafficIncidentBase.html">TrafficIncidentBase</a></li>
<li class="section-title">
<a href="traffic/TrafficIncidentBase-class.html#instance-properties">Properties</a>
</li>
<li><a href="traffic/TrafficIncidentBase/description.html">description</a></li>
<li><a href="traffic/TrafficIncidentBase/endTime.html">endTime</a></li>
<li class="inherited"><a href="traffic/TrafficIncidentBase/hashCode.html">hashCode</a></li>
<li><a href="traffic/TrafficIncidentBase/impact.html">impact</a></li>
<li class="inherited"><a href="traffic/TrafficIncidentBase/runtimeType.html">runtimeType</a></li>
<li><a href="traffic/TrafficIncidentBase/startTime.html">startTime</a></li>
<li><a href="traffic/TrafficIncidentBase/type.html">type</a></li>
<li class="section-title inherited"><a href="traffic/TrafficIncidentBase-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="traffic/TrafficIncidentBase/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="traffic/TrafficIncidentBase/toString.html">toString</a></li>
<li class="section-title inherited"><a href="traffic/TrafficIncidentBase-class.html#operators">Operators</a></li>
<li class="inherited"><a href="traffic/TrafficIncidentBase/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-traffic-traffic-library</li>
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
<li>/sdk-for-flutter-explore-mapview-picktrafficincidentresult-class</li>
<li>/sdk-for-flutter-explore-traffic-trafficincident-class</li>
<li>/sdk-for-flutter-explore-routing-trafficincidentonroute-class</li>
</ul></dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="TrafficIncidentBase">
/sdk-for-flutter-explore-traffic-trafficincidentbase-trafficincidentbase(/sdk-for-flutter-explore-traffic-trafficincidentimpact impactGetLambda(), /sdk-for-flutter-explore-traffic-trafficincidenttype typeGetLambda(), /sdk-for-flutter-explore-core-localizedtext-class descriptionGetLambda(), DateTime? startTimeGetLambda(), DateTime? endTimeGetLambda())
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
/sdk-for-flutter-explore-traffic-trafficincidentbase-description
→ /sdk-for-flutter-explore-core-localizedtext-class
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
/sdk-for-flutter-explore-traffic-trafficincidentbase-endtime
→ DateTime?
</dt>
<dd>
  The time until which the incident is valid, after this time the incident should not be considered.
The value is <code>null</code> if it hasn't been provided by the traffic incidents supplier.
Get the time until which the incident is valid, after this time the incident should not be considered.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-explore-traffic-trafficincidentbase-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="impact">
/sdk-for-flutter-explore-traffic-trafficincidentbase-impact
→ /sdk-for-flutter-explore-traffic-trafficincidentimpact
</dt>
<dd>
  The impact of the incident.
The value is /sdk-for-flutter-explore-traffic-trafficincidentimpact if it hasn't been provided by the traffic incidents supplier.
Gets the impact of the incident.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-traffic-trafficincidentbase-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="startTime">
/sdk-for-flutter-explore-traffic-trafficincidentbase-starttime
→ DateTime?
</dt>
<dd>
  The time from which the incident is valid, before this time the incident should not be considered.
The value is <code>null</code> if it hasn't been provided by the traffic incidents supplier.
Gets the time from which the incident is valid, before this time the incident should not be considered.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="type">
/sdk-for-flutter-explore-traffic-trafficincidentbase-type
→ /sdk-for-flutter-explore-traffic-trafficincidenttype
</dt>
<dd>
  The category of the incident.
The value is /sdk-for-flutter-explore-traffic-trafficincidenttype if it hasn't been provided by the traffic incidents supplier.
Gets the category of the incident.
  <div class="features">no setter</div>
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
<li>/sdk-for-flutter-explore-traffic-traffic-library</li>
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
</div></div>
</div>
`
}</HTMLBlock>
