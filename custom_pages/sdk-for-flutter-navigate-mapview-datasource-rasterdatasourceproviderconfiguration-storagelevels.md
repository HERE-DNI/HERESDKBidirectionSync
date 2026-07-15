---
title: "storageLevels property - RasterDataSourceProviderConfiguration class - mapview.datasource library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-datasource-rasterdatasourceproviderconfiguration-storagelevels"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview.datasource/RasterDataSourceProviderConfiguration-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">storageLevels</span> property

</div>

<div class="section multi-line-signature">

List<span class="signature">\<<wbr></wbr><span class="type-parameter">int</span>\></span> <span class="name">storageLevels</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

The storage levels available for this data source. Supported range \[0, 31\]. At least one level must be available for this provider to be used as a source of data. At storage level zero, the whole world is represented by one tile. At storage level 1 the world is split in 2x2 tiles (or in 2x1 tiles, depending on the tiling scheme). The tiling process continues in this fashion until sufficient granularity has been achieved. In the XYZ addresing scheme for tiles, z value of the tile key coresponds to the storage level. Depending on the available storage levels and the given camera zoom level, the appropriate z value of the tile key will be determined.

</div>

## Implementation

``` dart
List<int> storageLevels;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

