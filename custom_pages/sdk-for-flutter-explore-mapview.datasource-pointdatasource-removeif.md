---
title: "removeIf method - PointDataSource class - mapview.datasource library - Dart API"
slug: "sdk-for-flutter-explore-mapview.datasource-pointdatasource-removeif"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview.datasource/PointDataSource-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">removeIf</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">removeIf</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-removeIf-param-processor" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-datasource-pointdatasourcepointdataprocessor">PointDataSourcePointDataProcessor</a></span> <span class="parameter-name">processor</span></span>

)

</div>

<div class="section desc markdown">

Iterates through all the points from the data source and passes them to the given inspector, one by one.

All points for which the inspector returns `true` get removed from the data source. The inspector cannot update the point data.

- `processor` Point data processor.

</div>

## Implementation

``` dart
void removeIf(PointDataSourcePointDataProcessor processor);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

