---
title: "com.here.sdk.maploader.remote.connection (API Reference)"
slug: "sdk-for-android-navigate-navigate-com-here-sdk-maploader-remote-connection-package-summary"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- package-summary.html -->
<!DOCTYPE HTML>

<html lang="en">

<body class="package-declaration-page">


<div class="flex-box">
<header class="flex-header" role="banner">
<nav role="navigation">
<!-- ========= START OF TOP NAVBAR ======= -->
<div class="top-nav" id="navbar-top">
<div class="skip-nav"><a href="#skip-navbar-top" title="Skip navigation links">Skip navigation links</a></div>
<ul class="nav-list" id="navbar-top-firstrow" title="Navigation">
<li><a href="sdk-for-android-navigate-index">Overview</a></li>
<li class="nav-bar-cell1-rev">Package</li>
<li>Class</li>
<li><a href="sdk-for-android-navigate-package-tree">Tree</a></li>
<li><a href="sdk-for-android-navigate-deprecated-list">Deprecated</a></li>
<li><a href="sdk-for-android-navigate-index-all">Index</a></li>
<li><a href="sdk-for-android-navigate-help-doc#package">Help</a></li>
</ul>
</div>
<div class="sub-nav">
<div>
<ul class="sub-nav-list">
<li>Package: </li>
<li>Description | </li>
<li>Related Packages | </li>
<li><a href="#class-summary">Classes and Interfaces</a></li>
</ul>
</div>

</div>
<!-- ========= END OF TOP NAVBAR ========= -->
<span class="skip-nav" id="skip-navbar-top"></span></nav>
</header>
<div class="flex-content">
<main role="main">
<div class="header">

</div>
<hr/>
<div class="package-signature">package <span class="element-name">com.here.sdk.maploader.remote.connection</span></div>
<section class="summary">
<ul class="summary-list">
<li>
<div id="class-summary">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="class-summary.tabpanel" aria-selected="true" class="active-table-tab" id="class-summary-tab0" onclick="show('class-summary', 'class-summary', 2)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Classes and Interfaces</button><button aria-controls="class-summary.tabpanel" aria-selected="false" class="table-tab" id="class-summary-tab1" onclick="show('class-summary', 'class-summary-tab1', 2)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Interfaces</button><button aria-controls="class-summary.tabpanel" aria-selected="false" class="table-tab" id="class-summary-tab2" onclick="show('class-summary', 'class-summary-tab2', 2)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Classes</button><button aria-controls="class-summary.tabpanel" aria-selected="false" class="table-tab" id="class-summary-tab3" onclick="show('class-summary', 'class-summary-tab3', 2)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Enum Classes</button><button aria-controls="class-summary.tabpanel" aria-selected="false" class="table-tab" id="class-summary-tab5" onclick="show('class-summary', 'class-summary-tab5', 2)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Exceptions</button></div>
<div aria-labelledby="class-summary-tab0" id="class-summary.tabpanel" role="tabpanel">
<div class="summary-table two-column-summary">
<div class="table-header col-first">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color class-summary class-summary-tab3"><a href="sdk-for-android-navigate-clientcertificaterequesttype" title="enum class in com.here.sdk.maploader.remote.connection">ClientCertificateRequestType</a></div>
<div class="col-last even-row-color class-summary class-summary-tab3">
<div class="block">Controls the client certificate verification policy on the server.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab1"><a href="sdk-for-android-navigate-configureconnectioncallback" title="interface in com.here.sdk.maploader.remote.connection">ConfigureConnectionCallback</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab1">
<div class="block">This method will be called on the main thread when <a href="sdk-for-android-navigate-externalmapdatasourceclient#configureRemoteConnectionAsync(java.lang.String,com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.maploader.remote.connection.SslClientCredentialsOptions,com.here.sdk.maploader.remote.connection.ConfigureConnectionCallback)"><code>ExternalMapDataSourceClient.configureRemoteConnectionAsync(java.lang.String, com.here.sdk.core.engine.SDKNativeEngine, com.here.sdk.maploader.remote.connection.SslClientCredentialsOptions, com.here.sdk.maploader.remote.connection.ConfigureConnectionCallback)</code></a>
 has been completed.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-navigate-externalmapdatasourceclient" title="class in com.here.sdk.maploader.remote.connection">ExternalMapDataSourceClient</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block"><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab3"><a href="sdk-for-android-navigate-externalmapdatasourceerrorcode" title="enum class in com.here.sdk.maploader.remote.connection">ExternalMapDataSourceErrorCode</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab3">
<div class="block">Describes the reason for failing to configure <a href="sdk-for-android-navigate-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a> with external map data source.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab5"><a href="sdk-for-android-navigate-externalmapdatasourceexception" title="class in com.here.sdk.maploader.remote.connection">ExternalMapDataSourceException</a></div>
<div class="col-last even-row-color class-summary class-summary-tab5">
<div class="block"><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-navigate-externalmapdatasourceserver" title="class in com.here.sdk.maploader.remote.connection">ExternalMapDataSourceServer</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block"><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-navigate-pemkeycertpair" title="class in com.here.sdk.maploader.remote.connection">PemKeyCertPair</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">The structure below exactly match the corresponding gRPC PemKeyCertPair structure.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab1"><a href="sdk-for-android-navigate-serverstartedcallback" title="interface in com.here.sdk.maploader.remote.connection">ServerStartedCallback</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab1">
<div class="block">This method will be called on the main thread when <a href="sdk-for-android-navigate-externalmapdatasourceserver#start(java.lang.String,com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.maploader.remote.connection.SslServerCredentialsOptions,com.here.sdk.maploader.remote.connection.ServerStartedCallback)"><code>ExternalMapDataSourceServer.start(java.lang.String, com.here.sdk.core.engine.SDKNativeEngine, com.here.sdk.maploader.remote.connection.SslServerCredentialsOptions, com.here.sdk.maploader.remote.connection.ServerStartedCallback)</code></a>
 has been completed.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-navigate-sslclientcredentialsoptions" title="class in com.here.sdk.maploader.remote.connection">SslClientCredentialsOptions</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">The structure below exactly match the corresponding gRPC SslCredentialsOptions structure.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-navigate-sslservercredentialsoptions" title="class in com.here.sdk.maploader.remote.connection">SslServerCredentialsOptions</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">The structure below exactly match the corresponding gRPC SslServerCredentialsOptions structure.</div>
</div>
</div>
</div>
</div>
</li>
</ul>
</section>
</main>
</div>
</div>
</body>
</html>

</div>
`
}</HTMLBlock>
