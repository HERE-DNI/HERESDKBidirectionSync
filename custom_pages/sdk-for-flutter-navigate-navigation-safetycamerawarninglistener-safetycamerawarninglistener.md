---
title: "SafetyCameraWarningListener constructor - SafetyCameraWarningListener - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-safetycamerawarninglistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SafetyCameraWarningListener.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/SafetyCameraWarningListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">SafetyCameraWarningListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">SafetyCameraWarningListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onSafetyCameraWarningUpdatedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onSafetyCameraWarningUpdatedLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-safetycamerawarning-class">SafetyCameraWarning</a></span></span>

    )</span>

)

</div>

<div class="section desc markdown">

This abstract class should be implemented in order to receive notifications on safety cameras.

A `SafetyCameraWarning` will not be given until the previous warning of that type has been passed. For example, a route with `SafetyCameraWarning` 120 meters and `SafetyCameraWarning` 160 meters ahead, the first `SafetyCameraWarning.distance_to_camera_in_meters` is 120 meters and the next `SafetyCameraWarning.distance_to_camera_in_meters` is then 40 meters, since that is the distance between the first and second warnings.

When `SafetyCameraWarningListener` is enabled, a new set of text notifications (e.g. "Speed camera ahead") will be trigger if any has been also enabled. The updates for the same safety camera appear in order of the initial `DistanceType.AHEAD` event. That is a first in first out approach is used when multiple safety cameras are reached or passed on the same location.

</div>

## Implementation

``` dart
factory SafetyCameraWarningListener(
  void Function(SafetyCameraWarning) onSafetyCameraWarningUpdatedLambda,

) => SafetyCameraWarningListener$Lambdas(
  onSafetyCameraWarningUpdatedLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
