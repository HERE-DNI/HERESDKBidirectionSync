---
title: "sdk-for-ios-explore-api-reference-classes-collectionof"
slug: "sdk-for-ios-explore-api-reference-classes-collectionof"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/CollectionOf"></a>
<a title="CollectionOf Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-core">Core</a>
<img alt="" id="carat" src="/carat.png"/>
        CollectionOf Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>CollectionOf</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">CollectionOf</span><span class="o">&lt;</span><span class="kt">T</span><span class="o">&gt;</span> <span class="p">:</span> <span class="kt">Collection</span></code></pre>
</div>
</div>
<p>Custom collection implementation.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:ST7ElementQa"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/Element"></a>
<a class="token" href="#/s:ST7ElementQa">Element</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">Element</span> <span class="o">=</span> <span class="kt">T</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:Sl5IndexQa"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/Index"></a>
<a class="token" href="#/s:Sl5IndexQa">Index</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">Index</span> <span class="o">=</span> <span class="kt">UInt64</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:Sl10startIndex0B0Qzvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/startIndex"></a>
<a class="token" href="#/s:Sl10startIndex0B0Qzvp">startIndex</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">private(set)</span> <span class="kd">public</span> <span class="k">var</span> <span class="nv">startIndex</span><span class="p">:</span> <span class="kt"><a href="../Classes/CollectionOf.html#/s:Sl5IndexQa">Index</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:Sl8endIndex0B0Qzvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/endIndex"></a>
<a class="token" href="#/s:Sl8endIndex0B0Qzvp">endIndex</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">private(set)</span> <span class="kd">public</span> <span class="k">var</span> <span class="nv">endIndex</span><span class="p">:</span> <span class="kt"><a href="../Classes/CollectionOf.html#/s:Sl5IndexQa">Index</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:Sl5index5after5IndexQzAD_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/index(after:)"></a>
<a class="token" href="#/s:Sl5index5after5IndexQzAD_tF">index(after:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">index</span><span class="p">(</span><span class="n">after</span> <span class="nv">i</span><span class="p">:</span> <span class="kt"><a href="../Classes/CollectionOf.html#/s:Sl5IndexQa">Index</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="../Classes/CollectionOf.html#/s:Sl5IndexQa">Index</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:Sly7ElementQz5IndexQzcip"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/subscript(_:)"></a>
<a class="token" href="#/s:Sly7ElementQz5IndexQzcip">subscript(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">subscript</span><span class="p">(</span><span class="nv">position</span><span class="p">:</span> <span class="kt"><a href="../Classes/CollectionOf.html#/s:Sl5IndexQa">Index</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="../Classes/CollectionOf.html#/s:ST7ElementQa">Element</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
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
