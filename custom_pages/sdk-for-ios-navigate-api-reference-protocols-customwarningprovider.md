---
title: "Untitled"
slug: "sdk-for-ios-navigate-api-reference-protocols-customwarningprovider"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- CustomWarningProvider.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/CustomWarningProvider"></a>
<a title="CustomWarningProvider Protocol Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-warnerengine">WarnerEngine</a>
<img alt="" id="carat" src="../img/carat.png"/>
        CustomWarningProvider Protocol Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>CustomWarningProvider</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">CustomWarningProvider</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
<p>A protocol representing a provider of custom warnings based on vehicle position.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21CustomWarningProviderP03getbC4Types5Int32VyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getCustomWarningType()"></a>
<a class="token" href="#/s:7heresdk21CustomWarningProviderP03getbC4Types5Int32VyF">getCustomWarningType()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Returns the custom warning type identifier produced by this provider.</p>
<p>The returned value corresponds to <code><a href="../Structs/CustomWarning.html#/s:7heresdk13CustomWarningV06customC4Types5Int32Vvp">CustomWarning.customWarningType</a></code> and
<code><a href="../Structs/Warning.html#/s:7heresdk7WarningV06customB4Types5Int32VSgvp">Warning.customWarningType</a></code> and is used to apply per-type configuration,
such as notification distances.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">getCustomWarningType</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>The custom warning type identifier for this provider.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21CustomWarningProviderP11getWarnings14currentSegment08previousH0SayAA0bC0VGAA0H4DataC_AKSgtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getWarnings(currentSegment:previousSegment:)"></a>
<a class="token" href="#/s:7heresdk21CustomWarningProviderP11getWarnings14currentSegment08previousH0SayAA0bC0VGAA0H4DataC_AKSgtF">getWarnings(currentSegment:<wbr/>previousSegment:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Returns a list of custom warnings for the given vehicle position.</p>
<p>This method evaluates the custom warning provider using the current
vehicle position on the electronic horizon and returns the resulting
custom warnings along with corresponding payload.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">getWarnings</span><span class="p">(</span><span class="nv">currentSegment</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-segmentdata">SegmentData</a></span><span class="p">,</span> <span class="nv">previousSegment</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-segmentdata">SegmentData</a></span><span class="p">?)</span> <span class="o">-&gt;</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-customwarning">CustomWarning</a></span><span class="p">]</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>currentSegment</em>
</code>
</td>
<td>
<div>
<p>Segment data representing the vehicle’s current
position on the electronic horizon.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>previousSegment</em>
</code>
</td>
<td>
<div>
<p>Segment data representing the vehicle’s previous
position on the electronic horizon. This parameter may be null if no
previous position information is available.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>A list of <code><a href="sdk-for-ios-navigate-api-reference-..-structs-customwarning">CustomWarning</a></code> instances representing all applicable
custom warnings. The list may be empty if no warnings apply.</p>
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

</div>
`
}</HTMLBlock>
