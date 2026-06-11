---
title: "sdk-for-ios-navigate-api-reference-structs-rdsencryptionkey"
slug: "sdk-for-ios-navigate-api-reference-structs-rdsencryptionkey"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/RDSEncryptionKey"></a>
<a title="RDSEncryptionKey Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-trafficradio">TrafficRadio</a>
<img alt="" id="carat" src="/carat.png"/>
        RDSEncryptionKey Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>RDSEncryptionKey</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RDSEncryptionKey</span></code></pre>
</div>
</div>
<p>Represents the RDS encryption key.
Fields allocation information is described in CEN ISO/CD 14819-6.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16RDSEncryptionKeyV12encryptionIds5UInt8Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/encryptionId"></a>
<a class="token" href="#/s:7heresdk16RDSEncryptionKeyV12encryptionIds5UInt8Vvp">encryptionId</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Id of encryption key within the list.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">encryptionId</span><span class="p">:</span> <span class="kt">UInt8</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16RDSEncryptionKeyV11rotateRights5UInt8Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/rotateRight"></a>
<a class="token" href="#/s:7heresdk16RDSEncryptionKeyV11rotateRights5UInt8Vvp">rotateRight</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Rotate Right used for bit manipulations as a part of encryption process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">rotateRight</span><span class="p">:</span> <span class="kt">UInt8</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16RDSEncryptionKeyV8startBits5UInt8Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/startBit"></a>
<a class="token" href="#/s:7heresdk16RDSEncryptionKeyV8startBits5UInt8Vvp">startBit</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Start Bit used for bit manipulations as a part of encryption process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">startBit</span><span class="p">:</span> <span class="kt">UInt8</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16RDSEncryptionKeyV8xorValues5UInt8Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/xorValue"></a>
<a class="token" href="#/s:7heresdk16RDSEncryptionKeyV8xorValues5UInt8Vvp">xorValue</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>XOR Value used for bit manipulations as a part of encryption process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">xorValue</span><span class="p">:</span> <span class="kt">UInt8</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16RDSEncryptionKeyV12encryptionId11rotateRight8startBit8xorValueACs5UInt8V_A3Itcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(encryptionId:rotateRight:startBit:xorValue:)"></a>
<a class="token" href="#/s:7heresdk16RDSEncryptionKeyV12encryptionId11rotateRight8startBit8xorValueACs5UInt8V_A3Itcfc">init(encryptionId:<wbr/>rotateRight:<wbr/>startBit:<wbr/>xorValue:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">encryptionId</span><span class="p">:</span> <span class="kt">UInt8</span><span class="p">,</span> <span class="nv">rotateRight</span><span class="p">:</span> <span class="kt">UInt8</span><span class="p">,</span> <span class="nv">startBit</span><span class="p">:</span> <span class="kt">UInt8</span><span class="p">,</span> <span class="nv">xorValue</span><span class="p">:</span> <span class="kt">UInt8</span><span class="p">)</span></code></pre>
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
