---
title: "CatalogVersionHint class abstract"
slug: "sdk-for-flutter-explore-core-engine-catalogversionhint-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- CatalogVersionHint-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="core.engine/CatalogVersionHint-class.html#constructors">Constructors</a></li>
<li><a href="core.engine/CatalogVersionHint/CatalogVersionHint.html">CatalogVersionHint</a></li>
<li class="section-title inherited">
<a href="core.engine/CatalogVersionHint-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="core.engine/CatalogVersionHint/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="core.engine/CatalogVersionHint/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="core.engine/CatalogVersionHint-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="core.engine/CatalogVersionHint/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="core.engine/CatalogVersionHint/toString.html">toString</a></li>
<li class="section-title inherited"><a href="core.engine/CatalogVersionHint-class.html#operators">Operators</a></li>
<li class="inherited"><a href="core.engine/CatalogVersionHint/operator_equals.html">operator ==</a></li>
<li class="section-title"><a href="core.engine/CatalogVersionHint-class.html#static-methods">Static methods</a></li>
<li><a href="core.engine/CatalogVersionHint/latestWithIgnoringCachedData.html">latestWithIgnoringCachedData</a></li>
<li><a href="core.engine/CatalogVersionHint/specific.html">specific</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-core-engine-core-engine-library</li>
<li class="self-crumb">CatalogVersionHint class</li>
</ol>
<div class="self-name">CatalogVersionHint</div>
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
<div class="main-content" data-above-sidebar="core.engine/core.engine-library-sidebar.html" data-below-sidebar="core.engine/CatalogVersionHint-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>CatalogVersionHint class abstract</h1></div>
<section class="desc markdown">
<p>This is a class for capturing user's intent for the
desired catalog version to use in /sdk-for-flutter-explore-core-engine-desiredcatalog-class class.</p>
<p>You can request a specific or latest version of a catalog by calling the
static functions /sdk-for-flutter-explore-core-engine-catalogversionhint-specific and
/sdk-for-flutter-explore-core-engine-catalogversionhint-latestwithignoringcacheddata respectively. The HERE platform will make the
best effort to provide an appropriate version for the catalog based on this
version hint.
Please take note that for the API /sdk-for-flutter-explore-core-engine-catalogversionhint-specific to function properly,
it is essential that the mutable and persistent storage should be cleaned.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="CatalogVersionHint">
/sdk-for-flutter-explore-core-engine-catalogversionhint-catalogversionhint()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-explore-core-engine-catalogversionhint-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-core-engine-catalogversionhint-runtimetype
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
/sdk-for-flutter-explore-core-engine-catalogversionhint-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-core-engine-catalogversionhint-tostring(<wbr/>)
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
/sdk-for-flutter-explore-core-engine-catalogversionhint-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="static-methods">
<h2>Static Methods</h2>
<dl class="callables">
<dt class="callable" id="latestWithIgnoringCachedData">
/sdk-for-flutter-explore-core-engine-catalogversionhint-latestwithignoringcacheddata(<wbr/>bool ignoreCachedData)
    → /sdk-for-flutter-explore-core-engine-catalogversionhint-class

</dt>
<dd>
  This static method can be called when you are interested in getting the most latest version of
a catalog when initializing the HERE SDK with <code>SDKOptions</code> where you can specify the
catalog(s) you want to use.
  

</dd>
<dt class="callable" id="specific">
/sdk-for-flutter-explore-core-engine-catalogversionhint-specific(<wbr/>int version)
    → /sdk-for-flutter-explore-core-engine-catalogversionhint-class

</dt>
<dd>
  This static method is used when you are interested in a
specific version of a catalog, that you want to specify manually.
  

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
<li>/sdk-for-flutter-explore-core-engine-core-engine-library</li>
<li class="self-crumb">CatalogVersionHint class</li>
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
`
}</HTMLBlock>
