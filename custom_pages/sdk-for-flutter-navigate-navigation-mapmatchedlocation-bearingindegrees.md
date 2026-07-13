---
title: "bearingInDegrees property - MapMatchedLocation class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-mapmatchedlocation-bearingindegrees"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- bearingInDegrees.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/MapMatchedLocation-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">bearingInDegrees</span> property

</div>

<div class="section multi-line-signature">

double? <span class="name">bearingInDegrees</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

The bearing orientation points to the direction of travel, and has the same angle as the street where it is matched to. Therefore, it must not necessarily be the same as the bearing of a location source. Starts at 0 in the geographic north and rotates in a clockwise direction around the compass. It means that for going north it's equal to 0, for northeast it's equal to 45, for east it's equal to 90, and so on. If it cannot be determined, the value is `null`. Otherwise, it is guaranteed to be in the range \[0, 360).

</div>

## Implementation

``` dart
double? bearingInDegrees;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
