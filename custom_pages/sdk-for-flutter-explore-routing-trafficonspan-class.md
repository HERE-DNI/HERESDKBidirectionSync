---
title: "TrafficOnSpan class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-trafficonspan-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TrafficOnSpan-class.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/TrafficOnSpan-class-sidebar.html">

<div>

# <span class="kind-class">TrafficOnSpan</span> class

</div>

<div class="section desc markdown">

Traffic information of a span along a route.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-routing-trafficonspan-trafficonspan">TrafficOnSpan</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-explore-routing-trafficonspan-basespeedinmeterspersecond">baseSpeedInMetersPerSecond</a></span> <span class="signature">↔ double</span>  
The speed, in meters per second, without taking traffic into consideration.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-trafficonspan-consumptioninkilowatthours">consumptionInKilowattHours</a></span> <span class="signature">↔ double?</span>  
The power consumption in kilowatt-hours (kWh) necessary to traverse the span.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-trafficonspan-duration">duration</a></span> <span class="signature">↔ Duration</span>  
The time duration necessary to traverse the traffic span. This duration takes also into consideration the delays caused by the traffic.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-trafficonspan-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-trafficonspan-incidentindices">incidentIndices</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter">int</span>\></span></span>  
The indices of traffic incidents from the field <a href="sdk-for-flutter-explore-routing-trafficonsection-trafficincidents">TrafficOnSection.trafficIncidents</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-trafficonspan-jamfactor">jamFactor</a></span> <span class="signature">↔ double</span>  
The traffic jam factor shows the traffic condition in a numeric way. It is a value in the range \[0.0, 10.0\]. A large jamFactor value means more traffic jam in general. Specifically, 0.0 means free traffic and 10.0 means stationary traffic.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-trafficonspan-lengthinmeters">lengthInMeters</a></span> <span class="signature">↔ double</span>  
Length of the traffic span, in meters.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-trafficonspan-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-trafficonspan-trafficdelay">trafficDelay</a></span> <span class="signature">↔ Duration</span>  
The estimated extra time in seconds spent due to traffic delays along this traffic span. Negative values indicate that the traffic span can be traversed faster than usual.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-trafficonspan-trafficsectionpolylineoffset">trafficSectionPolylineOffset</a></span> <span class="signature">↔ int</span>  
Index over <a href="sdk-for-flutter-explore-routing-trafficonsection-geometry">TrafficOnSection.geometry</a> where this span starts.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-trafficonspan-trafficspeedinmeterspersecond">trafficSpeedInMetersPerSecond</a></span> <span class="signature">↔ double</span>  
The speed, in meters per second, considering traffic.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-routing-trafficonspan-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-trafficonspan-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-routing-trafficonspan-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
