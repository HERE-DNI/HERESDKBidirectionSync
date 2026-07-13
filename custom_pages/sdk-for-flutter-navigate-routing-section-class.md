---
title: "Section class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-section-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- Section-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/Section-class-sidebar.html">

<div>

# <span class="kind-class">Section</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

A section is a part of the route between two stopovers.

A stopover is a location on the route where a stop is made.

**Note:** A section contains a list of <a href="sdk-for-flutter-navigate-routing-sectionnotice-class">SectionNotice</a> objects that describe *potential issues* after the route was calculated. If the list is non-empty, it is recommended to evaluate possible violations against the requested route options and reject the route if deemed necessary.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-routing-section-section">Section</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-routing-section-arrivallocationtime">arrivalLocationTime</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-core-locationtime-class">LocationTime</a>?</span>  
The arrival location time of this section. Gets the arrival location time of this section.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-section-arrivalplace">arrivalPlace</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-routing-routeplace-class">RoutePlace</a></span>  
The arrival place. Describes the arrival place. Gets the arrival place.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-section-boundingbox">boundingBox</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-core-geobox-class">GeoBox</a></span>  
The closest rectangular area where this section fits in. Gets the closest rectangular area where this section fits in.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-section-consumptioninkilowatthours">consumptionInKilowattHours</a></span> <span class="signature">→ double?</span>  
Estimated net energy consumption (in kWh) if the transportation mode used for this route is an electric vehicle. Note that it can be negative due to energy recuperation. Gets estimated net energy consumption (in kWh) if the transportation mode used for this route is an electric vehicle. Note that it can be negative due to energy recuperation.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-section-departurelocationtime">departureLocationTime</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-core-locationtime-class">LocationTime</a>?</span>  
The departure location time of this section. Gets the departure location time of this section.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-section-departureplace">departurePlace</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-routing-routeplace-class">RoutePlace</a></span>  
Describes the departure place. Gets the departure place.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-section-duration">duration</a></span> <span class="signature">→ Duration</span>  
The estimated time in seconds needed to travel along this section, including real-time traffic delays if available. Gets the estimated time in seconds needed to travel along this section, including real-time traffic delays if available.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-section-geometry">geometry</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-core-geopolyline-class">GeoPolyline</a></span>  
The <a href="sdk-for-flutter-navigate-core-geopolyline-class">GeoPolyline</a> object representing the polyline of this section. Gets the <a href="sdk-for-flutter-navigate-core-geopolyline-class">GeoPolyline</a> object representing the polyline of this section.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-section-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-section-indoorsectiondetails">indoorSectionDetails</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-routing-indoorsectiondetails-class">IndoorSectionDetails</a>?</span>  
Indoor routing section information. Gets indoor routing section details.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-section-lengthinmeters">lengthInMeters</a></span> <span class="signature">→ int</span>  
The length of this section in meters. Gets the length of this section in meters.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-section-maneuvers">maneuvers</a></span> <span class="signature">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-maneuver-class">Maneuver</a></span>\></span></span>  
The maneuvers for this section. Gets the maneuvers for this section.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-section-nothroughrestrictions">noThroughRestrictions</a></span> <span class="signature">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-violatedrestriction-class">ViolatedRestriction</a></span>\></span></span>  
The list of no through restriction The no through restriction area is part of the road network that do not allow through traffic. For example the `Resident only` sign indicates that vehicles are only allowed to enter this area if they are making a stop. This area will be set only if `origin`, `destination` or `via` waypoint will be requested within the area. list of no through restriction.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-section-passthroughwaypoints">passthroughWaypoints</a></span> <span class="signature">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-passthroughwaypoint-class">PassThroughWaypoint</a></span>\></span></span>  
The list of passthrough waypoints in this section. Gets the list of passthrough waypoints in this section.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-section-postactions">postActions</a></span> <span class="signature">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-postaction-class">PostAction</a></span>\></span></span>  
The post actions that must be done after the arrival at the end of the section. Gets the post actions that must be done after the arrival at the end of the section.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-section-preactions">preActions</a></span> <span class="signature">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-preaction-class">PreAction</a></span>\></span></span>  
The preceding actions that must be done prior to departure at the beginning of the section. Gets the preceding actions that must be done prior to departure at the beginning of the section.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-section-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-section-sectionnotices">sectionNotices</a></span> <span class="signature">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-sectionnotice-class">SectionNotice</a></span>\></span></span>  
The notices which explain the issues encountered during processing of this section. For example, while the scooter transport mode is selected, if no reasonable alternative route is possible except violating controlled-access to highway rule for the section, one notice is generated for the violation. The user must judge all the notices carefully before proceeding. Gets the notices which explains the issues encountered during processing of this section. For example, while the scooter transport mode is selected, if no reasonable alternative route is possible except violating controlled-access to highway rule for the section, one notice is generated for the violation. The user must judge all the notices carefully before proceeding.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-section-sectiontransportmode">sectionTransportMode</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-routing-sectiontransportmode">SectionTransportMode</a></span>  
The transport mode of this section. Gets the transport mode of this section.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-section-spans">spans</a></span> <span class="signature">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-span-class">Span</a></span>\></span></span>  
The <a href="sdk-for-flutter-navigate-routing-span-class">Span</a>'s that constitute this section. Gets the <a href="sdk-for-flutter-navigate-routing-span-class">Span</a>'s that constitute this section.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-section-tolls">tolls</a></span> <span class="signature">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-toll-class">Toll</a></span>\></span></span>  
All the tolls for this section. Note that tolls are found depending on the transport mode. For example, if pedestrian or bicycle transport mode specified, route sections have no tolls. Indoor route sections have no tolls, too. **Note**: If you're using the `OfflineRoutingEngine`, be aware that this feature is currently in **beta**. As a result, there may be some bugs or unexpected behaviors. Additionally, this feature and related APIs may be updated in future releases without going through the deprecation process. Note that the `OfflineRoutingEngine` is only available with the Navigate license. If you're using the `RoutingEngine`, this feature is considered to be stable. Gets all the tolls for this section. Note that tolls are found depending on the transport mode. For example, if pedestrian or bicycle transport mode specified, route sections have no tolls. Indoor route sections have no tolls, too.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-section-trafficdelay">trafficDelay</a></span> <span class="signature">→ Duration</span>  
The estimated extra time in seconds spent due to traffic delays along this section. Negative values indicate that the route can be traversed faster than usual. Gets the estimated extra time in seconds spent due to traffic delays along this section. Negative values indicate that the route can be traversed faster than usual.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-section-trafficincidents">trafficIncidents</a></span> <span class="signature">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-trafficincidentonroute-class">TrafficIncidentOnRoute</a></span>\></span></span>  
The list of traffic incidents that are found on the section. the list of traffic incidents that are found on the section.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-section-transitdetails">transitDetails</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-routing-transitsectiondetails-class">TransitSectionDetails</a>?</span>  
The transit details which are avilable for transit sections of a route. Gets the details of a transit section.

<div class="features">

<span class="feature">no setter</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-routing-section-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-section-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-routing-section-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
