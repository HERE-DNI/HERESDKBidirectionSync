---
title: "Untitled"
slug: "sdk-for-ios-navigate-api-reference-enums-junctionstraversability"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- JunctionsTraversability.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Enum/JunctionsTraversability"></a>
<a title="JunctionsTraversability Enumeration Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-core">Core</a>
<img alt="" id="carat" src="../img/carat.png"/>
        JunctionsTraversability Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>JunctionsTraversability</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">JunctionsTraversability</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
<p>Junctions traversability of some traffic incident or flow section.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23JunctionsTraversabilityO7allOpenyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/allOpen"></a>
<a class="token" href="#/s:7heresdk23JunctionsTraversabilityO7allOpenyA2CmF">allOpen</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>All junctions are open.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">allOpen</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23JunctionsTraversabilityO9allClosedyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/allClosed"></a>
<a class="token" href="#/s:7heresdk23JunctionsTraversabilityO9allClosedyA2CmF">allClosed</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>All junctions are closed.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">allClosed</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23JunctionsTraversabilityO26intermediateClosedEdgeOpenyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/intermediateClosedEdgeOpen"></a>
<a class="token" href="#/s:7heresdk23JunctionsTraversabilityO26intermediateClosedEdgeOpenyA2CmF">intermediateClosedEdgeOpen</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Junctions at the beginning and end of the roadway are open, intermediate junctions are closed.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">intermediateClosedEdgeOpen</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23JunctionsTraversabilityO21startOpenOthersClosedyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/startOpenOthersClosed"></a>
<a class="token" href="#/s:7heresdk23JunctionsTraversabilityO21startOpenOthersClosedyA2CmF">startOpenOthersClosed</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>First edge junction is open, all others are closed.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">startOpenOthersClosed</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23JunctionsTraversabilityO19endOpenOthersClosedyA2CmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/endOpenOthersClosed"></a>
<a class="token" href="#/s:7heresdk23JunctionsTraversabilityO19endOpenOthersClosedyA2CmF">endOpenOthersClosed</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>First edge junction is open, all others are closed.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">endOpenOthersClosed</span></code></pre>
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

</div>
`
}</HTMLBlock>
