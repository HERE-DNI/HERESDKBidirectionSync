---
title: "searchByPickedPlace abstract method"
slug: "sdk-for-flutter-navigate-search-searchinterface-searchbypickedplace"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- searchByPickedPlace.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-search-search-library</li>
<li>/sdk-for-flutter-navigate-search-searchinterface-class</li>
<li class="self-crumb">searchByPickedPlace abstract method</li>
</ol>
<div class="self-name">searchByPickedPlace</div>
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
<h1>searchByPickedPlace abstract method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-core-threading-taskhandle-class
searchByPickedPlace(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-core-pickedplace-class pickedPlace, </li>
<li>/sdk-for-flutter-navigate-core-languagecode? languageCode, </li>
<li>/sdk-for-flutter-navigate-search-placeidsearchcallback callback</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Performs an asynchronous search for a /sdk-for-flutter-navigate-search-place-class based on the content found in /sdk-for-flutter-navigate-core-pickedplace-class.</p>
<p>If /sdk-for-flutter-navigate-core-pickedplace-class data is obtained from the offline map, it may happen that the newer version
that is used by the online service represented by <code>SearchEngine</code> no longer contains the
related POI. In that case, /sdk-for-flutter-navigate-search-searcherror error is reported.
When that happens, you may try to obtain the POI from the offline map by calling
<code>OfflineSearchEngine.searchByPickedPlace</code>, only available for the Navigate license.</p>
<ul>
<li>
<p><code>pickedPlace</code> The content picked from map.</p>
</li>
<li>
<p><code>languageCode</code> The preferred language for the search result. When unset or unsupported language is chosen,
result will be returned in the local language.</p>
</li>
<li>
<p><code>callback</code> Callback which receives the result on the main thread.</p>
</li>
</ul>
<p>Returns /sdk-for-flutter-navigate-core-threading-taskhandle-class. Handle that will be used to manipulate the execution of the task.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle searchByPickedPlace(PickedPlace pickedPlace, LanguageCode? languageCode, PlaceIdSearchCallback callback);</code></pre>
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
<li class="self-crumb">searchByPickedPlace abstract method</li>
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
