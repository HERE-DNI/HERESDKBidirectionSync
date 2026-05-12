---
title: "MaxSpeedOnSegment Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-maxspeedonsegment"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- MaxSpeedOnSegment.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/MaxSpeedOnSegment"></a>
<a title="MaxSpeedOnSegment Structure Reference"></a>
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
        MaxSpeedOnSegment Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct MaxSpeedOnSegment : Hashable</code></pre>
</div>
</div>
<p>New base speed for a segment. Affects route calculation and the ETA. Cannot increase base speed on segment.</p>
<p><strong>Note:</strong> This option can only be used with the <code><a href="../Classes/RoutingEngine.html">RoutingEngine</a></code>. The <code>OfflineRoutingEngine</code> is not supported and the option will be ignored. Note that the <code>OfflineRoutingEngine</code> is only available for the Navigate license.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17MaxSpeedOnSegmentV7segmentAA0E9ReferenceVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/segment"></a>
<a class="token" href="#/s:7heresdk17MaxSpeedOnSegmentV7segmentAA0E9ReferenceVvp">segment</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A segment for which the new base speed is specified. Only the <code>segmendId</code> and <code>travelDirection</code>
parameters are used, other parameters are ignored. Setting a <code>segmendId</code> is mandatory.</p>
<p><strong>Note:</strong> The <code><a href="../Structs/SegmentReference.html">SegmentReference</a></code> is not directly accessible from the map via the HERE SDK.
Although, after route calculation you can retrieve the related segments for each <code><a href="../Classes/Span.html">Span</a></code>.
The segment IDs are the same that are also used by, for example, the <a href="https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/topics/use-cases/avoid-segments.html">Routing REST API</a>.
These IDs are mostly stable and only change when the underlying map data changes
due to a new road or similar changes in the real world.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var segment: SegmentReference</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17MaxSpeedOnSegmentV04baseC17InMetersPerSecondSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/baseSpeedInMetersPerSecond"></a>
<a class="token" href="#/s:7heresdk17MaxSpeedOnSegmentV04baseC17InMetersPerSecondSdvp">baseSpeedInMetersPerSecond</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>New maximum value in m/s of baseSpeed on segment.  The provided value must be in the range [1.0, 70.0].
Cannot increase base speed on segment. If the value is greater than the default base speed, then such penalty will have no effect.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var baseSpeedInMetersPerSecond: Double</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17MaxSpeedOnSegmentV7segment04baseC17InMetersPerSecondAcA0E9ReferenceV_Sdtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(segment:baseSpeedInMetersPerSecond:)"></a>
<a class="token" href="#/s:7heresdk17MaxSpeedOnSegmentV7segment04baseC17InMetersPerSecondAcA0E9ReferenceV_Sdtcfc">init(segment:<wbr/>baseSpeedInMetersPerSecond:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance.</p>
<ul>
<li><p>Parameters</p>
<ul>
<li>segment: A segment for which the new base speed is specified. Only the <code>segmendId</code> and <code>travelDirection</code>
parameters are used, other parameters are ignored. Setting a <code>segmendId</code> is mandatory.</li>
</ul>
<p><strong>Note:</strong> The <code><a href="../Structs/SegmentReference.html">SegmentReference</a></code> is not directly accessible from the map via the HERE SDK.
  Although, after route calculation you can retrieve the related segments for each <code><a href="../Classes/Span.html">Span</a></code>.
  The segment IDs are the same that are also used by, for example, the <a href="https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/topics/use-cases/avoid-segments.html">Routing REST API</a>.
  These IDs are mostly stable and only change when the underlying map data changes
  due to a new road or similar changes in the real world.</p>
<ul>
<li>baseSpeedInMetersPerSecond: New maximum value in m/s of baseSpeed on segment.  The provided value must be in the range [1.0, 70.0].
Cannot increase base speed on segment. If the value is greater than the default base speed, then such penalty will have no effect.</li>
</ul></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public init(segment: SegmentReference, baseSpeedInMetersPerSecond: Double)</code></pre>
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



</div>
`
}</HTMLBlock>
