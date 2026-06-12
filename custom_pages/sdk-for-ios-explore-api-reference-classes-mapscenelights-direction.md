---
title: "Direction"
slug: "sdk-for-ios-explore-api-reference-classes-mapscenelights-direction"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/Direction"></a>
<a title="Direction Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>

<a href="sdk-for-ios-explore-api-reference-maps">Maps</a>

<a href="sdk-for-ios-explore-api-reference-classes-mapscenelights">MapSceneLights</a>

        Direction Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>Direction</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">Direction</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>The direction of lights as a pair of azimuth and altitude angles.
See <a href="https://en.wikipedia.org/wiki/Horizontal_coordinate_system">https://en.wikipedia.org/wiki/Horizontal_coordinate_system</a></p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14MapSceneLightsC9DirectionV7azimuthSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/azimuth"></a>
<a class="token" href="#/s:7heresdk14MapSceneLightsC9DirectionV7azimuthSdvp">azimuth</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Direction azimuth value in degrees in the range [0, 360).
The default value is 0.0.
The azimuth range is half-open, meaning the maximum value is not included in the range.
If the azimuth value falls outside the range, it is wrapped to stay within [0, 360).
Specifically, values less than 0 will be increased by 360 until they fall within the range,
and values greater than or equal to 360 will be reduced by 360 until they fall within the range.
By convention, an azimuth of 0 degrees corresponds to North, and azimuth values increase clockwise.
Thus, 90 degrees corresponds to East, 180 degrees to South, and 270 degrees to West.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">azimuth</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14MapSceneLightsC9DirectionV8altitudeSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/altitude"></a>
<a class="token" href="#/s:7heresdk14MapSceneLightsC9DirectionV8altitudeSdvp">altitude</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Direction altitude value in degrees in the range [0, 90].
The default value is 0.0.
The altitude value is clamped to this range.
If the value falls outside its supported range, it will be adjusted to stay within the range.
Specifically, values less than 0 will be set to 0, and values greater than 90 will be set to 90.
Note: Unlike azimuth, altitude values are not wrapped around; they are clamped directly.
For example, an altitude value of -10 will be adjusted to 0, and an altitude value of 100 will be adjusted to 90.
When both azimuth and altitude values are provided, they are adjusted independently:
For instance, (0, -10) is changed to (0, 0) rather than (180, 10).</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">altitude</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14MapSceneLightsC9DirectionV7azimuth8altitudeAESd_Sdtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(azimuth:altitude:)"></a>
<a class="token" href="#/s:7heresdk14MapSceneLightsC9DirectionV7azimuth8altitudeAESd_Sdtcfc">init(azimuth:<wbr/>altitude:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">azimuth</span><span class="p">:</span> <span class="kt">Double</span> <span class="o">=</span> <span class="mf">0.0</span><span class="p">,</span> <span class="nv">altitude</span><span class="p">:</span> <span class="kt">Double</span> <span class="o">=</span> <span class="mf">0.0</span><span class="p">)</span></code></pre>
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
