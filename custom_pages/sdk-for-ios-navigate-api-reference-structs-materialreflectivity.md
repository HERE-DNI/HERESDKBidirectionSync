---
title: "Maps / MaterialReflectivity"
slug: "sdk-for-ios-navigate-api-reference-structs-materialreflectivity"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/MaterialReflectivity"></a>
<a title="MaterialReflectivity Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-maps">Maps</a>
<img alt="" id="carat" src="../img/carat.png"/>
        MaterialReflectivity Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>MaterialReflectivity</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">MaterialReflectivity</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Material reflectivity properties are used to enable per‑pixel lighting for supported map objects
(e.g. <code><a href="sdk-for-ios-navigate-api-reference-..-classes-locationindicator">LocationIndicator</a></code> markers and their halo).</p>
<h2 class="heading" id="lighting-off-vs-on">Lighting OFF vs ON</h2>
<p>By default (when no MaterialReflectivity is assigned) objects are rendered “unlit” (emissive):
their texture / color appears at a constant brightness, unaffected by scene lights. Assigning a
<code>MaterialReflectivity</code> instance to an object that supports it (e.g. <code><a href="../Classes/LocationIndicator.html#/s:7heresdk17LocationIndicatorC20materialReflectivityAA08MaterialE0VSgvp">LocationIndicator.materialReflectivity</a></code>)
automatically enables lighting for this object and all its internal components. Clearing (setting the property to
<code>nil</code>) disables lighting again and restores the unlit appearance.</p>
<h2 class="heading" id="factors">Factors</h2>
<p>Both factors are expected to be within [0.0, 1.0]. Values outside this range are allowed but may
produce exaggerated results or be clamped by future implementations. Typical useful ranges:</p>
<ul>
<li>ambientFactor: 0.0 – 0.4 (higher values flatten the shading and reduce directional contrast)</li>
<li>diffuseFactor: 0.5 – 1.0 (lower values dim the object under directional light)</li>
</ul>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20MaterialReflectivityV13ambientFactorSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/ambientFactor"></a>
<a class="token" href="#/s:7heresdk20MaterialReflectivityV13ambientFactorSdvp">ambientFactor</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The ambient factor controls how much of the object’s base color is treated as
constant ambient contribution (independent of light direction) when lighting is enabled. Default value is 0.0.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">ambientFactor</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20MaterialReflectivityV13diffuseFactorSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/diffuseFactor"></a>
<a class="token" href="#/s:7heresdk20MaterialReflectivityV13diffuseFactorSdvp">diffuseFactor</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The diffuse factor controls how much of the object’s color contributes to
the diffuse lighting component when lighting is enabled. Default value is 1.0.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">diffuseFactor</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20MaterialReflectivityV13ambientFactor07diffuseE0ACSd_Sdtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(ambientFactor:diffuseFactor:)"></a>
<a class="token" href="#/s:7heresdk20MaterialReflectivityV13ambientFactor07diffuseE0ACSd_Sdtcfc">init(ambientFactor:<wbr/>diffuseFactor:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">ambientFactor</span><span class="p">:</span> <span class="kt">Double</span> <span class="o">=</span> <span class="mf">0.0</span><span class="p">,</span> <span class="nv">diffuseFactor</span><span class="p">:</span> <span class="kt">Double</span> <span class="o">=</span> <span class="mf">1.0</span><span class="p">)</span></code></pre>
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
