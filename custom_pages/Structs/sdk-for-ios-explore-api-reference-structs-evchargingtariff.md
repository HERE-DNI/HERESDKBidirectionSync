---
title: "EVChargingTariff Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-evchargingtariff"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- EVChargingTariff.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/EVChargingTariff"></a>
<a title="EVChargingTariff Structure Reference"></a>
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
        EVChargingTariff Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct EVChargingTariff : Hashable</code></pre>
</div>
</div>
<p>Tariffs provide detailed pricing information for charging electric vehicles at a specific location.
Each tariff describes how costs are calculated based on various factors such as energy consumed,
time spent charging, and session duration.
Tariffs are typically associated with specific connectors or connector groups, and are only
included in the response when relevant data is available and requested.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16EVChargingTariffV4nameSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/name"></a>
<a class="token" href="#/s:7heresdk16EVChargingTariffV4nameSSSgvp">name</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Name of the tariff. The name is not mandatory for ad-hoc tariffs, but may exist.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var name: String?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16EVChargingTariffV4typeAA0bC4TypeOvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/type"></a>
<a class="token" href="#/s:7heresdk16EVChargingTariffV4typeAA0bC4TypeOvp">type</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates the pricing model.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var type: EVChargingTariffType</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16EVChargingTariffV7partnerSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/partner"></a>
<a class="token" href="#/s:7heresdk16EVChargingTariffV7partnerSSvp">partner</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Name of the partner providing the tariff, either the charge point operator or eMSP.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var partner: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16EVChargingTariffV9partnerIDSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/partnerID"></a>
<a class="token" href="#/s:7heresdk16EVChargingTariffV9partnerIDSSvp">partnerID</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A unique ID representing the partner.
The same id is used also in other parts of the API and other related HERE APIs.</p>
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
<a name="/s:7heresdk16EVChargingTariffV8currencySSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/currency"></a>
<a class="token" href="#/s:7heresdk16EVChargingTariffV8currencySSvp">currency</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The currency in which the prices are given, represented by the ISO 4217 standard currency
code (e.g., EUR, DKK).</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var currency: String</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16EVChargingTariffV8elementsSayAA0bC7ElementVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/elements"></a>
<a class="token" href="#/s:7heresdk16EVChargingTariffV8elementsSayAA0bC7ElementVGvp">elements</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Elements composing the tariff. Each element can have multiple components. When multiple elements
are present, the associated condition helps the client to select the element that matches the
charging session. If no condition matches, the element without any condition applies.</p>
<p>Please note that tariff elements or conditions requiring access to vehicle APIs are not present in this API.
The provided elements can only be used to derive a price estimate, which in most cases is reasonably close to the final price.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var elements: [EVChargingTariffElement]</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16EVChargingTariffV4name4type7partner0F2ID8currency8elementsACSSSg_AA0bC4TypeOS3SSayAA0bC7ElementVGtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(name:type:partner:partnerID:currency:elements:)"></a>
<a class="token" href="#/s:7heresdk16EVChargingTariffV4name4type7partner0F2ID8currency8elementsACSSSg_AA0bC4TypeOS3SSayAA0bC7ElementVGtcfc">init(name:<wbr/>type:<wbr/>partner:<wbr/>partnerID:<wbr/>currency:<wbr/>elements:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance.</p>
<ul>
<li><p>Parameters</p>
<ul>
<li>name: Name of the tariff. The name is not mandatory for ad-hoc tariffs, but may exist.</li>
<li>type: Indicates the pricing model.</li>
<li>partner: Name of the partner providing the tariff, either the charge point operator or eMSP.</li>
<li>partnerID: A unique ID representing the partner.
The same id is used also in other parts of the API and other related HERE APIs.</li>
<li>currency: The currency in which the prices are given, represented by the ISO 4217 standard currency
code (e.g., EUR, DKK).</li>
<li>elements: Elements composing the tariff. Each element can have multiple components. When multiple elements
are present, the associated condition helps the client to select the element that matches the
charging session. If no condition matches, the element without any condition applies.</li>
</ul>
<p>Please note that tariff elements or conditions requiring access to vehicle APIs are not present in this API.
  The provided elements can only be used to derive a price estimate, which in most cases is reasonably close to the final price.</p></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public init(name: String? = nil, type: EVChargingTariffType = EVChargingTariffType.adHoc, partner: String = "", partnerID: String = "", currency: String = "", elements: [EVChargingTariffElement] = [])</code></pre>
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
