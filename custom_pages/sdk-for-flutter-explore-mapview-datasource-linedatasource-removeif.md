---
title: "removeIf method - LineDataSource class - mapview.datasource library - Dart API"
slug: "sdk-for-flutter-explore-mapview-datasource-linedatasource-removeif"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview.datasource/LineDataSource-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">removeIf</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">removeIf</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-removeIf-param-inspector" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-datasource-linedatasourcelinedataprocessor">LineDataSourceLineDataProcessor</a></span> <span class="parameter-name">inspector</span></span>

)

</div>

<div class="section desc markdown">

Iterates through all the lines from the data source and passes them to the given inspector, one by one.

All lines for which the inspector returns `true` get removed from the data source. The inspector cannot update the line data.

- `inspector` Line data processor.

</div>

## Implementation

``` dart
void removeIf(LineDataSourceLineDataProcessor inspector);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

