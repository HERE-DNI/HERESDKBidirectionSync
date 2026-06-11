---
title: "sdk-for-ios-navigate-api-reference-structs-trafficmergewarning"
slug: "sdk-for-ios-navigate-api-reference-structs-trafficmergewarning"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TrafficMergeWarning"></a>
<a title="TrafficMergeWarning Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-navigation">Navigation</a>
<img alt="" id="carat" src="/carat.png"/>
        TrafficMergeWarning Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>TrafficMergeWarning</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TrafficMergeWarning</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>A struct that provides warning for merging traffic. The main field describing the merging traffic is <code>TrafficMergeWarning.road_type</code>
specifying the type of road containing traffic which is merging with the current road.
Use <code>TrafficMergeWarningListener</code> to get notifications about upcoming merging traffic.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19TrafficMergeWarningV2ids5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/id"></a>
<a class="token" href="#/s:7heresdk19TrafficMergeWarningV2ids5Int32Vvp">id</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Unique identifier for this specific traffic merge warning instance.
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
<a name="/s:7heresdk19TrafficMergeWarningV010distanceTobC8InMetersSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/distanceToTrafficMergeInMeters"></a>
<a class="token" href="#/s:7heresdk19TrafficMergeWarningV010distanceTobC8InMetersSdvp">distanceToTrafficMergeInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Distance to merging traffic in meters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">distanceToTrafficMergeInMeters</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19TrafficMergeWarningV8roadTypeAA0bc4RoadF0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/roadType"></a>
<a class="token" href="#/s:7heresdk19TrafficMergeWarningV8roadTypeAA0bc4RoadF0Ovp">roadType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Type of road which contains the merging traffic.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">roadType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-trafficmergeroadtype">TrafficMergeRoadType</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19TrafficMergeWarningV4sideAA0bC4SideOvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/side"></a>
<a class="token" href="#/s:7heresdk19TrafficMergeWarningV4sideAA0bC4SideOvp">side</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The side from which the traffic is merging.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">side</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-trafficmergeside">TrafficMergeSide</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19TrafficMergeWarningV9laneCounts5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/laneCount"></a>
<a class="token" href="#/s:7heresdk19TrafficMergeWarningV9laneCounts5Int32Vvp">laneCount</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Number of lanes of the merging road containing the traffic. If the road has no lanes defined, than the
number of lanes returned will be 1.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">laneCount</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19TrafficMergeWarningV12distanceTypeAA08DistanceF0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/distanceType"></a>
<a class="token" href="#/s:7heresdk19TrafficMergeWarningV12distanceTypeAA08DistanceF0Ovp">distanceType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The distance type for the warning, e.g. a warning for a new traffic merge location ahead or a warning for
passing a traffic merge location. Since the traffic merge warning is given relative to a single position on
the route, <code>DistanceType.REACHED</code> will never be given for this warning.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">distanceType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-distancetype">DistanceType</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19TrafficMergeWarningV2id010distanceTobC8InMeters8roadType4side9laneCount0fK0ACs5Int32V_SdAA0bc4RoadK0OAA0bC4SideOAkA08DistanceK0Otcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(id:distanceToTrafficMergeInMeters:roadType:side:laneCount:distanceType:)"></a>
<a class="token" href="#/s:7heresdk19TrafficMergeWarningV2id010distanceTobC8InMeters8roadType4side9laneCount0fK0ACs5Int32V_SdAA0bc4RoadK0OAA0bC4SideOAkA08DistanceK0Otcfc">init(id:<wbr/>distanceToTrafficMergeInMeters:<wbr/>roadType:<wbr/>side:<wbr/>laneCount:<wbr/>distanceType:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">id</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nv">distanceToTrafficMergeInMeters</span><span class="p">:</span> <span class="kt">Double</span><span class="p">,</span> <span class="nv">roadType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-trafficmergeroadtype">TrafficMergeRoadType</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-trafficmergeroadtype">TrafficMergeRoadType</a></span><span class="o">.</span><span class="n">sliproad</span><span class="p">,</span> <span class="nv">side</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-trafficmergeside">TrafficMergeSide</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-trafficmergeside">TrafficMergeSide</a></span><span class="o">.</span><span class="n">right</span><span class="p">,</span> <span class="nv">laneCount</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span> <span class="nv">distanceType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-distancetype">DistanceType</a></span><span class="p">)</span></code></pre>
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
