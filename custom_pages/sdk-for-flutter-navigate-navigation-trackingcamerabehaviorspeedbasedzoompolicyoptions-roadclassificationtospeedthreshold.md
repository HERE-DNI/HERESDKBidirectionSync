---
title: "roadClassificationToSpeedThreshold property - TrackingCameraBehaviorSpeedBasedZoomPolicyOptions class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-trackingcamerabehaviorspeedbasedzoompolicyoptions-roadclassificationtospeedthreshold"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/TrackingCameraBehaviorSpeedBasedZoomPolicyOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">roadClassificationToSpeedThreshold</span> property

</div>

<div class="section multi-line-signature">

Map<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-roadclassification">RoadClassification</a></span>, <span class="type-parameter">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviorspeedthreshold-class">TrackingCameraBehaviorSpeedThreshold</a></span>\></span></span>\></span> <span class="name">roadClassificationToSpeedThreshold</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Defines, per road classification, how the zoom level should change in response to different vehicle speeds. If <a href="sdk-for-flutter-navigate-navigation-trackingcamerabehavior-defaultspeedbasedzoompolicyoptions">TrackingCameraBehavior.defaultSpeedBasedZoomPolicyOptions</a> is not used for <a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviorspeedbasedzoompolicyoptions-class">TrackingCameraBehaviorSpeedBasedZoomPolicyOptions</a>, it will be an empty map.

</div>

## Implementation

``` dart
Map<RoadClassification, List<TrackingCameraBehaviorSpeedThreshold>> roadClassificationToSpeedThreshold;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

