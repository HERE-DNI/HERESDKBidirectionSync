---
title: "polylineProgressWithEasing method - MapItemKeyFrameTrack class - animation library - Dart API"
slug: "sdk-for-flutter-navigate-animation-mapitemkeyframetrack-polylineprogresswitheasing"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="animation/MapItemKeyFrameTrack-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">polylineProgressWithEasing</span> static method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-animation-mapitemkeyframetrack-class">MapItemKeyFrameTrack</a></span> <span class="name">polylineProgressWithEasing</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-polylineProgressWithEasing-param-keyframes" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-animation-scalarkeyframe-class">ScalarKeyframe</a></span>\></span></span> <span class="parameter-name">keyframes</span>, </span>
2.  <span id="sdk-for-flutter-navigate-polylineProgressWithEasing-param-easing" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-animation-easing-class">Easing</a></span> <span class="parameter-name">easing</span>, </span>
3.  <span id="sdk-for-flutter-navigate-polylineProgressWithEasing-param-interpolationMode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-animation-keyframeinterpolationmode">KeyframeInterpolationMode</a></span> <span class="parameter-name">interpolationMode</span></span>

)

</div>

<div class="section desc markdown">

Creates a keyframe track used to animate the progress of a polyline.

Each scalar keyframe specifies the value of <a href="sdk-for-flutter-navigate-mapview-mappolyline-progress">MapPolyline.progress</a> at key points of the animation.

- `keyframes` The list of keyframes that specify how the polyline progress changes over time.

- `easing` The easing to apply during keyframe interpolation.

- `interpolationMode` The type of interpolation done between keyframe values.

Returns <a href="sdk-for-flutter-navigate-animation-mapitemkeyframetrack-class">MapItemKeyFrameTrack</a>. MapItemKeyFrameTrack instance.

Throws <a href="sdk-for-flutter-navigate-animation-mapitemkeyframetrackinstantiationexception-class">MapItemKeyFrameTrackInstantiationException</a>. If the supplied keyframe list is empty or first keyframe duration is not 0.

</div>

## Implementation

``` dart
static MapItemKeyFrameTrack polylineProgressWithEasing(List<ScalarKeyframe> keyframes, Easing easing, KeyframeInterpolationMode interpolationMode) => $prototype.polylineProgressWithEasing(keyframes, easing, interpolationMode);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

