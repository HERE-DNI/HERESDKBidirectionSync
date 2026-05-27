---
title: "Implementation"
slug: "sdk-for-flutter-explore-search-evsearchcallback"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- EVSearchCallback.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
<li class="self-crumb">EVSearchCallback typedef</li>
</ol>
<div class="self-name">EVSearchCallback</div>
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
<h1>EVSearchCallback typedef</h1></div>
<section class="multi-line-signature">
EVSearchCallback =
     void Function(<a href="../search/EVSearchError.html">/sdk-for-flutter-explore-search-evsearcherror</a>? error, List&lt;<wbr/><a href="../search/EVChargingLocation-class.html">/sdk-for-flutter-explore-search-evcharginglocation-class</a>&gt;? chargingLocations)
</section>
<section class="desc markdown">
<p>The method that will be called on the main thread when a search operation in <code>EVSearchEngine</code>
has been completed.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<ul>
<li>
<p><code>error</code> The ev search error.</p>
</li>
<li>
<p><code>chargingLocations</code> The ev charging locations.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">typedef EVSearchCallback = void Function(EVSearchError? error, List&lt;EVChargingLocation&gt;? chargingLocations);</code></pre>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
<li class="self-crumb">EVSearchCallback typedef</li>
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
</HTMLBlock>
