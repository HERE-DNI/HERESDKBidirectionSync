---
title: "RasterTileSourceLoadResultHandler constructor"
slug: "sdk-for-flutter-explore-mapview-datasource-rastertilesourceloadresulthandler-rastertilesourceloadresulthandler"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RasterTileSourceLoadResultHandler.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-datasource-mapview-datasource-library</li>
<li>/sdk-for-flutter-explore-mapview-datasource-rastertilesourceloadresulthandler-class</li>
<li class="self-crumb">RasterTileSourceLoadResultHandler factory constructor</li>
</ol>
<div class="self-name">RasterTileSourceLoadResultHandler</div>
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
<div class="main-content" data-above-sidebar="mapview.datasource/RasterTileSourceLoadResultHandler-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>RasterTileSourceLoadResultHandler constructor</h1></div>
<section class="multi-line-signature">
RasterTileSourceLoadResultHandler(<wbr/><ol class="parameter-list single-line"> <li>void loadedLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-explore-mapview-datasource-tilekey-class, </li>
<li>Uint8List, </li>
<li>/sdk-for-flutter-explore-mapview-datasource-tilesourcetilemetadata-class</li>
</ol>), </li>
<li>void failedLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-explore-mapview-datasource-tilekey-class</li>
</ol>)</li>
</ol>)
    </section>
<section class="desc markdown">
<p>Result handler of a load tile request.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory RasterTileSourceLoadResultHandler(
  void Function(TileKey, Uint8List, TileSourceTileMetadata) loadedLambda,
  void Function(TileKey) failedLambda,

) =&gt; RasterTileSourceLoadResultHandler$Lambdas(
  loadedLambda,
  failedLambda,

);</code></pre>
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
<li>/sdk-for-flutter-explore-mapview-datasource-rastertilesourceloadresulthandler-class</li>
<li class="self-crumb">RasterTileSourceLoadResultHandler factory constructor</li>
</ol>
<h5>RasterTileSourceLoadResultHandler class</h5>
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
