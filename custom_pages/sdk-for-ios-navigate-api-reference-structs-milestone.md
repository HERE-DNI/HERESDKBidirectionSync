---
title: "sdk-for-ios-navigate-api-reference-structs-milestone"
slug: "sdk-for-ios-navigate-api-reference-structs-milestone"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/Milestone"></a>
<a title="Milestone Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-navigation">Navigation</a>
<img alt="" id="carat" src="/carat.png"/>
        Milestone Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>Milestone</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">Milestone</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Represents information about the waypoints along the route.</p>
<p>Note that this can include additional waypoints added during route
calculation that may not have been part of the original user-defined
waypoint list. For example, additional waypoints are added automatically
between sections that require a different transport mode like when taking a
ferry.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MilestoneV12sectionIndexs5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/sectionIndex"></a>
<a class="token" href="#/s:7heresdk9MilestoneV12sectionIndexs5Int32Vvp">sectionIndex</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Index of the section on the route.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">sectionIndex</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MilestoneV13waypointIndexs5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/waypointIndex"></a>
<a class="token" href="#/s:7heresdk9MilestoneV13waypointIndexs5Int32VSgvp">waypointIndex</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>If present, this index corresponds to the waypoint in the original
user-defined waypoint list. Otherwise this waypoint was added during
route calculation by the system.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">waypointIndex</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MilestoneV19originalCoordinatesAA03GeoD0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/originalCoordinates"></a>
<a class="token" href="#/s:7heresdk9MilestoneV19originalCoordinatesAA03GeoD0VSgvp">originalCoordinates</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>User-defined geographic coordinates. If not available, this waypoint was
added during route calculation.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">originalCoordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MilestoneV21mapMatchedCoordinatesAA03GeoE0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/mapMatchedCoordinates"></a>
<a class="token" href="#/s:7heresdk9MilestoneV21mapMatchedCoordinatesAA03GeoE0Vvp">mapMatchedCoordinates</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Map-matched geographic coordinates.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">mapMatchedCoordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geocoordinates">GeoCoordinates</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MilestoneV4typeAA0B4TypeOvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/type"></a>
<a class="token" href="#/s:7heresdk9MilestoneV4typeAA0B4TypeOvp">type</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Type of this Milestone</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">type</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-milestonetype">MilestoneType</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MilestoneV12sectionIndex08waypointD019originalCoordinates010mapMatchedG04typeACs5Int32V_AJSgAA03GeoG0VSgAmA0B4TypeOtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(sectionIndex:waypointIndex:originalCoordinates:mapMatchedCoordinates:type:)"></a>
<a class="token" href="#/s:7heresdk9MilestoneV12sectionIndex08waypointD019originalCoordinates010mapMatchedG04typeACs5Int32V_AJSgAA03GeoG0VSgAmA0B4TypeOtcfc">init(sectionIndex:<wbr/>waypointIndex:<wbr/>originalCoordinates:<wbr/>mapMatchedCoordinates:<wbr/>type:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">sectionIndex</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">,</span> <span class="nv">waypointIndex</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">originalCoordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">mapMatchedCoordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">,</span> <span class="nv">type</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-milestonetype">MilestoneType</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-milestonetype">MilestoneType</a></span><span class="o">.</span><span class="n">stopover</span><span class="p">)</span></code></pre>
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
