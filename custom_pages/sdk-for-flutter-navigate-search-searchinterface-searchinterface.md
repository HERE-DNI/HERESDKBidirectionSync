---
title: "SearchInterface constructor"
slug: "sdk-for-flutter-navigate-search-searchinterface-searchinterface"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SearchInterface.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-search-search-library</li>
<li>/sdk-for-flutter-navigate-search-searchinterface-class</li>
<li class="self-crumb">SearchInterface factory constructor</li>
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
<div class="main-content" data-above-sidebar="search/SearchInterface-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>SearchInterface constructor</h1></div>
<section class="multi-line-signature">
SearchInterface(<wbr/><ol class="parameter-list"> <li>/sdk-for-flutter-navigate-core-threading-taskhandle-class searchByTextLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-search-textquery-class, </li>
<li>/sdk-for-flutter-navigate-search-searchoptions-class, </li>
<li>/sdk-for-flutter-navigate-search-searchcallback </li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-core-threading-taskhandle-class searchByAddressLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-search-addressquery-class, </li>
<li>/sdk-for-flutter-navigate-search-searchoptions-class, </li>
<li>/sdk-for-flutter-navigate-search-searchcallback </li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-core-threading-taskhandle-class searchByCategoryLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-search-categoryquery-class, </li>
<li>/sdk-for-flutter-navigate-search-searchoptions-class, </li>
<li>/sdk-for-flutter-navigate-search-searchcallback </li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-core-threading-taskhandle-class searchByCoordinatesLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-core-geocoordinates-class, </li>
<li>/sdk-for-flutter-navigate-search-searchoptions-class, </li>
<li>/sdk-for-flutter-navigate-search-searchcallback </li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-core-threading-taskhandle-class searchByPlaceIdLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-search-placeidquery-class, </li>
<li>/sdk-for-flutter-navigate-core-languagecode?, </li>
<li>/sdk-for-flutter-navigate-search-placeidsearchcallback </li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-core-threading-taskhandle-class searchByPickedPlaceLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-core-pickedplace-class, </li>
<li>/sdk-for-flutter-navigate-core-languagecode?, </li>
<li>/sdk-for-flutter-navigate-search-placeidsearchcallback </li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-core-threading-taskhandle-class suggestByTextLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-search-textquery-class, </li>
<li>/sdk-for-flutter-navigate-search-searchoptions-class, </li>
<li>/sdk-for-flutter-navigate-search-suggestcallback </li>
</ol>), </li>
</ol>)
    </section>
<section class="desc markdown">
<p>Provides the abstract class for the online and offline
search engines.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory SearchInterface(
  TaskHandle Function(TextQuery, SearchOptions, SearchCallback) searchByTextLambda,
  TaskHandle Function(AddressQuery, SearchOptions, SearchCallback) searchByAddressLambda,
  TaskHandle Function(CategoryQuery, SearchOptions, SearchCallback) searchByCategoryLambda,
  TaskHandle Function(GeoCoordinates, SearchOptions, SearchCallback) searchByCoordinatesLambda,
  TaskHandle Function(PlaceIdQuery, LanguageCode?, PlaceIdSearchCallback) searchByPlaceIdLambda,
  TaskHandle Function(PickedPlace, LanguageCode?, PlaceIdSearchCallback) searchByPickedPlaceLambda,
  TaskHandle Function(TextQuery, SearchOptions, SuggestCallback) suggestByTextLambda,

) =&gt; SearchInterface$Lambdas(
  searchByTextLambda,
  searchByAddressLambda,
  searchByCategoryLambda,
  searchByCoordinatesLambda,
  searchByPlaceIdLambda,
  searchByPickedPlaceLambda,
  suggestByTextLambda,

);</code></pre>
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
<li>/sdk-for-flutter-navigate-search-searchinterface-class</li>
<li class="self-crumb">SearchInterface factory constructor</li>
</ol>
<h5>SearchInterface class</h5>
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
