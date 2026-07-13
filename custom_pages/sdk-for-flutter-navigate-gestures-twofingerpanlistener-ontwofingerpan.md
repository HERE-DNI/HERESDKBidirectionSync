---
title: "onTwoFingerPan method - TwoFingerPanListener class - gestures library - Dart API"
slug: "sdk-for-flutter-navigate-gestures-twofingerpanlistener-ontwofingerpan"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="gestures/TwoFingerPanListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">onTwoFingerPan</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">onTwoFingerPan</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-onTwoFingerPan-param-state" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-gestures-gesturestate">GestureState</a></span> <span class="parameter-name">state</span>, </span>
2.  <span id="sdk-for-flutter-navigate-onTwoFingerPan-param-origin" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-point2d-class">Point2D</a></span> <span class="parameter-name">origin</span>, </span>
3.  <span id="sdk-for-flutter-navigate-onTwoFingerPan-param-translation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-point2d-class">Point2D</a></span> <span class="parameter-name">translation</span>, </span>
4.  <span id="sdk-for-flutter-navigate-onTwoFingerPan-param-velocity" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">velocity</span>, </span>

)

</div>

<div class="section desc markdown">

Called when the two finger pan gesture occurs.

- `state` Determines in which state the gesture is.

- `origin` Position halfway between two touch points relative to the MapView in pixels.

- `translation` Translation offset since the last position in pixels.

- `velocity` Velocity of panning in pixels per millisecond.

</div>

## Implementation

``` dart
void onTwoFingerPan(GestureState state, Point2D origin, Point2D translation, double velocity);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

