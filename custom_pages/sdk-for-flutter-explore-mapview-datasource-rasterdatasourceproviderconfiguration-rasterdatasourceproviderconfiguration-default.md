---
title: "RasterDataSourceProviderConfiguration.Default constructor - RasterDataSourceProviderConfiguration - mapview.datasource library - Dart API"
slug: "sdk-for-flutter-explore-mapview-datasource-rasterdatasourceproviderconfiguration-rasterdatasourceproviderconfiguration-default"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview.datasource/RasterDataSourceProviderConfiguration-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">RasterDataSourceProviderConfiguration.Default</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">RasterDataSourceProviderConfiguration.Default</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-Default-param-urlProvider" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-datasource-tileurlprovidercallback">TileUrlProviderCallback</a></span> <span class="parameter-name">urlProvider</span>, </span>
2.  <span id="sdk-for-flutter-explore-Default-param-tilingScheme" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-datasource-tilingscheme">TilingScheme</a></span> <span class="parameter-name">tilingScheme</span>, </span>
3.  <span id="sdk-for-flutter-explore-Default-param-storageLevels" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">int</span>\></span></span> <span class="parameter-name">storageLevels</span>, </span>
4.  <span id="sdk-for-flutter-explore-Default-param-hasAlphaChannel" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">hasAlphaChannel</span>, </span>
5.  <span id="sdk-for-flutter-explore-Default-param-headers" class="parameter"><span class="type-annotation">Map<span class="signature">\<<wbr></wbr><span class="type-parameter">String</span>, <span class="type-parameter">String</span>\></span>?</span> <span class="parameter-name">headers</span>, </span>

)

</div>

<div class="section desc markdown">

Creates a new instance.

- `urlProvider` Provides a function that generates URLs based on tile coordinates and storage level.
- `tilingScheme` The tiling scheme used by this source.
- `storageLevels` The storage levels available for this data source. Supported range \[0, 31\]. At least one level must be available for this provider to be used as a source of data. At storage level zero, the whole world is represented by one tile. At storage level 1 the world is split in 2x2 tiles (or in 2x1 tiles, depending on the tiling scheme). The tiling process continues in this fashion until sufficient granularity has been achieved. In the XYZ addresing scheme for tiles, z value of the tile key coresponds to the storage level. Depending on the available storage levels and the given camera zoom level, the appropriate z value of the tile key will be determined.
- `hasAlphaChannel` A flag indicating whether the image content contains an alpha channel for transparency. Default value is `false`.
- `headers` The optional name-value pairs specifying HTTP headers that are passed with each tile request.

</div>

## Implementation

``` dart
RasterDataSourceProviderConfiguration.Default(this.urlProvider, this.tilingScheme, this.storageLevels, this.hasAlphaChannel, this.headers);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

