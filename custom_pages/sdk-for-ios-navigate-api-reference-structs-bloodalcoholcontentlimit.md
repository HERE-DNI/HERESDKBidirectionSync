---
title: "BloodAlcoholContentLimit"
slug: "sdk-for-ios-navigate-api-reference-structs-bloodalcoholcontentlimit"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/BloodAlcoholContentLimit"></a>
<a title="BloodAlcoholContentLimit Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-mapdata">MapData</a>

        BloodAlcoholContentLimit Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>BloodAlcoholContentLimit</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">BloodAlcoholContentLimit</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Represents the rules regarding alcohol in blood content limit in a country or state for
all types of drivers.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24BloodAlcoholContentLimitV012noviceDriverE17InPartsPerMillions5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/noviceDriverLimitInPartsPerMillion"></a>
<a class="token" href="#/s:7heresdk24BloodAlcoholContentLimitV012noviceDriverE17InPartsPerMillions5Int32Vvp">noviceDriverLimitInPartsPerMillion</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Alcohol in blood content limit for novice drivers expressed in parts per million.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">noviceDriverLimitInPartsPerMillion</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24BloodAlcoholContentLimitV014standardDriverE17InPartsPerMillions5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/standardDriverLimitInPartsPerMillion"></a>
<a class="token" href="#/s:7heresdk24BloodAlcoholContentLimitV014standardDriverE17InPartsPerMillions5Int32Vvp">standardDriverLimitInPartsPerMillion</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Alcohol in blood content limit for standard drivers expressed in parts per million.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">standardDriverLimitInPartsPerMillion</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24BloodAlcoholContentLimitV016commercialDriverE17InPartsPerMillions5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/commercialDriverLimitInPartsPerMillion"></a>
<a class="token" href="#/s:7heresdk24BloodAlcoholContentLimitV016commercialDriverE17InPartsPerMillions5Int32Vvp">commercialDriverLimitInPartsPerMillion</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Alcohol in blood content limit for commercial drivers expressed in parts per million.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">commercialDriverLimitInPartsPerMillion</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24BloodAlcoholContentLimitV012noviceDriverE17InPartsPerMillion08standardgehijK0010commercialgehijK0ACs5Int32V_A2Htcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(noviceDriverLimitInPartsPerMillion:standardDriverLimitInPartsPerMillion:commercialDriverLimitInPartsPerMillion:)"></a>
<a class="token" href="#/s:7heresdk24BloodAlcoholContentLimitV012noviceDriverE17InPartsPerMillion08standardgehijK0010commercialgehijK0ACs5Int32V_A2Htcfc">init(noviceDriverLimitInPartsPerMillion:<wbr/>standardDriverLimitInPartsPerMillion:<wbr/>commercialDriverLimitInPartsPerMillion:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">noviceDriverLimitInPartsPerMillion</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nv">standardDriverLimitInPartsPerMillion</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nv">commercialDriverLimitInPartsPerMillion</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">0</span><span class="p">)</span></code></pre>
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
