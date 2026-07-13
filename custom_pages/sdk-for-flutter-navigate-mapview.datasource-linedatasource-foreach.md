---
title: "forEach method - LineDataSource class - mapview.datasource library - Dart API"
slug: "sdk-for-flutter-navigate-mapview.datasource-linedatasource-foreach"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview.datasource/LineDataSource-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">forEach</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">forEach</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-forEach-param-processor" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-datasource-linedatasourcelinedataprocessor">LineDataSourceLineDataProcessor</a></span> <span class="parameter-name">processor</span></span>

)

</div>

<div class="section desc markdown">

Iterates through all the lines from the data source and passes them to the given processor, one by one.

The processor can update the line data. The iteration stops after all lines have been processed or the processor returns false from the process call.

- `processor` Line processor.

</div>

## Implementation

``` dart
void forEach(LineDataSourceLineDataProcessor processor);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

