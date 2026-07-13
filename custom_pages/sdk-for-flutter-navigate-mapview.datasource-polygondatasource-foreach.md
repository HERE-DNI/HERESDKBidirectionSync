---
title: "forEach method - PolygonDataSource class - mapview.datasource library - Dart API"
slug: "sdk-for-flutter-navigate-mapview.datasource-polygondatasource-foreach"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview.datasource/PolygonDataSource-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">forEach</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">forEach</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-forEach-param-processor" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-datasource-polygondatasourcepolygondataprocessor">PolygonDataSourcePolygonDataProcessor</a></span> <span class="parameter-name">processor</span></span>

)

</div>

<div class="section desc markdown">

Iterates through all the polygons from the data source and passes them to the given processor, one by one.

The processor can update the polygon data.

The iteration stops after all polygons have been processed or the processor returns false from the process call.

- `processor` Polygon processor.

</div>

## Implementation

``` dart
void forEach(PolygonDataSourcePolygonDataProcessor processor);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

