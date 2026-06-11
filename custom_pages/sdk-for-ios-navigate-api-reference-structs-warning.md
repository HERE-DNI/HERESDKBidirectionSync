---
title: "sdk-for-ios-navigate-api-reference-structs-warning"
slug: "sdk-for-ios-navigate-api-reference-structs-warning"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/Warning"></a>
<a title="Warning Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-warnerengine">WarnerEngine</a>
<img alt="" id="carat" src="/carat.png"/>
        Warning Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>Warning</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">Warning</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>A struct which represents a warning.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7WarningV2ids5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/id"></a>
<a class="token" href="#/s:7heresdk7WarningV2ids5Int32Vvp">id</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Identifier of the warning.
The ID is unique only within its specific <code><a href="../Structs/Warning.html#/s:7heresdk7WarningV11warningTypeAA0bD0Ovp">warningType</a></code> and can be used
to retrieve additional information from a corresponding registry.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">id</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7WarningV12distanceTypeAA08DistanceD0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/distanceType"></a>
<a class="token" href="#/s:7heresdk7WarningV12distanceTypeAA08DistanceD0Ovp">distanceType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The type of distance measurement used for this warning.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">distanceType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-distancetype">DistanceType</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7WarningV11warningTypeAA0bD0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/warningType"></a>
<a class="token" href="#/s:7heresdk7WarningV11warningTypeAA0bD0Ovp">warningType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The specific type of the warning.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">warningType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-warningtype">WarningType</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7WarningV06customB4Types5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/customWarningType"></a>
<a class="token" href="#/s:7heresdk7WarningV06customB4Types5Int32VSgvp">customWarningType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Identifier of the custom warning type.</p>
<p>Defines the category of the custom warning and determines which warning
registry should be used to retrieve additional warning details.
This field is set only when <code>warningType == WarningType.CUSTOM</code> and is
<code>nil</code> for all other warning types.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">customWarningType</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7WarningV2id12distanceType07warningE006custombE0ACs5Int32V_AA08DistanceE0OAA0bE0OAISgtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(id:distanceType:warningType:customWarningType:)"></a>
<a class="token" href="#/s:7heresdk7WarningV2id12distanceType07warningE006custombE0ACs5Int32V_AA08DistanceE0OAA0bE0OAISgtcfc">init(id:<wbr/>distanceType:<wbr/>warningType:<wbr/>customWarningType:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance.</p>
<ul>
<li><p>Parameters</p>
<ul>
<li>id: Identifier of the warning.
The ID is unique only within its specific <code><a href="../Structs/Warning.html#/s:7heresdk7WarningV11warningTypeAA0bD0Ovp">warningType</a></code> and can be used
to retrieve additional information from a corresponding registry.</li>
<li>distanceType: The type of distance measurement used for this warning.</li>
<li>warningType: The specific type of the warning.</li>
<li>customWarningType: Identifier of the custom warning type.</li>
</ul>
<p>Defines the category of the custom warning and determines which warning
  registry should be used to retrieve additional warning details.
  This field is set only when <code>warningType == WarningType.CUSTOM</code> and is
  <code>nil</code> for all other warning types.</p></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">id</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">,</span> <span class="nv">distanceType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-distancetype">DistanceType</a></span><span class="p">,</span> <span class="nv">warningType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-warningtype">WarningType</a></span><span class="p">,</span> <span class="nv">customWarningType</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
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
