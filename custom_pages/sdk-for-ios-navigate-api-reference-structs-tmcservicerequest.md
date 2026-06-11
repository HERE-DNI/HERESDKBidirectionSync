---
title: "TMCServiceRequest"
slug: "sdk-for-ios-navigate-api-reference-structs-tmcservicerequest"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TMCServiceRequest"></a>
<a title="TMCServiceRequest Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-trafficradio">TrafficRadio</a>

        TMCServiceRequest Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>TMCServiceRequest</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TMCServiceRequest</span></code></pre>
</div>
</div>
<p>Represents the parameters used to request the traffic broadcast.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17TMCServiceRequestV11countryCodes5UInt8Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/countryCode"></a>
<a class="token" href="#/s:7heresdk17TMCServiceRequestV11countryCodes5UInt8Vvp">countryCode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Refers to a country in RDS-TMC format.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">countryCode</span><span class="p">:</span> <span class="kt">UInt8</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17TMCServiceRequestV13preferredSidsSays5UInt8VGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/preferredSids"></a>
<a class="token" href="#/s:7heresdk17TMCServiceRequestV13preferredSidsSays5UInt8VGvp">preferredSids</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of preferred SIDs (up to 8).</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">preferredSids</span><span class="p">:</span> <span class="p">[</span><span class="kt">UInt8</span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17TMCServiceRequestV13supportedLtnsSays5UInt8VGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/supportedLtns"></a>
<a class="token" href="#/s:7heresdk17TMCServiceRequestV13supportedLtnsSays5UInt8VGvp">supportedLtns</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of supported LTNs (up to 8).</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">supportedLtns</span><span class="p">:</span> <span class="p">[</span><span class="kt">UInt8</span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17TMCServiceRequestV11countryCode13preferredSids13supportedLtnsACs5UInt8V_SayAHGAItcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(countryCode:preferredSids:supportedLtns:)"></a>
<a class="token" href="#/s:7heresdk17TMCServiceRequestV11countryCode13preferredSids13supportedLtnsACs5UInt8V_SayAHGAItcfc">init(countryCode:<wbr/>preferredSids:<wbr/>supportedLtns:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">countryCode</span><span class="p">:</span> <span class="kt">UInt8</span><span class="p">,</span> <span class="nv">preferredSids</span><span class="p">:</span> <span class="p">[</span><span class="kt">UInt8</span><span class="p">],</span> <span class="nv">supportedLtns</span><span class="p">:</span> <span class="p">[</span><span class="kt">UInt8</span><span class="p">])</span></code></pre>
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
