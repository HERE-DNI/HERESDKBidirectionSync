---
title: "Implementation"
slug: "sdk-for-flutter-explore-search-suggestion-id"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- id.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
<li><a href="../../search/Suggestion-class.html">/sdk-for-flutter-explore-search-suggestion-class</a></li>
<li class="self-crumb">id property</li>
</ol>
<div class="self-name">id</div>
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
<div class="main-content" data-above-sidebar="search/Suggestion-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>id property</h1></div>
<section id="getter">
<section class="multi-line-signature">
String?
id
</section>
<section class="desc markdown">
<p>The unique id of suggested item. It can be used to query further information.
For online search, suggestion of type <a href="../../search/SuggestionType.html">/sdk-for-flutter-explore-search-suggestiontype</a>
will have Suggestion.id same as Place.id.
For offline search, only suggestion of type <a href="../../search/SuggestionType.html">/sdk-for-flutter-explore-search-suggestiontype</a>,
will have this property filled with identifier number of an associated chain.
For example, the chain ID "8778" corresponds to the chain name "ABC Shop".
For other types, <a href="../../search/SuggestionType.html">/sdk-for-flutter-explore-search-suggestiontype</a> and <a href="../../search/SuggestionType.html">/sdk-for-flutter-explore-search-suggestiontype</a>
this property will be null.
Gets the suggested item id.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">String? get id;</code></pre>
</section>
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
<li><a href="../../search/Suggestion-class.html">/sdk-for-flutter-explore-search-suggestion-class</a></li>
<li class="self-crumb">id property</li>
</ol>
<h5>Suggestion class</h5>
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
