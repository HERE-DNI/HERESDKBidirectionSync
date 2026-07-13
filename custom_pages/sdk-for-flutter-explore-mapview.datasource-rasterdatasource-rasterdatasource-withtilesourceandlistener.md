---
title: "RasterDataSource.withTileSourceAndListener constructor - RasterDataSource - mapview.datasource library - Dart API"
slug: "sdk-for-flutter-explore-mapview.datasource-rasterdatasource-rasterdatasource-withtilesourceandlistener"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview.datasource/RasterDataSource-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">RasterDataSource.withTileSourceAndListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">RasterDataSource.withTileSourceAndListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-withTileSourceAndListener-param-context" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapcontext-class">MapContext</a></span> <span class="parameter-name">context</span>, </span>
2.  <span id="sdk-for-flutter-explore-withTileSourceAndListener-param-name" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">name</span>, </span>
3.  <span id="sdk-for-flutter-explore-withTileSourceAndListener-param-tileSource" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-datasource-rastertilesource-class">RasterTileSource</a></span> <span class="parameter-name">tileSource</span>, </span>
4.  <span id="sdk-for-flutter-explore-withTileSourceAndListener-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-datasource-rasterdatasourcelistener-class">RasterDataSourceListener</a></span> <span class="parameter-name">listener</span>, </span>

)

</div>

<div class="section desc markdown">

Creates a RasterDataSource instance with the provided raster tile source and registers a listener.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

- `context` The map context to associate the data source with.

- `name` The unique name of the data source.

- `tileSource` The raster tile source.

- `listener` The initial listener to be registered for receiving state notifications. Due to the asynchronous nature of the data source initialization, the listeners registered later might miss some notifications. This listener is guaranteed to receive all notifications. The state notifications can occur on an arbitrary thread.

</div>

## Implementation

``` dart
factory RasterDataSource.withTileSourceAndListener(MapContext context, String name, RasterTileSource tileSource, RasterDataSourceListener listener) => $prototype.withTileSourceAndListener(context, name, tileSource, listener);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

