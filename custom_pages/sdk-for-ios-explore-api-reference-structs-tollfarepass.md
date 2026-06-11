---
title: "TollFarePass"
slug: "sdk-for-ios-explore-api-reference-structs-tollfarepass"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TollFarePass"></a>
<a title="TollFarePass Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>

<a href="sdk-for-ios-explore-api-reference-routing">Routing</a>

        TollFarePass Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>TollFarePass</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TollFarePass</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p><code><a href="sdk-for-ios-explore-api-reference-structs-tollfare">TollFare</a></code> multi-travel pass characteristics.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12TollFarePassV13returnJourneySbSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/returnJourney"></a>
<a class="token" href="#/s:7heresdk12TollFarePassV13returnJourneySbSgvp">returnJourney</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This pass includes the fare for the return journey.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">returnJourney</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12TollFarePassV14validityPeriodAA0cd8ValidityF0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/validityPeriod"></a>
<a class="token" href="#/s:7heresdk12TollFarePassV14validityPeriodAA0cd8ValidityF0VSgvp">validityPeriod</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies a temporal validity period for a pass.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">validityPeriod</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-farepassvalidityperiod">FarePassValidityPeriod</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12TollFarePassV7travelss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/travels"></a>
<a class="token" href="#/s:7heresdk12TollFarePassV7travelss5Int32VSgvp">travels</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This pass allows for the specified number of travels.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">travels</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12TollFarePassV9transferss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/transfers"></a>
<a class="token" href="#/s:7heresdk12TollFarePassV9transferss5Int32VSgvp">transfers</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates if transfers are permitted with this pass, and if so, how many.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">transfers</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12TollFarePassV06seniorD0SbSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/seniorPass"></a>
<a class="token" href="#/s:7heresdk12TollFarePassV06seniorD0SbSgvp">seniorPass</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This pass is valid only if presented by a senior person.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">seniorPass</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12TollFarePassV13returnJourney14validityPeriod7travels9transfers06seniorD0ACSbSg_AA0cd8ValidityH0VSgs5Int32VSgAoItcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(returnJourney:validityPeriod:travels:transfers:seniorPass:)"></a>
<a class="token" href="#/s:7heresdk12TollFarePassV13returnJourney14validityPeriod7travels9transfers06seniorD0ACSbSg_AA0cd8ValidityH0VSgs5Int32VSgAoItcfc">init(returnJourney:<wbr/>validityPeriod:<wbr/>travels:<wbr/>transfers:<wbr/>seniorPass:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">returnJourney</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">validityPeriod</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-farepassvalidityperiod">FarePassValidityPeriod</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">travels</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">transfers</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">seniorPass</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
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
