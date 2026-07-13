---
title: "PointTileSourceLoadResultHandler constructor - PointTileSourceLoadResultHandler - mapview.datasource library - Dart API"
slug: "sdk-for-flutter-explore-mapview.datasource-pointtilesourceloadresulthandler-pointtilesourceloadresulthandler"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview.datasource/PointTileSourceLoadResultHandler-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">PointTileSourceLoadResultHandler</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">PointTileSourceLoadResultHandler</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-param-loadedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">loadedLambda</span>(</span>
    1.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-datasource-tilekey-class">TileKey</a></span>, </span>
    2.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-mapview-datasource-pointdata-class">PointData</a></span>\></span></span>, </span>
    3.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-datasource-tilesourcetilemetadata-class">TileSourceTileMetadata</a></span></span>

    ), </span>
2.  <span id="sdk-for-flutter-explore-param-failedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">failedLambda</span>(</span>
    1.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-datasource-tilekey-class">TileKey</a></span></span>

    )</span>

)

</div>

<div class="section desc markdown">

Result handler of a load tile request.

</div>

## Implementation

``` dart
factory PointTileSourceLoadResultHandler(
  void Function(TileKey, List<PointData>, TileSourceTileMetadata) loadedLambda,
  void Function(TileKey) failedLambda,

) => PointTileSourceLoadResultHandler$Lambdas(
  loadedLambda,
  failedLambda,

);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

