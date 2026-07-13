---
title: "fieldOfViewWithEasing method - MapCameraKeyframeTrack class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-fieldofviewwitheasing"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- fieldOfViewWithEasing.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapCameraKeyframeTrack-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">fieldOfViewWithEasing</span> static method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-class">MapCameraKeyframeTrack</a></span> <span class="name">fieldOfViewWithEasing</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-fieldOfViewWithEasing-param-keyframes" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-animation-scalarkeyframe-class">ScalarKeyframe</a></span>\></span></span> <span class="parameter-name">keyframes</span>, </span>
2.  <span id="sdk-for-flutter-explore-fieldOfViewWithEasing-param-easing" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-animation-easing-class">Easing</a></span> <span class="parameter-name">easing</span>, </span>
3.  <span id="sdk-for-flutter-explore-fieldOfViewWithEasing-param-interpolationMode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-animation-keyframeinterpolationmode">KeyframeInterpolationMode</a></span> <span class="parameter-name">interpolationMode</span></span>

)

</div>

<div class="section desc markdown">

Creates a map camera field-of-view keyframe track.

It enables animations over the angle of the field of view captured by the map camera in degrees. Values will be clamped to a range from 1 to 150.

- `keyframes` The list of keyframes that specify how the camera property is changed. Keyframe time offsets are considered to be relative to the previous keyframe in the list or relative to the start of the animation if the current keyframe is first in the list. Time offset of the first keyframe in the list should be 0, otherwise an error occurs and creation of the keyframe track will fail.

- `easing` The easing to apply during keyframe interpolation.

- `interpolationMode` The type of interpolation done between keyframe values.

Returns <a href="sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-class">MapCameraKeyframeTrack</a>. A keyframe track over the map camera field-of-view.

Throws <a href="sdk-for-flutter-explore-mapview-mapcamerakeyframetrackinstantiationexception-class">MapCameraKeyframeTrackInstantiationException</a>. Indicates an instantiation issue.

</div>

## Implementation

``` dart
static MapCameraKeyframeTrack fieldOfViewWithEasing(List<ScalarKeyframe> keyframes, Easing easing, KeyframeInterpolationMode interpolationMode) => $prototype.fieldOfViewWithEasing(keyframes, easing, interpolationMode);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
