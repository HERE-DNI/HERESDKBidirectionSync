---
title: "TollStructureManeuver"
slug: "sdk-for-ios-navigate-api-reference-structs-tollstructuremaneuver"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TollStructureManeuver"></a>
<a title="TollStructureManeuver Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-mapdata">MapData</a>

        TollStructureManeuver Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>TollStructureManeuver</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TollStructureManeuver</span></code></pre>
</div>
</div>
<p>A struct that provides information for a toll structure at a toll point.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21TollStructureManeuverV04tollC0AA0bC0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/tollStructure"></a>
<a class="token" href="#/s:7heresdk21TollStructureManeuverV04tollC0AA0bC0VSgvp">tollStructure</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Toll structure properties
Could be empty for checkpoint not related to toll.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">tollStructure</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-tollstructure">TollStructure</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21TollStructureManeuverV12isCheckpointSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isCheckpoint"></a>
<a class="token" href="#/s:7heresdk21TollStructureManeuverV12isCheckpointSbvp">isCheckpoint</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Vehicle Checkpoint identifies locations on the through route, where vehicles
are required to slow down/stop with the intended purpose of inspecting vehicles to deter illegal immigration
and smuggling activities, to perform customs/passport checks, toll payment, etc. This is not limited to border locations.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isCheckpoint</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21TollStructureManeuverV12destinationsSayAA20DirectedOCMSegmentIdVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/destinations"></a>
<a class="token" href="#/s:7heresdk21TollStructureManeuverV12destinationsSayAA20DirectedOCMSegmentIdVGvp">destinations</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Optional destinations segment references.
Destination shows for which exactly outgoing segment current toll/checkpoint is applied.
Empty if structure applied to all outgoing connected segments.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">destinations</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-directedocmsegmentid">DirectedOCMSegmentId</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21TollStructureManeuverV15etcGuidanceFileAA0G9ReferenceVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/etcGuidanceFile"></a>
<a class="token" href="#/s:7heresdk21TollStructureManeuverV15etcGuidanceFileAA0G9ReferenceVSgvp">etcGuidanceFile</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Optional image providing guidance through an electronic toll collection (ETC) point.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">etcGuidanceFile</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-filereference">FileReference</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21TollStructureManeuverV04tollC012isCheckpoint12destinations15etcGuidanceFileAcA0bC0VSg_SbSayAA20DirectedOCMSegmentIdVGAA0K9ReferenceVSgtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(tollStructure:isCheckpoint:destinations:etcGuidanceFile:)"></a>
<a class="token" href="#/s:7heresdk21TollStructureManeuverV04tollC012isCheckpoint12destinations15etcGuidanceFileAcA0bC0VSg_SbSayAA20DirectedOCMSegmentIdVGAA0K9ReferenceVSgtcfc">init(tollStructure:<wbr/>isCheckpoint:<wbr/>destinations:<wbr/>etcGuidanceFile:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">tollStructure</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-tollstructure">TollStructure</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">isCheckpoint</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">destinations</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-directedocmsegmentid">DirectedOCMSegmentId</a></span><span class="p">],</span> <span class="nv">etcGuidanceFile</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-filereference">FileReference</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
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
