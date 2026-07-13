---
title: "TrafficIncidentBase class - traffic library - Dart API"
slug: "sdk-for-flutter-explore-traffic-trafficincidentbase-class"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="traffic/traffic-library-sidebar.html" data-below-sidebar="traffic/TrafficIncidentBase-class-sidebar.html">

<div>

# <span class="kind-class">TrafficIncidentBase</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

TrafficIncident provides details about a traffic incident.

</div>

<div class="section">

Implementers  
- <a href="sdk-for-flutter-explore-mapview-picktrafficincidentresult-class">PickTrafficIncidentResult</a>
- <a href="sdk-for-flutter-explore-traffic-trafficincident-class">TrafficIncident</a>
- <a href="sdk-for-flutter-explore-routing-trafficincidentonroute-class">TrafficIncidentOnRoute</a>

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficincidentbase-trafficincidentbase">TrafficIncidentBase</a></span><span class="signature">(<span id="sdk-for-flutter-explore-param-impactGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-traffic-trafficincidentimpact">TrafficIncidentImpact</a></span> <span class="parameter-name">impactGetLambda</span>(), </span><span id="sdk-for-flutter-explore-param-typeGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-traffic-trafficincidenttype">TrafficIncidentType</a></span> <span class="parameter-name">typeGetLambda</span>(), </span><span id="sdk-for-flutter-explore-param-descriptionGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-localizedtext-class">LocalizedText</a></span> <span class="parameter-name">descriptionGetLambda</span>(), </span><span id="sdk-for-flutter-explore-param-startTimeGetLambda" class="parameter"><span class="type-annotation">DateTime?</span> <span class="parameter-name">startTimeGetLambda</span>(), </span><span id="sdk-for-flutter-explore-param-endTimeGetLambda" class="parameter"><span class="type-annotation">DateTime?</span> <span class="parameter-name">endTimeGetLambda</span>()</span>)</span>  
TrafficIncident provides details about a traffic incident.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficincidentbase-description">description</a></span> <span class="signature">→ <a href="sdk-for-flutter-explore-core-localizedtext-class">LocalizedText</a></span>  
The human readable description of the incident, possibly with location information. The description is currently not present in our map data. Therefore, when accessing the data from a picked carto POI via `TrafficIncidentResult`, then always an empty string is returned. This does not apply when using the `TrafficEngine`. Gets the human readable description of the incident, possibly with location information.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficincidentbase-endtime">endTime</a></span> <span class="signature">→ DateTime?</span>  
The time until which the incident is valid, after this time the incident should not be considered. The value is `null` if it hasn't been provided by the traffic incidents supplier. Get the time until which the incident is valid, after this time the incident should not be considered.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficincidentbase-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficincidentbase-impact">impact</a></span> <span class="signature">→ <a href="sdk-for-flutter-explore-traffic-trafficincidentimpact">TrafficIncidentImpact</a></span>  
The impact of the incident. The value is <a href="sdk-for-flutter-explore-traffic-trafficincidentimpact">TrafficIncidentImpact.unknown</a> if it hasn't been provided by the traffic incidents supplier. Gets the impact of the incident.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficincidentbase-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficincidentbase-starttime">startTime</a></span> <span class="signature">→ DateTime?</span>  
The time from which the incident is valid, before this time the incident should not be considered. The value is `null` if it hasn't been provided by the traffic incidents supplier. Gets the time from which the incident is valid, before this time the incident should not be considered.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficincidentbase-type">type</a></span> <span class="signature">→ <a href="sdk-for-flutter-explore-traffic-trafficincidenttype">TrafficIncidentType</a></span>  
The category of the incident. The value is <a href="sdk-for-flutter-explore-traffic-trafficincidenttype">TrafficIncidentType.unknown</a> if it hasn't been provided by the traffic incidents supplier. Gets the category of the incident.

<div class="features">

<span class="feature">no setter</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficincidentbase-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficincidentbase-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficincidentbase-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

