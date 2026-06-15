---
title: "CustomWarning"
slug: "sdk-for-ios-navigate-api-reference-structs-customwarning"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/CustomWarning"></a>
<a title="CustomWarning Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-warnerengine">WarnerEngine</a>

        CustomWarning Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>CustomWarning</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">CustomWarning</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>struct container for custom warning data.</p>
<p>This structure represents the type-specific payload associated
with a custom warning.</p>
<p>Instances of this structure are typically produced by custom warning
evaluation logic and may also be retrieved from the <code>WarningRegistry</code>.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13CustomWarningV2ids5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/id"></a>
<a class="token" href="#/s:7heresdk13CustomWarningV2ids5Int32Vvp">id</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Identifier of the warning.
The ID is unique only within its specific <code><a href="../Structs/CustomWarning.html#/s:7heresdk13CustomWarningV06customC4Types5Int32Vvp">CustomWarning.customWarningType</a></code> and can be used
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
<a name="/s:7heresdk13CustomWarningV06customC4Types5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/customWarningType"></a>
<a class="token" href="#/s:7heresdk13CustomWarningV06customC4Types5Int32Vvp">customWarningType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Identifier of the custom warning type.</p>
<p>Defines the category of the custom warning and determines which warning
registry should be used to retrieve additional warning details.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">customWarningType</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13CustomWarningV19startOffsetInMetersSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/startOffsetInMeters"></a>
<a class="token" href="#/s:7heresdk13CustomWarningV19startOffsetInMetersSdvp">startOffsetInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Start offset of the warning range along the segment.</p>
<p>Specifies the distance, in meters, from the beginning of the
corresponding <code><a href="sdk-for-ios-navigate-api-reference-structs-electronichorizonsegment">ElectronicHorizonSegment</a></code> at which the warning becomes
applicable.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">startOffsetInMeters</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13CustomWarningV17endOffsetInMetersSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/endOffsetInMeters"></a>
<a class="token" href="#/s:7heresdk13CustomWarningV17endOffsetInMetersSdSgvp">endOffsetInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>End offset of the warning range along the segment.</p>
<p>Specifies the distance, in meters, from the beginning of the
corresponding <code><a href="sdk-for-ios-navigate-api-reference-structs-electronichorizonsegment">ElectronicHorizonSegment</a></code> at which the warning is no
longer applicable.</p>
<p>May be <code>nil</code>. In this case, the value is automatically considered
to be equal to <code><a href="../Structs/CustomWarning.html#/s:7heresdk13CustomWarningV19startOffsetInMetersSdvp">startOffsetInMeters</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">endOffsetInMeters</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13CustomWarningV7payloadAA8MetadataCSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/payload"></a>
<a class="token" href="#/s:7heresdk13CustomWarningV7payloadAA8MetadataCSgvp">payload</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Custom warning payload.</p>
<p>Contains warning-specific payload data.
A value of <code>nil</code> indicates that no additional data is associated with the warning.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">payload</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-metadata">Metadata</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13CustomWarningV2id06customC4Type19startOffsetInMeters03endhiJ07payloadACs5Int32V_AJS2dSgAA8MetadataCSgtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(id:customWarningType:startOffsetInMeters:endOffsetInMeters:payload:)"></a>
<a class="token" href="#/s:7heresdk13CustomWarningV2id06customC4Type19startOffsetInMeters03endhiJ07payloadACs5Int32V_AJS2dSgAA8MetadataCSgtcfc">init(id:<wbr/>customWarningType:<wbr/>startOffsetInMeters:<wbr/>endOffsetInMeters:<wbr/>payload:<wbr/>)</a>
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
The ID is unique only within its specific <code><a href="../Structs/CustomWarning.html#/s:7heresdk13CustomWarningV06customC4Types5Int32Vvp">CustomWarning.customWarningType</a></code> and can be used
to retrieve additional information from a corresponding registry.</li>
<li>customWarningType: Identifier of the custom warning type.</li>
</ul>
<p>Defines the category of the custom warning and determines which warning
  registry should be used to retrieve additional warning details.</p>
<ul>
<li>startOffsetInMeters: Start offset of the warning range along the segment.</li>
</ul>
<p>Specifies the distance, in meters, from the beginning of the
  corresponding <code><a href="sdk-for-ios-navigate-api-reference-structs-electronichorizonsegment">ElectronicHorizonSegment</a></code> at which the warning becomes
  applicable.</p>
<ul>
<li>endOffsetInMeters: End offset of the warning range along the segment.</li>
</ul>
<p>Specifies the distance, in meters, from the beginning of the
  corresponding <code><a href="sdk-for-ios-navigate-api-reference-structs-electronichorizonsegment">ElectronicHorizonSegment</a></code> at which the warning is no
  longer applicable.</p>
<p>May be <code>nil</code>. In this case, the value is automatically considered
  to be equal to <code><a href="../Structs/CustomWarning.html#/s:7heresdk13CustomWarningV19startOffsetInMetersSdvp">startOffsetInMeters</a></code>.</p>
<ul>
<li>payload: Custom warning payload.</li>
</ul>
<p>Contains warning-specific payload data.
  A value of <code>nil</code> indicates that no additional data is associated with the warning.</p></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">id</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nv">customWarningType</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nv">startOffsetInMeters</span><span class="p">:</span> <span class="kt">Double</span> <span class="o">=</span> <span class="mf">0.0</span><span class="p">,</span> <span class="nv">endOffsetInMeters</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">payload</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-metadata">Metadata</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
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
