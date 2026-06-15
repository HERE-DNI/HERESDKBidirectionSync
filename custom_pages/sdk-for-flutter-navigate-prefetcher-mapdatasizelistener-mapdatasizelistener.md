---
title: "MapDataSizeListener constructor"
slug: "sdk-for-flutter-navigate-prefetcher-mapdatasizelistener-mapdatasizelistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapDataSizeListener.html -->


<div>
<h1>MapDataSizeListener constructor</h1></div>

MapDataSizeListener(<ol class="parameter-list single-line"> <li>void onSizeEstimatedLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a>?, </li>
<li><a href="sdk-for-flutter-navigate-prefetcher-mapdatasize-class">MapDataSize</a>?</li>
</ol>)</li>
</ol>)
    

<p>Abstract class to get the result of map data size
estimation.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory MapDataSizeListener(
  void Function(MapLoaderError?, MapDataSize?) onSizeEstimatedLambda,

) =&gt; MapDataSizeListener$Lambdas(
  onSizeEstimatedLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
