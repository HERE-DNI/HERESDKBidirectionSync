---
title: "startAnimation method - MapPolyline class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mappolyline-startanimation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- startAnimation.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapPolyline-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">startAnimation</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">startAnimation</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-startAnimation-param-animation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-animation-mappolylineanimation-class">MapPolylineAnimation</a></span> <span class="parameter-name">animation</span>, </span>
2.  <span id="sdk-for-flutter-navigate-startAnimation-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-animation-animationlistener-class">AnimationListener</a></span> <span class="parameter-name">listener</span></span>

)

</div>

<div class="section desc markdown">

Starts an animation of this map polyline.

The `MapPolylineAnimation` may be shared between multiple instances of `MapPolyline`.

Starting animation on one polyline does not influence any ongoing animations on other polylines. Any ongoing animation of this map polyline will get cancelled.

- `animation` The animation to start.

- `listener` The listener to receive notifications about animation start, completion or cancellation.

</div>

## Implementation

``` dart
void startAnimation(MapPolylineAnimation animation, AnimationListener listener);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
