---
title: "TrafficIncident class - traffic library - Dart API"
slug: "sdk-for-flutter-navigate-traffic-trafficincident-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TrafficIncident-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="traffic/traffic-library-sidebar.html" data-below-sidebar="traffic/TrafficIncident-class-sidebar.html">

<div>

# <span class="kind-class">TrafficIncident</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

TrafficIncident provides details about a traffic incident.

</div>

<div class="section">

Implemented types  
- <a href="sdk-for-flutter-navigate-traffic-trafficincidentbase-class">TrafficIncidentBase</a>

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficincident-trafficincident">TrafficIncident</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficincident-codes">codes</a></span> <span class="signature">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter">int</span>\></span></span>  
The list of standardized codes as categorized in ISO 14819-2:2013 standard for this incident category. Codes are given in order of importance, so the first item in the list is considered the primary cause of the incident. Gets the list of standardized codes as categorized in ISO 14819-2:2013 standard for this incident category.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficincidentbase-description">description</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-core-localizedtext-class">LocalizedText</a></span>  
The human readable description of the incident, possibly with location information. The description is currently not present in our map data. Therefore, when accessing the data from a picked carto POI via `TrafficIncidentResult`, then always an empty string is returned. This does not apply when using the `TrafficEngine`. Gets the human readable description of the incident, possibly with location information.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficincidentbase-endtime">endTime</a></span> <span class="signature">→ DateTime?</span>  
The time until which the incident is valid, after this time the incident should not be considered. The value is `null` if it hasn't been provided by the traffic incidents supplier. Get the time until which the incident is valid, after this time the incident should not be considered.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficincident-entrytime">entryTime</a></span> <span class="signature">→ DateTime?</span>  
The time the incident was entered into the system. The value is `null` if it hasn't been provided by the traffic incidents supplier. Gets the time the incident was entered into the system.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficincidentbase-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficincident-id">id</a></span> <span class="signature">→ String</span>  
The unique current identifier for a traffic incident. Gets the unique current identifier for a traffic incident.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficincidentbase-impact">impact</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-traffic-trafficincidentimpact">TrafficIncidentImpact</a></span>  
The impact of the incident. The value is <a href="sdk-for-flutter-navigate-traffic-trafficincidentimpact">TrafficIncidentImpact.unknown</a> if it hasn't been provided by the traffic incidents supplier. Gets the impact of the incident.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficincident-isroadclosed">isRoadClosed</a></span> <span class="signature">→ bool</span>  
The flag indicates whether road is closed or not. Gets the flag indicating whether road is closed or not.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficincident-junctionstraversability">junctionsTraversability</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-traffic-junctionstraversability">JunctionsTraversability</a></span>  
The traversability of junctions along the affected road. Gets the traversability of junctions along the affected road.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficincident-location">location</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-traffic-trafficlocation-class">TrafficLocation</a></span>  
The location of the incident. Gets the location of the incident.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficincident-originalid">originalId</a></span> <span class="signature">→ String</span>  
The unique identifier of the first traffic incident. The original id remains the same whenever the traffic incident is updated and <a href="sdk-for-flutter-navigate-traffic-trafficincident-id">TrafficIncident.id</a> is changed. Once an incident chain has been created, this value will never change. The traffic incident an be looked up by original id using <a href="sdk-for-flutter-navigate-traffic-trafficengine-lookupincident">TrafficEngine.lookupIncident</a>. Gets the unique identifier of the first traffic incident.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficincident-parentid">parentId</a></span> <span class="signature">→ String?</span>  
The identifier of another incident to which this incident is linked. The value is `null` if the incident doesn't have a parent. Gets the identifier of another incident to which this incident is linked.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficincidentbase-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficincidentbase-starttime">startTime</a></span> <span class="signature">→ DateTime?</span>  
The time from which the incident is valid, before this time the incident should not be considered. The value is `null` if it hasn't been provided by the traffic incidents supplier. Gets the time from which the incident is valid, before this time the incident should not be considered.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficincident-summary">summary</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-core-localizedtext-class">LocalizedText</a></span>  
The human readable summary of the incident. The summary field provides a short version of the description containing no location information. The expected summary language can be managed via <a href="sdk-for-flutter-navigate-traffic-trafficincidentsqueryoptions-languagecode">TrafficIncidentsQueryOptions.languageCode</a> and <a href="sdk-for-flutter-navigate-traffic-trafficincidentlookupoptions-languagecode">TrafficIncidentLookupOptions.languageCode</a>. Gets the human readable summary of the incident.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficincidentbase-type">type</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-traffic-trafficincidenttype">TrafficIncidentType</a></span>  
The category of the incident. The value is <a href="sdk-for-flutter-navigate-traffic-trafficincidenttype">TrafficIncidentType.unknown</a> if it hasn't been provided by the traffic incidents supplier. Gets the category of the incident.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficincident-vehiclerestrictions">vehicleRestrictions</a></span> <span class="signature">→ Map<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-traffic-trafficincidentrestrictedvehiclecategory">TrafficIncidentRestrictedVehicleCategory</a></span>, <span class="type-parameter"><a href="sdk-for-flutter-navigate-traffic-trafficincidentvehiclerestriction-class">TrafficIncidentVehicleRestriction</a></span>\></span></span>  
The map of restricted vehicle categories to restrictions. A vehicle is restricted if at least one restriction field is applicable for it. If the map is empty, there're no restricted vehicles for the incident. Gets the map of restricted vehicle categories to restrictions.

<div class="features">

<span class="feature">no setter</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficincidentbase-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficincidentbase-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficincidentbase-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
