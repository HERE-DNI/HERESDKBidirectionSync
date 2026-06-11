---
title: "sdk-for-ios-navigate-api-reference-structs-electronichorizonupdate"
slug: "sdk-for-ios-navigate-api-reference-structs-electronichorizonupdate"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ElectronicHorizonUpdate"></a>
<a title="ElectronicHorizonUpdate Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-electronichorizon">ElectronicHorizon</a>
<img alt="" id="carat" src="/carat.png"/>
        ElectronicHorizonUpdate Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>ElectronicHorizonUpdate</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ElectronicHorizonUpdate</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>A struct representing a full update delivered via <code><a href="sdk-for-ios-navigate-api-reference-protocols-electronichorizondelegate">ElectronicHorizonDelegate</a></code> notifications.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23ElectronicHorizonUpdateV010electronicC0AA0bC0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/electronicHorizon"></a>
<a class="token" href="#/s:7heresdk23ElectronicHorizonUpdateV010electronicC0AA0bC0VSgvp">electronicHorizon</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The full electronic horizon recomputed for the current vehicle state.
May be <code>nil</code> if there is no update.</p>
<p>Contains the complete set of preferred paths.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">electronicHorizon</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-electronichorizon">ElectronicHorizon</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23ElectronicHorizonUpdateV14segmentChangesAA0bc7SegmentF0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/segmentChanges"></a>
<a class="token" href="#/s:7heresdk23ElectronicHorizonUpdateV14segmentChangesAA0bc7SegmentF0VSgvp">segmentChanges</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The difference between the previously emitted horizon and the newly computed one.
Contains added and removed segments.
May be <code>nil</code> if there is no update.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">segmentChanges</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-electronichorizonsegmentchanges">ElectronicHorizonSegmentChanges</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23ElectronicHorizonUpdateV8positionAA0bC8PositionVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/position"></a>
<a class="token" href="#/s:7heresdk23ElectronicHorizonUpdateV8positionAA0bC8PositionVvp">position</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The vehicle’s updated position relative to the electronic horizon.
Always present. If no <code>electronic_horizon</code> is available, the position
refers to the most recently known horizon.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">position</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-electronichorizonposition">ElectronicHorizonPosition</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23ElectronicHorizonUpdateV010electronicC014segmentChanges8positionAcA0bC0VSg_AA0bc7SegmentG0VSgAA0bC8PositionVtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(electronicHorizon:segmentChanges:position:)"></a>
<a class="token" href="#/s:7heresdk23ElectronicHorizonUpdateV010electronicC014segmentChanges8positionAcA0bC0VSg_AA0bc7SegmentG0VSgAA0bC8PositionVtcfc">init(electronicHorizon:<wbr/>segmentChanges:<wbr/>position:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance.</p>
<p>Offline availability: This property is available online and offline.</p>
<ul>
<li><p>Parameters</p>
<ul>
<li>electronicHorizon: The full electronic horizon recomputed for the current vehicle state.
May be <code>nil</code> if there is no update.</li>
</ul>
<p>Contains the complete set of preferred paths.</p>
<ul>
<li>segmentChanges: The difference between the previously emitted horizon and the newly computed one.
Contains added and removed segments.
May be <code>nil</code> if there is no update.</li>
<li>position: The vehicle’s updated position relative to the electronic horizon.
Always present. If no <code>electronic_horizon</code> is available, the position
refers to the most recently known horizon.</li>
</ul></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">electronicHorizon</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-electronichorizon">ElectronicHorizon</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">segmentChanges</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-electronichorizonsegmentchanges">ElectronicHorizonSegmentChanges</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">position</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-electronichorizonposition">ElectronicHorizonPosition</a></span><span class="p">)</span></code></pre>
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
