---
title: "Constructors"
slug: "sdk-for-flutter-explore-mapview-datasource-rasterdatasource-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- RasterDataSource-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview.datasource/RasterDataSource-class.html#constructors">Constructors</a></li>
<li><a href="mapview.datasource/RasterDataSource/RasterDataSource.html">RasterDataSource</a></li>
<li><a href="mapview.datasource/RasterDataSource/RasterDataSource.withConfigurationAndListener.html">withConfigurationAndListener</a></li>
<li><a href="mapview.datasource/RasterDataSource/RasterDataSource.withTileSource.html">withTileSource</a></li>
<li><a href="mapview.datasource/RasterDataSource/RasterDataSource.withTileSourceAndListener.html">withTileSourceAndListener</a></li>
<li class="section-title inherited">
<a href="mapview.datasource/RasterDataSource-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="mapview.datasource/RasterDataSource/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="mapview.datasource/RasterDataSource/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="mapview.datasource/RasterDataSource-class.html#instance-methods">Methods</a></li>
<li><a href="mapview.datasource/RasterDataSource/addListener.html">addListener</a></li>
<li><a href="mapview.datasource/RasterDataSource/changeConfiguration.html">changeConfiguration</a></li>
<li><a href="mapview.datasource/RasterDataSource/destroy.html">destroy</a></li>
<li class="inherited"><a href="mapview.datasource/RasterDataSource/noSuchMethod.html">noSuchMethod</a></li>
<li><a href="mapview.datasource/RasterDataSource/removeListener.html">removeListener</a></li>
<li><a href="mapview.datasource/RasterDataSource/removeListeners.html">removeListeners</a></li>
<li class="inherited"><a href="mapview.datasource/RasterDataSource/toString.html">toString</a></li>
<li class="section-title inherited"><a href="mapview.datasource/RasterDataSource-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapview.datasource/RasterDataSource/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../mapview.datasource/mapview.datasource-library.html">/sdk-for-flutter-explore-mapview-datasource-mapview-datasource-library</a></li>
<li class="self-crumb">RasterDataSource class</li>
</ol>
<div class="self-name">RasterDataSource</div>
<form class="search navbar-right" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-box" placeholder="Loading search..." type="text"/>
</form>
<div class="toggle" id="theme-button" title="Toggle brightness">
<label for="theme">
<input id="theme" type="checkbox" value="light-theme"/>

        dark_mode
      

        light_mode
      
</label>
</div>
</header>
<main>
<div class="main-content" data-above-sidebar="mapview.datasource/mapview.datasource-library-sidebar.html" data-below-sidebar="mapview.datasource/RasterDataSource-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>RasterDataSource class abstract</h1></div>
<section class="desc markdown">
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
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="RasterDataSource">
<a href="../mapview.datasource/RasterDataSource/RasterDataSource.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasource-rasterdatasource</a>(<a href="../mapview/MapContext-class.html">/sdk-for-flutter-explore-mapview-mapcontext-class</a> context, <a href="../mapview.datasource/RasterDataSourceConfiguration-class.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasourceconfiguration-class</a> configuration)
</dt>
<dd>
          Creates a RasterDataSource instance with the provided data source configuration.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="RasterDataSource.withConfigurationAndListener">
<a href="../mapview.datasource/RasterDataSource/RasterDataSource.withConfigurationAndListener.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasource-rasterdatasource-withconfigurationandlistener</a>(<a href="../mapview/MapContext-class.html">/sdk-for-flutter-explore-mapview-mapcontext-class</a> context, <a href="../mapview.datasource/RasterDataSourceConfiguration-class.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasourceconfiguration-class</a> configuration, <a href="../mapview.datasource/RasterDataSourceListener-class.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasourcelistener-class</a> listener)
</dt>
<dd>
          Creates a RasterDataSource instance with the provided data source configuration and
registers a listener.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="RasterDataSource.withTileSource">
<a href="../mapview.datasource/RasterDataSource/RasterDataSource.withTileSource.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasource-rasterdatasource-withtilesource</a>(<a href="../mapview/MapContext-class.html">/sdk-for-flutter-explore-mapview-mapcontext-class</a> context, String name, <a href="../mapview.datasource/RasterTileSource-class.html">/sdk-for-flutter-explore-mapview-datasource-rastertilesource-class</a> tileSource)
</dt>
<dd>
          Creates a RasterDataSource instance with the provided raster tile source.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="RasterDataSource.withTileSourceAndListener">
<a href="../mapview.datasource/RasterDataSource/RasterDataSource.withTileSourceAndListener.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasource-rasterdatasource-withtilesourceandlistener</a>(<a href="../mapview/MapContext-class.html">/sdk-for-flutter-explore-mapview-mapcontext-class</a> context, String name, <a href="../mapview.datasource/RasterTileSource-class.html">/sdk-for-flutter-explore-mapview-datasource-rastertilesource-class</a> tileSource, <a href="../mapview.datasource/RasterDataSourceListener-class.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasourcelistener-class</a> listener)
</dt>
<dd>
          Creates a RasterDataSource instance with the provided raster tile source and registers
a listener.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
<a href="../mapview.datasource/RasterDataSource/hashCode.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasource-hashcode</a>
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../mapview.datasource/RasterDataSource/runtimeType.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasource-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="addListener">
<a href="../mapview.datasource/RasterDataSource/addListener.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasource-addlistener</a>(<wbr/><a href="../mapview.datasource/RasterDataSourceListener-class.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasourcelistener-class</a> listener)
    → void

</dt>
<dd>
  Add listener for receiving state notifications.
  

</dd>
<dt class="callable" id="changeConfiguration">
<a href="../mapview.datasource/RasterDataSource/changeConfiguration.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasource-changeconfiguration</a>(<wbr/><a href="../mapview.datasource/RasterDataSourceConfigurationUpdate-class.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasourceconfigurationupdate-class</a> configuration)
    → void

</dt>
<dd>
  Applies the configuration update to the data source.
  

</dd>
<dt class="callable" id="destroy">
<a href="../mapview.datasource/RasterDataSource/destroy.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasource-destroy</a>(<wbr/>)
    → void

</dt>
<dd>
  Frees all internally used resources.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
<a href="../mapview.datasource/RasterDataSource/noSuchMethod.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasource-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="removeListener">
<a href="../mapview.datasource/RasterDataSource/removeListener.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasource-removelistener</a>(<wbr/><a href="../mapview.datasource/RasterDataSourceListener-class.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasourcelistener-class</a> listener)
    → void

</dt>
<dd>
  Remove a listener from receiving state notifications.
  

</dd>
<dt class="callable" id="removeListeners">
<a href="../mapview.datasource/RasterDataSource/removeListeners.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasource-removelisteners</a>(<wbr/>)
    → void

</dt>
<dd>
  Remove all listeners from receiving state notifications.
  

</dd>
<dt class="callable inherited" id="toString">
<a href="../mapview.datasource/RasterDataSource/toString.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasource-tostring</a>(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
<a href="../mapview.datasource/RasterDataSource/operator_equals.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasource-operator-equals</a>(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../mapview.datasource/mapview.datasource-library.html">/sdk-for-flutter-explore-mapview-datasource-mapview-datasource-library</a></li>
<li class="self-crumb">RasterDataSource class</li>
</ol>
<h5>mapview.datasource library</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>
</div></div>
</div>
</HTMLBlock>
