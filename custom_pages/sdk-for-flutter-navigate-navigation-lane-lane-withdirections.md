---
title: "Lane.withDirections constructor - Lane - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-lane-lane-withdirections"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- Lane.withDirections.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/Lane-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">Lane.withDirections</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">Lane.withDirections</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-withDirections-param-type" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-lanetype-class">LaneType</a></span> <span class="parameter-name">type</span>, </span>
2.  <span id="sdk-for-flutter-navigate-withDirections-param-access" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-laneaccess-class">LaneAccess</a></span> <span class="parameter-name">access</span>, </span>
3.  <span id="sdk-for-flutter-navigate-withDirections-param-laneMarkings" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-lanemarkings-class">LaneMarkings</a></span> <span class="parameter-name">laneMarkings</span>, </span>
4.  <span id="sdk-for-flutter-navigate-withDirections-param-directions" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-lanedirection">LaneDirection</a></span>\></span></span> <span class="parameter-name">directions</span>, </span>
5.  <span id="sdk-for-flutter-navigate-withDirections-param-directionsOnRoute" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-lanedirection">LaneDirection</a></span>\></span></span> <span class="parameter-name">directionsOnRoute</span>, </span>

)

</div>

<div class="section desc markdown">

Creates a new instance.

- `type` Indicates the properties of this lane. For example, it indicates whether parking is allowed, if it is an acceleration lane, an express lane, or other attributes.
- `access` Indicates which vehicle types can access this lane.
- `laneMarkings` Indicates the lane markings between the lanes.
- `directions` Indicates all the lane directions that are available for this lane.
- `directionsOnRoute` Indicates the lane directions that are on the route. Following these directions keeps the driver on the route. This is a subset of <a href="sdk-for-flutter-navigate-navigation-lane-directions">Lane.directions</a>.

</div>

## Implementation

``` dart
Lane.withDirections(this.type, this.access, this.laneMarkings, this.directions, this.directionsOnRoute)
    : recommendationState = LaneRecommendationState.notRecommended;
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
