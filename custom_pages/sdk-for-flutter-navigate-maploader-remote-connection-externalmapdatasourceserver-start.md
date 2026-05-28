---
title: "start abstract method"
slug: "sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceserver-start"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- start.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-maploader-remote-connection-maploader-remote-connection-library</li>
<li>/sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceserver-class</li>
<li class="self-crumb">start abstract method</li>
</ol>
<div class="self-name">start</div>
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
<div class="main-content" data-above-sidebar="maploader.remote.connection/ExternalMapDataSourceServer-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>start abstract method</h1></div>
<section class="multi-line-signature">
void
start(<wbr/><ol class="parameter-list"> <li>String url, </li>
<li>/sdk-for-flutter-navigate-core-engine-sdknativeengine-class engine, </li>
<li>/sdk-for-flutter-navigate-maploader-remote-connection-sslservercredentialsoptions-class? serviceCredential, </li>
<li>/sdk-for-flutter-navigate-maploader-remote-connection-serverstartedcallback callback, </li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Exposes map data source as GRPC service on given url for /sdk-for-flutter-navigate-core-engine-sdknativeengine-class.</p>
<p>The exposed service can be consumed with the help of /sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceclient-configureremoteconnectionasync.
It is a non-blocking function, and the result will be returned via a callback. /sdk-for-flutter-navigate-maploader-remote-connection-serverstartedcallback.</p>
<p>Note: This is a beta release of this feature,
so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<ul>
<li>
<p><code>url</code> URL in the 'ip_address:port' format. Address will be used to bind to the GRPC server.</p>
</li>
<li>
<p><code>engine</code> Instance of an existing /sdk-for-flutter-navigate-core-engine-sdknativeengine-class.</p>
</li>
<li>
<p><code>serviceCredential</code> Instance of /sdk-for-flutter-navigate-maploader-remote-connection-sslservercredentialsoptions-class</p>
</li>
<li>
<p><code>callback</code> Callback to retrieve an operation status on the main thread.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void start(String url, SDKNativeEngine engine, SslServerCredentialsOptions? serviceCredential, ServerStartedCallback callback);</code></pre>
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
<li>/sdk-for-flutter-navigate-maploader-remote-connection-externalmapdatasourceserver-class</li>
<li class="self-crumb">start abstract method</li>
</ol>
<h5>ExternalMapDataSourceServer class</h5>
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
