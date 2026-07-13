---
title: "RoadTextsListener constructor - RoadTextsListener - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-roadtextslistener-roadtextslistener"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/RoadTextsListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">RoadTextsListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">RoadTextsListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onRoadTextsUpdatedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onRoadTextsUpdatedLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-roadtexts-class">RoadTexts</a></span></span>

    )</span>

)

</div>

<div class="section desc markdown">

This abstract class should be implemented in order to receive textual attributes of the current road.

</div>

## Implementation

``` dart
factory RoadTextsListener(
  void Function(RoadTexts) onRoadTextsUpdatedLambda,

) => RoadTextsListener$Lambdas(
  onRoadTextsUpdatedLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

