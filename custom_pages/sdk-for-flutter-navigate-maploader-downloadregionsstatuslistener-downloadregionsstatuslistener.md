---
title: "DownloadRegionsStatusListener constructor"
slug: "sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-downloadregionsstatuslistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- DownloadRegionsStatusListener.html -->


<div>
<h1>DownloadRegionsStatusListener constructor</h1></div>

DownloadRegionsStatusListener(<ol class="parameter-list"> <li>void onDownloadRegionsCompleteLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a>?, </li>
<li>List&lt;<a href="sdk-for-flutter-navigate-maploader-regionid-class">RegionId</a>&gt;?</li>
</ol>), </li>
<li>void onProgressLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-maploader-regionid-class">RegionId</a>, </li>
<li>int</li>
</ol>), </li>
<li>void onPauseLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a>?</li>
</ol>), </li>
<li>void onResumeLambda(), </li>
</ol>)
    

<p>Abstract class to get notified on
status updates when downloading map regions.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory DownloadRegionsStatusListener(
  void Function(MapLoaderError?, List&lt;RegionId&gt;?) onDownloadRegionsCompleteLambda,
  void Function(RegionId, int) onProgressLambda,
  void Function(MapLoaderError?) onPauseLambda,
  void Function() onResumeLambda,

) =&gt; DownloadRegionsStatusListener$Lambdas(
  onDownloadRegionsCompleteLambda,
  onProgressLambda,
  onPauseLambda,
  onResumeLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
