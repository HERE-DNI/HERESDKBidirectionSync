---
title: "ExternalMapDataSourceServer (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-externalmapdatasourceserver"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-package-summary">com.here.sdk.maploader.remote.connection</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.maploader.remote.connection.ExternalMapDataSourceServer → com.here.NativeBase com.here.sdk.maploader.remote.connection.ExternalMapDataSourceServer → com.here.sdk.maploader.remote.connection.ExternalMapDataSourceServer

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">ExternalMapDataSourceServer</span> <span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span>

</div>

<div class="block">

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

</div>

- <div id="sdk-for-android-navigate-constructor-summary" class="section constructor-summary">

  <div class="caption">

  Constructors

  </div>

  <div class="summary-table two-column-summary">

  <div class="table-header col-first">

  Constructor

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-constructor-name even-row-color">

      ExternalMapDataSourceServer ()

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance of this class.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-navigate-method-summary" class="section method-summary">

  <div id="sdk-for-android-navigate-method-summary-table">

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Method

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      start ( String url, SDKNativeEngine engine, SslServerCredentialsOptions serviceCredential, ServerStartedCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Exposes map data source as GRPC service on given url for SDKNativeEngine .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      stop ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Stops the exposed map data source GRPC service started using start(java.lang.String, com.here.sdk.core.engine.SDKNativeEngine, com.here.sdk.maploader.remote.connection.SslServerCredentialsOptions, com.here.sdk.maploader.remote.connection.ServerStartedCallback) .

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init" class="section detail">

    ### ExternalMapDataSourceServer

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">ExternalMapDataSourceServer</span>() throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span>

    </div>

    <div class="block">

    Creates a new instance of this class.

    </div>

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">`InstantiationErrorException`</a> -

    Indicates what went wrong when the instantiation was attempted.

    </div>

  </div>

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-start-java-lang-String-com-here-sdk-core-engine-SDKNativeEngine-com-here-sdk-maploader-remote-connection-SslServerCredentialsOptions-com-here-sdk-maploader-remote-connection-ServerStartedCallback" class="section detail">

    ### start

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">start</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> url, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> engine, @Nullable <a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-sslservercredentialsoptions" title="class in com.here.sdk.maploader.remote.connection">SslServerCredentialsOptions</a> serviceCredential, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-serverstartedcallback" title="interface in com.here.sdk.maploader.remote.connection">ServerStartedCallback</a> callback)</span>

    </div>

    <div class="block">

    Exposes map data source as GRPC service on given url for SDKNativeEngine . The exposed service can be consumed with the help of ExternalMapDataSourceClient.configureRemoteConnectionAsync(java.lang.String, com.here.sdk.core.engine.SDKNativeEngine, com.here.sdk.maploader.remote.connection.SslClientCredentialsOptions, com.here.sdk.maploader.remote.connection.ConfigureConnectionCallback) . It is a non-blocking function, and the result will be returned via a callback. ServerStartedCallback . Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

    </div>

    Parameters:  
    `url` -

    URL in the 'ip_address:port' format. Address will be used to bind to the GRPC server.

    `engine` -

    Instance of an existing <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">`SDKNativeEngine`</a>.

    `serviceCredential` -

    Instance of <a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-sslservercredentialsoptions" title="class in com.here.sdk.maploader.remote.connection">`SslServerCredentialsOptions`</a>

    `callback` -

    Callback to retrieve an operation status on the main thread.

    </div>

  - <div id="sdk-for-android-navigate-stop" class="section detail">

    ### stop

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">stop</span>() throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-externalmapdatasourceexception" title="class in com.here.sdk.maploader.remote.connection">ExternalMapDataSourceException</a></span>

    </div>

    <div class="block">

    Stops the exposed map data source GRPC service started using start(java.lang.String, com.here.sdk.core.engine.SDKNativeEngine, com.here.sdk.maploader.remote.connection.SslServerCredentialsOptions, com.here.sdk.maploader.remote.connection.ServerStartedCallback) . Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

    </div>

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-externalmapdatasourceexception" title="class in com.here.sdk.maploader.remote.connection">`ExternalMapDataSourceException`</a> -

    Indicates what went wrong when trying to stop exposed external map data source service.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

