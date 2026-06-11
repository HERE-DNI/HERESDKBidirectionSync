---
title: "sdk-for-ios-explore-api-reference-structs-networkendpoint"
slug: "sdk-for-ios-explore-api-reference-structs-networkendpoint"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/NetworkEndpoint"></a>
<a title="NetworkEndpoint Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-core">Core</a>
<img alt="" id="carat" src="/carat.png"/>
        NetworkEndpoint Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>NetworkEndpoint</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">NetworkEndpoint</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Network endpoint.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15NetworkEndpointV7address0B09IPAddress_pvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/address"></a>
<a class="token" href="#/s:7heresdk15NetworkEndpointV7address0B09IPAddress_pvp">address</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The IP Address of the network endpoint.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">address</span><span class="p">:</span> <span class="kt">IPAddress</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15NetworkEndpointV4ports6UInt16VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/port"></a>
<a class="token" href="#/s:7heresdk15NetworkEndpointV4ports6UInt16VSgvp">port</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Optional port number of the network endpoint.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">port</span><span class="p">:</span> <span class="kt">UInt16</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15NetworkEndpointV7address4portAC0B09IPAddress_p_s6UInt16VSgtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(address:port:)"></a>
<a class="token" href="#/s:7heresdk15NetworkEndpointV7address4portAC0B09IPAddress_p_s6UInt16VSgtcfc">init(address:<wbr/>port:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">address</span><span class="p">:</span> <span class="kt">IPAddress</span><span class="p">,</span> <span class="nv">port</span><span class="p">:</span> <span class="kt">UInt16</span><span class="p">?)</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15NetworkEndpointV7addressAC0B09IPAddress_p_tcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(address:)"></a>
<a class="token" href="#/s:7heresdk15NetworkEndpointV7addressAC0B09IPAddress_p_tcfc">init(address:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">address</span><span class="p">:</span> <span class="kt">IPAddress</span><span class="p">)</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15NetworkEndpointV2eeoiySbAC_ACtFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/==(_:_:)"></a>
<a class="token" href="#/s:7heresdk15NetworkEndpointV2eeoiySbAC_ACtFZ">==(_:<wbr/>_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Compare objects</p>
<ul>
<li>Return true if objects are equal, false otherwise.</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">static</span> <span class="kd">func</span> <span class="o">==</span> <span class="p">(</span><span class="nv">lhs</span><span class="p">:</span> <span class="kt">NetworkEndpoint</span><span class="p">,</span> <span class="nv">rhs</span><span class="p">:</span> <span class="kt">NetworkEndpoint</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>lhs</em>
</code>
</td>
<td>
<div>
<p>First object to compare</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>rhs</em>
</code>
</td>
<td>
<div>
<p>Second object to compare</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15NetworkEndpointV4hash4intoys6HasherVz_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/hash(into:)"></a>
<a class="token" href="#/s:7heresdk15NetworkEndpointV4hash4intoys6HasherVz_tF">hash(into:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Hashes object</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">hash</span><span class="p">(</span><span class="n">into</span> <span class="nv">hasher</span><span class="p">:</span> <span class="k">inout</span> <span class="kt">Hasher</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>hasher</em>
</code>
</td>
<td>
<div>
<p>The hasher</p>
</div>
</td>
</tr>
</tbody>
</table>
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
