---
title: "OfflineSearchEngine class abstract"
slug: "sdk-for-flutter-navigate-search-offlinesearchengine-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- OfflineSearchEngine-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="search/OfflineSearchEngine-class.html#constructors">Constructors</a></li>
<li><a href="search/OfflineSearchEngine/OfflineSearchEngine.html">OfflineSearchEngine</a></li>
<li><a href="search/OfflineSearchEngine/OfflineSearchEngine.withSdkEngine.html">withSdkEngine</a></li>
<li class="section-title inherited">
<a href="search/OfflineSearchEngine-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="search/SearchInterface/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="search/SearchInterface/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="search/OfflineSearchEngine-class.html#instance-methods">Methods</a></li>
<li><a href="search/OfflineSearchEngine/attach.html">attach</a></li>
<li class="inherited"><a href="search/SearchInterface/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="search/SearchInterface/searchByAddress.html">searchByAddress</a></li>
<li><a href="search/OfflineSearchEngine/searchByAddressElements.html">searchByAddressElements</a></li>
<li class="inherited"><a href="search/SearchInterface/searchByCategory.html">searchByCategory</a></li>
<li class="inherited"><a href="search/SearchInterface/searchByCoordinates.html">searchByCoordinates</a></li>
<li class="inherited"><a href="search/SearchInterface/searchByPickedPlace.html">searchByPickedPlace</a></li>
<li class="inherited"><a href="search/SearchInterface/searchByPlaceId.html">searchByPlaceId</a></li>
<li class="inherited"><a href="search/SearchInterface/searchByText.html">searchByText</a></li>
<li><a href="search/OfflineSearchEngine/suggestByAddressElements.html">suggestByAddressElements</a></li>
<li class="inherited"><a href="search/SearchInterface/suggestByText.html">suggestByText</a></li>
<li class="inherited"><a href="search/SearchInterface/toString.html">toString</a></li>
<li class="section-title inherited"><a href="search/OfflineSearchEngine-class.html#operators">Operators</a></li>
<li class="inherited"><a href="search/SearchInterface/operator_equals.html">operator ==</a></li>
<li class="section-title"><a href="search/OfflineSearchEngine-class.html#static-methods">Static methods</a></li>
<li><a href="search/OfflineSearchEngine/setIndexOptions.html">setIndexOptions</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-search-search-library</li>
<li class="self-crumb">OfflineSearchEngine class</li>
</ol>
<div class="self-name">OfflineSearchEngine</div>
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
<div class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/OfflineSearchEngine-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>OfflineSearchEngine class abstract</h1></div>
<section class="desc markdown">
<p>The OfflineSearchEngine works without internet and unlocks the search and geocoding
capabilities of HERE services to provide developers with unmatched flexibility
to create differentiating location-enabled applications.</p>
<p>It provides the same interfaces as the SearchEngine, but the results may slightly
differ as the results are taken from already downloaded map data instead of initiating
a new request to a HERE backend service. This way the data may be, for example, older
compared to the data you may receive when using the SearchEngine. On the other hand,
this class provides results faster as no online connection is necessary.</p>
<p>In comparison to the SearchEngine, there are a few limitations:</p>
<ul>
<li>The IDs of POIs are different and may differ among different map versions.</li>
<li>The implementation is different and the resources are limited, so the results can differ.</li>
<li>OfflineSearchEngine sometimes doesn't return the requested number of results.</li>
</ul>
<p>Note: You can search only within persistent map data (downloaded via MapDownloader) or existing cached data.
However, cached data may be incomplete, which can result in searches returning partial or incomplete information.
Therefore, it is recommended to use persistent map data.
Make sure that at least /sdk-for-flutter-navigate-core-engine-layerconfigurationfeature is enabled.
For EV rich attributes also enable /sdk-for-flutter-navigate-core-engine-layerconfigurationfeature,
for truck rich attributes also enable /sdk-for-flutter-navigate-core-engine-layerconfigurationfeature,
for fuel station rich attributes also enable /sdk-for-flutter-navigate-core-engine-layerconfigurationfeature
in /sdk-for-flutter-navigate-core-engine-sdkoptions-layerconfiguration.</p>
</section>
<section>
<dl class="dl-horizontal">
<dt>Implemented types</dt>
<dd>
<ul class="comma-separated clazz-relationships">
<li>/sdk-for-flutter-navigate-search-searchinterface-class</li>
</ul>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="OfflineSearchEngine">
/sdk-for-flutter-navigate-search-offlinesearchengine-offlinesearchengine()
</dt>
<dd>
          Creates a new instance of this class.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="OfflineSearchEngine.withSdkEngine">
/sdk-for-flutter-navigate-search-offlinesearchengine-offlinesearchengine-withsdkengine(/sdk-for-flutter-navigate-core-engine-sdknativeengine-class sdkEngine)
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
/sdk-for-flutter-navigate-search-searchinterface-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-search-searchinterface-runtimetype
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
<dt class="callable" id="attach">
/sdk-for-flutter-navigate-search-offlinesearchengine-attach(<wbr/>/sdk-for-flutter-navigate-search-myplaces-class dataSource, /sdk-for-flutter-navigate-core-threading-ontaskcompleted callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Attach data source into SearchEngine instance.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-search-searchinterface-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="searchByAddress">
/sdk-for-flutter-navigate-search-searchinterface-searchbyaddress(<wbr/>/sdk-for-flutter-navigate-search-addressquery-class query, /sdk-for-flutter-navigate-search-searchoptions-class options, /sdk-for-flutter-navigate-search-searchcallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd class="inherited">
  Performs an asynchronous address query search for /sdk-for-flutter-navigate-search-place-class instances.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="searchByAddressElements">
/sdk-for-flutter-navigate-search-offlinesearchengine-searchbyaddresselements(<wbr/>/sdk-for-flutter-navigate-search-structuredquery-class query, /sdk-for-flutter-navigate-search-searchoptions-class options, /sdk-for-flutter-navigate-search-searchcallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Performs an asynchronous request to search for places.
  

</dd>
<dt class="callable inherited" id="searchByCategory">
/sdk-for-flutter-navigate-search-searchinterface-searchbycategory(<wbr/>/sdk-for-flutter-navigate-search-categoryquery-class query, /sdk-for-flutter-navigate-search-searchoptions-class options, /sdk-for-flutter-navigate-search-searchcallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd class="inherited">
  Performs an asynchronous category search for /sdk-for-flutter-navigate-search-place-class instances.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="searchByCoordinates">
/sdk-for-flutter-navigate-search-searchinterface-searchbycoordinates(<wbr/>/sdk-for-flutter-navigate-core-geocoordinates-class coordinates, /sdk-for-flutter-navigate-search-searchoptions-class options, /sdk-for-flutter-navigate-search-searchcallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd class="inherited">
  Performs an asynchronous search for /sdk-for-flutter-navigate-search-place-class instances based on the given
geographic coordinates.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="searchByPickedPlace">
/sdk-for-flutter-navigate-search-searchinterface-searchbypickedplace(<wbr/>/sdk-for-flutter-navigate-core-pickedplace-class pickedPlace, /sdk-for-flutter-navigate-core-languagecode? languageCode, /sdk-for-flutter-navigate-search-placeidsearchcallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd class="inherited">
  Performs an asynchronous search for a /sdk-for-flutter-navigate-search-place-class based on the content found in /sdk-for-flutter-navigate-core-pickedplace-class.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="searchByPlaceId">
/sdk-for-flutter-navigate-search-searchinterface-searchbyplaceid(<wbr/>/sdk-for-flutter-navigate-search-placeidquery-class query, /sdk-for-flutter-navigate-core-languagecode? languageCode, /sdk-for-flutter-navigate-search-placeidsearchcallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd class="inherited">
  Performs an asynchronous search for a /sdk-for-flutter-navigate-search-place-class based on its ID and
/sdk-for-flutter-navigate-core-languagecode.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="searchByText">
/sdk-for-flutter-navigate-search-searchinterface-searchbytext(<wbr/>/sdk-for-flutter-navigate-search-textquery-class query, /sdk-for-flutter-navigate-search-searchoptions-class options, /sdk-for-flutter-navigate-search-searchcallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd class="inherited">
  Performs an asynchronous text query search for /sdk-for-flutter-navigate-search-place-class instances within a given /sdk-for-flutter-navigate-search-textqueryarea-class.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="suggestByAddressElements">
/sdk-for-flutter-navigate-search-offlinesearchengine-suggestbyaddresselements(<wbr/>/sdk-for-flutter-navigate-search-structuredquery-class query, /sdk-for-flutter-navigate-search-searchoptions-class options, /sdk-for-flutter-navigate-search-suggestcallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd>
  Performs an asynchronous request to suggest places for a /sdk-for-flutter-navigate-search-structuredquery-class built with address elements and
returns candidate suggestions sorted by relevance.
  

</dd>
<dt class="callable inherited" id="suggestByText">
/sdk-for-flutter-navigate-search-searchinterface-suggestbytext(<wbr/>/sdk-for-flutter-navigate-search-textquery-class query, /sdk-for-flutter-navigate-search-searchoptions-class options, /sdk-for-flutter-navigate-search-suggestcallback callback)
    → /sdk-for-flutter-navigate-core-threading-taskhandle-class

</dt>
<dd class="inherited">
  Performs an asynchronous request to suggest places for text queries and
returns suggestions sorted by relevance.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-search-searchinterface-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-search-searchinterface-operator-equals(<wbr/>Object other)
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
<dt class="callable" id="setIndexOptions">
/sdk-for-flutter-navigate-search-offlinesearchengine-setindexoptions(<wbr/>/sdk-for-flutter-navigate-core-engine-sdknativeengine-class sdkEngine, /sdk-for-flutter-navigate-search-offlinesearchindexoptions-class options, /sdk-for-flutter-navigate-search-offlinesearchindexlistener-class listener)
    → /sdk-for-flutter-navigate-search-offlinesearchindexerror?

</dt>
<dd>
  Enables or disables indexing.
  

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
<li>/sdk-for-flutter-navigate-search-search-library</li>
<li class="self-crumb">OfflineSearchEngine class</li>
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
`
}</HTMLBlock>
