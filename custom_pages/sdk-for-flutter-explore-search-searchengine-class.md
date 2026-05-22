---
title: "Untitled"
slug: "sdk-for-flutter-explore-search-searchengine-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SearchEngine-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-search-search-library</li>
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
<p>It also allows to search along a given /sdk-for-flutter-explore-core-geopolyline-class set inside a /sdk-for-flutter-explore-core-geocorridor-class
as part of a /sdk-for-flutter-explore-search-textquery-class.</p>
<p>The SearchEngine API requires an online connection to execute the requests.</p>
<p><strong>Note:</strong> All methods are provided in two flavors. One uses a /sdk-for-flutter-explore-search-searchcallback and the
other uses a /sdk-for-flutter-explore-search-searchcallbackextended: The later adds a <code>ResponseDetails</code> result type
that provides the <code>requestId</code> of a search request and a <code>correlationId</code> to identify multiple,
related queries. This may be useful for debug purposes.</p>
</section>
<section>
<dl class="dl-horizontal">
<dt>Implemented types</dt>
<dd>
<ul class="comma-separated clazz-relationships">
<li>/sdk-for-flutter-explore-search-searchinterface-class</li>
</ul>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="SearchEngine">
/sdk-for-flutter-explore-search-searchengine-searchengine()
</dt>
<dd>
          Creates a new instance of this class.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="SearchEngine.withSdkEngine">
/sdk-for-flutter-explore-search-searchengine-searchengine-withsdkengine(/sdk-for-flutter-explore-core-engine-sdknativeengine-class sdkEngine)
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
/sdk-for-flutter-explore-search-searchinterface-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-search-searchinterface-runtimetype
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
/sdk-for-flutter-explore-search-searchinterface-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="searchByAddress">
/sdk-for-flutter-explore-search-searchinterface-searchbyaddress(<wbr/>/sdk-for-flutter-explore-search-addressquery-class query, /sdk-for-flutter-explore-search-searchoptions-class options, /sdk-for-flutter-explore-search-searchcallback callback)
    → /sdk-for-flutter-explore-core-threading-taskhandle-class

</dt>
<dd class="inherited">
  Performs an asynchronous address query search for /sdk-for-flutter-explore-search-place-class instances.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="searchByAddressExtended">
/sdk-for-flutter-explore-search-searchengine-searchbyaddressextended(<wbr/>/sdk-for-flutter-explore-search-addressquery-class query, /sdk-for-flutter-explore-search-searchoptions-class options, /sdk-for-flutter-explore-search-searchcallbackextended callback)
    → /sdk-for-flutter-explore-core-threading-taskhandle-class

</dt>
<dd>
  Performs an asynchronous request to search for places based on a given address.
  

</dd>
<dt class="callable inherited" id="searchByCategory">
/sdk-for-flutter-explore-search-searchinterface-searchbycategory(<wbr/>/sdk-for-flutter-explore-search-categoryquery-class query, /sdk-for-flutter-explore-search-searchoptions-class options, /sdk-for-flutter-explore-search-searchcallback callback)
    → /sdk-for-flutter-explore-core-threading-taskhandle-class

</dt>
<dd class="inherited">
  Performs an asynchronous category search for /sdk-for-flutter-explore-search-place-class instances.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="searchByCategoryExtended">
/sdk-for-flutter-explore-search-searchengine-searchbycategoryextended(<wbr/>/sdk-for-flutter-explore-search-categoryquery-class query, /sdk-for-flutter-explore-search-searchoptions-class options, /sdk-for-flutter-explore-search-searchcallbackextended callback)
    → /sdk-for-flutter-explore-core-threading-taskhandle-class

</dt>
<dd>
  Performs an asynchronous request to do a category search for /sdk-for-flutter-explore-search-place-class instances.
  

</dd>
<dt class="callable inherited" id="searchByCoordinates">
/sdk-for-flutter-explore-search-searchinterface-searchbycoordinates(<wbr/>/sdk-for-flutter-explore-core-geocoordinates-class coordinates, /sdk-for-flutter-explore-search-searchoptions-class options, /sdk-for-flutter-explore-search-searchcallback callback)
    → /sdk-for-flutter-explore-core-threading-taskhandle-class

</dt>
<dd class="inherited">
  Performs an asynchronous search for /sdk-for-flutter-explore-search-place-class instances based on the given
geographic coordinates.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="searchByCoordinatesExtended">
/sdk-for-flutter-explore-search-searchengine-searchbycoordinatesextended(<wbr/>/sdk-for-flutter-explore-core-geocoordinates-class coordinates, /sdk-for-flutter-explore-search-searchoptions-class options, /sdk-for-flutter-explore-search-searchcallbackextended callback)
    → /sdk-for-flutter-explore-core-threading-taskhandle-class

</dt>
<dd>
  Performs an asynchronous request to search for places based on given geographic coordinates.
  

</dd>
<dt class="callable" id="searchByCoordinatesWithRadius">
/sdk-for-flutter-explore-search-searchengine-searchbycoordinateswithradius(<wbr/>/sdk-for-flutter-explore-core-geocircle-class circle, /sdk-for-flutter-explore-search-searchoptions-class options, /sdk-for-flutter-explore-search-searchcallback callback)
    → /sdk-for-flutter-explore-core-threading-taskhandle-class

</dt>
<dd>
  Performs an asynchronous request to search for places based on given circular spatial filter.
  

</dd>
<dt class="callable" id="searchByCoordinatesWithRadiusExtended">
/sdk-for-flutter-explore-search-searchengine-searchbycoordinateswithradiusextended(<wbr/>/sdk-for-flutter-explore-core-geocircle-class circle, /sdk-for-flutter-explore-search-searchoptions-class options, /sdk-for-flutter-explore-search-searchcallbackextended callback)
    → /sdk-for-flutter-explore-core-threading-taskhandle-class

</dt>
<dd>
  Performs an asynchronous request to search for places based on given circular spatial filter.
  

</dd>
<dt class="callable inherited" id="searchByPickedPlace">
/sdk-for-flutter-explore-search-searchinterface-searchbypickedplace(<wbr/>/sdk-for-flutter-explore-core-pickedplace-class pickedPlace, /sdk-for-flutter-explore-core-languagecode? languageCode, /sdk-for-flutter-explore-search-placeidsearchcallback callback)
    → /sdk-for-flutter-explore-core-threading-taskhandle-class

</dt>
<dd class="inherited">
  Performs an asynchronous search for a /sdk-for-flutter-explore-search-place-class based on the content found in /sdk-for-flutter-explore-core-pickedplace-class.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="searchByPlaceId">
/sdk-for-flutter-explore-search-searchinterface-searchbyplaceid(<wbr/>/sdk-for-flutter-explore-search-placeidquery-class query, /sdk-for-flutter-explore-core-languagecode? languageCode, /sdk-for-flutter-explore-search-placeidsearchcallback callback)
    → /sdk-for-flutter-explore-core-threading-taskhandle-class

</dt>
<dd class="inherited">
  Performs an asynchronous search for a /sdk-for-flutter-explore-search-place-class based on its ID and
/sdk-for-flutter-explore-core-languagecode.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="searchByPlaceIdWithLanguageCodeExtended">
/sdk-for-flutter-explore-search-searchengine-searchbyplaceidwithlanguagecodeextended(<wbr/>/sdk-for-flutter-explore-search-placeidquery-class query, /sdk-for-flutter-explore-core-languagecode? languageCode, /sdk-for-flutter-explore-search-placeidsearchcallbackextended callback)
    → /sdk-for-flutter-explore-core-threading-taskhandle-class

</dt>
<dd>
  Performs an asynchronous request to search for a /sdk-for-flutter-explore-search-place-class based on its ID and
/sdk-for-flutter-explore-core-languagecode.
  

</dd>
<dt class="callable inherited" id="searchByText">
/sdk-for-flutter-explore-search-searchinterface-searchbytext(<wbr/>/sdk-for-flutter-explore-search-textquery-class query, /sdk-for-flutter-explore-search-searchoptions-class options, /sdk-for-flutter-explore-search-searchcallback callback)
    → /sdk-for-flutter-explore-core-threading-taskhandle-class

</dt>
<dd class="inherited">
  Performs an asynchronous text query search for /sdk-for-flutter-explore-search-place-class instances within a given /sdk-for-flutter-explore-search-textqueryarea-class.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="searchByTextExtended">
/sdk-for-flutter-explore-search-searchengine-searchbytextextended(<wbr/>/sdk-for-flutter-explore-search-textquery-class query, /sdk-for-flutter-explore-search-searchoptions-class options, /sdk-for-flutter-explore-search-searchcallbackextended callback)
    → /sdk-for-flutter-explore-core-threading-taskhandle-class

</dt>
<dd>
  Performs an asynchronous request to do a text query search for /sdk-for-flutter-explore-search-place-class instances.
  

</dd>
<dt class="callable" id="sendRequest">
/sdk-for-flutter-explore-search-searchengine-sendrequest(<wbr/>String href, /sdk-for-flutter-explore-search-searchcallback callback)
    → /sdk-for-flutter-explore-core-threading-taskhandle-class

</dt>
<dd>
  Performs an asynchronous request by using the given href.
  

</dd>
<dt class="callable" id="sendRequestExtended">
/sdk-for-flutter-explore-search-searchengine-sendrequestextended(<wbr/>String href, /sdk-for-flutter-explore-search-searchcallbackextended callback)
    → /sdk-for-flutter-explore-core-threading-taskhandle-class

</dt>
<dd>
  Performs an asynchronous request by using the given href.
  

</dd>
<dt class="callable" id="setCustomOption">
/sdk-for-flutter-explore-search-searchengine-setcustomoption(<wbr/>String name, String value)
    → /sdk-for-flutter-explore-search-searcherror?

</dt>
<dd>
  Sets a custom option for search backend queries.
  

</dd>
<dt class="callable" id="setEVInterface">
/sdk-for-flutter-explore-search-searchengine-setevinterface(<wbr/>/sdk-for-flutter-explore-search-evsearchinterface-class evcpInterface)
    → void

</dt>
<dd>
  Sets the EV interface through which search will interact with EVCP3.
  

</dd>
<dt class="callable inherited" id="suggestByText">
/sdk-for-flutter-explore-search-searchinterface-suggestbytext(<wbr/>/sdk-for-flutter-explore-search-textquery-class query, /sdk-for-flutter-explore-search-searchoptions-class options, /sdk-for-flutter-explore-search-suggestcallback callback)
    → /sdk-for-flutter-explore-core-threading-taskhandle-class

</dt>
<dd class="inherited">
  Performs an asynchronous request to suggest places for text queries and
returns suggestions sorted by relevance.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="suggestExtended">
/sdk-for-flutter-explore-search-searchengine-suggestextended(<wbr/>/sdk-for-flutter-explore-search-textquery-class query, /sdk-for-flutter-explore-search-searchoptions-class options, /sdk-for-flutter-explore-search-suggestcallbackextended callback)
    → /sdk-for-flutter-explore-core-threading-taskhandle-class

</dt>
<dd>
  Performs an asynchronous request to suggest places for text queries and
returns candidate suggestions sorted by relevance.
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-search-searchinterface-tostring(<wbr/>)
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
/sdk-for-flutter-explore-search-searchinterface-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-search-search-library</li>
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



</div>
`
}</HTMLBlock>
