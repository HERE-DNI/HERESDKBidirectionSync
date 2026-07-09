---
title: "SslServerCredentialsOptions (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-sslservercredentialsoptions"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- SslServerCredentialsOptions.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.maploader.remote.connection</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.maploader.remote.connection.SslServerCredentialsOptions</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">SslServerCredentialsOptions</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>The structure below exactly match the corresponding gRPC SslServerCredentialsOptions structure.
 Options for configuring a gRPC server with SSL/TLS credentials.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-clientcertificaterequesttype" title="enum class in com.here.sdk.maploader.remote.connection">ClientCertificateRequestType</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-sslservercredentialsoptions#clientCertificateRequest">clientCertificateRequest</a></code></div>
<div className="col-last even-row-color">
<div className="block">Indicates whether the server should request and verify the client's certificate.</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-pemkeycertpair" title="class in com.here.sdk.maploader.remote.connection">PemKeyCertPair</a>&gt;</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-sslservercredentialsoptions#pemKeyCertPairs">pemKeyCertPairs</a></code></div>
<div className="col-last odd-row-color">
<div className="block">List of server key/certificate pairs.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-sslservercredentialsoptions#pemRootCerts">pemRootCerts</a></code></div>
<div className="col-last even-row-color">
<div className="block">Root certificates (in PEM format) used to verify the client certificate.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-sslservercredentialsoptions#%3Cinit%3E(java.lang.String,java.util.List,com.here.sdk.maploader.remote.connection.ClientCertificateRequestType)">SslServerCredentialsOptions</a><wbr/>(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> pemRootCerts,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-pemkeycertpair" title="class in com.here.sdk.maploader.remote.connection">PemKeyCertPair</a>&gt; pemKeyCertPairs,
 <a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-clientcertificaterequesttype" title="enum class in com.here.sdk.maploader.remote.connection">ClientCertificateRequestType</a> clientCertificateRequest)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section className="field-details" id="field-detail">

<ul className="member-list">
<li>
<section className="detail" id="pemRootCerts">
<h3>pemRootCerts</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">pemRootCerts</span></div>
<div className="block"><p>Root certificates (in PEM format) used to verify the client certificate.
 Required only for mutual TLS.</p></div>
</section>
</li>
<li>
<section className="detail" id="pemKeyCertPairs">
<h3>pemKeyCertPairs</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-pemkeycertpair" title="class in com.here.sdk.maploader.remote.connection">PemKeyCertPair</a>&gt;</span> <span className="element-name">pemKeyCertPairs</span></div>
<div className="block"><p>List of server key/certificate pairs.
 At least one pair must be provided.</p></div>
</section>
</li>
<li>
<section className="detail" id="clientCertificateRequest">
<h3>clientCertificateRequest</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-clientcertificaterequesttype" title="enum class in com.here.sdk.maploader.remote.connection">ClientCertificateRequestType</a></span> <span className="element-name">clientCertificateRequest</span></div>
<div className="block"><p>Indicates whether the server should request and verify the client's certificate.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;(java.lang.String,java.util.List,com.here.sdk.maploader.remote.connection.ClientCertificateRequestType)">
<h3>SslServerCredentialsOptions</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">SslServerCredentialsOptions</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> pemRootCerts,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-pemkeycertpair" title="class in com.here.sdk.maploader.remote.connection">PemKeyCertPair</a>&gt; pemKeyCertPairs,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-clientcertificaterequesttype" title="enum class in com.here.sdk.maploader.remote.connection">ClientCertificateRequestType</a> clientCertificateRequest)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>pemRootCerts</code> - <p>Root certificates (in PEM format) used to verify the client certificate.
 Required only for mutual TLS.</p></dd>
<dd><code>pemKeyCertPairs</code> - <p>List of server key/certificate pairs.
 At least one pair must be provided.</p></dd>
<dd><code>clientCertificateRequest</code> - <p>Indicates whether the server should request and verify the client's certificate.</p></dd>
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
