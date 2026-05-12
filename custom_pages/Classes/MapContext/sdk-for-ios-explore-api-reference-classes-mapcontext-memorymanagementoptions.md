---
title: "MemoryManagementOptions Structure Reference"
slug: "sdk-for-ios-explore-api-reference-classes-mapcontext-memorymanagementoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- MemoryManagementOptions.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/MemoryManagementOptions"></a>
<a title="MemoryManagementOptions Structure Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="../../index.html">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="../../index.html">heresdk</a>
<img alt="" id="carat" src="../../img/carat.png"/>
<a href="../../Maps.html">Maps</a>
<img alt="" id="carat" src="../../img/carat.png"/>
<a href="../../Classes/MapContext.html">MapContext</a>
<img alt="" id="carat" src="../../img/carat.png"/>
        MemoryManagementOptions Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct MemoryManagementOptions</code></pre>
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
<pre><code>public var memoryManagementStrategy: MapContext.MemoryManagementStrategy</code></pre>
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
<pre><code>public var tileCacheMemoryLimitInKiB: Int32?</code></pre>
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
<pre><code>public var videoMemoryLimitInKiB: Int32?</code></pre>
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
<pre><code>public init(memoryManagementStrategy: MapContext.MemoryManagementStrategy = MapContext.MemoryManagementStrategy.dynamic, tileCacheMemoryLimitInKiB: Int32? = nil, videoMemoryLimitInKiB: Int32? = nil)</code></pre>
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
