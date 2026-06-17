---
title: "HazardousMaterialRestriction"
slug: "sdk-for-ios-navigate-structs-hazardousmaterialrestriction"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/HazardousMaterialRestriction"></a>
<a title="HazardousMaterialRestriction Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-index">heresdk</a>

<a href="sdk-for-ios-navigate-transport">Transport</a>

        HazardousMaterialRestriction Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>HazardousMaterialRestriction</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">HazardousMaterialRestriction</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Represents restriction on transport of hazardous materials.
A generic restriction, applying to any hazardous material, is encoded with empty member
variables.</p>
<p><strong>Note:</strong> This is a beta release of this feature.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk28HazardousMaterialRestrictionV09hazardousC0AA0bC0OSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/hazardousMaterial"></a>
<a class="token" href="#/s:7heresdk28HazardousMaterialRestrictionV09hazardousC0AA0bC0OSgvp">hazardousMaterial</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Restricted hazardous material.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">hazardousMaterial</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-hazardousmaterial">HazardousMaterial</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk28HazardousMaterialRestrictionV14tunnelCategoryAA06TunnelF0OSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/tunnelCategory"></a>
<a class="token" href="#/s:7heresdk28HazardousMaterialRestrictionV14tunnelCategoryAA06TunnelF0OSgvp">tunnelCategory</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Tunnel category to restrict transport of specific goods.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">tunnelCategory</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-tunnelcategory">TunnelCategory</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk28HazardousMaterialRestrictionV09hazardousC0AcA0bC0OSg_tcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(hazardousMaterial:)"></a>
<a class="token" href="#/s:7heresdk28HazardousMaterialRestrictionV09hazardousC0AcA0bC0OSg_tcfc">init(hazardousMaterial:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates hazardous material restriction for specified material.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">hazardousMaterial</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-hazardousmaterial">HazardousMaterial</a></span><span class="p">?)</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk28HazardousMaterialRestrictionV14tunnelCategoryAcA06TunnelF0OSg_tcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(tunnelCategory:)"></a>
<a class="token" href="#/s:7heresdk28HazardousMaterialRestrictionV14tunnelCategoryAcA06TunnelF0OSg_tcfc">init(tunnelCategory:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates hazardous material restriction for specified tunnel category.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">tunnelCategory</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-tunnelcategory">TunnelCategory</a></span><span class="p">?)</span></code></pre>
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
