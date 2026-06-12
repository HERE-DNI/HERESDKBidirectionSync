---
title: "OfflineSearchIndexListener constructor"
slug: "sdk-for-flutter-navigate-search-offlinesearchindexlistener-offlinesearchindexlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- OfflineSearchIndexListener.html -->


<div>
<h1>OfflineSearchIndexListener constructor</h1></div>

OfflineSearchIndexListener(<ol class="parameter-list single-line"> <li>void onStartedLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-search-offlinesearchindexoperation">OfflineSearchIndexOperation</a></li>
</ol>), </li>
<li>void onProgressLambda(<ol class="parameter-list single-line"> <li>int</li>
</ol>), </li>
<li>void onCompleteLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-search-offlinesearchindexerror">OfflineSearchIndexError</a>?</li>
</ol>)</li>
</ol>)
    

<p>Abstract class to get updates about progress
of creating persistent map index.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory OfflineSearchIndexListener(
  void Function(OfflineSearchIndexOperation) onStartedLambda,
  void Function(int) onProgressLambda,
  void Function(OfflineSearchIndexError?) onCompleteLambda,

) =&gt; OfflineSearchIndexListener$Lambdas(
  onStartedLambda,
  onProgressLambda,
  onCompleteLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
