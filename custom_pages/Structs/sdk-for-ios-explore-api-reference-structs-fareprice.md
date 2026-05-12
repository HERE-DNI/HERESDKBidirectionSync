---
title: "FarePrice Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-fareprice"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- FarePrice.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/FarePrice"></a>
<a title="FarePrice Structure Reference"></a>
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
        FarePrice Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct FarePrice : Hashable</code></pre>
</div>
</div>
<p>Price of a fare.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9FarePriceV4typeAA0bC4TypeOvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/type"></a>
<a class="token" href="#/s:7heresdk9FarePriceV4typeAA0bC4TypeOvp">type</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Type of price represented by this object.
Defaults to <code><a href="../Enums/FarePriceType.html#/s:7heresdk13FarePriceTypeO5valueyA2CmF">FarePriceType.value</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var type: FarePriceType</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9FarePriceV9estimatedSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/estimated"></a>
<a class="token" href="#/s:7heresdk9FarePriceV9estimatedSbvp">estimated</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p><code>True</code> when the fare price is estimated based on best guess and the actual price may differ.
Defaults to <code>false</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var estimated: Bool</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9FarePriceV8currencySSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/currency"></a>
<a class="token" href="#/s:7heresdk9FarePriceV8currencySSvp">currency</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Local currency of the price compliant to ISO 4217. For example, “GBP” for the British pound sterling.
Defaults to “EUR” string.</p>
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
<a name="/s:7heresdk9FarePriceV7minimumSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/minimum"></a>
<a class="token" href="#/s:7heresdk9FarePriceV7minimumSdvp">minimum</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Minimum price when the price is of <code><a href="../Enums/FarePriceType.html#/s:7heresdk13FarePriceTypeO5rangeyA2CmF">FarePriceType.range</a></code> type. Otherwise, it is
equal to <code><a href="../Structs/FarePrice.html#/s:7heresdk9FarePriceV7maximumSdvp">FarePrice.maximum</a></code>.
Defaults to 0.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var minimum: Double</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9FarePriceV7maximumSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maximum"></a>
<a class="token" href="#/s:7heresdk9FarePriceV7maximumSdvp">maximum</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Maximum price when the price is of <code><a href="../Enums/FarePriceType.html#/s:7heresdk13FarePriceTypeO5rangeyA2CmF">FarePriceType.range</a></code> type. Otherwise, it is
equal to <code><a href="../Structs/FarePrice.html#/s:7heresdk9FarePriceV7minimumSdvp">FarePrice.minimum</a></code>.
Defaults to 0.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var maximum: Double</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9FarePriceV14validityPeriodSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/validityPeriod"></a>
<a class="token" href="#/s:7heresdk9FarePriceV14validityPeriodSdSgvp">validityPeriod</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>When set, the price is paid for a specific duration.</p>
<p><strong>Examples</strong>:</p>
<p>3600 seconds - price for one hour</p>
<p>28800 seconds - price for eight hours</p>
<p>86400 seconds - price for one day</p>
<p><strong>Note:</strong> When the ticket validity period starts depends on the <code><a href="../Structs/Agency.html">Agency</a></code> providing the service.
Defaults to <code>nil</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var validityPeriod: TimeInterval?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9FarePriceV4type9estimated8currency7minimum7maximum14validityPeriodAcA0bC4TypeO_SbSSS3dSgtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(type:estimated:currency:minimum:maximum:validityPeriod:)"></a>
<a class="token" href="#/s:7heresdk9FarePriceV4type9estimated8currency7minimum7maximum14validityPeriodAcA0bC4TypeO_SbSSS3dSgtcfc">init(type:<wbr/>estimated:<wbr/>currency:<wbr/>minimum:<wbr/>maximum:<wbr/>validityPeriod:<wbr/>)</a>
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
<li>type: Type of price represented by this object.
Defaults to <code><a href="../Enums/FarePriceType.html#/s:7heresdk13FarePriceTypeO5valueyA2CmF">FarePriceType.value</a></code>.</li>
<li>estimated: <code>True</code> when the fare price is estimated based on best guess and the actual price may differ.
Defaults to <code>false</code>.</li>
<li>currency: Local currency of the price compliant to ISO 4217. For example, “GBP” for the British pound sterling.
Defaults to “EUR” string.</li>
<li>minimum: Minimum price when the price is of <code><a href="../Enums/FarePriceType.html#/s:7heresdk13FarePriceTypeO5rangeyA2CmF">FarePriceType.range</a></code> type. Otherwise, it is
equal to <code><a href="../Structs/FarePrice.html#/s:7heresdk9FarePriceV7maximumSdvp">FarePrice.maximum</a></code>.
Defaults to 0.</li>
<li>maximum: Maximum price when the price is of <code><a href="../Enums/FarePriceType.html#/s:7heresdk13FarePriceTypeO5rangeyA2CmF">FarePriceType.range</a></code> type. Otherwise, it is
equal to <code><a href="../Structs/FarePrice.html#/s:7heresdk9FarePriceV7minimumSdvp">FarePrice.minimum</a></code>.
Defaults to 0.</li>
<li>validityPeriod: When set, the price is paid for a specific duration.</li>
</ul>
<p><strong>Examples</strong>:</p>
<p>3600 seconds - price for one hour</p>
<p>28800 seconds - price for eight hours</p>
<p>86400 seconds - price for one day</p>
<p><strong>Note:</strong> When the ticket validity period starts depends on the <code><a href="../Structs/Agency.html">Agency</a></code> providing the service.
  Defaults to <code>nil</code>.</p></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public init(type: FarePriceType = FarePriceType.value, estimated: Bool = false, currency: String = "EUR", minimum: Double = 0.0, maximum: Double = 0.0, validityPeriod: TimeInterval? = nil)</code></pre>
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
