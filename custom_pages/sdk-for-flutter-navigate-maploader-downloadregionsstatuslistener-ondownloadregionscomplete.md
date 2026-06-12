---
title: "onDownloadRegionsComplete abstract method"
slug: "sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-ondownloadregionscomplete"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- onDownloadRegionsComplete.html -->


<div>
<h1>onDownloadRegionsComplete abstract method</h1></div>

void
onDownloadRegionsComplete(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a>? error, </li>
<li>List&lt;<a href="/sdk-for-flutter-navigate-maploader-regionid-class">RegionId</a>&gt;? regions</li>
</ol>)

      

    

<p>Called after the download for all requested regions has been completed with success or
failure.</p>
<p>In this callback, failure represents non-retryable error (eg. authentication failure
because of invalid credentials and similars). Temporary failures (eg. network errors) are
notified through <a href="/sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-onpause">DownloadRegionsStatusListener.onPause</a> and downloads will be
in paused state so they can be resumed later.
Invoked on the main thread.</p>
<ul>
<li>
<p><code>error</code> Represents an error in case of a failure. It is <code>null</code> for an operation that
succeeds.</p>
</li>
<li>
<p><code>regions</code> Represents a list of regions which has been downloaded. It is <code>null</code> in case
of an error.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void onDownloadRegionsComplete(MapLoaderError? error, List&lt;RegionId&gt;? regions);</code></pre>

 



</div>
`
}</HTMLBlock>
