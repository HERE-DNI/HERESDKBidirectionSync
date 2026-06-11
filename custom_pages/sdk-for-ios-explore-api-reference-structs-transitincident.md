---
title: "sdk-for-ios-explore-api-reference-structs-transitincident"
slug: "sdk-for-ios-explore-api-reference-structs-transitincident"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TransitIncident"></a>
<a title="TransitIncident Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-routing">Routing</a>
<img alt="" id="carat" src="/carat.png"/>
        TransitIncident Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>TransitIncident</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TransitIncident</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>A transit incident describes disruptions on the transit network.
Disruptions scale from delays to service cancellations.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TransitIncidentV7summarySSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/summary"></a>
<a class="token" href="#/s:7heresdk15TransitIncidentV7summarySSSgvp">summary</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A human readable summary of the incident.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">summary</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TransitIncidentV11descriptionSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/description"></a>
<a class="token" href="#/s:7heresdk15TransitIncidentV11descriptionSSSgvp">description</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A human readable description of the incident</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">description</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TransitIncidentV4typeAA0bC4TypeOSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/type"></a>
<a class="token" href="#/s:7heresdk15TransitIncidentV4typeAA0bC4TypeOSgvp">type</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Type of the incident.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">type</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-transitincidenttype">TransitIncidentType</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TransitIncidentV6effectAA0bC6EffectOSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/effect"></a>
<a class="token" href="#/s:7heresdk15TransitIncidentV6effectAA0bC6EffectOSgvp">effect</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Effect of the incident.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">effect</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-transitincidenteffect">TransitIncidentEffect</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TransitIncidentV9validFrom10Foundation4DateVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/validFrom"></a>
<a class="token" href="#/s:7heresdk15TransitIncidentV9validFrom10Foundation4DateVSgvp">validFrom</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Valid from.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">validFrom</span><span class="p">:</span> <span class="kt">Date</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TransitIncidentV10validUntil10Foundation4DateVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/validUntil"></a>
<a class="token" href="#/s:7heresdk15TransitIncidentV10validUntil10Foundation4DateVSgvp">validUntil</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Valid until.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">validUntil</span><span class="p">:</span> <span class="kt">Date</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TransitIncidentV3urlSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/url"></a>
<a class="token" href="#/s:7heresdk15TransitIncidentV3urlSSSgvp">url</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Link to the original incident published at the agency website.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">url</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TransitIncidentV7summary11description4type6effect9validFrom0H5Until3urlACSSSg_AkA0bC4TypeOSgAA0bC6EffectOSg10Foundation4DateVSgAuKtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(summary:description:type:effect:validFrom:validUntil:url:)"></a>
<a class="token" href="#/s:7heresdk15TransitIncidentV7summary11description4type6effect9validFrom0H5Until3urlACSSSg_AkA0bC4TypeOSgAA0bC6EffectOSg10Foundation4DateVSgAuKtcfc">init(summary:<wbr/>description:<wbr/>type:<wbr/>effect:<wbr/>validFrom:<wbr/>validUntil:<wbr/>url:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">summary</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">description</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">type</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-transitincidenttype">TransitIncidentType</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">effect</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-transitincidenteffect">TransitIncidentEffect</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">validFrom</span><span class="p">:</span> <span class="kt">Date</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">validUntil</span><span class="p">:</span> <span class="kt">Date</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">url</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
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
