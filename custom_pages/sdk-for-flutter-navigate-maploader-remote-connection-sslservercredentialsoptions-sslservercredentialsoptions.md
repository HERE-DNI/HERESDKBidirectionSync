---
title: "SslServerCredentialsOptions constructor"
slug: "sdk-for-flutter-navigate-maploader-remote-connection-sslservercredentialsoptions-sslservercredentialsoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SslServerCredentialsOptions.html -->


<div>
<h1>SslServerCredentialsOptions constructor</h1></div>

SslServerCredentialsOptions(<ol class="parameter-list single-line"> <li>String pemRootCerts, </li>
<li>List&lt;<a href="sdk-for-flutter-navigate-maploader-remote-connection-pemkeycertpair-class">PemKeyCertPair</a>&gt; pemKeyCertPairs, </li>
<li><a href="sdk-for-flutter-navigate-maploader-remote-connection-clientcertificaterequesttype">ClientCertificateRequestType</a> clientCertificateRequest</li>
</ol>)
    

<p>Creates a new instance.</p>
<ul>
<li><code>pemRootCerts</code> Root certificates (in PEM format) used to verify the client certificate.
Required only for mutual TLS.</li>
<li><code>pemKeyCertPairs</code> List of server key/certificate pairs.
At least one pair must be provided.</li>
<li><code>clientCertificateRequest</code> Indicates whether the server should request and verify the client's certificate.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">SslServerCredentialsOptions(this.pemRootCerts, this.pemKeyCertPairs, this.clientCertificateRequest);</code></pre>

 



</div>
`
}</HTMLBlock>
