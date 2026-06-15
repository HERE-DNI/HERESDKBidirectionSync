---
title: "TileSource constructor"
slug: "sdk-for-flutter-navigate-mapview-datasource-tilesource-tilesource"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TileSource.html -->


<div>
<h1>TileSource constructor</h1></div>

TileSource(<ol class="parameter-list"> <li><a href="sdk-for-flutter-navigate-mapview-datasource-tilesourcedataversion-class">TileSourceDataVersion</a> getDataVersionLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-mapview-datasource-tilekey-class">TileKey</a></li>
</ol>), </li>
<li>void addListenerLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-mapview-datasource-tilesourcelistener-class">TileSourceListener</a></li>
</ol>), </li>
<li>void removeListenerLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-mapview-datasource-tilesourcelistener-class">TileSourceListener</a></li>
</ol>), </li>
<li><a href="sdk-for-flutter-navigate-mapview-datasource-tilingscheme">TilingScheme</a> tilingSchemeGetLambda(), </li>
<li>List&lt;int&gt; storageLevelsGetLambda(), </li>
</ol>)
    

<p>A source of tiles.</p>
<p>The implementations must be thread-safe.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory TileSource(
  TileSourceDataVersion Function(TileKey) getDataVersionLambda,
  void Function(TileSourceListener) addListenerLambda,
  void Function(TileSourceListener) removeListenerLambda,
  TilingScheme Function() tilingSchemeGetLambda,
  List&lt;int&gt; Function() storageLevelsGetLambda
) =&gt; TileSource$Lambdas(
  getDataVersionLambda,
  addListenerLambda,
  removeListenerLambda,
  tilingSchemeGetLambda,
  storageLevelsGetLambda
);</code></pre>

 



</div>
`
}</HTMLBlock>
