---
title: "MapData / SegmentReferenceConverter"
slug: "sdk-for-ios-navigate-api-reference-classes-segmentreferenceconverter"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/SegmentReferenceConverter"></a>
<a title="SegmentReferenceConverter Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-mapdata">MapData</a>
<img alt="" id="carat" src="../img/carat.png"/>
        SegmentReferenceConverter Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>SegmentReferenceConverter</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">SegmentReferenceConverter</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">SegmentReferenceConverter</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">SegmentReferenceConverter</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>A SegmentReferenceConverter provides possibility to convert mapmatched instances of
<code><a href="sdk-for-ios-navigate-api-reference-..-structs-segmentreference">SegmentReference</a></code> to corresponding instances of <code><a href="sdk-for-ios-navigate-api-reference-..-structs-directedocmsegmentid">DirectedOCMSegmentId</a></code>.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25SegmentReferenceConverterC9sdkEngineAcA09SDKNativeF0C_tKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(sdkEngine:)"></a>
<a class="token" href="#/s:7heresdk25SegmentReferenceConverterC9sdkEngineAcA09SDKNativeF0C_tKcfc">init(sdkEngine:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of this class.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> Indicates what went wrong when the instantiation was attempted.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">sdkEngine</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-sdknativeengine">SDKNativeEngine</a></span><span class="p">)</span> <span class="k">throws</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>sdkEngine</em>
</code>
</td>
<td>
<div>
<p>A SDKEngine instance.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25SegmentReferenceConverterC15getOCMSegmentId07segmentC0AA08DirectedfG0VSgAA0bC0V_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getOCMSegmentId(segmentReference:)"></a>
<a class="token" href="#/s:7heresdk25SegmentReferenceConverterC15getOCMSegmentId07segmentC0AA08DirectedfG0VSgAA0bC0V_tF">getOCMSegmentId(segmentReference:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The <code><a href="sdk-for-ios-navigate-api-reference-..-structs-directedocmsegmentid">DirectedOCMSegmentId</a></code> for provided <code><a href="sdk-for-ios-navigate-api-reference-..-structs-segmentreference">SegmentReference</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getOCMSegmentId</span><span class="p">(</span><span class="nv">segmentReference</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-segmentreference">SegmentReference</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-directedocmsegmentid">DirectedOCMSegmentId</a></span><span class="p">?</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>segmentReference</em>
</code>
</td>
<td>
<div>
<p><code><a href="sdk-for-ios-navigate-api-reference-..-structs-segmentreference">SegmentReference</a></code> to convert.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p><code><a href="sdk-for-ios-navigate-api-reference-..-structs-directedocmsegmentid">DirectedOCMSegmentId</a></code> corresponding to provided <code><a href="sdk-for-ios-navigate-api-reference-..-structs-segmentreference">SegmentReference</a></code>.</p>
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
