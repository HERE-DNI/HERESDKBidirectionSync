---
title: "Constructors"
slug: "sdk-for-flutter-explore-mapview-datasource-rasterdatasourceconfiguration-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- RasterDataSourceConfiguration-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview.datasource/RasterDataSourceConfiguration-class.html#constructors">Constructors</a></li>
<li><a href="mapview.datasource/RasterDataSourceConfiguration/RasterDataSourceConfiguration.html">RasterDataSourceConfiguration</a></li>
<li><a href="mapview.datasource/RasterDataSourceConfiguration/RasterDataSourceConfiguration.withDefaults.html">withDefaults</a></li>
<li class="section-title">
<a href="mapview.datasource/RasterDataSourceConfiguration-class.html#instance-properties">Properties</a>
</li>
<li><a href="mapview.datasource/RasterDataSourceConfiguration/cache.html">cache</a></li>
<li class="inherited"><a href="mapview.datasource/RasterDataSourceConfiguration/hashCode.html">hashCode</a></li>
<li><a href="mapview.datasource/RasterDataSourceConfiguration/ignoreExpiredData.html">ignoreExpiredData</a></li>
<li><a href="mapview.datasource/RasterDataSourceConfiguration/name.html">name</a></li>
<li><a href="mapview.datasource/RasterDataSourceConfiguration/provider.html">provider</a></li>
<li class="inherited"><a href="mapview.datasource/RasterDataSourceConfiguration/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="mapview.datasource/RasterDataSourceConfiguration-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="mapview.datasource/RasterDataSourceConfiguration/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="mapview.datasource/RasterDataSourceConfiguration/toString.html">toString</a></li>
<li class="section-title inherited"><a href="mapview.datasource/RasterDataSourceConfiguration-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapview.datasource/RasterDataSourceConfiguration/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../mapview.datasource/mapview.datasource-library.html">/sdk-for-flutter-explore-mapview-datasource-mapview-datasource-library</a></li>
<li class="self-crumb">RasterDataSourceConfiguration class</li>
</ol>
<div class="self-name">RasterDataSourceConfiguration</div>
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
<div class="main-content" data-above-sidebar="mapview.datasource/mapview.datasource-library-sidebar.html" data-below-sidebar="mapview.datasource/RasterDataSourceConfiguration-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>RasterDataSourceConfiguration class</h1></div>
<section class="desc markdown">
<p>Called on the main thread after <code>fromJsonFile()</code> method finishes loading
the configuration.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="RasterDataSourceConfiguration">
<a href="../mapview.datasource/RasterDataSourceConfiguration/RasterDataSourceConfiguration.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasourceconfiguration-rasterdatasourceconfiguration</a>(String name, <a href="../mapview.datasource/RasterDataSourceProviderConfiguration-class.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasourceproviderconfiguration-class</a> provider, <a href="../mapview.datasource/RasterDataSourceCacheConfiguration-class.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasourcecacheconfiguration-class</a> cache, bool ignoreExpiredData)
</dt>
<dd>
          Creates a new instance.
        </dd>
<dt class="callable" id="RasterDataSourceConfiguration.withDefaults">
<a href="../mapview.datasource/RasterDataSourceConfiguration/RasterDataSourceConfiguration.withDefaults.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasourceconfiguration-rasterdatasourceconfiguration-withdefaults</a>(String name, <a href="../mapview.datasource/RasterDataSourceProviderConfiguration-class.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasourceproviderconfiguration-class</a> provider, <a href="../mapview.datasource/RasterDataSourceCacheConfiguration-class.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasourcecacheconfiguration-class</a> cache)
</dt>
<dd>
          Creates a new instance.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="cache">
<a href="../mapview.datasource/RasterDataSourceConfiguration/cache.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasourceconfiguration-cache</a>
↔ <a href="../mapview.datasource/RasterDataSourceCacheConfiguration-class.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasourcecacheconfiguration-class</a>
</dt>
<dd>
  Local cache configuration.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="hashCode">
<a href="../mapview.datasource/RasterDataSourceConfiguration/hashCode.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasourceconfiguration-hashcode</a>
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="ignoreExpiredData">
<a href="../mapview.datasource/RasterDataSourceConfiguration/ignoreExpiredData.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasourceconfiguration-ignoreexpireddata</a>
↔ bool
</dt>
<dd>
  A flag indicating whether expired data should be ignored until refreshed. Default value is <code>false</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="name">
<a href="../mapview.datasource/RasterDataSourceConfiguration/name.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasourceconfiguration-name</a>
↔ String
</dt>
<dd>
  The unique name of the data source.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="provider">
<a href="../mapview.datasource/RasterDataSourceConfiguration/provider.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasourceconfiguration-provider</a>
↔ <a href="../mapview.datasource/RasterDataSourceProviderConfiguration-class.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasourceproviderconfiguration-class</a>
</dt>
<dd>
  Data provider configuration.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../mapview.datasource/RasterDataSourceConfiguration/runtimeType.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasourceconfiguration-runtimetype</a>
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
<a href="../mapview.datasource/RasterDataSourceConfiguration/noSuchMethod.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasourceconfiguration-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../mapview.datasource/RasterDataSourceConfiguration/toString.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasourceconfiguration-tostring</a>(<wbr/>)
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
<a href="../mapview.datasource/RasterDataSourceConfiguration/operator_equals.html">/sdk-for-flutter-explore-mapview-datasource-rasterdatasourceconfiguration-operator-equals</a>(<wbr/>Object other)
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
<li class="self-crumb">RasterDataSourceConfiguration class</li>
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
