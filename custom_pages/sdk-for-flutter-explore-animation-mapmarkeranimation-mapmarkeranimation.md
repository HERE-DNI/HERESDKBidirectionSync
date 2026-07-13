---
title: "MapMarkerAnimation constructor - MapMarkerAnimation - animation library - Dart API"
slug: "sdk-for-flutter-explore-animation-mapmarkeranimation-mapmarkeranimation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapMarkerAnimation.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="animation/MapMarkerAnimation-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">MapMarkerAnimation</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">MapMarkerAnimation</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-param-track" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-animation-mapitemkeyframetrack-class">MapItemKeyFrameTrack</a></span> <span class="parameter-name">track</span></span>

)

</div>

<div class="section desc markdown">

Creates an animation of <a href="sdk-for-flutter-explore-mapview-mapmarker-class">MapMarker</a> based on provided keyframe track.

Supports tracks created with <a href="sdk-for-flutter-explore-animation-mapitemkeyframetrack-class">MapItemKeyFrameTrack</a> 'moveTo\*' methods.

For starting the animation see <a href="sdk-for-flutter-explore-mapview-mapmarker-startanimation">MapMarker.startAnimation</a>.

- `track` The track holding the keyframes for the animation.

Throws <a href="sdk-for-flutter-explore-animation-mapmarkeranimationinstantiationexception-class">MapMarkerAnimationInstantiationException</a>. If the specified keyframe track cannot be used to create animation of a <a href="sdk-for-flutter-explore-mapview-mapmarker-class">MapMarker</a>.

</div>

## Implementation

``` dart
factory MapMarkerAnimation(MapItemKeyFrameTrack track) => $prototype.$init(track);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
