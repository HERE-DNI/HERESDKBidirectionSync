---
title: "Span class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-span-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- Span-class.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/Span-class-sidebar.html">

<div>

# <span class="kind-class">Span</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

A span is a part of the <a href="sdk-for-flutter-explore-routing-section-class">Section</a> which is traversable or navigable.

Each span usually has some geometry associated with it.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-routing-span-span">Span</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-explore-routing-span-baseduration">baseDuration</a></span> <span class="signature">→ Duration</span>  
The time duration necessary to traverse the span, using the speed provided in <a href="sdk-for-flutter-explore-routing-span-dynamicspeedinfo">Span.dynamicSpeedInfo</a> without taking into consideration the delays caused by the traffic. Gets the time duration necessary to traverse the span, using the speed provided in <a href="sdk-for-flutter-explore-routing-span-dynamicspeedinfo">Span.dynamicSpeedInfo</a> without taking into consideration the delays caused by the traffic.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-span-carattributes">carAttributes</a></span> <span class="signature">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-routing-accessattributes">AccessAttributes</a></span>\></span></span>  
The list of car access attributes on the span. The list of car access attributes on the span.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-span-consumptioninkilowatthours">consumptionInKilowattHours</a></span> <span class="signature">→ double?</span>  
The power consumption in kilowatt per hour necessary to traverse the span. Gets the power consumption in kilowatt per hour necessary to traverse the span.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-span-countrycode">countryCode</a></span> <span class="signature">→ String?</span>  
The country code of the span. The value is `null` when no data is available. Gets the country code of the span. The value is `null` when no data is available.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-span-duration">duration</a></span> <span class="signature">→ Duration</span>  
The time duration necessary to traverse the span, using the speed provided in <a href="sdk-for-flutter-explore-routing-span-dynamicspeedinfo">Span.dynamicSpeedInfo</a>. This duration takes also into consideration the delays caused by the traffic. Gets the time duration necessary to traverse the span, using the speed provided in <a href="sdk-for-flutter-explore-routing-span-dynamicspeedinfo">Span.dynamicSpeedInfo</a>. This duration takes also into consideration the delays caused by the traffic.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-span-dynamicspeedinfo">dynamicSpeedInfo</a></span> <span class="signature">→ <a href="sdk-for-flutter-explore-routing-dynamicspeedinfo-class">DynamicSpeedInfo</a>?</span>  
The dynamic speed information on the span. The dynamic speed information on the span.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-span-functionalroadclass">functionalRoadClass</a></span> <span class="signature">→ <a href="sdk-for-flutter-explore-routing-functionalroadclass">FunctionalRoadClass</a>?</span>  
The functional road class of the span. Gets the functional road class of the span.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-span-geometry">geometry</a></span> <span class="signature">→ <a href="sdk-for-flutter-explore-core-geopolyline-class">GeoPolyline</a></span>  
The <a href="sdk-for-flutter-explore-core-geopolyline-class">GeoPolyline</a> object representing the polyline of this span. Gets the <a href="sdk-for-flutter-explore-core-geopolyline-class">GeoPolyline</a> object representing the polyline of this span.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-span-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-span-lengthinmeters">lengthInMeters</a></span> <span class="signature">→ int</span>  
The length of this span in meters. Gets the length of this span in meters.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-span-nothroughrestrictionsindexes">noThroughRestrictionsIndexes</a></span> <span class="signature">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter">int</span>\></span></span>  
The list of indexes to <a href="sdk-for-flutter-explore-routing-section-nothroughrestrictions">Section.noThroughRestrictions</a> the parent section owns. In case the list is not empty, the user must judge all the indexed sdk routing noThroughRestriction's carefully before proceeding. Get the list of indexes to <a href="sdk-for-flutter-explore-routing-section-nothroughrestrictions">Section.noThroughRestrictions</a> the parent section owns. In case the list is not empty, the user must judge all the indexed <a href="sdk-for-flutter-explore-routing-section-nothroughrestrictions">Section.noThroughRestrictions</a>'s carefully before proceeding.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-span-noticeindexes">noticeIndexes</a></span> <span class="signature">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter">int</span>\></span></span>  
The list of indexes to <a href="sdk-for-flutter-explore-routing-section-sectionnotices">Section.sectionNotices</a> the parent section owns. In case the list is not empty, the user must judge all the indexed <a href="sdk-for-flutter-explore-routing-sectionnotice-class">SectionNotice</a>s carefully before proceeding. Gets the list of indexes to <a href="sdk-for-flutter-explore-routing-section-sectionnotices">Section.sectionNotices</a> the parent section owns. In case the list is not empty, the user must judge all the indexed <a href="sdk-for-flutter-explore-routing-sectionnotice-class">SectionNotice</a>'s carefully before proceeding.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-span-roadnumbers">roadNumbers</a></span> <span class="signature">→ <a href="sdk-for-flutter-explore-routing-localizedroadnumbers-class">LocalizedRoadNumbers</a></span>  
The road numbers on the span enriched with information specific to *route numbers* of a road such as I-10, US-50, or A3, and cardinal direction, if available, and a road level classification (`RouteType`). Gets the road numbers on the span enriched with information specific to *route numbers* of a road such as I-10, US-50, or A3, and cardinal direction, if available, and a road level classification (`RouteType`).

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-span-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-span-scooterattributes">scooterAttributes</a></span> <span class="signature">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-routing-accessattributes">AccessAttributes</a></span>\></span></span>  
The list of scooter access attributes on the span. The list of scooter access attributes on the span.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-span-sectionpolylineoffset">sectionPolylineOffset</a></span> <span class="signature">→ int</span>  
The position of the span inside the section's geometry, given as an offset. The span geometry starts from this offset and ends on the offset of the next span, both start offset point and end offset point being included in the span, because the spans' geometry share a point in the section's geometry. Gets the position of the span inside the section's geometry, given as an offset. The span geometry starts from this offset and ends on the offset of the next span, both start offset point and end offset point being included in the span, because the spans' geometry share a point in the section's geometry.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-span-segmentreference">segmentReference</a></span> <span class="signature">→ <a href="sdk-for-flutter-explore-routing-segmentreference-class">SegmentReference</a></span>  
The segment reference of this span. Gets the segment reference of this span.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-span-speedlimitinmeterspersecond">speedLimitInMetersPerSecond</a></span> <span class="signature">→ double?</span>  
The speed limit in meters per second on the span. Gets the speed limit in meters per second on the span.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-span-statecode">stateCode</a></span> <span class="signature">→ String?</span>  
The state code of the span. State code is available in some countries to denote principal subdivisions(provinces or states), e.g. in the United States, AK stands for Alaska and OH stands for Ohio. The format of state code can vary for different countries, take the United States as example, it consists of two alphabet letters. The value is `null` when no data is available. Gets the state code of the span. State code is available in some countries to denote principal subdivisions(provinces or states), e.g. in the United States, AK stands for Alaska and OH stands for Ohio. The format of state code can vary for different countries, take the United States as example, it consists of two alphabet letters. The value is `null` when no data is available.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-span-streetattributes">streetAttributes</a></span> <span class="signature">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-routing-streetattributes">StreetAttributes</a></span>\></span></span>  
The list of street attributes on the span. The list of street attributes on the span.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-span-streetnames">streetNames</a></span> <span class="signature">→ <a href="sdk-for-flutter-explore-core-localizedtexts-class">LocalizedTexts</a></span>  
The street names on the span. The street names on the span.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-span-trafficincidentindexes">trafficIncidentIndexes</a></span> <span class="signature">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter">int</span>\></span></span>  
The indexes of traffic incidents from the field <a href="sdk-for-flutter-explore-routing-section-trafficincidents">Section.trafficIncidents</a> of the parent <a href="sdk-for-flutter-explore-routing-section-class">Section</a>. Each matching incident takes at least a whole <a href="sdk-for-flutter-explore-routing-span-geometry">Span.geometry</a>. The same incident can take other spans and an area out of the built route as well. The indexes of traffic incidents from the field <a href="sdk-for-flutter-explore-routing-section-trafficincidents">Section.trafficIncidents</a> of the parent <a href="sdk-for-flutter-explore-routing-section-class">Section</a>. Each matching incident takes at least a whole <a href="sdk-for-flutter-explore-routing-span-geometry">Span.geometry</a>. The same incident can take other spans and an area out of the built route as well.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-span-truckattributes">truckAttributes</a></span> <span class="signature">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-routing-accessattributes">AccessAttributes</a></span>\></span></span>  
The list of truck access attributes on the span. The list of truck access attributes on the span.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-span-walkattributes">walkAttributes</a></span> <span class="signature">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-routing-walkattributes">WalkAttributes</a></span>\></span></span>  
The list of walk attributes on the span. The list of walk attributes on the span.

<div class="features">

<span class="feature">no setter</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-routing-span-getshieldtext">getShieldText</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-getShieldText-param-roadNumber" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-localizedroadnumber-class">LocalizedRoadNumber</a></span> <span class="parameter-name">roadNumber</span></span>) <span class="returntype parameter">→ String</span> </span>  
Converts full route number to the value to be displayed on the road shield.

<span class="name"><a href="sdk-for-flutter-explore-routing-span-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-span-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-routing-span-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
