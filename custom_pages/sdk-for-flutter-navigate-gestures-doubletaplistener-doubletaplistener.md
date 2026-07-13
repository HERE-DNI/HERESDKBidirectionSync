---
title: "DoubleTapListener constructor - DoubleTapListener - gestures library - Dart API"
slug: "sdk-for-flutter-navigate-gestures-doubletaplistener-doubletaplistener"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="gestures/DoubleTapListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">DoubleTapListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">DoubleTapListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onDoubleTapLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onDoubleTapLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-point2d-class">Point2D</a></span></span>

    )</span>

)

</div>

<div class="section desc markdown">

Abstract class for handling double tap gestures.

Double-tap gesture occurs after double-tapping on the screen.

</div>

## Implementation

``` dart
factory DoubleTapListener(
  void Function(Point2D) onDoubleTapLambda,

) => DoubleTapListener$Lambdas(
  onDoubleTapLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

