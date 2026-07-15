---
title: "LineDataSourceLineDataProcessor typedef - mapview.datasource library - Dart API"
slug: "sdk-for-flutter-explore-mapview-datasource-linedatasourcelinedataprocessor"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview.datasource/mapview.datasource-library-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-typedef">LineDataSourceLineDataProcessor</span> typedef

</div>

<div class="section multi-line-signature">

<span class="name">LineDataSourceLineDataProcessor</span> = <span class="returntype">bool Function<span class="signature">(<span id="sdk-for-flutter-explore-param-lineAccessor" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-datasource-linedataaccessor-class">LineDataAccessor</a></span> <span class="parameter-name">lineAccessor</span></span>)</span></span>

</div>

<div class="section desc markdown">

Called for each line, allowing inspection, removal or update of coordinates and attributes.

- `lineAccessor` the line data accessor.

Returns value indicating the result of the processing.

</div>

## Implementation

``` dart
typedef LineDataSourceLineDataProcessor = bool Function(LineDataAccessor lineAccessor);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

