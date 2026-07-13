---
title: "RasterDataSource class - mapview.datasource library - Dart API"
slug: "sdk-for-flutter-navigate-mapview.datasource-rasterdatasource-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RasterDataSource-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview.datasource/mapview.datasource-library-sidebar.html" data-below-sidebar="mapview.datasource/RasterDataSource-class-sidebar.html">

<div>

# <span class="kind-class">RasterDataSource</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Data source to load map layers using a raster image format (jpg, png).

The example below illustrates how to create a raster data source and how to link it to a newly created map layer.

``` dart
final rasterDataSource = RasterDataSource(mapContext, rasterDataSourceConfig);

 var layer = MapLayerBuilder()
     // The name and the type of the data source have to be provided.
     // In our case, the name of the raster data source is in rasterDataSourceConfig.
     .withDataSource(rasterDataSourceConfig.name, MapContentType.rasterImage)
     .forMap(map)
     .withName("rasterLayer")
     .build();
```

</pre>

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-rasterdatasource-rasterdatasource">RasterDataSource</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-context" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapcontext-class">MapContext</a></span> <span class="parameter-name">context</span>, </span><span id="sdk-for-flutter-navigate-param-configuration" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-datasource-rasterdatasourceconfiguration-class">RasterDataSourceConfiguration</a></span> <span class="parameter-name">configuration</span></span>)</span>  
Creates a RasterDataSource instance with the provided data source configuration.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-rasterdatasource-rasterdatasource-withconfigurationandlistener">RasterDataSource.withConfigurationAndListener</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withConfigurationAndListener-param-context" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapcontext-class">MapContext</a></span> <span class="parameter-name">context</span>, </span><span id="sdk-for-flutter-navigate-withConfigurationAndListener-param-configuration" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-datasource-rasterdatasourceconfiguration-class">RasterDataSourceConfiguration</a></span> <span class="parameter-name">configuration</span>, </span><span id="sdk-for-flutter-navigate-withConfigurationAndListener-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-datasource-rasterdatasourcelistener-class">RasterDataSourceListener</a></span> <span class="parameter-name">listener</span></span>)</span>  
Creates a RasterDataSource instance with the provided data source configuration and registers a listener.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-rasterdatasource-rasterdatasource-withtilesource">RasterDataSource.withTileSource</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withTileSource-param-context" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapcontext-class">MapContext</a></span> <span class="parameter-name">context</span>, </span><span id="sdk-for-flutter-navigate-withTileSource-param-name" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">name</span>, </span><span id="sdk-for-flutter-navigate-withTileSource-param-tileSource" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-datasource-rastertilesource-class">RasterTileSource</a></span> <span class="parameter-name">tileSource</span></span>)</span>  
Creates a RasterDataSource instance with the provided raster tile source.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-rasterdatasource-rasterdatasource-withtilesourceandlistener">RasterDataSource.withTileSourceAndListener</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withTileSourceAndListener-param-context" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapcontext-class">MapContext</a></span> <span class="parameter-name">context</span>, </span><span id="sdk-for-flutter-navigate-withTileSourceAndListener-param-name" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">name</span>, </span><span id="sdk-for-flutter-navigate-withTileSourceAndListener-param-tileSource" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-datasource-rastertilesource-class">RasterTileSource</a></span> <span class="parameter-name">tileSource</span>, </span><span id="sdk-for-flutter-navigate-withTileSourceAndListener-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-datasource-rasterdatasourcelistener-class">RasterDataSourceListener</a></span> <span class="parameter-name">listener</span></span>)</span>  
Creates a RasterDataSource instance with the provided raster tile source and registers a listener.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-rasterdatasource-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-rasterdatasource-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-rasterdatasource-addlistener">addListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-addListener-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-datasource-rasterdatasourcelistener-class">RasterDataSourceListener</a></span> <span class="parameter-name">listener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Add listener for receiving state notifications.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-rasterdatasource-changeconfiguration">changeConfiguration</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-changeConfiguration-param-configuration" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-datasource-rasterdatasourceconfigurationupdate-class">RasterDataSourceConfigurationUpdate</a></span> <span class="parameter-name">configuration</span></span>) <span class="returntype parameter">→ void</span> </span>  
Applies the configuration update to the data source.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-rasterdatasource-destroy">destroy</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Frees all internally used resources.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-rasterdatasource-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-rasterdatasource-removelistener">removeListener</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-removeListener-param-listener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-datasource-rasterdatasourcelistener-class">RasterDataSourceListener</a></span> <span class="parameter-name">listener</span></span>) <span class="returntype parameter">→ void</span> </span>  
Remove a listener from receiving state notifications.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-rasterdatasource-removelisteners">removeListeners</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Remove all listeners from receiving state notifications.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-rasterdatasource-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-mapview-datasource-rasterdatasource-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
