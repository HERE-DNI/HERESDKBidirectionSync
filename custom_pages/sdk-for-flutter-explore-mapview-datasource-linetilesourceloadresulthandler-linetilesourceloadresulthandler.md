---
title: "LineTileSourceLoadResultHandler constructor"
slug: "sdk-for-flutter-explore-mapview-datasource-linetilesourceloadresulthandler-linetilesourceloadresulthandler"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LineTileSourceLoadResultHandler.html -->


<div>
<h1>LineTileSourceLoadResultHandler constructor</h1></div>

LineTileSourceLoadResultHandler(<ol class="parameter-list single-line"> <li>void loadedLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-explore-mapview-datasource-tilekey-class">TileKey</a>, </li>
<li>List&lt;<a href="/sdk-for-flutter-explore-mapview-datasource-linedata-class">LineData</a>&gt;, </li>
<li><a href="/sdk-for-flutter-explore-mapview-datasource-tilesourcetilemetadata-class">TileSourceTileMetadata</a></li>
</ol>), </li>
<li>void failedLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-explore-mapview-datasource-tilekey-class">TileKey</a></li>
</ol>)</li>
</ol>)
    

<p>Result handler of a load tile request.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory LineTileSourceLoadResultHandler(
  void Function(TileKey, List&lt;LineData&gt;, TileSourceTileMetadata) loadedLambda,
  void Function(TileKey) failedLambda,

) =&gt; LineTileSourceLoadResultHandler$Lambdas(
  loadedLambda,
  failedLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
