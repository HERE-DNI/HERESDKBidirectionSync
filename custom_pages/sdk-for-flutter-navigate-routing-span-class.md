---
title: "Untitled"
slug: "sdk-for-flutter-navigate-routing-span-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- Span-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
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
<p>A span is a part of the /sdk-for-flutter-navigate-routing-section-class which is traversable or navigable.</p>
<p>Each span
usually has some geometry associated with it.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="Span">
/sdk-for-flutter-navigate-routing-span-span()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="baseDuration">
/sdk-for-flutter-navigate-routing-span-baseduration
→ Duration
</dt>
<dd>
  The time duration necessary to traverse the span, using the speed provided
in /sdk-for-flutter-navigate-routing-span-dynamicspeedinfo without taking into consideration
the delays caused by the traffic.
Gets the time duration necessary to traverse the span, using the speed provided
in /sdk-for-flutter-navigate-routing-span-dynamicspeedinfo without taking into consideration
the delays caused by the traffic.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="carAttributes">
/sdk-for-flutter-navigate-routing-span-carattributes
→ List&lt;<wbr/>/sdk-for-flutter-navigate-routing-accessattributes&gt;
</dt>
<dd>
  The list of car access attributes on the span.
The list of car access attributes on the span.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="consumptionInKilowattHours">
/sdk-for-flutter-navigate-routing-span-consumptioninkilowatthours
→ double?
</dt>
<dd>
  The power consumption in kilowatt per hour necessary to traverse the span.
Gets the power consumption in kilowatt per hour necessary to traverse the span.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="countryCode">
/sdk-for-flutter-navigate-routing-span-countrycode
→ String?
</dt>
<dd>
  The country code of the span. The value is <code>null</code> when no data is available.
Gets the country code of the span. The value is <code>null</code> when no data is available.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="duration">
/sdk-for-flutter-navigate-routing-span-duration
→ Duration
</dt>
<dd>
  The time duration necessary to traverse the span, using the speed provided
in /sdk-for-flutter-navigate-routing-span-dynamicspeedinfo. This duration takes also into
consideration the delays caused by the traffic.
Gets the time duration necessary to traverse the span, using the speed provided
in /sdk-for-flutter-navigate-routing-span-dynamicspeedinfo. This duration takes also into
consideration the delays caused by the traffic.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="dynamicSpeedInfo">
/sdk-for-flutter-navigate-routing-span-dynamicspeedinfo
→ /sdk-for-flutter-navigate-routing-dynamicspeedinfo-class?
</dt>
<dd>
  The dynamic speed information on the span.
The dynamic speed information on the span.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="functionalRoadClass">
/sdk-for-flutter-navigate-routing-span-functionalroadclass
→ /sdk-for-flutter-navigate-routing-functionalroadclass?
</dt>
<dd>
  The functional road class of the span.
Gets the functional road class of the span.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="geometry">
/sdk-for-flutter-navigate-routing-span-geometry
→ /sdk-for-flutter-navigate-core-geopolyline-class
</dt>
<dd>
  The /sdk-for-flutter-navigate-core-geopolyline-class object representing the polyline of this span.
Gets the /sdk-for-flutter-navigate-core-geopolyline-class object representing the polyline of this span.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-routing-span-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="lengthInMeters">
/sdk-for-flutter-navigate-routing-span-lengthinmeters
→ int
</dt>
<dd>
  The length of this span in meters.
Gets the length of this span in meters.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="noThroughRestrictionsIndexes">
/sdk-for-flutter-navigate-routing-span-nothroughrestrictionsindexes
→ List&lt;<wbr/>int&gt;
</dt>
<dd>
  The list of indexes to /sdk-for-flutter-navigate-routing-section-nothroughrestrictions the parent section owns.
In case the list is not empty, the user must judge all the indexed sdk routing noThroughRestriction's
carefully before proceeding.
Get the list of indexes to /sdk-for-flutter-navigate-routing-section-nothroughrestrictions the parent section owns.
In case the list is not empty, the user must judge all the indexed /sdk-for-flutter-navigate-routing-section-nothroughrestrictions's
carefully before proceeding.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="noticeIndexes">
/sdk-for-flutter-navigate-routing-span-noticeindexes
→ List&lt;<wbr/>int&gt;
</dt>
<dd>
  The list of indexes to /sdk-for-flutter-navigate-routing-section-sectionnotices the parent section owns.
In case the list is not empty, the user must judge all the indexed /sdk-for-flutter-navigate-routing-sectionnotice-classs
carefully before proceeding.
Gets the list of indexes to /sdk-for-flutter-navigate-routing-section-sectionnotices the parent section owns.
In case the list is not empty, the user must judge all the indexed /sdk-for-flutter-navigate-routing-sectionnotice-class's
carefully before proceeding.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="roadNumbers">
/sdk-for-flutter-navigate-routing-span-roadnumbers
→ /sdk-for-flutter-navigate-routing-localizedroadnumbers-class
</dt>
<dd>
  The road numbers on the span enriched with information specific to <em>route numbers</em>
of a road such as I-10, US-50, or A3, and cardinal direction, if available, and a road level classification (<code>RouteType</code>).
Gets the road numbers on the span enriched with information specific to <em>route numbers</em>
of a road such as I-10, US-50, or A3, and cardinal direction, if available, and a road level classification (<code>RouteType</code>).
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-routing-span-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="scooterAttributes">
/sdk-for-flutter-navigate-routing-span-scooterattributes
→ List&lt;<wbr/>/sdk-for-flutter-navigate-routing-accessattributes&gt;
</dt>
<dd>
  The list of scooter access attributes on the span.
The list of scooter access attributes on the span.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="sectionPolylineOffset">
/sdk-for-flutter-navigate-routing-span-sectionpolylineoffset
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
/sdk-for-flutter-navigate-routing-span-segmentreference
→ /sdk-for-flutter-navigate-routing-segmentreference-class
</dt>
<dd>
  The segment reference of this span.
Gets the segment reference of this span.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="speedLimitInMetersPerSecond">
/sdk-for-flutter-navigate-routing-span-speedlimitinmeterspersecond
→ double?
</dt>
<dd>
  The speed limit in meters per second on the span.
Gets the speed limit in meters per second on the span.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="stateCode">
/sdk-for-flutter-navigate-routing-span-statecode
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
/sdk-for-flutter-navigate-routing-span-streetattributes
→ List&lt;<wbr/>/sdk-for-flutter-navigate-routing-streetattributes&gt;
</dt>
<dd>
  The list of street attributes on the span.
The list of street attributes on the span.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="streetNames">
/sdk-for-flutter-navigate-routing-span-streetnames
→ /sdk-for-flutter-navigate-core-localizedtexts-class
</dt>
<dd>
  The street names on the span.
The street names on the span.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="trafficIncidentIndexes">
/sdk-for-flutter-navigate-routing-span-trafficincidentindexes
→ List&lt;<wbr/>int&gt;
</dt>
<dd>
  The indexes of traffic incidents from the field /sdk-for-flutter-navigate-routing-section-trafficincidents of the parent /sdk-for-flutter-navigate-routing-section-class.
Each matching incident takes at least a whole /sdk-for-flutter-navigate-routing-span-geometry.
The same incident can take other spans and an area out of the built route as well.
The indexes of traffic incidents from the field /sdk-for-flutter-navigate-routing-section-trafficincidents of the parent /sdk-for-flutter-navigate-routing-section-class.
Each matching incident takes at least a whole /sdk-for-flutter-navigate-routing-span-geometry.
The same incident can take other spans and an area out of the built route as well.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="truckAttributes">
/sdk-for-flutter-navigate-routing-span-truckattributes
→ List&lt;<wbr/>/sdk-for-flutter-navigate-routing-accessattributes&gt;
</dt>
<dd>
  The list of truck access attributes on the span.
The list of truck access attributes on the span.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="walkAttributes">
/sdk-for-flutter-navigate-routing-span-walkattributes
→ List&lt;<wbr/>/sdk-for-flutter-navigate-routing-walkattributes&gt;
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
/sdk-for-flutter-navigate-routing-span-getshieldtext(<wbr/>/sdk-for-flutter-navigate-routing-localizedroadnumber-class roadNumber)
    → String

</dt>
<dd>
  Converts full route number to the value to be displayed on the road shield.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-routing-span-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-routing-span-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-routing-span-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
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



</div>
`
}</HTMLBlock>
