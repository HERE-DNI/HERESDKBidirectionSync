---
title: "createAnimationFromUpdateWithEasing method - MapCameraAnimationFactory class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapcameraanimationfactory-createanimationfromupdatewitheasing"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- createAnimationFromUpdateWithEasing.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapCameraAnimationFactory-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">createAnimationFromUpdateWithEasing</span> static method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-explore-mapview-mapcameraanimation-class">MapCameraAnimation</a></span> <span class="name">createAnimationFromUpdateWithEasing</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-createAnimationFromUpdateWithEasing-param-cameraUpdate" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapcameraupdate-class">MapCameraUpdate</a></span> <span class="parameter-name">cameraUpdate</span>, </span>
2.  <span id="sdk-for-flutter-explore-createAnimationFromUpdateWithEasing-param-duration" class="parameter"><span class="type-annotation">Duration</span> <span class="parameter-name">duration</span>, </span>
3.  <span id="sdk-for-flutter-explore-createAnimationFromUpdateWithEasing-param-easing" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-animation-easing-class">Easing</a></span> <span class="parameter-name">easing</span></span>

)

</div>

<div class="section desc markdown">

Creates a <a href="sdk-for-flutter-explore-mapview-mapcameraanimation-class">MapCameraAnimation</a> to gradually update the camera properties within a specified duration from its current values to the ones defined in the `MapCameraAnimationFactory.createAnimationFromUpdateWithEasing.cameraUpdate`.

`MapCameraAnimation` instances created from <a href="sdk-for-flutter-explore-mapview-mapcameraupdatefactory-compositeupdate">MapCameraUpdateFactory.compositeUpdate</a> instances are not supported. An <a href="sdk-for-flutter-explore-animation-animationlistener-class">AnimationListener</a> will receive an <a href="sdk-for-flutter-explore-animation-animationstate">AnimationState.cancelled</a> signal when trying to apply such animations.

- `cameraUpdate` Update which should be applied to the map camera.

- `duration` Duration of the animation. Negative duration results in no camera change when applied.

- `easing` Easing to apply.

Returns <a href="sdk-for-flutter-explore-mapview-mapcameraanimation-class">MapCameraAnimation</a>. MapCameraAnimation instance

</div>

## Implementation

``` dart
static MapCameraAnimation createAnimationFromUpdateWithEasing(MapCameraUpdate cameraUpdate, Duration duration, Easing easing) => $prototype.createAnimationFromUpdateWithEasing(cameraUpdate, duration, easing);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
