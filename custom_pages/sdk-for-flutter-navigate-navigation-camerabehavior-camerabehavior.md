---
title: "CameraBehavior constructor - CameraBehavior - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-camerabehavior-camerabehavior"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- CameraBehavior.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/CameraBehavior-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">CameraBehavior</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">CameraBehavior</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-normalizedPrincipalPointGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-anchor2d-class">Anchor2D</a></span> <span class="parameter-name">normalizedPrincipalPointGetLambda</span>(), </span>
2.  <span id="sdk-for-flutter-navigate-param-normalizedPrincipalPointSetLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">normalizedPrincipalPointSetLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-anchor2d-class">Anchor2D</a></span></span>

    )</span>

)

</div>

<div class="section desc markdown">

Abstract class used to change implement different camera behaviors.

</div>

## Implementation

``` dart
factory CameraBehavior(
  Anchor2D Function() normalizedPrincipalPointGetLambda,
  void Function(Anchor2D) normalizedPrincipalPointSetLambda
) => CameraBehavior$Lambdas(
  normalizedPrincipalPointGetLambda,
  normalizedPrincipalPointSetLambda
);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
