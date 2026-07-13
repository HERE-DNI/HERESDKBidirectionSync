---
title: "TrafficFlowBase class - traffic library - Dart API"
slug: "sdk-for-flutter-explore-traffic-trafficflowbase-class"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="traffic/traffic-library-sidebar.html" data-below-sidebar="traffic/TrafficFlowBase-class-sidebar.html">

<div>

# <span class="kind-class">TrafficFlowBase</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

This interface provides details about a traffic flow.\
For additional information about fields, refer to <a href="https://www.here.com/docs/bundle/traffic-api-v7-api-reference/page/index.html#tag/Real-Time-Traffic">Traffic API v7 API Reference: Traffic API v7</a>.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section">

Implementers  
- <a href="sdk-for-flutter-explore-traffic-trafficflow-class">TrafficFlow</a>

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficflowbase-trafficflowbase">TrafficFlowBase</a></span><span class="signature">(<span id="sdk-for-flutter-explore-param-freeFlowSpeedInMetersPerSecondGetLambda" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">freeFlowSpeedInMetersPerSecondGetLambda</span>(), </span><span id="sdk-for-flutter-explore-param-jamFactorGetLambda" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">jamFactorGetLambda</span>()</span>)</span>  
This interface provides details about a traffic flow.\
For additional information about fields, refer to <a href="https://www.here.com/docs/bundle/traffic-api-v7-api-reference/page/index.html#tag/Real-Time-Traffic">Traffic API v7 API Reference: Traffic API v7</a>.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficflowbase-freeflowspeedinmeterspersecond">freeFlowSpeedInMetersPerSecond</a></span> <span class="signature">→ double</span>  
The reference speed in meters per second along the roadway when no traffic is present. Gets the reference speed in meters per second along the roadway when no traffic is present.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficflowbase-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficflowbase-jamfactor">jamFactor</a></span> <span class="signature">→ double</span>  
A value for the amount of traffic on the roadway. The value, between 0.0 and 10.0, indicate the expected quality of travel. A value of 0.0 indicates that there is no congestion on the roadway. As the value approaches 10.0, it indicates increasing congestion. A value of 10.0 is reserved to represent a blocked roadway (closure). Gets a value for the amount of traffic on the roadway.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-traffic-trafficflowbase-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

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

