---
title: "TrafficMergeWarningListener constructor - TrafficMergeWarningListener - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-trafficmergewarninglistener"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/TrafficMergeWarningListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">TrafficMergeWarningListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">TrafficMergeWarningListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onTrafficMergeWarningUpdatedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onTrafficMergeWarningUpdatedLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-trafficmergewarning-class">TrafficMergeWarning</a></span></span>

    )</span>

)

</div>

<div class="section desc markdown">

This abstract class should be implemented in order to receive traffic merge warnings.

**Note:** The traffic merge warner is a point warner, which means that for a traffic merge there will *always* be 2 warnings emitted, with the `TrafficMergeWarning.distance_type` set to `DistanceType.AHEAD` and `DistanceType.PASSED` which is given when the location of the traffic merge is reached. A `TrafficMergeWarning` will not be given until the previous warning of that type has been passed. For example, a route with `TrafficMergeWarning` 120 meters and `TrafficMergeWarning` 160 meters ahead, the first `TrafficMergeWarning.distance_to_traffic_merge_in_meters` is 120 meters and the next `TrafficMergeWarning.distance_to_traffic_merge_in_meters` is then 40 meters, since that is the distance between the first and second warnings.

</div>

## Implementation

``` dart
factory TrafficMergeWarningListener(
  void Function(TrafficMergeWarning) onTrafficMergeWarningUpdatedLambda,

) => TrafficMergeWarningListener$Lambdas(
  onTrafficMergeWarningUpdatedLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

