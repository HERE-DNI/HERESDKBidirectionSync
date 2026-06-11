---
title: "sdk-for-ios-navigate-api-reference-structs-sslservercredentialsoptions"
slug: "sdk-for-ios-navigate-api-reference-structs-sslservercredentialsoptions"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/SslServerCredentialsOptions"></a>
<a title="SslServerCredentialsOptions Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-maploader">MapLoader</a>
<img alt="" id="carat" src="/carat.png"/>
        SslServerCredentialsOptions Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>SslServerCredentialsOptions</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">SslServerCredentialsOptions</span></code></pre>
</div>
</div>
<p>The structure below exactly match the corresponding gRPC SslServerCredentialsOptions structure.
Options for configuring a gRPC server with SSL/TLS credentials.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27SslServerCredentialsOptionsV12pemRootCertsSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/pemRootCerts"></a>
<a class="token" href="#/s:7heresdk27SslServerCredentialsOptionsV12pemRootCertsSSvp">pemRootCerts</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Root certificates (in PEM format) used to verify the client certificate.
Required only for mutual TLS.</p>
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
<a name="/s:7heresdk27SslServerCredentialsOptionsV15pemKeyCertPairsSayAA03PemgH4PairVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/pemKeyCertPairs"></a>
<a class="token" href="#/s:7heresdk27SslServerCredentialsOptionsV15pemKeyCertPairsSayAA03PemgH4PairVGvp">pemKeyCertPairs</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of server key/certificate pairs.
At least one pair must be provided.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">pemKeyCertPairs</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-pemkeycertpair">PemKeyCertPair</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27SslServerCredentialsOptionsV24clientCertificateRequestAA06ClientgH4TypeOvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/clientCertificateRequest"></a>
<a class="token" href="#/s:7heresdk27SslServerCredentialsOptionsV24clientCertificateRequestAA06ClientgH4TypeOvp">clientCertificateRequest</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates whether the server should request and verify the client’s certificate.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">clientCertificateRequest</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-clientcertificaterequesttype">ClientCertificateRequestType</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk27SslServerCredentialsOptionsV12pemRootCerts0F12KeyCertPairs24clientCertificateRequestACSS_SayAA03PemiJ4PairVGAA06ClientmN4TypeOtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(pemRootCerts:pemKeyCertPairs:clientCertificateRequest:)"></a>
<a class="token" href="#/s:7heresdk27SslServerCredentialsOptionsV12pemRootCerts0F12KeyCertPairs24clientCertificateRequestACSS_SayAA03PemiJ4PairVGAA06ClientmN4TypeOtcfc">init(pemRootCerts:<wbr/>pemKeyCertPairs:<wbr/>clientCertificateRequest:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">pemRootCerts</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">pemKeyCertPairs</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-pemkeycertpair">PemKeyCertPair</a></span><span class="p">],</span> <span class="nv">clientCertificateRequest</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-clientcertificaterequesttype">ClientCertificateRequestType</a></span><span class="p">)</span></code></pre>
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
}</HTMLBlock>
