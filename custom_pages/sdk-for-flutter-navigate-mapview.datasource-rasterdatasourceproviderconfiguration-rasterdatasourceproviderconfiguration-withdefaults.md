---
title: "RasterDataSourceProviderConfiguration.withDefaults constructor - RasterDataSourceProviderConfiguration - mapview.datasource library - Dart API"
slug: "sdk-for-flutter-navigate-mapview.datasource-rasterdatasourceproviderconfiguration-rasterdatasourceproviderconfiguration-withdefaults"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RasterDataSourceProviderConfiguration.withDefaults.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview.datasource/RasterDataSourceProviderConfiguration-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">RasterDataSourceProviderConfiguration.withDefaults</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">RasterDataSourceProviderConfiguration.withDefaults</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-withDefaults-param-urlProvider" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-datasource-tileurlprovidercallback">TileUrlProviderCallback</a></span> <span class="parameter-name">urlProvider</span>, </span>
2.  <span id="sdk-for-flutter-navigate-withDefaults-param-tilingScheme" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-datasource-tilingscheme">TilingScheme</a></span> <span class="parameter-name">tilingScheme</span>, </span>
3.  <span id="sdk-for-flutter-navigate-withDefaults-param-storageLevels" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">int</span>\></span></span> <span class="parameter-name">storageLevels</span></span>

)

</div>

<div class="section desc markdown">

Creates a new instance.

- `urlProvider` Provides a function that generates URLs based on tile coordinates and storage level.
- `tilingScheme` The tiling scheme used by this source.
- `storageLevels` The storage levels available for this data source. Supported range \[0, 31\]. At least one level must be available for this provider to be used as a source of data. At storage level zero, the whole world is represented by one tile. At storage level 1 the world is split in 2x2 tiles (or in 2x1 tiles, depending on the tiling scheme). The tiling process continues in this fashion until sufficient granularity has been achieved. In the XYZ addresing scheme for tiles, z value of the tile key coresponds to the storage level. Depending on the available storage levels and the given camera zoom level, the appropriate z value of the tile key will be determined.

</div>

## Implementation

``` dart
RasterDataSourceProviderConfiguration.withDefaults(this.urlProvider, this.tilingScheme, this.storageLevels)
    : hasAlphaChannel = false, headers = null;
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
