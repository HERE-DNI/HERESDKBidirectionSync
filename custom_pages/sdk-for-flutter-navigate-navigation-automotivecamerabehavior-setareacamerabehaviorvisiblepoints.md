---
title: "setAreaCameraBehaviorVisiblePoints method - AutomotiveCameraBehavior class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-automotivecamerabehavior-setareacamerabehaviorvisiblepoints"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/AutomotiveCameraBehavior-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">setAreaCameraBehaviorVisiblePoints</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">setAreaCameraBehaviorVisiblePoints</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-setAreaCameraBehaviorVisiblePoints-param-points" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span>\></span></span> <span class="parameter-name">points</span>, </span>
2.  <span id="sdk-for-flutter-navigate-setAreaCameraBehaviorVisiblePoints-param-includeCurrentPosition" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">includeCurrentPosition</span></span>

)

</div>

<div class="section desc markdown">

Configures the Area camera to frame the specified points.

The camera calculates the optimal zoom level and center position to display all provided coordinates within the viewport. Use this for showing a single point of interest or multiple points such as safety cameras.

This function does not change <a href="sdk-for-flutter-navigate-navigation-automotivecamerabehavior-activecameratype">AutomotiveCameraBehavior.activeCameraType</a>. To display the configured area view, set <a href="sdk-for-flutter-navigate-navigation-automotivecamerabehavior-activecameratype">AutomotiveCameraBehavior.activeCameraType</a> to <a href="sdk-for-flutter-navigate-navigation-automotivecamerabehavioractivecameratype">AutomotiveCameraBehaviorActiveCameraType.area</a>.

Calling this function overrides any previously set geographic bounding box configured via <a href="sdk-for-flutter-navigate-navigation-automotivecamerabehavior-setareacamerabehaviorgeobox">AutomotiveCameraBehavior.setAreaCameraBehaviorGeobox</a>.

- `points` The list of geographic coordinates to display.

- `includeCurrentPosition` When true, the current vehicle position is included in the visible area calculation, ensuring the vehicle remains visible alongside the provided points.

</div>

## Implementation

``` dart
void setAreaCameraBehaviorVisiblePoints(List<GeoCoordinates> points, bool includeCurrentPosition);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

