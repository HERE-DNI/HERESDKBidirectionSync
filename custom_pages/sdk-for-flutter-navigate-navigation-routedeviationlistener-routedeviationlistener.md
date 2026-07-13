---
title: "RouteDeviationListener constructor - RouteDeviationListener - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-routedeviationlistener-routedeviationlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RouteDeviationListener.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/RouteDeviationListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">RouteDeviationListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">RouteDeviationListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onRouteDeviationLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onRouteDeviationLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-routedeviation-class">RouteDeviation</a></span></span>

    )</span>

)

</div>

<div class="section desc markdown">

This abstract class should be implemented in order to receive notifications about route deviations from <a href="sdk-for-flutter-navigate-navigation-navigator-class">Navigator</a>.

</div>

## Implementation

``` dart
factory RouteDeviationListener(
  void Function(RouteDeviation) onRouteDeviationLambda,

) => RouteDeviationListener$Lambdas(
  onRouteDeviationLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
