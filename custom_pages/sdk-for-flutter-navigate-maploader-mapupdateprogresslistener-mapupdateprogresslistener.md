---
title: "MapUpdateProgressListener constructor"
slug: "sdk-for-flutter-navigate-maploader-mapupdateprogresslistener-mapupdateprogresslistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapUpdateProgressListener.html -->


<div>
<h1>MapUpdateProgressListener constructor</h1></div>

MapUpdateProgressListener(<ol class="parameter-list"> <li>void onProgressLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-maploader-regionid-class">RegionId</a>, </li>
<li>int</li>
</ol>), </li>
<li>void onPauseLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a>?</li>
</ol>), </li>
<li>void onCompleteLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a>?</li>
</ol>), </li>
<li>void onResumeLambda(), </li>
</ol>)
    

<p>Abstract class to get notified on status updates
when updating map data, previously downloaded by <a href="/sdk-for-flutter-navigate-maploader-mapdownloader-class">MapDownloader</a>.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory MapUpdateProgressListener(
  void Function(RegionId, int) onProgressLambda,
  void Function(MapLoaderError?) onPauseLambda,
  void Function(MapLoaderError?) onCompleteLambda,
  void Function() onResumeLambda,

) =&gt; MapUpdateProgressListener$Lambdas(
  onProgressLambda,
  onPauseLambda,
  onCompleteLambda,
  onResumeLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
