---
title: "PolygonDataSourcePolygonDataProcessor typedef - mapview.datasource library - Dart API"
slug: "sdk-for-flutter-explore-mapview-datasource-polygondatasourcepolygondataprocessor"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview.datasource/mapview.datasource-library-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-typedef">PolygonDataSourcePolygonDataProcessor</span> typedef

</div>

<div class="section multi-line-signature">

<span class="name">PolygonDataSourcePolygonDataProcessor</span> = <span class="returntype">bool Function<span class="signature">(<span id="sdk-for-flutter-explore-param-polygonAccessor" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-datasource-polygondataaccessor-class">PolygonDataAccessor</a></span> <span class="parameter-name">polygonAccessor</span></span>)</span></span>

</div>

<div class="section desc markdown">

Called for each polygon, allowing inspection, removal or update of coordinates and attributes.

- `polygonAccessor` the polygon data accessor.

Returns value indicating the result of the processing.

</div>

## Implementation

``` dart
typedef PolygonDataSourcePolygonDataProcessor = bool Function(PolygonDataAccessor polygonAccessor);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

