---
title: "Untitled"
slug: "sdk-for-flutter-navigate-search-offlinesearchindexlistener-onstarted"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- onStarted.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-search-search-library</li>
<li>/sdk-for-flutter-navigate-search-offlinesearchindexlistener-class</li>
<li class="self-crumb">onStarted abstract method</li>
</ol>
<div class="self-name">onStarted</div>
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
<div class="main-content" data-above-sidebar="search/OfflineSearchIndexListener-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>onStarted abstract method</h1></div>
<section class="multi-line-signature">
void
onStarted(<wbr/><ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-search-offlinesearchindexoperation operation</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Called each time that the indexing has started.</p>
<p>It is triggered by changes to persistent map
or by calling <code>OfflineSearchEngine.setIndexOptions</code>.
If a valid index was previously created for the installed regions, no additional indexing
is performed, so no notifications are sent. In this context, a valid index is the one
that contains data for the exact versions of the installed map regions. When any of them
is updated or new regions are downloaded or deleted, the index becomes invalid and is
automatically rebuilt, as long as indexing has been enabled previously.
Invoked on the main thread.</p>
<ul>
<li><code>operation</code> Shows whether the index is being created or removed.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void onStarted(OfflineSearchIndexOperation operation);</code></pre>
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
<li>/sdk-for-flutter-navigate-search-offlinesearchindexlistener-class</li>
<li class="self-crumb">onStarted abstract method</li>
</ol>
<h5>OfflineSearchIndexListener class</h5>
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
