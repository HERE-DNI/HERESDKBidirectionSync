---
title: "ServerStartedCallback typedef"
slug: "sdk-for-flutter-navigate-maploader-remote-connection-serverstartedcallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ServerStartedCallback.html -->


<div>
<h1>ServerStartedCallback typedef</h1></div>

ServerStartedCallback =
     void Function(<a href="/sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceerrorcode">ExternalMapDataSourceErrorCode</a>? errorCode)


<p>This method will be called on the main thread when <a href="/sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceserver-start">ExternalMapDataSourceServer.start</a>
has been completed.</p>
<ul>
<li><code>errorCode</code> Represents the operation status. It is 'null' for an operation that succeeds.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">typedef ServerStartedCallback = void Function(ExternalMapDataSourceErrorCode? errorCode);</code></pre>

 



</div>
`
}</HTMLBlock>
