---
title: "SegmentReference"
slug: "sdk-for-ios-navigate-api-reference-structs-segmentreference"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/SegmentReference"></a>
<a title="SegmentReference Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-routing">Routing</a>

        SegmentReference Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>SegmentReference</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">SegmentReference</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Reference to a segment id with a travel direction.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16SegmentReferenceV9segmentIdSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/segmentId"></a>
<a class="token" href="#/s:7heresdk16SegmentReferenceV9segmentIdSSvp">segmentId</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Topology segment id representing a unique identifier within the HERE platform catalogs.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">segmentId</span><span class="p">:</span> <span class="kt">String</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16SegmentReferenceV15travelDirectionAA06TravelE0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/travelDirection"></a>
<a class="token" href="#/s:7heresdk16SegmentReferenceV15travelDirectionAA06TravelE0Ovp">travelDirection</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Travel direction of the segment.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">travelDirection</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-traveldirection">TravelDirection</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16SegmentReferenceV11offsetStartSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/offsetStart"></a>
<a class="token" href="#/s:7heresdk16SegmentReferenceV11offsetStartSdvp">offsetStart</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The start offset is a non-negative number between 0 and 1, representing the start of the referenced range using a proportion of the length of the segment. 0 represents the start and 1 the end of the segment, relative to the indicated direction (or positive direction in case of undirected segments)</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">offsetStart</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16SegmentReferenceV9offsetEndSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/offsetEnd"></a>
<a class="token" href="#/s:7heresdk16SegmentReferenceV9offsetEndSdvp">offsetEnd</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The end offset is a non-negative number between 0 and 1, representing the end of the referenced range using a proportion of the length of the segment. 0 represents the start and 1 the end of the segment, relative to the indicated direction (or positive direction in case of undirected segments)</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">offsetEnd</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16SegmentReferenceV15tilePartitionIds6UInt32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/tilePartitionId"></a>
<a class="token" href="#/s:7heresdk16SegmentReferenceV15tilePartitionIds6UInt32Vvp">tilePartitionId</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>HERE tile partition id (Morton-encoding + level indicator) of the segment.
As in HERE Map Content.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">tilePartitionId</span><span class="p">:</span> <span class="kt">UInt32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16SegmentReferenceV7localIds6UInt32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/localId"></a>
<a class="token" href="#/s:7heresdk16SegmentReferenceV7localIds6UInt32VSgvp">localId</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Local ID of the segment inside the OCM tile.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">localId</span><span class="p">:</span> <span class="kt">UInt32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16SegmentReferenceV9segmentId15travelDirection11offsetStart0H3End013tilePartitionE005localE0ACSS_AA06TravelG0OS2ds6UInt32VAMSgtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(segmentId:travelDirection:offsetStart:offsetEnd:tilePartitionId:localId:)"></a>
<a class="token" href="#/s:7heresdk16SegmentReferenceV9segmentId15travelDirection11offsetStart0H3End013tilePartitionE005localE0ACSS_AA06TravelG0OS2ds6UInt32VAMSgtcfc">init(segmentId:<wbr/>travelDirection:<wbr/>offsetStart:<wbr/>offsetEnd:<wbr/>tilePartitionId:<wbr/>localId:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">segmentId</span><span class="p">:</span> <span class="kt">String</span> <span class="o">=</span> <span class="s">""</span><span class="p">,</span> <span class="nv">travelDirection</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-traveldirection">TravelDirection</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-traveldirection">TravelDirection</a></span><span class="o">.</span><span class="n">bidirectional</span><span class="p">,</span> <span class="nv">offsetStart</span><span class="p">:</span> <span class="kt">Double</span> <span class="o">=</span> <span class="mf">0.0</span><span class="p">,</span> <span class="nv">offsetEnd</span><span class="p">:</span> <span class="kt">Double</span> <span class="o">=</span> <span class="mf">1.0</span><span class="p">,</span> <span class="nv">tilePartitionId</span><span class="p">:</span> <span class="kt">UInt32</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nv">localId</span><span class="p">:</span> <span class="kt">UInt32</span><span class="p">?</span> <span class="o">=</span> <span class="mi">0</span><span class="p">)</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16SegmentReferenceV10fromString10segmentRefACSgSS_tFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/fromString(segmentRef:)"></a>
<a class="token" href="#/s:7heresdk16SegmentReferenceV10fromString10segmentRefACSgSS_tFZ">fromString(segmentRef:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Returns an instance of this struct from a string if it’s well-formatted, <code>nil</code> otherwise.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">fromString</span><span class="p">(</span><span class="nv">segmentRef</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">SegmentReference</span><span class="p">?</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>segmentRef</em>
</code>
</td>
<td>
<div>
<p>The string to parse</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>An instance of <code>SegmentReference</code> from a string if it’s well-formatted, <code>nil</code> otherwise.</p>
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
