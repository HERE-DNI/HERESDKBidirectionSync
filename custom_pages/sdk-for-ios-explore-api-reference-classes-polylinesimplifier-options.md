---
title: "Options"
slug: "sdk-for-ios-explore-api-reference-classes-polylinesimplifier-options"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/Options"></a>
<a title="Options Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>

<a href="sdk-for-ios-explore-api-reference-core">Core</a>

<a href="sdk-for-ios-explore-api-reference-classes-polylinesimplifier">PolylineSimplifier</a>

        Options Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>Options</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">Options</span></code></pre>
</div>
</div>
<p>Controls the strategy of <code><a href="../../Classes/PolylineSimplifier.html#/s:7heresdk18PolylineSimplifierC8simplify8polyline24simplificationParameters10completionAA10TaskHandle_pSayAA14GeoCoordinatesVG_AC7OptionsVyAA0B19SimplificationErrorOSg_AKSgtctF">PolylineSimplifier.simplify(...)</a></code>
when reducing a size of polyline.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18PolylineSimplifierC7OptionsV33simplificationInMeters14ZoomLevels6UInt64VvpZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Variable/simplificationInMeters14ZoomLevel"></a>
<a class="token" href="#/s:7heresdk18PolylineSimplifierC7OptionsV33simplificationInMeters14ZoomLevels6UInt64VvpZ">simplificationInMeters14ZoomLevel</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Value for simplification tolerance for 14 zoom level without significant artifacts.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="k">let</span> <span class="nv">simplificationInMeters14ZoomLevel</span><span class="p">:</span> <span class="kt">UInt64</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18PolylineSimplifierC7OptionsV9maxPointss6UInt64Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maxPoints"></a>
<a class="token" href="#/s:7heresdk18PolylineSimplifierC7OptionsV9maxPointss6UInt64Vvp">maxPoints</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the upper limit on the resulting collection for
the <code><a href="../../Classes/PolylineSimplifier.html#/s:7heresdk18PolylineSimplifierC8simplify8polyline24simplificationParameters10completionAA10TaskHandle_pSayAA14GeoCoordinatesVG_AC7OptionsVyAA0B19SimplificationErrorOSg_AKSgtctF">PolylineSimplifier.simplify(...)</a></code>. Lower
value results in the lower accuracy of the resulting
polyline. If <code>maxPoints</code> is less than <code>2</code>
then resulting polyline will not have an upper limit
on the size and only <code><a href="../../Classes/PolylineSimplifier/Options.html#/s:7heresdk18PolylineSimplifierC7OptionsV31simplificationToleranceInMeterss6UInt64Vvp">PolylineSimplifier.Options.simplificationToleranceInMeters</a></code>
will be considered. When <code>maxPoints</code> is greater than
size of the passed polyline then simplification algorithm
will take into account only <code><a href="../../Classes/PolylineSimplifier/Options.html#/s:7heresdk18PolylineSimplifierC7OptionsV31simplificationToleranceInMeterss6UInt64Vvp">PolylineSimplifier.Options.simplificationToleranceInMeters</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">maxPoints</span><span class="p">:</span> <span class="kt">UInt64</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18PolylineSimplifierC7OptionsV31simplificationToleranceInMeterss6UInt64Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/simplificationToleranceInMeters"></a>
<a class="token" href="#/s:7heresdk18PolylineSimplifierC7OptionsV31simplificationToleranceInMeterss6UInt64Vvp">simplificationToleranceInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the accuracy limit for the <code><a href="../../Classes/PolylineSimplifier.html#/s:7heresdk18PolylineSimplifierC8simplify8polyline24simplificationParameters10completionAA10TaskHandle_pSayAA14GeoCoordinatesVG_AC7OptionsVyAA0B19SimplificationErrorOSg_AKSgtctF">PolylineSimplifier.simplify(...)</a></code>:</p>
<ul>
<li>higher tolerance results in more simplification (fewer points);</li>
<li>lower tolerance keeps the line closer to its original shape.</li>
</ul>
<p>If removing a point produces polyline, which deviates from the
original one more than <code>simplificationToleranceInMeters</code>, then
this point is left in the collection.</p>
<p>If specified tolerance will not allow to create a polyline
conforming to <code><a href="../../Classes/PolylineSimplifier/Options.html#/s:7heresdk18PolylineSimplifierC7OptionsV9maxPointss6UInt64Vvp">PolylineSimplifier.Options.maxPoints</a></code>, then <code>simplificationToleranceInMeters</code>
is ignored.</p>
<p>Default value is equal to <code><a href="../../Classes/PolylineSimplifier/Options.html#/s:7heresdk18PolylineSimplifierC7OptionsV33simplificationInMeters14ZoomLevels6UInt64VvpZ">PolylineSimplifier.Options.simplificationInMeters14ZoomLevel</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">simplificationToleranceInMeters</span><span class="p">:</span> <span class="kt">UInt64</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18PolylineSimplifierC7OptionsV9maxPoints31simplificationToleranceInMetersAEs6UInt64V_AItcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(maxPoints:simplificationToleranceInMeters:)"></a>
<a class="token" href="#/s:7heresdk18PolylineSimplifierC7OptionsV9maxPoints31simplificationToleranceInMetersAEs6UInt64V_AItcfc">init(maxPoints:<wbr/>simplificationToleranceInMeters:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Undocumented</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">maxPoints</span><span class="p">:</span> <span class="kt">UInt64</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nv">simplificationToleranceInMeters</span><span class="p">:</span> <span class="kt">UInt64</span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-polylinesimplifier">PolylineSimplifier</a></span><span class="o">.</span><span class="kt">Options</span><span class="o">.</span><span class="n"><a href="../../Classes/PolylineSimplifier/Options.html#/s:7heresdk18PolylineSimplifierC7OptionsV33simplificationInMeters14ZoomLevels6UInt64VvpZ">simplificationInMeters14ZoomLevel</a></span><span class="p">)</span></code></pre>
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
