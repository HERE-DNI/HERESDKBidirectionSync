---
title: "PointDataSourcePointDataProcessor typedef - mapview.datasource library - Dart API"
slug: "sdk-for-flutter-navigate-mapview.datasource-pointdatasourcepointdataprocessor"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview.datasource/mapview.datasource-library-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-typedef">PointDataSourcePointDataProcessor</span> typedef

</div>

<div class="section multi-line-signature">

<span class="name">PointDataSourcePointDataProcessor</span> = <span class="returntype">bool Function<span class="signature">(<span id="sdk-for-flutter-navigate-param-pointAccessor" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-datasource-pointdataaccessor-class">PointDataAccessor</a></span> <span class="parameter-name">pointAccessor</span></span>)</span></span>

</div>

<div class="section desc markdown">

Called for each point, allowing inspection, removal or update of coordinates and attributes.

- `pointAccessor` the point data accessor.

Returns value indicating the result of the processing.

</div>

## Implementation

``` dart
typedef PointDataSourcePointDataProcessor = bool Function(PointDataAccessor pointAccessor);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

