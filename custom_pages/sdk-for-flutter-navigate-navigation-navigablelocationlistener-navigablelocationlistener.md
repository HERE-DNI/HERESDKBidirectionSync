---
title: "NavigableLocationListener constructor - NavigableLocationListener - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-navigablelocationlistener-navigablelocationlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- NavigableLocationListener.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/NavigableLocationListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">NavigableLocationListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">NavigableLocationListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onNavigableLocationUpdatedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onNavigableLocationUpdatedLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-navigablelocation-class">NavigableLocation</a></span></span>

    )</span>

)

</div>

<div class="section desc markdown">

This abstract class should be implemented in order to receive notifications about the current location from <a href="sdk-for-flutter-navigate-navigation-navigator-class">Navigator</a>.

</div>

## Implementation

``` dart
factory NavigableLocationListener(
  void Function(NavigableLocation) onNavigableLocationUpdatedLambda,

) => NavigableLocationListener$Lambdas(
  onNavigableLocationUpdatedLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
