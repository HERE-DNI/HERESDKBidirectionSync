---
title: "sdk-for-ios-explore-api-reference-structs-engineoptions"
slug: "sdk-for-ios-explore-api-reference-structs-engineoptions"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/EngineOptions"></a>
<a title="EngineOptions Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-core">Core</a>
<img alt="" id="carat" src="/carat.png"/>
        EngineOptions Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>EngineOptions</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EngineOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Specifies several options specific to different engines.
Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13EngineOptionsV13customBaseUrlSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/customBaseUrl"></a>
<a class="token" href="#/s:7heresdk13EngineOptionsV13customBaseUrlSSSgvp">customBaseUrl</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Allows engines to use custom base URLs for alternative services.
By default, the available endpoints use HERE backend endpoints.
If unsupported base URLs are specified, the related features will become non-functional.
Please contact your HERE representative to learn about possible custom base URL usage options</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">customBaseUrl</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13EngineOptionsV24customAuthenticationModeAA0eF0CSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/customAuthenticationMode"></a>
<a class="token" href="#/s:7heresdk13EngineOptionsV24customAuthenticationModeAA0eF0CSgvp">customAuthenticationMode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Allows bearer authentication mode for engines. This mode adds a header
(“Authorization”, “Bearer $Token”) to each online request made by the
module the object is added to. The token can either be provided directly
or retrieved via key/secret from a dedicated backend.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">customAuthenticationMode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-authenticationmode">AuthenticationMode</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13EngineOptionsV13customBaseUrl0D18AuthenticationModeACSSSg_AA0gH0CSgtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(customBaseUrl:customAuthenticationMode:)"></a>
<a class="token" href="#/s:7heresdk13EngineOptionsV13customBaseUrl0D18AuthenticationModeACSSSg_AA0gH0CSgtcfc">init(customBaseUrl:<wbr/>customAuthenticationMode:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Undocumented</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">customBaseUrl</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">customAuthenticationMode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-authenticationmode">AuthenticationMode</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
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
