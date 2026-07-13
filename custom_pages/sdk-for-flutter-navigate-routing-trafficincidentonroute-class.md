---
title: "TrafficIncidentOnRoute class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-trafficincidentonroute-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/TrafficIncidentOnRoute-class-sidebar.html">

<div>

# <span class="kind-class">TrafficIncidentOnRoute</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Traffic incidents on a route.

Use <a href="sdk-for-flutter-navigate-routing-section-trafficincidents">Section.trafficIncidents</a> to get a list of incidents on a route section. Use <a href="sdk-for-flutter-navigate-routing-span-trafficincidentindexes">Span.trafficIncidentIndexes</a> to associate incidents with spans. Each incident takes at least the whole geometry of matching spans. Also, an incident can take some place out of the built route.

</div>

<div class="section">

Implemented types  
- <a href="sdk-for-flutter-navigate-traffic-trafficincidentbase-class">TrafficIncidentBase</a>

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-routing-trafficincidentonroute-trafficincidentonroute">TrafficIncidentOnRoute</a></span><span class="signature">()</span>  

## Properties

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

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficincidentbase-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-trafficincidentonroute-id">id</a></span> <span class="signature">→ String?</span>  
The unique current identifier for a traffic incident. The identifier can be changed by the backend due to some events, e.g. changing of <a href="sdk-for-flutter-navigate-traffic-trafficincidentbase-endtime">TrafficIncidentBase.endTime</a>. This field will be empty for `OfflineRouting`. Gets the unique current identifier for a traffic incident.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficincidentbase-impact">impact</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-traffic-trafficincidentimpact">TrafficIncidentImpact</a></span>  
The impact of the incident. The value is <a href="sdk-for-flutter-navigate-traffic-trafficincidentimpact">TrafficIncidentImpact.unknown</a> if it hasn't been provided by the traffic incidents supplier. Gets the impact of the incident.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

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

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficincidentbase-type">type</a></span> <span class="signature">→ <a href="sdk-for-flutter-navigate-traffic-trafficincidenttype">TrafficIncidentType</a></span>  
The category of the incident. The value is <a href="sdk-for-flutter-navigate-traffic-trafficincidenttype">TrafficIncidentType.unknown</a> if it hasn't been provided by the traffic incidents supplier. Gets the category of the incident.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

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

