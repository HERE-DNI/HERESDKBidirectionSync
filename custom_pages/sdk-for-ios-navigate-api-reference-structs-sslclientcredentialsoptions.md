---
title: "SslClientCredentialsOptions"
slug: "sdk-for-ios-navigate-api-reference-structs-sslclientcredentialsoptions"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/SslClientCredentialsOptions"></a>
<a title="SslClientCredentialsOptions Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-maploader">MapLoader</a>

        SslClientCredentialsOptions Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>SslClientCredentialsOptions</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">SslClientCredentialsOptions</span></code></pre>
</div>
</div>
<p>The structure below exactly match the corresponding gRPC SslCredentialsOptions structure.
Options used to build SslCredentials.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27SslClientCredentialsOptionsV12pemRootCertsSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/pemRootCerts"></a>
<a class="token" href="#/s:7heresdk27SslClientCredentialsOptionsV12pemRootCertsSSvp">pemRootCerts</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The PEM-encoded root certificates used to verify the server.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">pemRootCerts</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27SslClientCredentialsOptionsV13pemPrivateKeySSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/pemPrivateKey"></a>
<a class="token" href="#/s:7heresdk27SslClientCredentialsOptionsV13pemPrivateKeySSvp">pemPrivateKey</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The client’s private key in PEM format.
It must be non-empty for mutual TLS. Else must be set to empty string.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">pemPrivateKey</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27SslClientCredentialsOptionsV12pemCertChainSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/pemCertChain"></a>
<a class="token" href="#/s:7heresdk27SslClientCredentialsOptionsV12pemCertChainSSvp">pemCertChain</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The client’s certificate chain in PEM format.
It must be non-empty for mutual TLS. Else must be set to empty string.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">pemCertChain</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27SslClientCredentialsOptionsV12pemRootCerts0F10PrivateKey0F9CertChainACSS_S2Stcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(pemRootCerts:pemPrivateKey:pemCertChain:)"></a>
<a class="token" href="#/s:7heresdk27SslClientCredentialsOptionsV12pemRootCerts0F10PrivateKey0F9CertChainACSS_S2Stcfc">init(pemRootCerts:<wbr/>pemPrivateKey:<wbr/>pemCertChain:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">pemRootCerts</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">pemPrivateKey</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">pemCertChain</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27SslClientCredentialsOptionsV12pemRootCertsACSS_tcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(pemRootCerts:)"></a>
<a class="token" href="#/s:7heresdk27SslClientCredentialsOptionsV12pemRootCertsACSS_tcfc">init(pemRootCerts:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The constructor which creates a new instance and sets both <code>pem_private_key</code> and
<code>pem_cert_chain</code> to empty strings.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">pemRootCerts</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span></code></pre>
</div>
</div>
</section>
</div>
</li>
</ul>
</div>
</section>
</section>
<section id="footer">
<p>© 2026 <a class="link" href="" rel="external noopener" target="_blank"></a>. All rights reserved. (Last updated: 2026-04-14)</p>
<p>Generated by <a class="link" href="https://github.com/realm/jazzy" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a class="link" href="https://realm.io" rel="external noopener" target="_blank">Realm</a> project.</p>
</section>
</article>
</div>
</body>
</html>

`
} </HTMLBlock>
