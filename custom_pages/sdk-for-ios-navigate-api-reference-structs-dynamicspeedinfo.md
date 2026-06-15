---
title: "DynamicSpeedInfo"
slug: "sdk-for-ios-navigate-api-reference-structs-dynamicspeedinfo"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/DynamicSpeedInfo"></a>
<a title="DynamicSpeedInfo Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-routing">Routing</a>

        DynamicSpeedInfo Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>DynamicSpeedInfo</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">DynamicSpeedInfo</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Provides estimated speed information.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16DynamicSpeedInfoV04baseC17InMetersPerSecondSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/baseSpeedInMetersPerSecond"></a>
<a class="token" href="#/s:7heresdk16DynamicSpeedInfoV04baseC17InMetersPerSecondSdvp">baseSpeedInMetersPerSecond</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The speed in meters per second without taking traffic into consideration.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">baseSpeedInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16DynamicSpeedInfoV07trafficC17InMetersPerSecondSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/trafficSpeedInMetersPerSecond"></a>
<a class="token" href="#/s:7heresdk16DynamicSpeedInfoV07trafficC17InMetersPerSecondSdvp">trafficSpeedInMetersPerSecond</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The speed in meters per second considering traffic.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">trafficSpeedInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16DynamicSpeedInfoV17turnTimeInSecondss5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/turnTimeInSeconds"></a>
<a class="token" href="#/s:7heresdk16DynamicSpeedInfoV17turnTimeInSecondss5Int32Vvp">turnTimeInSeconds</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The time it takes to make a turn, represented in seconds.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">turnTimeInSeconds</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16DynamicSpeedInfoV04baseC17InMetersPerSecond07trafficcfghI008turnTimeF7SecondsACSd_Sds5Int32Vtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(baseSpeedInMetersPerSecond:trafficSpeedInMetersPerSecond:turnTimeInSeconds:)"></a>
<a class="token" href="#/s:7heresdk16DynamicSpeedInfoV04baseC17InMetersPerSecond07trafficcfghI008turnTimeF7SecondsACSd_Sds5Int32Vtcfc">init(baseSpeedInMetersPerSecond:<wbr/>trafficSpeedInMetersPerSecond:<wbr/>turnTimeInSeconds:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">baseSpeedInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span><span class="p">,</span> <span class="nv">trafficSpeedInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span><span class="p">,</span> <span class="nv">turnTimeInSeconds</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">)</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16DynamicSpeedInfoV18calculateJamFactorSdyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/calculateJamFactor()"></a>
<a class="token" href="#/s:7heresdk16DynamicSpeedInfoV18calculateJamFactorSdyF">calculateJamFactor()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Calculates the traffic jam factor that shows the traffic condition in a numeric way.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">calculateJamFactor</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="kt">Double</span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>Returns calculated jam factor in the range [0.0, 10.0].
A large jamFactor value means more traffic jam in general.
Specifically, 0.0 means free traffic and 10.0 means stationary traffic.</p>
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
