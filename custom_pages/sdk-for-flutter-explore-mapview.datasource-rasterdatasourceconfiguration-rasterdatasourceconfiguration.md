---
title: "RasterDataSourceConfiguration constructor - RasterDataSourceConfiguration - mapview.datasource library - Dart API"
slug: "sdk-for-flutter-explore-mapview.datasource-rasterdatasourceconfiguration-rasterdatasourceconfiguration"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview.datasource/RasterDataSourceConfiguration-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">RasterDataSourceConfiguration</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">RasterDataSourceConfiguration</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-param-name" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">name</span>, </span>
2.  <span id="sdk-for-flutter-explore-param-provider" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-datasource-rasterdatasourceproviderconfiguration-class">RasterDataSourceProviderConfiguration</a></span> <span class="parameter-name">provider</span>, </span>
3.  <span id="sdk-for-flutter-explore-param-cache" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-datasource-rasterdatasourcecacheconfiguration-class">RasterDataSourceCacheConfiguration</a></span> <span class="parameter-name">cache</span>, </span>
4.  <span id="sdk-for-flutter-explore-param-ignoreExpiredData" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">ignoreExpiredData</span>, </span>

)

</div>

<div class="section desc markdown">

Creates a new instance.

- `name` The unique name of the data source.
- `provider` Data provider configuration.
- `cache` Local cache configuration.
- `ignoreExpiredData` A flag indicating whether expired data should be ignored until refreshed. Default value is `false`.

</div>

## Implementation

``` dart
RasterDataSourceConfiguration(this.name, this.provider, this.cache, this.ignoreExpiredData);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

