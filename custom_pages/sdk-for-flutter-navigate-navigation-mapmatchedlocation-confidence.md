---
title: "confidence property - MapMatchedLocation class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-mapmatchedlocation-confidence"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/MapMatchedLocation-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">confidence</span> property

</div>

<div class="section multi-line-signature">

double <span class="name">confidence</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Confidence level (between 0 and 1) of the matched location. A low confidence value means that the map-matched vehicle location is not reliable and it may not be clear which part of the road the vehicle has taken. This can happen when the accuracy or frequency of the provided location updates is poor. If the confidence level is too small then, for example, overspeed warnings may be also inaccurate.

</div>

## Implementation

``` dart
double confidence;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

