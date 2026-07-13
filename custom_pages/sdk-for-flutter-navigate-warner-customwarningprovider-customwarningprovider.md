---
title: "CustomWarningProvider constructor - CustomWarningProvider - warner library - Dart API"
slug: "sdk-for-flutter-navigate-warner-customwarningprovider-customwarningprovider"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- CustomWarningProvider.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="warner/CustomWarningProvider-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">CustomWarningProvider</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">CustomWarningProvider</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-getCustomWarningTypeLambda" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">getCustomWarningTypeLambda</span>(), </span>
2.  <span id="sdk-for-flutter-navigate-param-getWarningsLambda" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-warner-customwarning-class">CustomWarning</a></span>\></span></span> <span class="parameter-name">getWarningsLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapdata-segmentdata-class">SegmentData</a></span>, </span>
    2.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapdata-segmentdata-class">SegmentData</a>?</span></span>

    )</span>

)

</div>

<div class="section desc markdown">

A abstract class representing a provider of custom warnings based on vehicle position.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Implementation

``` dart
factory CustomWarningProvider(
  int Function() getCustomWarningTypeLambda,
  List<CustomWarning> Function(SegmentData, SegmentData?) getWarningsLambda,

) => CustomWarningProvider$Lambdas(
  getCustomWarningTypeLambda,
  getWarningsLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
