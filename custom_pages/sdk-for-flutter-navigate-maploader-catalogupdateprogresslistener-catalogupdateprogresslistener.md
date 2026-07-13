---
title: "CatalogUpdateProgressListener constructor - CatalogUpdateProgressListener - maploader library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-catalogupdateprogresslistener-catalogupdateprogresslistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- CatalogUpdateProgressListener.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader/CatalogUpdateProgressListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">CatalogUpdateProgressListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">CatalogUpdateProgressListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onProgressLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onProgressLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-regionid-class">RegionId</a></span>, </span>
    2.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">int</span></span>

    ), </span>
2.  <span id="sdk-for-flutter-navigate-param-onPauseLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onPauseLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a>?</span></span>

    ), </span>
3.  <span id="sdk-for-flutter-navigate-param-onCompleteLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onCompleteLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a>?</span></span>

    ), </span>
4.  <span id="sdk-for-flutter-navigate-param-onResumeLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onResumeLambda</span>(), </span>

)

</div>

<div class="section desc markdown">

Abstract class to get notified on status updates when updating catalog, previously downloaded by <a href="sdk-for-flutter-navigate-maploader-mapdownloader-class">MapDownloader</a>.

</div>

## Implementation

``` dart
factory CatalogUpdateProgressListener(
  void Function(RegionId, int) onProgressLambda,
  void Function(MapLoaderError?) onPauseLambda,
  void Function(MapLoaderError?) onCompleteLambda,
  void Function() onResumeLambda,

) => CatalogUpdateProgressListener$Lambdas(
  onProgressLambda,
  onPauseLambda,
  onCompleteLambda,
  onResumeLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
