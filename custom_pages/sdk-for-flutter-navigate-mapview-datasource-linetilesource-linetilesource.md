---
title: "Untitled"
slug: "sdk-for-flutter-navigate-mapview-datasource-linetilesource-linetilesource"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LineTileSource.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-datasource-mapview-datasource-library</li>
<li>/sdk-for-flutter-navigate-mapview-datasource-linetilesource-class</li>
<li class="self-crumb">LineTileSource factory constructor</li>
</ol>
<div class="self-name">LineTileSource</div>
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
<div class="main-content" data-above-sidebar="mapview.datasource/LineTileSource-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>LineTileSource constructor</h1></div>
<section class="multi-line-signature">
LineTileSource(<wbr/><ol class="parameter-list"> <li>/sdk-for-flutter-navigate-mapview-datasource-tilesourcedataversion-class getDataVersionLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-mapview-datasource-tilekey-class</li>
</ol>), </li>
<li>void addListenerLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-mapview-datasource-tilesourcelistener-class</li>
</ol>), </li>
<li>void removeListenerLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-mapview-datasource-tilesourcelistener-class</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-mapview-datasource-tilesourceloadtilerequesthandle-class? loadTileLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-navigate-mapview-datasource-tilekey-class, </li>
<li>/sdk-for-flutter-navigate-mapview-datasource-linetilesourceloadresulthandler-class</li>
</ol>), </li>
<li>/sdk-for-flutter-navigate-mapview-datasource-tilingscheme tilingSchemeGetLambda(), </li>
<li>List&lt;<wbr/>int&gt; storageLevelsGetLambda(), </li>
</ol>)
    </section>
<section class="desc markdown">
<p>A source of geodetic line tiles.</p>
<p>Lines provided by an implementation must be clipped to the boundaries of the requested tile.
The implementations must be thread-safe.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory LineTileSource(
  TileSourceDataVersion Function(TileKey) getDataVersionLambda,
  void Function(TileSourceListener) addListenerLambda,
  void Function(TileSourceListener) removeListenerLambda,
  TileSourceLoadTileRequestHandle? Function(TileKey, LineTileSourceLoadResultHandler) loadTileLambda,
  TilingScheme Function() tilingSchemeGetLambda,
  List&lt;int&gt; Function() storageLevelsGetLambda
) =&gt; LineTileSource$Lambdas(
  getDataVersionLambda,
  addListenerLambda,
  removeListenerLambda,
  loadTileLambda,
  tilingSchemeGetLambda,
  storageLevelsGetLambda
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
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-datasource-mapview-datasource-library</li>
<li>/sdk-for-flutter-navigate-mapview-datasource-linetilesource-class</li>
<li class="self-crumb">LineTileSource factory constructor</li>
</ol>
<h5>LineTileSource class</h5>
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
