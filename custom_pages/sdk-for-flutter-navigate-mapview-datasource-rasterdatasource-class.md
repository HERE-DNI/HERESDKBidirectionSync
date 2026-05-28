---
title: "RasterDataSource class abstract"
slug: "sdk-for-flutter-navigate-mapview-datasource-rasterdatasource-class"
---

<HTMLBlock>{
`
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
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-datasource-mapview-datasource-library</li>
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
/sdk-for-flutter-navigate-mapview-datasource-rasterdatasource-rasterdatasource(/sdk-for-flutter-navigate-mapview-mapcontext-class context, /sdk-for-flutter-navigate-mapview-datasource-rasterdatasourceconfiguration-class configuration)
</dt>
<dd>
          Creates a RasterDataSource instance with the provided data source configuration.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="RasterDataSource.withConfigurationAndListener">
/sdk-for-flutter-navigate-mapview-datasource-rasterdatasource-rasterdatasource-withconfigurationandlistener(/sdk-for-flutter-navigate-mapview-mapcontext-class context, /sdk-for-flutter-navigate-mapview-datasource-rasterdatasourceconfiguration-class configuration, /sdk-for-flutter-navigate-mapview-datasource-rasterdatasourcelistener-class listener)
</dt>
<dd>
          Creates a RasterDataSource instance with the provided data source configuration and
registers a listener.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="RasterDataSource.withTileSource">
/sdk-for-flutter-navigate-mapview-datasource-rasterdatasource-rasterdatasource-withtilesource(/sdk-for-flutter-navigate-mapview-mapcontext-class context, String name, /sdk-for-flutter-navigate-mapview-datasource-rastertilesource-class tileSource)
</dt>
<dd>
          Creates a RasterDataSource instance with the provided raster tile source.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="RasterDataSource.withTileSourceAndListener">
/sdk-for-flutter-navigate-mapview-datasource-rasterdatasource-rasterdatasource-withtilesourceandlistener(/sdk-for-flutter-navigate-mapview-mapcontext-class context, String name, /sdk-for-flutter-navigate-mapview-datasource-rastertilesource-class tileSource, /sdk-for-flutter-navigate-mapview-datasource-rasterdatasourcelistener-class listener)
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
/sdk-for-flutter-navigate-mapview-datasource-rasterdatasource-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-mapview-datasource-rasterdatasource-runtimetype
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
/sdk-for-flutter-navigate-mapview-datasource-rasterdatasource-addlistener(<wbr/>/sdk-for-flutter-navigate-mapview-datasource-rasterdatasourcelistener-class listener)
    → void

</dt>
<dd>
  Add listener for receiving state notifications.
  

</dd>
<dt class="callable" id="changeConfiguration">
/sdk-for-flutter-navigate-mapview-datasource-rasterdatasource-changeconfiguration(<wbr/>/sdk-for-flutter-navigate-mapview-datasource-rasterdatasourceconfigurationupdate-class configuration)
    → void

</dt>
<dd>
  Applies the configuration update to the data source.
  

</dd>
<dt class="callable" id="destroy">
/sdk-for-flutter-navigate-mapview-datasource-rasterdatasource-destroy(<wbr/>)
    → void

</dt>
<dd>
  Frees all internally used resources.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-mapview-datasource-rasterdatasource-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="removeListener">
/sdk-for-flutter-navigate-mapview-datasource-rasterdatasource-removelistener(<wbr/>/sdk-for-flutter-navigate-mapview-datasource-rasterdatasourcelistener-class listener)
    → void

</dt>
<dd>
  Remove a listener from receiving state notifications.
  

</dd>
<dt class="callable" id="removeListeners">
/sdk-for-flutter-navigate-mapview-datasource-rasterdatasource-removelisteners(<wbr/>)
    → void

</dt>
<dd>
  Remove all listeners from receiving state notifications.
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-mapview-datasource-rasterdatasource-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-mapview-datasource-rasterdatasource-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-datasource-mapview-datasource-library</li>
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
`
}</HTMLBlock>
