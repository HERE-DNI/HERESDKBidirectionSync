---
title: "MemoryManagementResult Structure Reference"
slug: "sdk-for-ios-explore-api-reference-classes-mapcontext-memorymanagementresult"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- MemoryManagementResult.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/MemoryManagementResult"></a>
<a title="MemoryManagementResult Structure Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="sdk-for-ios-explore-api-reference-..-..-index">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-..-index">heresdk</a>
<img alt="" id="carat" src="../../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-..-maps">Maps</a>
<img alt="" id="carat" src="../../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-..-classes-mapcontext">MapContext</a>
<img alt="" id="carat" src="../../img/carat.png"/>
        MemoryManagementResult Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct MemoryManagementResult</code></pre>
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
<pre><code>public var diffBetweenVideoMemoryLimitAndRequirementInKiB: Int32?</code></pre>
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
<pre><code>public var resultCode: MapContext.MemoryManagementResultCode</code></pre>
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
<pre><code>public init(diffBetweenVideoMemoryLimitAndRequirementInKiB: Int32? = nil, resultCode: MapContext.MemoryManagementResultCode)</code></pre>
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
