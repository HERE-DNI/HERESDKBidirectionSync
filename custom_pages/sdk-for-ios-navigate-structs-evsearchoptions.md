---
title: "EVSearchOptions"
slug: "sdk-for-ios-navigate-structs-evsearchoptions"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/EVSearchOptions"></a>
<a title="EVSearchOptions Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-index">heresdk</a>

<a href="sdk-for-ios-navigate-search">Search</a>

        EVSearchOptions Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>EVSearchOptions</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EVSearchOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Encapsulates additional options that control the behavior of <code><a href="sdk-for-ios-navigate-classes-evsearchengine">EVSearchEngine</a></code>.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15EVSearchOptionsV18additionalFeaturesSayAA25EVChargingLocationFeatureOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/additionalFeatures"></a>
<a class="token" href="#/s:7heresdk15EVSearchOptionsV18additionalFeaturesSayAA25EVChargingLocationFeatureOGvp">additionalFeatures</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of additional optional features to be returned in <code><a href="sdk-for-ios-navigate-classes-evcharginglocation">EVChargingLocation</a></code>.
If empty, only minimal set of the required features will be returned.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">additionalFeatures</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-enums-evcharginglocationfeature">EVChargingLocationFeature</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15EVSearchOptionsV16requestedTariffsSayAA23EVChargingTariffRequestVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/requestedTariffs"></a>
<a class="token" href="#/s:7heresdk15EVSearchOptionsV16requestedTariffsSayAA23EVChargingTariffRequestVGvp">requestedTariffs</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of tariff search options.
This parameter is effective only if the <code><a href="../Structs/EVSearchOptions.html#/s:7heresdk15EVSearchOptionsV18additionalFeaturesSayAA25EVChargingLocationFeatureOGvp">EVSearchOptions.additionalFeatures</a></code> contains <code><a href="../Enums/EVChargingLocationFeature.html#/s:7heresdk25EVChargingLocationFeatureO7tariffsyA2CmF">EVChargingLocationFeature.tariffs</a></code>.
If empty, the response contains only ad-hoc tariffs, if available.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">requestedTariffs</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-structs-evchargingtariffrequest">EVChargingTariffRequest</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15EVSearchOptionsV18additionalFeatures16requestedTariffsACSayAA25EVChargingLocationFeatureOG_SayAA0H13TariffRequestVGtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(additionalFeatures:requestedTariffs:)"></a>
<a class="token" href="#/s:7heresdk15EVSearchOptionsV18additionalFeatures16requestedTariffsACSayAA25EVChargingLocationFeatureOG_SayAA0H13TariffRequestVGtcfc">init(additionalFeatures:<wbr/>requestedTariffs:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates an EVSearchOptions object.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">additionalFeatures</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-enums-evcharginglocationfeature">EVChargingLocationFeature</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">requestedTariffs</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-structs-evchargingtariffrequest">EVChargingTariffRequest</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[])</span></code></pre>
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
