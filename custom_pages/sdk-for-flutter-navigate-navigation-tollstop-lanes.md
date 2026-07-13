---
title: "lanes property - TollStop class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-tollstop-lanes"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/TollStop-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">lanes</span> property

</div>

<div class="section multi-line-signature">

List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-tollboothlane-class">TollBoothLane</a></span>\></span> <span class="name">lanes</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Describes the features of the booth for the lane. The lanes are sorted from left to right: The lane at index 0 represents the leftmost lane and the last index represents the rightmost lane. This is valid for right-hand and left-hand driving countries. An empty list means that the complex junction has been passed and that the lane information is not valid anymore. Exactly one event with a non-empty list is delivered before reaching a complex junction and one event with an empty list afterwards.

**Note:** Lanes going in opposite direction are not included in the list.

</div>

## Implementation

``` dart
List<TollBoothLane> lanes;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

