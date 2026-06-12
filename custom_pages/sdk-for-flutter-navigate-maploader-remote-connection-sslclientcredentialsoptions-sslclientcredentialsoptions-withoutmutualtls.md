---
title: "SslClientCredentialsOptions.withoutMutualTLS constructor"
slug: "sdk-for-flutter-navigate-maploader-remote-connection-sslclientcredentialsoptions-sslclientcredentialsoptions-withoutmutualtls"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SslClientCredentialsOptions.withoutMutualTLS.html -->


<div>
<h1>SslClientCredentialsOptions.withoutMutualTLS constructor</h1></div>

SslClientCredentialsOptions.withoutMutualTLS(<ol class="parameter-list single-line"> <li>String pemRootCerts</li>
</ol>)
    

<p>The constructor which creates a new instance and sets both <code>pem_private_key</code> and
<code>pem_cert_chain</code> to empty strings.</p>
<ul>
<li><code>pemRootCerts</code> The PEM-encoded root certificates used to verify the server.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">SslClientCredentialsOptions.withoutMutualTLS(this.pemRootCerts)
    : pemPrivateKey = "", pemCertChain = "";</code></pre>

 



</div>
`
}</HTMLBlock>
