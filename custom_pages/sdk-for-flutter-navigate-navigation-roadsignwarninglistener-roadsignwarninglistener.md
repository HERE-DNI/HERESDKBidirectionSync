---
title: "RoadSignWarningListener constructor - RoadSignWarningListener - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-roadsignwarninglistener-roadsignwarninglistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RoadSignWarningListener.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/RoadSignWarningListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">RoadSignWarningListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">RoadSignWarningListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onRoadSignWarningUpdatedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onRoadSignWarningUpdatedLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-roadsignwarning-class">RoadSignWarning</a></span></span>

    )</span>

)

</div>

<div class="section desc markdown">

This abstract class should be implemented in order to receive road sign warnings.

**Note:** The road sign warner is a point warner, which means that for a road sign there will *always* be 2 warnings emitted, with the <a href="sdk-for-flutter-navigate-navigation-roadsignwarning-distancetype">RoadSignWarning.distanceType</a> set to <a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType.ahead</a> and <a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType.passed</a> which is given when the location of the road sign is reached. A <a href="sdk-for-flutter-navigate-navigation-roadsignwarning-class">RoadSignWarning</a> will not be given until the previous warning of that type has been passed. For example, a route with <a href="sdk-for-flutter-navigate-navigation-roadsignwarning-class">RoadSignWarning</a> 120 meters and <a href="sdk-for-flutter-navigate-navigation-roadsignwarning-class">RoadSignWarning</a> 160 meters ahead, the first <a href="sdk-for-flutter-navigate-navigation-roadsignwarning-distancetoroadsigninmeters">RoadSignWarning.distanceToRoadSignInMeters</a> is 120 meters and the next <a href="sdk-for-flutter-navigate-navigation-roadsignwarning-distancetoroadsigninmeters">RoadSignWarning.distanceToRoadSignInMeters</a> is then 40 meters, since that is the distance between the first and second warnings.

</div>

## Implementation

``` dart
factory RoadSignWarningListener(
  void Function(RoadSignWarning) onRoadSignWarningUpdatedLambda,

) => RoadSignWarningListener$Lambdas(
  onRoadSignWarningUpdatedLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
