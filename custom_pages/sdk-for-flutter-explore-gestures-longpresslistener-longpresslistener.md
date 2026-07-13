---
title: "LongPressListener constructor - LongPressListener - gestures library - Dart API"
slug: "sdk-for-flutter-explore-gestures-longpresslistener-longpresslistener"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="gestures/LongPressListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">LongPressListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">LongPressListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-param-onLongPressLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onLongPressLambda</span>(</span>
    1.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-gestures-gesturestate">GestureState</a></span>, </span>
    2.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-point2d-class">Point2D</a></span></span>

    )</span>

)

</div>

<div class="section desc markdown">

Abstract class for handling long-press gestures.

Long-press gesture occurs after tapping and holding the finger for a long time on the screen.

</div>

## Implementation

``` dart
factory LongPressListener(
  void Function(GestureState, Point2D) onLongPressLambda,

) => LongPressListener$Lambdas(
  onLongPressLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

