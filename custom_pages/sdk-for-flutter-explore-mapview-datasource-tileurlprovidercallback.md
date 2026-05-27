---
title: "TileUrlProviderCallback typedef"
slug: "sdk-for-flutter-explore-mapview-datasource-tileurlprovidercallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TileUrlProviderCallback.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-datasource-mapview-datasource-library</li>
<li class="self-crumb">TileUrlProviderCallback typedef</li>
</ol>
<div class="self-name">TileUrlProviderCallback</div>
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
<div class="main-content" data-above-sidebar="mapview.datasource/mapview.datasource-library-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>TileUrlProviderCallback typedef</h1></div>
<section class="multi-line-signature">
TileUrlProviderCallback =
     String Function(int x, int y, int level)
</section>
<section class="desc markdown">
<p>Provides the URL as String for the given tile coordinates and storage level.</p>
<p>The first and second parameters correspond to the X and Y coordinates of the tile, respectively, and have values ranging from 0 to 2^level − 1.
The third parameter indicates the level of the tile.</p>
<ul>
<li>
<p><code>x</code> X coordinate of the tile. This ranges from 0 to 2^level − 1.</p>
</li>
<li>
<p><code>y</code> Y coordinate of the tile. This ranges from 0 to 2^level − 1.</p>
</li>
<li>
<p><code>level</code> Level of the tile.</p>
</li>
</ul>
<p>Returns the URL.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">typedef TileUrlProviderCallback = String Function(int x, int y, int level);</code></pre>
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
<li>/sdk-for-flutter-explore-mapview-datasource-mapview-datasource-library</li>
<li class="self-crumb">TileUrlProviderCallback typedef</li>
</ol>
<h5>mapview.datasource library</h5>
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
