---
title: "LowSpeedZoneWarningListener constructor - LowSpeedZoneWarningListener - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-lowspeedzonewarninglistener-lowspeedzonewarninglistener"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/LowSpeedZoneWarningListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">LowSpeedZoneWarningListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">LowSpeedZoneWarningListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onLowSpeedZoneWarningUpdatedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onLowSpeedZoneWarningUpdatedLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-lowspeedzonewarning-class">LowSpeedZoneWarning</a></span></span>

    )</span>

)

</div>

<div class="section desc markdown">

This abstract class should be implemented in order to receive low speed zone warnings.

**Note:** This is currently available *only* for Japan. The low speed zone warner is a zone warner, which means that for a low speed zone there will *always* be 3 warnings emitted, with the `LowSpeedZoneWarning.distance_type` set to `DistanceType.AHEAD`, `DistanceType.REACHED` and lastly `DistanceType.PASSED` when the end of the low speed zone is passed.

</div>

## Implementation

``` dart
factory LowSpeedZoneWarningListener(
  void Function(LowSpeedZoneWarning) onLowSpeedZoneWarningUpdatedLambda,

) => LowSpeedZoneWarningListener$Lambdas(
  onLowSpeedZoneWarningUpdatedLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

