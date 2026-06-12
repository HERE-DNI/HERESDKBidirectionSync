---
title: "PrefetchStatusListener constructor"
slug: "sdk-for-flutter-navigate-prefetcher-prefetchstatuslistener-prefetchstatuslistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- PrefetchStatusListener.html -->


<div>
<h1>PrefetchStatusListener constructor</h1></div>

PrefetchStatusListener(<ol class="parameter-list single-line"> <li>void onProgressLambda(<ol class="parameter-list single-line"> <li>int</li>
</ol>), </li>
<li>void onCompleteLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a>?</li>
</ol>)</li>
</ol>)
    

<p>Abstract class to get notified on status updates
when prefetching map data.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory PrefetchStatusListener(
  void Function(int) onProgressLambda,
  void Function(MapLoaderError?) onCompleteLambda,

) =&gt; PrefetchStatusListener$Lambdas(
  onProgressLambda,
  onCompleteLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
