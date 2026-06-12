---
title: "TileSourceListener constructor"
slug: "sdk-for-flutter-navigate-mapview-datasource-tilesourcelistener-tilesourcelistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TileSourceListener.html -->


<div>
<h1>TileSourceListener constructor</h1></div>

TileSourceListener(<ol class="parameter-list single-line"> <li>void onDataVersionChangedLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-mapview-datasource-tilesourcedataversion-class">TileSourceDataVersion</a></li>
</ol>)</li>
</ol>)
    

<p>Listener of <a href="/sdk-for-flutter-navigate-mapview-datasource-tilesource-class">TileSource</a> events.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory TileSourceListener(
  void Function(TileSourceDataVersion) onDataVersionChangedLambda,

) =&gt; TileSourceListener$Lambdas(
  onDataVersionChangedLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
