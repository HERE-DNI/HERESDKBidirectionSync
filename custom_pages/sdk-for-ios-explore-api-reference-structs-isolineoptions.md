---
title: "Untitled"
slug: "sdk-for-ios-explore-api-reference-structs-isolineoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- IsolineOptions.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/IsolineOptions"></a>
<a title="IsolineOptions Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-routing">Routing</a>
<img alt="" id="carat" src="../img/carat.png"/>
        IsolineOptions Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>IsolineOptions</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">IsolineOptions</span></code></pre>
</div>
</div>
<p>Specifies options for isolines calculation.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14IsolineOptionsV011calculationC0AC11CalculationVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/calculationOptions"></a>
<a class="token" href="#/s:7heresdk14IsolineOptionsV011calculationC0AC11CalculationVvp">calculationOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies isoline parameters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">calculationOptions</span><span class="p">:</span> <span class="kt">IsolineOptions</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-isolineoptions-calculation">Calculation</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14IsolineOptionsV03carC0AA03CarC0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/carOptions"></a>
<a class="token" href="#/s:7heresdk14IsolineOptionsV03carC0AA03CarC0VSgvp">carOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies options for calculation of isolines for car.
Mutually exclusive with <code><a href="../Structs/IsolineOptions.html#/s:7heresdk14IsolineOptionsV05truckC0AA05TruckC0VSgvp">IsolineOptions.truckOptions</a></code>, <code><a href="../Structs/IsolineOptions.html#/s:7heresdk14IsolineOptionsV05evCarC0AA05EVCarC0VSgvp">IsolineOptions.evCarOptions</a></code>, <code><a href="../Structs/IsolineOptions.html#/s:7heresdk14IsolineOptionsV07evTruckC0AA07EVTruckC0VSgvp">IsolineOptions.evTruckOptions</a></code> and <code><a href="../Structs/IsolineOptions.html#/s:7heresdk14IsolineOptionsV07routingC0AA07RoutingC0VSgvp">IsolineOptions.routingOptions</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the <code>routing_options</code> instead.")</span>
<span class="kd">public</span> <span class="k">var</span> <span class="nv">carOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-caroptions">CarOptions</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14IsolineOptionsV05truckC0AA05TruckC0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/truckOptions"></a>
<a class="token" href="#/s:7heresdk14IsolineOptionsV05truckC0AA05TruckC0VSgvp">truckOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies options for calculation of isolines for truck.
Mutually exclusive with <code><a href="../Structs/IsolineOptions.html#/s:7heresdk14IsolineOptionsV03carC0AA03CarC0VSgvp">IsolineOptions.carOptions</a></code>, <code><a href="../Structs/IsolineOptions.html#/s:7heresdk14IsolineOptionsV05evCarC0AA05EVCarC0VSgvp">IsolineOptions.evCarOptions</a></code>, <code><a href="../Structs/IsolineOptions.html#/s:7heresdk14IsolineOptionsV07evTruckC0AA07EVTruckC0VSgvp">IsolineOptions.evTruckOptions</a></code> and <code><a href="../Structs/IsolineOptions.html#/s:7heresdk14IsolineOptionsV07routingC0AA07RoutingC0VSgvp">IsolineOptions.routingOptions</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the <code>routing_options</code> instead.")</span>
<span class="kd">public</span> <span class="k">var</span> <span class="nv">truckOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-truckoptions">TruckOptions</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14IsolineOptionsV05evCarC0AA05EVCarC0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/evCarOptions"></a>
<a class="token" href="#/s:7heresdk14IsolineOptionsV05evCarC0AA05EVCarC0VSgvp">evCarOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies options for calculation of isolines for electric car.
Mutually exclusive with <code><a href="../Structs/IsolineOptions.html#/s:7heresdk14IsolineOptionsV03carC0AA03CarC0VSgvp">IsolineOptions.carOptions</a></code>, <code><a href="../Structs/IsolineOptions.html#/s:7heresdk14IsolineOptionsV05truckC0AA05TruckC0VSgvp">IsolineOptions.truckOptions</a></code>, <code><a href="../Structs/IsolineOptions.html#/s:7heresdk14IsolineOptionsV07evTruckC0AA07EVTruckC0VSgvp">IsolineOptions.evTruckOptions</a></code> and <code><a href="../Structs/IsolineOptions.html#/s:7heresdk14IsolineOptionsV07routingC0AA07RoutingC0VSgvp">IsolineOptions.routingOptions</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the <code>routing_options</code> instead.")</span>
<span class="kd">public</span> <span class="k">var</span> <span class="nv">evCarOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-evcaroptions">EVCarOptions</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14IsolineOptionsV07evTruckC0AA07EVTruckC0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/evTruckOptions"></a>
<a class="token" href="#/s:7heresdk14IsolineOptionsV07evTruckC0AA07EVTruckC0VSgvp">evTruckOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies options for calculation of isolines for electric truck.
Mutually exclusive with <code><a href="../Structs/IsolineOptions.html#/s:7heresdk14IsolineOptionsV03carC0AA03CarC0VSgvp">IsolineOptions.carOptions</a></code>, <code><a href="../Structs/IsolineOptions.html#/s:7heresdk14IsolineOptionsV05truckC0AA05TruckC0VSgvp">IsolineOptions.truckOptions</a></code>, <code><a href="../Structs/IsolineOptions.html#/s:7heresdk14IsolineOptionsV05evCarC0AA05EVCarC0VSgvp">IsolineOptions.evCarOptions</a></code> and <code><a href="../Structs/IsolineOptions.html#/s:7heresdk14IsolineOptionsV07routingC0AA07RoutingC0VSgvp">IsolineOptions.routingOptions</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the <code>routing_options</code> instead.")</span>
<span class="kd">public</span> <span class="k">var</span> <span class="nv">evTruckOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-evtruckoptions">EVTruckOptions</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14IsolineOptionsV07routingC0AA07RoutingC0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/routingOptions"></a>
<a class="token" href="#/s:7heresdk14IsolineOptionsV07routingC0AA07RoutingC0VSgvp">routingOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies options for calculation of isolines for any vehicle type.
Mutually exclusive with <code><a href="../Structs/IsolineOptions.html#/s:7heresdk14IsolineOptionsV03carC0AA03CarC0VSgvp">IsolineOptions.carOptions</a></code>, <code><a href="../Structs/IsolineOptions.html#/s:7heresdk14IsolineOptionsV05truckC0AA05TruckC0VSgvp">IsolineOptions.truckOptions</a></code>, <code><a href="../Structs/IsolineOptions.html#/s:7heresdk14IsolineOptionsV05evCarC0AA05EVCarC0VSgvp">IsolineOptions.evCarOptions</a></code> and <code><a href="../Structs/IsolineOptions.html#/s:7heresdk14IsolineOptionsV07evTruckC0AA07EVTruckC0VSgvp">IsolineOptions.evTruckOptions</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">routingOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-routingoptions">RoutingOptions</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14IsolineOptionsV011calculationC003carC0A2C11CalculationV_AA03CarC0Vtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(calculationOptions:carOptions:)"></a>
<a class="token" href="#/s:7heresdk14IsolineOptionsV011calculationC003carC0A2C11CalculationV_AA03CarC0Vtcfc">init(calculationOptions:<wbr/>carOptions:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs options to calculate isolines from destination or origin,
with preferences for isoline calculation and car routing options.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the constructor with <code>RoutingOptions</code> parameter instead.")</span>
<span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">calculationOptions</span><span class="p">:</span> <span class="kt">IsolineOptions</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-isolineoptions-calculation">Calculation</a></span><span class="p">,</span> <span class="nv">carOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-caroptions">CarOptions</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>calculationOptions</em>
</code>
</td>
<td>
<div>
<p>The options to be used to calculate this isoline.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>carOptions</em>
</code>
</td>
<td>
<div>
<p>The options that should influence the possible routes within the isoline.
This determines also the transportation type.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14IsolineOptionsV011calculationC005truckC0A2C11CalculationV_AA05TruckC0Vtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(calculationOptions:truckOptions:)"></a>
<a class="token" href="#/s:7heresdk14IsolineOptionsV011calculationC005truckC0A2C11CalculationV_AA05TruckC0Vtcfc">init(calculationOptions:<wbr/>truckOptions:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs options to calculate isolines from destination or origin,
with preferences for isoline calculation and truck routing options.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the constructor with <code>RoutingOptions</code> parameter instead.")</span>
<span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">calculationOptions</span><span class="p">:</span> <span class="kt">IsolineOptions</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-isolineoptions-calculation">Calculation</a></span><span class="p">,</span> <span class="nv">truckOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-truckoptions">TruckOptions</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>calculationOptions</em>
</code>
</td>
<td>
<div>
<p>The options to be used to calculate this isoline.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>truckOptions</em>
</code>
</td>
<td>
<div>
<p>The options that should influence the possible routes within the isoline.
This determines also the transportation type.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14IsolineOptionsV011calculationC005evCarC0A2C11CalculationV_AA05EVCarC0Vtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(calculationOptions:evCarOptions:)"></a>
<a class="token" href="#/s:7heresdk14IsolineOptionsV011calculationC005evCarC0A2C11CalculationV_AA05EVCarC0Vtcfc">init(calculationOptions:<wbr/>evCarOptions:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs options to calculate isolines from destination or origin,
with preferences for isoline calculation and electric car routing options.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the constructor with <code>RoutingOptions</code> parameter instead.")</span>
<span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">calculationOptions</span><span class="p">:</span> <span class="kt">IsolineOptions</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-isolineoptions-calculation">Calculation</a></span><span class="p">,</span> <span class="nv">evCarOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-evcaroptions">EVCarOptions</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>calculationOptions</em>
</code>
</td>
<td>
<div>
<p>The options to be used to calculate this isoline.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>evCarOptions</em>
</code>
</td>
<td>
<div>
<p>The options that should influence the possible routes within the isoline.
This determines also the transportation type.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14IsolineOptionsV011calculationC007evTruckC0A2C11CalculationV_AA07EVTruckC0Vtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(calculationOptions:evTruckOptions:)"></a>
<a class="token" href="#/s:7heresdk14IsolineOptionsV011calculationC007evTruckC0A2C11CalculationV_AA07EVTruckC0Vtcfc">init(calculationOptions:<wbr/>evTruckOptions:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs options to calculate isolines from destination or origin,
with preferences for isoline calculation and electric truck routing options.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the constructor with <code>RoutingOptions</code> parameter instead.")</span>
<span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">calculationOptions</span><span class="p">:</span> <span class="kt">IsolineOptions</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-isolineoptions-calculation">Calculation</a></span><span class="p">,</span> <span class="nv">evTruckOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-evtruckoptions">EVTruckOptions</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>calculationOptions</em>
</code>
</td>
<td>
<div>
<p>The options to be used to calculate this isoline.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>evTruckOptions</em>
</code>
</td>
<td>
<div>
<p>The options that should influence the possible routes within the isoline.
This determines also the transportation type.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14IsolineOptionsV011calculationC007routingC0A2C11CalculationV_AA07RoutingC0Vtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(calculationOptions:routingOptions:)"></a>
<a class="token" href="#/s:7heresdk14IsolineOptionsV011calculationC007routingC0A2C11CalculationV_AA07RoutingC0Vtcfc">init(calculationOptions:<wbr/>routingOptions:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs options to calculate isolines from destination or origin,
with preferences for isoline calculation and routing options.
<strong>Notes</strong></p>
<ul>
<li>By default all vehicle specifications from <code><a href="../Structs/RoutingOptions.html#/s:7heresdk14RoutingOptionsV22transportSpecificationAA09TransportE0Vvp">RoutingOptions.transportSpecification</a></code> are set to
<code>nil</code> and the <code><a href="../Structs/TransportSpecification.html#/s:7heresdk22TransportSpecificationV13transportModeAA0bE0Ovp">TransportSpecification.transportMode</a></code> from <code><a href="../Structs/RoutingOptions.html#/s:7heresdk14RoutingOptionsV22transportSpecificationAA09TransportE0Vvp">RoutingOptions.transportSpecification</a></code>
is set to <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code>.</li>
<li>A route can be calculated with only the <code><a href="../Structs/TransportSpecification.html#/s:7heresdk22TransportSpecificationV13transportModeAA0bE0Ovp">TransportSpecification.transportMode</a></code> from
<code><a href="../Structs/RoutingOptions.html#/s:7heresdk14RoutingOptionsV22transportSpecificationAA09TransportE0Vvp">RoutingOptions.transportSpecification</a></code> set.</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">calculationOptions</span><span class="p">:</span> <span class="kt">IsolineOptions</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-isolineoptions-calculation">Calculation</a></span><span class="p">,</span> <span class="nv">routingOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-routingoptions">RoutingOptions</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>calculationOptions</em>
</code>
</td>
<td>
<div>
<p>The options to be used to calculate this isoline.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>routingOptions</em>
</code>
</td>
<td>
<div>
<p>The options that should influence the possible routes within the isoline.
This determines also the transportation type.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14IsolineOptionsV11CalculationV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/Calculation"></a>
<a class="token" href="#/s:7heresdk14IsolineOptionsV11CalculationV">Calculation</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies isoline parameters.
Setting at least one limit to <code><a href="../Structs/IsolineOptions/Calculation.html#/s:7heresdk14IsolineOptionsV11CalculationV11rangeValuesSays5Int32VGvp">IsolineOptions.Calculation.rangeValues</a></code> is mandatory or the calculation will fail.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-..-structs-isolineoptions-calculation">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">Calculation</span></code></pre>
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

</div>
`
}</HTMLBlock>
