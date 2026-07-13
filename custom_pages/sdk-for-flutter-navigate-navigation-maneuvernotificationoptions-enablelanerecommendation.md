---
title: "enableLaneRecommendation property - ManeuverNotificationOptions class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-enablelanerecommendation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- enableLaneRecommendation.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/ManeuverNotificationOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">enableLaneRecommendation</span> property

</div>

<div class="section multi-line-signature">

bool <span class="name">enableLaneRecommendation</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

A flag that indicates whether lane recommendation should be used when generating notifications. In case the flag is enabled, *only* the notification for the <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationtype">ManeuverNotificationType.distance</a> maneuver notification type will contain the lane recommendation. The lane recommandation will replace the direction information in the notification. **Example:** 'After 250 meters use the right two lanes and turn right.'. Defaults to `false`.

</div>

## Implementation

``` dart
bool enableLaneRecommendation;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
