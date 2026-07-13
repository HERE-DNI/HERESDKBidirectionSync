---
title: "JunctionViewLaneAssistance constructor - JunctionViewLaneAssistance - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-junctionviewlaneassistance"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/JunctionViewLaneAssistance-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">JunctionViewLaneAssistance</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">JunctionViewLaneAssistance</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-lanesForNextJunction" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-lane-class">Lane</a></span>\></span></span> <span class="parameter-name">lanesForNextJunction</span>, </span>
2.  <span id="sdk-for-flutter-navigate-param-distanceToJunctionInMeters" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">distanceToJunctionInMeters</span></span>

)

</div>

<div class="section desc markdown">

Creates a new instance.

- `lanesForNextJunction` A list of lanes on the next complex junction. The lanes are sorted from left to right: The lane at index 0 represents the leftmost lane and the last index represents the rightmost lane. This is valid for right-hand and left-hand driving countries. An empty list means that the complex junction has been passed and that the lane information is not valid anymore. Exactly one event with a non-empty list is delivered before reaching a complex junction and one event with an empty list afterwards.

**Note:** Lanes going in opposite direction are not included in the list.

- `distanceToJunctionInMeters` Distance to the next complex junction in meters.

</div>

## Implementation

``` dart
JunctionViewLaneAssistance(this.lanesForNextJunction, this.distanceToJunctionInMeters);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

