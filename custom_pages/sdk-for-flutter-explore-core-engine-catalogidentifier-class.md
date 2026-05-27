---
title: "Constructors"
slug: "sdk-for-flutter-explore-core-engine-catalogidentifier-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- CatalogIdentifier-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="core.engine/CatalogIdentifier-class.html#constructors">Constructors</a></li>
<li><a href="core.engine/CatalogIdentifier/CatalogIdentifier.html">CatalogIdentifier</a></li>
<li class="section-title">
<a href="core.engine/CatalogIdentifier-class.html#instance-properties">Properties</a>
</li>
<li><a href="core.engine/CatalogIdentifier/hashCode.html">hashCode</a></li>
<li><a href="core.engine/CatalogIdentifier/hrn.html">hrn</a></li>
<li class="inherited"><a href="core.engine/CatalogIdentifier/runtimeType.html">runtimeType</a></li>
<li><a href="core.engine/CatalogIdentifier/version.html">version</a></li>
<li class="section-title inherited"><a href="core.engine/CatalogIdentifier-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="core.engine/CatalogIdentifier/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="core.engine/CatalogIdentifier/toString.html">toString</a></li>
<li class="section-title"><a href="core.engine/CatalogIdentifier-class.html#operators">Operators</a></li>
<li><a href="core.engine/CatalogIdentifier/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../core.engine/core.engine-library.html">/sdk-for-flutter-explore-core-engine-core-engine-library</a></li>
<li class="self-crumb">CatalogIdentifier class</li>
</ol>
<div class="self-name">CatalogIdentifier</div>
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
<div class="main-content" data-above-sidebar="core.engine/core.engine-library-sidebar.html" data-below-sidebar="core.engine/CatalogIdentifier-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>CatalogIdentifier class</h1></div>
<section class="desc markdown">
<p>This class is used to identify any catalog in the HERE platform.</p>
<p>A catalog is a storage-representation to store map data on the HERE platform.
The data inside a catalog is divided into layers, where each layer consists
of datasets with similar functional attributes in the physical world.
For example, there can be a layer for road-topology, a layer for
road-attributes (such as speed limits) and a layer for places and business
addresses. All these layers, in different geographic regions, can be grouped together into a
catalog to create a representation of the world we live in, called HERE map.
It can be also used to render a <code>MapView</code>. Each geographic region is cut into geospatial
tiles for efficient search, map display, routing, map matching, and driver warnings.
Each tile partitions the map data (in one or more layers, depending on the product)
in the geolocation of that specific tile.
The data inside a catalog is logically managed and access controlled
as a single set. If you have any data that you want to bring to the HERE
platform, you need a catalog to contain it.
For additional information about catalogs, and related concepts of data representation
on the HERE platform, refer to
<a href="https://www.here.com/docs/bundle/data-api-developer-guide/page/rest/catalogs.html">the Data API</a>
and <a href="https://www.here.com/docs/bundle/introduction-to-mapping-concepts-user-guide/page/topics/maps-layers-tiles.html">Introduction to Mapping Concepts</a></p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="CatalogIdentifier">
<a href="../core.engine/CatalogIdentifier/CatalogIdentifier.html">/sdk-for-flutter-explore-core-engine-catalogidentifier-catalogidentifier</a>()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="hashCode">
<a href="../core.engine/CatalogIdentifier/hashCode.html">/sdk-for-flutter-explore-core-engine-catalogidentifier-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="hrn">
<a href="../core.engine/CatalogIdentifier/hrn.html">/sdk-for-flutter-explore-core-engine-catalogidentifier-hrn</a>
↔ String
</dt>
<dd>
  A HERE Resource Name (HRN) for this catalog. This is a unique string returned by the HERE platform when you add a new
catalog to your project. For information about catalog creation process refer to
<a href="https://www.here.com/docs/bundle/data-api-developer-guide/page/rest/creating-a-catalog.html">the Data API</a>
By default, this field points to a default catalog on HERE platform, which contains data for the whole world excluding the region of Japan.
Use <a href="../core.engine/CatalogConfiguration/getDefault.html">/sdk-for-flutter-explore-core-engine-catalogconfiguration-getdefault</a> to get the default HRN value for use with the HERE platform.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../core.engine/CatalogIdentifier/runtimeType.html">/sdk-for-flutter-explore-core-engine-catalogidentifier-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="version">
<a href="../core.engine/CatalogIdentifier/version.html">/sdk-for-flutter-explore-core-engine-catalogidentifier-version</a>
↔ int?
</dt>
<dd>
  A version number for a catalog. When accessing a catalog, this version must be specified.
Set <code>null</code> to automatically get the latest version for a catalog.
The field defaults to <code>null</code>.
Since the data inside a catalog can be updated, each published modification needs to correlate
to a specific version number.
Note: when <code>CatalogIdentifier</code> created with <a href="../core.engine/DesiredCatalog-class.html">/sdk-for-flutter-explore-core-engine-desiredcatalog-class</a> then:
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
<a href="../core.engine/CatalogIdentifier/noSuchMethod.html">/sdk-for-flutter-explore-core-engine-catalogidentifier-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../core.engine/CatalogIdentifier/toString.html">/sdk-for-flutter-explore-core-engine-catalogidentifier-tostring</a>(<wbr/>)
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
<a href="../core.engine/CatalogIdentifier/operator_equals.html">/sdk-for-flutter-explore-core-engine-catalogidentifier-operator-equals</a>(<wbr/>Object other)
    → bool

</dt>
<dd>
  The equality operator.
  

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
<li class="self-crumb">CatalogIdentifier class</li>
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
