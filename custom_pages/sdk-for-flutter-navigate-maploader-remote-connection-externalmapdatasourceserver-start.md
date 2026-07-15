---
title: "start method - ExternalMapDataSourceServer class - maploader.remote.connection library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceserver-start"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader.remote.connection/ExternalMapDataSourceServer-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">start</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">start</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-start-param-url" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">url</span>, </span>
2.  <span id="sdk-for-flutter-navigate-start-param-engine" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a></span> <span class="parameter-name">engine</span>, </span>
3.  <span id="sdk-for-flutter-navigate-start-param-serviceCredential" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-remote-connection-sslservercredentialsoptions-class">SslServerCredentialsOptions</a>?</span> <span class="parameter-name">serviceCredential</span>, </span>
4.  <span id="sdk-for-flutter-navigate-start-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-remote-connection-serverstartedcallback">ServerStartedCallback</a></span> <span class="parameter-name">callback</span>, </span>

)

</div>

<div class="section desc markdown">

Exposes map data source as GRPC service on given url for <a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a>.

The exposed service can be consumed with the help of <a href="sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceclient-configureremoteconnectionasync">ExternalMapDataSourceClient.configureRemoteConnectionAsync</a>. It is a non-blocking function, and the result will be returned via a callback. <a href="sdk-for-flutter-navigate-maploader-remote-connection-serverstartedcallback">ServerStartedCallback</a>.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

- `url` URL in the 'ip_address:port' format. Address will be used to bind to the GRPC server.

- `engine` Instance of an existing <a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a>.

- `serviceCredential` Instance of <a href="sdk-for-flutter-navigate-maploader-remote-connection-sslservercredentialsoptions-class">SslServerCredentialsOptions</a>

- `callback` Callback to retrieve an operation status on the main thread.

</div>

## Implementation

``` dart
void start(String url, SDKNativeEngine engine, SslServerCredentialsOptions? serviceCredential, ServerStartedCallback callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

