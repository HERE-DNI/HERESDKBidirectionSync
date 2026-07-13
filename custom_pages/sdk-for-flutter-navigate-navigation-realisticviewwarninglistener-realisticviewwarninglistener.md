---
title: "RealisticViewWarningListener constructor - RealisticViewWarningListener - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-realisticviewwarninglistener-realisticviewwarninglistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RealisticViewWarningListener.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/RealisticViewWarningListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">RealisticViewWarningListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">RealisticViewWarningListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onRealisticViewWarningUpdatedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onRealisticViewWarningUpdatedLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-class">RealisticViewWarning</a></span></span>

    )</span>

)

</div>

<div class="section desc markdown">

This abstract class should be implemented in order to receive realistic view warnings.

A <a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-class">RealisticViewWarning</a> will not be given until the previous warning of that type has been passed. For example, a route with <a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-class">RealisticViewWarning</a> 120 meters and <a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-class">RealisticViewWarning</a> 160 meters ahead, the first <a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-distancetorealisticviewinmeters">RealisticViewWarning.distanceToRealisticViewInMeters</a> is 120 meters and the next <a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-distancetorealisticviewinmeters">RealisticViewWarning.distanceToRealisticViewInMeters</a> is then 40 meters, since that is the distance between the first and second warnings.

</div>

## Implementation

``` dart
factory RealisticViewWarningListener(
  void Function(RealisticViewWarning) onRealisticViewWarningUpdatedLambda,

) => RealisticViewWarningListener$Lambdas(
  onRealisticViewWarningUpdatedLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
