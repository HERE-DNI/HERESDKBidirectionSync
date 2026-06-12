---
title: "RasterTileSource constructor"
slug: "sdk-for-flutter-navigate-mapview-datasource-rastertilesource-rastertilesource"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RasterTileSource.html -->


<div>
<h1>RasterTileSource constructor</h1></div>

RasterTileSource(<ol class="parameter-list"> <li><a href="/sdk-for-flutter-navigate-mapview-datasource-tilesourcedataversion-class">TileSourceDataVersion</a> getDataVersionLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-mapview-datasource-tilekey-class">TileKey</a></li>
</ol>), </li>
<li>void addListenerLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-mapview-datasource-tilesourcelistener-class">TileSourceListener</a></li>
</ol>), </li>
<li>void removeListenerLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-mapview-datasource-tilesourcelistener-class">TileSourceListener</a></li>
</ol>), </li>
<li><a href="/sdk-for-flutter-navigate-mapview-datasource-tilesourceloadtilerequesthandle-class">TileSourceLoadTileRequestHandle</a>? loadTileLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-mapview-datasource-tilekey-class">TileKey</a>, </li>
<li><a href="/sdk-for-flutter-navigate-mapview-datasource-rastertilesourceloadresulthandler-class">RasterTileSourceLoadResultHandler</a></li>
</ol>), </li>
<li><a href="/sdk-for-flutter-navigate-mapview-datasource-tilingscheme">TilingScheme</a> tilingSchemeGetLambda(), </li>
<li>List&lt;int&gt; storageLevelsGetLambda(), </li>
</ol>)
    

<p>A source of raster tiles.</p>
<p>The implementations must be thread-safe.
Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory RasterTileSource(
  TileSourceDataVersion Function(TileKey) getDataVersionLambda,
  void Function(TileSourceListener) addListenerLambda,
  void Function(TileSourceListener) removeListenerLambda,
  TileSourceLoadTileRequestHandle? Function(TileKey, RasterTileSourceLoadResultHandler) loadTileLambda,
  TilingScheme Function() tilingSchemeGetLambda,
  List&lt;int&gt; Function() storageLevelsGetLambda
) =&gt; RasterTileSource$Lambdas(
  getDataVersionLambda,
  addListenerLambda,
  removeListenerLambda,
  loadTileLambda,
  tilingSchemeGetLambda,
  storageLevelsGetLambda
);</code></pre>

 



</div>
`
}</HTMLBlock>
