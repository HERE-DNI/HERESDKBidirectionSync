---
title: "FarePrice"
slug: "sdk-for-ios-explore-api-reference-structs-fareprice"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/FarePrice"></a>
<a title="FarePrice Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>

<a href="sdk-for-ios-explore-api-reference-routing">Routing</a>

        FarePrice Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>FarePrice</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">FarePrice</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">type</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-farepricetype">FarePriceType</a></span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">estimated</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">currency</span><span class="p">:</span> <span class="kt">String</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">minimum</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">maximum</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
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
<p><strong>Note:</strong> When the ticket validity period starts depends on the <code><a href="sdk-for-ios-explore-api-reference-structs-agency">Agency</a></code> providing the service.
Defaults to <code>nil</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">validityPeriod</span><span class="p">:</span> <span class="kt">TimeInterval</span><span class="p">?</span></code></pre>
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
<p><strong>Note:</strong> When the ticket validity period starts depends on the <code><a href="sdk-for-ios-explore-api-reference-structs-agency">Agency</a></code> providing the service.
  Defaults to <code>nil</code>.</p></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">type</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-farepricetype">FarePriceType</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-farepricetype">FarePriceType</a></span><span class="o">.</span><span class="n">value</span><span class="p">,</span> <span class="nv">estimated</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">currency</span><span class="p">:</span> <span class="kt">String</span> <span class="o">=</span> <span class="s">"EUR"</span><span class="p">,</span> <span class="nv">minimum</span><span class="p">:</span> <span class="kt">Double</span> <span class="o">=</span> <span class="mf">0.0</span><span class="p">,</span> <span class="nv">maximum</span><span class="p">:</span> <span class="kt">Double</span> <span class="o">=</span> <span class="mf">0.0</span><span class="p">,</span> <span class="nv">validityPeriod</span><span class="p">:</span> <span class="kt">TimeInterval</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
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
