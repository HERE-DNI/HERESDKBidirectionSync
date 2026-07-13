---
title: "TollStopWarningListener constructor - TollStopWarningListener - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-tollstopwarninglistener-tollstopwarninglistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TollStopWarningListener.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/TollStopWarningListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">TollStopWarningListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">TollStopWarningListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onTollStopWarningLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onTollStopWarningLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-tollstop-class">TollStop</a></span></span>

    )</span>

)

</div>

<div class="section desc markdown">

This abstract class should be implemented in order to receive information on the upcoming toll booth structure.

The warner might also warn about gates/checkpoints for vignette, border checkpoints and similar structures on the street.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process. A `TollStop` will not be given until the previous warning of that type has been passed. For example, a route with `TollStop` 120 meters and `TollStop` 160 meters ahead, the first `TollStop.distance_to_toll_stop_in_meters` is 120 meters and the next `TollStop.distance_to_toll_stop_in_meters` is then 40 meters, since that is the distance between the first and second warnings.

</div>

## Implementation

``` dart
factory TollStopWarningListener(
  void Function(TollStop) onTollStopWarningLambda,

) => TollStopWarningListener$Lambdas(
  onTollStopWarningLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
