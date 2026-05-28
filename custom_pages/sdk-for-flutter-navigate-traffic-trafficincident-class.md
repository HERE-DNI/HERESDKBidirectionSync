---
title: "TrafficIncident class abstract"
slug: "sdk-for-flutter-navigate-traffic-trafficincident-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TrafficIncident-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="traffic/TrafficIncident-class.html#constructors">Constructors</a></li>
<li><a href="traffic/TrafficIncident/TrafficIncident.html">TrafficIncident</a></li>
<li class="section-title">
<a href="traffic/TrafficIncident-class.html#instance-properties">Properties</a>
</li>
<li><a href="traffic/TrafficIncident/codes.html">codes</a></li>
<li class="inherited"><a href="traffic/TrafficIncidentBase/description.html">description</a></li>
<li class="inherited"><a href="traffic/TrafficIncidentBase/endTime.html">endTime</a></li>
<li><a href="traffic/TrafficIncident/entryTime.html">entryTime</a></li>
<li class="inherited"><a href="traffic/TrafficIncidentBase/hashCode.html">hashCode</a></li>
<li><a href="traffic/TrafficIncident/id.html">id</a></li>
<li class="inherited"><a href="traffic/TrafficIncidentBase/impact.html">impact</a></li>
<li><a href="traffic/TrafficIncident/isRoadClosed.html">isRoadClosed</a></li>
<li><a href="traffic/TrafficIncident/junctionsTraversability.html">junctionsTraversability</a></li>
<li><a href="traffic/TrafficIncident/location.html">location</a></li>
<li><a href="traffic/TrafficIncident/originalId.html">originalId</a></li>
<li><a href="traffic/TrafficIncident/parentId.html">parentId</a></li>
<li class="inherited"><a href="traffic/TrafficIncidentBase/runtimeType.html">runtimeType</a></li>
<li class="inherited"><a href="traffic/TrafficIncidentBase/startTime.html">startTime</a></li>
<li><a href="traffic/TrafficIncident/summary.html">summary</a></li>
<li class="inherited"><a href="traffic/TrafficIncidentBase/type.html">type</a></li>
<li><a href="traffic/TrafficIncident/vehicleRestrictions.html">vehicleRestrictions</a></li>
<li class="section-title inherited"><a href="traffic/TrafficIncident-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="traffic/TrafficIncidentBase/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="traffic/TrafficIncidentBase/toString.html">toString</a></li>
<li class="section-title inherited"><a href="traffic/TrafficIncident-class.html#operators">Operators</a></li>
<li class="inherited"><a href="traffic/TrafficIncidentBase/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-traffic-traffic-library</li>
<li class="self-crumb">TrafficIncident class</li>
</ol>
<div class="self-name">TrafficIncident</div>
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
<div class="main-content" data-above-sidebar="traffic/traffic-library-sidebar.html" data-below-sidebar="traffic/TrafficIncident-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>TrafficIncident class abstract</h1></div>
<section class="desc markdown">
<p>TrafficIncident provides details about a traffic incident.</p>
</section>
<section>
<dl class="dl-horizontal">
<dt>Implemented types</dt>
<dd>
<ul class="comma-separated clazz-relationships">
<li>/sdk-for-flutter-navigate-traffic-trafficincidentbase-class</li>
</ul>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="TrafficIncident">
/sdk-for-flutter-navigate-traffic-trafficincident-trafficincident()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="codes">
/sdk-for-flutter-navigate-traffic-trafficincident-codes
→ List&lt;<wbr/>int&gt;
</dt>
<dd>
  The list of standardized codes as categorized in ISO 14819-2:2013 standard for this incident category.
Codes are given in order of importance, so the first item in the list is considered the primary cause of the incident.
Gets the list of standardized codes as categorized in ISO 14819-2:2013 standard for this incident category.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="description">
/sdk-for-flutter-navigate-traffic-trafficincidentbase-description
→ /sdk-for-flutter-navigate-core-localizedtext-class
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
/sdk-for-flutter-navigate-traffic-trafficincidentbase-endtime
→ DateTime?
</dt>
<dd class="inherited">
  The time until which the incident is valid, after this time the incident should not be considered.
The value is <code>null</code> if it hasn't been provided by the traffic incidents supplier.
Get the time until which the incident is valid, after this time the incident should not be considered.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="entryTime">
/sdk-for-flutter-navigate-traffic-trafficincident-entrytime
→ DateTime?
</dt>
<dd>
  The time the incident was entered into the system.
The value is <code>null</code> if it hasn't been provided by the traffic incidents supplier.
Gets the time the incident was entered into the system.
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
<dt class="property" id="id">
/sdk-for-flutter-navigate-traffic-trafficincident-id
→ String
</dt>
<dd>
  The unique current identifier for a traffic incident.
Gets the unique current identifier for a traffic incident.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="impact">
/sdk-for-flutter-navigate-traffic-trafficincidentbase-impact
→ /sdk-for-flutter-navigate-traffic-trafficincidentimpact
</dt>
<dd class="inherited">
  The impact of the incident.
The value is /sdk-for-flutter-navigate-traffic-trafficincidentimpact if it hasn't been provided by the traffic incidents supplier.
Gets the impact of the incident.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="isRoadClosed">
/sdk-for-flutter-navigate-traffic-trafficincident-isroadclosed
→ bool
</dt>
<dd>
  The flag indicates whether road is closed or not.
Gets the flag indicating whether road is closed or not.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="junctionsTraversability">
/sdk-for-flutter-navigate-traffic-trafficincident-junctionstraversability
→ /sdk-for-flutter-navigate-traffic-junctionstraversability
</dt>
<dd>
  The traversability of junctions along the affected road.
Gets the traversability of junctions along the affected road.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="location">
/sdk-for-flutter-navigate-traffic-trafficincident-location
→ /sdk-for-flutter-navigate-traffic-trafficlocation-class
</dt>
<dd>
  The location of the incident.
Gets the location of the incident.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="originalId">
/sdk-for-flutter-navigate-traffic-trafficincident-originalid
→ String
</dt>
<dd>
  The unique identifier of the first traffic incident.
The original id remains the same whenever the traffic incident is updated and /sdk-for-flutter-navigate-traffic-trafficincident-id is changed.
Once an incident chain has been created, this value will never change.
The traffic incident an be looked up by original id using /sdk-for-flutter-navigate-traffic-trafficengine-lookupincident.
Gets the unique identifier of the first traffic incident.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="parentId">
/sdk-for-flutter-navigate-traffic-trafficincident-parentid
→ String?
</dt>
<dd>
  The identifier of another incident to which this incident is linked.
The value is <code>null</code> if the incident doesn't have a parent.
Gets the identifier of another incident to which this incident is linked.
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
<dt class="property inherited" id="startTime">
/sdk-for-flutter-navigate-traffic-trafficincidentbase-starttime
→ DateTime?
</dt>
<dd class="inherited">
  The time from which the incident is valid, before this time the incident should not be considered.
The value is <code>null</code> if it hasn't been provided by the traffic incidents supplier.
Gets the time from which the incident is valid, before this time the incident should not be considered.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="summary">
/sdk-for-flutter-navigate-traffic-trafficincident-summary
→ /sdk-for-flutter-navigate-core-localizedtext-class
</dt>
<dd>
  The human readable summary of the incident.
The summary field provides a short version of the description containing no location information.
The expected summary language can be managed
via /sdk-for-flutter-navigate-traffic-trafficincidentsqueryoptions-languagecode and /sdk-for-flutter-navigate-traffic-trafficincidentlookupoptions-languagecode.
Gets the human readable summary of the incident.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="type">
/sdk-for-flutter-navigate-traffic-trafficincidentbase-type
→ /sdk-for-flutter-navigate-traffic-trafficincidenttype
</dt>
<dd class="inherited">
  The category of the incident.
The value is /sdk-for-flutter-navigate-traffic-trafficincidenttype if it hasn't been provided by the traffic incidents supplier.
Gets the category of the incident.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="vehicleRestrictions">
/sdk-for-flutter-navigate-traffic-trafficincident-vehiclerestrictions
→ Map&lt;<wbr/>/sdk-for-flutter-navigate-traffic-trafficincidentrestrictedvehiclecategory, /sdk-for-flutter-navigate-traffic-trafficincidentvehiclerestriction-class&gt;
</dt>
<dd>
  The map of restricted vehicle categories to restrictions.
A vehicle is restricted if at least one restriction field is applicable for it.
If the map is empty, there're no restricted vehicles for the incident.
Gets the map of restricted vehicle categories to restrictions.
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
<li class="self-crumb">TrafficIncident class</li>
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
