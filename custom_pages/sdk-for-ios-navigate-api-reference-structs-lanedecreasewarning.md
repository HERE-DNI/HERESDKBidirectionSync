---
title: "Other Structures / LaneDecreaseWarning"
slug: "sdk-for-ios-navigate-api-reference-structs-lanedecreasewarning"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/LaneDecreaseWarning"></a>
<a title="LaneDecreaseWarning Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-other%20structs">Other Structures</a>
<img alt="" id="carat" src="../img/carat.png"/>
        LaneDecreaseWarning Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>LaneDecreaseWarning</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">LaneDecreaseWarning</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Represents a lane decrease warning that notifies about upcoming reductions in the number of available lanes.</p>
<p>Lane decrease warnings are generated when the road ahead has fewer lanes
than the previous road segment provided by <code>sdk.electronic_horizon.ElectronicHorizonEngine</code>,
requiring drivers to merge or change lanes.
Lane decrease is provided only on highways and motorways. It will not be provided for junctions,
when maneuver is given for the lane decrease situation or when the <code><a href="sdk-for-ios-navigate-api-reference-..-structs-trafficmergewarning">TrafficMergeWarning</a></code>
is provided. Special lanes (e.g. Bus lane, HOV) will only be included to the lane decrease warning generation
if the according options are set in <code><a href="sdk-for-ios-navigate-api-reference-..-structs-transportspecification">TransportSpecification</a></code>.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19LaneDecreaseWarningV2ids5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/id"></a>
<a class="token" href="#/s:7heresdk19LaneDecreaseWarningV2ids5Int32Vvp">id</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Unique identifier for this lane decrease warning instance.
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
<a name="/s:7heresdk19LaneDecreaseWarningV08previousB6Numbers5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/previousLaneNumber"></a>
<a class="token" href="#/s:7heresdk19LaneDecreaseWarningV08previousB6Numbers5Int32Vvp">previousLaneNumber</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Number of lanes before the lane decrease event.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">previousLaneNumber</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19LaneDecreaseWarningV03newB6Numbers5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/newLaneNumber"></a>
<a class="token" href="#/s:7heresdk19LaneDecreaseWarningV03newB6Numbers5Int32Vvp">newLaneNumber</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Number of lanes after the lane decrease event.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">newLaneNumber</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19LaneDecreaseWarningV22lanesDecreasedFromLefts5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/lanesDecreasedFromLeft"></a>
<a class="token" href="#/s:7heresdk19LaneDecreaseWarningV22lanesDecreasedFromLefts5Int32VSgvp">lanesDecreasedFromLeft</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Number of lanes decreased on the left side of the road,
<code>nil</code> if the left-side change is unknown or not applicable.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">lanesDecreasedFromLeft</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19LaneDecreaseWarningV23lanesDecreasedFromRights5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/lanesDecreasedFromRight"></a>
<a class="token" href="#/s:7heresdk19LaneDecreaseWarningV23lanesDecreasedFromRights5Int32VSgvp">lanesDecreasedFromRight</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Number of lanes decreased on the right side of the road,
<code>nil</code> if the right-side change is unknown or not applicable.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">lanesDecreasedFromRight</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19LaneDecreaseWarningV16distanceInMetersSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/distanceInMeters"></a>
<a class="token" href="#/s:7heresdk19LaneDecreaseWarningV16distanceInMetersSdvp">distanceInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The distance from the current location to the Lane decrease event.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">distanceInMeters</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19LaneDecreaseWarningV12distanceTypeAA08DistanceF0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/distanceType"></a>
<a class="token" href="#/s:7heresdk19LaneDecreaseWarningV12distanceTypeAA08DistanceF0Ovp">distanceType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates if the specified event is ahead of the vehicle or has just passed by. If it is
ahead, then <code><a href="../Structs/LaneDecreaseWarning.html#/s:7heresdk19LaneDecreaseWarningV16distanceInMetersSdvp">LaneDecreaseWarning.distanceInMeters</a></code> is greater than 0.</p>
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
<a name="/s:7heresdk19LaneDecreaseWarningV2id08previousB6Number03newbG022lanesDecreasedFromLeft0ijK5Right16distanceInMeters0N4TypeACs5Int32V_A3LSgAMSdAA08DistanceQ0Otcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(id:previousLaneNumber:newLaneNumber:lanesDecreasedFromLeft:lanesDecreasedFromRight:distanceInMeters:distanceType:)"></a>
<a class="token" href="#/s:7heresdk19LaneDecreaseWarningV2id08previousB6Number03newbG022lanesDecreasedFromLeft0ijK5Right16distanceInMeters0N4TypeACs5Int32V_A3LSgAMSdAA08DistanceQ0Otcfc">init(id:<wbr/>previousLaneNumber:<wbr/>newLaneNumber:<wbr/>lanesDecreasedFromLeft:<wbr/>lanesDecreasedFromRight:<wbr/>distanceInMeters:<wbr/>distanceType:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">id</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nv">previousLaneNumber</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nv">newLaneNumber</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nv">lanesDecreasedFromLeft</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">lanesDecreasedFromRight</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">distanceInMeters</span><span class="p">:</span> <span class="kt">Double</span><span class="p">,</span> <span class="nv">distanceType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-distancetype">DistanceType</a></span><span class="p">)</span></code></pre>
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
