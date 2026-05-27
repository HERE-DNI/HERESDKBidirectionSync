---
title: "Constructors"
slug: "sdk-for-flutter-explore-core-engine-desiredcatalog-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- DesiredCatalog-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="core.engine/DesiredCatalog-class.html#constructors">Constructors</a></li>
<li><a href="core.engine/DesiredCatalog/DesiredCatalog.html">DesiredCatalog</a></li>
<li class="section-title">
<a href="core.engine/DesiredCatalog-class.html#instance-properties">Properties</a>
</li>
<li><a href="core.engine/DesiredCatalog/hashCode.html">hashCode</a></li>
<li><a href="core.engine/DesiredCatalog/id.html">id</a></li>
<li class="inherited"><a href="core.engine/DesiredCatalog/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="core.engine/DesiredCatalog-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="core.engine/DesiredCatalog/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="core.engine/DesiredCatalog/toString.html">toString</a></li>
<li class="section-title"><a href="core.engine/DesiredCatalog-class.html#operators">Operators</a></li>
<li><a href="core.engine/DesiredCatalog/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../core.engine/core.engine-library.html">/sdk-for-flutter-explore-core-engine-core-engine-library</a></li>
<li class="self-crumb">DesiredCatalog class</li>
</ol>
<div class="self-name">DesiredCatalog</div>
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
<div class="main-content" data-above-sidebar="core.engine/core.engine-library-sidebar.html" data-below-sidebar="core.engine/DesiredCatalog-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>DesiredCatalog class</h1></div>
<section class="desc markdown">
<p>This class provides an interface to the user, to identify a catalog on the HERE platform, whose data he wants to access.</p>
<p>The user can specify the HERE Resource Name (HRN) for the catalog along with a hint for the desired version.
If the desired version is not available, the HERE platform will determine the best version to use for a specific catalog or result in error logs.
For information on how to specify the catalog version, see <a href="../core.engine/CatalogVersionHint-class.html">/sdk-for-flutter-explore-core-engine-catalogversionhint-class</a>.
For information about catalogs and related concepts see <a href="../core.engine/CatalogIdentifier-class.html">/sdk-for-flutter-explore-core-engine-catalogidentifier-class</a>.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="DesiredCatalog">
<a href="../core.engine/DesiredCatalog/DesiredCatalog.html">/sdk-for-flutter-explore-core-engine-desiredcatalog-desiredcatalog</a>(String hrn, <a href="../core.engine/CatalogVersionHint-class.html">/sdk-for-flutter-explore-core-engine-catalogversionhint-class</a> version)
</dt>
<dd>
          Creates a new instance.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="hashCode">
<a href="../core.engine/DesiredCatalog/hashCode.html">/sdk-for-flutter-explore-core-engine-desiredcatalog-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="id">
<a href="../core.engine/DesiredCatalog/id.html">/sdk-for-flutter-explore-core-engine-desiredcatalog-id</a>
↔ <a href="../core.engine/CatalogIdentifier-class.html">/sdk-for-flutter-explore-core-engine-catalogidentifier-class</a>
</dt>
<dd>
  The identifier for the catalog to be accessed on the HERE platform.
See <a href="../core.engine/CatalogIdentifier-class.html">/sdk-for-flutter-explore-core-engine-catalogidentifier-class</a>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../core.engine/DesiredCatalog/runtimeType.html">/sdk-for-flutter-explore-core-engine-desiredcatalog-runtimetype</a>
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
<a href="../core.engine/DesiredCatalog/noSuchMethod.html">/sdk-for-flutter-explore-core-engine-desiredcatalog-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../core.engine/DesiredCatalog/toString.html">/sdk-for-flutter-explore-core-engine-desiredcatalog-tostring</a>(<wbr/>)
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
<a href="../core.engine/DesiredCatalog/operator_equals.html">/sdk-for-flutter-explore-core-engine-desiredcatalog-operator-equals</a>(<wbr/>Object other)
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
<li class="self-crumb">DesiredCatalog class</li>
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
