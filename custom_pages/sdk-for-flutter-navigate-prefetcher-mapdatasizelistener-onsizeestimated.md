---
title: "onSizeEstimated abstract method"
slug: "sdk-for-flutter-navigate-prefetcher-mapdatasizelistener-onsizeestimated"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- onSizeEstimated.html -->


<div>
<h1>onSizeEstimated abstract method</h1></div>

void
onSizeEstimated(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a>? error, </li>
<li><a href="sdk-for-flutter-navigate-prefetcher-mapdatasize-class">MapDataSize</a>? dataSize</li>
</ol>)

      

    

<p>Called after map data size estimation has been completed either with success or with error.</p>
<p>Invoked on the main thread.</p>
<ul>
<li>
<p><code>error</code> Represents an error in case of a failure. If the operation was successful,
<code>null</code> is returned.</p>
</li>
<li>
<p><code>dataSize</code> Represents the map data size. In case of failure,
<code>null</code> is returned.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void onSizeEstimated(MapLoaderError? error, MapDataSize? dataSize);</code></pre>

 



</div>
`
}</HTMLBlock>
