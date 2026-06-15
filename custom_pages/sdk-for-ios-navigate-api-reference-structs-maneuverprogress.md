---
title: "ManeuverProgress"
slug: "sdk-for-ios-navigate-api-reference-structs-maneuverprogress"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ManeuverProgress"></a>
<a title="ManeuverProgress Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-navigation">Navigation</a>

        ManeuverProgress Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>ManeuverProgress</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ManeuverProgress</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Indicates a user’s progress to a <code><a href="sdk-for-ios-navigate-api-reference-classes-maneuver">Maneuver</a></code>.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16ManeuverProgressV13maneuverIndexs5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maneuverIndex"></a>
<a class="token" href="#/s:7heresdk16ManeuverProgressV13maneuverIndexs5Int32Vvp">maneuverIndex</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Index of the <code><a href="sdk-for-ios-navigate-api-reference-classes-maneuver">Maneuver</a></code> being traversed along the route.
Defaults to 0.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">maneuverIndex</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16ManeuverProgressV25remainingDistanceInMeterss5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/remainingDistanceInMeters"></a>
<a class="token" href="#/s:7heresdk16ManeuverProgressV25remainingDistanceInMeterss5Int32Vvp">remainingDistanceInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The distance in meters from current location until the <code><a href="sdk-for-ios-navigate-api-reference-classes-maneuver">Maneuver</a></code>.
Defaults to 0.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">remainingDistanceInMeters</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16ManeuverProgressV17remainingDurationSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/remainingDuration"></a>
<a class="token" href="#/s:7heresdk16ManeuverProgressV17remainingDurationSdvp">remainingDuration</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The estimated time in seconds for traversing the <code><a href="sdk-for-ios-navigate-api-reference-classes-section">Section</a></code>
from current location until the <code><a href="sdk-for-ios-navigate-api-reference-classes-maneuver">Maneuver</a></code> is reached,
including traffic delays if available.
Defaults to 0 seconds.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">remainingDuration</span><span class="p">:</span> <span class="kt">TimeInterval</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16ManeuverProgressV13maneuverIndex25remainingDistanceInMeters0F8DurationACs5Int32V_AHSdtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(maneuverIndex:remainingDistanceInMeters:remainingDuration:)"></a>
<a class="token" href="#/s:7heresdk16ManeuverProgressV13maneuverIndex25remainingDistanceInMeters0F8DurationACs5Int32V_AHSdtcfc">init(maneuverIndex:<wbr/>remainingDistanceInMeters:<wbr/>remainingDuration:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">maneuverIndex</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nv">remainingDistanceInMeters</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nv">remainingDuration</span><span class="p">:</span> <span class="kt">TimeInterval</span> <span class="o">=</span> <span class="mi">0</span><span class="p">)</span></code></pre>
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
