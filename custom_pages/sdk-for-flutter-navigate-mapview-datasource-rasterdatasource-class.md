---
title: "RasterDataSource class abstract"
slug: "sdk-for-flutter-navigate-mapview-datasource-rasterdatasource-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RasterDataSource-class.html -->


<div>
<h1>RasterDataSource class abstract</h1></div>

<p>Data source to load map layers using a raster image format (jpg, png).</p>
<p>The example below illustrates how to create a raster data source and how to link it to
a newly created map layer.</p>
<pre class="language-dart"><code> final rasterDataSource = RasterDataSource(mapContext, rasterDataSourceConfig);

 var layer = MapLayerBuilder()
     // The name and the type of the data source have to be provided.
     // In our case, the name of the raster data source is in rasterDataSourceConfig.
     .withDataSource(rasterDataSourceConfig.name, MapContentType.rasterImage)
     .forMap(map)
     .withName("rasterLayer")
     .build();
</code></pre>


<h2>Constructors</h2>
<ul><li><a href="/sdk-for-flutter-navigate-mapview-datasource-rasterdatasource-rasterdatasource">RasterDataSource</a></li><li><a href="/sdk-for-flutter-navigate-mapview-datasource-rasterdatasource-rasterdatasource-withconfigurationandlistener">RasterDataSource.withConfigurationAndListener</a></li><li><a href="/sdk-for-flutter-navigate-mapview-datasource-rasterdatasource-rasterdatasource-withtilesource">RasterDataSource.withTileSource</a></li><li><a href="/sdk-for-flutter-navigate-mapview-datasource-rasterdatasource-rasterdatasource-withtilesourceandlistener">RasterDataSource.withTileSourceAndListener</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="/sdk-for-flutter-navigate-mapview-datasource-rasterdatasource-hashcode">hashCode</a></li><li><a href="/sdk-for-flutter-navigate-mapview-datasource-rasterdatasource-runtimetype">runtimeType</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="/sdk-for-flutter-navigate-mapview-datasource-rasterdatasource-addlistener">addListener</a></li><li><a href="/sdk-for-flutter-navigate-mapview-datasource-rasterdatasource-changeconfiguration">changeConfiguration</a></li><li><a href="/sdk-for-flutter-navigate-mapview-datasource-rasterdatasource-destroy">destroy</a></li><li><a href="/sdk-for-flutter-navigate-mapview-datasource-rasterdatasource-nosuchmethod">noSuchMethod</a></li><li><a href="/sdk-for-flutter-navigate-mapview-datasource-rasterdatasource-removelistener">removeListener</a></li><li><a href="/sdk-for-flutter-navigate-mapview-datasource-rasterdatasource-removelisteners">removeListeners</a></li><li><a href="/sdk-for-flutter-navigate-mapview-datasource-rasterdatasource-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="/sdk-for-flutter-navigate-mapview-datasource-rasterdatasource-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>
