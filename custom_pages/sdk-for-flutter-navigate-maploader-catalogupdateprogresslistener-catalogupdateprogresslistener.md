---
title: "CatalogUpdateProgressListener constructor"
slug: "sdk-for-flutter-navigate-maploader-catalogupdateprogresslistener-catalogupdateprogresslistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- CatalogUpdateProgressListener.html -->


<div>
<h1>CatalogUpdateProgressListener constructor</h1></div>

CatalogUpdateProgressListener(<ol class="parameter-list"> <li>void onProgressLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-maploader-regionid-class">RegionId</a>, </li>
<li>int</li>
</ol>), </li>
<li>void onPauseLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a>?</li>
</ol>), </li>
<li>void onCompleteLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a>?</li>
</ol>), </li>
<li>void onResumeLambda(), </li>
</ol>)
    

<p>Abstract class to get notified on status updates
when updating catalog, previously downloaded by <a href="/sdk-for-flutter-navigate-maploader-mapdownloader-class">MapDownloader</a>.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory CatalogUpdateProgressListener(
  void Function(RegionId, int) onProgressLambda,
  void Function(MapLoaderError?) onPauseLambda,
  void Function(MapLoaderError?) onCompleteLambda,
  void Function() onResumeLambda,

) =&gt; CatalogUpdateProgressListener$Lambdas(
  onProgressLambda,
  onPauseLambda,
  onCompleteLambda,
  onResumeLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
