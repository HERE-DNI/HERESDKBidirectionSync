---
title: "RasterDataSource.withConfigurationAndListener constructor - RasterDataSource - mapview.datasource library - Dart API"
slug: "sdk-for-flutter-navigate-mapview.datasource-rasterdatasource-rasterdatasource-withconfigurationandlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RasterDataSource.withConfigurationAndListener.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview.datasource/RasterDataSource-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">RasterDataSource.withConfigurationAndListener</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">RasterDataSource.withConfigurationAndListener</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-withConfigurationAndListener-param-context" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapcontext-class">MapContext</a></span> <span class="parameter-name">context</span>, </span>
2.  <span id="sdk-for-flutter-navigate-withConfigurationAndListener-param-configuration" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-datasource-rasterdatasourceconfiguration-class">RasterDataSourceConfiguration</a></span> <span class="parameter-name">configuration</span>, </span>
3.  <span id="sdk-for-flutter-navigate-withConfigurationAndListener-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-datasource-rasterdatasourcelistener-class">RasterDataSourceListener</a></span> <span class="parameter-name">listener</span></span>

)

</div>

<div class="section desc markdown">

Creates a RasterDataSource instance with the provided data source configuration and registers a listener.

- `context` The map context to associate the data source with.

- `configuration` The data source configuration object to use.

- `listener` The initial listener to be registered for receiving state notifications. Due to the asynchronous nature of the data source initialization, the listeners registered later might miss some notifications. This listener is guaranteed to receive all notifications. The state notifications can occur on an arbitrary thread.

</div>

## Implementation

``` dart
factory RasterDataSource.withConfigurationAndListener(MapContext context, RasterDataSourceConfiguration configuration, RasterDataSourceListener listener) => $prototype.withConfigurationAndListener(context, configuration, listener);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
