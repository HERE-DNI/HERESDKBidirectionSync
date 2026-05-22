---
title: "Untitled"
slug: "sdk-for-flutter-explore-search-searchinterface-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SearchInterface-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-search-search-library</li>
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
<li>/sdk-for-flutter-explore-search-searchengine-class</li>
</ul></dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="SearchInterface">
/sdk-for-flutter-explore-search-searchinterface-searchinterface(/sdk-for-flutter-explore-core-threading-taskhandle-class searchByTextLambda(/sdk-for-flutter-explore-search-textquery-class, /sdk-for-flutter-explore-search-searchoptions-class, /sdk-for-flutter-explore-search-searchcallback ), /sdk-for-flutter-explore-core-threading-taskhandle-class searchByAddressLambda(/sdk-for-flutter-explore-search-addressquery-class, /sdk-for-flutter-explore-search-searchoptions-class, /sdk-for-flutter-explore-search-searchcallback ), /sdk-for-flutter-explore-core-threading-taskhandle-class searchByCategoryLambda(/sdk-for-flutter-explore-search-categoryquery-class, /sdk-for-flutter-explore-search-searchoptions-class, /sdk-for-flutter-explore-search-searchcallback ), /sdk-for-flutter-explore-core-threading-taskhandle-class searchByCoordinatesLambda(/sdk-for-flutter-explore-core-geocoordinates-class, /sdk-for-flutter-explore-search-searchoptions-class, /sdk-for-flutter-explore-search-searchcallback ), /sdk-for-flutter-explore-core-threading-taskhandle-class searchByPlaceIdLambda(/sdk-for-flutter-explore-search-placeidquery-class, /sdk-for-flutter-explore-core-languagecode?, /sdk-for-flutter-explore-search-placeidsearchcallback ), /sdk-for-flutter-explore-core-threading-taskhandle-class searchByPickedPlaceLambda(/sdk-for-flutter-explore-core-pickedplace-class, /sdk-for-flutter-explore-core-languagecode?, /sdk-for-flutter-explore-search-placeidsearchcallback ), /sdk-for-flutter-explore-core-threading-taskhandle-class suggestByTextLambda(/sdk-for-flutter-explore-search-textquery-class, /sdk-for-flutter-explore-search-searchoptions-class, /sdk-for-flutter-explore-search-suggestcallback ))
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
<dt class="callable" id="searchByAddress">
/sdk-for-flutter-explore-search-searchinterface-searchbyaddress(<wbr/>/sdk-for-flutter-explore-search-addressquery-class query, /sdk-for-flutter-explore-search-searchoptions-class options, /sdk-for-flutter-explore-search-searchcallback callback)
    → /sdk-for-flutter-explore-core-threading-taskhandle-class

</dt>
<dd>
  Performs an asynchronous address query search for /sdk-for-flutter-explore-search-place-class instances.
  

</dd>
<dt class="callable" id="searchByCategory">
/sdk-for-flutter-explore-search-searchinterface-searchbycategory(<wbr/>/sdk-for-flutter-explore-search-categoryquery-class query, /sdk-for-flutter-explore-search-searchoptions-class options, /sdk-for-flutter-explore-search-searchcallback callback)
    → /sdk-for-flutter-explore-core-threading-taskhandle-class

</dt>
<dd>
  Performs an asynchronous category search for /sdk-for-flutter-explore-search-place-class instances.
  

</dd>
<dt class="callable" id="searchByCoordinates">
/sdk-for-flutter-explore-search-searchinterface-searchbycoordinates(<wbr/>/sdk-for-flutter-explore-core-geocoordinates-class coordinates, /sdk-for-flutter-explore-search-searchoptions-class options, /sdk-for-flutter-explore-search-searchcallback callback)
    → /sdk-for-flutter-explore-core-threading-taskhandle-class

</dt>
<dd>
  Performs an asynchronous search for /sdk-for-flutter-explore-search-place-class instances based on the given
geographic coordinates.
  

</dd>
<dt class="callable" id="searchByPickedPlace">
/sdk-for-flutter-explore-search-searchinterface-searchbypickedplace(<wbr/>/sdk-for-flutter-explore-core-pickedplace-class pickedPlace, /sdk-for-flutter-explore-core-languagecode? languageCode, /sdk-for-flutter-explore-search-placeidsearchcallback callback)
    → /sdk-for-flutter-explore-core-threading-taskhandle-class

</dt>
<dd>
  Performs an asynchronous search for a /sdk-for-flutter-explore-search-place-class based on the content found in /sdk-for-flutter-explore-core-pickedplace-class.
  

</dd>
<dt class="callable" id="searchByPlaceId">
/sdk-for-flutter-explore-search-searchinterface-searchbyplaceid(<wbr/>/sdk-for-flutter-explore-search-placeidquery-class query, /sdk-for-flutter-explore-core-languagecode? languageCode, /sdk-for-flutter-explore-search-placeidsearchcallback callback)
    → /sdk-for-flutter-explore-core-threading-taskhandle-class

</dt>
<dd>
  Performs an asynchronous search for a /sdk-for-flutter-explore-search-place-class based on its ID and
/sdk-for-flutter-explore-core-languagecode.
  

</dd>
<dt class="callable" id="searchByText">
/sdk-for-flutter-explore-search-searchinterface-searchbytext(<wbr/>/sdk-for-flutter-explore-search-textquery-class query, /sdk-for-flutter-explore-search-searchoptions-class options, /sdk-for-flutter-explore-search-searchcallback callback)
    → /sdk-for-flutter-explore-core-threading-taskhandle-class

</dt>
<dd>
  Performs an asynchronous text query search for /sdk-for-flutter-explore-search-place-class instances within a given /sdk-for-flutter-explore-search-textqueryarea-class.
  

</dd>
<dt class="callable" id="suggestByText">
/sdk-for-flutter-explore-search-searchinterface-suggestbytext(<wbr/>/sdk-for-flutter-explore-search-textquery-class query, /sdk-for-flutter-explore-search-searchoptions-class options, /sdk-for-flutter-explore-search-suggestcallback callback)
    → /sdk-for-flutter-explore-core-threading-taskhandle-class

</dt>
<dd>
  Performs an asynchronous request to suggest places for text queries and
returns suggestions sorted by relevance.
  

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



</div>
`
}</HTMLBlock>
