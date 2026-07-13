---
title: "cameraBearingInDegrees property - FixedCameraBehavior class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-fixedcamerabehavior-camerabearingindegrees"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/FixedCameraBehavior-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">cameraBearingInDegrees</span> property

</div>

<div id="sdk-for-flutter-navigate-getter" class="section">

<div class="section multi-line-signature">

<span class="returntype">double?</span> <span class="name">cameraBearingInDegrees</span>

</div>

<div class="section desc markdown">

Camera bearing in degrees. Optional fixed bearing, from true North (0 degrees) in clockwise direction. The valid range is \[0, 360\]. If set, it will prevent the map from rotating to the direction of travel. For example, a value of zero results in "north up" mode. Defaults to `null`, which means the camera derives the bearing from the <a href="sdk-for-flutter-navigate-core-location-class">Location</a>, so that it points to the direction of travel. If this property is `null` and the device does not provide bearing, the last known value is used or zero otherwise. Gets the currently set fixed bearing.

</div>

## Implementation

``` dart
double? get cameraBearingInDegrees;
```

</div>

<div id="sdk-for-flutter-navigate-setter" class="section">

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">cameraBearingInDegrees=</span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-cameraBearingInDegrees-param-value" class="parameter"><span class="type-annotation">double?</span> <span class="parameter-name">value</span></span>)</span>

</div>

<div class="section desc markdown">

Camera bearing in degrees. Optional fixed bearing, from true North (0 degrees) in clockwise direction. The valid range is \[0, 360\]. If set, it will prevent the map from rotating to the direction of travel. For example, a value of zero results in "north up" mode. Defaults to `null`, which means the camera derives the bearing from the <a href="sdk-for-flutter-navigate-core-location-class">Location</a>, so that it points to the direction of travel. If this property is `null` and the device does not provide bearing, the last known value is used or zero otherwise. Sets an optional fixed bearing value, from true North (0 degrees) in clockwise direction.

</div>

## Implementation

``` dart
set cameraBearingInDegrees(double? value);
```

</pre>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

