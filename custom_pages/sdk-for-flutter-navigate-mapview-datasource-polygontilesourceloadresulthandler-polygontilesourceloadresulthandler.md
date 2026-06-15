---
title: "PolygonTileSourceLoadResultHandler constructor"
slug: "sdk-for-flutter-navigate-mapview-datasource-polygontilesourceloadresulthandler-polygontilesourceloadresulthandler"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- PolygonTileSourceLoadResultHandler.html -->


<div>
<h1>PolygonTileSourceLoadResultHandler constructor</h1></div>

PolygonTileSourceLoadResultHandler(<ol class="parameter-list single-line"> <li>void loadedLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-mapview-datasource-tilekey-class">TileKey</a>, </li>
<li>List&lt;<a href="sdk-for-flutter-navigate-mapview-datasource-polygondata-class">PolygonData</a>&gt;, </li>
<li><a href="sdk-for-flutter-navigate-mapview-datasource-tilesourcetilemetadata-class">TileSourceTileMetadata</a></li>
</ol>), </li>
<li>void failedLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-mapview-datasource-tilekey-class">TileKey</a></li>
</ol>)</li>
</ol>)
    

<p>Result handler of a load tile request.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory PolygonTileSourceLoadResultHandler(
  void Function(TileKey, List&lt;PolygonData&gt;, TileSourceTileMetadata) loadedLambda,
  void Function(TileKey) failedLambda,

) =&gt; PolygonTileSourceLoadResultHandler$Lambdas(
  loadedLambda,
  failedLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
