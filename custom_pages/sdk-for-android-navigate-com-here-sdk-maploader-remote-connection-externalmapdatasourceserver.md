---
title: "ExternalMapDataSourceServer (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-externalmapdatasourceserver"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- ExternalMapDataSourceServer.html -->






<div class="flex-box">

<div class="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.maploader.remote.connection</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.maploader.remote.connection.ExternalMapDataSourceServer</div>
</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">ExternalMapDataSourceServer</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-externalmapdatasourceserver#%3Cinit%3E()">ExternalMapDataSourceServer</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance of this class.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-externalmapdatasourceserver#start(java.lang.String,com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.maploader.remote.connection.SslServerCredentialsOptions,com.here.sdk.maploader.remote.connection.ServerStartedCallback)">start</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> url,
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> engine,
 <a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-sslservercredentialsoptions" title="class in com.here.sdk.maploader.remote.connection">SslServerCredentialsOptions</a> serviceCredential,
 <a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-serverstartedcallback" title="interface in com.here.sdk.maploader.remote.connection">ServerStartedCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Exposes map data source as GRPC service on given url for <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-externalmapdatasourceserver#stop()">stop</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Stops the exposed map data source GRPC service started using <a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-externalmapdatasourceserver#start(java.lang.String,com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.maploader.remote.connection.SslServerCredentialsOptions,com.here.sdk.maploader.remote.connection.ServerStartedCallback)"><code>start(java.lang.String, com.here.sdk.core.engine.SDKNativeEngine, com.here.sdk.maploader.remote.connection.SslServerCredentialsOptions, com.here.sdk.maploader.remote.connection.ServerStartedCallback)</code></a>.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>ExternalMapDataSourceServer</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ExternalMapDataSourceServer</span>()
                            throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block"><p>Creates a new instance of this class.</p></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="start(java.lang.String,com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.maploader.remote.connection.SslServerCredentialsOptions,com.here.sdk.maploader.remote.connection.ServerStartedCallback)">
<h3>start</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">start</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> url,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> engine,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-sslservercredentialsoptions" title="class in com.here.sdk.maploader.remote.connection">SslServerCredentialsOptions</a> serviceCredential,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-serverstartedcallback" title="interface in com.here.sdk.maploader.remote.connection">ServerStartedCallback</a> callback)</span></div>
<div class="block"><p>Exposes map data source as GRPC service on given url for <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a>.
 The exposed service can be consumed with the help of <a href="sdk-for-android-navigate-externalmapdatasourceclient#configureRemoteConnectionAsync(java.lang.String,com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.maploader.remote.connection.SslClientCredentialsOptions,com.here.sdk.maploader.remote.connection.ConfigureConnectionCallback)"><code>ExternalMapDataSourceClient.configureRemoteConnectionAsync(java.lang.String, com.here.sdk.core.engine.SDKNativeEngine, com.here.sdk.maploader.remote.connection.SslClientCredentialsOptions, com.here.sdk.maploader.remote.connection.ConfigureConnectionCallback)</code></a>.
 It is a non-blocking function, and the result will be returned via a callback. <a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-serverstartedcallback" title="interface in com.here.sdk.maploader.remote.connection"><code>ServerStartedCallback</code></a>.
 Note: This is a beta release of this feature,
 so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>url</code> - <p>URL in the 'ip_address:port' format. Address will be used to bind to the GRPC server.</p></dd>
<dd><code>engine</code> - <p>Instance of an existing <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a>.</p></dd>
<dd><code>serviceCredential</code> - <p>Instance of <a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-sslservercredentialsoptions" title="class in com.here.sdk.maploader.remote.connection"><code>SslServerCredentialsOptions</code></a></p></dd>
<dd><code>callback</code> - <p>Callback to retrieve an operation status on the main thread.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="stop()">
<h3>stop</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">stop</span>()
          throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-externalmapdatasourceexception" title="class in com.here.sdk.maploader.remote.connection">ExternalMapDataSourceException</a></span></div>
<div class="block"><p>Stops the exposed map data source GRPC service started using <a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-externalmapdatasourceserver#start(java.lang.String,com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.maploader.remote.connection.SslServerCredentialsOptions,com.here.sdk.maploader.remote.connection.ServerStartedCallback)"><code>start(java.lang.String, com.here.sdk.core.engine.SDKNativeEngine, com.here.sdk.maploader.remote.connection.SslServerCredentialsOptions, com.here.sdk.maploader.remote.connection.ServerStartedCallback)</code></a>.
 Note: This is a beta release of this feature,
 so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-externalmapdatasourceexception" title="class in com.here.sdk.maploader.remote.connection">ExternalMapDataSourceException</a></code> - <p>Indicates what went wrong when trying to stop exposed external map data source service.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->

</div>
</div>



</div>
`
}</HTMLBlock>
