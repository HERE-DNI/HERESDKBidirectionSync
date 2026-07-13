---
title: "SpeedWarningListener constructor - SpeedWarningListener - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-speedwarninglistener-speedwarninglistener"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/SpeedWarningListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">SpeedWarningListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">SpeedWarningListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onSpeedWarningStatusChangedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onSpeedWarningStatusChangedLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-speedwarningstatus">SpeedWarningStatus</a></span></span>

    )</span>

)

</div>

<div class="section desc markdown">

This abstract class should be implemented in order to receive notifications when a speed limit on a road is exceeded or driving speed is restored back to normal.

**Note:** The warnings issued by this abstract class don't take into account any temporary special speed limits. See `SpeedLimitListener`.

</div>

## Implementation

``` dart
factory SpeedWarningListener(
  void Function(SpeedWarningStatus) onSpeedWarningStatusChangedLambda,

) => SpeedWarningListener$Lambdas(
  onSpeedWarningStatusChangedLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

