---
title: "RasterTileSource constructor - RasterTileSource - mapview.datasource library - Dart API"
slug: "sdk-for-flutter-explore-mapview.datasource-rastertilesource-rastertilesource"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RasterTileSource.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview.datasource/RasterTileSource-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">RasterTileSource</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">RasterTileSource</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-param-getDataVersionLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-datasource-tilesourcedataversion-class">TileSourceDataVersion</a></span> <span class="parameter-name">getDataVersionLambda</span>(</span>
    1.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-datasource-tilekey-class">TileKey</a></span></span>

    ), </span>
2.  <span id="sdk-for-flutter-explore-param-addListenerLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">addListenerLambda</span>(</span>
    1.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-datasource-tilesourcelistener-class">TileSourceListener</a></span></span>

    ), </span>
3.  <span id="sdk-for-flutter-explore-param-removeListenerLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">removeListenerLambda</span>(</span>
    1.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-datasource-tilesourcelistener-class">TileSourceListener</a></span></span>

    ), </span>
4.  <span id="sdk-for-flutter-explore-param-loadTileLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-datasource-tilesourceloadtilerequesthandle-class">TileSourceLoadTileRequestHandle</a>?</span> <span class="parameter-name">loadTileLambda</span>(</span>
    1.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-datasource-tilekey-class">TileKey</a></span>, </span>
    2.  <span id="sdk-for-flutter-explore-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-datasource-rastertilesourceloadresulthandler-class">RasterTileSourceLoadResultHandler</a></span></span>

    ), </span>
5.  <span id="sdk-for-flutter-explore-param-tilingSchemeGetLambda" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-datasource-tilingscheme">TilingScheme</a></span> <span class="parameter-name">tilingSchemeGetLambda</span>(), </span>
6.  <span id="sdk-for-flutter-explore-param-storageLevelsGetLambda" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">int</span>\></span></span> <span class="parameter-name">storageLevelsGetLambda</span>(), </span>

)

</div>

<div class="section desc markdown">

A source of raster tiles.

The implementations must be thread-safe. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

</div>

## Implementation

``` dart
factory RasterTileSource(
  TileSourceDataVersion Function(TileKey) getDataVersionLambda,
  void Function(TileSourceListener) addListenerLambda,
  void Function(TileSourceListener) removeListenerLambda,
  TileSourceLoadTileRequestHandle? Function(TileKey, RasterTileSourceLoadResultHandler) loadTileLambda,
  TilingScheme Function() tilingSchemeGetLambda,
  List<int> Function() storageLevelsGetLambda
) => RasterTileSource$Lambdas(
  getDataVersionLambda,
  addListenerLambda,
  removeListenerLambda,
  loadTileLambda,
  tilingSchemeGetLambda,
  storageLevelsGetLambda
);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
