---
title: "onComplete abstract method"
slug: "sdk-for-flutter-navigate-prefetcher-prefetchstatuslistener-oncomplete"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- onComplete.html -->


<div>
<h1>onComplete abstract method</h1></div>

void
onComplete(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a>? error</li>
</ol>)

      

    

<p>Called after the geo-corridor data downloads has been completed either with success or with error.</p>
<p>Invoked on the main thread.</p>
<ul>
<li><code>error</code> Represents an error in case of a failure.
If an error occurs, to resume operation, please download geo-corridor again.
It is <code>null</code> for an operation that succeeds.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void onComplete(MapLoaderError? error);</code></pre>

 



</div>
`
}</HTMLBlock>
