---
title: "ExternalMapDataSourceClient (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-externalmapdatasourceclient"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-package-summary">com.here.sdk.maploader.remote.connection</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.maploader.remote.connection.ExternalMapDataSourceClient → com.here.NativeBase com.here.sdk.maploader.remote.connection.ExternalMapDataSourceClient → com.here.sdk.maploader.remote.connection.ExternalMapDataSourceClient

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">ExternalMapDataSourceClient</span> <span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span>

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

      ExternalMapDataSourceClient ()

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

  <a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">`TaskHandle`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      configureRemoteConnectionAsync ( String url, SDKNativeEngine engine, SslClientCredentialsOptions credentials, ConfigureConnectionCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Initialize SDKNativeEngine with URL of the remote map data source gRPC server.

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

    ### ExternalMapDataSourceClient

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">ExternalMapDataSourceClient</span>() throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span>

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

  - <div id="sdk-for-android-navigate-configureRemoteConnectionAsync-java-lang-String-com-here-sdk-core-engine-SDKNativeEngine-com-here-sdk-maploader-remote-connection-SslClientCredentialsOptions-com-here-sdk-maploader-remote-connection-ConfigureConnectionCallback" class="section detail">

    ### configureRemoteConnectionAsync

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">configureRemoteConnectionAsync</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> url, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> engine, @Nullable <a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-sslclientcredentialsoptions" title="class in com.here.sdk.maploader.remote.connection">SslClientCredentialsOptions</a> credentials, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-configureconnectioncallback" title="interface in com.here.sdk.maploader.remote.connection">ConfigureConnectionCallback</a> callback)</span>

    </div>

    <div class="block">

    Initialize SDKNativeEngine with URL of the remote map data source gRPC server. Newly injected map data source replaces exiting one if SDKNativeEngine was already connected. Suggested configuration is taken from SDKOptions.catalogConfigurations , actual catalog versions are queried from the remote connection in order to be in sync. It is a non-blocking function, and the result will be returned via a callback ConfigureConnectionCallback .

    </div>

    Parameters:  
    `url` -

    URL to connect with the remote map data source gRPC server. The remote map data source gRPC server could be self managed service created with help OCM Access Manager (OCM AM) or service exposed using [](sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-externalmapdatasourceserver#start(java.lang.String,com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.maploader.remote.connection.SslServerCredentialsOptions,com.here.sdk.maploader.remote.connection.ServerStartedCallback))

        ExternalMapDataSourceServer.start(java.lang.String, com.here.sdk.core.engine.SDKNativeEngine, com.here.sdk.maploader.remote.connection.SslServerCredentialsOptions, com.here.sdk.maploader.remote.connection.ServerStartedCallback)

    </a>

    </p>

    `engine` -

    Instance of an existing <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">`SDKNativeEngine`</a>.

    `credentials` -

    Instance of <a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-sslclientcredentialsoptions" title="class in com.here.sdk.maploader.remote.connection">`SslClientCredentialsOptions`</a>

    `callback` -

    Callback to retrieve an operation status on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task, for example, to cancel on ongoing request. NOTE: Cancelation functionality has not implemented yet!

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

