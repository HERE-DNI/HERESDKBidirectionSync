---
title: "TrafficFlow class - traffic library - Dart API"
slug: "sdk-for-flutter-explore-traffic-trafficflow-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TrafficFlow-class.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="traffic/traffic-library-sidebar.html" data-below-sidebar="traffic/TrafficFlow-class-sidebar.html">

<div>

# <span class="kind-class">TrafficFlow</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

This class provides details about traffic flow along a <a href="sdk-for-flutter-explore-core-geocorridor-class">GeoCorridor</a>, inside a <a href="sdk-for-flutter-explore-core-geocircle-class">GeoCircle</a> or a <a href="sdk-for-flutter-explore-core-geobox-class">GeoBox</a>, that represents particular path of the road network.\
Backends for TrafficEngine and traffic vector tiles are different however backends may share the same data.\
For additional information about fields, refer to <a href="https://www.here.com/docs/bundle/traffic-api-v7-api-reference/page/index.html#tag/Real-Time-Traffic">Traffic API v7 API Reference: Traffic API v7</a>.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section">

Implemented types  
- <a href="sdk-for-flutter-explore-traffic-trafficflowbase-class">TrafficFlowBase</a>

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficflow-trafficflow">TrafficFlow</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficflow-confidence">confidence</a></span> <span class="signature">→ double?</span>  
The confidence field indicates the proportion of real-time data included in the speed calculation. It is a normalized value between 0.0 and 1.0 with the following meaning:

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficflowbase-freeflowspeedinmeterspersecond">freeFlowSpeedInMetersPerSecond</a></span> <span class="signature">→ double</span>  
The reference speed in meters per second along the roadway when no traffic is present. Gets the reference speed in meters per second along the roadway when no traffic is present.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficflowbase-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficflowbase-jamfactor">jamFactor</a></span> <span class="signature">→ double</span>  
A value for the amount of traffic on the roadway. The value, between 0.0 and 10.0, indicate the expected quality of travel. A value of 0.0 indicates that there is no congestion on the roadway. As the value approaches 10.0, it indicates increasing congestion. A value of 10.0 is reserved to represent a blocked roadway (closure). Gets a value for the amount of traffic on the roadway.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficflow-jamtendency">jamTendency</a></span> <span class="signature">→ int?</span>  
The jamTendency field denotes whether the congestion is increasing, decreasing, or constant. The congestion tendency may take the following values:

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficflow-junctionstraversability">junctionsTraversability</a></span> <span class="signature">→ <a href="sdk-for-flutter-explore-traffic-junctionstraversability">JunctionsTraversability</a>?</span>  
The traversability of junctions along the affected road. Gets the traversability of junctions along the affected road.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficflow-location">location</a></span> <span class="signature">→ <a href="sdk-for-flutter-explore-traffic-trafficlocation-class">TrafficLocation</a></span>  
Defines the location affected by traffic flow. Gets the location of the incident.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficflowbase-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficflow-speedinmeterspersecond">speedInMetersPerSecond</a></span> <span class="signature">→ double?</span>  
The expected speed in meters per second along the roadway; will not exceed the legal speed limit. Gets the expected speed in meters per second along the roadway; will not exceed the legal speed limit.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficflow-speeduncappedinmeterspersecond">speedUncappedInMetersPerSecond</a></span> <span class="signature">→ double?</span>  
The expected speed in meters per second that a car can drive along a roadway right now; may exceed the legal speed limit. It is based on probe data (GPS coordinates sent by vehicles or mobile devices driving along that roadway). The calculated 'expected speed' may be over the legal speed limit for that roadway because people are driving over the speed limit. Gets the expected speed in meters per second along the roadway.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficflow-traversability">traversability</a></span> <span class="signature">→ <a href="sdk-for-flutter-explore-traffic-traversability">Traversability</a>?</span>  
The traversability of roadway. Gets the traversability of roadway.

<div class="features">

<span class="feature">no setter</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficflowbase-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficflowbase-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficflowbase-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
