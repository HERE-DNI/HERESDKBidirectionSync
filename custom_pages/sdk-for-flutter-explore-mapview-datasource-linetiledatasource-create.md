---
title: "create method - LineTileDataSource class - mapview.datasource library - Dart API"
slug: "sdk-for-flutter-explore-mapview-datasource-linetiledatasource-create"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview.datasource/LineTileDataSource-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">create</span> static method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-explore-mapview-datasource-linetiledatasource-class">LineTileDataSource</a></span> <span class="name">create</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-create-param-context" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapcontext-class">MapContext</a></span> <span class="parameter-name">context</span>, </span>
2.  <span id="sdk-for-flutter-explore-create-param-name" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">name</span>, </span>
3.  <span id="sdk-for-flutter-explore-create-param-tileSource" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-datasource-linetilesource-class">LineTileSource</a></span> <span class="parameter-name">tileSource</span></span>

)

</div>

<div class="section desc markdown">

Creates a named <a href="sdk-for-flutter-explore-mapview-datasource-linetiledatasource-class">LineTileDataSource</a> in the given context over a given <a href="sdk-for-flutter-explore-mapview-datasource-linetilesource-class">LineTileSource</a>.

- `context` Map context to associate the data source with.

- `name` Name of the data source to be created. Must be unique.

- `tileSource` The source of tile data.

Returns <a href="sdk-for-flutter-explore-mapview-datasource-linetiledatasource-class">LineTileDataSource</a>. Instance of the data source created with given name and tile source.

</div>

## Implementation

``` dart
static LineTileDataSource create(MapContext context, String name, LineTileSource tileSource) => $prototype.create(context, name, tileSource);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

