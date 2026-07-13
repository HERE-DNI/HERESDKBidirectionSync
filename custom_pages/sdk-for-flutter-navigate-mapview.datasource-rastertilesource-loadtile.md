---
title: "loadTile method - RasterTileSource class - mapview.datasource library - Dart API"
slug: "sdk-for-flutter-navigate-mapview.datasource-rastertilesource-loadtile"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- loadTile.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview.datasource/RasterTileSource-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">loadTile</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-mapview-datasource-tilesourceloadtilerequesthandle-class">TileSourceLoadTileRequestHandle</a>?</span> <span class="name">loadTile</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-loadTile-param-tileKey" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-datasource-tilekey-class">TileKey</a></span> <span class="parameter-name">tileKey</span>, </span>
2.  <span id="sdk-for-flutter-navigate-loadTile-param-completionHandler" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-datasource-rastertilesourceloadresulthandler-class">RasterTileSourceLoadResultHandler</a></span> <span class="parameter-name">completionHandler</span></span>

)

</div>

<div class="section desc markdown">

Load data of a tile.

Upon completion, the handler gets informed.

- `tileKey` Key of the tile to load data for.

- `completionHandler` Load result handler.

Returns <a href="sdk-for-flutter-navigate-mapview-datasource-tilesourceloadtilerequesthandle-class">TileSourceLoadTileRequestHandle?</a>. A handle to the created load request.

</div>

## Implementation

``` dart
TileSourceLoadTileRequestHandle? loadTile(TileKey tileKey, RasterTileSourceLoadResultHandler completionHandler);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
