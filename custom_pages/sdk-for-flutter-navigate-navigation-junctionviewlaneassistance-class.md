---
title: "JunctionViewLaneAssistance class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/JunctionViewLaneAssistance-class-sidebar.html">

<div>

# <span class="kind-class">JunctionViewLaneAssistance</span> class

</div>

<div class="section desc markdown">

A class that provides lane assistance information for the next complex junction in order to keep following the route.

It is recommended to indicate <a href="sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-class">JunctionViewLaneAssistance</a> and <a href="sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-class">ManeuverViewLaneAssistance</a> separately or to indicate only <a href="sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-class">ManeuverViewLaneAssistance</a> information - <a href="sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-class">JunctionViewLaneAssistance</a> will recommend all lanes that allow to pass the upcoming complex junction, regardless if they will lead to the next maneuver or not. If the location of a maneuver lies on an upcoming complex junction, the recommended lanes will be the same as the ones from <a href="sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-class">ManeuverViewLaneAssistance</a>.

A junction is recognized as complex only if:

- it is at least a bifurcation;
- it has at least two lanes whose directions do not follow the current route. In opposition to <a href="sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-class">ManeuverViewLaneAssistance</a>, notifications are also forwarded when there is no maneuver action occurring at the next complex junction. Therefore, <a href="sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-class">JunctionViewLaneAssistance</a> can be disjointed from maneuvers. If lane assistance should be used to associate it with upcoming maneuvers, consider to use <a href="sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-class">ManeuverViewLaneAssistance</a> instead. Note that <a href="sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-class">ManeuverViewLaneAssistance</a> notifications are synchronized with maneuver events, whereas <a href="sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-class">JunctionViewLaneAssistance</a> events are not strictly synchronized with maneuver events.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-junctionviewlaneassistance">JunctionViewLaneAssistance</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-lanesForNextJunction" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-lane-class">Lane</a></span>\></span></span> <span class="parameter-name">lanesForNextJunction</span>, </span><span id="sdk-for-flutter-navigate-param-distanceToJunctionInMeters" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">distanceToJunctionInMeters</span></span>)</span>  
Creates a new instance.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-distancetojunctioninmeters">distanceToJunctionInMeters</a></span> <span class="signature">↔ double</span>  
Distance to the next complex junction in meters.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-lanesfornextjunction">lanesForNextJunction</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-lane-class">Lane</a></span>\></span></span>  
A list of lanes on the next complex junction. The lanes are sorted from left to right: The lane at index 0 represents the leftmost lane and the last index represents the rightmost lane. This is valid for right-hand and left-hand driving countries. An empty list means that the complex junction has been passed and that the lane information is not valid anymore. Exactly one event with a non-empty list is delivered before reaching a complex junction and one event with an empty list afterwards.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

