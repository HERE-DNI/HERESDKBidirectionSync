---
title: "InterpolatedLocationListener constructor - InterpolatedLocationListener - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-interpolatedlocationlistener-interpolatedlocationlistener"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/InterpolatedLocationListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">InterpolatedLocationListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">InterpolatedLocationListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onInterpolatedLocationUpdatedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onInterpolatedLocationUpdatedLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-location-class">Location</a></span></span>

    )</span>

)

</div>

<div class="section desc markdown">

This abstract class should be implemented in order to receive interpolated locations.

The interpolated locations are only provided between <a href="sdk-for-flutter-navigate-navigation-visualnavigator-startrendering">VisualNavigator.startRendering</a> and <a href="sdk-for-flutter-navigate-navigation-visualnavigator-stoprendering">VisualNavigator.stopRendering</a> calls and the application is not running in the background.

</div>

## Implementation

``` dart
factory InterpolatedLocationListener(
  void Function(Location) onInterpolatedLocationUpdatedLambda,

) => InterpolatedLocationListener$Lambdas(
  onInterpolatedLocationUpdatedLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

