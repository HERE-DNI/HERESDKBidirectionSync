---
title: "forEach method - PointDataSource class - mapview.datasource library - Dart API"
slug: "sdk-for-flutter-explore-mapview.datasource-pointdatasource-foreach"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview.datasource/PointDataSource-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">forEach</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">forEach</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-forEach-param-processor" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-datasource-pointdatasourcepointdataprocessor">PointDataSourcePointDataProcessor</a></span> <span class="parameter-name">processor</span></span>

)

</div>

<div class="section desc markdown">

Iterates through all the points from the data source and passes them to the given processor, one by one.

The processor can update the point data.

The iteration stops after all points have been processed or the processor returns false from the process call.

- `processor` Point data processor.

</div>

## Implementation

``` dart
void forEach(PointDataSourcePointDataProcessor processor);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

