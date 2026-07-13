---
title: "TrafficFlowQueryOptions class - traffic library - Dart API"
slug: "sdk-for-flutter-navigate-traffic-trafficflowqueryoptions-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="traffic/traffic-library-sidebar.html" data-below-sidebar="traffic/TrafficFlowQueryOptions-class-sidebar.html">

<div>

# <span class="kind-class">TrafficFlowQueryOptions</span> class

</div>

<div class="section desc markdown">

The options to specify how traffic flow data should be queried.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficflowqueryoptions-trafficflowqueryoptions">TrafficFlowQueryOptions</a></span><span class="signature">()</span>  
Creates a new instance.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficflowqueryoptions-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficflowqueryoptions-maxjamfactor">maxJamFactor</a></span> <span class="signature">↔ double?</span>  
Max jam factor value. The jam factor is a value for the amount of traffic on the roadway. The value is between 0.0 and 10.0 (inclusive). This will be used with <a href="sdk-for-flutter-navigate-traffic-trafficflowqueryoptions-minjamfactor">TrafficFlowQueryOptions.minJamFactor</a> to filter queried flow. If the value is null filtering by the max jam factor is not applied.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficflowqueryoptions-minjamfactor">minJamFactor</a></span> <span class="signature">↔ double?</span>  
Min jam factor value. The jam factor is a value for the amount of traffic on the roadway. The value is between 0.0 and 10.0 (inclusive). This will be used with <a href="sdk-for-flutter-navigate-traffic-trafficflowqueryoptions-maxjamfactor">TrafficFlowQueryOptions.maxJamFactor</a> to filter queried flow. If the value is `null`, then filtering by the min jam factor is not applied.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficflowqueryoptions-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficflowqueryoptions-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficflowqueryoptions-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficflowqueryoptions-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

