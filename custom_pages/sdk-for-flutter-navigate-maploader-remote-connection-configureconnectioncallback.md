---
title: "ConfigureConnectionCallback typedef"
slug: "sdk-for-flutter-navigate-maploader-remote-connection-configureconnectioncallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ConfigureConnectionCallback.html -->


<div>
<h1>ConfigureConnectionCallback typedef</h1></div>

ConfigureConnectionCallback =
     void Function(<a href="sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceerrorcode">ExternalMapDataSourceErrorCode</a>? errorCode)


<p>This method will be called on the main thread when <a href="sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceclient-configureremoteconnectionasync">ExternalMapDataSourceClient.configureRemoteConnectionAsync</a>
has been completed.</p>
<ul>
<li><code>errorCode</code> Represents the operation status. It is 'null' for an operation that succeeds.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">typedef ConfigureConnectionCallback = void Function(ExternalMapDataSourceErrorCode? errorCode);</code></pre>

 



</div>
`
}</HTMLBlock>
