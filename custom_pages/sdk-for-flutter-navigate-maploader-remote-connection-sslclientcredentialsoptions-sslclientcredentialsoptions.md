---
title: "SslClientCredentialsOptions constructor"
slug: "sdk-for-flutter-navigate-maploader-remote-connection-sslclientcredentialsoptions-sslclientcredentialsoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SslClientCredentialsOptions.html -->


<div>
<h1>SslClientCredentialsOptions constructor</h1></div>

SslClientCredentialsOptions(<ol class="parameter-list single-line"> <li>String pemRootCerts, </li>
<li>String pemPrivateKey, </li>
<li>String pemCertChain</li>
</ol>)
    

<p>Creates a new instance.</p>
<ul>
<li><code>pemRootCerts</code> The PEM-encoded root certificates used to verify the server.</li>
<li><code>pemPrivateKey</code> The client's private key in PEM format.
It must be non-empty for mutual TLS. Else must be set to empty string.</li>
<li><code>pemCertChain</code> The client's certificate chain in PEM format.
It must be non-empty for mutual TLS. Else must be set to empty string.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">SslClientCredentialsOptions(this.pemRootCerts, this.pemPrivateKey, this.pemCertChain);</code></pre>

 



</div>
`
}</HTMLBlock>
