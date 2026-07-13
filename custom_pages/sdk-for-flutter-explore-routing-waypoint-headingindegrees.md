---
title: "headingInDegrees property - Waypoint class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-waypoint-headingindegrees"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- headingInDegrees.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/Waypoint-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">headingInDegrees</span> property

</div>

<div class="section multi-line-signature">

double? <span class="name">headingInDegrees</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Optional heading angle referenced by true North, clockwise specifying the direction of travel. The heading direction may help the routing algorithm to select the best direction, for example, when multiple directions are possible at a road junction. North is 0 degrees, East is 90 degrees, South is 180 degrees, and West is 270 degrees. The value must be in the range \[0, 360\] when specified. By default, or when `null` is set, heading is ignored for route calculation.

</div>

## Implementation

``` dart
double? headingInDegrees;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
