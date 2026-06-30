---
title: "com.here.sdk.maploader.remote.connection (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-package-summary"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- package-summary.html -->






<div class="flex-box">

<div class="flex-content">

<div class="header">

</div>

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
<div class="col-first even-row-color class-summary class-summary-tab3"><a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-clientcertificaterequesttype" title="enum class in com.here.sdk.maploader.remote.connection">ClientCertificateRequestType</a></div>
<div class="col-last even-row-color class-summary class-summary-tab3">
<div class="block">Controls the client certificate verification policy on the server.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab1"><a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-configureconnectioncallback" title="interface in com.here.sdk.maploader.remote.connection">ConfigureConnectionCallback</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab1">
<div class="block">This method will be called on the main thread when <a href="sdk-for-android-navigate-externalmapdatasourceclient#configureRemoteConnectionAsync(java.lang.String,com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.maploader.remote.connection.SslClientCredentialsOptions,com.here.sdk.maploader.remote.connection.ConfigureConnectionCallback)"><code>ExternalMapDataSourceClient.configureRemoteConnectionAsync(java.lang.String, com.here.sdk.core.engine.SDKNativeEngine, com.here.sdk.maploader.remote.connection.SslClientCredentialsOptions, com.here.sdk.maploader.remote.connection.ConfigureConnectionCallback)</code></a>
 has been completed.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-externalmapdatasourceclient" title="class in com.here.sdk.maploader.remote.connection">ExternalMapDataSourceClient</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block"><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab3"><a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-externalmapdatasourceerrorcode" title="enum class in com.here.sdk.maploader.remote.connection">ExternalMapDataSourceErrorCode</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab3">
<div class="block">Describes the reason for failing to configure <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a> with external map data source.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab5"><a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-externalmapdatasourceexception" title="class in com.here.sdk.maploader.remote.connection">ExternalMapDataSourceException</a></div>
<div class="col-last even-row-color class-summary class-summary-tab5">
<div class="block"><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-externalmapdatasourceserver" title="class in com.here.sdk.maploader.remote.connection">ExternalMapDataSourceServer</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block"><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-pemkeycertpair" title="class in com.here.sdk.maploader.remote.connection">PemKeyCertPair</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">The structure below exactly match the corresponding gRPC PemKeyCertPair structure.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab1"><a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-serverstartedcallback" title="interface in com.here.sdk.maploader.remote.connection">ServerStartedCallback</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab1">
<div class="block">This method will be called on the main thread when <a href="sdk-for-android-navigate-externalmapdatasourceserver#start(java.lang.String,com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.maploader.remote.connection.SslServerCredentialsOptions,com.here.sdk.maploader.remote.connection.ServerStartedCallback)"><code>ExternalMapDataSourceServer.start(java.lang.String, com.here.sdk.core.engine.SDKNativeEngine, com.here.sdk.maploader.remote.connection.SslServerCredentialsOptions, com.here.sdk.maploader.remote.connection.ServerStartedCallback)</code></a>
 has been completed.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-sslclientcredentialsoptions" title="class in com.here.sdk.maploader.remote.connection">SslClientCredentialsOptions</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">The structure below exactly match the corresponding gRPC SslCredentialsOptions structure.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-sslservercredentialsoptions" title="class in com.here.sdk.maploader.remote.connection">SslServerCredentialsOptions</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">The structure below exactly match the corresponding gRPC SslServerCredentialsOptions structure.</div>
</div>
</div>
</div>
</div>
</li>
</ul>
</section>

</div>
</div>



</div>
`
}</HTMLBlock>
