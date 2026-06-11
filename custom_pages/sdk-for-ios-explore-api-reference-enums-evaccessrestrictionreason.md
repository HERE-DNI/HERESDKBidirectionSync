---
title: "EVAccessRestrictionReason"
slug: "sdk-for-ios-explore-api-reference-enums-evaccessrestrictionreason"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Enum/EVAccessRestrictionReason"></a>
<a title="EVAccessRestrictionReason Enumeration Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>

<a href="sdk-for-ios-explore-api-reference-search">Search</a>

        EVAccessRestrictionReason Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>EVAccessRestrictionReason</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">EVAccessRestrictionReason</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
<p>Represents the restriction reason of an <code><a href="sdk-for-ios-explore-api-reference-structs-evchargingpool">EVChargingPool</a></code>.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25EVAccessRestrictionReasonO13customersOnlyyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/customersOnly"></a>
<a class="token" href="#/s:7heresdk25EVAccessRestrictionReasonO13customersOnlyyA2CmF">customersOnly</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Charging for customers of a hotel, restaurant, store etc.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">customersOnly</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25EVAccessRestrictionReasonO9brandOnlyyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/brandOnly"></a>
<a class="token" href="#/s:7heresdk25EVAccessRestrictionReasonO9brandOnlyyA2CmF">brandOnly</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Vehicle brand-restriction, e.g. Tesla, BMW.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">brandOnly</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25EVAccessRestrictionReasonO14carSharingOnlyyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/carSharingOnly"></a>
<a class="token" href="#/s:7heresdk25EVAccessRestrictionReasonO14carSharingOnlyyA2CmF">carSharingOnly</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Charging for car sharing.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">carSharingOnly</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25EVAccessRestrictionReasonO9taxisOnlyyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/taxisOnly"></a>
<a class="token" href="#/s:7heresdk25EVAccessRestrictionReasonO9taxisOnlyyA2CmF">taxisOnly</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Charging for taxis</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">taxisOnly</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25EVAccessRestrictionReasonO5otheryA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/other"></a>
<a class="token" href="#/s:7heresdk25EVAccessRestrictionReasonO5otheryA2CmF">other</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Charging is restricted due to other reasons</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">other</span></code></pre>
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
