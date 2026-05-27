---
title: "Constructors"
slug: "sdk-for-flutter-explore-routing-span-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- Span-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="routing/Span-class.html#constructors">Constructors</a></li>
<li><a href="routing/Span/Span.html">Span</a></li>
<li class="section-title">
<a href="routing/Span-class.html#instance-properties">Properties</a>
</li>
<li><a href="routing/Span/baseDuration.html">baseDuration</a></li>
<li><a href="routing/Span/carAttributes.html">carAttributes</a></li>
<li><a href="routing/Span/consumptionInKilowattHours.html">consumptionInKilowattHours</a></li>
<li><a href="routing/Span/countryCode.html">countryCode</a></li>
<li><a href="routing/Span/duration.html">duration</a></li>
<li><a href="routing/Span/dynamicSpeedInfo.html">dynamicSpeedInfo</a></li>
<li><a href="routing/Span/functionalRoadClass.html">functionalRoadClass</a></li>
<li><a href="routing/Span/geometry.html">geometry</a></li>
<li class="inherited"><a href="routing/Span/hashCode.html">hashCode</a></li>
<li><a href="routing/Span/lengthInMeters.html">lengthInMeters</a></li>
<li><a href="routing/Span/noThroughRestrictionsIndexes.html">noThroughRestrictionsIndexes</a></li>
<li><a href="routing/Span/noticeIndexes.html">noticeIndexes</a></li>
<li><a href="routing/Span/roadNumbers.html">roadNumbers</a></li>
<li class="inherited"><a href="routing/Span/runtimeType.html">runtimeType</a></li>
<li><a href="routing/Span/scooterAttributes.html">scooterAttributes</a></li>
<li><a href="routing/Span/sectionPolylineOffset.html">sectionPolylineOffset</a></li>
<li><a href="routing/Span/segmentReference.html">segmentReference</a></li>
<li><a href="routing/Span/speedLimitInMetersPerSecond.html">speedLimitInMetersPerSecond</a></li>
<li><a href="routing/Span/stateCode.html">stateCode</a></li>
<li><a href="routing/Span/streetAttributes.html">streetAttributes</a></li>
<li><a href="routing/Span/streetNames.html">streetNames</a></li>
<li><a href="routing/Span/trafficIncidentIndexes.html">trafficIncidentIndexes</a></li>
<li><a href="routing/Span/truckAttributes.html">truckAttributes</a></li>
<li><a href="routing/Span/walkAttributes.html">walkAttributes</a></li>
<li class="section-title"><a href="routing/Span-class.html#instance-methods">Methods</a></li>
<li><a href="routing/Span/getShieldText.html">getShieldText</a></li>
<li class="inherited"><a href="routing/Span/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="routing/Span/toString.html">toString</a></li>
<li class="section-title inherited"><a href="routing/Span-class.html#operators">Operators</a></li>
<li class="inherited"><a href="routing/Span/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li class="self-crumb">Span class</li>
</ol>
<div class="self-name">Span</div>
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
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/Span-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>Span class abstract</h1></div>
<section class="desc markdown">
<p>A span is a part of the <a href="../routing/Section-class.html">/sdk-for-flutter-explore-routing-section-class</a> which is traversable or navigable.</p>
<p>Each span
usually has some geometry associated with it.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="Span">
<a href="../routing/Span/Span.html">/sdk-for-flutter-explore-routing-span-span</a>()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="baseDuration">
<a href="../routing/Span/baseDuration.html">/sdk-for-flutter-explore-routing-span-baseduration</a>
→ Duration
</dt>
<dd>
  The time duration necessary to traverse the span, using the speed provided
in <a href="../routing/Span/dynamicSpeedInfo.html">/sdk-for-flutter-explore-routing-span-dynamicspeedinfo</a> without taking into consideration
the delays caused by the traffic.
Gets the time duration necessary to traverse the span, using the speed provided
in <a href="../routing/Span/dynamicSpeedInfo.html">/sdk-for-flutter-explore-routing-span-dynamicspeedinfo</a> without taking into consideration
the delays caused by the traffic.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="carAttributes">
<a href="../routing/Span/carAttributes.html">/sdk-for-flutter-explore-routing-span-carattributes</a>
→ List&lt;<wbr/><a href="../routing/AccessAttributes.html">/sdk-for-flutter-explore-routing-accessattributes</a>&gt;
</dt>
<dd>
  The list of car access attributes on the span.
The list of car access attributes on the span.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="consumptionInKilowattHours">
<a href="../routing/Span/consumptionInKilowattHours.html">/sdk-for-flutter-explore-routing-span-consumptioninkilowatthours</a>
→ double?
</dt>
<dd>
  The power consumption in kilowatt per hour necessary to traverse the span.
Gets the power consumption in kilowatt per hour necessary to traverse the span.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="countryCode">
<a href="../routing/Span/countryCode.html">/sdk-for-flutter-explore-routing-span-countrycode</a>
→ String?
</dt>
<dd>
  The country code of the span. The value is <code>null</code> when no data is available.
Gets the country code of the span. The value is <code>null</code> when no data is available.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="duration">
<a href="../routing/Span/duration.html">/sdk-for-flutter-explore-routing-span-duration</a>
→ Duration
</dt>
<dd>
  The time duration necessary to traverse the span, using the speed provided
in <a href="../routing/Span/dynamicSpeedInfo.html">/sdk-for-flutter-explore-routing-span-dynamicspeedinfo</a>. This duration takes also into
consideration the delays caused by the traffic.
Gets the time duration necessary to traverse the span, using the speed provided
in <a href="../routing/Span/dynamicSpeedInfo.html">/sdk-for-flutter-explore-routing-span-dynamicspeedinfo</a>. This duration takes also into
consideration the delays caused by the traffic.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="dynamicSpeedInfo">
<a href="../routing/Span/dynamicSpeedInfo.html">/sdk-for-flutter-explore-routing-span-dynamicspeedinfo</a>
→ <a href="../routing/DynamicSpeedInfo-class.html">/sdk-for-flutter-explore-routing-dynamicspeedinfo-class</a>?
</dt>
<dd>
  The dynamic speed information on the span.
The dynamic speed information on the span.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="functionalRoadClass">
<a href="../routing/Span/functionalRoadClass.html">/sdk-for-flutter-explore-routing-span-functionalroadclass</a>
→ <a href="../routing/FunctionalRoadClass.html">/sdk-for-flutter-explore-routing-functionalroadclass</a>?
</dt>
<dd>
  The functional road class of the span.
Gets the functional road class of the span.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="geometry">
<a href="../routing/Span/geometry.html">/sdk-for-flutter-explore-routing-span-geometry</a>
→ <a href="../core/GeoPolyline-class.html">/sdk-for-flutter-explore-core-geopolyline-class</a>
</dt>
<dd>
  The <a href="../core/GeoPolyline-class.html">/sdk-for-flutter-explore-core-geopolyline-class</a> object representing the polyline of this span.
Gets the <a href="../core/GeoPolyline-class.html">/sdk-for-flutter-explore-core-geopolyline-class</a> object representing the polyline of this span.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="hashCode">
<a href="../routing/Span/hashCode.html">/sdk-for-flutter-explore-routing-span-hashcode</a>
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="lengthInMeters">
<a href="../routing/Span/lengthInMeters.html">/sdk-for-flutter-explore-routing-span-lengthinmeters</a>
→ int
</dt>
<dd>
  The length of this span in meters.
Gets the length of this span in meters.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="noThroughRestrictionsIndexes">
<a href="../routing/Span/noThroughRestrictionsIndexes.html">/sdk-for-flutter-explore-routing-span-nothroughrestrictionsindexes</a>
→ List&lt;<wbr/>int&gt;
</dt>
<dd>
  The list of indexes to <a href="../routing/Section/noThroughRestrictions.html">/sdk-for-flutter-explore-routing-section-nothroughrestrictions</a> the parent section owns.
In case the list is not empty, the user must judge all the indexed sdk routing noThroughRestriction's
carefully before proceeding.
Get the list of indexes to <a href="../routing/Section/noThroughRestrictions.html">/sdk-for-flutter-explore-routing-section-nothroughrestrictions</a> the parent section owns.
In case the list is not empty, the user must judge all the indexed <a href="../routing/Section/noThroughRestrictions.html">/sdk-for-flutter-explore-routing-section-nothroughrestrictions</a>'s
carefully before proceeding.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="noticeIndexes">
<a href="../routing/Span/noticeIndexes.html">/sdk-for-flutter-explore-routing-span-noticeindexes</a>
→ List&lt;<wbr/>int&gt;
</dt>
<dd>
  The list of indexes to <a href="../routing/Section/sectionNotices.html">/sdk-for-flutter-explore-routing-section-sectionnotices</a> the parent section owns.
In case the list is not empty, the user must judge all the indexed <a href="../routing/SectionNotice-class.html">/sdk-for-flutter-explore-routing-sectionnotice-class</a>s
carefully before proceeding.
Gets the list of indexes to <a href="../routing/Section/sectionNotices.html">/sdk-for-flutter-explore-routing-section-sectionnotices</a> the parent section owns.
In case the list is not empty, the user must judge all the indexed <a href="../routing/SectionNotice-class.html">/sdk-for-flutter-explore-routing-sectionnotice-class</a>'s
carefully before proceeding.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="roadNumbers">
<a href="../routing/Span/roadNumbers.html">/sdk-for-flutter-explore-routing-span-roadnumbers</a>
→ <a href="../routing/LocalizedRoadNumbers-class.html">/sdk-for-flutter-explore-routing-localizedroadnumbers-class</a>
</dt>
<dd>
  The road numbers on the span enriched with information specific to <em>route numbers</em>
of a road such as I-10, US-50, or A3, and cardinal direction, if available, and a road level classification (<code>RouteType</code>).
Gets the road numbers on the span enriched with information specific to <em>route numbers</em>
of a road such as I-10, US-50, or A3, and cardinal direction, if available, and a road level classification (<code>RouteType</code>).
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../routing/Span/runtimeType.html">/sdk-for-flutter-explore-routing-span-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="scooterAttributes">
<a href="../routing/Span/scooterAttributes.html">/sdk-for-flutter-explore-routing-span-scooterattributes</a>
→ List&lt;<wbr/><a href="../routing/AccessAttributes.html">/sdk-for-flutter-explore-routing-accessattributes</a>&gt;
</dt>
<dd>
  The list of scooter access attributes on the span.
The list of scooter access attributes on the span.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="sectionPolylineOffset">
<a href="../routing/Span/sectionPolylineOffset.html">/sdk-for-flutter-explore-routing-span-sectionpolylineoffset</a>
→ int
</dt>
<dd>
  The position of the span inside the section's geometry, given as an offset. The span geometry starts from
this offset and ends on the offset of the next span, both start offset point and end offset point being
included in the span, because the spans' geometry share a point in the section's geometry.
Gets the position of the span inside the section's geometry, given as an offset. The span geometry starts from
this offset and ends on the offset of the next span, both start offset point and end offset point being
included in the span, because the spans' geometry share a point in the section's geometry.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="segmentReference">
<a href="../routing/Span/segmentReference.html">/sdk-for-flutter-explore-routing-span-segmentreference</a>
→ <a href="../routing/SegmentReference-class.html">/sdk-for-flutter-explore-routing-segmentreference-class</a>
</dt>
<dd>
  The segment reference of this span.
Gets the segment reference of this span.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="speedLimitInMetersPerSecond">
<a href="../routing/Span/speedLimitInMetersPerSecond.html">/sdk-for-flutter-explore-routing-span-speedlimitinmeterspersecond</a>
→ double?
</dt>
<dd>
  The speed limit in meters per second on the span.
Gets the speed limit in meters per second on the span.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="stateCode">
<a href="../routing/Span/stateCode.html">/sdk-for-flutter-explore-routing-span-statecode</a>
→ String?
</dt>
<dd>
  The state code of the span. State code is available in some countries to denote principal
subdivisions(provinces or states), e.g. in the United States, AK stands for Alaska and OH stands for Ohio.
The format of state code can vary for different countries, take the United States as example,
it consists of two alphabet letters.
The value is <code>null</code> when no data is available.
Gets the state code of the span. State code is available in some countries to denote principal
subdivisions(provinces or states), e.g. in the United States, AK stands for Alaska and OH stands for Ohio.
The format of state code can vary for different countries, take the United States as example,
it consists of two alphabet letters. The value is <code>null</code> when no data is available.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="streetAttributes">
<a href="../routing/Span/streetAttributes.html">/sdk-for-flutter-explore-routing-span-streetattributes</a>
→ List&lt;<wbr/><a href="../routing/StreetAttributes.html">/sdk-for-flutter-explore-routing-streetattributes</a>&gt;
</dt>
<dd>
  The list of street attributes on the span.
The list of street attributes on the span.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="streetNames">
<a href="../routing/Span/streetNames.html">/sdk-for-flutter-explore-routing-span-streetnames</a>
→ <a href="../core/LocalizedTexts-class.html">/sdk-for-flutter-explore-core-localizedtexts-class</a>
</dt>
<dd>
  The street names on the span.
The street names on the span.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="trafficIncidentIndexes">
<a href="../routing/Span/trafficIncidentIndexes.html">/sdk-for-flutter-explore-routing-span-trafficincidentindexes</a>
→ List&lt;<wbr/>int&gt;
</dt>
<dd>
  The indexes of traffic incidents from the field <a href="../routing/Section/trafficIncidents.html">/sdk-for-flutter-explore-routing-section-trafficincidents</a> of the parent <a href="../routing/Section-class.html">/sdk-for-flutter-explore-routing-section-class</a>.
Each matching incident takes at least a whole <a href="../routing/Span/geometry.html">/sdk-for-flutter-explore-routing-span-geometry</a>.
The same incident can take other spans and an area out of the built route as well.
The indexes of traffic incidents from the field <a href="../routing/Section/trafficIncidents.html">/sdk-for-flutter-explore-routing-section-trafficincidents</a> of the parent <a href="../routing/Section-class.html">/sdk-for-flutter-explore-routing-section-class</a>.
Each matching incident takes at least a whole <a href="../routing/Span/geometry.html">/sdk-for-flutter-explore-routing-span-geometry</a>.
The same incident can take other spans and an area out of the built route as well.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="truckAttributes">
<a href="../routing/Span/truckAttributes.html">/sdk-for-flutter-explore-routing-span-truckattributes</a>
→ List&lt;<wbr/><a href="../routing/AccessAttributes.html">/sdk-for-flutter-explore-routing-accessattributes</a>&gt;
</dt>
<dd>
  The list of truck access attributes on the span.
The list of truck access attributes on the span.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="walkAttributes">
<a href="../routing/Span/walkAttributes.html">/sdk-for-flutter-explore-routing-span-walkattributes</a>
→ List&lt;<wbr/><a href="../routing/WalkAttributes.html">/sdk-for-flutter-explore-routing-walkattributes</a>&gt;
</dt>
<dd>
  The list of walk attributes on the span.
The list of walk attributes on the span.
  <div class="features">no setter</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="getShieldText">
<a href="../routing/Span/getShieldText.html">/sdk-for-flutter-explore-routing-span-getshieldtext</a>(<wbr/><a href="../routing/LocalizedRoadNumber-class.html">/sdk-for-flutter-explore-routing-localizedroadnumber-class</a> roadNumber)
    → String

</dt>
<dd>
  Converts full route number to the value to be displayed on the road shield.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
<a href="../routing/Span/noSuchMethod.html">/sdk-for-flutter-explore-routing-span-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../routing/Span/toString.html">/sdk-for-flutter-explore-routing-span-tostring</a>(<wbr/>)
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
<a href="../routing/Span/operator_equals.html">/sdk-for-flutter-explore-routing-span-operator-equals</a>(<wbr/>Object other)
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
<li class="self-crumb">Span class</li>
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
