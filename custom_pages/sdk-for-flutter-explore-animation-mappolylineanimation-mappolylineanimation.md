---
title: "MapPolylineAnimation constructor - MapPolylineAnimation - animation library - Dart API"
slug: "sdk-for-flutter-explore-animation-mappolylineanimation-mappolylineanimation"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="animation/MapPolylineAnimation-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">MapPolylineAnimation</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">MapPolylineAnimation</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-param-track" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-animation-mapitemkeyframetrack-class">MapItemKeyFrameTrack</a></span> <span class="parameter-name">track</span></span>

)

</div>

<div class="section desc markdown">

Creates an animation of <a href="sdk-for-flutter-explore-mapview-mappolyline-class">MapPolyline</a> based on provided keyframe track.

Supports tracks created with <a href="sdk-for-flutter-explore-animation-mapitemkeyframetrack-class">MapItemKeyFrameTrack</a> 'polylineProgress\*' methods. For starting the animation, see <a href="sdk-for-flutter-explore-mapview-mappolyline-startanimation">MapPolyline.startAnimation</a>.

- `track` The track holding the keyframes for the animation.

Throws <a href="sdk-for-flutter-explore-animation-mappolylineanimationinstantiationexception-class">MapPolylineAnimationInstantiationException</a>. If the specified keyframe track cannot be used to create animation of a <a href="sdk-for-flutter-explore-mapview-mappolyline-class">MapPolyline</a>.

</div>

## Implementation

``` dart
factory MapPolylineAnimation(MapItemKeyFrameTrack track) => $prototype.$init(track);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

