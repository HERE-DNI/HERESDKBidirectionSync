---
title: "cancel abstract method"
slug: "sdk-for-flutter-navigate-maploader-mapupdatetask-cancel"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- cancel.html -->


<div>
<h1>cancel abstract method</h1></div>

void
cancel()

      

    

<p>Cancels the ongoing map update operation.</p>
<p>Operation cannot be resumed afterwards.
It will do nothing if the task was already cancelled or has been completed.
Status of the call will be reported via <a href="sdk-for-flutter-navigate-maploader-mapupdateprogresslistener-oncomplete">MapUpdateProgressListener.onComplete</a>.
<a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError.operationCancelled</a> will be reported for a successful cancel operation.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void cancel();</code></pre>

 



</div>
`
}</HTMLBlock>
