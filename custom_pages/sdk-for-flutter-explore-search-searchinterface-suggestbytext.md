---
title: "Implementation"
slug: "sdk-for-flutter-explore-search-searchinterface-suggestbytext"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- suggestByText.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
<li><a href="../../search/SearchInterface-class.html">/sdk-for-flutter-explore-search-searchinterface-class</a></li>
<li class="self-crumb">suggestByText abstract method</li>
</ol>
<div class="self-name">suggestByText</div>
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
<h1>suggestByText abstract method</h1></div>
<section class="multi-line-signature">
<a href="../../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
suggestByText(<wbr/><ol class="parameter-list single-line"> <li><a href="../../search/TextQuery-class.html">/sdk-for-flutter-explore-search-textquery-class</a> query, </li>
<li><a href="../../search/SearchOptions-class.html">/sdk-for-flutter-explore-search-searchoptions-class</a> options, </li>
<li><a href="../../search/SuggestCallback.html">/sdk-for-flutter-explore-search-suggestcallback</a> callback</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Performs an asynchronous request to suggest places for text queries and
returns suggestions sorted by relevance.</p>
<p>Note that while <code>OfflineSearchEngine</code> includes as many details as are available,
<code>SearchEngine</code> includes only the information that is relevant for autosuggest use cases.
Complete details can be obtained by searching with <a href="../../search/PlaceIdQuery-class.html">/sdk-for-flutter-explore-search-placeidquery-class</a>.</p>
<ul>
<li>
<p><code>query</code> Desired text query to search.</p>
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
<pre class="language-dart"><code class="language-dart">TaskHandle suggestByText(TextQuery query, SearchOptions options, SuggestCallback callback);</code></pre>
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
<li class="self-crumb">suggestByText abstract method</li>
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
