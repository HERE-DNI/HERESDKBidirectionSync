---
title: "maploader.remote.connection library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-remote-connection-maploader-remote-connection-library"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="" data-below-sidebar="maploader.remote.connection/maploader.remote.connection-library-sidebar.html">

<div>

# <span class="kind-library">maploader.remote.connection</span> library

</div>

## Classes

<span class="name"><a href="sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceclient-class">ExternalMapDataSourceClient</a></span>  
**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceserver-class">ExternalMapDataSourceServer</a></span>  
**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-remote-connection-pemkeycertpair-class">PemKeyCertPair</a></span>  
The structure below exactly match the corresponding gRPC PemKeyCertPair structure.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-remote-connection-sslclientcredentialsoptions-class">SslClientCredentialsOptions</a></span>  
The structure below exactly match the corresponding gRPC SslCredentialsOptions structure.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-remote-connection-sslservercredentialsoptions-class">SslServerCredentialsOptions</a></span>  
The structure below exactly match the corresponding gRPC SslServerCredentialsOptions structure.

## Enums

<span class="name"><a href="sdk-for-flutter-navigate-maploader-remote-connection-clientcertificaterequesttype">ClientCertificateRequestType</a></span>  
Controls the client certificate verification policy on the server.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceerrorcode">ExternalMapDataSourceErrorCode</a></span>  
Describes the reason for failing to configure <a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a> with external map data source.

## Typedefs

<span class="name"><a href="sdk-for-flutter-navigate-maploader-remote-connection-configureconnectioncallback">ConfigureConnectionCallback</a></span><span class="signature"> <span class="returntype parameter">= void Function<span class="signature">(<span id="sdk-for-flutter-navigate-param-errorCode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceerrorcode">ExternalMapDataSourceErrorCode</a>?</span> <span class="parameter-name">errorCode</span></span>)</span></span> </span>  
This method will be called on the main thread when <a href="sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceclient-configureremoteconnectionasync">ExternalMapDataSourceClient.configureRemoteConnectionAsync</a> has been completed.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-remote-connection-serverstartedcallback">ServerStartedCallback</a></span><span class="signature"> <span class="returntype parameter">= void Function<span class="signature">(<span id="sdk-for-flutter-navigate-param-errorCode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceerrorcode">ExternalMapDataSourceErrorCode</a>?</span> <span class="parameter-name">errorCode</span></span>)</span></span> </span>  
This method will be called on the main thread when <a href="sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceserver-start">ExternalMapDataSourceServer.start</a> has been completed.

## Exceptions / Errors

<span class="name"><a href="sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceexceptionexception-class">ExternalMapDataSourceExceptionException</a></span>  
**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.

</div>

<!-- /.main-content --> <!--/sidebar-offcanvas-right--> <span class="no-break"> here_sdk 4.26.0 </span>

