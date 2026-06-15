---
title: "onPause abstract method"
slug: "sdk-for-flutter-navigate-maploader-catalogupdateprogresslistener-onpause"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- onPause.html -->


<div>
<h1>onPause abstract method</h1></div>

void
onPause(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a>? error</li>
</ol>)

      

    

<p>Called when update is paused.</p>
<p>Invoked on the main thread.</p>
<ul>
<li><code>error</code> Populated when a retryable error is the reason for a pause. A retryable error can happen,
when, for example, the HERE SDK tries too often to resume a download that was paused due to a lost connection.
In general, the HERE SDK will try a few times, before the update is paused.
This error value gives a hint on the reason for the necessary retry operation.
A paused download can be resumed by the user at a later time.
It is 'null' when <code>CatalogUpdateTask.pauseWithCompaction</code> was called by the user.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void onPause(MapLoaderError? error);</code></pre>

 



</div>
`
}</HTMLBlock>
