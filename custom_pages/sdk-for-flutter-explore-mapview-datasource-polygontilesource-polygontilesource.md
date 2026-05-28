---
title: "PolygonTileSource constructor"
slug: "sdk-for-flutter-explore-mapview-datasource-polygontilesource-polygontilesource"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- PolygonTileSource.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-datasource-mapview-datasource-library</li>
<li>/sdk-for-flutter-explore-mapview-datasource-polygontilesource-class</li>
<li class="self-crumb">PolygonTileSource factory constructor</li>
</ol>
<div class="self-name">PolygonTileSource</div>
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
<div class="main-content" data-above-sidebar="mapview.datasource/PolygonTileSource-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>PolygonTileSource constructor</h1></div>
<section class="multi-line-signature">
PolygonTileSource(<wbr/><ol class="parameter-list"> <li>/sdk-for-flutter-explore-mapview-datasource-tilesourcedataversion-class getDataVersionLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-explore-mapview-datasource-tilekey-class</li>
</ol>), </li>
<li>void addListenerLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-explore-mapview-datasource-tilesourcelistener-class</li>
</ol>), </li>
<li>void removeListenerLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-explore-mapview-datasource-tilesourcelistener-class</li>
</ol>), </li>
<li>/sdk-for-flutter-explore-mapview-datasource-tilesourceloadtilerequesthandle-class? loadTileLambda(<ol class="parameter-list single-line"> <li>/sdk-for-flutter-explore-mapview-datasource-tilekey-class, </li>
<li>/sdk-for-flutter-explore-mapview-datasource-polygontilesourceloadresulthandler-class</li>
</ol>), </li>
<li>/sdk-for-flutter-explore-mapview-datasource-tilingscheme tilingSchemeGetLambda(), </li>
<li>List&lt;<wbr/>int&gt; storageLevelsGetLambda(), </li>
</ol>)
    </section>
<section class="desc markdown">
<p>A source of geodetic polygon tiles.</p>
<p>Polygons provided by an implementation must be clipped to the boundaries of the requested tile.
The implementations must be thread-safe.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory PolygonTileSource(
  TileSourceDataVersion Function(TileKey) getDataVersionLambda,
  void Function(TileSourceListener) addListenerLambda,
  void Function(TileSourceListener) removeListenerLambda,
  TileSourceLoadTileRequestHandle? Function(TileKey, PolygonTileSourceLoadResultHandler) loadTileLambda,
  TilingScheme Function() tilingSchemeGetLambda,
  List&lt;int&gt; Function() storageLevelsGetLambda
) =&gt; PolygonTileSource$Lambdas(
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
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-datasource-mapview-datasource-library</li>
<li>/sdk-for-flutter-explore-mapview-datasource-polygontilesource-class</li>
<li class="self-crumb">PolygonTileSource factory constructor</li>
</ol>
<h5>PolygonTileSource class</h5>
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
