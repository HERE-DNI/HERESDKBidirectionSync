---
title: "ServerStartedCallback (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-serverstartedcallback"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-package-summary">com.here.sdk.maploader.remote.connection</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

Functional Interface:  
This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

<div class="type-signature">

<span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html" class="external-link" title="class or interface in java.lang">@FunctionalInterface</a> </span><span class="modifiers">public interface </span><span class="element-name type-name-label">ServerStartedCallback</span>

</div>

<div class="block">

This method will be called on the main thread when ExternalMapDataSourceServer.start(java.lang.String, com.here.sdk.core.engine.SDKNativeEngine, com.here.sdk.maploader.remote.connection.SslServerCredentialsOptions, com.here.sdk.maploader.remote.connection.ServerStartedCallback) has been completed.

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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      onServerStarted ( ExternalMapDataSourceErrorCode errorCode)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  This method will be called on the main thread when ExternalMapDataSourceServer.start(java.lang.String, com.here.sdk.core.engine.SDKNativeEngine, com.here.sdk.maploader.remote.connection.SslServerCredentialsOptions, com.here.sdk.maploader.remote.connection.ServerStartedCallback) has been completed.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onServerStarted-com-here-sdk-maploader-remote-connection-ExternalMapDataSourceErrorCode" class="section detail">

    ### onServerStarted

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onServerStarted</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-externalmapdatasourceerrorcode" title="enum class in com.here.sdk.maploader.remote.connection">ExternalMapDataSourceErrorCode</a> errorCode)</span>

    </div>

    <div class="block">

    This method will be called on the main thread when ExternalMapDataSourceServer.start(java.lang.String, com.here.sdk.core.engine.SDKNativeEngine, com.here.sdk.maploader.remote.connection.SslServerCredentialsOptions, com.here.sdk.maploader.remote.connection.ServerStartedCallback) has been completed.

    </div>

    Parameters:  
    `errorCode` -

    Represents the operation status. It is 'null' for an operation that succeeds.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

