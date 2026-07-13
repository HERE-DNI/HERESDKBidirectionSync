---
title: "startAnimation method - MapMarker class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapmarker-startanimation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- startAnimation.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapMarker-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">startAnimation</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">startAnimation</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-startAnimation-param-animation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-animation-mapmarkeranimation-class">MapMarkerAnimation</a></span> <span class="parameter-name">animation</span>, </span>
2.  <span id="sdk-for-flutter-explore-startAnimation-param-animationListener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-animation-animationlistener-class">AnimationListener</a>?</span> <span class="parameter-name">animationListener</span></span>

)

</div>

<div class="section desc markdown">

Starts animation of this map marker according to provided <a href="sdk-for-flutter-explore-animation-mapmarkeranimation-class">MapMarkerAnimation</a>.

The `MapMarkerAnimation` may be shared between multiple instances of `MapMarker`.

Starting animation on one map marker does not influence any ongoing animations on other map markers. Any ongoing animation of this marker instance will get cancelled.

- `animation` The animation to start, may be used for multiple different map markers.

- `animationListener` The listener to receive notifications about animation start, completion or cancellation.

</div>

## Implementation

``` dart
void startAnimation(MapMarkerAnimation animation, AnimationListener? animationListener);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
