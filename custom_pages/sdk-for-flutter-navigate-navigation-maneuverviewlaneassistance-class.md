---
title: "ManeuverViewLaneAssistance class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ManeuverViewLaneAssistance-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/ManeuverViewLaneAssistance-class-sidebar.html">

<div>

# <span class="kind-class">ManeuverViewLaneAssistance</span> class

</div>

<div class="section desc markdown">

A class that provides lane assistance information for the next maneuver(s).

During turn-by-turn navigation lane assistance can help a driver to choose the recommended lanes in order to complete the upcoming maneuvers. The notifications are synchronized with the <a href="sdk-for-flutter-navigate-navigation-eventtextlistener-class">EventTextListener</a>. <a href="sdk-for-flutter-navigate-navigation-eventtextlistener-class">EventTextListener</a> has 4 notification types for each maneuver: Range, Reminder, Distance and Action. Only the maneuver notification of type Distance will also notify a ManeuverViewLaneAssistance object (e.g. "After 400 meters, turn right onto Invalidenstraße"). The notification will not be sent when other types of maneuver notification are given. The notification will not be sent when no lane data is available. During tracking mode, no notifications are delivered. This ManeuverViewLaneAssistance information is valid until the next maneuver is reached.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-maneuverviewlaneassistance">ManeuverViewLaneAssistance</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-lanesForNextManeuver" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-lane-class">Lane</a></span>\></span></span> <span class="parameter-name">lanesForNextManeuver</span>, </span><span id="sdk-for-flutter-navigate-param-lanesForNextNextManeuver" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-lane-class">Lane</a></span>\></span></span> <span class="parameter-name">lanesForNextNextManeuver</span></span>)</span>  
Creates a new instance.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-lanesfornextmaneuver">lanesForNextManeuver</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-lane-class">Lane</a></span>\></span></span>  
A list of lanes on the current road that leads to the upcoming maneuver. The lanes are sorted from left to right: The lane at index 0 represents the leftmost lane and the last index represents the rightmost lane. This is valid for both right-hand and left-hand driving countries. Contraflow lanes are not included in the list. The list is guaranteed to be non-empty. <a href="sdk-for-flutter-navigate-navigation-roadattributes-isrightdrivingside">RoadAttributes.isRightDrivingSide</a> indicates if this is a left-hand driving country or not.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-lanesfornextnextmaneuver">lanesForNextNextManeuver</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-lane-class">Lane</a></span>\></span></span>  
A list of lanes on the road that leads to the maneuver after the upcoming maneuver. The lanes are sorted from left to right: The lane at index 0 represents the leftmost lane and the last index represents the rightmost lane. This is valid for both right-hand and left-hand driving countries. Contraflow lanes are not included in the list. <a href="sdk-for-flutter-navigate-navigation-roadattributes-isrightdrivingside">RoadAttributes.isRightDrivingSide</a> indicates if this is a left-hand driving country or not. By default, this list is empty. It will be filled when the next two maneuvers are too close to each other, or when the next two maneuvers are roundabout maneuvers. Note: This notification is delivered at the same time as the <a href="sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-lanesfornextmaneuver">ManeuverViewLaneAssistance.lanesForNextManeuver</a>. There is no separate maneuver notification on the second maneuver when two maneuvers are are too close to each other.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
