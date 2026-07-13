---
title: "DynamicRoutingEngineOptions class - trafficawarenavigation library - Dart API"
slug: "sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengineoptions-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- DynamicRoutingEngineOptions-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="trafficawarenavigation/trafficawarenavigation-library-sidebar.html" data-below-sidebar="trafficawarenavigation/DynamicRoutingEngineOptions-class-sidebar.html">

<div>

# <span class="kind-class">DynamicRoutingEngineOptions</span> class

</div>

<div class="section desc markdown">

Options defining the behavior of the <a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-class">DynamicRoutingEngine</a>.

Both, `minTimeDifference` and `minTimeDifferencePercentage`, will be checked: When the poll interval is reached, the smaller difference will win and the <a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutinglistener-class">DynamicRoutingListener</a> is notified.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengineoptions-dynamicroutingengineoptions">DynamicRoutingEngineOptions</a></span><span class="signature">()</span>  
Creates an instance of this class.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengineoptions-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengineoptions-mintimedifference">minTimeDifference</a></span> <span class="signature">↔ Duration?</span>  
The minimum time difference, before notifying the <a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutinglistener-class">DynamicRoutingListener</a>. To get notified, the following check must be true: oldEstimatedTimeOfArrival - newEstimatedTimeOfArrival \> <a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengineoptions-mintimedifference">DynamicRoutingEngineOptions.minTimeDifference</a>. A value of 0 will be treated as `null` meaning no event will be sent. In order to receive events the difference needs to be greater than 0. Defaults to `null`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengineoptions-mintimedifferencepercentage">minTimeDifferencePercentage</a></span> <span class="signature">↔ double?</span>  
The value is in the range of \[0, 1\] over the remaining (current position to next waypoint) To get notified, the following check must be true: oldEstimatedTimeOfArrival - newEstimatedTimeOfArrival \>= newRouteDuration \* `min_time_difference_percentage`. A value of 0 will be treated as `null` meaning no event will be sent. In order to receive events the difference needs to be greater than 0. Defaults to `null`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengineoptions-pollinterval">pollInterval</a></span> <span class="signature">↔ Duration</span>  
The poll interval. Zero duration triggers a route calculation with each position update. Triggered via <a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-updatecurrentlocation">DynamicRoutingEngine.updateCurrentLocation</a> Defaults to 15 minutes.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengineoptions-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengineoptions-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengineoptions-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengineoptions-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
