---
title: "Navigation / RailwayCrossingWarning"
slug: "sdk-for-ios-navigate-api-reference-structs-railwaycrossingwarning"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/RailwayCrossingWarning"></a>
<a title="RailwayCrossingWarning Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-navigation">Navigation</a>
<img alt="" id="carat" src="../img/carat.png"/>
        RailwayCrossingWarning Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>RailwayCrossingWarning</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RailwayCrossingWarning</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>A struct that provides railway crossing. The main field describing the railway crossing is <code><a href="../Structs/RailwayCrossingWarning.html#/s:7heresdk22RailwayCrossingWarningV4typeAA05RoutebC4TypeOvp">RailwayCrossingWarning.type</a></code> specifying
whether the railway crossing is protected by a barrier or not.
Use <code>RailwayCrossingWarningListener</code> to get notifications about upcoming railway crossings.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22RailwayCrossingWarningV2ids5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/id"></a>
<a class="token" href="#/s:7heresdk22RailwayCrossingWarningV2ids5Int32Vvp">id</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Unique identifier for this specific railway crossing warning instance.
Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace.
Use this ID to track, update, or dismiss individual warning instances of this type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">id</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22RailwayCrossingWarningV010distanceTobC8InMetersSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/distanceToRailwayCrossingInMeters"></a>
<a class="token" href="#/s:7heresdk22RailwayCrossingWarningV010distanceTobC8InMetersSdvp">distanceToRailwayCrossingInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Distance to the railway crossing in meters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">distanceToRailwayCrossingInMeters</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22RailwayCrossingWarningV4typeAA05RoutebC4TypeOvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/type"></a>
<a class="token" href="#/s:7heresdk22RailwayCrossingWarningV4typeAA05RoutebC4TypeOvp">type</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Type of railway crossing, specifying whether it is protected by a barrier or not.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">type</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-routerailwaycrossingtype">RouteRailwayCrossingType</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22RailwayCrossingWarningV12distanceTypeAA08DistanceF0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/distanceType"></a>
<a class="token" href="#/s:7heresdk22RailwayCrossingWarningV12distanceTypeAA08DistanceF0Ovp">distanceType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The distance type for the warning, e.g. a warning for a new railway crossing ahead or a warning
for passing a railway crossing.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">distanceType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-distancetype">DistanceType</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22RailwayCrossingWarningV16segmentReferenceAA07SegmentF0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/segmentReference"></a>
<a class="token" href="#/s:7heresdk22RailwayCrossingWarningV16segmentReferenceAA07SegmentF0Vvp">segmentReference</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The reference to the segment where the railway crossing is located. It can be used to identify the
location.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">segmentReference</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-segmentreference">SegmentReference</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22RailwayCrossingWarningV2id010distanceTobC8InMeters4type0F4Type16segmentReferenceACs5Int32V_SdAA05RoutebcK0OAA08DistanceK0OAA07SegmentM0Vtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(id:distanceToRailwayCrossingInMeters:type:distanceType:segmentReference:)"></a>
<a class="token" href="#/s:7heresdk22RailwayCrossingWarningV2id010distanceTobC8InMeters4type0F4Type16segmentReferenceACs5Int32V_SdAA05RoutebcK0OAA08DistanceK0OAA07SegmentM0Vtcfc">init(id:<wbr/>distanceToRailwayCrossingInMeters:<wbr/>type:<wbr/>distanceType:<wbr/>segmentReference:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">id</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nv">distanceToRailwayCrossingInMeters</span><span class="p">:</span> <span class="kt">Double</span><span class="p">,</span> <span class="nv">type</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-routerailwaycrossingtype">RouteRailwayCrossingType</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-routerailwaycrossingtype">RouteRailwayCrossingType</a></span><span class="o">.</span><span class="n">unknown</span><span class="p">,</span> <span class="nv">distanceType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-distancetype">DistanceType</a></span><span class="p">,</span> <span class="nv">segmentReference</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-segmentreference">SegmentReference</a></span><span class="p">)</span></code></pre>
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
