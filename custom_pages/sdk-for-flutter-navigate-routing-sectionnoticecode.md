---
title: "SectionNoticeCode enum - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-sectionnoticecode"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SectionNoticeCode.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/SectionNoticeCode-enum-sidebar.html">

<div>

# <span class="kind-enum">SectionNoticeCode</span> enum

</div>

<div class="section desc markdown">

Notice codes which point the issues encountered during processing of a <a href="sdk-for-flutter-navigate-routing-section-class">Section</a>.

**Note:** The section notice codes are going to be extended for new error situations.

</div>

## Values

<span class="name">violatedCriticalRule</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode</a></span>  
Route has violoated a non-detailed critical rule. Severity: <a href="sdk-for-flutter-navigate-routing-noticeseverity">NoticeSeverity.critical</a>.

<span class="name">violatedAvoidControlledAccessHighway</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode</a></span>  
Route did not manage to avoid user preference. Severity: <a href="sdk-for-flutter-navigate-routing-noticeseverity">NoticeSeverity.critical</a>.

<span class="name">violatedAvoidTollRoad</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode</a></span>  
Route did not manage to avoid user preference. Severity: <a href="sdk-for-flutter-navigate-routing-noticeseverity">NoticeSeverity.critical</a>.

<span class="name">violatedAvoidFerry</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode</a></span>  
Route did not manage to avoid user preference. Severity: <a href="sdk-for-flutter-navigate-routing-noticeseverity">NoticeSeverity.critical</a>.

<span class="name">violatedAvoidTunnel</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode</a></span>  
Route did not manage to avoid user preference. Severity: <a href="sdk-for-flutter-navigate-routing-noticeseverity">NoticeSeverity.critical</a>.

<span class="name">violatedAvoidDirtRoad</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode</a></span>  
Route did not manage to avoid user preference. Severity: <a href="sdk-for-flutter-navigate-routing-noticeseverity">NoticeSeverity.critical</a>.

<span class="name">violatedAvoidRailFerry</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode</a></span>  
Route did not manage to avoid user preference. Severity: <a href="sdk-for-flutter-navigate-routing-noticeseverity">NoticeSeverity.critical</a>.

<span class="name">violatedAvoidPark</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode</a></span>  
Route did not manage to avoid user preference. Severity: <a href="sdk-for-flutter-navigate-routing-noticeseverity">NoticeSeverity.critical</a>.

<span class="name">violatedBlockedRoad</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode</a></span>  
Route uses roads blocked by traffic events or route did not manage to avoid the requested `avoidBoundingBoxAreas` or `countries` or `segments`. Severity: <a href="sdk-for-flutter-navigate-routing-noticeseverity">NoticeSeverity.critical</a>.

<span class="name">violatedStartDirection</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode</a></span>  
Start direction of the route is not as requested. Severity: <a href="sdk-for-flutter-navigate-routing-noticeseverity">NoticeSeverity.critical</a>.

<span class="name">violatedCarpool</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode</a></span>  
Route did not manage to avoid user preference. Severity: <a href="sdk-for-flutter-navigate-routing-noticeseverity">NoticeSeverity.critical</a>.

<span class="name">violatedTurnRestriction</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode</a></span>  
Route uses a time-restricted turn. Severity: <a href="sdk-for-flutter-navigate-routing-noticeseverity">NoticeSeverity.critical</a>.

<span class="name">violatedVehicleRestriction</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode</a></span>  
Route uses a road which is forbidden for the given vehicle profile. Severity: <a href="sdk-for-flutter-navigate-routing-noticeseverity">NoticeSeverity.critical</a>.

<span class="name">violatedZoneRestriction</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode</a></span>  
Route uses a road which is part of restricted `zoneCategories` requested to be avoided by user. Severity: <a href="sdk-for-flutter-navigate-routing-noticeseverity">NoticeSeverity.critical</a>.

<span class="name">violatedAvoidUTurns</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode</a></span>  
Route did not manage to avoid u turns. Severity: <a href="sdk-for-flutter-navigate-routing-noticeseverity">NoticeSeverity.critical</a>.

<span class="name">violatedEmergencyGate</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode</a></span>  
Route goes through an emergency gate. Severity: <a href="sdk-for-flutter-navigate-routing-noticeseverity">NoticeSeverity.critical</a>.

<span class="name">violatedAvoidSeasonalClosure</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode</a></span>  
Route did not manage to avoid seasonal closure. Severity: <a href="sdk-for-flutter-navigate-routing-noticeseverity">NoticeSeverity.critical</a>.

<span class="name">violatedAvoidTruckRoadType</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode</a></span>  
Route did not manage to avoid restricted truck road types.

<span class="name">violatedAvoidTollTransponder</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode</a></span>  
Route did not manage to avoid toll booth that requires transponder. Severity: <a href="sdk-for-flutter-navigate-routing-noticeseverity">NoticeSeverity.critical</a>.

<span class="name">violatedChargingStationOpeningHours</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode</a></span>  
Charging at the charging station planned at the destination of this section falls outside of opening hours. Severity: <a href="sdk-for-flutter-navigate-routing-noticeseverity">NoticeSeverity.critical</a>.

<span class="name">violatedAvoidDifficultTurns</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode</a></span>  
Route did not manage to avoid difficult turns. Severity: <a href="sdk-for-flutter-navigate-routing-noticeseverity">NoticeSeverity.critical</a>.

<span class="name">seasonalClosure</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode</a></span>  
Route goes through seasonal closure. Severity: <a href="sdk-for-flutter-navigate-routing-noticeseverity">NoticeSeverity.info</a>.

<span class="name">tollTransponder</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode</a></span>  
Route goes through toll booth that requires transponder. Severity: <a href="sdk-for-flutter-navigate-routing-noticeseverity">NoticeSeverity.info</a>.

<span class="name">tollsDataUnavailable</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode</a></span>  
Tolls data was requested but could not be calculated for this section. Severity: <a href="sdk-for-flutter-navigate-routing-noticeseverity">NoticeSeverity.info</a>.

<span class="name">tollsDataTemporarilyUnavailable</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode</a></span>  
Tolls data was requested but is temporarily unavailable. Severity: <a href="sdk-for-flutter-navigate-routing-noticeseverity">NoticeSeverity.info</a>.

<span class="name">chargingStopNotNeeded</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode</a></span>  
A charging stop was planned at the destination of this section, but it is no longer needed. It may be issued only when refreshing a route via <a href="sdk-for-flutter-navigate-routing-routehandle-class">RouteHandle</a>. Severity: <a href="sdk-for-flutter-navigate-routing-noticeseverity">NoticeSeverity.info</a>.

<span class="name">noSchedule</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode</a></span>  
No schedule information is available for a transit section. As a result, departure/arrival times are approximated. Severity: <a href="sdk-for-flutter-navigate-routing-noticeseverity">NoticeSeverity.info</a>.

<span class="name">noIntermediate</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode</a></span>  
Information about intermediate stops is not available for a transit section. Severity: <a href="sdk-for-flutter-navigate-routing-noticeseverity">NoticeSeverity.info</a>.

<span class="name">unwantedMode</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode</a></span>  
This transit section contains a transport mode that was explictly disabled. Mode filtering is not available in this area. Severity: <a href="sdk-for-flutter-navigate-routing-noticeseverity">NoticeSeverity.info</a>.

<span class="name">scheduledTimes</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode</a></span>  
This transit section returned times which are scheduled times, even though delay information is available. Severity: <a href="sdk-for-flutter-navigate-routing-noticeseverity">NoticeSeverity.info</a>.

<span class="name">simplePolyline</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode</a></span>  
An accurate polyline is not available for this section. An accurate polyline is not available for this section. The returned polyline has been generated from departure and arrival places. Severity: <a href="sdk-for-flutter-navigate-routing-noticeseverity">NoticeSeverity.info</a>.

<span class="name">potentialCarpool</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode</a></span>  
Route utilizes a designated carpool lane, potentially subject to restrictions beyond the scheduled travel hours. Severity: <a href="sdk-for-flutter-navigate-routing-noticeseverity">NoticeSeverity.info</a>.

<span class="name">potentialTurnRestriction</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode</a></span>  
Route includes a turn that is potentially restricted and inaccessible beyond the scheduled travel hours. Severity: <a href="sdk-for-flutter-navigate-routing-noticeseverity">NoticeSeverity.info</a>.

<span class="name">potentialVehicleRestriction</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode</a></span>  
Route utilizes roads that are potentially off-limits to the specified vehicle profile beyond the scheduled travel hours. Severity: <a href="sdk-for-flutter-navigate-routing-noticeseverity">NoticeSeverity.info</a>.

<span class="name">potentialZoneRestriction</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode</a></span>  
Route incorporates roads within zones, which are potentially not accessible beyond the scheduled travel hours. Severity: <a href="sdk-for-flutter-navigate-routing-noticeseverity">NoticeSeverity.info</a>.

<span class="name">violatedMinChargeAtFirstCs</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode</a></span>  
The route can not reach the first charging station with the minimum required charge, as the initial charge was to low.

<span class="name">violatedMinChargeAtCs</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode</a></span>  
The route can not reach all charging stations on the route with the minimum required charge, as the initial charge was to low.

<span class="name">violatedMinChargeAtDestination</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode</a></span>  
The route can not reach the waypoint, as the there are not enough charging stops available or the initial charge was to low.

<span class="name">noThroughRestriction</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode</a></span>  
Route goes through a road that does not allow through traffic.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-routing-sectionnoticecode-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-sectionnoticecode-index">index</a></span> <span class="signature">→ int</span>  
A numeric identifier for the enumerated value.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-sectionnoticecode-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-routing-sectionnoticecode-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-sectionnoticecode-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-routing-sectionnoticecode-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Constants

<span class="name"><a href="sdk-for-flutter-navigate-routing-sectionnoticecode-values-constant">values</a></span> <span class="signature">→ const List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode</a></span>\></span></span>  
A constant List of the values in this enum, in order of their declaration.

</div>

<!-- /.main-content --> <!-- /.sidebar-offcanvas --> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
