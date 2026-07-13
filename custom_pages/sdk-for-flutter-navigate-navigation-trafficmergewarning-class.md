---
title: "TrafficMergeWarning class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-trafficmergewarning-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TrafficMergeWarning-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/TrafficMergeWarning-class-sidebar.html">

<div>

# <span class="kind-class">TrafficMergeWarning</span> class

</div>

<div class="section desc markdown">

A class that provides warning for merging traffic.

The main field describing the merging traffic is `TrafficMergeWarning.road_type` specifying the type of road containing traffic which is merging with the current road. Use `TrafficMergeWarningListener` to get notifications about upcoming merging traffic.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trafficmergewarning-trafficmergewarning">TrafficMergeWarning</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-distanceToTrafficMergeInMeters" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">distanceToTrafficMergeInMeters</span>, </span><span id="sdk-for-flutter-navigate-param-distanceType" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType</a></span> <span class="parameter-name">distanceType</span></span>)</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trafficmergewarning-distancetotrafficmergeinmeters">distanceToTrafficMergeInMeters</a></span> <span class="signature">↔ double</span>  
Distance to merging traffic in meters.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trafficmergewarning-distancetype">distanceType</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType</a></span>  
The distance type for the warning, e.g. a warning for a new traffic merge location ahead or a warning for passing a traffic merge location. Since the traffic merge warning is given relative to a single position on the route, `DistanceType.REACHED` will never be given for this warning.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trafficmergewarning-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trafficmergewarning-id">id</a></span> <span class="signature">↔ int</span>  
Unique identifier for this specific traffic merge warning instance. Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace. Use this ID to track, update, or dismiss individual warning instances of this type.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trafficmergewarning-lanecount">laneCount</a></span> <span class="signature">↔ int</span>  
Number of lanes of the merging road containing the traffic. If the road has no lanes defined, than the number of lanes returned will be 1.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trafficmergewarning-roadtype">roadType</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-trafficmergeroadtype">TrafficMergeRoadType</a></span>  
Type of road which contains the merging traffic.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trafficmergewarning-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trafficmergewarning-side">side</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-trafficmergeside">TrafficMergeSide</a></span>  
The side from which the traffic is merging.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trafficmergewarning-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trafficmergewarning-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trafficmergewarning-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
