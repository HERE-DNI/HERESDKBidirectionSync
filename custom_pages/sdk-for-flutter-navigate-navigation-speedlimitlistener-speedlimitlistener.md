---
title: "SpeedLimitListener constructor - SpeedLimitListener - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-speedlimitlistener-speedlimitlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SpeedLimitListener.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/SpeedLimitListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">SpeedLimitListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">SpeedLimitListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onSpeedLimitUpdatedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onSpeedLimitUpdatedLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-speedlimit-class">SpeedLimit</a></span></span>

    )</span>

)

</div>

<div class="section desc markdown">

This abstract class should be implemented in order to receive the speed limit of the current road.

</div>

## Implementation

``` dart
factory SpeedLimitListener(
  void Function(SpeedLimit) onSpeedLimitUpdatedLambda,

) => SpeedLimitListener$Lambdas(
  onSpeedLimitUpdatedLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
