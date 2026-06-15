---
title: "RasterTileSourceLoadResultHandler constructor"
slug: "sdk-for-flutter-navigate-mapview-datasource-rastertilesourceloadresulthandler-rastertilesourceloadresulthandler"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RasterTileSourceLoadResultHandler.html -->


<div>
<h1>RasterTileSourceLoadResultHandler constructor</h1></div>

RasterTileSourceLoadResultHandler(<ol class="parameter-list single-line"> <li>void loadedLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-mapview-datasource-tilekey-class">TileKey</a>, </li>
<li>Uint8List, </li>
<li><a href="sdk-for-flutter-navigate-mapview-datasource-tilesourcetilemetadata-class">TileSourceTileMetadata</a></li>
</ol>), </li>
<li>void failedLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-mapview-datasource-tilekey-class">TileKey</a></li>
</ol>)</li>
</ol>)
    

<p>Result handler of a load tile request.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory RasterTileSourceLoadResultHandler(
  void Function(TileKey, Uint8List, TileSourceTileMetadata) loadedLambda,
  void Function(TileKey) failedLambda,

) =&gt; RasterTileSourceLoadResultHandler$Lambdas(
  loadedLambda,
  failedLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
