---
title: "sdk-for-ios-navigate-api-reference-structs-electronichorizon"
slug: "sdk-for-ios-navigate-api-reference-structs-electronichorizon"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ElectronicHorizon"></a>
<a title="ElectronicHorizon Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-electronichorizon">ElectronicHorizon</a>
<img alt="" id="carat" src="/carat.png"/>
        ElectronicHorizon Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>ElectronicHorizon</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ElectronicHorizon</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>A struct containing the full set of available paths
predicted for the current vehicle state.</p>
<p>Represents a snapshot of the horizon estimation at the moment the update
was generated.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17ElectronicHorizonV5pathsSayAA0bC4PathVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/paths"></a>
<a class="token" href="#/s:7heresdk17ElectronicHorizonV5pathsSayAA0bC4PathVGvp">paths</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A list of all available electronic horizon paths.
The list may be empty if none of the <code><a href="sdk-for-ios-navigate-api-reference-structs-electronichorizonpath">ElectronicHorizonPath</a></code>s are available.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">paths</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-electronichorizonpath">ElectronicHorizonPath</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17ElectronicHorizonV5pathsACSayAA0bC4PathVG_tcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(paths:)"></a>
<a class="token" href="#/s:7heresdk17ElectronicHorizonV5pathsACSayAA0bC4PathVG_tcfc">init(paths:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance.</p>
<p>Offline availability: This property is available online and offline.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">paths</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-electronichorizonpath">ElectronicHorizonPath</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[])</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17ElectronicHorizonV17mostPreferredPathAA0bcF0VSgyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/mostPreferredPath()"></a>
<a class="token" href="#/s:7heresdk17ElectronicHorizonV17mostPreferredPathAA0bcF0VSgyF">mostPreferredPath()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Returns the most preferred path among the set of available paths.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">mostPreferredPath</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-electronichorizonpath">ElectronicHorizonPath</a></span><span class="p">?</span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>The most preferred path, or <code>nil</code> if the list of available paths is empty.</p>
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
