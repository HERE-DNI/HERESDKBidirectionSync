---
title: "RasterDataSourceConfigurationUpdate constructor - RasterDataSourceConfigurationUpdate - mapview.datasource library - Dart API"
slug: "sdk-for-flutter-navigate-mapview.datasource-rasterdatasourceconfigurationupdate-rasterdatasourceconfigurationupdate"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview.datasource/RasterDataSourceConfigurationUpdate-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">RasterDataSourceConfigurationUpdate</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">RasterDataSourceConfigurationUpdate</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-providerHeaders" class="parameter"><span class="type-annotation">Map<span class="signature">\<<wbr></wbr><span class="type-parameter">String</span>, <span class="type-parameter">String</span>\></span>?</span> <span class="parameter-name">providerHeaders</span>, </span>
2.  <span id="sdk-for-flutter-navigate-param-ignoreExpiredData" class="parameter"><span class="type-annotation">bool?</span> <span class="parameter-name">ignoreExpiredData</span>, </span>
3.  <span id="sdk-for-flutter-navigate-param-cacheDiskSize" class="parameter"><span class="type-annotation">int?</span> <span class="parameter-name">cacheDiskSize</span></span>

)

</div>

<div class="section desc markdown">

Creates a new instance.

- `providerHeaders` Optional update of the provider headers. The new list replaces the current one. When not set, no change is made to the current list.
- `ignoreExpiredData` Optional update of the flag indicating whether expired data should be ignored until refreshed. When not set, no change is made to the current flag state.
- `cacheDiskSize` Optional update of the cache disk size, in bytes. When not set, no change is made to the current value.

</div>

## Implementation

``` dart
RasterDataSourceConfigurationUpdate(this.providerHeaders, this.ignoreExpiredData, this.cacheDiskSize);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

