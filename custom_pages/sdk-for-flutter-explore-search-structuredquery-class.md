---
title: "Constructors"
slug: "sdk-for-flutter-explore-search-structuredquery-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- StructuredQuery-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="search/StructuredQuery-class.html#constructors">Constructors</a></li>
<li><a href="search/StructuredQuery/StructuredQuery.html">StructuredQuery</a></li>
<li class="section-title">
<a href="search/StructuredQuery-class.html#instance-properties">Properties</a>
</li>
<li><a href="search/StructuredQuery/addressElements.html">addressElements</a></li>
<li><a href="search/StructuredQuery/areaCenter.html">areaCenter</a></li>
<li><a href="search/StructuredQuery/hashCode.html">hashCode</a></li>
<li><a href="search/StructuredQuery/query.html">query</a></li>
<li><a href="search/StructuredQuery/resultType.html">resultType</a></li>
<li class="inherited"><a href="search/StructuredQuery/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="search/StructuredQuery-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="search/StructuredQuery/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="search/StructuredQuery/toString.html">toString</a></li>
<li class="section-title"><a href="search/StructuredQuery-class.html#operators">Operators</a></li>
<li><a href="search/StructuredQuery/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
<li class="self-crumb">StructuredQuery class</li>
</ol>
<div class="self-name">StructuredQuery</div>
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
<div class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/StructuredQuery-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>StructuredQuery class</h1></div>
<section class="desc markdown">
<p>The options to specify a structured query.</p>
<p>Only supported in <code>OfflineSearchEngine</code> (only available for the Navigate license).</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="StructuredQuery">
<a href="../search/StructuredQuery/StructuredQuery.html">/sdk-for-flutter-explore-search-structuredquery-structuredquery</a>(String query, <a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a> areaCenter)
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="addressElements">
<a href="../search/StructuredQuery/addressElements.html">/sdk-for-flutter-explore-search-structuredquery-addresselements</a>
↔ <a href="../search/StructuredQueryAddressElements-class.html">/sdk-for-flutter-explore-search-structuredqueryaddresselements-class</a>
</dt>
<dd>
  Query address elements to get the results from a specific geographical area.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="areaCenter">
<a href="../search/StructuredQuery/areaCenter.html">/sdk-for-flutter-explore-search-structuredquery-areacenter</a>
↔ <a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a>
</dt>
<dd>
  Geographic coordinates of the prioritized area center.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
<a href="../search/StructuredQuery/hashCode.html">/sdk-for-flutter-explore-search-structuredquery-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="query">
<a href="../search/StructuredQuery/query.html">/sdk-for-flutter-explore-search-structuredquery-query</a>
↔ String
</dt>
<dd>
  Desired query to search.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="resultType">
<a href="../search/StructuredQuery/resultType.html">/sdk-for-flutter-explore-search-structuredquery-resulttype</a>
↔ <a href="../search/StructuredQueryResultType.html">/sdk-for-flutter-explore-search-structuredqueryresulttype</a>?
</dt>
<dd>
  An optional field to indicates the type of result expected.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../search/StructuredQuery/runtimeType.html">/sdk-for-flutter-explore-search-structuredquery-runtimetype</a>
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
<a href="../search/StructuredQuery/noSuchMethod.html">/sdk-for-flutter-explore-search-structuredquery-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../search/StructuredQuery/toString.html">/sdk-for-flutter-explore-search-structuredquery-tostring</a>(<wbr/>)
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
<a href="../search/StructuredQuery/operator_equals.html">/sdk-for-flutter-explore-search-structuredquery-operator-equals</a>(<wbr/>Object other)
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
<li><a href="../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
<li class="self-crumb">StructuredQuery class</li>
</ol>
<h5>search library</h5>
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
