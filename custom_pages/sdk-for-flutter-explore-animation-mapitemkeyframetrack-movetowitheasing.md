---
title: "moveToWithEasing method - MapItemKeyFrameTrack class - animation library - Dart API"
slug: "sdk-for-flutter-explore-animation-mapitemkeyframetrack-movetowitheasing"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="animation/MapItemKeyFrameTrack-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">moveToWithEasing</span> static method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-explore-animation-mapitemkeyframetrack-class">MapItemKeyFrameTrack</a></span> <span class="name">moveToWithEasing</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-moveToWithEasing-param-keyframes" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-animation-geocoordinateskeyframe-class">GeoCoordinatesKeyframe</a></span>\></span></span> <span class="parameter-name">keyframes</span>, </span>
2.  <span id="sdk-for-flutter-explore-moveToWithEasing-param-easing" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-animation-easing-class">Easing</a></span> <span class="parameter-name">easing</span>, </span>
3.  <span id="sdk-for-flutter-explore-moveToWithEasing-param-interpolationMode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-animation-keyframeinterpolationmode">KeyframeInterpolationMode</a></span> <span class="parameter-name">interpolationMode</span></span>

)

</div>

<div class="section desc markdown">

Creates a map item position keyframe track.

It enables animations over the geographical coordinates where the map item is positioned.

- `keyframes` The list of keyframes that specify how the map item position changes over time.

- `easing` The easing to apply during keyframe interpolation.

- `interpolationMode` The type of interpolation done between keyframe values.

Returns <a href="sdk-for-flutter-explore-animation-mapitemkeyframetrack-class">MapItemKeyFrameTrack</a>. MapItemKeyFrameTrack instance.

Throws <a href="sdk-for-flutter-explore-animation-mapitemkeyframetrackinstantiationexception-class">MapItemKeyFrameTrackInstantiationException</a>. If the supplied keyframe list is empty or first keyframe duration is not 0.

</div>

## Implementation

``` dart
static MapItemKeyFrameTrack moveToWithEasing(List<GeoCoordinatesKeyframe> keyframes, Easing easing, KeyframeInterpolationMode interpolationMode) => $prototype.moveToWithEasing(keyframes, easing, interpolationMode);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

