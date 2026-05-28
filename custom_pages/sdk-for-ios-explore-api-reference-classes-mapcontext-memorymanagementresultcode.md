---
title: "MapContext / MemoryManagementResultCode"
slug: "sdk-for-ios-explore-api-reference-classes-mapcontext-memorymanagementresultcode"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Enum/MemoryManagementResultCode"></a>
<a title="MemoryManagementResultCode Enumeration Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-..-index">heresdk</a>
<img alt="" id="carat" src="../../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-..-maps">Maps</a>
<img alt="" id="carat" src="../../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-..-classes-mapcontext">MapContext</a>
<img alt="" id="carat" src="../../img/carat.png"/>
        MemoryManagementResultCode Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>MemoryManagementResultCode</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">MemoryManagementResultCode</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
<p>The memory management result code.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10MapContextC26MemoryManagementResultCodeO7appliedyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/applied"></a>
<a class="token" href="#/s:7heresdk10MapContextC26MemoryManagementResultCodeO7appliedyA2EmF">applied</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The memory management options were successfully applied.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">applied</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10MapContextC26MemoryManagementResultCodeO012tileCacheCpuD13LimitExceededyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/tileCacheCpuMemoryLimitExceeded"></a>
<a class="token" href="#/s:7heresdk10MapContextC26MemoryManagementResultCodeO012tileCacheCpuD13LimitExceededyA2EmF">tileCacheCpuMemoryLimitExceeded</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The requested memory limit exceeds the maximum allowed limit for CPU tile cache.
Previous value of CPU tile cache limit is preserved.
Video memory limit applied correctly.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">tileCacheCpuMemoryLimitExceeded</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10MapContextC26MemoryManagementResultCodeO05videoD13LimitExceededyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/videoMemoryLimitExceeded"></a>
<a class="token" href="#/s:7heresdk10MapContextC26MemoryManagementResultCodeO05videoD13LimitExceededyA2EmF">videoMemoryLimitExceeded</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The requested memory limit exceeds the maximum allowed limit for video memory.
Previous value of video memory limit is preserved.
CPU tile cache limit applied correctly.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">videoMemoryLimitExceeded</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10MapContextC26MemoryManagementResultCodeO010failedBothD14LimitsExceededyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/failedBothMemoryLimitsExceeded"></a>
<a class="token" href="#/s:7heresdk10MapContextC26MemoryManagementResultCodeO010failedBothD14LimitsExceededyA2EmF">failedBothMemoryLimitsExceeded</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Both video memory and CPU tile cache limits were exceeded and limits were not applied.
Previous values of video memory and CPU tile cache limits are preserved.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">failedBothMemoryLimitsExceeded</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10MapContextC26MemoryManagementResultCodeO6failedyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/failed"></a>
<a class="token" href="#/s:7heresdk10MapContextC26MemoryManagementResultCodeO6failedyA2EmF">failed</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The memory management options could not be applied due to other errors.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">failed</span></code></pre>
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
