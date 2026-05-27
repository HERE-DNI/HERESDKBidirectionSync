---
title: "Constructors"
slug: "sdk-for-flutter-explore-search-searchengine-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- SearchEngine-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="search/SearchEngine-class.html#constructors">Constructors</a></li>
<li><a href="search/SearchEngine/SearchEngine.html">SearchEngine</a></li>
<li><a href="search/SearchEngine/SearchEngine.withSdkEngine.html">withSdkEngine</a></li>
<li class="section-title inherited">
<a href="search/SearchEngine-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="search/SearchInterface/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="search/SearchInterface/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="search/SearchEngine-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="search/SearchInterface/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="search/SearchInterface/searchByAddress.html">searchByAddress</a></li>
<li><a href="search/SearchEngine/searchByAddressExtended.html">searchByAddressExtended</a></li>
<li class="inherited"><a href="search/SearchInterface/searchByCategory.html">searchByCategory</a></li>
<li><a href="search/SearchEngine/searchByCategoryExtended.html">searchByCategoryExtended</a></li>
<li class="inherited"><a href="search/SearchInterface/searchByCoordinates.html">searchByCoordinates</a></li>
<li><a href="search/SearchEngine/searchByCoordinatesExtended.html">searchByCoordinatesExtended</a></li>
<li><a href="search/SearchEngine/searchByCoordinatesWithRadius.html">searchByCoordinatesWithRadius</a></li>
<li><a href="search/SearchEngine/searchByCoordinatesWithRadiusExtended.html">searchByCoordinatesWithRadiusExtended</a></li>
<li class="inherited"><a href="search/SearchInterface/searchByPickedPlace.html">searchByPickedPlace</a></li>
<li class="inherited"><a href="search/SearchInterface/searchByPlaceId.html">searchByPlaceId</a></li>
<li><a href="search/SearchEngine/searchByPlaceIdWithLanguageCodeExtended.html">searchByPlaceIdWithLanguageCodeExtended</a></li>
<li class="inherited"><a href="search/SearchInterface/searchByText.html">searchByText</a></li>
<li><a href="search/SearchEngine/searchByTextExtended.html">searchByTextExtended</a></li>
<li><a href="search/SearchEngine/sendRequest.html">sendRequest</a></li>
<li><a href="search/SearchEngine/sendRequestExtended.html">sendRequestExtended</a></li>
<li><a href="search/SearchEngine/setCustomOption.html">setCustomOption</a></li>
<li><a href="search/SearchEngine/setEVInterface.html">setEVInterface</a></li>
<li class="inherited"><a href="search/SearchInterface/suggestByText.html">suggestByText</a></li>
<li><a href="search/SearchEngine/suggestExtended.html">suggestExtended</a></li>
<li class="inherited"><a href="search/SearchInterface/toString.html">toString</a></li>
<li class="section-title inherited"><a href="search/SearchEngine-class.html#operators">Operators</a></li>
<li class="inherited"><a href="search/SearchInterface/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
<li class="self-crumb">SearchEngine class</li>
</ol>
<div class="self-name">SearchEngine</div>
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
<div class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/SearchEngine-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>SearchEngine class abstract</h1></div>
<section class="desc markdown">
<p>The SearchEngine API unlocks the search, geocoding and suggesting capabilities of HERE services
to provide developers with unmatched flexibility to create differentiating location-enabled
applications.</p>
<p>It enables to search for HERE points of interests, forward and reverse
geocode addresses and geographic coordinates from the HERE map and search for suggested addresses
or place candidates based on incomplete or misspelled queries.</p>
<p>It also allows to search along a given <a href="../core/GeoPolyline-class.html">/sdk-for-flutter-explore-core-geopolyline-class</a> set inside a <a href="../core/GeoCorridor-class.html">/sdk-for-flutter-explore-core-geocorridor-class</a>
as part of a <a href="../search/TextQuery-class.html">/sdk-for-flutter-explore-search-textquery-class</a>.</p>
<p>The SearchEngine API requires an online connection to execute the requests.</p>
<p><strong>Note:</strong> All methods are provided in two flavors. One uses a <a href="../search/SearchCallback.html">/sdk-for-flutter-explore-search-searchcallback</a> and the
other uses a <a href="../search/SearchCallbackExtended.html">/sdk-for-flutter-explore-search-searchcallbackextended</a>: The later adds a <code>ResponseDetails</code> result type
that provides the <code>requestId</code> of a search request and a <code>correlationId</code> to identify multiple,
related queries. This may be useful for debug purposes.</p>
</section>
<section>
<dl class="dl-horizontal">
<dt>Implemented types</dt>
<dd>
<ul class="comma-separated clazz-relationships">
<li><a href="../search/SearchInterface-class.html">/sdk-for-flutter-explore-search-searchinterface-class</a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="SearchEngine">
<a href="../search/SearchEngine/SearchEngine.html">/sdk-for-flutter-explore-search-searchengine-searchengine</a>()
</dt>
<dd>
          Creates a new instance of this class.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="SearchEngine.withSdkEngine">
<a href="../search/SearchEngine/SearchEngine.withSdkEngine.html">/sdk-for-flutter-explore-search-searchengine-searchengine-withsdkengine</a>(<a href="../core.engine/SDKNativeEngine-class.html">/sdk-for-flutter-explore-core-engine-sdknativeengine-class</a> sdkEngine)
</dt>
<dd>
          Creates a new instance of this class.
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
<dt class="callable inherited" id="searchByAddress">
<a href="../search/SearchInterface/searchByAddress.html">/sdk-for-flutter-explore-search-searchinterface-searchbyaddress</a>(<wbr/><a href="../search/AddressQuery-class.html">/sdk-for-flutter-explore-search-addressquery-class</a> query, <a href="../search/SearchOptions-class.html">/sdk-for-flutter-explore-search-searchoptions-class</a> options, <a href="../search/SearchCallback.html">/sdk-for-flutter-explore-search-searchcallback</a> callback)
    → <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
</dt>
<dd class="inherited">
  Performs an asynchronous address query search for <a href="../search/Place-class.html">/sdk-for-flutter-explore-search-place-class</a> instances.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="searchByAddressExtended">
<a href="../search/SearchEngine/searchByAddressExtended.html">/sdk-for-flutter-explore-search-searchengine-searchbyaddressextended</a>(<wbr/><a href="../search/AddressQuery-class.html">/sdk-for-flutter-explore-search-addressquery-class</a> query, <a href="../search/SearchOptions-class.html">/sdk-for-flutter-explore-search-searchoptions-class</a> options, <a href="../search/SearchCallbackExtended.html">/sdk-for-flutter-explore-search-searchcallbackextended</a> callback)
    → <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
</dt>
<dd>
  Performs an asynchronous request to search for places based on a given address.
  

</dd>
<dt class="callable inherited" id="searchByCategory">
<a href="../search/SearchInterface/searchByCategory.html">/sdk-for-flutter-explore-search-searchinterface-searchbycategory</a>(<wbr/><a href="../search/CategoryQuery-class.html">/sdk-for-flutter-explore-search-categoryquery-class</a> query, <a href="../search/SearchOptions-class.html">/sdk-for-flutter-explore-search-searchoptions-class</a> options, <a href="../search/SearchCallback.html">/sdk-for-flutter-explore-search-searchcallback</a> callback)
    → <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
</dt>
<dd class="inherited">
  Performs an asynchronous category search for <a href="../search/Place-class.html">/sdk-for-flutter-explore-search-place-class</a> instances.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="searchByCategoryExtended">
<a href="../search/SearchEngine/searchByCategoryExtended.html">/sdk-for-flutter-explore-search-searchengine-searchbycategoryextended</a>(<wbr/><a href="../search/CategoryQuery-class.html">/sdk-for-flutter-explore-search-categoryquery-class</a> query, <a href="../search/SearchOptions-class.html">/sdk-for-flutter-explore-search-searchoptions-class</a> options, <a href="../search/SearchCallbackExtended.html">/sdk-for-flutter-explore-search-searchcallbackextended</a> callback)
    → <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
</dt>
<dd>
  Performs an asynchronous request to do a category search for <a href="../search/Place-class.html">/sdk-for-flutter-explore-search-place-class</a> instances.
  

</dd>
<dt class="callable inherited" id="searchByCoordinates">
<a href="../search/SearchInterface/searchByCoordinates.html">/sdk-for-flutter-explore-search-searchinterface-searchbycoordinates</a>(<wbr/><a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a> coordinates, <a href="../search/SearchOptions-class.html">/sdk-for-flutter-explore-search-searchoptions-class</a> options, <a href="../search/SearchCallback.html">/sdk-for-flutter-explore-search-searchcallback</a> callback)
    → <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
</dt>
<dd class="inherited">
  Performs an asynchronous search for <a href="../search/Place-class.html">/sdk-for-flutter-explore-search-place-class</a> instances based on the given
geographic coordinates.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="searchByCoordinatesExtended">
<a href="../search/SearchEngine/searchByCoordinatesExtended.html">/sdk-for-flutter-explore-search-searchengine-searchbycoordinatesextended</a>(<wbr/><a href="../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a> coordinates, <a href="../search/SearchOptions-class.html">/sdk-for-flutter-explore-search-searchoptions-class</a> options, <a href="../search/SearchCallbackExtended.html">/sdk-for-flutter-explore-search-searchcallbackextended</a> callback)
    → <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
</dt>
<dd>
  Performs an asynchronous request to search for places based on given geographic coordinates.
  

</dd>
<dt class="callable" id="searchByCoordinatesWithRadius">
<a href="../search/SearchEngine/searchByCoordinatesWithRadius.html">/sdk-for-flutter-explore-search-searchengine-searchbycoordinateswithradius</a>(<wbr/><a href="../core/GeoCircle-class.html">/sdk-for-flutter-explore-core-geocircle-class</a> circle, <a href="../search/SearchOptions-class.html">/sdk-for-flutter-explore-search-searchoptions-class</a> options, <a href="../search/SearchCallback.html">/sdk-for-flutter-explore-search-searchcallback</a> callback)
    → <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
</dt>
<dd>
  Performs an asynchronous request to search for places based on given circular spatial filter.
  

</dd>
<dt class="callable" id="searchByCoordinatesWithRadiusExtended">
<a href="../search/SearchEngine/searchByCoordinatesWithRadiusExtended.html">/sdk-for-flutter-explore-search-searchengine-searchbycoordinateswithradiusextended</a>(<wbr/><a href="../core/GeoCircle-class.html">/sdk-for-flutter-explore-core-geocircle-class</a> circle, <a href="../search/SearchOptions-class.html">/sdk-for-flutter-explore-search-searchoptions-class</a> options, <a href="../search/SearchCallbackExtended.html">/sdk-for-flutter-explore-search-searchcallbackextended</a> callback)
    → <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
</dt>
<dd>
  Performs an asynchronous request to search for places based on given circular spatial filter.
  

</dd>
<dt class="callable inherited" id="searchByPickedPlace">
<a href="../search/SearchInterface/searchByPickedPlace.html">/sdk-for-flutter-explore-search-searchinterface-searchbypickedplace</a>(<wbr/><a href="../core/PickedPlace-class.html">/sdk-for-flutter-explore-core-pickedplace-class</a> pickedPlace, <a href="../core/LanguageCode.html">/sdk-for-flutter-explore-core-languagecode</a>? languageCode, <a href="../search/PlaceIdSearchCallback.html">/sdk-for-flutter-explore-search-placeidsearchcallback</a> callback)
    → <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
</dt>
<dd class="inherited">
  Performs an asynchronous search for a <a href="../search/Place-class.html">/sdk-for-flutter-explore-search-place-class</a> based on the content found in <a href="../core/PickedPlace-class.html">/sdk-for-flutter-explore-core-pickedplace-class</a>.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="searchByPlaceId">
<a href="../search/SearchInterface/searchByPlaceId.html">/sdk-for-flutter-explore-search-searchinterface-searchbyplaceid</a>(<wbr/><a href="../search/PlaceIdQuery-class.html">/sdk-for-flutter-explore-search-placeidquery-class</a> query, <a href="../core/LanguageCode.html">/sdk-for-flutter-explore-core-languagecode</a>? languageCode, <a href="../search/PlaceIdSearchCallback.html">/sdk-for-flutter-explore-search-placeidsearchcallback</a> callback)
    → <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
</dt>
<dd class="inherited">
  Performs an asynchronous search for a <a href="../search/Place-class.html">/sdk-for-flutter-explore-search-place-class</a> based on its ID and
<a href="../core/LanguageCode.html">/sdk-for-flutter-explore-core-languagecode</a>.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="searchByPlaceIdWithLanguageCodeExtended">
<a href="../search/SearchEngine/searchByPlaceIdWithLanguageCodeExtended.html">/sdk-for-flutter-explore-search-searchengine-searchbyplaceidwithlanguagecodeextended</a>(<wbr/><a href="../search/PlaceIdQuery-class.html">/sdk-for-flutter-explore-search-placeidquery-class</a> query, <a href="../core/LanguageCode.html">/sdk-for-flutter-explore-core-languagecode</a>? languageCode, <a href="../search/PlaceIdSearchCallbackExtended.html">/sdk-for-flutter-explore-search-placeidsearchcallbackextended</a> callback)
    → <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
</dt>
<dd>
  Performs an asynchronous request to search for a <a href="../search/Place-class.html">/sdk-for-flutter-explore-search-place-class</a> based on its ID and
<a href="../core/LanguageCode.html">/sdk-for-flutter-explore-core-languagecode</a>.
  

</dd>
<dt class="callable inherited" id="searchByText">
<a href="../search/SearchInterface/searchByText.html">/sdk-for-flutter-explore-search-searchinterface-searchbytext</a>(<wbr/><a href="../search/TextQuery-class.html">/sdk-for-flutter-explore-search-textquery-class</a> query, <a href="../search/SearchOptions-class.html">/sdk-for-flutter-explore-search-searchoptions-class</a> options, <a href="../search/SearchCallback.html">/sdk-for-flutter-explore-search-searchcallback</a> callback)
    → <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
</dt>
<dd class="inherited">
  Performs an asynchronous text query search for <a href="../search/Place-class.html">/sdk-for-flutter-explore-search-place-class</a> instances within a given <a href="../search/TextQueryArea-class.html">/sdk-for-flutter-explore-search-textqueryarea-class</a>.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="searchByTextExtended">
<a href="../search/SearchEngine/searchByTextExtended.html">/sdk-for-flutter-explore-search-searchengine-searchbytextextended</a>(<wbr/><a href="../search/TextQuery-class.html">/sdk-for-flutter-explore-search-textquery-class</a> query, <a href="../search/SearchOptions-class.html">/sdk-for-flutter-explore-search-searchoptions-class</a> options, <a href="../search/SearchCallbackExtended.html">/sdk-for-flutter-explore-search-searchcallbackextended</a> callback)
    → <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
</dt>
<dd>
  Performs an asynchronous request to do a text query search for <a href="../search/Place-class.html">/sdk-for-flutter-explore-search-place-class</a> instances.
  

</dd>
<dt class="callable" id="sendRequest">
<a href="../search/SearchEngine/sendRequest.html">/sdk-for-flutter-explore-search-searchengine-sendrequest</a>(<wbr/>String href, <a href="../search/SearchCallback.html">/sdk-for-flutter-explore-search-searchcallback</a> callback)
    → <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
</dt>
<dd>
  Performs an asynchronous request by using the given href.
  

</dd>
<dt class="callable" id="sendRequestExtended">
<a href="../search/SearchEngine/sendRequestExtended.html">/sdk-for-flutter-explore-search-searchengine-sendrequestextended</a>(<wbr/>String href, <a href="../search/SearchCallbackExtended.html">/sdk-for-flutter-explore-search-searchcallbackextended</a> callback)
    → <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
</dt>
<dd>
  Performs an asynchronous request by using the given href.
  

</dd>
<dt class="callable" id="setCustomOption">
<a href="../search/SearchEngine/setCustomOption.html">/sdk-for-flutter-explore-search-searchengine-setcustomoption</a>(<wbr/>String name, String value)
    → <a href="../search/SearchError.html">/sdk-for-flutter-explore-search-searcherror</a>?

</dt>
<dd>
  Sets a custom option for search backend queries.
  

</dd>
<dt class="callable" id="setEVInterface">
<a href="../search/SearchEngine/setEVInterface.html">/sdk-for-flutter-explore-search-searchengine-setevinterface</a>(<wbr/><a href="../search/EVSearchInterface-class.html">/sdk-for-flutter-explore-search-evsearchinterface-class</a> evcpInterface)
    → void

</dt>
<dd>
  Sets the EV interface through which search will interact with EVCP3.
  

</dd>
<dt class="callable inherited" id="suggestByText">
<a href="../search/SearchInterface/suggestByText.html">/sdk-for-flutter-explore-search-searchinterface-suggestbytext</a>(<wbr/><a href="../search/TextQuery-class.html">/sdk-for-flutter-explore-search-textquery-class</a> query, <a href="../search/SearchOptions-class.html">/sdk-for-flutter-explore-search-searchoptions-class</a> options, <a href="../search/SuggestCallback.html">/sdk-for-flutter-explore-search-suggestcallback</a> callback)
    → <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
</dt>
<dd class="inherited">
  Performs an asynchronous request to suggest places for text queries and
returns suggestions sorted by relevance.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="suggestExtended">
<a href="../search/SearchEngine/suggestExtended.html">/sdk-for-flutter-explore-search-searchengine-suggestextended</a>(<wbr/><a href="../search/TextQuery-class.html">/sdk-for-flutter-explore-search-textquery-class</a> query, <a href="../search/SearchOptions-class.html">/sdk-for-flutter-explore-search-searchoptions-class</a> options, <a href="../search/SuggestCallbackExtended.html">/sdk-for-flutter-explore-search-suggestcallbackextended</a> callback)
    → <a href="../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
</dt>
<dd>
  Performs an asynchronous request to suggest places for text queries and
returns candidate suggestions sorted by relevance.
  

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
<li class="self-crumb">SearchEngine class</li>
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
