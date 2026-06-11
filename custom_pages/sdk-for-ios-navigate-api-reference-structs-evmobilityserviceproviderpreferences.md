---
title: "EVMobilityServiceProviderPreferences"
slug: "sdk-for-ios-navigate-api-reference-structs-evmobilityserviceproviderpreferences"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/EVMobilityServiceProviderPreferences"></a>
<a title="EVMobilityServiceProviderPreferences Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-routing">Routing</a>

        EVMobilityServiceProviderPreferences Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>EVMobilityServiceProviderPreferences</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EVMobilityServiceProviderPreferences</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Defines preference level per known E-Mobility Service Provider.
The E-Mobility Service Provider ID partner id as received from
<a href="https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-roamings.html">https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-roamings.html</a>
An alternative way to get <code>partnerId</code> is the <code>eMobilityServiceProviders.partnerId</code> as part of <code>HERE SDK Search</code>.
Maximum number of E-Mobility Service Providers is limited to 10 across all preference.
Defaults to using all available providers with no prioritization.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk36EVMobilityServiceProviderPreferencesV4highSaySSGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/high"></a>
<a class="token" href="#/s:7heresdk36EVMobilityServiceProviderPreferencesV4highSaySSGvp">high</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies the E-Mobility Service Provider partnerId that are preferred the most.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">high</span><span class="p">:</span> <span class="p">[</span><span class="kt">String</span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk36EVMobilityServiceProviderPreferencesV6mediumSaySSGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/medium"></a>
<a class="token" href="#/s:7heresdk36EVMobilityServiceProviderPreferencesV6mediumSaySSGvp">medium</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies the E-Mobility Service Provider partnerId that can be used when no better provider could be found or reached.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">medium</span><span class="p">:</span> <span class="p">[</span><span class="kt">String</span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk36EVMobilityServiceProviderPreferencesV3lowSaySSGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/low"></a>
<a class="token" href="#/s:7heresdk36EVMobilityServiceProviderPreferencesV3lowSaySSGvp">low</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies the E-Mobility Service Provider partnerId that are preferred the least.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">low</span><span class="p">:</span> <span class="p">[</span><span class="kt">String</span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk36EVMobilityServiceProviderPreferencesV4high6medium3lowACSaySSG_A2Gtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(high:medium:low:)"></a>
<a class="token" href="#/s:7heresdk36EVMobilityServiceProviderPreferencesV4high6medium3lowACSaySSG_A2Gtcfc">init(high:<wbr/>medium:<wbr/>low:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">high</span><span class="p">:</span> <span class="p">[</span><span class="kt">String</span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">medium</span><span class="p">:</span> <span class="p">[</span><span class="kt">String</span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">low</span><span class="p">:</span> <span class="p">[</span><span class="kt">String</span><span class="p">]</span> <span class="o">=</span> <span class="p">[])</span></code></pre>
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
