---
title: "TwoFingerPanListener constructor - TwoFingerPanListener - gestures library - Dart API"
slug: "sdk-for-flutter-explore-gestures-twofingerpanlistener-twofingerpanlistener"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="gestures/TwoFingerPanListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">TwoFingerPanListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">TwoFingerPanListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-param-onTwoFingerPanLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onTwoFingerPanLambda</span>(</span>
    1.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-gestures-gesturestate">GestureState</a></span>, </span>
    2.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-point2d-class">Point2D</a></span>, </span>
    3.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-point2d-class">Point2D</a></span>, </span>
    4.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation">double</span>, </span>

    )</span>

)

</div>

<div class="section desc markdown">

Abstract class for handling two finger pan gestures.

Two finger pan gesture occurs when two fingers are on the screen and both of them are moving vertically.

</div>

## Implementation

``` dart
factory TwoFingerPanListener(
  void Function(GestureState, Point2D, Point2D, double) onTwoFingerPanLambda,

) => TwoFingerPanListener$Lambdas(
  onTwoFingerPanLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

