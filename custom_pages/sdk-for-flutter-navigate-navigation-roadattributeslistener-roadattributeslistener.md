---
title: "RoadAttributesListener constructor - RoadAttributesListener - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-roadattributeslistener-roadattributeslistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RoadAttributesListener.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/RoadAttributesListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">RoadAttributesListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">RoadAttributesListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onRoadAttributesUpdatedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onRoadAttributesUpdatedLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-roadattributes-class">RoadAttributes</a></span></span>

    )</span>

)

</div>

<div class="section desc markdown">

This abstract class should be implemented in order to receive attributes of the current road.

</div>

## Implementation

``` dart
factory RoadAttributesListener(
  void Function(RoadAttributes) onRoadAttributesUpdatedLambda,

) => RoadAttributesListener$Lambdas(
  onRoadAttributesUpdatedLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
