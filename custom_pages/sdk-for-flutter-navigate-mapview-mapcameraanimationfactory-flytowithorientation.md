---
title: "flyToWithOrientation method - MapCameraAnimationFactory class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapcameraanimationfactory-flytowithorientation"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapCameraAnimationFactory-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">flyToWithOrientation</span> static method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-mapview-mapcameraanimation-class">MapCameraAnimation</a></span> <span class="name">flyToWithOrientation</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-flyToWithOrientation-param-target" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinatesupdate-class">GeoCoordinatesUpdate</a></span> <span class="parameter-name">target</span>, </span>
2.  <span id="sdk-for-flutter-navigate-flyToWithOrientation-param-orientation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geoorientationupdate-class">GeoOrientationUpdate</a></span> <span class="parameter-name">orientation</span>, </span>
3.  <span id="sdk-for-flutter-navigate-flyToWithOrientation-param-bowFactor" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">bowFactor</span>, </span>
4.  <span id="sdk-for-flutter-navigate-flyToWithOrientation-param-duration" class="parameter"><span class="type-annotation">Duration</span> <span class="parameter-name">duration</span>, </span>

)

</div>

<div class="section desc markdown">

Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position and orientation along an adaptive ballistic curve.

The beginning and end of the animation will use the current zoom.

Note: The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.

- `target` The coordinates of the camera destination point. Any target sub-element value that is not finite will be set to the current camera target sub-element value. Note: The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.

- `orientation` The orientation at destination.

- `bowFactor` A bow factor that specifies how high (bowFactor \> 0) or low (bowFactor \< 0) the camera will fly.

The highest (bowFactor = 1) or lowest point (bowFactor = -1) of the ballistic animation curve is relative to the travel distance between current camera target and destination target.

A bow factor of 0 does not change the camera's zoom over time.

Values greater 0 result in a convex bow animation, values below 0 in a concave bowl animation.

The bow factor is clamped to \[-1, +1\].

Note that the lowest possible camera distance to earth is 0 meters and that the animation curve will not go below this value.

Note that currently, bow factor is ignored and assumed to be 1 if either start or end of animation has a non zero tilt.

- `duration` Duration of the flight. Negative duration results in no camera change when applied.

Returns <a href="sdk-for-flutter-navigate-mapview-mapcameraanimation-class">MapCameraAnimation</a>. MapCameraAnimation instance

</div>

## Implementation

``` dart
static MapCameraAnimation flyToWithOrientation(GeoCoordinatesUpdate target, GeoOrientationUpdate orientation, double bowFactor, Duration duration) => $prototype.flyToWithOrientation(target, orientation, bowFactor, duration);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

