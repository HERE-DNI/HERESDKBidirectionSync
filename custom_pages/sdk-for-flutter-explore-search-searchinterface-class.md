---
title: "Constructors"
slug: "sdk-for-flutter-explore-search-searchinterface-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- SearchInterface-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="search/SearchInterface-class.html#constructors">Constructors</a></li>
<li><a href="search/SearchInterface/SearchInterface.html">SearchInterface</a></li>
<li class="section-title inherited">
<a href="search/SearchInterface-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="search/SearchInterface/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="search/SearchInterface/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="search/SearchInterface-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="search/SearchInterface/noSuchMethod.html">noSuchMethod</a></li>
<li><a href="search/SearchInterface/searchByAddress.html">searchByAddress</a></li>
<li><a href="search/SearchInterface/searchByCategory.html">searchByCategory</a></li>
<li><a href="search/SearchInterface/searchByCoordinates.html">searchByCoordinates</a></li>
<li><a href="search/SearchInterface/searchByPickedPlace.html">searchByPickedPlace</a></li>
<li><a href="search/SearchInterface/searchByPlaceId.html">searchByPlaceId</a></li>
<li><a href="search/SearchInterface/searchByText.html">searchByText</a></li>
<li><a href="search/SearchInterface/suggestByText.html">suggestByText</a></li>
<li class="inherited"><a href="search/SearchInterface/toString.html">toString</a></li>
<li class="section-title inherited"><a href="search/SearchInterface-class.html#operators">Operators</a></li>
<li class="inherited"><a href="search/SearchInterface/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
<li class="self-crumb">SearchInterface class</li>
</ol>
<div class="self-name">SearchInterface</div>
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
<div class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/SearchInterface-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>SearchInterface class abstract</h1></div>
<section class="desc markdown">
<p>Provides the abstract class for the online and offline
search engines.</p>
</section>
<section>
<dl class="dl-horizontal">
<dt>Implementers</dt>
<dd><ul class="comma-separated clazz-relationships">
<li><a href="../search/SearchEngine-class.html">/sdk-for-flutter-explore-search-searchengine-class</a></li>
</ul></dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="SearchInterface">
<a href="../search/SearchInterface/SearchInterface.html">/sdk-for-flutter-explore-search-searchinterface-searchinterface</a>(<a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a> searchByTextLambda(<a href="../search/TextQuery-class.html">/sdk-for-flutter-explore-search-textquery-class</a>, <a href="../search/SearchOptions-class.html">/sdk-for-flutter-explore-search-searchoptions-class</a>, <a href="../search/SearchCallback.html">/sdk-for-flutter-explore-search-searchcallback</a> ), <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a> searchByAddressLambda(<a href="../search/AddressQuery-class.html">/sdk-for-flutter-explore-search-addressquery-class</a>, <a href="../search/SearchOptions-class.html">/sdk-for-flutter-explore-search-searchoptions-class</a>, <a href="../search/SearchCallback.html">/sdk-for-flutter-explore-search-searchcallback</a> ), <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a> searchByCategoryLambda(<a href="../search/CategoryQuery-class.html">/sdk-for-flutter-explore-search-categoryquery-class</a>, <a href="../search/SearchOptions-class.html">/sdk-for-flutter-explore-search-searchoptions-class</a>, <a href="../search/SearchCallback.html">/sdk-for-flutter-explore-search-searchcallback</a> ), <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a> searchByCoordinatesLambda(<a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a>, <a href="../search/SearchOptions-class.html">/sdk-for-flutter-explore-search-searchoptions-class</a>, <a href="../search/SearchCallback.html">/sdk-for-flutter-explore-search-searchcallback</a> ), <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a> searchByPlaceIdLambda(<a href="../search/PlaceIdQuery-class.html">/sdk-for-flutter-explore-search-placeidquery-class</a>, <a href="../core/LanguageCode.html">/sdk-for-flutter-explore-core-languagecode</a>?, <a href="../search/PlaceIdSearchCallback.html">/sdk-for-flutter-explore-search-placeidsearchcallback</a> ), <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a> searchByPickedPlaceLambda(<a href="../core/PickedPlace-class.html">/sdk-for-flutter-explore-core-pickedplace-class</a>, <a href="../core/LanguageCode.html">/sdk-for-flutter-explore-core-languagecode</a>?, <a href="../search/PlaceIdSearchCallback.html">/sdk-for-flutter-explore-search-placeidsearchcallback</a> ), <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a> suggestByTextLambda(<a href="../search/TextQuery-class.html">/sdk-for-flutter-explore-search-textquery-class</a>, <a href="../search/SearchOptions-class.html">/sdk-for-flutter-explore-search-searchoptions-class</a>, <a href="../search/SuggestCallback.html">/sdk-for-flutter-explore-search-suggestcallback</a> ))
</dt>
<dd>
          Provides the abstract class for the online and offline
search engines.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
<a href="../search/SearchInterface/hashCode.html">/sdk-for-flutter-explore-search-searchinterface-hashcode</a>
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../search/SearchInterface/runtimeType.html">/sdk-for-flutter-explore-search-searchinterface-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
<a href="../search/SearchInterface/noSuchMethod.html">/sdk-for-flutter-explore-search-searchinterface-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="searchByAddress">
<a href="../search/SearchInterface/searchByAddress.html">/sdk-for-flutter-explore-search-searchinterface-searchbyaddress</a>(<wbr/><a href="../search/AddressQuery-class.html">/sdk-for-flutter-explore-search-addressquery-class</a> query, <a href="../search/SearchOptions-class.html">/sdk-for-flutter-explore-search-searchoptions-class</a> options, <a href="../search/SearchCallback.html">/sdk-for-flutter-explore-search-searchcallback</a> callback)
    → <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
</dt>
<dd>
  Performs an asynchronous address query search for <a href="../search/Place-class.html">/sdk-for-flutter-explore-search-place-class</a> instances.
  

</dd>
<dt class="callable" id="searchByCategory">
<a href="../search/SearchInterface/searchByCategory.html">/sdk-for-flutter-explore-search-searchinterface-searchbycategory</a>(<wbr/><a href="../search/CategoryQuery-class.html">/sdk-for-flutter-explore-search-categoryquery-class</a> query, <a href="../search/SearchOptions-class.html">/sdk-for-flutter-explore-search-searchoptions-class</a> options, <a href="../search/SearchCallback.html">/sdk-for-flutter-explore-search-searchcallback</a> callback)
    → <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
</dt>
<dd>
  Performs an asynchronous category search for <a href="../search/Place-class.html">/sdk-for-flutter-explore-search-place-class</a> instances.
  

</dd>
<dt class="callable" id="searchByCoordinates">
<a href="../search/SearchInterface/searchByCoordinates.html">/sdk-for-flutter-explore-search-searchinterface-searchbycoordinates</a>(<wbr/><a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a> coordinates, <a href="../search/SearchOptions-class.html">/sdk-for-flutter-explore-search-searchoptions-class</a> options, <a href="../search/SearchCallback.html">/sdk-for-flutter-explore-search-searchcallback</a> callback)
    → <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
</dt>
<dd>
  Performs an asynchronous search for <a href="../search/Place-class.html">/sdk-for-flutter-explore-search-place-class</a> instances based on the given
geographic coordinates.
  

</dd>
<dt class="callable" id="searchByPickedPlace">
<a href="../search/SearchInterface/searchByPickedPlace.html">/sdk-for-flutter-explore-search-searchinterface-searchbypickedplace</a>(<wbr/><a href="../core/PickedPlace-class.html">/sdk-for-flutter-explore-core-pickedplace-class</a> pickedPlace, <a href="../core/LanguageCode.html">/sdk-for-flutter-explore-core-languagecode</a>? languageCode, <a href="../search/PlaceIdSearchCallback.html">/sdk-for-flutter-explore-search-placeidsearchcallback</a> callback)
    → <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
</dt>
<dd>
  Performs an asynchronous search for a <a href="../search/Place-class.html">/sdk-for-flutter-explore-search-place-class</a> based on the content found in <a href="../core/PickedPlace-class.html">/sdk-for-flutter-explore-core-pickedplace-class</a>.
  

</dd>
<dt class="callable" id="searchByPlaceId">
<a href="../search/SearchInterface/searchByPlaceId.html">/sdk-for-flutter-explore-search-searchinterface-searchbyplaceid</a>(<wbr/><a href="../search/PlaceIdQuery-class.html">/sdk-for-flutter-explore-search-placeidquery-class</a> query, <a href="../core/LanguageCode.html">/sdk-for-flutter-explore-core-languagecode</a>? languageCode, <a href="../search/PlaceIdSearchCallback.html">/sdk-for-flutter-explore-search-placeidsearchcallback</a> callback)
    → <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
</dt>
<dd>
  Performs an asynchronous search for a <a href="../search/Place-class.html">/sdk-for-flutter-explore-search-place-class</a> based on its ID and
<a href="../core/LanguageCode.html">/sdk-for-flutter-explore-core-languagecode</a>.
  

</dd>
<dt class="callable" id="searchByText">
<a href="../search/SearchInterface/searchByText.html">/sdk-for-flutter-explore-search-searchinterface-searchbytext</a>(<wbr/><a href="../search/TextQuery-class.html">/sdk-for-flutter-explore-search-textquery-class</a> query, <a href="../search/SearchOptions-class.html">/sdk-for-flutter-explore-search-searchoptions-class</a> options, <a href="../search/SearchCallback.html">/sdk-for-flutter-explore-search-searchcallback</a> callback)
    → <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
</dt>
<dd>
  Performs an asynchronous text query search for <a href="../search/Place-class.html">/sdk-for-flutter-explore-search-place-class</a> instances within a given <a href="../search/TextQueryArea-class.html">/sdk-for-flutter-explore-search-textqueryarea-class</a>.
  

</dd>
<dt class="callable" id="suggestByText">
<a href="../search/SearchInterface/suggestByText.html">/sdk-for-flutter-explore-search-searchinterface-suggestbytext</a>(<wbr/><a href="../search/TextQuery-class.html">/sdk-for-flutter-explore-search-textquery-class</a> query, <a href="../search/SearchOptions-class.html">/sdk-for-flutter-explore-search-searchoptions-class</a> options, <a href="../search/SuggestCallback.html">/sdk-for-flutter-explore-search-suggestcallback</a> callback)
    → <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
</dt>
<dd>
  Performs an asynchronous request to suggest places for text queries and
returns suggestions sorted by relevance.
  

</dd>
<dt class="callable inherited" id="toString">
<a href="../search/SearchInterface/toString.html">/sdk-for-flutter-explore-search-searchinterface-tostring</a>(<wbr/>)
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
<a href="../search/SearchInterface/operator_equals.html">/sdk-for-flutter-explore-search-searchinterface-operator-equals</a>(<wbr/>Object other)
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
<li><a href="../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
<li class="self-crumb">SearchInterface class</li>
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
