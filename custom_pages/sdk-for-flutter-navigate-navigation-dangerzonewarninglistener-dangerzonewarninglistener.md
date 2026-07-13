---
title: "DangerZoneWarningListener constructor - DangerZoneWarningListener - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-dangerzonewarninglistener-dangerzonewarninglistener"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/DangerZoneWarningListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">DangerZoneWarningListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">DangerZoneWarningListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onDangerZoneWarningsUpdatedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onDangerZoneWarningsUpdatedLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-dangerzonewarning-class">DangerZoneWarning</a></span></span>

    )</span>

)

</div>

<div class="section desc markdown">

This abstract class should be implemented in order to receive notifications about the Danger zones.

</div>

## Implementation

``` dart
factory DangerZoneWarningListener(
  void Function(DangerZoneWarning) onDangerZoneWarningsUpdatedLambda,

) => DangerZoneWarningListener$Lambdas(
  onDangerZoneWarningsUpdatedLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

