---
title: "ManeuverAction enum - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-maneuveraction"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ManeuverAction.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/ManeuverAction-enum-sidebar.html">

<div>

# <span class="kind-enum">ManeuverAction</span> enum

</div>

<div class="section desc markdown">

Maneuver action type.

</div>

## Values

<span class="name">depart</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction</a></span>  
Departure maneuver, such as "Head towards".

<span class="name">arrive</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction</a></span>  
Arrival maneuver, such as "You have reached your destination/waypoint".

<span class="name">leftUTurn</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction</a></span>  
Left-hand U-turn maneuver, such as "Make a U-turn".

<span class="name">sharpLeftTurn</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction</a></span>  
Sharp left turn maneuver, such as "Turn sharply left".

<span class="name">leftTurn</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction</a></span>  
Left turn maneuver, such as "Turn left".

<span class="name">slightLeftTurn</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction</a></span>  
Slight left turn maneuver, such as "Turn slightly left".

<span class="name">continueOn</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction</a></span>  
Continue maneuver, such as "Continue straight ahead".

<span class="name">slightRightTurn</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction</a></span>  
Slight right turn maneuver, such as "Turn slightly right".

<span class="name">rightTurn</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction</a></span>  
Right turn maneuver, such as "Turn right".

<span class="name">sharpRightTurn</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction</a></span>  
Sharp right turn maneuver, such as "Turn sharply right".

<span class="name">rightUTurn</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction</a></span>  
Right u-turn maneuver, such as "Make a U-turn".

<span class="name">leftExit</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction</a></span>  
Left exit maneuver, such as "Take the exit".

<span class="name">rightExit</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction</a></span>  
Right exit maneuver, such as "Take the exit".

<span class="name">leftRamp</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction</a></span>  
Left ramp maneuver, such as "Join the highway".

<span class="name">rightRamp</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction</a></span>  
Right ramp maneuver, such as "Join the highway".

<span class="name">leftFork</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction</a></span>  
Left fork maneuver, such as "Keep left".

<span class="name">middleFork</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction</a></span>  
Middle fork maneuver, such as "Keep middle".

<span class="name">rightFork</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction</a></span>  
Right fork maneuver, such as "Keep right".

<span class="name">enterHighwayFromLeft</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction</a></span>  
Merge onto a highway from the left side. Such a maneuver occurs only in countries that drive on the left side of the road (left-hand traffic).

**Note:** This action is only generated when using the Navigate license. On top, until release of HERE SDK 4.16.0, it needs to be enabled via `RouteOptions`.

<span class="name">enterHighwayFromRight</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction</a></span>  
Merge onto a highway from the right side. Such a maneuver occurs only in countries that drive on the right side of the road (right-hand traffic).

**Note:** This action is only generated when using the Navigate license. On top, until release of HERE SDK 4.16.0, it needs to be enabled via `RouteOptions`.

<span class="name">leftRoundaboutEnter</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction</a></span>  
Roundabout maneuver (left-hand traffic), such as "Enter the roundabout".

<span class="name">rightRoundaboutEnter</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction</a></span>  
Roundabout maneuver (right-hand traffic), such as "Enter the roundabout".

<span class="name">leftRoundaboutPass</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction</a></span>  
Roundabout maneuver (left-hand traffic), such as "Pass the roundabout".

<span class="name">rightRoundaboutPass</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction</a></span>  
Roundabout maneuver (right-hand traffic), such as "Pass the roundabout".

<span class="name">leftRoundaboutExit1</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction</a></span>  
Roundabout maneuver (left-hand traffic), such as "Take the first exit at the roundabout".

<span class="name">leftRoundaboutExit2</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction</a></span>  
Roundabout maneuver (left-hand traffic), such as "Take the second exit at the roundabout".

<span class="name">leftRoundaboutExit3</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction</a></span>  
Roundabout maneuver (left-hand traffic), such as "Take the third exit at the roundabout".

<span class="name">leftRoundaboutExit4</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction</a></span>  
Roundabout maneuver (left-hand traffic), such as "Take the fourth exit at the roundabout".

<span class="name">leftRoundaboutExit5</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction</a></span>  
Roundabout maneuver (left-hand traffic), such as "Take the fifth exit at the roundabout".

<span class="name">leftRoundaboutExit6</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction</a></span>  
Roundabout maneuver (left-hand traffic), such as "Take the sixth exit at the roundabout".

<span class="name">leftRoundaboutExit7</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction</a></span>  
Roundabout maneuver (left-hand traffic), such as "Take the seventh exit at the roundabout".

<span class="name">leftRoundaboutExit8</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction</a></span>  
Roundabout maneuver (left-hand traffic), such as "Take the eighth exit at the roundabout".

<span class="name">leftRoundaboutExit9</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction</a></span>  
Roundabout maneuver (left-hand traffic), such as "Take the ninth exit at the roundabout".

<span class="name">leftRoundaboutExit10</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction</a></span>  
Roundabout maneuver (left-hand traffic), such as "Take the tenth exit at the roundabout".

<span class="name">leftRoundaboutExit11</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction</a></span>  
Roundabout maneuver (left-hand traffic), such as "Take the eleventh exit at the roundabout".

<span class="name">leftRoundaboutExit12</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction</a></span>  
Roundabout maneuver (left-hand traffic), such as "Take the twelfth exit at the roundabout".

<span class="name">rightRoundaboutExit1</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction</a></span>  
Roundabout maneuver (right-hand traffic), such as "Take the first exit at the roundabout".

<span class="name">rightRoundaboutExit2</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction</a></span>  
Roundabout maneuver (right-hand traffic), such as "Take the second exit at the roundabout".

<span class="name">rightRoundaboutExit3</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction</a></span>  
Roundabout maneuver (right-hand traffic), such as "Take the third exit at the roundabout".

<span class="name">rightRoundaboutExit4</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction</a></span>  
Roundabout maneuver (right-hand traffic), such as "Take the fourth exit at the roundabout".

<span class="name">rightRoundaboutExit5</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction</a></span>  
Roundabout maneuver (right-hand traffic), such as "Take the fifth exit at the roundabout".

<span class="name">rightRoundaboutExit6</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction</a></span>  
Roundabout maneuver (right-hand traffic), such as "Take the sixth exit at the roundabout".

<span class="name">rightRoundaboutExit7</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction</a></span>  
Roundabout maneuver (right-hand traffic), such as "Take the seventh exit at the roundabout".

<span class="name">rightRoundaboutExit8</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction</a></span>  
Roundabout maneuver (right-hand traffic), such as "Take the eighth exit at the roundabout".

<span class="name">rightRoundaboutExit9</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction</a></span>  
Roundabout maneuver (right-hand traffic), such as "Take the ninth exit at the roundabout".

<span class="name">rightRoundaboutExit10</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction</a></span>  
Roundabout maneuver (right-hand traffic), such as "Take the tenth exit at the roundabout".

<span class="name">rightRoundaboutExit11</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction</a></span>  
Roundabout maneuver (right-hand traffic), such as "Take the eleventh exit at the roundabout".

<span class="name">rightRoundaboutExit12</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction</a></span>  
Roundabout maneuver (right-hand traffic), such as "Take the twelfth exit at the roundabout".

## Properties

<span class="name"><a href="sdk-for-flutter-explore-routing-maneuveraction-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-maneuveraction-index">index</a></span> <span class="signature">→ int</span>  
A numeric identifier for the enumerated value.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-maneuveraction-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-routing-maneuveraction-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-maneuveraction-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-routing-maneuveraction-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Constants

<span class="name"><a href="sdk-for-flutter-explore-routing-maneuveraction-values-constant">values</a></span> <span class="signature">→ const List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-routing-maneuveraction">ManeuverAction</a></span>\></span></span>  
A constant List of the values in this enum, in order of their declaration.

</div>

<!-- /.main-content --> <!-- /.sidebar-offcanvas --> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
