---
title: "start abstract method"
slug: "sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceserver-start"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- start.html -->


<div>
<h1>start abstract method</h1></div>

void
start(<ol class="parameter-list"> <li>String url, </li>
<li><a href="/sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a> engine, </li>
<li><a href="/sdk-for-flutter-navigate-maploader-remote-connection-sslservercredentialsoptions-class">SslServerCredentialsOptions</a>? serviceCredential, </li>
<li><a href="/sdk-for-flutter-navigate-maploader-remote-connection-serverstartedcallback">ServerStartedCallback</a> callback, </li>
</ol>)

      

    

<p>Exposes map data source as GRPC service on given url for <a href="/sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a>.</p>
<p>The exposed service can be consumed with the help of <a href="/sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceclient-configureremoteconnectionasync">ExternalMapDataSourceClient.configureRemoteConnectionAsync</a>.
It is a non-blocking function, and the result will be returned via a callback. <a href="/sdk-for-flutter-navigate-maploader-remote-connection-serverstartedcallback">ServerStartedCallback</a>.</p>
<p>Note: This is a beta release of this feature,
so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<ul>
<li>
<p><code>url</code> URL in the 'ip_address:port' format. Address will be used to bind to the GRPC server.</p>
</li>
<li>
<p><code>engine</code> Instance of an existing <a href="/sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a>.</p>
</li>
<li>
<p><code>serviceCredential</code> Instance of <a href="/sdk-for-flutter-navigate-maploader-remote-connection-sslservercredentialsoptions-class">SslServerCredentialsOptions</a></p>
</li>
<li>
<p><code>callback</code> Callback to retrieve an operation status on the main thread.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void start(String url, SDKNativeEngine engine, SslServerCredentialsOptions? serviceCredential, ServerStartedCallback callback);</code></pre>

 



</div>
`
}</HTMLBlock>
