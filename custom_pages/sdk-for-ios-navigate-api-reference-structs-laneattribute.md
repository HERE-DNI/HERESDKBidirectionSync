---
title: "MapData / LaneAttribute"
slug: "sdk-for-ios-navigate-api-reference-structs-laneattribute"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/LaneAttribute"></a>
<a title="LaneAttribute Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-mapdata">MapData</a>
<img alt="" id="carat" src="../img/carat.png"/>
        LaneAttribute Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>LaneAttribute</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">LaneAttribute</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>A struct that describes attributes assigned to a specific section of a lane.
It includes lane markings, allowed travel directions, tolling info, access restrictions, and optional lane type.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13LaneAttributeV19startOffsetInMeterss5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/startOffsetInMeters"></a>
<a class="token" href="#/s:7heresdk13LaneAttributeV19startOffsetInMeterss5Int32Vvp">startOffsetInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The start offset of the lane in meters from the beginning of the segment</p>
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
<a name="/s:7heresdk13LaneAttributeV8markingsAA0B8MarkingsVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/markings"></a>
<a class="token" href="#/s:7heresdk13LaneAttributeV8markingsAA0B8MarkingsVvp">markings</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicate the markings on the road</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">markings</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-lanemarkings">LaneMarkings</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13LaneAttributeV6accessAA0B6AccessVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/access"></a>
<a class="token" href="#/s:7heresdk13LaneAttributeV6accessAA0B6AccessVvp">access</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Access characteristics of the lane that identifies the vehicle type(s) allowed to access a lane.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">access</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-laneaccess">LaneAccess</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13LaneAttributeV14tollStructuresSayAA13TollStructureVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/tollStructures"></a>
<a class="token" href="#/s:7heresdk13LaneAttributeV14tollStructuresSayAA13TollStructureVGvp">tollStructures</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of Toll Structure that identifies the presence of physical toll structures or automatic controls on the lane
at entry and exit points along a toll road which requires payment (cash, electronic, etc.) or ticket</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">tollStructures</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-tollstructure">TollStructure</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13LaneAttributeV4typeAA0B4TypeVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/type"></a>
<a class="token" href="#/s:7heresdk13LaneAttributeV4typeAA0B4TypeVSgvp">type</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies the functional and regulatory roles a lane may serve, such as turn, express, HOV, or bike use</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">type</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-lanetype">LaneType</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13LaneAttributeV19startOffsetInMeters8markings6access14tollStructures4typeACs5Int32V_AA0B8MarkingsVAA0B6AccessVSayAA13TollStructureVGAA0B4TypeVSgtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(startOffsetInMeters:markings:access:tollStructures:type:)"></a>
<a class="token" href="#/s:7heresdk13LaneAttributeV19startOffsetInMeters8markings6access14tollStructures4typeACs5Int32V_AA0B8MarkingsVAA0B6AccessVSayAA13TollStructureVGAA0B4TypeVSgtcfc">init(startOffsetInMeters:<wbr/>markings:<wbr/>access:<wbr/>tollStructures:<wbr/>type:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">startOffsetInMeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">,</span> <span class="nv">markings</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-lanemarkings">LaneMarkings</a></span><span class="p">,</span> <span class="nv">access</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-laneaccess">LaneAccess</a></span><span class="p">,</span> <span class="nv">tollStructures</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-tollstructure">TollStructure</a></span><span class="p">],</span> <span class="nv">type</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-lanetype">LaneType</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
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
