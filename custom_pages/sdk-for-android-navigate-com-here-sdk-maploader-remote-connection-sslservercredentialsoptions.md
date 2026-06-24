---
title: "SslServerCredentialsOptions (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-sslservercredentialsoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- SslServerCredentialsOptions.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.maploader.remote.connection.SslServerCredentialsOptions</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">SslServerCredentialsOptions</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>The structure below exactly match the corresponding gRPC SslServerCredentialsOptions structure.
 Options for configuring a gRPC server with SSL/TLS credentials.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">

<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-clientcertificaterequesttype" title="enum class in com.here.sdk.maploader.remote.connection">ClientCertificateRequestType</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-sslservercredentialsoptions#clientCertificateRequest">clientCertificateRequest</a></code></div>
<div class="col-last even-row-color">
<div class="block">Indicates whether the server should request and verify the client's certificate.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-pemkeycertpair" title="class in com.here.sdk.maploader.remote.connection">PemKeyCertPair</a>&gt;</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-sslservercredentialsoptions#pemKeyCertPairs">pemKeyCertPairs</a></code></div>
<div class="col-last odd-row-color">
<div class="block">List of server key/certificate pairs.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-sslservercredentialsoptions#pemRootCerts">pemRootCerts</a></code></div>
<div class="col-last even-row-color">
<div class="block">Root certificates (in PEM format) used to verify the client certificate.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-maploader-remote-connection-sslservercredentialsoptions#%3Cinit%3E(java.lang.String,java.util.List,com.here.sdk.maploader.remote.connection.ClientCertificateRequestType)">SslServerCredentialsOptions</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> pemRootCerts,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-pemkeycertpair" title="class in com.here.sdk.maploader.remote.connection">PemKeyCertPair</a>&gt; pemKeyCertPairs,
 <a href="sdk-for-android-navigate-clientcertificaterequesttype" title="enum class in com.here.sdk.maploader.remote.connection">ClientCertificateRequestType</a> clientCertificateRequest)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">

<ul class="member-list">
<li>
<section class="detail" id="pemRootCerts">
<h3>pemRootCerts</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">pemRootCerts</span></div>
<div class="block"><p>Root certificates (in PEM format) used to verify the client certificate.
 Required only for mutual TLS.</p></div>
</section>
</li>
<li>
<section class="detail" id="pemKeyCertPairs">
<h3>pemKeyCertPairs</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-pemkeycertpair" title="class in com.here.sdk.maploader.remote.connection">PemKeyCertPair</a>&gt;</span> <span class="element-name">pemKeyCertPairs</span></div>
<div class="block"><p>List of server key/certificate pairs.
 At least one pair must be provided.</p></div>
</section>
</li>
<li>
<section class="detail" id="clientCertificateRequest">
<h3>clientCertificateRequest</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-clientcertificaterequesttype" title="enum class in com.here.sdk.maploader.remote.connection">ClientCertificateRequestType</a></span> <span class="element-name">clientCertificateRequest</span></div>
<div class="block"><p>Indicates whether the server should request and verify the client's certificate.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,java.util.List,com.here.sdk.maploader.remote.connection.ClientCertificateRequestType)">
<h3>SslServerCredentialsOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SslServerCredentialsOptions</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> pemRootCerts,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-pemkeycertpair" title="class in com.here.sdk.maploader.remote.connection">PemKeyCertPair</a>&gt; pemKeyCertPairs,
 @NonNull
 <a href="sdk-for-android-navigate-clientcertificaterequesttype" title="enum class in com.here.sdk.maploader.remote.connection">ClientCertificateRequestType</a> clientCertificateRequest)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
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
`
}</HTMLBlock>
