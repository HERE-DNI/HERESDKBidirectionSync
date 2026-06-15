---
title: "PointTileSourceLoadResultHandler constructor"
slug: "sdk-for-flutter-navigate-mapview-datasource-pointtilesourceloadresulthandler-pointtilesourceloadresulthandler"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- PointTileSourceLoadResultHandler.html -->


<div>
<h1>PointTileSourceLoadResultHandler constructor</h1></div>

PointTileSourceLoadResultHandler(<ol class="parameter-list single-line"> <li>void loadedLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-mapview-datasource-tilekey-class">TileKey</a>, </li>
<li>List&lt;<a href="sdk-for-flutter-navigate-mapview-datasource-pointdata-class">PointData</a>&gt;, </li>
<li><a href="sdk-for-flutter-navigate-mapview-datasource-tilesourcetilemetadata-class">TileSourceTileMetadata</a></li>
</ol>), </li>
<li>void failedLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-mapview-datasource-tilekey-class">TileKey</a></li>
</ol>)</li>
</ol>)
    

<p>Result handler of a load tile request.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory PointTileSourceLoadResultHandler(
  void Function(TileKey, List&lt;PointData&gt;, TileSourceTileMetadata) loadedLambda,
  void Function(TileKey) failedLambda,

) =&gt; PointTileSourceLoadResultHandler$Lambdas(
  loadedLambda,
  failedLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
