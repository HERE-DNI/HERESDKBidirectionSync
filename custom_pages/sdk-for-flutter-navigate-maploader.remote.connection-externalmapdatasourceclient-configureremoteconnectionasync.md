---
title: "configureRemoteConnectionAsync method - ExternalMapDataSourceClient class - maploader.remote.connection library - Dart API"
slug: "sdk-for-flutter-navigate-maploader.remote.connection-externalmapdatasourceclient-configureremoteconnectionasync"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- configureRemoteConnectionAsync.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader.remote.connection/ExternalMapDataSourceClient-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">configureRemoteConnectionAsync</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> <span class="name">configureRemoteConnectionAsync</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-configureRemoteConnectionAsync-param-url" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">url</span>, </span>
2.  <span id="sdk-for-flutter-navigate-configureRemoteConnectionAsync-param-engine" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a></span> <span class="parameter-name">engine</span>, </span>
3.  <span id="sdk-for-flutter-navigate-configureRemoteConnectionAsync-param-credentials" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-remote-connection-sslclientcredentialsoptions-class">SslClientCredentialsOptions</a>?</span> <span class="parameter-name">credentials</span>, </span>
4.  <span id="sdk-for-flutter-navigate-configureRemoteConnectionAsync-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-remote-connection-configureconnectioncallback">ConfigureConnectionCallback</a></span> <span class="parameter-name">callback</span>, </span>

)

</div>

<div class="section desc markdown">

Initialize <a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a> with URL of the remote map data source gRPC server.

Newly injected map data source replaces exiting one if <a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a> was already connected. Suggested configuration is taken from <a href="sdk-for-flutter-navigate-core-engine-sdkoptions-catalogconfigurations">SDKOptions.catalogConfigurations</a>, actual catalog versions are queried from the remote connection in order to be in sync. It is a non-blocking function, and the result will be returned via a callback <a href="sdk-for-flutter-navigate-maploader-remote-connection-configureconnectioncallback">ConfigureConnectionCallback</a>.

- `url` URL to connect with the remote map data source gRPC server. The remote map data source gRPC server could be self managed service created with help OCM Access Manager (OCM AM) or service exposed using <a href="sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceserver-start">ExternalMapDataSourceServer.start</a>

- `engine` Instance of an existing <a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a>.

- `credentials` Instance of <a href="sdk-for-flutter-navigate-maploader-remote-connection-sslclientcredentialsoptions-class">SslClientCredentialsOptions</a>

- `callback` Callback to retrieve an operation status on the main thread.

Returns <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task, for example, to cancel on ongoing request.

NOTE: Cancelation functionality has not implemented yet!

</div>

## Implementation

``` dart
TaskHandle configureRemoteConnectionAsync(String url, SDKNativeEngine engine, SslClientCredentialsOptions? credentials, ConfigureConnectionCallback callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
