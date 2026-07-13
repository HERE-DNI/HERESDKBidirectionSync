---
title: "RailwayCrossingWarningListener constructor - RailwayCrossingWarningListener - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-railwaycrossingwarninglistener-railwaycrossingwarninglistener"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/RailwayCrossingWarningListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">RailwayCrossingWarningListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">RailwayCrossingWarningListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onRailwayCrossingWarningUpdatedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onRailwayCrossingWarningUpdatedLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-railwaycrossingwarning-class">RailwayCrossingWarning</a></span></span>

    )</span>

)

</div>

<div class="section desc markdown">

This abstract class should be implemented in order to receive railway crossing warnings.

**Note:** The railway crossing warner can be either a zone warner or a point warner, depending on whether the railroad crossing warning is given for a railroad crossing zone or just a point. This means that for a railway crossing there will can be either 2 or 3 warnings emitted. In case the railroad crossing is a zone warner then 3 warnings will be emitted with the `RailwayCrossingWarning.distance_type` set to `DistanceType.AHEAD`, `DistanceType.REACHED` and lastly `DistanceType.PASSED` when the end of the railway crossing is passed. In case the railroad crossing is a point warner then 2 warnings will be emitted with the `RailwayCrossingWarning.distance_type` set to `DistanceType.AHEAD` and `DistanceType.PASSED` when the end of the railway crossing is passed.

</div>

## Implementation

``` dart
factory RailwayCrossingWarningListener(
  void Function(RailwayCrossingWarning) onRailwayCrossingWarningUpdatedLambda,

) => RailwayCrossingWarningListener$Lambdas(
  onRailwayCrossingWarningUpdatedLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

