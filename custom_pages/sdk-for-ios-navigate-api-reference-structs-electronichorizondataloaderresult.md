---
title: "ElectronicHorizonDataLoaderResult"
slug: "sdk-for-ios-navigate-api-reference-structs-electronichorizondataloaderresult"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ElectronicHorizonDataLoaderResult"></a>
<a title="ElectronicHorizonDataLoaderResult Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-electronichorizon">ElectronicHorizon</a>

        ElectronicHorizonDataLoaderResult Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>ElectronicHorizonDataLoaderResult</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ElectronicHorizonDataLoaderResult</span></code></pre>
</div>
</div>
<p>Represents the result of a data loading operation performed by <code><a href="sdk-for-ios-navigate-api-reference-classes-electronichorizondataloader">ElectronicHorizonDataLoader</a></code>.
The result contains either the loaded segment data or an error code.</p>
<p>Note: This is a <strong>beta</strong> release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk33ElectronicHorizonDataLoaderResultV9errorCodeAA0bcde5ErrorH0OSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/errorCode"></a>
<a class="token" href="#/s:7heresdk33ElectronicHorizonDataLoaderResultV9errorCodeAA0bcde5ErrorH0OSgvp">errorCode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The error code if the data could not be loaded, otherwise <code>nil</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">errorCode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-electronichorizondataloadererrorcode">ElectronicHorizonDataLoaderErrorCode</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk33ElectronicHorizonDataLoaderResultV07segmentD0AA07SegmentD0CSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/segmentData"></a>
<a class="token" href="#/s:7heresdk33ElectronicHorizonDataLoaderResultV07segmentD0AA07SegmentD0CSgvp">segmentData</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The loaded segment data if it is available, otherwise <code>nil</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">segmentData</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-segmentdata">SegmentData</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk33ElectronicHorizonDataLoaderResultV9errorCode07segmentD0AcA0bcde5ErrorH0OSg_AA07SegmentD0CSgtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(errorCode:segmentData:)"></a>
<a class="token" href="#/s:7heresdk33ElectronicHorizonDataLoaderResultV9errorCode07segmentD0AcA0bcde5ErrorH0OSg_AA07SegmentD0CSgtcfc">init(errorCode:<wbr/>segmentData:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance.</p>
<p>Offline availability: This property is available online and offline.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">errorCode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-electronichorizondataloadererrorcode">ElectronicHorizonDataLoaderErrorCode</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">segmentData</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-segmentdata">SegmentData</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
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
