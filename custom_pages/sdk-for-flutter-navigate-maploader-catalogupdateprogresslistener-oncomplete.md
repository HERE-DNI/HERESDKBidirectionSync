---
title: "onComplete abstract method"
slug: "sdk-for-flutter-navigate-maploader-catalogupdateprogresslistener-oncomplete"
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

      

    

<p>Called after the update process for all regions has been completed.</p>
<p>Invoked on the main thread.</p>
<ul>
<li><code>error</code> Represents an error in case of a failure.
If an error occurs, the operation cannot be resumed later.
It is <code>null</code> for an operation that succeeds.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void onComplete(MapLoaderError? error);</code></pre>

 



</div>
`
}</HTMLBlock>
