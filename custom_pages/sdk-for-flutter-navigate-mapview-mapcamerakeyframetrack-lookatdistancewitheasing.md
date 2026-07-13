---
title: "lookAtDistanceWithEasing method - MapCameraKeyframeTrack class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapcamerakeyframetrack-lookatdistancewitheasing"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapCameraKeyframeTrack-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">lookAtDistanceWithEasing</span> static method

</div>

<div class="section multi-line-signature">

<div>

1.  @Deprecated("Will be removed in v4.27.0. Use \[MapCameraKeyframeTrack.lookAtDistanceWithKind\] instead.")

</div>

<span class="returntype"><a href="sdk-for-flutter-navigate-mapview-mapcamerakeyframetrack-class">MapCameraKeyframeTrack</a></span> <span class="name deprecated">lookAtDistanceWithEasing</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-lookAtDistanceWithEasing-param-keyframes" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-animation-scalarkeyframe-class">ScalarKeyframe</a></span>\></span></span> <span class="parameter-name">keyframes</span>, </span>
2.  <span id="sdk-for-flutter-navigate-lookAtDistanceWithEasing-param-easing" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-animation-easing-class">Easing</a></span> <span class="parameter-name">easing</span>, </span>
3.  <span id="sdk-for-flutter-navigate-lookAtDistanceWithEasing-param-interpolationMode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-animation-keyframeinterpolationmode">KeyframeInterpolationMode</a></span> <span class="parameter-name">interpolationMode</span></span>

)

</div>

<div class="section desc markdown">

Creates a map camera look-at distance keyframe track.

It enables animations of the distance from the map camera to the target point that the camera looks at in meters. The values will be clamped according to the minimum and maximum zoom levels set for the map camera.

- `keyframes` The list of keyframes that specify how the camera property is changed. Keyframe time offsets are considered to be relative to the previous keyframe in the list or relative to the start of the animation if the current keyframe is first in the list. Time offset of the first keyframe in the list should be 0, otherwise an error occurs and creation of the keyframe track will fail.

- `easing` The easing to apply during keyframe interpolation.

- `interpolationMode` The type of interpolation done between keyframe values.

Returns <a href="sdk-for-flutter-navigate-mapview-mapcamerakeyframetrack-class">MapCameraKeyframeTrack</a>. A keyframe track over the distance from the map camera to its target.

Throws <a href="sdk-for-flutter-navigate-mapview-mapcamerakeyframetrackinstantiationexception-class">MapCameraKeyframeTrackInstantiationException</a>. Indicates an instantiation issue.

</div>

## Implementation

``` dart
@Deprecated("Will be removed in v4.27.0. Use [MapCameraKeyframeTrack.lookAtDistanceWithKind] instead.")

static MapCameraKeyframeTrack lookAtDistanceWithEasing(List<ScalarKeyframe> keyframes, Easing easing, KeyframeInterpolationMode interpolationMode) => $prototype.lookAtDistanceWithEasing(keyframes, easing, interpolationMode);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

