---
title: "Implementation"
slug: "sdk-for-flutter-explore-search-searchinterface-searchbypickedplace"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- searchByPickedPlace.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
<li><a href="../../search/SearchInterface-class.html">/sdk-for-flutter-explore-search-searchinterface-class</a></li>
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
<a href="../../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
searchByPickedPlace(<wbr/><ol class="parameter-list single-line"> <li><a href="../../core/PickedPlace-class.html">/sdk-for-flutter-explore-core-pickedplace-class</a> pickedPlace, </li>
<li><a href="../../core/LanguageCode.html">/sdk-for-flutter-explore-core-languagecode</a>? languageCode, </li>
<li><a href="../../search/PlaceIdSearchCallback.html">/sdk-for-flutter-explore-search-placeidsearchcallback</a> callback</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Performs an asynchronous search for a <a href="../../search/Place-class.html">/sdk-for-flutter-explore-search-place-class</a> based on the content found in <a href="../../core/PickedPlace-class.html">/sdk-for-flutter-explore-core-pickedplace-class</a>.</p>
<p>If <a href="../../core/PickedPlace-class.html">/sdk-for-flutter-explore-core-pickedplace-class</a> data is obtained from the offline map, it may happen that the newer version
that is used by the online service represented by <code>SearchEngine</code> no longer contains the
related POI. In that case, <a href="../../search/SearchError.html">/sdk-for-flutter-explore-search-searcherror</a> error is reported.
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
<p>Returns <a href="../../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>. Handle that will be used to manipulate the execution of the task.</p>
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
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
<li><a href="../../search/SearchInterface-class.html">/sdk-for-flutter-explore-search-searchinterface-class</a></li>
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
</HTMLBlock>
