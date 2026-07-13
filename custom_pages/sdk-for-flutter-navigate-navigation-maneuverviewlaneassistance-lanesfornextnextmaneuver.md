---
title: "lanesForNextNextManeuver property - ManeuverViewLaneAssistance class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-lanesfornextnextmaneuver"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/ManeuverViewLaneAssistance-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">lanesForNextNextManeuver</span> property

</div>

<div class="section multi-line-signature">

List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-lane-class">Lane</a></span>\></span> <span class="name">lanesForNextNextManeuver</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

A list of lanes on the road that leads to the maneuver after the upcoming maneuver. The lanes are sorted from left to right: The lane at index 0 represents the leftmost lane and the last index represents the rightmost lane. This is valid for both right-hand and left-hand driving countries. Contraflow lanes are not included in the list. <a href="sdk-for-flutter-navigate-navigation-roadattributes-isrightdrivingside">RoadAttributes.isRightDrivingSide</a> indicates if this is a left-hand driving country or not. By default, this list is empty. It will be filled when the next two maneuvers are too close to each other, or when the next two maneuvers are roundabout maneuvers. Note: This notification is delivered at the same time as the <a href="sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-lanesfornextmaneuver">ManeuverViewLaneAssistance.lanesForNextManeuver</a>. There is no separate maneuver notification on the second maneuver when two maneuvers are are too close to each other.

</div>

## Implementation

``` dart
List<Lane> lanesForNextNextManeuver;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

