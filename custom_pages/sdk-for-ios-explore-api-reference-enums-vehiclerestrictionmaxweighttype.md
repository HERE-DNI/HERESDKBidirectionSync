---
title: "sdk-for-ios-explore-api-reference-enums-vehiclerestrictionmaxweighttype"
slug: "sdk-for-ios-explore-api-reference-enums-vehiclerestrictionmaxweighttype"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Enum/VehicleRestrictionMaxWeightType"></a>
<a title="VehicleRestrictionMaxWeightType Enumeration Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-routing">Routing</a>
<img alt="" id="carat" src="../img/carat.png"/>
        VehicleRestrictionMaxWeightType Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>VehicleRestrictionMaxWeightType</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">VehicleRestrictionMaxWeightType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
<p>This enum represents the specific type of the maximum permitted weight restriction.
<strong>NOTES:</strong>
A restriction of type <code><a href="../Enums/VehicleRestrictionMaxWeightType.html#/s:7heresdk31VehicleRestrictionMaxWeightTypeO7unknownyA2CmF">VehicleRestrictionMaxWeightType.unknown</a></code> may change to <code><a href="../Enums/VehicleRestrictionMaxWeightType.html#/s:7heresdk31VehicleRestrictionMaxWeightTypeO5grossyA2CmF">VehicleRestrictionMaxWeightType.gross</a></code>, <code><a href="../Enums/VehicleRestrictionMaxWeightType.html#/s:7heresdk31VehicleRestrictionMaxWeightTypeO7currentyA2CmF">VehicleRestrictionMaxWeightType.current</a></code> or <code><a href="../Enums/VehicleRestrictionMaxWeightType.html#/s:7heresdk31VehicleRestrictionMaxWeightTypeO5emptyyA2CmF">VehicleRestrictionMaxWeightType.empty</a></code> when
data becomes available in future.
A restriction of type <code><a href="../Enums/VehicleRestrictionMaxWeightType.html#/s:7heresdk31VehicleRestrictionMaxWeightTypeO5grossyA2CmF">VehicleRestrictionMaxWeightType.gross</a></code>, <code><a href="../Enums/VehicleRestrictionMaxWeightType.html#/s:7heresdk31VehicleRestrictionMaxWeightTypeO7currentyA2CmF">VehicleRestrictionMaxWeightType.current</a></code> or <code><a href="../Enums/VehicleRestrictionMaxWeightType.html#/s:7heresdk31VehicleRestrictionMaxWeightTypeO5emptyyA2CmF">VehicleRestrictionMaxWeightType.empty</a></code> may also change to a different type if actual regulation changes.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk31VehicleRestrictionMaxWeightTypeO7unknownyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/unknown"></a>
<a class="token" href="#/s:7heresdk31VehicleRestrictionMaxWeightTypeO7unknownyA2CmF">unknown</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Restriction may apply to gross or current weight.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">unknown</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk31VehicleRestrictionMaxWeightTypeO5grossyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/gross"></a>
<a class="token" href="#/s:7heresdk31VehicleRestrictionMaxWeightTypeO5grossyA2CmF">gross</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Restriction is for gross weight.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">gross</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk31VehicleRestrictionMaxWeightTypeO7currentyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/current"></a>
<a class="token" href="#/s:7heresdk31VehicleRestrictionMaxWeightTypeO7currentyA2CmF">current</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Restriction is for current weight.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">current</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk31VehicleRestrictionMaxWeightTypeO5emptyyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/empty"></a>
<a class="token" href="#/s:7heresdk31VehicleRestrictionMaxWeightTypeO5emptyyA2CmF">empty</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Restriction is for empty weight.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">empty</span></code></pre>
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
