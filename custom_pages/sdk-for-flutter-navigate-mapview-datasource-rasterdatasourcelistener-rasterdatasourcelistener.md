---
title: "RasterDataSourceListener constructor"
slug: "sdk-for-flutter-navigate-mapview-datasource-rasterdatasourcelistener-rasterdatasourcelistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RasterDataSourceListener.html -->


<div>
<h1>RasterDataSourceListener constructor</h1></div>

RasterDataSourceListener(<ol class="parameter-list single-line"> <li>void onRasterDataSourceReadyLambda(), </li>
<li>void onRasterDataSourceErrorLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-mapview-datasource-rasterdatasourceerror">RasterDataSourceError</a></li>
</ol>)</li>
</ol>)
    

<p>Listener for RasterDataSource events.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory RasterDataSourceListener(
  void Function() onRasterDataSourceReadyLambda,
  void Function(RasterDataSourceError) onRasterDataSourceErrorLambda,

) =&gt; RasterDataSourceListener$Lambdas(
  onRasterDataSourceReadyLambda,
  onRasterDataSourceErrorLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
