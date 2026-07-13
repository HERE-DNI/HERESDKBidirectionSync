---
title: "Milestone.withType constructor - Milestone - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-milestone-milestone-withtype"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- Milestone.withType.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/Milestone-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">Milestone.withType</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">Milestone.withType</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-withType-param-sectionIndex" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">sectionIndex</span>, </span>
2.  <span id="sdk-for-flutter-navigate-withType-param-waypointIndex" class="parameter"><span class="type-annotation">int?</span> <span class="parameter-name">waypointIndex</span>, </span>
3.  <span id="sdk-for-flutter-navigate-withType-param-originalCoordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a>?</span> <span class="parameter-name">originalCoordinates</span>, </span>
4.  <span id="sdk-for-flutter-navigate-withType-param-mapMatchedCoordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">mapMatchedCoordinates</span>, </span>
5.  <span id="sdk-for-flutter-navigate-withType-param-type" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-milestonetype">MilestoneType</a></span> <span class="parameter-name">type</span>, </span>

)

</div>

<div class="section desc markdown">

Creates a new instance.

- `sectionIndex` Index of the section on the route.
- `waypointIndex` If present, this index corresponds to the waypoint in the original user-defined waypoint list. Otherwise this waypoint was added during route calculation by the system.
- `originalCoordinates` User-defined geographic coordinates. If not available, this waypoint was added during route calculation.
- `mapMatchedCoordinates` Map-matched geographic coordinates.
- `type` Type of this Milestone

</div>

## Implementation

``` dart
Milestone.withType(this.sectionIndex, this.waypointIndex, this.originalCoordinates, this.mapMatchedCoordinates, this.type);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
