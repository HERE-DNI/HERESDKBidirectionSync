---
title: "Untitled"
slug: "sdk-for-ios-navigate-api-reference-structs-railwaycrossing"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- RailwayCrossing.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/RailwayCrossing"></a>
<a title="RailwayCrossing Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-mapdata">MapData</a>
<img alt="" id="carat" src="../img/carat.png"/>
        RailwayCrossing Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>RailwayCrossing</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RailwayCrossing</span></code></pre>
</div>
</div>
<p>Identifies the presence and the location of railway corssings.
Included in <code><a href="sdk-for-ios-navigate-api-reference-..-classes-segmentdata">SegmentData</a></code> only if <code><a href="../Structs/SegmentDataLoaderOptions.html#/s:7heresdk24SegmentDataLoaderOptionsV20loadRailwayCrossingsSbvp">SegmentDataLoaderOptions.loadRailwayCrossings</a></code> is set to <code>true</code>.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15RailwayCrossingV19startOffsetInMeterss5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/startOffsetInMeters"></a>
<a class="token" href="#/s:7heresdk15RailwayCrossingV19startOffsetInMeterss5Int32Vvp">startOffsetInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The start offset, in meters, from the beginning of the segment.</p>
<p>If <code><a href="../Structs/RailwayCrossing.html#/s:7heresdk15RailwayCrossingV17endOffsetInMeterss5Int32Vvp">RailwayCrossing.endOffsetInMeters</a></code> = 0, then <code>RailwayCrossing.startOffsetInMeters</code> approximately indicates a middle of a railway crossing.
If <code><a href="../Structs/RailwayCrossing.html#/s:7heresdk15RailwayCrossingV17endOffsetInMeterss5Int32Vvp">RailwayCrossing.endOffsetInMeters</a></code> &gt; 0, it means crossing consists of several rails, and
<code>RailwayCrossing.startOffsetInMeters</code> and <code><a href="../Structs/RailwayCrossing.html#/s:7heresdk15RailwayCrossingV17endOffsetInMeterss5Int32Vvp">RailwayCrossing.endOffsetInMeters</a></code> indicates starting and ending points of the crossing respectively.
Default value is 0.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">startOffsetInMeters</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15RailwayCrossingV17endOffsetInMeterss5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/endOffsetInMeters"></a>
<a class="token" href="#/s:7heresdk15RailwayCrossingV17endOffsetInMeterss5Int32Vvp">endOffsetInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The end offset, in meters, from the beginning of the segment.
Could be 0. See <code><a href="../Structs/RailwayCrossing.html#/s:7heresdk15RailwayCrossingV19startOffsetInMeterss5Int32Vvp">RailwayCrossing.startOffsetInMeters</a></code> description.
Default value is 0.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">endOffsetInMeters</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15RailwayCrossingV07railwayC4TypeAA0bcE0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/railwayCrossingType"></a>
<a class="token" href="#/s:7heresdk15RailwayCrossingV07railwayC4TypeAA0bcE0Ovp">railwayCrossingType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The type of barrier presented by the railway crossing.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">railwayCrossingType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-railwaycrossingtype">RailwayCrossingType</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15RailwayCrossingV19startOffsetInMeters03endefG007railwayC4TypeACs5Int32V_AhA0bcJ0Otcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(startOffsetInMeters:endOffsetInMeters:railwayCrossingType:)"></a>
<a class="token" href="#/s:7heresdk15RailwayCrossingV19startOffsetInMeters03endefG007railwayC4TypeACs5Int32V_AhA0bcJ0Otcfc">init(startOffsetInMeters:<wbr/>endOffsetInMeters:<wbr/>railwayCrossingType:<wbr/>)</a>
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
<li>startOffsetInMeters: The start offset, in meters, from the beginning of the segment.</li>
</ul>
<p>If <code><a href="../Structs/RailwayCrossing.html#/s:7heresdk15RailwayCrossingV17endOffsetInMeterss5Int32Vvp">RailwayCrossing.endOffsetInMeters</a></code> = 0, then <code><a href="../Structs/RailwayCrossing.html#/s:7heresdk15RailwayCrossingV19startOffsetInMeterss5Int32Vvp">RailwayCrossing.startOffsetInMeters</a></code> approximately indicates a middle of a railway crossing.
  If <code><a href="../Structs/RailwayCrossing.html#/s:7heresdk15RailwayCrossingV17endOffsetInMeterss5Int32Vvp">RailwayCrossing.endOffsetInMeters</a></code> &gt; 0, it means crossing consists of several rails, and
  <code><a href="../Structs/RailwayCrossing.html#/s:7heresdk15RailwayCrossingV19startOffsetInMeterss5Int32Vvp">RailwayCrossing.startOffsetInMeters</a></code> and <code><a href="../Structs/RailwayCrossing.html#/s:7heresdk15RailwayCrossingV17endOffsetInMeterss5Int32Vvp">RailwayCrossing.endOffsetInMeters</a></code> indicates starting and ending points of the crossing respectively.
  Default value is 0.</p>
<ul>
<li>endOffsetInMeters: The end offset, in meters, from the beginning of the segment.
Could be 0. See <code><a href="../Structs/RailwayCrossing.html#/s:7heresdk15RailwayCrossingV19startOffsetInMeterss5Int32Vvp">RailwayCrossing.startOffsetInMeters</a></code> description.
Default value is 0.</li>
<li>railwayCrossingType: The type of barrier presented by the railway crossing.</li>
</ul></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">startOffsetInMeters</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nv">endOffsetInMeters</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nv">railwayCrossingType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-railwaycrossingtype">RailwayCrossingType</a></span><span class="p">)</span></code></pre>
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

</div>
`
}</HTMLBlock>
