---
title: "Untitled"
slug: "sdk-for-flutter-navigate-core-engine-catalogconfiguration-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- CatalogConfiguration-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-core-engine-core-engine-library</li>
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
<p>Using this class you can configure in the /sdk-for-flutter-navigate-core-engine-sdkoptions-class,
how the /sdk-for-flutter-navigate-core-engine-sdknativeengine-class should access, use and store the data for the desired catalog.</p>
<p>Using this class, you can access default catalogs on the HERE platform and also custom catalogs
such as for self-hosted or BYOD (bring your own data) use cases.</p>
<p>For information on how the user can identify a catalog on the HERE platform, see /sdk-for-flutter-navigate-core-engine-desiredcatalog-class
For further information about catalogs and related concepts see /sdk-for-flutter-navigate-core-engine-catalogidentifier-class.</p>
<p><strong>Note:</strong>
This API is only applicable for the Navigate license.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="CatalogConfiguration">
/sdk-for-flutter-navigate-core-engine-catalogconfiguration-catalogconfiguration(/sdk-for-flutter-navigate-core-engine-desiredcatalog-class catalog)
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="allowDownload">
/sdk-for-flutter-navigate-core-engine-catalogconfiguration-allowdownload
↔ bool
</dt>
<dd>
  A flag to indicate if the data for this catalog is allowed to be stored in persistent storage for use with offline maps.
The storage path is specified in /sdk-for-flutter-navigate-core-engine-sdkoptions-persistentmapstoragepath.
If set to false, the data is not stored in persistent storage and is only retained in the cache for a limited time (see /sdk-for-flutter-navigate-core-engine-catalogconfiguration-cacheexpirationperiod).
Defaults to <code>true</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="cacheExpirationPeriod">
/sdk-for-flutter-navigate-core-engine-catalogconfiguration-cacheexpirationperiod
↔ Duration?
</dt>
<dd>
  Expiration time in seconds for how long the catalog data is retained in the
map cache before it is removed. Cache path is specified by /sdk-for-flutter-navigate-core-engine-sdkoptions-cachepath.
If not set, the cache will be deleted on a Least Recently Used (LRU) basis.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="catalog">
/sdk-for-flutter-navigate-core-engine-catalogconfiguration-catalog
↔ /sdk-for-flutter-navigate-core-engine-desiredcatalog-class
</dt>
<dd>
  The identifier for the desired catalog to be accessed on the HERE platform.
See /sdk-for-flutter-navigate-core-engine-desiredcatalog-class.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-core-engine-catalogconfiguration-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="patchHrn">
/sdk-for-flutter-navigate-core-engine-catalogconfiguration-patchhrn
↔ String?
</dt>
<dd>
  Some catalogs may have additional modifications to their data
contained in an entirely separate catalog, called the patch catalog.
This field indicates the HERE Resource Name (HRN) for the patch catalog.
When this field is present, the catalog's data as referenced by
/sdk-for-flutter-navigate-core-engine-catalogconfiguration-catalog is merged with data from the patch catalog.
If this field is <code>null</code>, then incremental updates are disabled.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-core-engine-catalogconfiguration-runtimetype
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
/sdk-for-flutter-navigate-core-engine-catalogconfiguration-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-core-engine-catalogconfiguration-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-core-engine-catalogconfiguration-operator-equals(<wbr/>Object other)
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
/sdk-for-flutter-navigate-core-engine-catalogconfiguration-getdefault(<wbr/>/sdk-for-flutter-navigate-core-engine-catalogtype catalogType)
    → /sdk-for-flutter-navigate-core-engine-catalogconfiguration-class

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
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-core-engine-core-engine-library</li>
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



</div>
`
}</HTMLBlock>
