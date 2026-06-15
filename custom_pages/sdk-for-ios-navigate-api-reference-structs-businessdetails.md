---
title: "BusinessDetails"
slug: "sdk-for-ios-navigate-api-reference-structs-businessdetails"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/BusinessDetails"></a>
<a title="BusinessDetails Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-search">Search</a>

        BusinessDetails Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>BusinessDetails</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">BusinessDetails</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Contains place details such as contacts, opening hours and some electro vehicle info.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15BusinessDetailsV8contactsSayAA7ContactVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/contacts"></a>
<a class="token" href="#/s:7heresdk15BusinessDetailsV8contactsSayAA7ContactVGvp">contacts</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of contact information of the place.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">contacts</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-contact">Contact</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15BusinessDetailsV12openingHoursSayAA07OpeningE0VGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/openingHours"></a>
<a class="token" href="#/s:7heresdk15BusinessDetailsV12openingHoursSayAA07OpeningE0VGvp">openingHours</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of opening hours information of the place (not available in result of suggest request).</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">openingHours</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-openinghours">OpeningHours</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15BusinessDetailsV14evChargingPoolAA010EVChargingF0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/evChargingPool"></a>
<a class="token" href="#/s:7heresdk15BusinessDetailsV14evChargingPoolAA010EVChargingF0VSgvp">evChargingPool</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>EV charging pool details. It is available only for a place that is a charging pool
for electric vehicles. Charging stations data are only available to users with
valid contracts with HERE.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">evChargingPool</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-evchargingpool">EVChargingPool</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15BusinessDetailsV8contacts12openingHours14evChargingPoolACSayAA7ContactVG_SayAA07OpeningF0VGAA010EVChargingI0VSgtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(contacts:openingHours:evChargingPool:)"></a>
<a class="token" href="#/s:7heresdk15BusinessDetailsV8contacts12openingHours14evChargingPoolACSayAA7ContactVG_SayAA07OpeningF0VGAA010EVChargingI0VSgtcfc">init(contacts:<wbr/>openingHours:<wbr/>evChargingPool:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">contacts</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-contact">Contact</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">openingHours</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-openinghours">OpeningHours</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">evChargingPool</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-evchargingpool">EVChargingPool</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
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
