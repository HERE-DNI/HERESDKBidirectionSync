---
title: "AnimationListener constructor - AnimationListener - animation library - Dart API"
slug: "sdk-for-flutter-navigate-animation-animationlistener-animationlistener"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="animation/AnimationListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">AnimationListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">AnimationListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onAnimationStateChangedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onAnimationStateChangedLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-animation-animationstate">AnimationState</a></span></span>

    )</span>

)

</div>

<div class="section desc markdown">

A listener for animation events.

</div>

## Implementation

``` dart
factory AnimationListener(
  void Function(AnimationState) onAnimationStateChangedLambda,

) => AnimationListener$Lambdas(
  onAnimationStateChangedLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

