---
title: "FuelAdditive"
slug: "sdk-for-ios-navigate-api-reference-structs-fueladditive"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/FuelAdditive"></a>
<a title="FuelAdditive Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-search">Search</a>

        FuelAdditive Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>FuelAdditive</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">FuelAdditive</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Contains fuel additive information for generic fuel type.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12FuelAdditiveV4typeAA0bC4TypeOvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/type"></a>
<a class="token" href="#/s:7heresdk12FuelAdditiveV4typeAA0bC4TypeOvp">type</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The type of the fuel additive. For now, only AUS 32 is supported.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">type</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-fueladditivetype">FuelAdditiveType</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12FuelAdditiveV15availableInCansSbSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/availableInCans"></a>
<a class="token" href="#/s:7heresdk12FuelAdditiveV15availableInCansSbSgvp">availableInCans</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates if the fuel additive is available in cans or not. <code>nil</code> means information is unknown.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">availableInCans</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12FuelAdditiveV15availableAtPumpSbSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/availableAtPump"></a>
<a class="token" href="#/s:7heresdk12FuelAdditiveV15availableAtPumpSbSgvp">availableAtPump</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates if the fuel additive is available at the pump or not. <code>nil</code> means information is unknown.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">availableAtPump</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12FuelAdditiveV4type15availableInCans0E6AtPumpAcA0bC4TypeO_SbSgAItcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(type:availableInCans:availableAtPump:)"></a>
<a class="token" href="#/s:7heresdk12FuelAdditiveV4type15availableInCans0E6AtPumpAcA0bC4TypeO_SbSgAItcfc">init(type:<wbr/>availableInCans:<wbr/>availableAtPump:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">type</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-fueladditivetype">FuelAdditiveType</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-fueladditivetype">FuelAdditiveType</a></span><span class="o">.</span><span class="n">aus32</span><span class="p">,</span> <span class="nv">availableInCans</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">availableAtPump</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
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
