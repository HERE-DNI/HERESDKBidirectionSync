---
title: "SegmentReference Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-segmentreference"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- SegmentReference.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/SegmentReference"></a>
<a title="SegmentReference Structure Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="../index.html">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="../index.html">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="../Routing.html">Routing</a>
<img alt="" id="carat" src="../img/carat.png"/>
        SegmentReference Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct SegmentReference : Hashable</code></pre>
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
<pre><code>public var segmentId: String</code></pre>
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
<pre><code>public var travelDirection: TravelDirection</code></pre>
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
<pre><code>public var offsetStart: Double</code></pre>
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
<pre><code>public var offsetEnd: Double</code></pre>
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
<pre><code>public var tilePartitionId: UInt32</code></pre>
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
<pre><code>public var localId: UInt32?</code></pre>
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
<pre><code>public init(segmentId: String = "", travelDirection: TravelDirection = TravelDirection.bidirectional, offsetStart: Double = 0.0, offsetEnd: Double = 1.0, tilePartitionId: UInt32 = 0, localId: UInt32? = 0)</code></pre>
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
<pre><code>public static func fromString(segmentRef: String) -&gt; SegmentReference?</code></pre>
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



</div>
`
}</HTMLBlock>
