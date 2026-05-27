---
title: "Constructors"
slug: "sdk-for-flutter-explore-mapview-datasource-rasterdatasourceproviderconfiguration-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- RasterDataSourceProviderConfiguration-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview.datasource/RasterDataSourceProviderConfiguration-class.html#constructors">Constructors</a></li>
<li><a href="mapview.datasource/RasterDataSourceProviderConfiguration/RasterDataSourceProviderConfiguration.Default.html">Default</a></li>
<li><a href="mapview.datasource/RasterDataSourceProviderConfiguration/RasterDataSourceProviderConfiguration.withDefaults.html">withDefaults</a></li>
<li class="section-title">
<a href="mapview.datasource/RasterDataSourceProviderConfiguration-class.html#instance-properties">Properties</a>
</li>
<li><a href="mapview.datasource/RasterDataSourceProviderConfiguration/hasAlphaChannel.html">hasAlphaChannel</a></li>
<li class="inherited"><a href="mapview.datasource/RasterDataSourceProviderConfiguration/hashCode.html">hashCode</a></li>
<li><a href="mapview.datasource/RasterDataSourceProviderConfiguration/headers.html">headers</a></li>
<li class="inherited"><a href="mapview.datasource/RasterDataSourceProviderConfiguration/runtimeType.html">runtimeType</a></li>
<li><a href="mapview.datasource/RasterDataSourceProviderConfiguration/storageLevels.html">storageLevels</a></li>
<li><a href="mapview.datasource/RasterDataSourceProviderConfiguration/tilingScheme.html">tilingScheme</a></li>
<li><a href="mapview.datasource/RasterDataSourceProviderConfiguration/urlProvider.html">urlProvider</a></li>
<li class="section-title inherited"><a href="mapview.datasource/RasterDataSourceProviderConfiguration-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="mapview.datasource/RasterDataSourceProviderConfiguration/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="mapview.datasource/RasterDataSourceProviderConfiguration/toString.html">toString</a></li>
<li class="section-title inherited"><a href="mapview.datasource/RasterDataSourceProviderConfiguration-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapview.datasource/RasterDataSourceProviderConfiguration/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../mapview.datasource/mapview.datasource-library.html">/sdk-for-flutter-explore-mapview-datasource-mapview-datasource-library</a></li>
<li class="self-crumb">RasterDataSourceProviderConfiguration class</li>
</ol>
<div class="self-name">RasterDataSourceProviderConfiguration</div>
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
<div class="main-content" data-above-sidebar="mapview.datasource/mapview.datasource-library-sidebar.html" data-below-sidebar="mapview.datasource/RasterDataSourceProviderConfiguration-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>RasterDataSourceProviderConfiguration class</h1></div>
<section class="desc markdown">
<p>Configuration of a data provider.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="RasterDataSourceProviderConfiguration.Default">
<a href="../mapview.datasource/RasterDataSourceProviderConfiguration/RasterDataSourceProviderConfiguration.Default.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasourceproviderconfiguration-rasterdatasourceproviderconfiguration-default</a>(<a href="../mapview.datasource/TileUrlProviderCallback.html">/sdk-for-flutter-explore-mapview-datasource-tileurlprovidercallback</a> urlProvider, <a href="../mapview.datasource/TilingScheme.html">/sdk-for-flutter-explore-mapview-datasource-tilingscheme</a> tilingScheme, List&lt;<wbr/>int&gt; storageLevels, bool hasAlphaChannel, Map&lt;<wbr/>String, String&gt;? headers)
</dt>
<dd>
          Creates a new instance.
        </dd>
<dt class="callable" id="RasterDataSourceProviderConfiguration.withDefaults">
<a href="../mapview.datasource/RasterDataSourceProviderConfiguration/RasterDataSourceProviderConfiguration.withDefaults.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasourceproviderconfiguration-rasterdatasourceproviderconfiguration-withdefaults</a>(<a href="../mapview.datasource/TileUrlProviderCallback.html">/sdk-for-flutter-explore-mapview-datasource-tileurlprovidercallback</a> urlProvider, <a href="../mapview.datasource/TilingScheme.html">/sdk-for-flutter-explore-mapview-datasource-tilingscheme</a> tilingScheme, List&lt;<wbr/>int&gt; storageLevels)
</dt>
<dd>
          Creates a new instance.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="hasAlphaChannel">
<a href="../mapview.datasource/RasterDataSourceProviderConfiguration/hasAlphaChannel.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasourceproviderconfiguration-hasalphachannel</a>
↔ bool
</dt>
<dd>
  A flag indicating whether the image content contains an alpha channel for transparency. Default value is <code>false</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="hashCode">
<a href="../mapview.datasource/RasterDataSourceProviderConfiguration/hashCode.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasourceproviderconfiguration-hashcode</a>
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="headers">
<a href="../mapview.datasource/RasterDataSourceProviderConfiguration/headers.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasourceproviderconfiguration-headers</a>
↔ Map&lt;<wbr/>String, String&gt;?
</dt>
<dd>
  The optional name-value pairs specifying HTTP headers that are passed with each tile request.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../mapview.datasource/RasterDataSourceProviderConfiguration/runtimeType.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasourceproviderconfiguration-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="storageLevels">
<a href="../mapview.datasource/RasterDataSourceProviderConfiguration/storageLevels.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasourceproviderconfiguration-storagelevels</a>
↔ List&lt;<wbr/>int&gt;
</dt>
<dd>
  The storage levels available for this data source. Supported range [0, 31].
At least one level must be available for this provider to be used as a source of data.
At storage level zero, the whole world is represented by one tile. At storage level 1
the world is split in 2x2 tiles (or in 2x1 tiles, depending on the tiling scheme).
The tiling process continues in this fashion until sufficient granularity has been
achieved. In the XYZ addresing scheme for tiles, z value of the tile key coresponds
to the storage level.
Depending on the available storage levels and the given camera zoom level, the
appropriate z value of the tile key will be determined.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="tilingScheme">
<a href="../mapview.datasource/RasterDataSourceProviderConfiguration/tilingScheme.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasourceproviderconfiguration-tilingscheme</a>
↔ <a href="../mapview.datasource/TilingScheme.html">/sdk-for-flutter-explore-mapview-datasource-tilingscheme</a>
</dt>
<dd>
  The tiling scheme used by this source.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="urlProvider">
<a href="../mapview.datasource/RasterDataSourceProviderConfiguration/urlProvider.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasourceproviderconfiguration-urlprovider</a>
↔ <a href="../mapview.datasource/TileUrlProviderCallback.html">/sdk-for-flutter-explore-mapview-datasource-tileurlprovidercallback</a>
</dt>
<dd>
  Provides a function that generates URLs based on tile coordinates and storage level.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
<a href="../mapview.datasource/RasterDataSourceProviderConfiguration/noSuchMethod.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasourceproviderconfiguration-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../mapview.datasource/RasterDataSourceProviderConfiguration/toString.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasourceproviderconfiguration-tostring</a>(<wbr/>)
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
<a href="../mapview.datasource/RasterDataSourceProviderConfiguration/operator_equals.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasourceproviderconfiguration-operator-equals</a>(<wbr/>Object other)
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
<li class="self-crumb">RasterDataSourceProviderConfiguration class</li>
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
