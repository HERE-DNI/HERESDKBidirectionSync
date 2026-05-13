---
title: "MapData / RoadUsages"
slug: "sdk-for-ios-navigate-api-reference-structs-roadusages"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/RoadUsages"></a>
<a title="RoadUsages Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-mapdata">MapData</a>
<img alt="" id="carat" src="../img/carat.png"/>
        RoadUsages Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>RoadUsages</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RoadUsages</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Road Usages of the segment.</p>
<p><strong><em>Note</em></strong> a road can have more than one attribute at the same time.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10RoadUsagesV6isRampSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isRamp"></a>
<a class="token" href="#/s:7heresdk10RoadUsagesV6isRampSbvp">isRamp</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Range is a ramp: connects roads that do not intersect at grade.
Ramp allows explication of maneuvers involving ramps (e.g., “Take the ramp”)
and for route guidance when determining if sign text should be used.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isRamp</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10RoadUsagesV18isControlledAccessSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isControlledAccess"></a>
<a class="token" href="#/s:7heresdk10RoadUsagesV18isControlledAccessSbvp">isControlledAccess</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Controlled access roads are roads with limited entrances and exits
that allow uninterrupted high-speed traffic flow.
For example, the Interstate/Freeway network in the United States or
the Motorway network in Europe.
Controlled Access can be used for map display, avoidance of freeway/motorway,
publishing speed limits, and route guidance timing.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isControlledAccess</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10RoadUsagesV9isTollwaySbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isTollway"></a>
<a class="token" href="#/s:7heresdk10RoadUsagesV9isTollwaySbvp">isTollway</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Identifies a road for which a fee must be paid to use the road.
Tollway may be used for map display (e.g., different rendering of toll roads) and routing.
Tollway is flagged on roads that require a fee for traversal.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isTollway</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10RoadUsagesV010isPriorityB0Sbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isPriorityRoad"></a>
<a class="token" href="#/s:7heresdk10RoadUsagesV010isPriorityB0Sbvp">isPriorityRoad</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates road stretches that have signs indicating priority on the road.
On these roads all traffic has priority over the traffic on the incoming roads.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isPriorityRoad</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10RoadUsagesV6isRamp0D16ControlledAccess0D7Tollway0d8PriorityB0ACSb_S3btcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(isRamp:isControlledAccess:isTollway:isPriorityRoad:)"></a>
<a class="token" href="#/s:7heresdk10RoadUsagesV6isRamp0D16ControlledAccess0D7Tollway0d8PriorityB0ACSb_S3btcfc">init(isRamp:<wbr/>isControlledAccess:<wbr/>isTollway:<wbr/>isPriorityRoad:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance with default values.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">isRamp</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">isControlledAccess</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">isTollway</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">isPriorityRoad</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">)</span></code></pre>
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
