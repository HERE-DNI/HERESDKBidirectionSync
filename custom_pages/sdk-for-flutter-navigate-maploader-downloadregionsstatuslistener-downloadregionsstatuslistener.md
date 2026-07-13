---
title: "DownloadRegionsStatusListener constructor - DownloadRegionsStatusListener - maploader library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-downloadregionsstatuslistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- DownloadRegionsStatusListener.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader/DownloadRegionsStatusListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">DownloadRegionsStatusListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">DownloadRegionsStatusListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onDownloadRegionsCompleteLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onDownloadRegionsCompleteLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a>?</span>, </span>
    2.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-maploader-regionid-class">RegionId</a></span>\></span>?</span></span>

    ), </span>
2.  <span id="sdk-for-flutter-navigate-param-onProgressLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onProgressLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-regionid-class">RegionId</a></span>, </span>
    2.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">int</span></span>

    ), </span>
3.  <span id="sdk-for-flutter-navigate-param-onPauseLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onPauseLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a>?</span></span>

    ), </span>
4.  <span id="sdk-for-flutter-navigate-param-onResumeLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onResumeLambda</span>(), </span>

)

</div>

<div class="section desc markdown">

Abstract class to get notified on status updates when downloading map regions.

</div>

## Implementation

``` dart
factory DownloadRegionsStatusListener(
  void Function(MapLoaderError?, List<RegionId>?) onDownloadRegionsCompleteLambda,
  void Function(RegionId, int) onProgressLambda,
  void Function(MapLoaderError?) onPauseLambda,
  void Function() onResumeLambda,

) => DownloadRegionsStatusListener$Lambdas(
  onDownloadRegionsCompleteLambda,
  onProgressLambda,
  onPauseLambda,
  onResumeLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
