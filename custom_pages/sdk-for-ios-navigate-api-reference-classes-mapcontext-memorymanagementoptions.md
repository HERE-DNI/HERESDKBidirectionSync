---
title: "MemoryManagementOptions"
slug: "sdk-for-ios-navigate-api-reference-classes-mapcontext-memorymanagementoptions"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/MemoryManagementOptions"></a>
<a title="MemoryManagementOptions Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-maps">Maps</a>

<a href="sdk-for-ios-navigate-api-reference-classes-mapcontext">MapContext</a>

        MemoryManagementOptions Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>MemoryManagementOptions</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">MemoryManagementOptions</span></code></pre>
</div>
</div>
<p>Memory management options.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10MapContextC23MemoryManagementOptionsV06memoryE8StrategyAC0deH0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/memoryManagementStrategy"></a>
<a class="token" href="#/s:7heresdk10MapContextC23MemoryManagementOptionsV06memoryE8StrategyAC0deH0Ovp">memoryManagementStrategy</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The default setting MemoryManagementStrategy.DYNAMIC is suitable for common cases. The map
data cache can adjust dynamically to fit visible data. When the visible data needs extra
memory, it would increase. When it’s not needed, it will reduce to a limit which is
calculated internally or by using <code><a href="../../Classes/MapContext/MemoryManagementOptions.html#/s:7heresdk10MapContextC23MemoryManagementOptionsV09tileCacheD10LimitInKiBs5Int32VSgvp">MapContext.MemoryManagementOptions.tileCacheMemoryLimitInKiB</a></code> option.
The MemoryManagementStrategy.FIXED would be only useful when there is very
strict memory consumption requirement for the application. It potentially can have
flickering visual artifacts when the map data to be visualized is very large and exceeds
the cache limit.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">memoryManagementStrategy</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapcontext">MapContext</a></span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapcontext-memorymanagementstrategy">MemoryManagementStrategy</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10MapContextC23MemoryManagementOptionsV09tileCacheD10LimitInKiBs5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/tileCacheMemoryLimitInKiB"></a>
<a class="token" href="#/s:7heresdk10MapContextC23MemoryManagementOptionsV09tileCacheD10LimitInKiBs5Int32VSgvp">tileCacheMemoryLimitInKiB</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Tile cache memory limit in kibibytes. Non positive or <code>nil</code> values are ignored.
Default value is <code>nil</code>.
Low tile cache limit will lead to eviction of tiles only if MemoryManagementStrategy is set to FIXED.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">tileCacheMemoryLimitInKiB</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10MapContextC23MemoryManagementOptionsV05videoD10LimitInKiBs5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/videoMemoryLimitInKiB"></a>
<a class="token" href="#/s:7heresdk10MapContextC23MemoryManagementOptionsV05videoD10LimitInKiBs5Int32VSgvp">videoMemoryLimitInKiB</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Target video memory limit in kibibytes. Non positive or <code>nil</code> values are ignored.
Default value is <code>nil</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">videoMemoryLimitInKiB</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10MapContextC23MemoryManagementOptionsV06memoryE8Strategy09tileCacheD10LimitInKiB05videodklM1BAeC0deH0O_s5Int32VSgAMtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(memoryManagementStrategy:tileCacheMemoryLimitInKiB:videoMemoryLimitInKiB:)"></a>
<a class="token" href="#/s:7heresdk10MapContextC23MemoryManagementOptionsV06memoryE8Strategy09tileCacheD10LimitInKiB05videodklM1BAeC0deH0O_s5Int32VSgAMtcfc">init(memoryManagementStrategy:<wbr/>tileCacheMemoryLimitInKiB:<wbr/>videoMemoryLimitInKiB:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">memoryManagementStrategy</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapcontext">MapContext</a></span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapcontext-memorymanagementstrategy">MemoryManagementStrategy</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapcontext">MapContext</a></span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapcontext-memorymanagementstrategy">MemoryManagementStrategy</a></span><span class="o">.</span><span class="kd">dynamic</span><span class="p">,</span> <span class="nv">tileCacheMemoryLimitInKiB</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">videoMemoryLimitInKiB</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
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
