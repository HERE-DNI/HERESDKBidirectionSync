---
title: "TollCost"
slug: "sdk-for-ios-navigate-api-reference-structs-tollcost"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TollCost"></a>
<a title="TollCost Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-mapdata">MapData</a>

        TollCost Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>TollCost</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TollCost</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Contains informations about the toll costs for a specific vehicle profile.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8TollCostV8currencySSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/currency"></a>
<a class="token" href="#/s:7heresdk8TollCostV8currencySSvp">currency</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The currency in which the toll is to be paid in ISO 4217 format, e.g. “USD”.</p>
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
<a name="/s:7heresdk8TollCostV5priceSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/price"></a>
<a class="token" href="#/s:7heresdk8TollCostV5priceSdvp">price</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The amount of currency to be paid for the toll.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">price</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8TollCostV14paymentMethodsSayAA13PaymentMethodOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/paymentMethods"></a>
<a class="token" href="#/s:7heresdk8TollCostV14paymentMethodsSayAA13PaymentMethodOGvp">paymentMethods</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of accepted payment methods like cash and credit card.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">paymentMethods</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-paymentmethod">PaymentMethod</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8TollCostV29isPriceCalculatedPerKilometerSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isPriceCalculatedPerKilometer"></a>
<a class="token" href="#/s:7heresdk8TollCostV29isPriceCalculatedPerKilometerSbvp">isPriceCalculatedPerKilometer</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates if the toll cost is based on the distance traveled. Defaults
to <code>false</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isPriceCalculatedPerKilometer</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8TollCostV15vehicleProfilesSayAA14VehicleProfileVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/vehicleProfiles"></a>
<a class="token" href="#/s:7heresdk8TollCostV15vehicleProfilesSayAA14VehicleProfileVGvp">vehicleProfiles</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of vehicle profile containing vehicle characteristics for which the toll cost applies.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the TollCost.transport_specifications instead.")</span>
<span class="kd">public</span> <span class="k">var</span> <span class="nv">vehicleProfiles</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-vehicleprofile">VehicleProfile</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8TollCostV23transportSpecificationsSayAA22TransportSpecificationVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/transportSpecifications"></a>
<a class="token" href="#/s:7heresdk8TollCostV23transportSpecificationsSayAA22TransportSpecificationVGvp">transportSpecifications</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of transport specifications containing the vehicle characteristics for which the toll
cost applies.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">transportSpecifications</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-transportspecification">TransportSpecification</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8TollCostV8currency5price14paymentMethods29isPriceCalculatedPerKilometer23transportSpecificationsACSS_SdSayAA13PaymentMethodOGSbSayAA22TransportSpecificationVGtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(currency:price:paymentMethods:isPriceCalculatedPerKilometer:transportSpecifications:)"></a>
<a class="token" href="#/s:7heresdk8TollCostV8currency5price14paymentMethods29isPriceCalculatedPerKilometer23transportSpecificationsACSS_SdSayAA13PaymentMethodOGSbSayAA22TransportSpecificationVGtcfc">init(currency:<wbr/>price:<wbr/>paymentMethods:<wbr/>isPriceCalculatedPerKilometer:<wbr/>transportSpecifications:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">currency</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">price</span><span class="p">:</span> <span class="kt">Double</span> <span class="o">=</span> <span class="mf">0.0</span><span class="p">,</span> <span class="nv">paymentMethods</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-paymentmethod">PaymentMethod</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">isPriceCalculatedPerKilometer</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">transportSpecifications</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-transportspecification">TransportSpecification</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[])</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8TollCostV8currency5price14paymentMethods29isPriceCalculatedPerKilometer15vehicleProfiles23transportSpecificationsACSS_SdSayAA13PaymentMethodOGSbSayAA14VehicleProfileVGSayAA22TransportSpecificationVGtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(currency:price:paymentMethods:isPriceCalculatedPerKilometer:vehicleProfiles:transportSpecifications:)"></a>
<a class="token" href="#/s:7heresdk8TollCostV8currency5price14paymentMethods29isPriceCalculatedPerKilometer15vehicleProfiles23transportSpecificationsACSS_SdSayAA13PaymentMethodOGSbSayAA14VehicleProfileVGSayAA22TransportSpecificationVGtcfc">init(currency:<wbr/>price:<wbr/>paymentMethods:<wbr/>isPriceCalculatedPerKilometer:<wbr/>vehicleProfiles:<wbr/>transportSpecifications:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated)</span>
<span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">currency</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">price</span><span class="p">:</span> <span class="kt">Double</span> <span class="o">=</span> <span class="mf">0.0</span><span class="p">,</span> <span class="nv">paymentMethods</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-paymentmethod">PaymentMethod</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">isPriceCalculatedPerKilometer</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">vehicleProfiles</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-vehicleprofile">VehicleProfile</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">transportSpecifications</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-transportspecification">TransportSpecification</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[])</span></code></pre>
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
