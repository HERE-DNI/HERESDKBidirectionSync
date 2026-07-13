---
title: "TapListener constructor - TapListener - gestures library - Dart API"
slug: "sdk-for-flutter-navigate-gestures-taplistener-taplistener"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="gestures/TapListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">TapListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">TapListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onTapLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onTapLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-point2d-class">Point2D</a></span></span>

    )</span>

)

</div>

<div class="section desc markdown">

Abstract class for handling tap gestures.

Tap gesture occurs after tapping on the screen.

</div>

## Implementation

``` dart
factory TapListener(
  void Function(Point2D) onTapLambda,

) => TapListener$Lambdas(
  onTapLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

