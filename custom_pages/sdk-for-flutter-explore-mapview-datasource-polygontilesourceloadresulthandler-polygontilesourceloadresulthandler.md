---
title: "Implementation"
slug: "sdk-for-flutter-explore-mapview-datasource-polygontilesourceloadresulthandler-polygontilesourceloadresulthandler"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- PolygonTileSourceLoadResultHandler.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview.datasource/mapview.datasource-library.html">/sdk-for-flutter-explore-mapview-datasource-mapview-datasource-library</a></li>
<li><a href="../../mapview.datasource/PolygonTileSourceLoadResultHandler-class.html">/sdk-for-flutter-explore-mapview-datasource-polygontilesourceloadresulthandler-class</a></li>
<li class="self-crumb">PolygonTileSourceLoadResultHandler factory constructor</li>
</ol>
<div class="self-name">PolygonTileSourceLoadResultHandler</div>
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
<div class="main-content" data-above-sidebar="mapview.datasource/PolygonTileSourceLoadResultHandler-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>PolygonTileSourceLoadResultHandler constructor</h1></div>
<section class="multi-line-signature">
PolygonTileSourceLoadResultHandler(<wbr/><ol class="parameter-list single-line"> <li>void loadedLambda(<ol class="parameter-list single-line"> <li><a href="../../mapview.datasource/TileKey-class.html">/sdk-for-flutter-explore-mapview-datasource-tilekey-class</a>, </li>
<li>List&lt;<wbr/><a href="../../mapview.datasource/PolygonData-class.html">/sdk-for-flutter-explore-mapview-datasource-polygondata-class</a>&gt;, </li>
<li><a href="../../mapview.datasource/TileSourceTileMetadata-class.html">/sdk-for-flutter-explore-mapview-datasource-tilesourcetilemetadata-class</a></li>
</ol>), </li>
<li>void failedLambda(<ol class="parameter-list single-line"> <li><a href="../../mapview.datasource/TileKey-class.html">/sdk-for-flutter-explore-mapview-datasource-tilekey-class</a></li>
</ol>)</li>
</ol>)
    </section>
<section class="desc markdown">
<p>Result handler of a load tile request.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory PolygonTileSourceLoadResultHandler(
  void Function(TileKey, List&lt;PolygonData&gt;, TileSourceTileMetadata) loadedLambda,
  void Function(TileKey) failedLambda,

) =&gt; PolygonTileSourceLoadResultHandler$Lambdas(
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
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../mapview.datasource/mapview.datasource-library.html">/sdk-for-flutter-explore-mapview-datasource-mapview-datasource-library</a></li>
<li><a href="../../mapview.datasource/PolygonTileSourceLoadResultHandler-class.html">/sdk-for-flutter-explore-mapview-datasource-polygontilesourceloadresulthandler-class</a></li>
<li class="self-crumb">PolygonTileSourceLoadResultHandler factory constructor</li>
</ol>
<h5>PolygonTileSourceLoadResultHandler class</h5>
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
