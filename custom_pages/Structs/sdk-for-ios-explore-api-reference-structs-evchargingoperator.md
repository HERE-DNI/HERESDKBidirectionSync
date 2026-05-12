---
title: "EVChargingOperator Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-evchargingoperator"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- EVChargingOperator.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/EVChargingOperator"></a>
<a title="EVChargingOperator Structure Reference"></a>
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
<a href="../Search.html">Search</a>
<img alt="" id="carat" src="../img/carat.png"/>
        EVChargingOperator Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct EVChargingOperator : Hashable</code></pre>
</div>
</div>
<p>Represents name and optionally other details about operator, suboperator, or e-Mobility service provider.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18EVChargingOperatorV4nameSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/name"></a>
<a class="token" href="#/s:7heresdk18EVChargingOperatorV4nameSSvp">name</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Name of the company.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var name: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18EVChargingOperatorV9partnerIDSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/partnerID"></a>
<a class="token" href="#/s:7heresdk18EVChargingOperatorV9partnerIDSSvp">partnerID</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A unique ID for the company.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var partnerID: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18EVChargingOperatorV7websiteSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/website"></a>
<a class="token" href="#/s:7heresdk18EVChargingOperatorV7websiteSSSgvp">website</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Link to the company’s website, if available.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var website: String?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18EVChargingOperatorV4logoAA9BrandLogoVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/logo"></a>
<a class="token" href="#/s:7heresdk18EVChargingOperatorV4logoAA9BrandLogoVSgvp">logo</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Image link to the company’s logo, if available.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var logo: BrandLogo?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18EVChargingOperatorV12eMobilityIDsSaySSGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/eMobilityIDs"></a>
<a class="token" href="#/s:7heresdk18EVChargingOperatorV12eMobilityIDsSaySSGvp">eMobilityIDs</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>e-Mobility IDs for the company.
This list may be empty where map coverage is limited or incomplete.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var eMobilityIDs: [String]</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18EVChargingOperatorV4name9partnerID7website4logo12eMobilityIDsACSS_S2SSgAA9BrandLogoVSgSaySSGtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(name:partnerID:website:logo:eMobilityIDs:)"></a>
<a class="token" href="#/s:7heresdk18EVChargingOperatorV4name9partnerID7website4logo12eMobilityIDsACSS_S2SSgAA9BrandLogoVSgSaySSGtcfc">init(name:<wbr/>partnerID:<wbr/>website:<wbr/>logo:<wbr/>eMobilityIDs:<wbr/>)</a>
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
<pre><code>public init(name: String = "", partnerID: String = "", website: String? = nil, logo: BrandLogo? = nil, eMobilityIDs: [String] = [])</code></pre>
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
