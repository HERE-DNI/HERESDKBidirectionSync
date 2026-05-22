---
title: "Untitled"
slug: "sdk-for-flutter-explore-traffic-trafficincident-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TrafficIncident-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-traffic-traffic-library</li>
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
<li>/sdk-for-flutter-explore-traffic-trafficincidentbase-class</li>
</ul>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="TrafficIncident">
/sdk-for-flutter-explore-traffic-trafficincident-trafficincident()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="codes">
/sdk-for-flutter-explore-traffic-trafficincident-codes
→ List&lt;<wbr/>int&gt;
</dt>
<dd>
  The list of standardized codes as categorized in ISO 14819-2:2013 standard for this incident category.
Codes are given in order of importance, so the first item in the list is considered the primary cause of the incident.
Gets the list of standardized codes as categorized in ISO 14819-2:2013 standard for this incident category.
  <div class="features">no setter</div>
</dd>
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
<dt class="property" id="entryTime">
/sdk-for-flutter-explore-traffic-trafficincident-entrytime
→ DateTime?
</dt>
<dd>
  The time the incident was entered into the system.
The value is <code>null</code> if it hasn't been provided by the traffic incidents supplier.
Gets the time the incident was entered into the system.
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
<dt class="property" id="id">
/sdk-for-flutter-explore-traffic-trafficincident-id
→ String
</dt>
<dd>
  The unique current identifier for a traffic incident.
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
<dt class="property" id="isRoadClosed">
/sdk-for-flutter-explore-traffic-trafficincident-isroadclosed
→ bool
</dt>
<dd>
  The flag indicates whether road is closed or not.
Gets the flag indicating whether road is closed or not.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="junctionsTraversability">
/sdk-for-flutter-explore-traffic-trafficincident-junctionstraversability
→ /sdk-for-flutter-explore-traffic-junctionstraversability
</dt>
<dd>
  The traversability of junctions along the affected road.
Gets the traversability of junctions along the affected road.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="location">
/sdk-for-flutter-explore-traffic-trafficincident-location
→ /sdk-for-flutter-explore-traffic-trafficlocation-class
</dt>
<dd>
  The location of the incident.
Gets the location of the incident.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="originalId">
/sdk-for-flutter-explore-traffic-trafficincident-originalid
→ String
</dt>
<dd>
  The unique identifier of the first traffic incident.
The original id remains the same whenever the traffic incident is updated and /sdk-for-flutter-explore-traffic-trafficincident-id is changed.
Once an incident chain has been created, this value will never change.
The traffic incident an be looked up by original id using /sdk-for-flutter-explore-traffic-trafficengine-lookupincident.
Gets the unique identifier of the first traffic incident.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="parentId">
/sdk-for-flutter-explore-traffic-trafficincident-parentid
→ String?
</dt>
<dd>
  The identifier of another incident to which this incident is linked.
The value is <code>null</code> if the incident doesn't have a parent.
Gets the identifier of another incident to which this incident is linked.
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
<dt class="property" id="summary">
/sdk-for-flutter-explore-traffic-trafficincident-summary
→ /sdk-for-flutter-explore-core-localizedtext-class
</dt>
<dd>
  The human readable summary of the incident.
The summary field provides a short version of the description containing no location information.
The expected summary language can be managed
via /sdk-for-flutter-explore-traffic-trafficincidentsqueryoptions-languagecode and /sdk-for-flutter-explore-traffic-trafficincidentlookupoptions-languagecode.
Gets the human readable summary of the incident.
  <div class="features">no setter</div>
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
<dt class="property" id="vehicleRestrictions">
/sdk-for-flutter-explore-traffic-trafficincident-vehiclerestrictions
→ Map&lt;<wbr/>/sdk-for-flutter-explore-traffic-trafficincidentrestrictedvehiclecategory, /sdk-for-flutter-explore-traffic-trafficincidentvehiclerestriction-class&gt;
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



</div>
`
}</HTMLBlock>
