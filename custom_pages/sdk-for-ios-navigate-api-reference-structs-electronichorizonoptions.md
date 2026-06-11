---
title: "sdk-for-ios-navigate-api-reference-structs-electronichorizonoptions"
slug: "sdk-for-ios-navigate-api-reference-structs-electronichorizonoptions"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ElectronicHorizonOptions"></a>
<a title="ElectronicHorizonOptions Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-electronichorizon">ElectronicHorizon</a>
<img alt="" id="carat" src="/carat.png"/>
        ElectronicHorizonOptions Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>ElectronicHorizonOptions</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ElectronicHorizonOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Provides options to configure <code><a href="sdk-for-ios-navigate-api-reference-classes-electronichorizonengine">ElectronicHorizonEngine</a></code>.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24ElectronicHorizonOptionsV26lookAheadDistancesInMetersSaySdGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/lookAheadDistancesInMeters"></a>
<a class="token" href="#/s:7heresdk24ElectronicHorizonOptionsV26lookAheadDistancesInMetersSaySdGvp">lookAheadDistancesInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The ordered list of distances that define how far to look ahead in meters when calculating electronic horizon paths.
The first entry of the list is for the most preferred path, the second is for the side paths of the first level,
the third is for the side paths of the second level, and so on. Each entry defines how far ahead the path should be provided.
The valid number of values is from one to ten. Values beyond the tenth entry are removed from the list.
If the list is empty, a single default distance value is used instead.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">lookAheadDistancesInMeters</span><span class="p">:</span> <span class="p">[</span><span class="kt">Double</span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24ElectronicHorizonOptionsV24trailingDistanceInMetersSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/trailingDistanceInMeters"></a>
<a class="token" href="#/s:7heresdk24ElectronicHorizonOptionsV24trailingDistanceInMetersSdvp">trailingDistanceInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The trailing distance of the electronic horizon path in meters.
Segments are removed from the path once they are passed and the distance to them exceeds this value.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">trailingDistanceInMeters</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24ElectronicHorizonOptionsV26lookAheadDistancesInMeters016trailingDistancehI0ACSaySdG_Sdtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(lookAheadDistancesInMeters:trailingDistanceInMeters:)"></a>
<a class="token" href="#/s:7heresdk24ElectronicHorizonOptionsV26lookAheadDistancesInMeters016trailingDistancehI0ACSaySdG_Sdtcfc">init(lookAheadDistancesInMeters:<wbr/>trailingDistanceInMeters:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">lookAheadDistancesInMeters</span><span class="p">:</span> <span class="p">[</span><span class="kt">Double</span><span class="p">],</span> <span class="nv">trailingDistanceInMeters</span><span class="p">:</span> <span class="kt">Double</span><span class="p">)</span></code></pre>
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
