---
title: "SDKCacheCallback typedef"
slug: "sdk-for-flutter-navigate-maploader-sdkcachecallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SDKCacheCallback.html -->


<div>
<h1>SDKCacheCallback typedef</h1></div>

SDKCacheCallback =
     void Function(<a href="/sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a>? maploaderError)


<p>A method which is called on the main thread when <a href="/sdk-for-flutter-navigate-maploader-sdkcache-clearappcache">SDKCache.clearAppCache</a> has been completed.</p>
<ul>
<li><code>maploaderError</code> Represents an error in case of a failure. It is <code>null</code> for an operation that succeeds.
Please note, in case of failure, only <a href="/sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError.internalError</a> error returned for now.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">typedef SDKCacheCallback = void Function(MapLoaderError? maploaderError);</code></pre>

 



</div>
`
}</HTMLBlock>
