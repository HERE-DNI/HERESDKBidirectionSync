---
title: "Untitled"
slug: "sdk-for-flutter-explore-mapview-datasource-rasterdatasourceproviderconfiguration-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RasterDataSourceProviderConfiguration-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-datasource-mapview-datasource-library</li>
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
/sdk-for-flutter-explore-mapview-datasource-rasterdatasourceproviderconfiguration-rasterdatasourceproviderconfiguration-default(/sdk-for-flutter-explore-mapview-datasource-tileurlprovidercallback urlProvider, /sdk-for-flutter-explore-mapview-datasource-tilingscheme tilingScheme, List&lt;<wbr/>int&gt; storageLevels, bool hasAlphaChannel, Map&lt;<wbr/>String, String&gt;? headers)
</dt>
<dd>
          Creates a new instance.
        </dd>
<dt class="callable" id="RasterDataSourceProviderConfiguration.withDefaults">
/sdk-for-flutter-explore-mapview-datasource-rasterdatasourceproviderconfiguration-rasterdatasourceproviderconfiguration-withdefaults(/sdk-for-flutter-explore-mapview-datasource-tileurlprovidercallback urlProvider, /sdk-for-flutter-explore-mapview-datasource-tilingscheme tilingScheme, List&lt;<wbr/>int&gt; storageLevels)
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
/sdk-for-flutter-explore-mapview-datasource-rasterdatasourceproviderconfiguration-hasalphachannel
↔ bool
</dt>
<dd>
  A flag indicating whether the image content contains an alpha channel for transparency. Default value is <code>false</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-explore-mapview-datasource-rasterdatasourceproviderconfiguration-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="headers">
/sdk-for-flutter-explore-mapview-datasource-rasterdatasourceproviderconfiguration-headers
↔ Map&lt;<wbr/>String, String&gt;?
</dt>
<dd>
  The optional name-value pairs specifying HTTP headers that are passed with each tile request.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-mapview-datasource-rasterdatasourceproviderconfiguration-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="storageLevels">
/sdk-for-flutter-explore-mapview-datasource-rasterdatasourceproviderconfiguration-storagelevels
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
/sdk-for-flutter-explore-mapview-datasource-rasterdatasourceproviderconfiguration-tilingscheme
↔ /sdk-for-flutter-explore-mapview-datasource-tilingscheme
</dt>
<dd>
  The tiling scheme used by this source.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="urlProvider">
/sdk-for-flutter-explore-mapview-datasource-rasterdatasourceproviderconfiguration-urlprovider
↔ /sdk-for-flutter-explore-mapview-datasource-tileurlprovidercallback
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
/sdk-for-flutter-explore-mapview-datasource-rasterdatasourceproviderconfiguration-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-mapview-datasource-rasterdatasourceproviderconfiguration-tostring(<wbr/>)
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
/sdk-for-flutter-explore-mapview-datasource-rasterdatasourceproviderconfiguration-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-datasource-mapview-datasource-library</li>
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



</div>
`
}</HTMLBlock>
