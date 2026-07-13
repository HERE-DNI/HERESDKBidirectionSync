---
title: "lookAtOrientationWithEasing method - MapCameraKeyframeTrack class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapcamerakeyframetrack-lookatorientationwitheasing"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lookAtOrientationWithEasing.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapCameraKeyframeTrack-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">lookAtOrientationWithEasing</span> static method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-mapview-mapcamerakeyframetrack-class">MapCameraKeyframeTrack</a></span> <span class="name">lookAtOrientationWithEasing</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-lookAtOrientationWithEasing-param-keyframes" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-animation-geoorientationkeyframe-class">GeoOrientationKeyframe</a></span>\></span></span> <span class="parameter-name">keyframes</span>, </span>
2.  <span id="sdk-for-flutter-navigate-lookAtOrientationWithEasing-param-easing" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-animation-easing-class">Easing</a></span> <span class="parameter-name">easing</span>, </span>
3.  <span id="sdk-for-flutter-navigate-lookAtOrientationWithEasing-param-interpolationMode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-animation-keyframeinterpolationmode">KeyframeInterpolationMode</a></span> <span class="parameter-name">interpolationMode</span></span>

)

</div>

<div class="section desc markdown">

Creates a map camera look-at orientation keyframe track.

It enables animations over the orientation of the map camera target (bearing and tilt).

- `keyframes` The list of keyframes that specify how the camera property is changed. Keyframe time offsets are considered to be relative to the previous keyframe in the list or relative to the start of the animation if the current keyframe is first in the list. Time offset of the first keyframe in the list should be 0, otherwise an error occurs and creation of the keyframe track will fail.

- `easing` The easing to apply during keyframe interpolation.

- `interpolationMode` The type of interpolation done between keyframe values.

Returns <a href="sdk-for-flutter-navigate-mapview-mapcamerakeyframetrack-class">MapCameraKeyframeTrack</a>. A keyframe track over the map camera target orientation.

Throws <a href="sdk-for-flutter-navigate-mapview-mapcamerakeyframetrackinstantiationexception-class">MapCameraKeyframeTrackInstantiationException</a>. Indicates an instantiation issue.

</div>

## Implementation

``` dart
static MapCameraKeyframeTrack lookAtOrientationWithEasing(List<GeoOrientationKeyframe> keyframes, Easing easing, KeyframeInterpolationMode interpolationMode) => $prototype.lookAtOrientationWithEasing(keyframes, easing, interpolationMode);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
