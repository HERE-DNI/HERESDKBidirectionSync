---
title: "Constructors"
slug: "sdk-for-flutter-explore-routing-section-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- Section-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="routing/Section-class.html#constructors">Constructors</a></li>
<li><a href="routing/Section/Section.html">Section</a></li>
<li class="section-title">
<a href="routing/Section-class.html#instance-properties">Properties</a>
</li>
<li><a href="routing/Section/arrivalLocationTime.html">arrivalLocationTime</a></li>
<li><a href="routing/Section/arrivalPlace.html">arrivalPlace</a></li>
<li><a href="routing/Section/boundingBox.html">boundingBox</a></li>
<li><a href="routing/Section/consumptionInKilowattHours.html">consumptionInKilowattHours</a></li>
<li><a href="routing/Section/departureLocationTime.html">departureLocationTime</a></li>
<li><a href="routing/Section/departurePlace.html">departurePlace</a></li>
<li><a href="routing/Section/duration.html">duration</a></li>
<li><a href="routing/Section/geometry.html">geometry</a></li>
<li class="inherited"><a href="routing/Section/hashCode.html">hashCode</a></li>
<li><a href="routing/Section/indoorSectionDetails.html">indoorSectionDetails</a></li>
<li><a href="routing/Section/lengthInMeters.html">lengthInMeters</a></li>
<li><a href="routing/Section/maneuvers.html">maneuvers</a></li>
<li><a href="routing/Section/noThroughRestrictions.html">noThroughRestrictions</a></li>
<li><a href="routing/Section/passthroughWaypoints.html">passthroughWaypoints</a></li>
<li><a href="routing/Section/postActions.html">postActions</a></li>
<li><a href="routing/Section/preActions.html">preActions</a></li>
<li class="inherited"><a href="routing/Section/runtimeType.html">runtimeType</a></li>
<li><a href="routing/Section/sectionNotices.html">sectionNotices</a></li>
<li><a href="routing/Section/sectionTransportMode.html">sectionTransportMode</a></li>
<li><a href="routing/Section/spans.html">spans</a></li>
<li><a href="routing/Section/tolls.html">tolls</a></li>
<li><a href="routing/Section/trafficDelay.html">trafficDelay</a></li>
<li><a href="routing/Section/trafficIncidents.html">trafficIncidents</a></li>
<li><a href="routing/Section/transitDetails.html">transitDetails</a></li>
<li class="section-title inherited"><a href="routing/Section-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="routing/Section/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="routing/Section/toString.html">toString</a></li>
<li class="section-title inherited"><a href="routing/Section-class.html#operators">Operators</a></li>
<li class="inherited"><a href="routing/Section/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li class="self-crumb">Section class</li>
</ol>
<div class="self-name">Section</div>
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
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/Section-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>Section class abstract</h1></div>
<section class="desc markdown">
<p>A section is a part of the route between two stopovers.</p>
<p>A stopover is a location on the route where a stop is made.</p>
<p><strong>Note:</strong> A section contains a list of <a href="../routing/SectionNotice-class.html">/sdk-for-flutter-explore-routing-sectionnotice-class</a> objects that describe
<em>potential issues</em> after the route was calculated. If the list is non-empty, it
is recommended to evaluate possible violations against the requested route options
and reject the route if deemed necessary.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="Section">
<a href="../routing/Section/Section.html">/sdk-for-flutter-explore-routing-section-section</a>()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="arrivalLocationTime">
<a href="../routing/Section/arrivalLocationTime.html">/sdk-for-flutter-explore-routing-section-arrivallocationtime</a>
→ <a href="../core/LocationTime-class.html">/sdk-for-flutter-explore-core-locationtime-class</a>?
</dt>
<dd>
  The arrival location time of this section.
Gets the arrival location time of this section.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="arrivalPlace">
<a href="../routing/Section/arrivalPlace.html">/sdk-for-flutter-explore-routing-section-arrivalplace</a>
→ <a href="../routing/RoutePlace-class.html">/sdk-for-flutter-explore-routing-routeplace-class</a>
</dt>
<dd>
  The arrival place.
Describes the arrival place.
Gets the arrival place.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="boundingBox">
<a href="../routing/Section/boundingBox.html">/sdk-for-flutter-explore-routing-section-boundingbox</a>
→ <a href="../core/GeoBox-class.html">/sdk-for-flutter-explore-core-geobox-class</a>
</dt>
<dd>
  The closest rectangular area where this section fits in.
Gets the closest rectangular area where this section fits in.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="consumptionInKilowattHours">
<a href="../routing/Section/consumptionInKilowattHours.html">/sdk-for-flutter-explore-routing-section-consumptioninkilowatthours</a>
→ double?
</dt>
<dd>
  Estimated net energy consumption (in kWh) if the transportation mode used for this route
is an electric vehicle. Note that it can be negative due to energy recuperation.
Gets estimated net energy consumption (in kWh) if the transportation mode used for this route
is an electric vehicle. Note that it can be negative due to energy recuperation.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="departureLocationTime">
<a href="../routing/Section/departureLocationTime.html">/sdk-for-flutter-explore-routing-section-departurelocationtime</a>
→ <a href="../core/LocationTime-class.html">/sdk-for-flutter-explore-core-locationtime-class</a>?
</dt>
<dd>
  The departure location time of this section.
Gets the departure location time of this section.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="departurePlace">
<a href="../routing/Section/departurePlace.html">/sdk-for-flutter-explore-routing-section-departureplace</a>
→ <a href="../routing/RoutePlace-class.html">/sdk-for-flutter-explore-routing-routeplace-class</a>
</dt>
<dd>
  Describes the departure place.
Gets the departure place.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="duration">
<a href="../routing/Section/duration.html">/sdk-for-flutter-explore-routing-section-duration</a>
→ Duration
</dt>
<dd>
  The estimated time in seconds needed to travel along this section, including
real-time traffic delays if available.
Gets the estimated time in seconds needed to travel along this section, including
real-time traffic delays if available.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="geometry">
<a href="../routing/Section/geometry.html">/sdk-for-flutter-explore-routing-section-geometry</a>
→ <a href="../core/GeoPolyline-class.html">/sdk-for-flutter-explore-core-geopolyline-class</a>
</dt>
<dd>
  The <a href="../core/GeoPolyline-class.html">/sdk-for-flutter-explore-core-geopolyline-class</a> object representing the polyline of this section.
Gets the <a href="../core/GeoPolyline-class.html">/sdk-for-flutter-explore-core-geopolyline-class</a> object representing the polyline of this section.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="hashCode">
<a href="../routing/Section/hashCode.html">/sdk-for-flutter-explore-routing-section-hashcode</a>
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="indoorSectionDetails">
<a href="../routing/Section/indoorSectionDetails.html">/sdk-for-flutter-explore-routing-section-indoorsectiondetails</a>
→ <a href="../routing/IndoorSectionDetails-class.html">/sdk-for-flutter-explore-routing-indoorsectiondetails-class</a>?
</dt>
<dd>
  Indoor routing section information.
Gets indoor routing section details.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="lengthInMeters">
<a href="../routing/Section/lengthInMeters.html">/sdk-for-flutter-explore-routing-section-lengthinmeters</a>
→ int
</dt>
<dd>
  The length of this section in meters.
Gets the length of this section in meters.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="maneuvers">
<a href="../routing/Section/maneuvers.html">/sdk-for-flutter-explore-routing-section-maneuvers</a>
→ List&lt;<wbr/><a href="../routing/Maneuver-class.html">/sdk-for-flutter-explore-routing-maneuver-class</a>&gt;
</dt>
<dd>
  The maneuvers for this section.
Gets the maneuvers for this section.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="noThroughRestrictions">
<a href="../routing/Section/noThroughRestrictions.html">/sdk-for-flutter-explore-routing-section-nothroughrestrictions</a>
→ List&lt;<wbr/><a href="../routing/ViolatedRestriction-class.html">/sdk-for-flutter-explore-routing-violatedrestriction-class</a>&gt;
</dt>
<dd>
  The list of no through restriction
The no through restriction area is part of the road network that do not allow through traffic.
For example the <code>Resident only</code> sign indicates that vehicles are only allowed to enter this area if they are making a stop.
This area will be set only if <code>origin</code>, <code>destination</code> or <code>via</code> waypoint will be requested within the area.
list of no through restriction.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="passthroughWaypoints">
<a href="../routing/Section/passthroughWaypoints.html">/sdk-for-flutter-explore-routing-section-passthroughwaypoints</a>
→ List&lt;<wbr/><a href="../routing/PassThroughWaypoint-class.html">/sdk-for-flutter-explore-routing-passthroughwaypoint-class</a>&gt;
</dt>
<dd>
  The list of passthrough waypoints in this section.
Gets the list of passthrough waypoints in this section.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="postActions">
<a href="../routing/Section/postActions.html">/sdk-for-flutter-explore-routing-section-postactions</a>
→ List&lt;<wbr/><a href="../routing/PostAction-class.html">/sdk-for-flutter-explore-routing-postaction-class</a>&gt;
</dt>
<dd>
  The post actions that must be done after the arrival at the end of the section.
Gets the post actions that must be done after the arrival at the end of the section.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="preActions">
<a href="../routing/Section/preActions.html">/sdk-for-flutter-explore-routing-section-preactions</a>
→ List&lt;<wbr/><a href="../routing/PreAction-class.html">/sdk-for-flutter-explore-routing-preaction-class</a>&gt;
</dt>
<dd>
  The preceding actions that must be done prior to departure at the beginning of the section.
Gets the preceding actions that must be done prior to departure at the beginning of the section.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../routing/Section/runtimeType.html">/sdk-for-flutter-explore-routing-section-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="sectionNotices">
<a href="../routing/Section/sectionNotices.html">/sdk-for-flutter-explore-routing-section-sectionnotices</a>
→ List&lt;<wbr/><a href="../routing/SectionNotice-class.html">/sdk-for-flutter-explore-routing-sectionnotice-class</a>&gt;
</dt>
<dd>
  The notices which explain the issues encountered during processing of this section.
For example, while the scooter transport mode is selected, if no reasonable alternative route is
possible except violating controlled-access to highway rule for the section, one notice is generated
for the violation. The user must judge all the notices carefully before proceeding.
Gets the notices which explains the issues encountered during processing of this section.
For example, while the scooter transport mode is selected, if no reasonable alternative route is
possible except violating controlled-access to highway rule for the section, one notice is generated
for the violation. The user must judge all the notices carefully before proceeding.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="sectionTransportMode">
<a href="../routing/Section/sectionTransportMode.html">/sdk-for-flutter-explore-routing-section-sectiontransportmode</a>
→ <a href="../routing/SectionTransportMode.html">/sdk-for-flutter-explore-routing-sectiontransportmode</a>
</dt>
<dd>
  The transport mode of this section.
Gets the transport mode of this section.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="spans">
<a href="../routing/Section/spans.html">/sdk-for-flutter-explore-routing-section-spans</a>
→ List&lt;<wbr/><a href="../routing/Span-class.html">/sdk-for-flutter-explore-routing-span-class</a>&gt;
</dt>
<dd>
  The <a href="../routing/Span-class.html">/sdk-for-flutter-explore-routing-span-class</a>'s that constitute this section.
Gets the <a href="../routing/Span-class.html">/sdk-for-flutter-explore-routing-span-class</a>'s that constitute this section.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="tolls">
<a href="../routing/Section/tolls.html">/sdk-for-flutter-explore-routing-section-tolls</a>
→ List&lt;<wbr/><a href="../routing/Toll-class.html">/sdk-for-flutter-explore-routing-toll-class</a>&gt;
</dt>
<dd>
  All the tolls for this section.
Note that tolls are found depending on the transport mode.
For example, if pedestrian or bicycle transport mode specified, route sections have no tolls. Indoor
route sections have no tolls, too.
<strong>Note</strong>: If you're using the <code>OfflineRoutingEngine</code>, be aware that this feature is
currently in <strong>beta</strong>. As a result, there may be some bugs or unexpected behaviors.
Additionally, this feature and related APIs may be updated in future releases
without going through the deprecation process. Note that the <code>OfflineRoutingEngine</code>
is only available with the Navigate license. If you're using the
<code>RoutingEngine</code>, this feature is considered to be stable.
Gets all the tolls for this section. Note that tolls are found depending on the
transport mode. For example, if pedestrian or bicycle transport mode specified, route sections have no tolls.
Indoor route sections have no tolls, too.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="trafficDelay">
<a href="../routing/Section/trafficDelay.html">/sdk-for-flutter-explore-routing-section-trafficdelay</a>
→ Duration
</dt>
<dd>
  The estimated extra time in seconds spent due to traffic delays along this section. Negative values
indicate that the route can be traversed faster than usual.
Gets the estimated extra time in seconds spent due to traffic delays along this section.
Negative values indicate that the route can be traversed faster than usual.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="trafficIncidents">
<a href="../routing/Section/trafficIncidents.html">/sdk-for-flutter-explore-routing-section-trafficincidents</a>
→ List&lt;<wbr/><a href="../routing/TrafficIncidentOnRoute-class.html">/sdk-for-flutter-explore-routing-trafficincidentonroute-class</a>&gt;
</dt>
<dd>
  The list of traffic incidents that are found on the section.
the list of traffic incidents that are found on the section.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="transitDetails">
<a href="../routing/Section/transitDetails.html">/sdk-for-flutter-explore-routing-section-transitdetails</a>
→ <a href="../routing/TransitSectionDetails-class.html">/sdk-for-flutter-explore-routing-transitsectiondetails-class</a>?
</dt>
<dd>
  The transit details which are avilable for transit sections of a route.
Gets the details of a transit section.
  <div class="features">no setter</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
<a href="../routing/Section/noSuchMethod.html">/sdk-for-flutter-explore-routing-section-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../routing/Section/toString.html">/sdk-for-flutter-explore-routing-section-tostring</a>(<wbr/>)
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
<a href="../routing/Section/operator_equals.html">/sdk-for-flutter-explore-routing-section-operator-equals</a>(<wbr/>Object other)
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
<li class="self-crumb">Section class</li>
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
