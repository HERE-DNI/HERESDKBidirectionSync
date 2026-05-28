---
title: "RasterDataSourceCacheConfiguration class"
slug: "sdk-for-flutter-navigate-mapview-datasource-rasterdatasourcecacheconfiguration-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RasterDataSourceCacheConfiguration-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview.datasource/RasterDataSourceCacheConfiguration-class.html#constructors">Constructors</a></li>
<li><a href="mapview.datasource/RasterDataSourceCacheConfiguration/RasterDataSourceCacheConfiguration.html">RasterDataSourceCacheConfiguration</a></li>
<li><a href="mapview.datasource/RasterDataSourceCacheConfiguration/RasterDataSourceCacheConfiguration.withDefaults.html">withDefaults</a></li>
<li class="section-title">
<a href="mapview.datasource/RasterDataSourceCacheConfiguration-class.html#instance-properties">Properties</a>
</li>
<li><a href="mapview.datasource/RasterDataSourceCacheConfiguration/diskSize.html">diskSize</a></li>
<li class="inherited"><a href="mapview.datasource/RasterDataSourceCacheConfiguration/hashCode.html">hashCode</a></li>
<li><a href="mapview.datasource/RasterDataSourceCacheConfiguration/path.html">path</a></li>
<li class="inherited"><a href="mapview.datasource/RasterDataSourceCacheConfiguration/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="mapview.datasource/RasterDataSourceCacheConfiguration-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="mapview.datasource/RasterDataSourceCacheConfiguration/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="mapview.datasource/RasterDataSourceCacheConfiguration/toString.html">toString</a></li>
<li class="section-title inherited"><a href="mapview.datasource/RasterDataSourceCacheConfiguration-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapview.datasource/RasterDataSourceCacheConfiguration/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-datasource-mapview-datasource-library</li>
<li class="self-crumb">RasterDataSourceCacheConfiguration class</li>
</ol>
<div class="self-name">RasterDataSourceCacheConfiguration</div>
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
<div class="main-content" data-above-sidebar="mapview.datasource/mapview.datasource-library-sidebar.html" data-below-sidebar="mapview.datasource/RasterDataSourceCacheConfiguration-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>RasterDataSourceCacheConfiguration class</h1></div>
<section class="desc markdown">
<p>Configuration of a local data cache.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="RasterDataSourceCacheConfiguration">
/sdk-for-flutter-navigate-mapview-datasource-rasterdatasourcecacheconfiguration-rasterdatasourcecacheconfiguration(String path, int diskSize)
</dt>
<dd>
          Constructs a Cache object from the provided path and cache size.
        </dd>
<dt class="callable" id="RasterDataSourceCacheConfiguration.withDefaults">
/sdk-for-flutter-navigate-mapview-datasource-rasterdatasourcecacheconfiguration-rasterdatasourcecacheconfiguration-withdefaults(String path)
</dt>
<dd>
          Constructs a Cache object from the provided path and a default cache size of 32 MiB.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="diskSize">
/sdk-for-flutter-navigate-mapview-datasource-rasterdatasourcecacheconfiguration-disksize
↔ int
</dt>
<dd>
  The maximum size to use on disk for the cache, in bytes. Default is 32 MiB.
This cache is independent from the map cache as defined via <code>SDKOptions</code>.
Its size is only limited by the total device storage capacity.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-mapview-datasource-rasterdatasourcecacheconfiguration-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="path">
/sdk-for-flutter-navigate-mapview-datasource-rasterdatasourcecacheconfiguration-path
↔ String
</dt>
<dd>
  The path to the directory to use for the cache. By default, the map gets initialized with a
data path which can be fetched from <code>SDKOptions.cachePath</code>. The cache will be relative to this path,
unless an absolute path is provided. The cache can be stored in an internal/external storage as long
as the app has read/write permissions.
Empty string means the data path will be used for caching.
If the provided path, either as absolute path or as relative path is invalid,
then caching will be disabled.
There is no contraint regarding the existence of the path. If the path does not exist
but is valid, it will be created.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-mapview-datasource-rasterdatasourcecacheconfiguration-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-mapview-datasource-rasterdatasourcecacheconfiguration-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-mapview-datasource-rasterdatasourcecacheconfiguration-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-mapview-datasource-rasterdatasourcecacheconfiguration-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">RasterDataSourceCacheConfiguration class</li>
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
