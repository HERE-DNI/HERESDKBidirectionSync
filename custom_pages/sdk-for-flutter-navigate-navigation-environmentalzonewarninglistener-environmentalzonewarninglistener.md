---
title: "EnvironmentalZoneWarningListener constructor - EnvironmentalZoneWarningListener - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-environmentalzonewarninglistener-environmentalzonewarninglistener"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/EnvironmentalZoneWarningListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">EnvironmentalZoneWarningListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">EnvironmentalZoneWarningListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onEnvironmentalZoneWarningsUpdatedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onEnvironmentalZoneWarningsUpdatedLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-environmentalzonewarning-class">EnvironmentalZoneWarning</a></span>\></span></span></span>

    )</span>

)

</div>

<div class="section desc markdown">

This abstract class should be implemented in order to receive notifications about the environmental zones.

</div>

## Implementation

``` dart
factory EnvironmentalZoneWarningListener(
  void Function(List<EnvironmentalZoneWarning>) onEnvironmentalZoneWarningsUpdatedLambda,

) => EnvironmentalZoneWarningListener$Lambdas(
  onEnvironmentalZoneWarningsUpdatedLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

