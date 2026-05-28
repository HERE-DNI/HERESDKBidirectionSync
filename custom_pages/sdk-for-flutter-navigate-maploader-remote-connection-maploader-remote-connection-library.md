---
title: "maploader.remote.connection library"
slug: "sdk-for-flutter-navigate-maploader-remote-connection-maploader-remote-connection-library"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- maploader.remote.connection-library.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="maploader.remote.connection/maploader.remote.connection-library.html#classes">Classes</a></li>
<li><a href="maploader.remote.connection/ExternalMapDataSourceClient-class.html">ExternalMapDataSourceClient</a></li>
<li><a href="maploader.remote.connection/ExternalMapDataSourceServer-class.html">ExternalMapDataSourceServer</a></li>
<li><a href="maploader.remote.connection/PemKeyCertPair-class.html">PemKeyCertPair</a></li>
<li><a href="maploader.remote.connection/SslClientCredentialsOptions-class.html">SslClientCredentialsOptions</a></li>
<li><a href="maploader.remote.connection/SslServerCredentialsOptions-class.html">SslServerCredentialsOptions</a></li>
<li class="section-title"><a href="maploader.remote.connection/maploader.remote.connection-library.html#enums">Enums</a></li>
<li><a href="maploader.remote.connection/ClientCertificateRequestType.html">ClientCertificateRequestType</a></li>
<li><a href="maploader.remote.connection/ExternalMapDataSourceErrorCode.html">ExternalMapDataSourceErrorCode</a></li>
<li class="section-title"><a href="maploader.remote.connection/maploader.remote.connection-library.html#typedefs">Typedefs</a></li>
<li><a href="maploader.remote.connection/ConfigureConnectionCallback.html">ConfigureConnectionCallback</a></li>
<li><a href="maploader.remote.connection/ServerStartedCallback.html">ServerStartedCallback</a></li>
<li class="section-title"><a href="maploader.remote.connection/maploader.remote.connection-library.html#exceptions">Exceptions</a></li>
<li><a href="maploader.remote.connection/ExternalMapDataSourceExceptionException-class.html">ExternalMapDataSourceExceptionException</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li class="self-crumb">maploader.remote.connection.dart</li>
</ol>
<div class="self-name">maploader.remote.connection</div>
<form class="search navbar-right" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-box" placeholder="Loading search..." type="text"/>
</form>
<div class="toggle" id="theme-button" title="Toggle brightness">
<label for="theme">
<input id="theme" type="checkbox" value="light-theme"/>

        dark_mode
      

        light_mode
      
</label>
</div>
</header>
<main>
<div class="main-content" data-above-sidebar="" data-below-sidebar="maploader.remote.connection/maploader.remote.connection-library-sidebar.html" id="dartdoc-main-content">
<div>
<h1>maploader.remote.connection library</h1>
</div>
<section class="summary offset-anchor" id="classes">
<h2>Classes</h2>
<dl>
<dt id="ExternalMapDataSourceClient">
/sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceclient-class
</dt>
<dd>
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
</dd>
<dt id="ExternalMapDataSourceServer">
/sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceserver-class
</dt>
<dd>
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
</dd>
<dt id="PemKeyCertPair">
/sdk-for-flutter-navigate-maploader-remote-connection-pemkeycertpair-class
</dt>
<dd>
  The structure below exactly match the corresponding gRPC PemKeyCertPair structure.
</dd>
<dt id="SslClientCredentialsOptions">
/sdk-for-flutter-navigate-maploader-remote-connection-sslclientcredentialsoptions-class
</dt>
<dd>
  The structure below exactly match the corresponding gRPC SslCredentialsOptions structure.
</dd>
<dt id="SslServerCredentialsOptions">
/sdk-for-flutter-navigate-maploader-remote-connection-sslservercredentialsoptions-class
</dt>
<dd>
  The structure below exactly match the corresponding gRPC SslServerCredentialsOptions structure.
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="enums">
<h2>Enums</h2>
<dl>
<dt id="ClientCertificateRequestType">
/sdk-for-flutter-navigate-maploader-remote-connection-clientcertificaterequesttype
</dt>
<dd>
  Controls the client certificate verification policy on the server.
</dd>
<dt id="ExternalMapDataSourceErrorCode">
/sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceerrorcode
</dt>
<dd>
  Describes the reason for failing to configure /sdk-for-flutter-navigate-core-engine-sdknativeengine-class with external map data source.
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="typedefs">
<h2>Typedefs</h2>
<dl>
<dt class="callable" id="ConfigureConnectionCallback">
/sdk-for-flutter-navigate-maploader-remote-connection-configureconnectioncallback
= void Function(/sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceerrorcode? errorCode)

</dt>
<dd>
    This method will be called on the main thread when /sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceclient-configureremoteconnectionasync
has been completed.
    

  </dd>
<dt class="callable" id="ServerStartedCallback">
/sdk-for-flutter-navigate-maploader-remote-connection-serverstartedcallback
= void Function(/sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceerrorcode? errorCode)

</dt>
<dd>
    This method will be called on the main thread when /sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceserver-start
has been completed.
    

  </dd>
</dl>
</section>
<section class="summary offset-anchor" id="exceptions">
<h2>Exceptions / Errors</h2>
<dl>
<dt id="ExternalMapDataSourceExceptionException">
/sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceexceptionexception-class
</dt>
<dd>
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
</dd>
</dl>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-navigate</li>
<li class="self-crumb">maploader.remote.connection.dart</li>
</ol>
<h5>here_sdk package</h5>
<ol>
<li class="section-title">Libraries</li>
<li>/sdk-for-flutter-navigate-animation-animation-library</li>
<li>/sdk-for-flutter-navigate-core-core-library</li>
<li>/sdk-for-flutter-navigate-core-engine-core-engine-library</li>
<li>/sdk-for-flutter-navigate-core-errors-core-errors-library</li>
<li>/sdk-for-flutter-navigate-core-threading-core-threading-library</li>
<li>/sdk-for-flutter-navigate-electronic-horizon-electronic-horizon-library</li>
<li>/sdk-for-flutter-navigate-ev-ev-library</li>
<li>/sdk-for-flutter-navigate-gestures-gestures-library</li>
<li>/sdk-for-flutter-navigate-location-location-library</li>
<li>/sdk-for-flutter-navigate-mapdata-mapdata-library</li>
<li>/sdk-for-flutter-navigate-maploader-maploader-library</li>
<li>/sdk-for-flutter-navigate-maploader-remote-connection-maploader-remote-connection-library</li>
<li>/sdk-for-flutter-navigate-mapmatcher-mapmatcher-library</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-datasource-mapview-datasource-library</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-prefetcher-prefetcher-library</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li>/sdk-for-flutter-navigate-search-search-library</li>
<li>/sdk-for-flutter-navigate-traffic-traffic-library</li>
<li>/sdk-for-flutter-navigate-trafficawarenavigation-trafficawarenavigation-library</li>
<li>/sdk-for-flutter-navigate-trafficbroadcast-trafficbroadcast-library</li>
<li>/sdk-for-flutter-navigate-transport-transport-library</li>
<li>/sdk-for-flutter-navigate-venue-venue-library</li>
<li>/sdk-for-flutter-navigate-venue-control-venue-control-library</li>
<li>/sdk-for-flutter-navigate-venue-data-venue-data-library</li>
<li>/sdk-for-flutter-navigate-venue-routing-venue-routing-library</li>
<li>/sdk-for-flutter-navigate-venue-service-venue-service-library</li>
<li>/sdk-for-flutter-navigate-venue-style-venue-style-library</li>
<li>/sdk-for-flutter-navigate-warner-warner-library</li>
</ol>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
<h5>maploader.remote.connection library</h5>
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>
</div></div>
</div>
`
}</HTMLBlock>
