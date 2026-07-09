---
title: "ExternalMapDataSourceServer (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-externalmapdatasourceserver"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- ExternalMapDataSourceServer.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.maploader.remote.connection</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.maploader.remote.connection.ExternalMapDataSourceServer</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">ExternalMapDataSourceServer</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-externalmapdatasourceserver#%3Cinit%3E()">ExternalMapDataSourceServer</a>()</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance of this class.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;()">
<h3>ExternalMapDataSourceServer</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">ExternalMapDataSourceServer</span>()
                            throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div className="block"><p>Creates a new instance of this class.</p></div>
<dl className="notes">
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
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="start(java.lang.String,com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.maploader.remote.connection.SslServerCredentialsOptions,com.here.sdk.maploader.remote.connection.ServerStartedCallback)">
<h3>start</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">start</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> url,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> engine,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-sslservercredentialsoptions" title="class in com.here.sdk.maploader.remote.connection">SslServerCredentialsOptions</a> serviceCredential,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-serverstartedcallback" title="interface in com.here.sdk.maploader.remote.connection">ServerStartedCallback</a> callback)</span></div>
<div className="block"><p>Exposes map data source as GRPC service on given url for <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a>.
 The exposed service can be consumed with the help of <a href="sdk-for-android-navigate-externalmapdatasourceclient#configureRemoteConnectionAsync(java.lang.String,com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.maploader.remote.connection.SslClientCredentialsOptions,com.here.sdk.maploader.remote.connection.ConfigureConnectionCallback)"><code>ExternalMapDataSourceClient.configureRemoteConnectionAsync(java.lang.String, com.here.sdk.core.engine.SDKNativeEngine, com.here.sdk.maploader.remote.connection.SslClientCredentialsOptions, com.here.sdk.maploader.remote.connection.ConfigureConnectionCallback)</code></a>.
 It is a non-blocking function, and the result will be returned via a callback. <a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-serverstartedcallback" title="interface in com.here.sdk.maploader.remote.connection"><code>ServerStartedCallback</code></a>.
 Note: This is a beta release of this feature,
 so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>url</code> - <p>URL in the 'ip_address:port' format. Address will be used to bind to the GRPC server.</p></dd>
<dd><code>engine</code> - <p>Instance of an existing <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a>.</p></dd>
<dd><code>serviceCredential</code> - <p>Instance of <a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-sslservercredentialsoptions" title="class in com.here.sdk.maploader.remote.connection"><code>SslServerCredentialsOptions</code></a></p></dd>
<dd><code>callback</code> - <p>Callback to retrieve an operation status on the main thread.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="stop()">
<h3>stop</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">stop</span>()
          throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-externalmapdatasourceexception" title="class in com.here.sdk.maploader.remote.connection">ExternalMapDataSourceException</a></span></div>
<div className="block"><p>Stops the exposed map data source GRPC service started using <a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-externalmapdatasourceserver#start(java.lang.String,com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.maploader.remote.connection.SslServerCredentialsOptions,com.here.sdk.maploader.remote.connection.ServerStartedCallback)"><code>start(java.lang.String, com.here.sdk.core.engine.SDKNativeEngine, com.here.sdk.maploader.remote.connection.SslServerCredentialsOptions, com.here.sdk.maploader.remote.connection.ServerStartedCallback)</code></a>.
 Note: This is a beta release of this feature,
 so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
<dl className="notes">
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
