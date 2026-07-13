---
title: "onPinchRotate method - PinchRotateListener class - gestures library - Dart API"
slug: "sdk-for-flutter-explore-gestures-pinchrotatelistener-onpinchrotate"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="gestures/PinchRotateListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">onPinchRotate</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">onPinchRotate</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-onPinchRotate-param-state" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-gestures-gesturestate">GestureState</a></span> <span class="parameter-name">state</span>, </span>
2.  <span id="sdk-for-flutter-explore-onPinchRotate-param-pinchOrigin" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-point2d-class">Point2D</a></span> <span class="parameter-name">pinchOrigin</span>, </span>
3.  <span id="sdk-for-flutter-explore-onPinchRotate-param-rotationOrigin" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-point2d-class">Point2D</a></span> <span class="parameter-name">rotationOrigin</span>, </span>
4.  <span id="sdk-for-flutter-explore-onPinchRotate-param-twoFingerDistance" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">twoFingerDistance</span>, </span>
5.  <span id="sdk-for-flutter-explore-onPinchRotate-param-rotation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-angle-class">Angle</a></span> <span class="parameter-name">rotation</span>, </span>

)

</div>

<div class="section desc markdown">

Called when the pinch rotate gesture occurs.

- `state` Determines in which state the gesture is.

- `pinchOrigin` Position where the pinch happened relative to the MapView in pixels.

- `rotationOrigin` Position where the rotation happened relative to the MapView in pixels.

- `twoFingerDistance` Distance between the two fingers in pixels.

- `rotation` Fingers rotation angle delta. Indicates how much the fingers rotation angle has changed since the previous gesture update. Clockwise finger rotation gives positive deltas, counter clockwise finger rotation gives negative deltas.

</div>

## Implementation

``` dart
void onPinchRotate(GestureState state, Point2D pinchOrigin, Point2D rotationOrigin, double twoFingerDistance, Angle rotation);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

