---
title: "Implementation"
slug: "sdk-for-flutter-explore-mapview-datasource-rastertilesource-loadtile"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- loadTile.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview.datasource/mapview.datasource-library.html">/sdk-for-flutter-explore-mapview-datasource-mapview-datasource-library</a></li>
<li><a href="../../mapview.datasource/RasterTileSource-class.html">/sdk-for-flutter-explore-mapview-datasource-rastertilesource-class</a></li>
<li class="self-crumb">loadTile abstract method</li>
</ol>
<div class="self-name">loadTile</div>
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
<div class="main-content" data-above-sidebar="mapview.datasource/RasterTileSource-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>loadTile abstract method</h1></div>
<section class="multi-line-signature">
<a href="../../mapview.datasource/TileSourceLoadTileRequestHandle-class.html">/sdk-for-flutter-explore-mapview-datasource-tilesourceloadtilerequesthandle-class</a>?
loadTile(<wbr/><ol class="parameter-list single-line"> <li><a href="../../mapview.datasource/TileKey-class.html">/sdk-for-flutter-explore-mapview-datasource-tilekey-class</a> tileKey, </li>
<li><a href="../../mapview.datasource/RasterTileSourceLoadResultHandler-class.html">/sdk-for-flutter-explore-mapview-datasource-rastertilesourceloadresulthandler-class</a> completionHandler</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Load data of a tile.</p>
<p>Upon completion, the handler gets informed.</p>
<ul>
<li>
<p><code>tileKey</code> Key of the tile to load data for.</p>
</li>
<li>
<p><code>completionHandler</code> Load result handler.</p>
</li>
</ul>
<p>Returns <a href="../../mapview.datasource/TileSourceLoadTileRequestHandle-class.html">/sdk-for-flutter-explore-mapview-datasource-tilesourceloadtilerequesthandle-class</a>. A handle to the created load request.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TileSourceLoadTileRequestHandle? loadTile(TileKey tileKey, RasterTileSourceLoadResultHandler completionHandler);</code></pre>
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
<li><a href="../../mapview.datasource/mapview.datasource-library.html">/sdk-for-flutter-explore-mapview-datasource-mapview-datasource-library</a></li>
<li><a href="../../mapview.datasource/RasterTileSource-class.html">/sdk-for-flutter-explore-mapview-datasource-rastertilesource-class</a></li>
<li class="self-crumb">loadTile abstract method</li>
</ol>
<h5>RasterTileSource class</h5>
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
