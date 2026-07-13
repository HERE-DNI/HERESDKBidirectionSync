---
title: "normalizedPrincipalPointWithEasing method - MapCameraKeyframeTrack class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapcamerakeyframetrack-normalizedprincipalpointwitheasing"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapCameraKeyframeTrack-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">normalizedPrincipalPointWithEasing</span> static method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-mapview-mapcamerakeyframetrack-class">MapCameraKeyframeTrack</a></span> <span class="name">normalizedPrincipalPointWithEasing</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-normalizedPrincipalPointWithEasing-param-keyframes" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-animation-anchor2dkeyframe-class">Anchor2DKeyframe</a></span>\></span></span> <span class="parameter-name">keyframes</span>, </span>
2.  <span id="sdk-for-flutter-navigate-normalizedPrincipalPointWithEasing-param-easing" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-animation-easing-class">Easing</a></span> <span class="parameter-name">easing</span>, </span>
3.  <span id="sdk-for-flutter-navigate-normalizedPrincipalPointWithEasing-param-interpolationMode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-animation-keyframeinterpolationmode">KeyframeInterpolationMode</a></span> <span class="parameter-name">interpolationMode</span></span>

)

</div>

<div class="section desc markdown">

Creates a map camera principal point keyframe track.

It enables animations on the point where the map camera's target is placed in normalized view coordinates. (0,0) is top left of the viewport, (1, 1) is bottom right.

- `keyframes` The list of keyframes that specify how the camera property is changed. Point values must be in normalized screen coordinates with origin (0,0) in the top left and (1,1) in the bottom right of the viewport. Point values outside of viewport boundaries will be clamped to the viewport boundaries during animation. Keyframe time offsets are considered to be relative to the previous keyframe in the list or relative to the start of the animation if the current keyframe is first in the list. Time offset of the first keyframe in the list should be 0, otherwise an error occurs and creation of the keyframe track will fail.

- `easing` The easing to apply during keyframe interpolation.

- `interpolationMode` The type of interpolation done between keyframe values.

Returns <a href="sdk-for-flutter-navigate-mapview-mapcamerakeyframetrack-class">MapCameraKeyframeTrack</a>. A keyframe track over the principal point.

Throws <a href="sdk-for-flutter-navigate-mapview-mapcamerakeyframetrackinstantiationexception-class">MapCameraKeyframeTrackInstantiationException</a>. Indicates an instantiation issue.

</div>

## Implementation

``` dart
static MapCameraKeyframeTrack normalizedPrincipalPointWithEasing(List<Anchor2DKeyframe> keyframes, Easing easing, KeyframeInterpolationMode interpolationMode) => $prototype.normalizedPrincipalPointWithEasing(keyframes, easing, interpolationMode);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

