---
title: "MatchedLocationListener constructor - MatchedLocationListener - mapmatcher library - Dart API"
slug: "sdk-for-flutter-navigate-mapmatcher-matchedlocationlistener-matchedlocationlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MatchedLocationListener.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapmatcher/MatchedLocationListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">MatchedLocationListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">MatchedLocationListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onMatchedLocationUpdatedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onMatchedLocationUpdatedLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapmatcher-matchedlocation-class">MatchedLocation</a></span></span>

    )</span>

)

</div>

<div class="section desc markdown">

This abstract class should be implemented to receive notifications about the current location from <a href="sdk-for-flutter-navigate-navigation-mapmatchedlocation-class">MapMatchedLocation</a>.

**Note:** This is a **beta** release of this feature. There may be bugs and unexpected behaviors. Related APIs may change in future releases without a deprecation process.

</div>

## Implementation

``` dart
factory MatchedLocationListener(
  void Function(MatchedLocation) onMatchedLocationUpdatedLambda,

) => MatchedLocationListener$Lambdas(
  onMatchedLocationUpdatedLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
