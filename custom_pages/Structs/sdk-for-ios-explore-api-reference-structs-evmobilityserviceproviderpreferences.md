---
title: "EVMobilityServiceProviderPreferences Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-evmobilityserviceproviderpreferences"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- EVMobilityServiceProviderPreferences.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/EVMobilityServiceProviderPreferences"></a>
<a title="EVMobilityServiceProviderPreferences Structure Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="../index.html">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="../index.html">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="../Routing.html">Routing</a>
<img alt="" id="carat" src="../img/carat.png"/>
        EVMobilityServiceProviderPreferences Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct EVMobilityServiceProviderPreferences : Hashable</code></pre>
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
<pre><code>public var high: [String]</code></pre>
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
<pre><code>public var medium: [String]</code></pre>
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
<pre><code>public var low: [String]</code></pre>
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
<pre><code>public init(high: [String] = [], medium: [String] = [], low: [String] = [])</code></pre>
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



</div>
`
}</HTMLBlock>
