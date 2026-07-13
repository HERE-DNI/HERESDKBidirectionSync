---
title: "ManeuverViewLaneAssistanceListener constructor - ManeuverViewLaneAssistanceListener - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-maneuverviewlaneassistancelistener-maneuverviewlaneassistancelistener"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/ManeuverViewLaneAssistanceListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">ManeuverViewLaneAssistanceListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">ManeuverViewLaneAssistanceListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onLaneAssistanceUpdatedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onLaneAssistanceUpdatedLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-class">ManeuverViewLaneAssistance</a></span></span>

    )</span>

)

</div>

<div class="section desc markdown">

This abstract class should be implemented in order to receive notifications on <a href="sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-class">ManeuverViewLaneAssistance</a>.

See <a href="sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-class">ManeuverViewLaneAssistance</a> documentation for further details.

</div>

## Implementation

``` dart
factory ManeuverViewLaneAssistanceListener(
  void Function(ManeuverViewLaneAssistance) onLaneAssistanceUpdatedLambda,

) => ManeuverViewLaneAssistanceListener$Lambdas(
  onLaneAssistanceUpdatedLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

