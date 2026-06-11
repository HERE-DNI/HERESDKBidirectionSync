---
title: "RouteProgressColors"
slug: "sdk-for-ios-navigate-api-reference-structs-routeprogresscolors"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/RouteProgressColors"></a>
<a title="RouteProgressColors Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-navigation">Navigation</a>

        RouteProgressColors Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>RouteProgressColors</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RouteProgressColors</span></code></pre>
</div>
</div>
<p>This struct contains colors for the route progress visualization.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19RouteProgressColorsV5aheadSo7UIColorCvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/ahead"></a>
<a class="token" href="#/s:7heresdk19RouteProgressColorsV5aheadSo7UIColorCvp">ahead</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Color of the route part that lies ahead of the current location.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">ahead</span><span class="p">:</span> <span class="kt">UIColor</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19RouteProgressColorsV6behindSo7UIColorCvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/behind"></a>
<a class="token" href="#/s:7heresdk19RouteProgressColorsV6behindSo7UIColorCvp">behind</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Color of the route part that lies behind of the current location.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">behind</span><span class="p">:</span> <span class="kt">UIColor</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19RouteProgressColorsV7offRoadSo7UIColorCvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/offRoad"></a>
<a class="token" href="#/s:7heresdk19RouteProgressColorsV7offRoadSo7UIColorCvp">offRoad</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Color of the dashed line between the map-matched and the off-road destinations.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">offRoad</span><span class="p">:</span> <span class="kt">UIColor</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19RouteProgressColorsV12outlineAheadSo7UIColorCvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/outlineAhead"></a>
<a class="token" href="#/s:7heresdk19RouteProgressColorsV12outlineAheadSo7UIColorCvp">outlineAhead</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Outline color of the route part that lies ahead of the current location.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">outlineAhead</span><span class="p">:</span> <span class="kt">UIColor</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19RouteProgressColorsV13outlineBehindSo7UIColorCvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/outlineBehind"></a>
<a class="token" href="#/s:7heresdk19RouteProgressColorsV13outlineBehindSo7UIColorCvp">outlineBehind</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Outline color of the route part that lies behind of the current location.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">outlineBehind</span><span class="p">:</span> <span class="kt">UIColor</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19RouteProgressColorsV5ahead6behind7offRoad12outlineAhead0I6BehindACSo7UIColorC_A4Jtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(ahead:behind:offRoad:outlineAhead:outlineBehind:)"></a>
<a class="token" href="#/s:7heresdk19RouteProgressColorsV5ahead6behind7offRoad12outlineAhead0I6BehindACSo7UIColorC_A4Jtcfc">init(ahead:<wbr/>behind:<wbr/>offRoad:<wbr/>outlineAhead:<wbr/>outlineBehind:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">ahead</span><span class="p">:</span> <span class="kt">UIColor</span><span class="p">,</span> <span class="nv">behind</span><span class="p">:</span> <span class="kt">UIColor</span><span class="p">,</span> <span class="nv">offRoad</span><span class="p">:</span> <span class="kt">UIColor</span> <span class="o">=</span> <span class="kt">NamedColor</span><span class="o">.</span><span class="n">white</span><span class="p">,</span> <span class="nv">outlineAhead</span><span class="p">:</span> <span class="kt">UIColor</span><span class="p">,</span> <span class="nv">outlineBehind</span><span class="p">:</span> <span class="kt">UIColor</span><span class="p">)</span></code></pre>
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
