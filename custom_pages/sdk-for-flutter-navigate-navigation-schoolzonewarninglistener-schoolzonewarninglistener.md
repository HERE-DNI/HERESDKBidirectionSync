---
title: "SchoolZoneWarningListener constructor - SchoolZoneWarningListener - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-schoolzonewarninglistener-schoolzonewarninglistener"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/SchoolZoneWarningListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">SchoolZoneWarningListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">SchoolZoneWarningListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onSchoolZoneWarningUpdatedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onSchoolZoneWarningUpdatedLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-schoolzonewarning-class">SchoolZoneWarning</a></span>\></span></span></span>

    )</span>

)

</div>

<div class="section desc markdown">

This abstract class should be implemented in order to receive school zone warnings.

</div>

## Implementation

``` dart
factory SchoolZoneWarningListener(
  void Function(List<SchoolZoneWarning>) onSchoolZoneWarningUpdatedLambda,

) => SchoolZoneWarningListener$Lambdas(
  onSchoolZoneWarningUpdatedLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

