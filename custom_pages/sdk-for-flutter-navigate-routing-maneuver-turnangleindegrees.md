---
title: "turnAngleInDegrees property - Maneuver class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-maneuver-turnangleindegrees"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- turnAngleInDegrees.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/Maneuver-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">turnAngleInDegrees</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype">double?</span> <span class="name">turnAngleInDegrees</span>

</div>

<div class="section desc markdown">

The angle of the turn component of the maneuver. The angle increases clockwise and small values are used for going straight, i.e. a positive number means there is a right turn and a negative number is a left turn. Some maneuvers like Depart, Arrive and Roundabout pass doesn't have a well defined angle, so the value is omitted. **Note:** These attributes are only available for the Navigate license. Gets the angle of the turn component of the maneuver. The value is in degrees and from -180 to 180.

</div>

## Implementation

``` dart
double? get turnAngleInDegrees;
```

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
