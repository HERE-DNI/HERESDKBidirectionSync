---
title: "configureRemoteConnectionAsync abstract method"
slug: "sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceclient-configureremoteconnectionasync"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- configureRemoteConnectionAsync.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-maploader-remote-connection-maploader-remote-connection-library</li>
<li>/sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceclient-class</li>
<li class="self-crumb">configureRemoteConnectionAsync abstract method</li>
</ol>
<div class="self-name">configureRemoteConnectionAsync</div>
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
<div class="main-content" data-above-sidebar="maploader.remote.connection/ExternalMapDataSourceClient-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>configureRemoteConnectionAsync abstract method</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-core-threading-taskhandle-class
configureRemoteConnectionAsync(<wbr/><ol class="parameter-list"> <li>String url, </li>
<li>/sdk-for-flutter-navigate-core-engine-sdknativeengine-class engine, </li>
<li>/sdk-for-flutter-navigate-maploader-remote-connection-sslclientcredentialsoptions-class? credentials, </li>
<li>/sdk-for-flutter-navigate-maploader-remote-connection-configureconnectioncallback callback, </li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Initialize /sdk-for-flutter-navigate-core-engine-sdknativeengine-class with URL of the remote map data source gRPC server.</p>
<p>Newly injected map data source replaces exiting one if /sdk-for-flutter-navigate-core-engine-sdknativeengine-class was already connected.
Suggested configuration is taken from /sdk-for-flutter-navigate-core-engine-sdkoptions-catalogconfigurations, actual catalog
versions are queried from the remote connection in order to be in sync.
It is a non-blocking function, and the result will be returned via a callback /sdk-for-flutter-navigate-maploader-remote-connection-configureconnectioncallback.</p>
<ul>
<li>
<p><code>url</code> URL to connect with the remote map data source gRPC server.
The remote map data source gRPC server could be self managed service created with help OCM Access Manager (OCM AM) or
service exposed using /sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceserver-start</p>
</li>
<li>
<p><code>engine</code> Instance of an existing /sdk-for-flutter-navigate-core-engine-sdknativeengine-class.</p>
</li>
<li>
<p><code>credentials</code> Instance of /sdk-for-flutter-navigate-maploader-remote-connection-sslclientcredentialsoptions-class</p>
</li>
<li>
<p><code>callback</code> Callback to retrieve an operation status on the main thread.</p>
</li>
</ul>
<p>Returns /sdk-for-flutter-navigate-core-threading-taskhandle-class. Handle that will be used to manipulate the execution of the task, for example, to cancel on ongoing request.</p>
<p>NOTE: Cancelation functionality has not implemented yet!</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle configureRemoteConnectionAsync(String url, SDKNativeEngine engine, SslClientCredentialsOptions? credentials, ConfigureConnectionCallback callback);</code></pre>
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
<li>/sdk-for-flutter-navigate-maploader-remote-connection-maploader-remote-connection-library</li>
<li>/sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceclient-class</li>
<li class="self-crumb">configureRemoteConnectionAsync abstract method</li>
</ol>
<h5>ExternalMapDataSourceClient class</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
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
