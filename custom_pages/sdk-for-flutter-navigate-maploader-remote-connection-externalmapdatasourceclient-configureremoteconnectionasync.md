---
title: "configureRemoteConnectionAsync abstract method"
slug: "sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceclient-configureremoteconnectionasync"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- configureRemoteConnectionAsync.html -->


<div>
<h1>configureRemoteConnectionAsync abstract method</h1></div>

<a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>
configureRemoteConnectionAsync(<ol class="parameter-list"> <li>String url, </li>
<li><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a> engine, </li>
<li><a href="sdk-for-flutter-navigate-maploader-remote-connection-sslclientcredentialsoptions-class">SslClientCredentialsOptions</a>? credentials, </li>
<li><a href="sdk-for-flutter-navigate-maploader-remote-connection-configureconnectioncallback">ConfigureConnectionCallback</a> callback, </li>
</ol>)

      

    

<p>Initialize <a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a> with URL of the remote map data source gRPC server.</p>
<p>Newly injected map data source replaces exiting one if <a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a> was already connected.
Suggested configuration is taken from <a href="sdk-for-flutter-navigate-core-engine-sdkoptions-catalogconfigurations">SDKOptions.catalogConfigurations</a>, actual catalog
versions are queried from the remote connection in order to be in sync.
It is a non-blocking function, and the result will be returned via a callback <a href="sdk-for-flutter-navigate-maploader-remote-connection-configureconnectioncallback">ConfigureConnectionCallback</a>.</p>
<ul>
<li>
<p><code>url</code> URL to connect with the remote map data source gRPC server.
The remote map data source gRPC server could be self managed service created with help OCM Access Manager (OCM AM) or
service exposed using <a href="sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceserver-start">ExternalMapDataSourceServer.start</a></p>
</li>
<li>
<p><code>engine</code> Instance of an existing <a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a>.</p>
</li>
<li>
<p><code>credentials</code> Instance of <a href="sdk-for-flutter-navigate-maploader-remote-connection-sslclientcredentialsoptions-class">SslClientCredentialsOptions</a></p>
</li>
<li>
<p><code>callback</code> Callback to retrieve an operation status on the main thread.</p>
</li>
</ul>
<p>Returns <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task, for example, to cancel on ongoing request.</p>
<p>NOTE: Cancelation functionality has not implemented yet!</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle configureRemoteConnectionAsync(String url, SDKNativeEngine engine, SslClientCredentialsOptions? credentials, ConfigureConnectionCallback callback);</code></pre>

 



</div>
`
}</HTMLBlock>
