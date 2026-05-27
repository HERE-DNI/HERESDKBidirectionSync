---
title: "Implementation"
slug: "sdk-for-flutter-explore-search-searchengine-searchbytextextended"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- searchByTextExtended.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
<li><a href="../../search/SearchEngine-class.html">/sdk-for-flutter-explore-search-searchengine-class</a></li>
<li class="self-crumb">searchByTextExtended abstract method</li>
</ol>
<div class="self-name">searchByTextExtended</div>
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
<h1>searchByTextExtended abstract method</h1></div>
<section class="multi-line-signature">
<a href="../../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
searchByTextExtended(<wbr/><ol class="parameter-list single-line"> <li><a href="../../search/TextQuery-class.html">/sdk-for-flutter-explore-search-textquery-class</a> query, </li>
<li><a href="../../search/SearchOptions-class.html">/sdk-for-flutter-explore-search-searchoptions-class</a> options, </li>
<li><a href="../../search/SearchCallbackExtended.html">/sdk-for-flutter-explore-search-searchcallbackextended</a> callback</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Performs an asynchronous request to do a text query search for <a href="../../search/Place-class.html">/sdk-for-flutter-explore-search-place-class</a> instances.</p>
<p>Optionally, search along a polyline, such as a route, by specifying a <a href="../../core/GeoCorridor-class.html">/sdk-for-flutter-explore-core-geocorridor-class</a>.
Provides candidate places sorted by relevance.</p>
<ul>
<li>
<p><code>query</code> Desired free-form text query to search.</p>
</li>
<li>
<p><code>options</code> Search options.</p>
</li>
<li>
<p><code>callback</code> Callback which receives the result on the main thread.</p>
</li>
</ul>
<p>Returns <a href="../../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>. Handle that will be used to manipulate the execution of the task.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle searchByTextExtended(TextQuery query, SearchOptions options, SearchCallbackExtended callback);</code></pre>
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
<li class="self-crumb">searchByTextExtended abstract method</li>
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
