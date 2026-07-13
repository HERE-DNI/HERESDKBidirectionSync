---
title: "OffRoadProgressListener constructor - OffRoadProgressListener - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-offroadprogresslistener-offroadprogresslistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- OffRoadProgressListener.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/OffRoadProgressListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">OffRoadProgressListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">OffRoadProgressListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onOffRoadProgressUpdatedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onOffRoadProgressUpdatedLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-offroadprogress-class">OffRoadProgress</a></span></span>

    )</span>

)

</div>

<div class="section desc markdown">

This abstract class should be implemented in order to receive notifications about the current off-road location from <a href="sdk-for-flutter-navigate-navigation-navigator-class">Navigator</a>.

</div>

## Implementation

``` dart
factory OffRoadProgressListener(
  void Function(OffRoadProgress) onOffRoadProgressUpdatedLambda,

) => OffRoadProgressListener$Lambdas(
  onOffRoadProgressUpdatedLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
