---
title: "lanes property - CurrentSituationLaneAssistanceView class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-currentsituationlaneassistanceview-lanes"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/CurrentSituationLaneAssistanceView-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">lanes</span> property

</div>

<div class="section multi-line-signature">

List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-currentsituationlaneview-class">CurrentSituationLaneView</a></span>\></span> <span class="name">lanes</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

A list of lanes on the current road. The lanes are sorted from left to right: The lane at index 0 represents the leftmost lane and the last index represents the rightmost lane. This is valid for right-hand and left-hand driving countries. Empty list means unavailability of lane data for the current location.

The left to right order is in the travel direction. Only the lanes for the current driving direction are included.

**Note:** Lanes going in opposite direction are not included in the list.

</div>

## Implementation

``` dart
List<CurrentSituationLaneView> lanes;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

