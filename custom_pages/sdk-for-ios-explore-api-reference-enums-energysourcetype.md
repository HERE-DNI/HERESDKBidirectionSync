---
title: "EnergySourceType Enumeration Reference"
slug: "sdk-for-ios-explore-api-reference-enums-energysourcetype"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- EnergySourceType.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Enum/EnergySourceType"></a>
<a title="EnergySourceType Enumeration Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="sdk-for-ios-explore-api-reference-..-index">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-search">Search</a>
<img alt="" id="carat" src="../img/carat.png"/>
        EnergySourceType Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public enum EnergySourceType : UInt32, CaseIterable, Codable</code></pre>
</div>
</div>
<p>Represents energy source type.
EnergySource contains this representing the type of the energy source.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16EnergySourceTypeO7nuclearyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/nuclear"></a>
<a class="token" href="#/s:7heresdk16EnergySourceTypeO7nuclearyA2CmF">nuclear</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Nuclear power sources.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case nuclear</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16EnergySourceTypeO13generalFossilyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/generalFossil"></a>
<a class="token" href="#/s:7heresdk16EnergySourceTypeO13generalFossilyA2CmF">generalFossil</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>All kinds of fossil power sources.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case generalFossil</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16EnergySourceTypeO4coalyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/coal"></a>
<a class="token" href="#/s:7heresdk16EnergySourceTypeO4coalyA2CmF">coal</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Fossil power from coal.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case coal</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16EnergySourceTypeO3gasyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/gas"></a>
<a class="token" href="#/s:7heresdk16EnergySourceTypeO3gasyA2CmF">gas</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Fossil power from gas.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case gas</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16EnergySourceTypeO12generalGreenyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/generalGreen"></a>
<a class="token" href="#/s:7heresdk16EnergySourceTypeO12generalGreenyA2CmF">generalGreen</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>All kinds of regenerative power sources.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case generalGreen</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16EnergySourceTypeO5solaryA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/solar"></a>
<a class="token" href="#/s:7heresdk16EnergySourceTypeO5solaryA2CmF">solar</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Regenerative power from sunlight.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case solar</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16EnergySourceTypeO4windyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/wind"></a>
<a class="token" href="#/s:7heresdk16EnergySourceTypeO4windyA2CmF">wind</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Regenerative power from wind.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case wind</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16EnergySourceTypeO5wateryA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/water"></a>
<a class="token" href="#/s:7heresdk16EnergySourceTypeO5wateryA2CmF">water</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Regenerative power from water.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>case water</code></pre>
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



</div>
`
}</HTMLBlock>
