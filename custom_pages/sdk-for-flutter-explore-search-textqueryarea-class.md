---
title: "Constructors"
slug: "sdk-for-flutter-explore-search-textqueryarea-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- TextQueryArea-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="search/TextQueryArea-class.html#constructors">Constructors</a></li>
<li><a href="search/TextQueryArea/TextQueryArea.withBox.html">withBox</a></li>
<li><a href="search/TextQueryArea/TextQueryArea.withCenter.html">withCenter</a></li>
<li><a href="search/TextQueryArea/TextQueryArea.withCircle.html">withCircle</a></li>
<li><a href="search/TextQueryArea/TextQueryArea.withCorridor.html">withCorridor</a></li>
<li><a href="search/TextQueryArea/TextQueryArea.withCountries.html">withCountries</a></li>
<li class="section-title">
<a href="search/TextQueryArea-class.html#instance-properties">Properties</a>
</li>
<li><a href="search/TextQueryArea/areaCenter.html">areaCenter</a></li>
<li><a href="search/TextQueryArea/boxArea.html">boxArea</a></li>
<li><a href="search/TextQueryArea/circleArea.html">circleArea</a></li>
<li><a href="search/TextQueryArea/corridorArea.html">corridorArea</a></li>
<li><a href="search/TextQueryArea/countries.html">countries</a></li>
<li><a href="search/TextQueryArea/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="search/TextQueryArea/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="search/TextQueryArea-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="search/TextQueryArea/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="search/TextQueryArea/toString.html">toString</a></li>
<li class="section-title"><a href="search/TextQueryArea-class.html#operators">Operators</a></li>
<li><a href="search/TextQueryArea/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
<li class="self-crumb">TextQueryArea class</li>
</ol>
<div class="self-name">TextQueryArea</div>
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
<div class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/TextQueryArea-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>TextQueryArea class</h1></div>
<section class="desc markdown">
<p>Area to perform search on.</p>
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
<dt class="callable" id="TextQueryArea.withBox">
<a href="../search/TextQueryArea/TextQueryArea.withBox.html">/sdk-for-flutter-explore-search-textqueryarea-textqueryarea-withbox</a>(<a href="../core/GeoBox-class.html">/sdk-for-flutter-explore-core-geobox-class</a> boxArea)
</dt>
<dd>
          Constructs a new instance of this class from provided parameters.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="TextQueryArea.withCenter">
<a href="../search/TextQueryArea/TextQueryArea.withCenter.html">/sdk-for-flutter-explore-search-textqueryarea-textqueryarea-withcenter</a>(<a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a> areaCenter)
</dt>
<dd>
          Constructs a new instance of this class from provided parameters.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="TextQueryArea.withCircle">
<a href="../search/TextQueryArea/TextQueryArea.withCircle.html">/sdk-for-flutter-explore-search-textqueryarea-textqueryarea-withcircle</a>(<a href="../core/GeoCircle-class.html">/sdk-for-flutter-explore-core-geocircle-class</a> circleArea)
</dt>
<dd>
          Constructs a new instance of this class from provided parameters.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="TextQueryArea.withCorridor">
<a href="../search/TextQueryArea/TextQueryArea.withCorridor.html">/sdk-for-flutter-explore-search-textqueryarea-textqueryarea-withcorridor</a>(<a href="../core/GeoCorridor-class.html">/sdk-for-flutter-explore-core-geocorridor-class</a> corridorArea, <a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a> areaCenter)
</dt>
<dd>
          Constructs a new instance of this class from provided parameters.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="TextQueryArea.withCountries">
<a href="../search/TextQueryArea/TextQueryArea.withCountries.html">/sdk-for-flutter-explore-search-textqueryarea-textqueryarea-withcountries</a>(List&lt;<wbr/><a href="../core/CountryCode.html">/sdk-for-flutter-explore-core-countrycode</a>&gt; countries, <a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a> areaCenter)
</dt>
<dd>
          Constructs a new instance of this class from provided parameters.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="areaCenter">
<a href="../search/TextQueryArea/areaCenter.html">/sdk-for-flutter-explore-search-textqueryarea-areacenter</a>
→ <a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a>?
</dt>
<dd>
  Geographic coordinates of the center around which to provide the most relevant places.
For Offline Search, one of <a href="../search/TextQueryArea/areaCenter.html">/sdk-for-flutter-explore-search-textqueryarea-areacenter</a>, <a href="../search/TextQueryArea/boxArea.html">/sdk-for-flutter-explore-search-textqueryarea-boxarea</a> and <a href="../search/TextQueryArea/circleArea.html">/sdk-for-flutter-explore-search-textqueryarea-circlearea</a> has to be set,
otherwise it will result in <a href="../search/SearchError.html">/sdk-for-flutter-explore-search-searcherror</a>.
  <div class="features">final</div>
</dd>
<dt class="property" id="boxArea">
<a href="../search/TextQueryArea/boxArea.html">/sdk-for-flutter-explore-search-textqueryarea-boxarea</a>
→ <a href="../core/GeoBox-class.html">/sdk-for-flutter-explore-core-geobox-class</a>?
</dt>
<dd>
  Geographic rectangle area in which to provide the most relevant places.
For Offline Search, one of <a href="../search/TextQueryArea/areaCenter.html">/sdk-for-flutter-explore-search-textqueryarea-areacenter</a>, <a href="../search/TextQueryArea/boxArea.html">/sdk-for-flutter-explore-search-textqueryarea-boxarea</a> and <a href="../search/TextQueryArea/circleArea.html">/sdk-for-flutter-explore-search-textqueryarea-circlearea</a> has to be set,
otherwise it will result in <a href="../search/SearchError.html">/sdk-for-flutter-explore-search-searcherror</a>.
Also, for Offline Search, search in a given <code>GeoBox</code> restricts the results to only POIs.
  <div class="features">final</div>
</dd>
<dt class="property" id="circleArea">
<a href="../search/TextQueryArea/circleArea.html">/sdk-for-flutter-explore-search-textqueryarea-circlearea</a>
→ <a href="../core/GeoCircle-class.html">/sdk-for-flutter-explore-core-geocircle-class</a>?
</dt>
<dd>
  Geographic circle area in which to provide the most relevant places.
For Offline Search, one of <a href="../search/TextQueryArea/areaCenter.html">/sdk-for-flutter-explore-search-textqueryarea-areacenter</a>, <a href="../search/TextQueryArea/boxArea.html">/sdk-for-flutter-explore-search-textqueryarea-boxarea</a> and <a href="../search/TextQueryArea/circleArea.html">/sdk-for-flutter-explore-search-textqueryarea-circlearea</a> has to be set,
otherwise it will result in <a href="../search/SearchError.html">/sdk-for-flutter-explore-search-searcherror</a>.
Also, for Offline Search, search in a given <code>GeoCircle</code> restricts the results to only POIs.
  <div class="features">final</div>
</dd>
<dt class="property" id="corridorArea">
<a href="../search/TextQueryArea/corridorArea.html">/sdk-for-flutter-explore-search-textqueryarea-corridorarea</a>
→ <a href="../core/GeoCorridor-class.html">/sdk-for-flutter-explore-core-geocorridor-class</a>?
</dt>
<dd>
  Geographic corridor area in which to provide the most relevant places.
The contained polyline and half-width define the area that will be used in a search query.
  <div class="features">final</div>
</dd>
<dt class="property" id="countries">
<a href="../search/TextQueryArea/countries.html">/sdk-for-flutter-explore-search-textqueryarea-countries</a>
→ List&lt;<wbr/><a href="../core/CountryCode.html">/sdk-for-flutter-explore-core-countrycode</a>&gt;
</dt>
<dd>
  A list of countries that the query is applied in.
Not supported in <code>OfflineSearchEngine</code> (which is only available for the Navigate license).
  <div class="features">final</div>
</dd>
<dt class="property" id="hashCode">
<a href="../search/TextQueryArea/hashCode.html">/sdk-for-flutter-explore-search-textqueryarea-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../search/TextQueryArea/runtimeType.html">/sdk-for-flutter-explore-search-textqueryarea-runtimetype</a>
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
<a href="../search/TextQueryArea/noSuchMethod.html">/sdk-for-flutter-explore-search-textqueryarea-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../search/TextQueryArea/toString.html">/sdk-for-flutter-explore-search-textqueryarea-tostring</a>(<wbr/>)
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
<a href="../search/TextQueryArea/operator_equals.html">/sdk-for-flutter-explore-search-textqueryarea-operator-equals</a>(<wbr/>Object other)
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
<li class="self-crumb">TextQueryArea class</li>
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
