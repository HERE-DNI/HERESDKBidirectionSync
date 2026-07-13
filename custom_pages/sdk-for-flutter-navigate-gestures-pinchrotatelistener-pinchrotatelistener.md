---
title: "PinchRotateListener constructor - PinchRotateListener - gestures library - Dart API"
slug: "sdk-for-flutter-navigate-gestures-pinchrotatelistener-pinchrotatelistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- PinchRotateListener.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="gestures/PinchRotateListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">PinchRotateListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">PinchRotateListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onPinchRotateLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onPinchRotateLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-gestures-gesturestate">GestureState</a></span>, </span>
    2.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-point2d-class">Point2D</a></span>, </span>
    3.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-point2d-class">Point2D</a></span>, </span>
    4.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">double</span>, </span>
    5.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-angle-class">Angle</a></span>, </span>

    )</span>

)

</div>

<div class="section desc markdown">

Abstract class for handling pinch rotate gestures.

Pinch rotate gesture occurs when two fingers are on the screen and at least one of them moves.

</div>

## Implementation

``` dart
factory PinchRotateListener(
  void Function(GestureState, Point2D, Point2D, double, Angle) onPinchRotateLambda,

) => PinchRotateListener$Lambdas(
  onPinchRotateLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
