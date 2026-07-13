---
title: "RasterDataSourceListener constructor - RasterDataSourceListener - mapview.datasource library - Dart API"
slug: "sdk-for-flutter-navigate-mapview.datasource-rasterdatasourcelistener-rasterdatasourcelistener"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview.datasource/RasterDataSourceListener-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">RasterDataSourceListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">RasterDataSourceListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-onRasterDataSourceReadyLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onRasterDataSourceReadyLambda</span>(), </span>
2.  <span id="sdk-for-flutter-navigate-param-onRasterDataSourceErrorLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onRasterDataSourceErrorLambda</span>(</span>
    1.  <span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-datasource-rasterdatasourceerror">RasterDataSourceError</a></span></span>

    )</span>

)

</div>

<div class="section desc markdown">

Listener for RasterDataSource events.

</div>

## Implementation

``` dart
factory RasterDataSourceListener(
  void Function() onRasterDataSourceReadyLambda,
  void Function(RasterDataSourceError) onRasterDataSourceErrorLambda,

) => RasterDataSourceListener$Lambdas(
  onRasterDataSourceReadyLambda,
  onRasterDataSourceErrorLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

