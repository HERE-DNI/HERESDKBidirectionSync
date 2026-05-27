---
title: "Constructors"
slug: "sdk-for-flutter-explore-search-addressquery-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- AddressQuery-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="search/AddressQuery-class.html#constructors">Constructors</a></li>
<li><a href="search/AddressQuery/AddressQuery.html">AddressQuery</a></li>
<li><a href="search/AddressQuery/AddressQuery.withAreaCenter.html">withAreaCenter</a></li>
<li><a href="search/AddressQuery/AddressQuery.withAreaCenterInCountries.html">withAreaCenterInCountries</a></li>
<li class="section-title">
<a href="search/AddressQuery-class.html#instance-properties">Properties</a>
</li>
<li><a href="search/AddressQuery/areaCenter.html">areaCenter</a></li>
<li><a href="search/AddressQuery/countries.html">countries</a></li>
<li><a href="search/AddressQuery/hashCode.html">hashCode</a></li>
<li><a href="search/AddressQuery/query.html">query</a></li>
<li class="inherited"><a href="search/AddressQuery/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="search/AddressQuery-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="search/AddressQuery/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="search/AddressQuery/toString.html">toString</a></li>
<li class="section-title"><a href="search/AddressQuery-class.html#operators">Operators</a></li>
<li><a href="search/AddressQuery/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
<li class="self-crumb">AddressQuery class</li>
</ol>
<div class="self-name">AddressQuery</div>
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
<div class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/AddressQuery-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>AddressQuery class</h1></div>
<section class="desc markdown">
<p>The options to specify an address query.</p>
<p>A <a href="../search/AddressQuery/query.html">/sdk-for-flutter-explore-search-addressquery-query</a> can consist of parts of an address or full addresses,
optionally comma separated. <a href="../search/AddressQuery-class.html">/sdk-for-flutter-explore-search-addressquery-class</a> should only be used to search for parts of the address,
excluding the POI name. For example, "Invalidenstraße 116, Berlin, Germany" is appropriate, whereas
"HERE, Invalidenstraße 116, Berlin, Germany" is not. To be able to include the POI name, use
<a href="../search/TextQuery-class.html">/sdk-for-flutter-explore-search-textquery-class</a> instead. <a href="../search/SearchOptions/languageCode.html">/sdk-for-flutter-explore-search-searchoptions-languagecode</a> specifies the language of the
<a href="../search/AddressQuery/query.html">/sdk-for-flutter-explore-search-addressquery-query</a> and determines the preferred language of the results.</p>
</section>
<section>
<dl class="dl-horizontal">
<dt>Annotations</dt>
<dd>
<ul class="annotation-list clazz-relationships">
<li>@<a href="https://pub.dev/documentation/meta/1.17.0/meta/immutable-constant.html">immutable</a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="AddressQuery">
<a href="../search/AddressQuery/AddressQuery.html">/sdk-for-flutter-explore-search-addressquery-addressquery</a>(String query)
</dt>
<dd>
          Constructs an AddressQuery from the provided text query.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="AddressQuery.withAreaCenter">
<a href="../search/AddressQuery/AddressQuery.withAreaCenter.html">/sdk-for-flutter-explore-search-addressquery-addressquery-withareacenter</a>(String query, <a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a> areaCenter)
</dt>
<dd>
          Constructs an AddressQuery from the provided text query and geographical coordinates.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="AddressQuery.withAreaCenterInCountries">
<a href="../search/AddressQuery/AddressQuery.withAreaCenterInCountries.html">/sdk-for-flutter-explore-search-addressquery-addressquery-withareacenterincountries</a>(String query, <a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a> areaCenter, List&lt;<wbr/><a href="../core/CountryCode.html">/sdk-for-flutter-explore-core-countrycode</a>&gt; countries)
</dt>
<dd>
          Constructs an AddressQuery from the provided text query, geographical coordinates and the
list of countries the query is applied in.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="areaCenter">
<a href="../search/AddressQuery/areaCenter.html">/sdk-for-flutter-explore-search-addressquery-areacenter</a>
→ <a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a>?
</dt>
<dd>
  Geographical coordinates of the center around which to provide the most relevant places.
For Offline Search null value will result in <a href="../search/SearchError.html">/sdk-for-flutter-explore-search-searcherror</a>
<div class="features">final</div>
</dd>
<dt class="property" id="countries">
<a href="../search/AddressQuery/countries.html">/sdk-for-flutter-explore-search-addressquery-countries</a>
→ List&lt;<wbr/><a href="../core/CountryCode.html">/sdk-for-flutter-explore-core-countrycode</a>&gt;
</dt>
<dd>
  A list of countries that the query is applied in.
Not supported in <code>OfflineSearchEngine</code> (only available for the Navigate license).
  <div class="features">final</div>
</dd>
<dt class="property" id="hashCode">
<a href="../search/AddressQuery/hashCode.html">/sdk-for-flutter-explore-search-addressquery-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="query">
<a href="../search/AddressQuery/query.html">/sdk-for-flutter-explore-search-addressquery-query</a>
→ String
</dt>
<dd>
  Desired address query to search.
  <div class="features">final</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../search/AddressQuery/runtimeType.html">/sdk-for-flutter-explore-search-addressquery-runtimetype</a>
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
<a href="../search/AddressQuery/noSuchMethod.html">/sdk-for-flutter-explore-search-addressquery-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../search/AddressQuery/toString.html">/sdk-for-flutter-explore-search-addressquery-tostring</a>(<wbr/>)
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
<a href="../search/AddressQuery/operator_equals.html">/sdk-for-flutter-explore-search-addressquery-operator-equals</a>(<wbr/>Object other)
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
<li class="self-crumb">AddressQuery class</li>
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
