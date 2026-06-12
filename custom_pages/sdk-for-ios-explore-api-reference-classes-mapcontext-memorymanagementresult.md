---
title: "MemoryManagementResult"
slug: "sdk-for-ios-explore-api-reference-classes-mapcontext-memorymanagementresult"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/MemoryManagementResult"></a>
<a title="MemoryManagementResult Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>

<a href="sdk-for-ios-explore-api-reference-maps">Maps</a>

<a href="sdk-for-ios-explore-api-reference-classes-mapcontext">MapContext</a>

        MemoryManagementResult Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>MemoryManagementResult</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">MemoryManagementResult</span></code></pre>
</div>
</div>
<p>Memory management result.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10MapContextC22MemoryManagementResultV016diffBetweenVideoD24LimitAndRequirementInKiBs5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/diffBetweenVideoMemoryLimitAndRequirementInKiB"></a>
<a class="token" href="#/s:7heresdk10MapContextC22MemoryManagementResultV016diffBetweenVideoD24LimitAndRequirementInKiBs5Int32VSgvp">diffBetweenVideoMemoryLimitAndRequirementInKiB</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The difference in kibibytes between the limit and the video-memory requirement
for only the currently visible data. If positive, the returned value is the surplus
value over the currently required bare minimum. Even when positive, if the limit set
is low, the application could later breach the limit and delete even visible data.
A non positive value means the limit cannot fit the existing visible data and there could
be data disappearing or flickering. If for some reason the callback is ignored or
correct memory limit cannot be calculated, <code>nil</code> value is returned.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">diffBetweenVideoMemoryLimitAndRequirementInKiB</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10MapContextC22MemoryManagementResultV10resultCodeAC0defH0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/resultCode"></a>
<a class="token" href="#/s:7heresdk10MapContextC22MemoryManagementResultV10resultCodeAC0defH0Ovp">resultCode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The result code of the memory management request.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">resultCode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-mapcontext">MapContext</a></span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-mapcontext-memorymanagementresultcode">MemoryManagementResultCode</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10MapContextC22MemoryManagementResultV016diffBetweenVideoD24LimitAndRequirementInKiB10resultCodeAEs5Int32VSg_AC0defP0Otcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(diffBetweenVideoMemoryLimitAndRequirementInKiB:resultCode:)"></a>
<a class="token" href="#/s:7heresdk10MapContextC22MemoryManagementResultV016diffBetweenVideoD24LimitAndRequirementInKiB10resultCodeAEs5Int32VSg_AC0defP0Otcfc">init(diffBetweenVideoMemoryLimitAndRequirementInKiB:<wbr/>resultCode:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">diffBetweenVideoMemoryLimitAndRequirementInKiB</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">resultCode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-mapcontext">MapContext</a></span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-mapcontext-memorymanagementresultcode">MemoryManagementResultCode</a></span><span class="p">)</span></code></pre>
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
