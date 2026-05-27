---
title: "Constructors"
slug: "sdk-for-flutter-explore-core-engine-catalogconfiguration-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- CatalogConfiguration-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="core.engine/CatalogConfiguration-class.html#constructors">Constructors</a></li>
<li><a href="core.engine/CatalogConfiguration/CatalogConfiguration.html">CatalogConfiguration</a></li>
<li class="section-title">
<a href="core.engine/CatalogConfiguration-class.html#instance-properties">Properties</a>
</li>
<li><a href="core.engine/CatalogConfiguration/allowDownload.html">allowDownload</a></li>
<li><a href="core.engine/CatalogConfiguration/cacheExpirationPeriod.html">cacheExpirationPeriod</a></li>
<li><a href="core.engine/CatalogConfiguration/catalog.html">catalog</a></li>
<li><a href="core.engine/CatalogConfiguration/hashCode.html">hashCode</a></li>
<li><a href="core.engine/CatalogConfiguration/patchHrn.html">patchHrn</a></li>
<li class="inherited"><a href="core.engine/CatalogConfiguration/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="core.engine/CatalogConfiguration-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="core.engine/CatalogConfiguration/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="core.engine/CatalogConfiguration/toString.html">toString</a></li>
<li class="section-title"><a href="core.engine/CatalogConfiguration-class.html#operators">Operators</a></li>
<li><a href="core.engine/CatalogConfiguration/operator_equals.html">operator ==</a></li>
<li class="section-title"><a href="core.engine/CatalogConfiguration-class.html#static-methods">Static methods</a></li>
<li><a href="core.engine/CatalogConfiguration/getDefault.html">getDefault</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../core.engine/core.engine-library.html">/sdk-for-flutter-explore-core-engine-core-engine-library</a></li>
<li class="self-crumb">CatalogConfiguration class</li>
</ol>
<div class="self-name">CatalogConfiguration</div>
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
<div class="main-content" data-above-sidebar="core.engine/core.engine-library-sidebar.html" data-below-sidebar="core.engine/CatalogConfiguration-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>CatalogConfiguration class</h1></div>
<section class="desc markdown">
<p>Using this class you can configure in the <a href="../core.engine/SDKOptions-class.html">/sdk-for-flutter-explore-core-engine-sdkoptions-class</a>,
how the <a href="../core.engine/SDKNativeEngine-class.html">/sdk-for-flutter-explore-core-engine-sdknativeengine-class</a> should access, use and store the data for the desired catalog.</p>
<p>Using this class, you can access default catalogs on the HERE platform and also custom catalogs
such as for self-hosted or BYOD (bring your own data) use cases.</p>
<p>For information on how the user can identify a catalog on the HERE platform, see <a href="../core.engine/DesiredCatalog-class.html">/sdk-for-flutter-explore-core-engine-desiredcatalog-class</a>
For further information about catalogs and related concepts see <a href="../core.engine/CatalogIdentifier-class.html">/sdk-for-flutter-explore-core-engine-catalogidentifier-class</a>.</p>
<p><strong>Note:</strong>
This API is only applicable for the Navigate license.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="CatalogConfiguration">
<a href="../core.engine/CatalogConfiguration/CatalogConfiguration.html">/sdk-for-flutter-explore-core-engine-catalogconfiguration-catalogconfiguration</a>(<a href="../core.engine/DesiredCatalog-class.html">/sdk-for-flutter-explore-core-engine-desiredcatalog-class</a> catalog)
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="allowDownload">
<a href="../core.engine/CatalogConfiguration/allowDownload.html">/sdk-for-flutter-explore-core-engine-catalogconfiguration-allowdownload</a>
↔ bool
</dt>
<dd>
  A flag to indicate if the data for this catalog is allowed to be stored in persistent storage for use with offline maps.
The storage path is specified in <a href="../core.engine/SDKOptions/persistentMapStoragePath.html">/sdk-for-flutter-explore-core-engine-sdkoptions-persistentmapstoragepath</a>.
If set to false, the data is not stored in persistent storage and is only retained in the cache for a limited time (see <a href="../core.engine/CatalogConfiguration/cacheExpirationPeriod.html">/sdk-for-flutter-explore-core-engine-catalogconfiguration-cacheexpirationperiod</a>).
Defaults to <code>true</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="cacheExpirationPeriod">
<a href="../core.engine/CatalogConfiguration/cacheExpirationPeriod.html">/sdk-for-flutter-explore-core-engine-catalogconfiguration-cacheexpirationperiod</a>
↔ Duration?
</dt>
<dd>
  Expiration time in seconds for how long the catalog data is retained in the
map cache before it is removed. Cache path is specified by <a href="../core.engine/SDKOptions/cachePath.html">/sdk-for-flutter-explore-core-engine-sdkoptions-cachepath</a>.
If not set, the cache will be deleted on a Least Recently Used (LRU) basis.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="catalog">
<a href="../core.engine/CatalogConfiguration/catalog.html">/sdk-for-flutter-explore-core-engine-catalogconfiguration-catalog</a>
↔ <a href="../core.engine/DesiredCatalog-class.html">/sdk-for-flutter-explore-core-engine-desiredcatalog-class</a>
</dt>
<dd>
  The identifier for the desired catalog to be accessed on the HERE platform.
See <a href="../core.engine/DesiredCatalog-class.html">/sdk-for-flutter-explore-core-engine-desiredcatalog-class</a>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
<a href="../core.engine/CatalogConfiguration/hashCode.html">/sdk-for-flutter-explore-core-engine-catalogconfiguration-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="patchHrn">
<a href="../core.engine/CatalogConfiguration/patchHrn.html">/sdk-for-flutter-explore-core-engine-catalogconfiguration-patchhrn</a>
↔ String?
</dt>
<dd>
  Some catalogs may have additional modifications to their data
contained in an entirely separate catalog, called the patch catalog.
This field indicates the HERE Resource Name (HRN) for the patch catalog.
When this field is present, the catalog's data as referenced by
<a href="../core.engine/CatalogConfiguration/catalog.html">/sdk-for-flutter-explore-core-engine-catalogconfiguration-catalog</a> is merged with data from the patch catalog.
If this field is <code>null</code>, then incremental updates are disabled.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../core.engine/CatalogConfiguration/runtimeType.html">/sdk-for-flutter-explore-core-engine-catalogconfiguration-runtimetype</a>
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
<a href="../core.engine/CatalogConfiguration/noSuchMethod.html">/sdk-for-flutter-explore-core-engine-catalogconfiguration-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../core.engine/CatalogConfiguration/toString.html">/sdk-for-flutter-explore-core-engine-catalogconfiguration-tostring</a>(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable" id="operator ==">
<a href="../core.engine/CatalogConfiguration/operator_equals.html">/sdk-for-flutter-explore-core-engine-catalogconfiguration-operator-equals</a>(<wbr/>Object other)
    → bool

</dt>
<dd>
  The equality operator.
  

</dd>
</dl>
</section>
<section class="summary offset-anchor" id="static-methods">
<h2>Static Methods</h2>
<dl class="callables">
<dt class="callable" id="getDefault">
<a href="../core.engine/CatalogConfiguration/getDefault.html">/sdk-for-flutter-explore-core-engine-catalogconfiguration-getdefault</a>(<wbr/><a href="../core.engine/CatalogType.html">/sdk-for-flutter-explore-core-engine-catalogtype</a> catalogType)
    → <a href="../core.engine/CatalogConfiguration-class.html">/sdk-for-flutter-explore-core-engine-catalogconfiguration-class</a>
</dt>
<dd>
  Gets the default catalog configuration for the specified catalog type.
  

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
<li><a href="../core.engine/core.engine-library.html">/sdk-for-flutter-explore-core-engine-core-engine-library</a></li>
<li class="self-crumb">CatalogConfiguration class</li>
</ol>
<h5>core.engine library</h5>
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
