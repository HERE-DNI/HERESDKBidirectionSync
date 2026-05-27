---
title: "Implementation"
slug: "sdk-for-flutter-explore-search-searchengine-searchbycoordinatesextended"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- searchByCoordinatesExtended.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
<li><a href="../../search/SearchEngine-class.html">/sdk-for-flutter-explore-search-searchengine-class</a></li>
<li class="self-crumb">searchByCoordinatesExtended abstract method</li>
</ol>
<div class="self-name">searchByCoordinatesExtended</div>
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
<div class="main-content" data-above-sidebar="search/SearchEngine-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>searchByCoordinatesExtended abstract method</h1></div>
<section class="multi-line-signature">
<a href="../../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
searchByCoordinatesExtended(<wbr/><ol class="parameter-list single-line"> <li><a href="../../core/GeoCoordinates-class.html">/sdk-for-flutter-explore-core-geocoordinates-class</a> coordinates, </li>
<li><a href="../../search/SearchOptions-class.html">/sdk-for-flutter-explore-search-searchoptions-class</a> options, </li>
<li><a href="../../search/SearchCallbackExtended.html">/sdk-for-flutter-explore-search-searchcallbackextended</a> callback</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Performs an asynchronous request to search for places based on given geographic coordinates.</p>
<p>This is the same process as reverse geocoding, except that more data is returned
than just the <a href="../../search/Address-class.html">/sdk-for-flutter-explore-search-address-class</a> that belongs to given coordinates. Note that coordinates
can belong to more than one <a href="../../search/Place-class.html">/sdk-for-flutter-explore-search-place-class</a> result.
Provides candidate places sorted by relevance.</p>
<ul>
<li>
<p><code>coordinates</code> The coordinates where to search.</p>
</li>
<li>
<p><code>options</code> Search options.</p>
</li>
<li>
<p><code>callback</code> Callback which receives result on the main thread.</p>
</li>
</ul>
<p>Returns <a href="../../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>. Handle that will be used to manipulate execution of the task.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle searchByCoordinatesExtended(GeoCoordinates coordinates, SearchOptions options, SearchCallbackExtended callback);</code></pre>
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
<li><a href="../../search/SearchEngine-class.html">/sdk-for-flutter-explore-search-searchengine-class</a></li>
<li class="self-crumb">searchByCoordinatesExtended abstract method</li>
</ol>
<h5>SearchEngine class</h5>
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
