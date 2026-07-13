---
title: "PanListener constructor - PanListener - gestures library - Dart API"
slug: "sdk-for-flutter-navigate-gestures-panlistener-panlistener"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="gestures/PanListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">PanListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">PanListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onPanLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onPanLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-gestures-gesturestate">GestureState</a></span>, </span>
    2.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-point2d-class">Point2D</a></span>, </span>
    3.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-point2d-class">Point2D</a></span>, </span>
    4.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">double</span>, </span>

    )</span>

)

</div>

<div class="section desc markdown">

Abstract class for handling pan gestures.

Pan gesture occurs when a finger is moving on the screen.

</div>

## Implementation

``` dart
factory PanListener(
  void Function(GestureState, Point2D, Point2D, double) onPanLambda,

) => PanListener$Lambdas(
  onPanLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

