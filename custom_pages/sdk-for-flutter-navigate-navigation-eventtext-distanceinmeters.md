---
title: "distanceInMeters property - EventText class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-eventtext-distanceinmeters"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/EventText-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">distanceInMeters</span> property

</div>

<div class="section multi-line-signature">

double <span class="name">distanceInMeters</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Distance in meters to the location of the event for which the text notification is given.

**Note:** For greater distances, distance in kilometers is rounded to the nearest digit (0.5 or greater rounds up, else down) to simplify the distance phrase in `ManeuverNotifications` texts during navigation. Distance in miles is rounded to the nearest 0.5 step. For example, 3.5 kilometers are rounded to 4 kilometers and the notification will begin with `After 4 kilometers...`. However, 3.5 miles are not rounded up and the notification will begin with `After three and a half miles...`. Same for 3.7 miles, whereas 3.8 miles are rounded to 4 miles. Note that the measurement units itself are defined in the `UnitSystem` class.

</div>

## Implementation

``` dart
double distanceInMeters;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

