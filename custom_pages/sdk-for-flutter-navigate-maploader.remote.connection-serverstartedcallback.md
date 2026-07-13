---
title: "ServerStartedCallback typedef - maploader.remote.connection library - Dart API"
slug: "sdk-for-flutter-navigate-maploader.remote.connection-serverstartedcallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ServerStartedCallback.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader.remote.connection/maploader.remote.connection-library-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-typedef">ServerStartedCallback</span> typedef

</div>

<div class="section multi-line-signature">

<span class="name">ServerStartedCallback</span> = <span class="returntype">void Function<span class="signature">(<span id="sdk-for-flutter-navigate-param-errorCode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceerrorcode">ExternalMapDataSourceErrorCode</a>?</span> <span class="parameter-name">errorCode</span></span>)</span></span>

</div>

<div class="section desc markdown">

This method will be called on the main thread when <a href="sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceserver-start">ExternalMapDataSourceServer.start</a> has been completed.

- `errorCode` Represents the operation status. It is 'null' for an operation that succeeds.

</div>

## Implementation

``` dart
typedef ServerStartedCallback = void Function(ExternalMapDataSourceErrorCode? errorCode);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
