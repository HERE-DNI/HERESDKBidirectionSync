---
title: "SslServerCredentialsOptions (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-sslservercredentialsoptions"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-package-summary">com.here.sdk.maploader.remote.connection</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.maploader.remote.connection.SslServerCredentialsOptions → com.here.sdk.maploader.remote.connection.SslServerCredentialsOptions

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">SslServerCredentialsOptions</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

The structure below exactly match the corresponding gRPC SslServerCredentialsOptions structure. Options for configuring a gRPC server with SSL/TLS credentials.

</div>

</div>

- <div id="sdk-for-android-navigate-field-summary" class="section field-summary">

  <div class="caption">

  Fields

  </div>

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Field

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-clientcertificaterequesttype" title="enum class in com.here.sdk.maploader.remote.connection">`ClientCertificateRequestType`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-sslservercredentialsoptions#clientCertificateRequest" class="member-name-link"><code>clientCertificateRequest</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Indicates whether the server should request and verify the client's certificate.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-pemkeycertpair" title="class in com.here.sdk.maploader.remote.connection">`PemKeyCertPair`</a>`>`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-sslservercredentialsoptions#pemKeyCertPairs" class="member-name-link"><code>pemKeyCertPairs</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  List of server key/certificate pairs.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-sslservercredentialsoptions#pemRootCerts" class="member-name-link"><code>pemRootCerts</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Root certificates (in PEM format) used to verify the client certificate.

  </div>

  </div>

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

      SslServerCredentialsOptions ( String pemRootCerts, List < PemKeyCertPair > pemKeyCertPairs, ClientCertificateRequestType clientCertificateRequest)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-navigate-method-summary" class="section method-summary">

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-field-detail" class="section field-details">

  - <div id="sdk-for-android-navigate-pemRootCerts" class="section detail">

    ### pemRootCerts

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">pemRootCerts</span>

    </div>

    <div class="block">

    Root certificates (in PEM format) used to verify the client certificate. Required only for mutual TLS.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-pemKeyCertPairs" class="section detail">

    ### pemKeyCertPairs

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-pemkeycertpair" title="class in com.here.sdk.maploader.remote.connection">PemKeyCertPair</a>\></span> <span class="element-name">pemKeyCertPairs</span>

    </div>

    <div class="block">

    List of server key/certificate pairs. At least one pair must be provided.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-clientCertificateRequest" class="section detail">

    ### clientCertificateRequest

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-clientcertificaterequesttype" title="enum class in com.here.sdk.maploader.remote.connection">ClientCertificateRequestType</a></span> <span class="element-name">clientCertificateRequest</span>

    </div>

    <div class="block">

    Indicates whether the server should request and verify the client's certificate.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init-java-lang-String-java-util-List-com-here-sdk-maploader-remote-connection-ClientCertificateRequestType" class="section detail">

    ### SslServerCredentialsOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">SslServerCredentialsOptions</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> pemRootCerts, @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-pemkeycertpair" title="class in com.here.sdk.maploader.remote.connection">PemKeyCertPair</a>\> pemKeyCertPairs, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-clientcertificaterequesttype" title="enum class in com.here.sdk.maploader.remote.connection">ClientCertificateRequestType</a> clientCertificateRequest)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `pemRootCerts` -

    Root certificates (in PEM format) used to verify the client certificate. Required only for mutual TLS.

    `pemKeyCertPairs` -

    List of server key/certificate pairs. At least one pair must be provided.

    `clientCertificateRequest` -

    Indicates whether the server should request and verify the client's certificate.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

