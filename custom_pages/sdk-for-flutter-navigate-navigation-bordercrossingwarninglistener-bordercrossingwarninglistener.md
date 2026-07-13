---
title: "BorderCrossingWarningListener constructor - BorderCrossingWarningListener - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-bordercrossingwarninglistener-bordercrossingwarninglistener"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/BorderCrossingWarningListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">BorderCrossingWarningListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">BorderCrossingWarningListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onBorderCrossingWarningUpdatedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onBorderCrossingWarningUpdatedLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-bordercrossingwarning-class">BorderCrossingWarning</a></span></span>

    )</span>

)

</div>

<div class="section desc markdown">

This abstract class should be implemented in order to receive border crossing warnings for country and state borders.

**Note:** The border crossing warner is a point warner, which means that for a border crossing there will *always* be 2 warnings emitted, with the <a href="sdk-for-flutter-navigate-navigation-bordercrossingwarning-distancetype">BorderCrossingWarning.distanceType</a> set to <a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType.ahead</a> and <a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType.passed</a> which is given when the location of the border crossing is reached. A <a href="sdk-for-flutter-navigate-navigation-bordercrossingwarning-class">BorderCrossingWarning</a> will not be given until the previous warning of that type has been passed. For example, a route with <a href="sdk-for-flutter-navigate-navigation-bordercrossingwarning-class">BorderCrossingWarning</a> 120 meters and <a href="sdk-for-flutter-navigate-navigation-bordercrossingwarning-class">BorderCrossingWarning</a> 160 meters ahead, the first <a href="sdk-for-flutter-navigate-navigation-bordercrossingwarning-distancetobordercrossinginmeters">BorderCrossingWarning.distanceToBorderCrossingInMeters</a> is 120 meters and the next <a href="sdk-for-flutter-navigate-navigation-bordercrossingwarning-distancetobordercrossinginmeters">BorderCrossingWarning.distanceToBorderCrossingInMeters</a> is then 40 meters, since that is the distance between the first and second warnings.

</div>

## Implementation

``` dart
factory BorderCrossingWarningListener(
  void Function(BorderCrossingWarning) onBorderCrossingWarningUpdatedLambda,

) => BorderCrossingWarningListener$Lambdas(
  onBorderCrossingWarningUpdatedLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

