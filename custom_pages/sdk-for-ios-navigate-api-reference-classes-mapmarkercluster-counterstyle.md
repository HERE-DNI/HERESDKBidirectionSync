---
title: "CounterStyle"
slug: "sdk-for-ios-navigate-api-reference-classes-mapmarkercluster-counterstyle"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/CounterStyle"></a>
<a title="CounterStyle Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-maps">Maps</a>

<a href="sdk-for-ios-navigate-api-reference-classes-mapmarkercluster">MapMarkerCluster</a>

        CounterStyle Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>CounterStyle</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">CounterStyle</span></code></pre>
</div>
</div>
<p>Styling options for a marker cluster which is represented by the marker count as a text.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16MapMarkerClusterC12CounterStyleV9textColorSo7UIColorCvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/textColor"></a>
<a class="token" href="#/s:7heresdk16MapMarkerClusterC12CounterStyleV9textColorSo7UIColorCvp">textColor</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Font color of counter. Default value is white.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">textColor</span><span class="p">:</span> <span class="kt">UIColor</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16MapMarkerClusterC12CounterStyleV8fontSizeSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/fontSize"></a>
<a class="token" href="#/s:7heresdk16MapMarkerClusterC12CounterStyleV8fontSizeSdvp">fontSize</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Font size of counter. Default value is 20.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">fontSize</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16MapMarkerClusterC12CounterStyleV10textAnchorAA8Anchor2DVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/textAnchor"></a>
<a class="token" href="#/s:7heresdk16MapMarkerClusterC12CounterStyleV10textAnchorAA8Anchor2DVvp">textAnchor</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Anchor of counter in regards to marker cluster image. Default is at the center.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">textAnchor</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-anchor2d">Anchor2D</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16MapMarkerClusterC12CounterStyleV14maxCountNumbers5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maxCountNumber"></a>
<a class="token" href="#/s:7heresdk16MapMarkerClusterC12CounterStyleV14maxCountNumbers5Int32Vvp">maxCountNumber</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Maximal number of markers represented as exact number. Values smaller than 2 will be clamped to 2.
Default value is 99. When this value is changed, it is recommended to adapt <code><a href="../../Classes/MapMarkerCluster/CounterStyle.html#/s:7heresdk16MapMarkerClusterC12CounterStyleV12aboveMaxTextSSvp">MapMarkerCluster.CounterStyle.aboveMaxText</a></code> accordingly.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">maxCountNumber</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16MapMarkerClusterC12CounterStyleV12aboveMaxTextSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/aboveMaxText"></a>
<a class="token" href="#/s:7heresdk16MapMarkerClusterC12CounterStyleV12aboveMaxTextSSvp">aboveMaxText</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>String to display if there are more markers clustered than <code><a href="../../Classes/MapMarkerCluster/CounterStyle.html#/s:7heresdk16MapMarkerClusterC12CounterStyleV14maxCountNumbers5Int32Vvp">MapMarkerCluster.CounterStyle.maxCountNumber</a></code>. Default value is “+99”.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">aboveMaxText</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16MapMarkerClusterC12CounterStyleV9textColor8fontSize0G6Anchor14maxCountNumber12aboveMaxTextAESo7UIColorC_SdAA8Anchor2DVs5Int32VSStcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(textColor:fontSize:textAnchor:maxCountNumber:aboveMaxText:)"></a>
<a class="token" href="#/s:7heresdk16MapMarkerClusterC12CounterStyleV9textColor8fontSize0G6Anchor14maxCountNumber12aboveMaxTextAESo7UIColorC_SdAA8Anchor2DVs5Int32VSStcfc">init(textColor:<wbr/>fontSize:<wbr/>textAnchor:<wbr/>maxCountNumber:<wbr/>aboveMaxText:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">textColor</span><span class="p">:</span> <span class="kt">UIColor</span> <span class="o">=</span> <span class="kt">NamedColor</span><span class="o">.</span><span class="n">white</span><span class="p">,</span> <span class="nv">fontSize</span><span class="p">:</span> <span class="kt">Double</span> <span class="o">=</span> <span class="mf">20.0</span><span class="p">,</span> <span class="nv">textAnchor</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-anchor2d">Anchor2D</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-anchor2d">Anchor2D</a></span><span class="p">(),</span> <span class="nv">maxCountNumber</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">99</span><span class="p">,</span> <span class="nv">aboveMaxText</span><span class="p">:</span> <span class="kt">String</span> <span class="o">=</span> <span class="s">"+99"</span><span class="p">)</span></code></pre>
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
