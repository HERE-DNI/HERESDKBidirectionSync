---
title: "SuggestCallback typedef"
slug: "sdk-for-flutter-navigate-search-suggestcallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SuggestCallback.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-search-search-library</li>
<li class="self-crumb">SuggestCallback typedef</li>
</ol>
<div class="self-name">SuggestCallback</div>
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
<div class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>SuggestCallback typedef</h1></div>
<section class="multi-line-signature">
SuggestCallback =
     void Function(/sdk-for-flutter-navigate-search-searcherror? searchError, List&lt;<wbr/>/sdk-for-flutter-navigate-search-suggestion-class&gt;? suggestions)
</section>
<section class="desc markdown">
<p>The method will be called on the main thread when a suggest call has been completed.</p>
<p>The first argument indicates an error in case of a failure. The second argument contains the results.
Both arguments cannot be <code>null</code> at the same time - or not <code>null</code> at the same time.</p>
<ul>
<li>
<p><code>searchError</code> An error enum indicating what went wrong. It is <code>null</code> for an operation that succeeds.</p>
</li>
<li>
<p><code>suggestions</code> The list of suggestion results. It is <code>null</code> in case of an error.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">typedef SuggestCallback = void Function(SearchError? searchError, List&lt;Suggestion&gt;? suggestions);</code></pre>
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
<li class="self-crumb">SuggestCallback typedef</li>
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
