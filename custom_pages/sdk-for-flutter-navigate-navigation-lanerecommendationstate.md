---
title: "LaneRecommendationState enum - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-lanerecommendationstate"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LaneRecommendationState.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/LaneRecommendationState-enum-sidebar.html">

<div>

# <span class="kind-enum">LaneRecommendationState</span> enum

</div>

<div class="section desc markdown">

Indicates whether this lane leads to the next maneuvers or not.

The next maneuver is the next upcoming maneuver which is not yet reached, but that was already announced as *new* maneuver in <a href="sdk-for-flutter-navigate-navigation-routeprogress-maneuverprogress">RouteProgress.maneuverProgress</a>.

</div>

## Values

<span class="name">notRecommended</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-navigation-lanerecommendationstate">LaneRecommendationState</a></span>  
This lane will not lead the user to the next maneuver.

<span class="name">recommended</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-navigation-lanerecommendationstate">LaneRecommendationState</a></span>  
Only possible when <a href="sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-lanesfornextnextmaneuver">ManeuverViewLaneAssistance.lanesForNextNextManeuver</a> is not empty. If <a href="sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-lanesfornextnextmaneuver">ManeuverViewLaneAssistance.lanesForNextNextManeuver</a> is not empty, then this lane will lead the user only to the next maneuver, but not to the maneuver after the next maneuver.

<span class="name">highlyRecommended</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-navigation-lanerecommendationstate">LaneRecommendationState</a></span>  
This lane will lead the user to the next maneuver. If <a href="sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-lanesfornextnextmaneuver">ManeuverViewLaneAssistance.lanesForNextNextManeuver</a> is not empty, then this lane will lead the user to the next maneuver *and* to the maneuver after the next maneuver.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lanerecommendationstate-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lanerecommendationstate-index">index</a></span> <span class="signature">→ int</span>  
A numeric identifier for the enumerated value.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lanerecommendationstate-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lanerecommendationstate-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lanerecommendationstate-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lanerecommendationstate-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Constants

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lanerecommendationstate-values-constant">values</a></span> <span class="signature">→ const List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-lanerecommendationstate">LaneRecommendationState</a></span>\></span></span>  
A constant List of the values in this enum, in order of their declaration.

</div>

<!-- /.main-content --> <!-- /.sidebar-offcanvas --> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
