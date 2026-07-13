---
title: "loaded method - RasterTileSourceLoadResultHandler class - mapview.datasource library - Dart API"
slug: "sdk-for-flutter-explore-mapview.datasource-rastertilesourceloadresulthandler-loaded"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview.datasource/RasterTileSourceLoadResultHandler-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">loaded</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">loaded</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-loaded-param-tileKey" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-datasource-tilekey-class">TileKey</a></span> <span class="parameter-name">tileKey</span>, </span>
2.  <span id="sdk-for-flutter-explore-loaded-param-data" class="parameter"><span class="type-annotation">Uint8List</span> <span class="parameter-name">data</span>, </span>
3.  <span id="sdk-for-flutter-explore-loaded-param-metadata" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-datasource-tilesourcetilemetadata-class">TileSourceTileMetadata</a></span> <span class="parameter-name">metadata</span></span>

)

</div>

<div class="section desc markdown">

Called upon successful load tile request.

- `tileKey` Loaded tile key.

- `data` Loaded tile data. Supported are images in PNG or JPEG format.

- `metadata` Loaded tile metadata.

</div>

## Implementation

``` dart
void loaded(TileKey tileKey, Uint8List data, TileSourceTileMetadata metadata);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

