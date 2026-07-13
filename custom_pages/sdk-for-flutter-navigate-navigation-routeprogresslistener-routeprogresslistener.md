---
title: "RouteProgressListener constructor - RouteProgressListener - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-routeprogresslistener-routeprogresslistener"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/RouteProgressListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">RouteProgressListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">RouteProgressListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onRouteProgressUpdatedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onRouteProgressUpdatedLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-routeprogress-class">RouteProgress</a></span></span>

    )</span>

)

</div>

<div class="section desc markdown">

This abstract class should be implemented in order to receive notifications about the route progress from <a href="sdk-for-flutter-navigate-navigation-navigator-class">Navigator</a>.

</div>

## Implementation

``` dart
factory RouteProgressListener(
  void Function(RouteProgress) onRouteProgressUpdatedLambda,

) => RouteProgressListener$Lambdas(
  onRouteProgressUpdatedLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

