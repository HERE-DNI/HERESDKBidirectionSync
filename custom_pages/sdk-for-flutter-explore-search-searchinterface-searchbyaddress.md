---
title: "searchByAddress abstract method"
slug: "sdk-for-flutter-explore-search-searchinterface-searchbyaddress"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- searchByAddress.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-search-search-library</li>
<li>/sdk-for-flutter-explore-search-searchinterface-class</li>
<li class="self-crumb">searchByAddress abstract method</li>
</ol>
<div class="self-name">searchByAddress</div>
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
<h1>searchByAddress abstract method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-explore-core-threading-taskhandle-class
searchByAddress(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-explore-search-addressquery-class query, </li>
<li>/sdk-for-flutter-explore-search-searchoptions-class options, </li>
<li>/sdk-for-flutter-explore-search-searchcallback callback</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Performs an asynchronous address query search for /sdk-for-flutter-explore-search-place-class instances.</p>
<p>This is the same type of search as forward geocoding, except that more data is returned
than just the geographic coordinates of a given address. Note that an address can
belong to more than one /sdk-for-flutter-explore-search-place-class result, although all found places will
share the same geographic coordinates.
The returned places are sorted by relevance.</p>
<ul>
<li>
<p><code>query</code> Desired free-form address query text to search.</p>
</li>
<li>
<p><code>options</code> Search options.</p>
</li>
<li>
<p><code>callback</code> Callback which receives the result on the main thread.</p>
</li>
</ul>
<p>Returns /sdk-for-flutter-explore-core-threading-taskhandle-class. Handle that will be used to manipulate the execution of the task.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle searchByAddress(AddressQuery query, SearchOptions options, SearchCallback callback);</code></pre>
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
<li>/sdk-for-flutter-explore-search-searchinterface-class</li>
<li class="self-crumb">searchByAddress abstract method</li>
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
